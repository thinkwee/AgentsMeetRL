# Problem: discount factor γ — how to set it for multi-turn

## TL;DR

| Episode length | γ |
|---|---|
| 1–3 turns | 1.0 (no discount) |
| 4–10 turns | 0.99 |
| 10–30 turns | 0.99 |
| 30–100 turns | 0.95–0.97 |
| 100+ turns | 0.95 |

Apply γ at **turn level**, not token level, for agentic settings.

## Why γ matters at all

For multi-turn agents:

- γ=1 means a 50-step rollout's terminal reward propagates fully back
  to step 0. Step 0 and step 49 get the same advantage. No temporal
  credit signal.
- γ < 1 propagates earlier, creating gradient toward "do useful things
  earlier." This is what you want for long-horizon training.

## Token-level vs turn-level γ

veRL's GAE discounts at token level — the standard recurrence:

```python
delta = token_level_rewards[t] + gamma * nextvalues - values[t]
```

For long rollouts this means γ^L where L is hundreds of tokens —
collapses to ~0 even at moderate γ.

For agentic settings, discount per *turn*, not per token. The idea
(formalized in **GiGPO**'s step-discounted return) is to apply γ at
the rollout-step level:

```python
for t in reversed(range(len(traj_rewards))):
    running_return = traj_rewards[t] + gamma * running_return
    traj_returns[t] = running_return
```

## When γ=1 is correct

- Outcome-only reward at the end: each turn equally responsible for
  outcome. (But then you should use trajectory-level GRPO, not GAE.)
- Episodes ≤ 3 turns: temporal structure too short to matter.

## When γ < 1 hurts

- If your *only* reward is the terminal one and you discount it heavily,
  the gradient becomes near-zero for early turns. Make sure γ^L is at
  least 0.5 across your typical episode length.

For 50-step episodes: γ = 0.99 → γ^50 ≈ 0.6. OK.
For 100-step: γ = 0.99 → γ^100 ≈ 0.37. Marginal. Use 0.995.
For 200-step (DR-Venus territory): γ = 0.995 → γ^200 ≈ 0.37. Still
marginal. Need per-turn intermediate signal (info-gain) anyway.

## Paper / repo references

- `GiGPO` — github: `https://github.com/langfengQ/verl-agent`,
  paper: `https://arxiv.org/abs/2505.10978`, NTU/Skywork, date: 2025.5.
