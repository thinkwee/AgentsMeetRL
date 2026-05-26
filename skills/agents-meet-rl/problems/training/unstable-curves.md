# Problem: training curves are noisy / unstable run-to-run

## Symptoms

- Same code, same data, same seed, but reward curves look very different
  across runs.
- Eval at the same step varies by 5+ points between seeds.
- Hard to tell if a hyperparam change helped or just hit a lucky run.

## Root causes

1. **Genuine variance** — RL on LLMs has high variance. Some of this is
   intrinsic.
2. **Non-deterministic rollout** — env, sampling, retrieval all
   non-deterministic.
3. **Async batching order** — async pipelines can reorder updates in
   non-deterministic ways.
4. **Multi-GPU communication non-determinism** (NCCL allreduce).
5. **Float ops in different order** depending on graph execution.

## Diagnosis

Run before reaching for fixes — most "instability" is variance you'd
expect, and the right action is to report it honestly rather than
chase it.

- **Run 3 seeds at the same step.** Compare reward and eval. A 1-2
  point spread is intrinsic; 5+ points is suspect.
- **Compute paired variance.** On the same eval prompts and same
  seeds, compare your method to baseline. If the per-prompt deltas
  have small variance even when the per-run averages don't, your
  method's effect is real and the run-to-run noise is shared.
- **Plot reward vs step with EMA overlay.** If raw curve looks chaotic
  but the EMA is monotone, you have noise, not instability.
- **Check whether the divergence is run-1 vs run-2 entirely.** If
  run-1 succeeds and run-2 collapses, that's a bug not variance —
  see `training-collapse.md`.
- **Bisect on env determinism.** Set the env to deterministic mode
  (fixed seeds for retrieval / sampling). If variance drops to near-0,
  the env was the source.
- **Bisect on float precision.** Same run twice with deterministic
  algorithms (`torch.use_deterministic_algorithms(True)`) — if seeds
  now match exactly, NCCL / float ordering was the source.

## Fixes

### Fix: report 3-seed mean ± std

Single-seed numbers are not credible. Most papers in the corpus report
1 seed and call it a "trend" — for a researcher you should run ≥ 3
seeds.

### Fix: seed everything

```python
torch.manual_seed(seed)
np.random.seed(seed)
random.seed(seed)
torch.cuda.manual_seed_all(seed)
torch.use_deterministic_algorithms(True)  # may slow training
os.environ["CUBLAS_WORKSPACE_CONFIG"] = ":4096:8"
```

### Fix: bound variance with EMA reporting

Report exponential-moving-average of reward / eval, not point values.

### Fix: longer training horizon for robust comparison

Compare at convergence, not at arbitrary step K.

### Fix: paired evaluation

When comparing two methods, run them on the *same* eval prompts with
the *same* seeds. Pairing reduces variance ~4x.

### Fix: fix the env first

Most variance from RL is reward variance, which comes from env variance.
See `env-flakiness.md`.

## Statistical practice

- Report seeds and code commit hash with every result.
- Confidence intervals (bootstrap) over 3-5 seeds are standard.
- Pre-register your eval set for new comparisons; don't fish.

## Paper / repo references

The corpus has limited statistical rigour overall. As a researcher,
your contribution is partly **multi-seed evaluation** because most
papers don't do it. See `../evaluation/statistical-significance.md`.

> **RAGEN** — github: `https://github.com/RAGEN-AI/RAGEN`,
> paper: `https://arxiv.org/abs/2504.20073`, org: RAGEN-AI, date: 2025.4.
> Why: rare in the corpus for actually publishing wandb logs across
> seeds — useful baseline for distinguishing run-to-run variance from
> collapse.

> **Skywork-OR1** — github: `https://github.com/SkyworkAI/Skywork-OR1`,
> paper: `https://arxiv.org/abs/2505.22312`, org: Skywork AI, date: 2025.5.
> Why: large-scale stability study; documents what is intrinsic
> variance vs what is fixable engineering noise.

> **Search-R1** — github: `https://github.com/PeterGriffinJin/Search-R1`,
> paper: `https://arxiv.org/abs/2503.09516`, org: UIUC/Google, date: 2025.3.
> Why: public wandb across v0.1/v0.2/v0.3 — useful run-to-run
> variance reference for search-agent training.
