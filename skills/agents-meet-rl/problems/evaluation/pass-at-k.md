# Problem: pass@1 vs pass@k vs majority@k — what to report

## TL;DR

| Setting | Best metric |
|---|---|
| Verifiable single-answer (math, exact-match QA) | **pass@1** with T=0 sampling |
| Verifiable code (test pass) | pass@1 (T=0) and pass@k (T=0.7, k=10) |
| Open-ended | majority@k or LLM-judge with confidence intervals |
| Train-vs-eval comparison | same metric both sides |

## Definitions

- **pass@1 (T=0)**: greedy decode, single attempt, success ratio.
  Most common. Lowest variance.
- **pass@k (T>0)**: sample k attempts at temperature T; success if any
  succeeds. Captures the model's "best-of-k" capability.
- **maj@k**: sample k attempts; take majority answer; success if
  majority is correct. Lower variance than pass@1, higher than pass@k.

## Common mistakes

### Mistake 1: pass@k at T=0

Useless. T=0 makes all k samples identical; pass@k = pass@1. If you
want pass@k, you must use T>0.

### Mistake 2: pass@k as flagship metric

pass@k can hide a worse pass@1. A model with pass@1=20%, pass@10=80%
may underperform a model with pass@1=40%, pass@10=70% in deployment.
Report both.

### Mistake 3: comparing pass@k across different k

pass@10 of model A vs pass@5 of model B is unfair. Match k.

### Mistake 4: not reporting k or T

Always report. "pass@1" alone is ambiguous (T=0 or T=1?).

### Mistake 5: fishing for k

Don't run pass@5, pass@10, pass@20 and pick the one that looks best.
Pre-register.

## Sampling parameters

For pass@k:

- T = 0.6–1.0 (0.7 typical).
- top_p = 0.9–0.95.
- Match across baseline and your method.

veRL's eval scripts have these as defaults. Check your fork didn't
override them.

## Statistical care

### Sample size

For pass@1:

- 200 prompts: ±3 points at 95% CI.
- 500 prompts: ±2 points.
- 1000 prompts: ±1 point.

If your benchmark has < 200 prompts, **don't claim < 3 point
improvements** without seeds.

### Multiple seeds

Run eval 3+ times with different seeds. Report mean ± std (or 95% CI).
Most papers in the corpus don't do this — it's a research-quality
differentiator.

### Paired bootstrap

Compare two methods on the *same* prompts. Bootstrap reduces variance
significantly.

## Inference-time scaling: when it counts

Many recent papers report flashy pass@k numbers via:

- Self-consistency (majority@k)
- Tree search / MCTS
- Best-of-N with reward model
- Process-reward-guided search

If your paper claims a number, **state whether inference-time scaling
was used** and what budget. A pass@1 win at 1x compute beats a pass@10
win at 10x compute, often.

> **AgentRM** — github: `https://github.com/thunlp/AgentRM`,
> paper: `https://arxiv.org/abs/2502.18407`, THUNLP, date: 2025.2.
> RM-guided search at eval time.

> **MASPRM** — github: `https://github.com/milad1378yz/MASPRM`,
> paper: `https://arxiv.org/abs/2510.24803`, UBC/Huawei, date: 2025.10.
> MCTS at eval.

## See also

- `inference-time-scaling.md` — best-of-N, tree search.
- `statistical-significance.md` — variance and sample size.
