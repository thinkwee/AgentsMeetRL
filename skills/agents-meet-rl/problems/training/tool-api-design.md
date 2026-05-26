# Question: how to design the tool / env layer for RL

## Why this is its own topic

The tool layer is a research surface most papers underplay. A poorly
designed tool API:

- Eats 30%+ of rollout compute on retries / parse failures.
- Makes credit assignment ambiguous (was the bad answer the agent's
  fault or the tool's?).
- Causes silent training divergence when the tool changes between
  versions.
- Gives the model implicit incentives to game the tool layer rather
  than solve the task.

Most of `env-flakiness.md`, `tool-call-parse-failures.md`,
`observation-truncation.md` are downstream symptoms of bad tool design.
This file is the **design principles** view.

## Design principles

### Principle 1: tool errors must be readable, not silent

The model needs to learn to recover from tool errors. Silent zero-
reward = no learning signal. Explicit error message = the rollout
gets another chance and the optimizer learns the recovery pattern.

```python
# BAD
try:
    result = tool.call(args)
except Exception:
    return ""           # silent — model can't tell what happened

# GOOD
try:
    result = tool.call(args)
except RateLimitError as e:
    return f"<error type='rate_limit'>API rate limit hit. Retry in {e.retry_after}s.</error>"
except ParseError as e:
    return f"<error type='parse'>{e.message}. Expected format: {e.expected}</error>"
except TimeoutError:
    return f"<error type='timeout'>Tool took >{TIMEOUT}s. Try a smaller query.</error>"
```

The model can read this; subsequent turn can adapt.

### Principle 2: deterministic outputs where possible

Two rollouts of the "same" call should return the same result. Sources
of non-determinism:

- Live API (network, server state).
- Database with concurrent writes.
- Random sampling in the tool itself.

Make tools **content-addressed and cached**:

```python
@cached(key=lambda args: hash(args))
def search(query: str) -> str:
    ...
```

Cache hits = exact reproduction. Cache misses = first call result is
recorded for future replay.

This is what Search-R1 does for retrieval (cached Wikipedia/E5 index)
and ZeroSearch does for the entire engine (simulated).

### Principle 3: bound output size at the tool layer, not agent layer

Don't ship 100KB of HTML to the agent and expect it to truncate. The
agent forgets / loses signal. Truncate at the tool:

```python
def search(query):
    results = engine.query(query, top_k=5)
    return [
        {"title": r.title, "snippet": r.snippet[:500]}
        for r in results
    ]
```

Make the contract explicit: the tool returns at most N tokens of
content per call.

### Principle 4: separate "tool failed" from "tool succeeded but answer is bad"

These are distinct learning signals:

| Tool result | Reward signal | What model should learn |
|---|---|---|
| Tool failed (network, parse) | Don't penalize hard | Retry, format better |
| Tool ran, returned wrong | Penalize | Choose better tool / args |
| Tool ran, returned right | Reward | Reinforce |

If you collapse all of these into "outcome = 0", the model learns
something but slowly and confused.

### Principle 5: action-budget cap

Cap consecutive tool calls per rollout (e.g., 30). Not a soft penalty
— a hard termination. Otherwise pathological rollouts burn compute.

```python
if rollout.tool_calls >= MAX_TOOL_CALLS:
    return done(reason="action_budget_exhausted", reward=0)
```

### Principle 6: format consistency between SFT and RL

The single biggest silent killer. SFT trajectories using
`<search>...</search>`, RL parser expecting
`<tool_call name="search">{...}</tool_call>` → the model effectively
restarts. Pick one format and use it everywhere:

- SFT data.
- Eval prompts.
- Training prompts.
- Tool parser.
- Documentation.

If you must change format mid-project, run a fresh SFT pass on the new
format before resuming RL.

## Architectural patterns

### Pattern A: in-trainer tool execution

The trainer process calls the tool directly. Simplest; works for fast,
deterministic tools (cached retrieval, math eval, JSON parsing).

```python
def rollout_step(prompt, model):
    response = model.generate(prompt)
    tool_call = parse(response)
    if tool_call:
        result = execute_tool(tool_call)
        return prompt + response + format_tool_response(result)
```

Trade-off: slow tools (Docker, real APIs) block the trainer. Use
Pattern B.

### Pattern B: separate tool-server process

Tools run in a dedicated server / container; trainer communicates
over IPC or HTTP.

```
Trainer  ──HTTP──>  Tool-server  ──>  Docker / API / DB
                          │
                          └─> caching, retries, rate-limit, isolation
```

Used by SWE agents (SWE-Gym, SWE-Swiss), GUI agents (sandbox-based),
and most production-scale agentic RL.

### Pattern C: tool-as-env (gym-style)

Wrap tools as a Gym environment with `step(action) → obs, reward,
done`. Cleanest abstraction; integrates with any RL framework.

```python
class SearchEnv(gym.Env):
    def reset(self):
        self.history = []
        return self._make_observation()

    def step(self, action):
        result = execute_tool(action)
        self.history.append((action, result))
        obs = self._make_observation()
        reward = self._compute_reward()
        done = self._is_done()
        return obs, reward, done, {}
```

Used by verl-tool, SkyRL-Gym, AReaL.

> **verl-tool** — github: `https://github.com/TIGER-AI-Lab/verl-tool`,
> TIGER-Lab, date: 2025.6. Why: Robust action loop with structured
> tool execution; lenient parsing with explicit error feedback.

> **SkyRL** — github: `https://github.com/NovaSky-AI/SkyRL`,
> paper: `https://arxiv.org/abs/2511.16108`, NovaSky-AI,
> date: 2025.11. Why: split into `skyrl-gym` for environments,
> `skyrl-agent` for agent loop — clean separation.

## Tool-call format choices

### Custom XML (`<search>...</search>`)

Pros: simple; readable; matches early agent papers.

Cons: tokenizer may split tags; brittle to whitespace; no type
checking on args.

Used by: Search-R1, R1-Searcher, RAGEN.

### Function-calling (model-native JSON)

Pros: more constrained; tokenizer respects the format; supported by
inference engines (vLLM tool-calling mode).

Cons: heavier output; some models don't have function-calling SFT.

```json
{"name": "search", "arguments": {"query": "agentic RL"}}
```

Used by: Tool-N1, ReTool (Python interpreter), UI-TARS.

### MCP (Model Context Protocol)

Pros: standardized across tools; ecosystem support.

Cons: newer; tooling stability varies; debugging across MCP boundaries
is harder.

Used by: MCP-Bench, MCP-Universe.

> **MCP-Bench** — github: `https://github.com/Accenture/mcp-bench`,
> paper: `https://arxiv.org/abs/2508.20453`, Accenture, date: 2025.8.
> Why: 28 MCP servers; reference for MCP-style training infra.

> **UI-TARS** — github: `https://github.com/bytedance/UI-TARS`,
> paper: `https://arxiv.org/abs/2509.02544`, ByteDance Seed,
> date: 2025.1. Why: ships `ui_tars.action_parser` as a separate,
> well-tested library; reference for robust action parsing.

## Tool-quality signals to log

For every rollout, log:

- `tool_calls_total`: how many times any tool was called.
- `tool_calls_per_type`: breakdown by tool name.
- `tool_parse_failures`: how many parses failed.
- `tool_runtime_failures`: how many runtimes raised.
- `tool_p95_latency`: tail latency.
- `tool_output_p95_size`: tail output size.
- `tool_cache_hit_rate`: caching effectiveness.

This data tells you whether the tool layer is the bottleneck and which
tools to invest in.

## Common bugs

### Bug 1: tool returns success on bad input

```python
def search(query):
    return engine.query(query)  # returns "" on bad query
```

`""` parses as "no results" not as "bad query." Model can't learn the
distinction. Fix: validate input, raise on bad input.

### Bug 2: tool output contains literal answer

If a search tool returns the gold answer verbatim in a passage, the
agent learns to echo. See `search-hacking.md`.

### Bug 3: tool latency variance > 100×

p50 = 0.1s, p99 = 30s. Without per-call timeout, one bad call stalls
the whole rollout. Set timeouts; treat timeouts as readable errors.

### Bug 4: shared tool state between rollouts

Two parallel rollouts hit the same DB / port / file. State pollutes.
Use per-rollout containers or thread-local state.

### Bug 5: tool-call format drift between SFT and RL

The most common silent killer. SFT used one syntax, RL parser expects
another. KL is 0 at init but reward never moves. See
`sft-to-rl-transition.md`.

## Test-driven tool design

Before training:

1. Build a small test set of 20 (input, expected_output) tool-call
   pairs.
2. Run the parser on each. Assert every passes.
3. Build 10 known-bad inputs. Assert parser fails predictably.

```python
test_cases = [
    ('<search>foo</search>',
     {'tool': 'search', 'args': {'query': 'foo'}}),
    ('  <search>  foo  </search>  ',     # whitespace-tolerant
     {'tool': 'search', 'args': {'query': 'foo'}}),
    ('<answer>42</answer>',               # not a tool call
     None),
]
for raw, expected in test_cases:
    assert parse_tool_call(raw) == expected
```

Run before each training session. Catches drift introduced by tokenizer
or template changes.

## Paper / repo references

> **verl-tool** — github: `https://github.com/TIGER-AI-Lab/verl-tool`,
> TIGER-Lab, date: 2025.6. Why: structured tool execution + explicit
> error feedback as first-class.

> **UI-TARS** — github: `https://github.com/bytedance/UI-TARS`,
> paper: `https://arxiv.org/abs/2509.02544`, ByteDance Seed,
> date: 2025.1. Why: robust action parser library.

> **Agent-R1** — github: `https://github.com/0russwest0/Agent-R1`,
> paper: `https://arxiv.org/abs/2511.14460`, USTC, date: 2025.11.
> Why: step-level MDP keeps parse logic in env layer, not trainer.

> **Search-R1** — github: `https://github.com/PeterGriffinJin/Search-R1`,
> paper: `https://arxiv.org/abs/2503.09516`, UIUC, date: 2025.3.
> Why: cached Wikipedia/E5 retrieval as a deterministic tool;
> reference for cache-based reproducibility.

> **ZeroSearch** — github: `https://github.com/Alibaba-NLP/ZeroSearch`,
> paper: `https://arxiv.org/abs/2505.04588`, Alibaba, date: 2025.5.
> Why: simulates the search engine entirely; full determinism, full
> control of noise.

> **SWE-Gym** — github: `https://github.com/SWE-Gym/SWE-Gym`,
> paper: `https://arxiv.org/abs/2412.21139`, UC Berkeley/UIUC/CMU/Apple,
> date: 2024.12. Why: per-task Docker isolation; reference for
> production-grade sandbox design.

> **SkyRL** — see above.

> **MCP-Bench** — see above.

**Other corpus entries:**

- `MATPO` — multi-agent GRPO for tool-use/search.
  github: `https://github.com/mzf666/MATPO`, paper: `https://arxiv.org/abs/2510.04678`, MiroMind AI, date: 2025.10

- `MiroRL` — GRPO for reasoning/planning/tool-use with rule-based reward.
  github: `https://github.com/MiroMindAI/MiroRL`, paper: `https://huggingface.co/miromind-ai`, MiroMindAI, date: 2025.8

- `Multi-Turn-RL-Agent` — GRPO multi-turn tool-use with rule/external reward.
  github: `https://github.com/SiliangZeng/Multi-Turn-RL-Agent`, paper: `https://arxiv.org/abs/2505.11821`, University of Minnesota, date: 2025.5

- `RL-Factory` — GRPO across tool-use and NL2SQL.
  github: `https://github.com/Simple-Efficient/RL-Factory`, paper: `https://huggingface.co/Simple-Efficient/RLFactory-Qwen3-8B-GRPO`, Simple-Efficient, date: 2025.5

- `AWorld` — GRPO across search/web/code.
  github: `https://github.com/inclusionAI/AWorld`, paper: `https://arxiv.org/abs/2508.20404`, Ant Group (inclusionAI), date: 2025.8

- `ReCall` — compares PPO/GRPO/RLOO/REINFORCE++/ReMax for tool-use.
  github: `https://github.com/Agent-RL/ReCall`, paper: `https://arxiv.org/abs/2503.19470`, BaiChuan, date: 2025.3

- `ToolRL` — GRPO/PPO for general tool learning.
  github: `https://github.com/qiancheng0/ToolRL`, paper: `https://arxiv.org/abs/2504.13958`, UIUC, date: 2025.4

- `ToolBrain` — GRPO/DPO for agentic tool training.
  github: `https://github.com/ToolBrain/ToolBrain`, paper: `https://arxiv.org/abs/2510.00023`, ToolBrain (AAMAS 2026), date: 2025.10

- `Tool-R1` — policy optimization for agentic tool-use on GAIA.
  github: `https://github.com/YBYBZhang/Tool-R1`, paper: `https://arxiv.org/abs/2509.12867`, Individual (YBYBZhang), date: 2025.9

## See also

- `env-flakiness.md` — runtime failure modes.
- `tool-call-parse-failures.md` — parser-level pitfalls.
- `observation-truncation.md` — output bounding.
- `search-hacking.md` — adversarial use of tool outputs.
- `code-swe-specific.md` — sandbox-specific concerns.
