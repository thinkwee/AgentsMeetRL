# Problem: env API rate-limits / times out / returns garbage during training

## Symptoms

- Sporadic rollout failures (5-30%) with no apparent rhyme — same prompt
  fails sometimes, succeeds others.
- Reward signal has high run-to-run variance even on the same model.
- Real search engines / LLM judges / external APIs hit rate limits.
- Sandbox environments crash, leak memory, or return inconsistent state.

## Root causes

1. **Live external service.** Real search engine, real GPT-4, real DB.
2. **Sandbox container instability.** Docker out-of-memory, port
   conflicts, file descriptor leaks.
3. **Unbounded tool output.** Some tool returns 100MB once in a while
   and OOMs the rollout worker.
4. **Concurrent env access without isolation.** Two rollouts hit the
   same env state at the same time.

## Diagnosis

- Per-step env-failure rate metric. Should be < 1%.
- Episode termination breakdown by reason.
- For each tool, p95 latency and error rate. Outliers point at flaky
  tools.

## Fixes

### Fix 1: cache or simulate the tool

Live engines are unreliable; cache results.

> **Search-R1** — github: `https://github.com/PeterGriffinJin/Search-R1`,
> paper: `https://arxiv.org/abs/2503.09516`, UIUC, date: 2025.3.
> Ships a Wikipedia/E5 retrieval index for offline search so RL training
> never depends on a live engine.

> **ZeroSearch** — github: `https://github.com/Alibaba-NLP/ZeroSearch`,
> paper: `https://arxiv.org/abs/2505.04588`, Alibaba, date: 2025.5.
> Simulates a search engine entirely. Decouples training from live API
> stability.

### Fix 2: retry with backoff

Don't fail a rollout because the API hiccupped. Retry 3x with
exponential backoff. Treat persistent failures as missing data, not
zero reward.

### Fix 3: bound tool output size

Cap responses at, e.g., 4K tokens at the env layer. Truncate, summarize,
or rerank.

### Fix 4: dedicated sandbox per rollout

Especially for code: a fresh container per rollout (or pool of N
isolated containers). Don't share state.

> **SWE-Gym** — github: `https://github.com/SWE-Gym/SWE-Gym`,
> paper: `https://arxiv.org/abs/2412.21139`, UC Berkeley/UIUC/CMU/Apple,
> date: 2024.12. Docker-based per-task isolation.

> **R2E-Gym** — github: `https://github.com/R2E-Gym/R2E-Gym`,
> UC Berkeley/ANU, date: 2025.4. Alternative.

> **SWE-World** — github: `https://github.com/RUCAIBox/SWE-World`,
> paper: `https://arxiv.org/abs/2602.03419`, RUC, date: 2026.2.
> Docker-free SWE training via learned world-model surrogate; useful when
> Docker fleet itself is unreliable.

> **OpenSandbox** — github: `https://github.com/alibaba/OpenSandbox`,
> Alibaba, date: 2026.3. Newer general sandbox.

### Fix 5: rate-limit-aware concurrency

If the env has a known rate limit (Serper API: N queries/sec), shape
your rollout concurrency to match.

### Fix 6: deterministic env for reproducibility

Where possible, seed the env per rollout so two runs of the "same"
prompt are bit-identical. Reduces noise in advantage estimation.

### Fix 7: env mocking for debugging

When debugging an algo issue, swap the live env for a mock that always
returns the same result. If the bug persists, env wasn't the cause.

> **IGPO** — github: `https://github.com/GuoqingWang1/IGPO`. Ships an
> `IGPO_MOCK_SEARCH=true` flag that returns deterministic stub
> retrieval for exactly this kind of debugging — a clean reference
> pattern to copy.

## Paper / repo references

- `Search-R1` — github: `https://github.com/PeterGriffinJin/Search-R1`.
- `ZeroSearch` — github: `https://github.com/Alibaba-NLP/ZeroSearch`,
  paper: `https://arxiv.org/abs/2505.04588`, Alibaba, date: 2025.5.
- `SWE-Gym` — github: `https://github.com/SWE-Gym/SWE-Gym`,
  paper: `https://arxiv.org/abs/2412.21139`, date: 2024.12.
- `SWE-World` — github: `https://github.com/RUCAIBox/SWE-World`,
  paper: `https://arxiv.org/abs/2602.03419`, RUC, date: 2026.2.
- `IGPO` — github: `https://github.com/GuoqingWang1/IGPO`,
  paper: `https://arxiv.org/abs/2510.14967`.
