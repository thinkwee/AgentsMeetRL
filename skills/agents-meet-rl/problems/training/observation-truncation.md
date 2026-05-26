# Problem: observations get truncated mid-trajectory and credit is wrong

## Symptoms

- Tool returns 50KB of HTML; you keep last 4K tokens; the action that
  caused the next decision was in the dropped portion.
- Advantage signal trains on responses to *truncated* context — partial
  observation, full reward.
- Eval breaks because at deploy time observations aren't truncated the
  same way.

## Root causes

1. **Naive truncation strategy** (drop oldest, drop random, fixed window
   from end).
2. **Tool returns raw output** instead of pre-filtered.
3. **Truncation happens in the rollout, but reward is computed on
   ground-truth (untruncated) data.**

## Diagnosis

- Per-turn `obs_length` histogram — find the offending tools.
- Episode termination breakdown: "completed" vs "max_turns" vs
  "context_overflow."
- Read 10 truncated episodes — was useful info dropped?

## Fixes

### Fix 1: tool-side filtering, not agent-side truncation

Make the tool return less, instead of the agent forgetting more.

> **multimodal-search-r1** —
> github: `https://github.com/EvolvingLMMs-Lab/multimodal-search-r1`,
> paper: `https://arxiv.org/abs/2506.20670`, ByteDance/NTU, date: 2025.6.
> Returns top-k chunks, not raw HTML.

> **Pixel-Reasoner** — github: `https://github.com/TIGER-AI-Lab/Pixel-Reasoner`,
> paper: `https://arxiv.org/abs/2505.15966`, Waterloo, date: 2025.5.
> Curiosity-driven GRPO with zoom/select-frame; agent picks which region.

> **Mini-o3** — github: `https://github.com/Mini-o3/Mini-o3`,
> paper: `https://arxiv.org/abs/2509.07969`, date: 2025.9. Visual search
> with image cropping.

> **Chain-of-Focus** — github: `https://github.com/xtong-zhang/Chain-of-Focus`,
> paper: `https://arxiv.org/abs/2505.15436`, date: 2025.5. Zoom-in actions.

> **Tool-N1** — github: `https://github.com/NVlabs/Tool-N1`,
> paper: `https://arxiv.org/abs/2505.00024`, NVIDIA, date: 2025.5. Caps
> tool output length explicitly.

### Fix 2: summarize, don't truncate

Insert a summarization turn every K steps. Loses less information than
naive truncation.

> **DR-Venus** / **Kimi-Researcher** / **MemAgent** — see
> `memory-context-overflow.md`.

### Fix 3: bound the env up front

If the env can return 50KB, bound it before the rollout starts.

> **ZeroSearch** — github: `https://github.com/Alibaba-NLP/ZeroSearch`,
> paper: `https://arxiv.org/abs/2505.04588`, Alibaba, date: 2025.5.
> Simulated search with bounded result size.

### Fix 4: log per-turn observation length and cap p95

Don't let tail observations (rare 100KB returns) destabilize an
otherwise-bounded rollout.

### Fix 5: step-based rollout abstraction

If you concatenate all observations into one growing prompt, truncation
is on the entire history. With step-based rollouts, you can keep older
turns intact via memory while bounding only the current observation.

> **verl-agent** — github: `https://github.com/langfengQ/verl-agent`,
> paper: `https://arxiv.org/abs/2505.10978`, NTU, date: 2025.5. Ships a
> step-independent multi-turn rollout abstraction so you can decide
> between turns what to keep, summarize, or drop.

> **Agent-R1** — github: `https://github.com/0russwest0/Agent-R1`,
> paper: `https://arxiv.org/abs/2511.14460`, USTC, date: 2025.11.
> Step-level MDP exposes per-step truncation, summarization, rewriting,
> and augmentation as first-class hooks between turns.

## Paper / repo references

(All cited above.)
