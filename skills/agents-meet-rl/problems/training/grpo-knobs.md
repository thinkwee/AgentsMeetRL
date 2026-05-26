# Problem: GRPO knobs — group size, normalization, baseline, advantage scaling

## When this matters

You're already on GRPO and training is roughly working, but you want to
tune. This file lists the knobs that actually move the needle in this
corpus, with the algorithm/idea behind each.

Config flag names below (e.g. `norm_adv_by_std_in_grpo`) are taken from
veRL at the snapshot date; they may be renamed across releases, so check
them against the framework version you use.

## Knob 1: group size N

- **Common settings**: N=8 to N=16 in most papers; N=4 only on cheap
  tasks. **IGPO uses N=16**.
- N=2 essentially turns GRPO into a dueling baseline; doesn't work
  well for sparse rewards.
- Larger N reduces variance but burns rollout compute linearly.

## Knob 2: advantage normalization (with vs without std) — Dr.GRPO

veRL exposes a `norm_adv_by_std_in_grpo` toggle:

- **True (default)**: advantage = (r - μ) / (σ + ε). Original GRPO.
- **False**: advantage = r - μ. **Dr.GRPO**. Used when length blow-up
  is a problem; std-normalized advantage couples reward magnitude
  with length.
- Switch to False if `mean_response_length` keeps growing
  monotonically.

> **Dr.GRPO** — paper: `https://arxiv.org/abs/2503.20783`. The idea:
> remove std-normalization to decouple advantage magnitude from
> sequence length.

## Knob 3: epsilon for std stability

`epsilon=1e-6` is the typical default. If you see NaN/inf in
advantage, raise to 1e-4. veRL handles all-equal-reward groups
specifically by setting std=1, mean=0 — so the group silently
contributes 0 gradient (filter at the dataloader instead, see
`zero-variance-rollouts.md`).

## Knob 4: vectorized vs loop GRPO

veRL ships both a per-prompt loop and a fully-vectorized GRPO
implementation. Functionally equivalent; vectorized is faster on
large batches. If you hit numerical drift between them (rare), prefer
loop for debugging.

## Knob 5: pass@k variant for code/math

GRPO with a pass@k baseline instead of mean-of-N: useful when you
want to optimize "any-of-N solves it," not "average of N solves it."
veRL ships this as a separate advantage estimator.

## Knob 6: KL penalty vs KL loss

veRL's KL controller supports both:

- KL added to advantage (penalty form).
- KL added to total loss (loss form).

Most agentic-RL papers use the **loss form** with small
`kl_loss_coef` (~0.001).

## Knob 7: entropy bonus

`entropy_coef` typically 0.001 or 0; some papers raise it to 0.01 to
fight collapse. See `entropy-collapse.md`.

## Knob 8: token-level vs sequence-level loss aggregation

`loss_agg_mode = token-mean` is mandatory for long generations and
DAPO-style training. See `token-vs-sequence-loss.md`.

## Knob 9: filter low-variance groups

Drop groups whose reward std is below threshold so each step trains
only on prompts where rollouts disagree. See
`zero-variance-rollouts.md`.

## Knob 10: clip ratio (DAPO clip-higher)

PPO-style symmetric ε is 0.1 or 0.2 typical. **DAPO** uses asymmetric
`clip_ratio_low` / `clip_ratio_high` — letting positive advantages
take larger ratio steps than negative ones. Lower if importance
ratios blow up; widen the upper bound if exploration is too cautious.

## Recommended starting config (corpus consensus)

```yaml
algorithm:
  adv_estimator: grpo
  norm_adv_by_std_in_grpo: true        # set false if length blows up
  kl_loss_coef: 0.001
  kl_penalty: kl
  entropy_coef: 0.0
  loss_agg_mode: token-mean             # not seq-mean
  clip_ratio: 0.2
  filter_groups:
    enable: true
    threshold: 1e-4                     # drop near-zero-variance groups
agent_grpo:
  n: 8                                  # 16 if compute permits
```

## GRPO variants registered in modern frameworks

veRL and verl-agent both expose multiple advantage estimators side by
side: `gae` (PPO with critic), `grpo` (outcome GRPO), `grpo_passk`
(pass@k baseline), `reinforce_plus_plus`, `rloo`, plus DAPO and
GSPO variants. Picking one is mostly a config flag.

## Paper / repo references

- **veRL** — github: `https://github.com/volcengine/verl`,
  paper: `https://arxiv.org/abs/2409.19256`, ByteDance Seed, date: 2024.9.
  Reference for the GRPO knob taxonomy used here.
- **verl-agent** — github: `https://github.com/langfengQ/verl-agent`,
  paper: `https://arxiv.org/abs/2505.10978`, NTU, 2025.5. Agentic
  fork; supports `PPO/GRPO/GIGPO/DAPO/RLOO/...` as side-by-side
  estimators.
- **Dr.GRPO** — paper: `https://arxiv.org/abs/2503.20783`. Length-
  stable GRPO via removing advantage std-normalization.
- **GiGPO** — github: `https://github.com/langfengQ/verl-agent`,
  paper: `https://arxiv.org/abs/2505.10978`, NTU, 2025.5
  (NeurIPS 2025). Hierarchical GRPO with inner step-level groups.
- **IGPO** — github: `https://github.com/GuoqingWang1/IGPO`,
  paper: `https://arxiv.org/abs/2510.14967`, Ant Group, 2025.10.
  Per-turn info-gain reward; uses N=16.
