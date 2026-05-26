# Problem: what ablations to run; how to isolate the contribution

## The ablation question

You proposed method X = (component A + component B + component C). You
measure: X works better than baseline. Which components actually
matter?

## Standard ablations

### Single-component drop

`X − A`, `X − B`, `X − C`. Each tells you marginal contribution of
that component.

### Component-only

`baseline + A`, `baseline + B`, `baseline + C`. Tells you which
component alone gets you most of the way.

### Pairwise

`X − A − B`, etc. Reveals interactions.

### Hyperparam sensitivity

For each knob: vary across reasonable range. If results are flat across
the range, the knob doesn't matter.

## What papers in this corpus typically ablate

- **Reward weights** (most common). e.g. IGPO ablates curriculum on/off,
  info-gain type (`log_prob_diff` vs `prob_diff`),
  normalization mode (separate vs joint).
- **Algorithm variants**. e.g. GiGPO ablates inner-group similarity
  threshold.
- **Cold-start** (SFT vs no-SFT, or SFT data size).
- **Group size N**.
- **Curriculum schedule** (linear vs constant).

## What papers often *don't* ablate (and you should)

- **Reference model choice** (SFT model vs base model).
- **Tokenizer / chat template variations**.
- **Random seed variance**. Most papers report 1 seed; ablation should
  include at least 3 seeds.
- **Data scale**. Often the gain is from more data, not the method.

## Strong-ablation checklist

For each method component:

- [ ] What does it add over the baseline alone?
- [ ] What does removing it from the full method cost?
- [ ] Is its contribution stable across seeds?
- [ ] Is it sensitive to a single hyperparam?
- [ ] Does the contribution shrink with stronger baseline / longer
      training?

## When ablations are misleading

### "Ablation looks good but the real source is data"

If you trained method X on more data than baseline, ablation shows
"X works." But it's the data, not X.

**Fix**: match training data exactly. Same dataset, same number of
rollouts seen.

### "Ablation looks good for 1k steps but disappears at convergence"

A method that helps early-training but doesn't help late-training is a
warm-up / curriculum, not a fundamental contribution.

**Fix**: train to convergence, ablate at convergence too.

### "Ablation cherry-picks one of N seeds"

**Fix**: report all seeds.

### "Ablation against a weak baseline"

Reviewers will compare your ablation against the *next-strongest*
method in the literature, not your home-grown weak baseline.

**Fix**: ablate against the strongest reasonable baseline.

## Examples from the corpus

### IGPO ablations

> **IGPO** — github: `https://github.com/GuoqingWang1/IGPO`,
> paper: `https://arxiv.org/abs/2510.14967`, date: 2025.10.

IGPO's `train.sh` config exposes:

- `info_gain_type`: log_prob_diff vs prob_diff.
- `info_gain_norm_mode`: separate vs joint.
- `use_curriculum`: on/off.
- `agent_grpo.n`: group size.

These are the natural ablations. The paper covers them.

### GiGPO ablations

> **verl-agent / GiGPO** — github:
> `https://github.com/langfengQ/verl-agent`,
> paper: `https://arxiv.org/abs/2505.10978`, org: Ant Group, date: 2025.5.

The paper ablates (1) inner step-group similarity threshold, (2)
cross-step grouping toggle, (3) the two γ discount factors (step vs
episode). Each isolates one piece of the hierarchical-advantage idea.

### RAGEN ablations

> **RAGEN** — github: `https://github.com/RAGEN-AI/RAGEN`,
> paper: `https://arxiv.org/abs/2504.20073`, date: 2025.4.

Diagnoses-as-ablation: MI metric on/off, reasoning-entropy on/off,
template-collapse threshold variations. The diagnostic instrument
*is* the contribution.

## See also

- `baseline-selection.md`
- `../evaluation/statistical-significance.md` — how many seeds
- `../training/unstable-curves.md` — variance during training
