# Problem: NaN / inf in loss or gradients

## Symptoms

- `loss=nan` after training step K.
- `grad_norm=inf`.
- Training crashes or model produces garbage afterward.

## Root causes (most common to least)

1. **Single bad rollout** (corrupted observation, `inf` reward, infinite
   string).
2. **Importance ratio explosion + clipping bug.** See
   `importance-ratio-blowup.md`.
3. **KL computed on mismatched distributions** (template / tokenizer
   bug). See `kl-explosion.md`.
4. **Mixed-precision overflow** (bf16/fp16 with extreme log-probs).
5. **Division by zero** in advantage normalization (group std=0 not
   handled correctly).

## Diagnosis

When you hit NaN:

1. Save the offending batch.
2. Inspect: any inf rewards? Any rollout with response_length = 0? Any
   token IDs out of vocabulary?
3. Recompute loss step by step; pinpoint which term went NaN first.
4. If multiple steps lead to NaN, suspect a systematic issue (drift,
   numerics) rather than one bad batch.

## Fixes

### Fix: skip NaN batches

Add a hard check: if any element of loss/grad is NaN/inf, skip the step
entirely. Don't let one bad batch destabilize Adam state.

### Fix: gradient clipping

`max_grad_norm=1.0` is veRL's default. If you see NaN, lower to 0.5.

### Fix: log-prob in fp32

Always compute log-probs in fp32 even with bf16 model.

### Fix: sanity-check reward function

```python
assert torch.isfinite(reward).all()
assert reward.min() >= -10 and reward.max() <= 10  # reasonable bounds
```

### Fix: fix the underlying KL / ratio explosion

NaN is usually the *symptom*; the root cause is usually one of:
- KL explosion → see `kl-explosion.md`.
- Ratio blowup → see `importance-ratio-blowup.md`.
- Retokenization drift → see `retokenization-drift.md`.

## Paper / repo references

> **veRL** — github: `https://github.com/volcengine/verl`,
> paper: `https://arxiv.org/abs/2409.19256`, ByteDance Seed, date: 2024.9.
> Why: production-grade GRPO/PPO trainer with `max_grad_norm`,
> log-prob fp32, and divide-by-zero guards baked in — fork these
> safeties rather than rolling your own.

> **OpenRLHF** — github: `https://github.com/OpenRLHF/OpenRLHF`,
> paper: `https://arxiv.org/abs/2405.11143`, org: OpenRLHF, date:
> 2024.5. Why: independent reference implementation of PPO/REINFORCE
> stability tricks; useful to cross-check when veRL behaves
> unexpectedly under bf16.

> **AReaL** — github: `https://github.com/inclusionAI/AReaL`,
> paper: `https://arxiv.org/abs/2505.24298`, org: AntGroup/Tsinghua, date: 2025.5.
> Why: documents the staleness and numerics issues that drive most
> agentic-RL NaNs in async pipelines (see `async-rollout-staleness.md`).
