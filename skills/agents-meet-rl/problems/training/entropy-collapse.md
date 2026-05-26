# Problem: Output entropy / diversity drops; outputs all look the same

## Symptoms

- `entropy_loss` or `mean_token_entropy` decays toward 0 within a few
  hundred steps.
- Inspecting rollouts reveals identical or near-identical reasoning
  templates across very different prompts.
- Eval accuracy stops climbing or starts to drop.
- Sampling at higher temperature changes nothing — outputs collapse to
  the same template anyway.

## Root causes

1. **Mode collapse** — the policy collapsed to the single highest-reward
   template it found early.
2. **Template collapse** — outputs look diverse *within* a single prompt
   but become input-agnostic *across* prompts. Entropy alone won't catch
   this; you need MI-based diagnostics.
3. **Length / format reward swamps outcome reward**, so the model is
   optimizing the easy term.
4. **KL coefficient is too small** — the policy drifts far from the
   reference and falls into a trivial attractor.

## Diagnosis

### Distinguish entropy collapse from template collapse

The two phenomena look identical on a per-token entropy plot but need
different fixes:

- **Entropy collapse**: model becomes more deterministic per input
  (low H(Z | X)).
- **Template collapse**: reasoning becomes input-independent
  (low I(X; Z)) — diverse-looking traces *within* a prompt but the
  same scaffold *across* prompts.

A cheap proxy that doesn't need a full MI estimator: take 100 rollouts
on 20 different prompts, embed them, and compute mean cosine similarity
*between* prompts vs *within* a prompt. Rising cross-prompt similarity
is template collapse; rising within-prompt similarity is entropy
collapse.

> **RAGEN** — github: `https://github.com/RAGEN-AI/RAGEN`,
> paper: `https://arxiv.org/abs/2504.20073`, RAGEN-AI, date: 2025.4.
> StarPO documents agentic-RL collapse modes and motivates separating
> per-input determinism from input-independence.

### Other diagnostics

- Per-token entropy histogram over time.
- Format-reward fraction of total reward — if > 0.5, outcome reward is
  not driving learning.
- KL to reference model, divergence rate, and whether it has plateaued
  or saturated.

## Fixes

### Fix 1: variance-based prompt filtering

Template collapse correlates with low-variance prompts: when every
rollout in a group earns the same reward, the gradient signal vanishes
and the policy can drift into a generic scaffold without penalty. Drop
groups whose per-prompt reward std is below a threshold (or up-weight
high-variance prompts) so each gradient step pulls from prompts that
actually disagree across rollouts.

> **veRL** — github: `https://github.com/volcengine/verl`,
> paper: `https://arxiv.org/abs/2409.19256`, ByteDance Seed, date: 2024.9.
> Ships `FilterGroupsConfig` for filtering groups by metric — the
> canonical knob for low-variance group dropout.

> **RAGEN** — github: `https://github.com/RAGEN-AI/RAGEN`,
> paper: `https://arxiv.org/abs/2504.20073`, RAGEN-AI, date: 2025.4.
> StarPO is the agentic-RL framework that highlights low-variance /
> bimodal-reward groups as a primary collapse driver.

### Fix 2: stronger KL regularizer to ref model

Increase β (KL penalty weight) or switch to KL-as-loss formulation.

> **veRL** — github: `https://github.com/volcengine/verl`,
> paper: `https://arxiv.org/abs/2409.19256`, ByteDance Seed, date: 2024.9.
> Exposes `KLControlConfig` (`kl_loss_coef`, `kl_penalty`) as
> first-class knobs for tuning β online.

> **GUI-Libra** — github: `https://github.com/GUI-Libra/GUI-Libra`,
> paper: `https://arxiv.org/abs/2602.22190`, date: 2026.2. Uses
> KL-regularized GRPO ("Partially Verifiable RL") explicitly because
> their reward is partial — strong KL is what stops collapse.

### Fix 3: cap format-reward weight

If format/thinking-tag reward dominates, the model learns the format
without the content.

Rule of thumb from the corpus: format weight ≤ 0.1× outcome weight, and
require a non-empty content gate (empty `<answer></answer>` gets 0
format reward, not the typical 0.5).

### Fix 4: token-level loss (Dr.GRPO / DAPO)

Sequence-level loss biases towards short, low-entropy outputs because
short outputs have lower per-token loss variance.

> **verl-agent** — github: `https://github.com/langfengQ/verl-agent`,
> paper: `https://arxiv.org/abs/2505.10978`, NTU, 2025.5. Supports
> `PPO/GRPO/GIGPO/DAPO/RLOO/...` with token-level aggregation as
> default — DAPO clip-higher is a config flip away.

> **Dr.GRPO** — paper: `https://arxiv.org/abs/2503.20783`. Removes
> std-normalization in GRPO advantage; combined with token-level loss,
> length stability improves. Exposed in veRL as the
> `norm_adv_by_std_in_grpo=False` config option.

### Fix 5: entropy bonus

Add an explicit entropy bonus to the loss (small coefficient, e.g. 0.001).
This is old-school RL but still works — many open-source recipes that
tune entropy coefficient (verl's `entropy_coef`) recover from collapse.

### Fix 6: keep a pool of past checkpoints

For self-play / RLAIF, sampling against current-only policy collapses
fastest. Use a buffer.

> **SPIRAL** — github: `https://github.com/spiral-rl/spiral`,
> paper: `https://arxiv.org/abs/2506.24119`, NUS/A*STAR/Sea AI, date: 2025.6.
> Self-play needs an opponent pool to avoid mode collapse.

### Fix 7: harder / more diverse training data

The cheapest fix is often "more data." If 30% of your prompts are
trivial, you'll collapse trivially.

## Paper / repo references

- **RAGEN** — github: `https://github.com/RAGEN-AI/RAGEN`,
  paper: `https://arxiv.org/abs/2504.20073`, RAGEN-AI, date: 2025.4.
  StarPO framework; frames template / mode collapse as agentic-RL's
  central failure mode.
- **veRL** — github: `https://github.com/volcengine/verl`,
  paper: `https://arxiv.org/abs/2409.19256`, ByteDance Seed, date: 2024.9.
  KL knobs and Dr.GRPO toggle.
- **Dr.GRPO** — paper: `https://arxiv.org/abs/2503.20783`. Length-
  stable GRPO via removing advantage std-normalization.
- **verl-agent** — github: `https://github.com/langfengQ/verl-agent`,
  paper: `https://arxiv.org/abs/2505.10978`, NTU, 2025.5. Token-level
  DAPO/GRPO out of the box.
- **SPIRAL** — github: `https://github.com/spiral-rl/spiral`,
  paper: `https://arxiv.org/abs/2506.24119`, NUS/A*STAR/Sea AI,
  2025.6. Opponent pooling for self-play stability.
- **GUI-Libra** — github: `https://github.com/GUI-Libra/GUI-Libra`,
  paper: `https://arxiv.org/abs/2602.22190`, 2026.2. KL-regularized
  GRPO under partial reward.
