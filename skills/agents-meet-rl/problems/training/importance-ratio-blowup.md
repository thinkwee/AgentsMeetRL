# Problem: importance ratios become huge (PPO ratio > 5+)

## Symptoms

- `max_ratio` per batch spikes above 5 or 10.
- `mean_ratio` drifts away from 1.0.
- KL eventually explodes (see `kl-explosion.md`).
- Loss has wide variance per batch.

## Root causes

1. **Async-rollout staleness.** See `async-rollout-staleness.md`.
2. **Retokenization drift.** See `retokenization-drift.md`.
3. **`old_log_probs` not stored from the same policy that generated.**
4. **Off-policy update too aggressive** (multiple PPO epochs without
   clip).
5. **Numerical issues**: log-probs computed in fp16 / bf16 with extreme
   values get clipped wrong.

## Diagnosis

- Hist of `ratio` per token. Healthy: tight gaussian around 1.0.
- `train_step - rollout_gen_step` per batch — if growing, staleness.
- Check `old_log_probs` vs recompute on same policy snapshot.

## Fixes

See:
- `async-rollout-staleness.md`
- `retokenization-drift.md`

Plus:

### Fix: smaller PPO clip ε

Reduce from 0.2 → 0.1. DAPO's asymmetric clipping is even better when
sequences are long.

### Fix: fewer PPO epochs

Reduce `ppo_epochs` to 1 or 2. More epochs amplify off-policy bias.

### Fix: TIS (Truncated Importance Sampling)

veRL's `RolloutCorrectionConfig` exposes TIS-style rollout correction
as a config flag — clip per-token importance ratios at a max, accept
small bias for stability.

### Fix: log-prob in fp32

Compute log-probs in fp32 even if model is bf16. Avoids subtle clipping
issues when log-prob is very negative.

## Paper / repo references

> **veRL** — github: `https://github.com/volcengine/verl`,
> paper: `https://arxiv.org/abs/2409.19256`, ByteDance Seed, date: 2024.9.
> Why: `RolloutCorrectionConfig` (TIS) and PPO clip knobs are
> the canonical implementation for clipping ratio explosions.

> **verl-agent** — github: `https://github.com/langfengQ/verl-agent`,
> paper: `https://arxiv.org/abs/2505.10978`, org: NTU/Skywork, date: 2025.5.
> Why: supports DAPO with asymmetric clipping (`PPO/GRPO/GIGPO/DAPO/...`)
> as a direct drop-in over GRPO's symmetric ε; useful when long
> rollouts cause one-sided ratio drift.

> **AReaL** — github: `https://github.com/inclusionAI/AReaL`,
> paper: `https://arxiv.org/abs/2505.24298`, org: AntGroup/Tsinghua, date:
> 2025.5. Why: async pipeline that documents the staleness-vs-ratio
> trade-off explicitly; pair with `async-rollout-staleness.md`.
