# Problem: PPO knobs — clip ε, GAE λ, value coef, KL formulation

## When this matters

You've decided to use PPO with a critic (not GRPO). Common when:

- Reward is dense or you have a learned PRM.
- You need a stable value estimate for long trajectories.
- Tasks where GRPO's group-relative advantage isn't useful (e.g., huge
  state space, can't sample N comparable trajectories).

Config flag names below (e.g. `KLControlConfig`) are taken from veRL at
the snapshot date; they may be renamed across releases, so check them
against the framework version you use.

## Knob 1: clip ε

- 0.2 — vanilla PPO default.
- 0.1 — stricter; use when ratio drift is a problem (long sequences,
  async rollout).
- DAPO's asymmetric clipping: ε_low for negative-advantage tokens,
  ε_high for positive. Keep positive-side clip looser (more reward to
  good tokens, more clip on bad tokens).

> **DAPO** — paper: `https://arxiv.org/abs/2503.14476`,
> blog: `https://dapo-sia.github.io/`, ByteDance Seed, date: 2025.3.
> Reference recipe for asymmetric clipping.

> **VAPO** — `https://arxiv.org/abs/2504.05118`. Value-based augmented
> PPO. Outperforms DAPO on AIME from Qwen-32B-base.

## Knob 2: GAE λ

- λ=0.95 (verl default) — typical PPO setting.
- λ=1.0 — pure Monte Carlo; high-variance.
- λ=0.0 — pure TD; biased.

For multi-turn agents with intermediate rewards, λ=0.95 is fine.
For pure outcome-only multi-turn, λ=1.0 is sometimes used (since there's
no intermediate signal anyway).

## Knob 3: γ (discount)

- γ=1.0 for short generations and outcome-only reward.
- γ=0.99 for multi-turn (10–30 turns) with any per-turn signal.
- γ=0.95 for very long-horizon (50+ turns).

veRL's GAE applies γ at the token level by default. For multi-turn
agentic settings you may want γ at the *turn* level, not token —
verl-agent's GiGPO computes a step-discounted return per trajectory
(propagating per-step rewards end-to-start with γ at the *turn*
boundary, not the token).

## Knob 4: value loss coefficient

- 0.5 — vanilla PPO default.
- 0.1 — when the value head is harder to train (long sequences, sparse
  rewards). Reduces value-loss dominating policy-loss.
- 1.0 — when value head is the bottleneck.

## Knob 5: KL formulation (penalty vs loss)

- **KL penalty** (subtract β*KL from advantage). Easier to control.
- **KL loss** (add β*KL to total loss). Smoother gradient.

Most agentic-RL papers use KL loss with small β (0.001–0.01).
veRL's `KLControlConfig` exposes both formulations as a config flag.

## Knob 6: PPO epochs

- 1–2 epochs: most agentic-RL setups. Larger amplifies off-policy bias.
- 4 epochs: stable single-turn RL (math-only TIR).
- More than 4: rarely helpful.

## Knob 7: minibatch size

Large minibatches reduce variance but increase memory. Standard:
4–32 effective minibatches per training-batch.

## Knob 8: critic warm-up

When starting fresh (no critic init), the value head outputs noise.
First 100 steps: reduce policy LR, increase value LR. Or freeze policy
for the first ~100 steps.

> **AReaL** —
> github: `https://github.com/inclusionAI/AReaL`,
> paper: `https://arxiv.org/abs/2505.24298`, AntGroup/Tsinghua, date: 2025.5.
> Decoupled PPO with explicit critic management.

## When NOT to use PPO with critic

- You don't have process / dense reward — use GRPO (no critic needed).
- Short trajectories (≤ 5 turns) — GRPO is simpler.
- Memory budget is tight — critic ≈ +50% activations.

## Recommended starting config

```yaml
algorithm:
  adv_estimator: gae
  gamma: 0.99
  lam: 0.95
  clip_ratio: 0.2
  value_clip_range: 0.2
  vf_coef: 0.5
  ppo_epochs: 2
  kl_loss_coef: 0.001
  entropy_coef: 0.0
  loss_agg_mode: token-mean
```

## Paper / repo references

- `DAPO` — paper: `https://arxiv.org/abs/2503.14476`,
  blog: `https://dapo-sia.github.io/`, ByteDance Seed, 2025.3.
- `VAPO` — `https://arxiv.org/abs/2504.05118`.
- `AReaL` — github: `https://github.com/inclusionAI/AReaL`,
  paper: `https://arxiv.org/abs/2505.24298`, AntGroup/Tsinghua, date: 2025.5.
