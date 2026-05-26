# Problem: All N rollouts in a group share the same reward (zero-variance group)

## Symptoms

- GRPO advantage looks fine on average but fraction of "useful" prompts in
  a batch is small.
- Loss decreases slowly even with many GPUs and many steps.
- Logging shows `id2std ≈ 0` for many groups, or the per-group mean and
  per-rollout score are identical.
- After a few hundred steps the model "knows" the easy prompts and the
  hard ones, with nothing in between contributing gradient.

## Root causes

1. **Prompt difficulty is bimodal.** Either the model gets all N right or
   all N wrong. Both produce zero advantage in GRPO.
2. **Stochastic env state isn't seeded per rollout.** Two rollouts of the
   "same" prompt can hit different search results / sandbox state, but the
   resulting reward still ends up identical because the env masks
   variance behind a binary outcome.
3. **Reward function is too coarse.** Pass/fail with no shaping; small
   differences between rollouts collapse to the same scalar.
4. **Group size N is too small** to expose any disagreement.

## Diagnosis

- Log per-step *fraction of groups with std==0*. If > 50%, you're starving
  the policy of signal.
- Inspect a sample of zero-variance groups. Are they all-correct, or
  all-failed-with-the-same-error?
- For RAGEN-style template-collapse, also compute MI-based diagnostics
  (see `entropy-collapse.md`).

## Fixes

### Fix 1: filter or re-weight low-variance prompts (the canonical fix)

Drop prompts whose group-reward variance is below a threshold, or
up-weight high-variance prompts. Use reward variance per prompt as a
signal-to-noise proxy and skip those prompts before they consume
rollout budget.

> **veRL** — github: `https://github.com/volcengine/verl`,
> paper: `https://arxiv.org/abs/2409.19256`, ByteDance Seed, date: 2024.9.
> Ships `FilterGroupsConfig` for filtering groups by metric, and
> handles the all-equal-reward branch by setting mean=0/std=1 (group
> still produces 0 gradient — filter at the dataloader, not the loss).

> **RAGEN** — github: `https://github.com/RAGEN-AI/RAGEN`,
> paper: `https://arxiv.org/abs/2504.20073`, RAGEN-AI, date: 2025.4.
> StarPO framework: documents bimodal/zero-variance groups as a
> central failure mode of multi-turn agentic RL.

### Fix 2: dynamic group size

Increase N for hard prompts; keep small N for easy ones.

### Fix 3: shape the reward so all-correct groups still vary

Make the reward graded:

- Add length-normalized correctness (more partial credit).
- Add format reward as a tiebreaker (small weight ≤ 0.1).
- For tool-use: reward intermediate tool-call validity even on
  unsuccessful final answer.

### Fix 4: process / info-gain reward to recover signal on hard prompts

When *all-fail*, info-gain still gives per-turn signal, even though the
final outcome was 0.

> **IGPO** — github: `https://github.com/GuoqingWang1/IGPO`,
> paper: `https://arxiv.org/abs/2510.14967`, Ant Group, 2025.10
> (ICLR 2026). The idea: per-turn info-gain reward = change in log-
> probability of the gold answer between consecutive turns. Gives
> dense per-turn signal even when outcome reward is 0.

### Fix 5: difficulty curriculum

Sort prompts by historical success rate; train preferentially on
"learnable" ones (success rate in [0.1, 0.9]).

> **Absolute-Zero-Reasoner** — github:
> `https://github.com/LeapLabTHU/Absolute-Zero-Reasoner`,
> paper: `https://arxiv.org/abs/2505.03335`, Tsinghua, date: 2025.5.
> TRR++ uses *learnability* as a weighting term.

> **R-Zero** — github: `https://github.com/Chengsong-Huang/R-Zero`,
> paper: `https://arxiv.org/abs/2508.05004`, Tencent AI Seattle, date: 2025.8.
> A challenger generates harder problems as the solver improves.

## Paper / repo references

- **RAGEN** — github: `https://github.com/RAGEN-AI/RAGEN`,
  paper: `https://arxiv.org/abs/2504.20073`, RAGEN-AI, date: 2025.4.
  StarPO framework: bimodal-reward / zero-variance groups as the
  central failure mode of agentic RL.
- **IGPO** — github: `https://github.com/GuoqingWang1/IGPO`,
  paper: `https://arxiv.org/abs/2510.14967`, Ant Group, 2025.10.
  Per-turn info-gain reward.
- **Absolute-Zero-Reasoner** — github:
  `https://github.com/LeapLabTHU/Absolute-Zero-Reasoner`,
  paper: `https://arxiv.org/abs/2505.03335`, Tsinghua, 2025.5.
  Learnability-weighted training.
- **R-Zero** — github: `https://github.com/Chengsong-Huang/R-Zero`,
  paper: `https://arxiv.org/abs/2508.05004`, Tencent AI Seattle, 2025.8.
  Challenger-solver self-play for difficulty curriculum.
- **veRL** — github: `https://github.com/volcengine/verl`,
  paper: `https://arxiv.org/abs/2409.19256`, ByteDance Seed, date: 2024.9.
  `FilterGroupsConfig` for filtering by metric.
