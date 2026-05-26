# Problem: high tool-call parse failure rate during rollout

## Symptoms

- Many rollouts get 0 reward not because the answer was wrong but
  because the tool-call action was malformed.
- Train logs show high `parse_failure_rate` (or you don't log it — also
  bad).
- Model emits `<search>foo</search>` but parser expects
  `<tool_call name="search">{"q": "foo"}</tool_call>`, or vice versa.
- Sometimes works on training cases, breaks on prompts where the model
  generates a slightly different format.

## Root causes

1. **Strict regex/parser, lenient model.** The parser only accepts one
   exact format; the model can emit superset variants.
2. **Mismatch between SFT-time format and RL-time format.** The cold
   start used one syntax (e.g. natural language), RL expects another
   (e.g. JSON tool call).
3. **Reward signal doesn't punish parse failure consistently.** Either
   silently scored as 0 (no feedback) or scored as -1 indistinguishable
   from "tool returned nothing useful."
4. **Multiple tool-call variants** in training data, so the model
   ambiguously interpolates them.

## Diagnosis

- **Log parse-failure rate every step.** Not optional. If it's > 1%, it
  matters; if it's > 10%, it's the dominant failure mode.
- Sample 20 parse failures. Categorize by failure type: missing closing
  tag? wrong tag name? non-JSON args? extra whitespace? Each implies a
  different fix.
- Check the *parse* code path itself — silent failures (returning empty
  result) are worse than loud ones (returning explicit "ERROR").

## Fixes

### Fix 1: SFT cold-start with the exact RL format

The simplest fix: SFT must produce trajectories in the RL parser's
exact format. Most projects in the corpus do this:

> **Search-R1** —
> github: `https://github.com/PeterGriffinJin/Search-R1`,
> paper: `https://arxiv.org/abs/2503.09516`, UIUC/Google, date: 2025.3.
> Strict `<search>...</search>` and `<answer>...</answer>` template
> shared between SFT and RL — the simplest way to guarantee the parser
> sees what the model emits.

> **ReTool** — github: `https://github.com/ReTool-RL/ReTool`,
> paper: `https://arxiv.org/abs/2504.11536`, ByteDance, date: 2025.4.
> Code interpreter format consistent across SFT and RL.

> **Tool-Star** — github: `https://github.com/dongguanting/Tool-Star`,
> paper: `https://arxiv.org/abs/2505.16410`, RUC, date: 2025.5.
> Multi-stage SFT with the RL-format intact.

### Fix 2: lenient parser with explicit error feedback

Make the parser tolerant (whitespace, attribute order, optional fields)
*and* return an explicit error message that the model can read on the
next turn:

> **verl-tool** — github: `https://github.com/TIGER-AI-Lab/verl-tool`,
> TIGER-Lab, date: 2025.6. Robust action loop with structured tool
> execution; lenient parsing with explicit error feedback baked in.

> **Agent-R1's Step-level MDP** — github:
> `https://github.com/0russwest0/Agent-R1`, paper:
> `https://arxiv.org/abs/2511.14460`, USTC. Action parsing lives in the
> env layer, not the trainer; parse failure becomes an observable env
> response (an error string the model can read on the next turn) rather
> than a silent zero reward.

### Fix 3: punish parse failure explicitly

Don't silently zero out parse failures. Either:

- Reward = -ε (small negative) for parse failure, so the model learns
  to fix format.
- Reward = 0 but the env *responds* with an error string the model can
  read; effectively the rollout gets another chance.

### Fix 4: function-calling format (not custom XML)

If you control the format, use the model's native function-calling
schema (Qwen, Llama, GPT format). The tokenizer / chat template is more
likely to keep it intact. Custom XML tags drift more.

> **UI-TARS** —
> github: `https://github.com/bytedance/UI-TARS`,
> paper: `https://arxiv.org/abs/2509.02544`, ByteDance Seed, date: 2025.1.
> Ships `ui_tars.action_parser` as a separate library, action parser is
> robust, well-tested.

### Fix 5: assert on a parser test set before training

Build a unit test of 20 example outputs: 10 well-formed (must parse
cleanly) + 10 known-bad (must fail predictably). Run before each
training session.

```python
# pseudo
for example, expected in test_cases:
    result = parser.parse(example)
    assert (result.success, result.error_type) == expected
```

### Fix 6: action-budget on parse failures

Cap consecutive parse failures per rollout (e.g. 3). Otherwise rollouts
hit max_turns burning compute on unparseable outputs.

## Reference parser implementations

| Project | Why useful |
|---|---|
| **UI-TARS** (`ui_tars.action_parser`) | Standalone, well-tested action parser library |
| **verl-tool** | Tool execution loop with explicit env feedback |
| **Agent-R1** | Step-level MDP keeps parse logic in env layer |
| **Search-R1** | Search-tag parser pattern reused across many forks |

## Paper / repo references

- `Search-R1` — github: `https://github.com/PeterGriffinJin/Search-R1`,
  papers: `https://arxiv.org/abs/2503.09516`,
  `https://arxiv.org/abs/2505.15117`, UIUC/Google, date: 2025.3.
- `ReTool` — github: `https://github.com/ReTool-RL/ReTool`,
  paper: `https://arxiv.org/abs/2504.11536`, ByteDance, date: 2025.4.
- `Tool-N1` — github: `https://github.com/NVlabs/Tool-N1`,
  paper: `https://arxiv.org/abs/2505.00024`, NVIDIA, date: 2025.5.
- `ToolMaster` — github: `https://github.com/NEUIR/ToolMaster`,
  paper: `https://arxiv.org/abs/2601.12762`, NEUIR, date: 2026.1.
  SFT + GRPO trial-then-execute pattern.
- `UI-TARS` — github: `https://github.com/bytedance/UI-TARS`,
  paper: `https://arxiv.org/abs/2509.02544`, ByteDance Seed, date: 2025.1.
- `Agent-R1` — github: `https://github.com/0russwest0/Agent-R1`,
  paper: `https://arxiv.org/abs/2511.14460`, USTC, date: 2025.11.
