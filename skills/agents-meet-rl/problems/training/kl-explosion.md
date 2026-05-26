# Problem: KL divergence to reference model explodes

## Symptoms

- Logged `kl_div` or `kl_loss` rises super-linearly within tens of steps.
- Often paired with NaN gradients, large importance ratios, or sudden
  reward collapse.
- Eval breaks badly — model has drifted far from its SFT init.
- Sometimes the *reverse* happens: KL stays at 0.0 throughout. That's
  also a bug (see end).

## Root causes

1. **β / KL coefficient too small** — no anchoring force.
2. **No KL penalty at all** — some recipes default to none, expecting it
   in the loss instead.
3. **KL formulation bug** — KL computed on the wrong distribution
   (forward vs reverse, raw vs masked, including/excluding response
   tokens).
4. **Reference model not frozen** — accidentally updating ref params.
5. **Tokenizer / chat-template mismatch** between policy and reference
   (KL divergence is over different distributions even at init —
   diverges to inf trivially). Often co-occurs with retokenization
   drift.
6. **Off-policy gap too large** (async rollout / outdated old_log_probs)
   — the ratio `pi_new / pi_old` is huge, KL estimate explodes.

## Diagnosis

- Log per-step `mean_ratio`, `max_ratio`, `kl_loss`, `kl_penalty`.
  Healthy: ratio ≈ 1.0, max ratio < 5, KL < 0.5.
- If `max_ratio` is huge, it's an off-policy / drift problem.
- If `mean_ratio ≈ 1` but `kl_loss` is huge, suspect KL formulation bug.
- Compute KL at init (step 0). It should be exactly 0 (policy ≡
  reference). If not, you have a chat-template / tokenizer mismatch.

## Fixes

### Fix 1: increase KL coefficient

veRL exposes a `KLControlConfig` with two formulations:

- **KL penalty** (subtract from advantage): set `kl_penalty=0.001` and
  scale up if you see drift.
- **KL loss** (add to total loss): set `kl_loss_coef=0.001`.

Most agentic-RL papers in this corpus use small β (0.001–0.01); if you
need to crank it to 0.1 you have a deeper bug.

### Fix 2: GUI-Libra-style strong-KL GRPO when reward is partial

When the reward signal is weak/partial, KL anchoring becomes the main
stabilizer.

> **GUI-Libra** — github: `https://github.com/GUI-Libra/GUI-Libra`,
> paper: `https://arxiv.org/abs/2602.22190`, date: 2026.2.
> KL-regularized GRPO ("Partially Verifiable RL"). Designed for tasks
> where outcome reward is incomplete.

### Fix 3: clip importance ratios more aggressively

PPO clip ε reduction (e.g., 0.1 → 0.05). DAPO uses dynamic clipping —
different ε for positive and negative advantage:

> **DAPO** — paper: `https://arxiv.org/abs/2503.14476`,
> blog: `https://dapo-sia.github.io/`, ByteDance Seed, date: 2025.3.
> Token-level loss + dynamic clipping; explicitly meant to handle
> importance-ratio blowup at long-sequence training.

### Fix 4: refresh `old_log_probs` more often

If async rollout: shorten the gap between policy update and rollout
collection.

> **AReaL** — github: `https://github.com/inclusionAI/AReaL`,
> paper: `https://arxiv.org/abs/2505.24298`, AntGroup/Tsinghua, date: 2025.5.
> Decoupled PPO designed to handle staleness explicitly.

If sync: ensure `old_log_probs` are stored from the *same* policy that
generated the tokens (not a stale copy from before the last update).

### Fix 5: fix retokenization drift first

If you're storing rollouts as text and re-tokenizing for training, KL is
computed on a *different sequence* than what was generated. Fix this
before chasing KL hyperparameters.

See `retokenization-drift.md`.

### Fix 6: chat-template parity check

At init, KL must equal exactly 0. If not:

- Are you applying the same chat template to policy and reference?
- Are you including system prompt the same way?
- Are you tokenizing with same `add_special_tokens` / `padding_side`?

A common bug: policy uses `tokenizer.apply_chat_template(...,
add_generation_prompt=True)` while reference uses
`add_generation_prompt=False`.

## The opposite symptom: KL stuck at 0

If KL is exactly 0 always:

- Your KL term might be applied only to the prompt tokens, not the
  response tokens (mask bug).
- Or you're not actually backpropagating through it.

veRL's reference handling masks observation/prompt tokens explicitly
(this is the role of the `compute_gae_advantage_return` step) so that
KL is computed only over response tokens — make sure your custom code
doesn't over-mask and zero everything out.

## Paper / repo references

- `GUI-Libra` — github: `https://github.com/GUI-Libra/GUI-Libra`,
  paper: `https://arxiv.org/abs/2602.22190`, date: 2026.2.
- `DAPO` — paper: `https://arxiv.org/abs/2503.14476`,
  blog: `https://dapo-sia.github.io/`, ByteDance Seed, 2025.3.
- `AReaL` — github: `https://github.com/inclusionAI/AReaL`,
  paper: `https://arxiv.org/abs/2505.24298`, AntGroup/Tsinghua, date: 2025.5.
