# Problem: my number is high but variance huge — sample size question

## Symptoms

- Two methods differ by 1.5 points on a 200-prompt benchmark.
- Run 1: A=72%, B=70%. Run 2: A=70%, B=73%. Are they actually different?
- Reviewer asks for confidence intervals.

## Quick answer

For binary success (pass/fail) on N prompts, 95% CI half-width is
roughly:

- N=100 → ±10 points.
- N=200 → ±7 points.
- N=500 → ±4 points.
- N=1000 → ±3 points.

If your reported gap is below this width, you can't claim significance
on a single seed.

## Practice

### Multi-seed

Run eval 3+ times with different seeds. The within-method std lower-
bounds your effective uncertainty.

### Paired bootstrap

For comparison: bootstrap on a per-prompt basis. Significantly tighter
than independent samples.

```python
deltas = [score_A[i] - score_B[i] for i in range(N)]
bootstrap_means = []
for _ in range(10000):
    sample = np.random.choice(deltas, size=N, replace=True)
    bootstrap_means.append(np.mean(sample))
ci = np.percentile(bootstrap_means, [2.5, 97.5])
```

If 0 ∈ CI, your gap isn't significant.

### Pre-register sample size

If you're going to report a 1-point improvement, you need ≥ 1000
prompts.

## What the corpus typically does

- Most papers report a single seed.
- Most papers report 1 number per benchmark.
- A single seed, 200-prompt benchmark with 1-point gap is **typical**
  and **not significant**.

You can do better. Reporting 3-seed mean ± std is the simplest research-
quality differentiator.

## Variance sources

- **Sampling variance** — random temperature decoding.
- **Seed variance** — different RL seeds.
- **Env variance** — flaky search/sandbox.
- **Judge variance** — for LLM-judge eval.

Each contributes; report the combined effect.

## Reporting recipe

```
Method A: 72.3 ± 0.8 (n=3 seeds, T=0, paired bootstrap CI [71.5, 73.1])
Method B: 70.1 ± 1.2 (same)
Δ = +2.2 (95% paired CI [+1.0, +3.4])
```

Better than:

```
Method A: 72.3
Method B: 70.1
```

## Paper / repo references

> **RAGEN** — github: `https://github.com/RAGEN-AI/RAGEN`,
> paper: `https://arxiv.org/abs/2504.20073`, org: RAGEN-AI, date: 2025.4.
> Why: rare exemplar in the corpus that publishes per-seed wandb
> across multiple runs and frames the variance question explicitly.

> **Skywork-OR1** — github: `https://github.com/SkyworkAI/Skywork-OR1`,
> paper: `https://arxiv.org/abs/2505.22312`, org: Skywork AI, date: 2025.5.
> Why: large-scale stability study; reports run-to-run gaps that bound
> what counts as "real" improvement at typical eval scale.

> **Search-R1** — github: `https://github.com/PeterGriffinJin/Search-R1`,
> paper: `https://arxiv.org/abs/2503.09516`, org: UIUC/Google, date: 2025.3.
> Why: public wandb across versions → can compute paired bootstrap
> across released checkpoints rather than re-running from scratch.

## See also

- `pass-at-k.md` — what metric to use.
- `reproducibility.md` — variance from env / Docker.
- `../training/unstable-curves.md` — variance during training.
