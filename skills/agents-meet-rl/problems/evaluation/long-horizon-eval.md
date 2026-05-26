# Problem: long-horizon eval — episodes too costly, partial credit, failure-mode breakdown

## Symptoms

- Each eval episode takes minutes (Docker spin-up, multi-turn rollout).
- Even with 200 episodes, run takes hours.
- Many episodes hit max_turns; can't tell if they were "almost there"
  or "hopelessly off."

## Patterns from the corpus

### Lite subset for fast iteration

Most long-horizon benchmarks have a Lite split:

- **WebArena-Lite** vs WebArena (from `WebAgent-R1`).
- **SWE-Bench Lite** vs SWE-Bench Verified.
- **GAIA Lite** in GAIA family.

Use Lite during dev iteration; full at paper time.

### Partial-credit metrics

Binary success is harsh on long horizon. Add intermediate signals:

- **Step-success rate**: how many sub-goals completed.
- **Action-validity rate**: how many actions were syntactically valid.
- **Tool-success rate**: how many tool calls returned non-error.

> **MagicGUI** — github: `https://github.com/MagicAgent-GUI/MagicGUI`,
> paper: `https://arxiv.org/abs/2508.03700`, Honor, date: 2025.8.
> RFT framework with multi-level metrics.

### Failure-mode breakdown

Categorize failures explicitly:

- "Completed correctly."
- "Completed wrong" (gave wrong answer).
- "Hit max_turns" (out of compute budget).
- "Env error" (Docker/API failure).
- "Parse error" (action couldn't be executed).
- "OOM" (rollout exceeded memory).

Each implies a different fix. A model with 30% completed + 30%
max_turns is much closer to working than 30% completed + 30% parse_error.

### Episode-level statistics

For long episodes, sample size is small. Bootstrap CIs on per-episode
success.

### Run subset, not full benchmark, frequently

For SWE-Bench: iterating on full takes 6+ hours. Use a 50-instance
subset for hourly check-ins, full eval at end of run.

## Cost-saving tricks

### 1. Cap max_turns at training rather than re-running

If your model hit max_turns at 50% of episodes, raising max_turns from
50 to 100 won't necessarily help — it might just spend more compute.

### 2. Cache rollouts

If env is deterministic (after seed), cache rollout outputs. Don't re-
run for every metric tweak.

### 3. Pre-fetch tool / search responses

For search agents: pre-fetch top-k results offline. Run rollouts
against cache.

### 4. Eval at scale-down

Eval first at 7B model size, then 70B. Cheaper iteration.

## Reporting long-horizon eval

```
SWE-Bench Verified (n=500):
  Completed correctly:       42.1% [38.4, 45.7]
  Completed wrong:           18.2% [15.4, 21.1]
  Max-turns hit:             24.0% [20.6, 27.6]
  Env error:                  9.7% [7.5, 12.4]
  Parse error:                4.5% [3.0, 6.4]
  OOM:                        1.5% [0.6, 2.7]
```

This tells a researcher *where to invest* far more than "42.1%."

## See also

- `reproducibility.md` — env / Docker drift specific to
  long-horizon.
- `../training/observation-truncation.md` — long-horizon train issues.
- `../training/credit-assignment-long-horizon.md` — per-turn credit when
  episodes are 50+ turns.
- `../training/memory-context-overflow.md` — context-window strategies
  for long-horizon rollouts.

## Paper / repo references

**Other corpus entries:**

- `debug-gym` — debugging benchmark — multi-turn agent debug sessions.
  github: `https://github.com/microsoft/debug-gym`, Microsoft Research, date: 2024.11

- `MLE-Dojo` — MLE benchmark with multi-step pipeline tasks.
  github: `https://github.com/MLE-Dojo/MLE-Dojo`, GIT, Stanford, date: 2025.5

- `LoCoBench-Agent` — long-context SWE benchmark.
  github: `https://github.com/SalesforceAIResearch/LoCoBench-Agent`, Salesforce AI Research, date: 2025.11
