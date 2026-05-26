# Problem: token-level vs sequence-level loss aggregation — which?

## Decision

| Task | Recommended | Reason |
|---|---|---|
| Long generations (CoT, agentic rollouts) | **token-level** | Length blow-up otherwise |
| Short generations (≤ 100 tokens) | sequence-level OK | Length not a concern |
| Length-stability matters | token-level + Dr.GRPO | Decouple length from advantage |
| Variable-length agentic rollout | **token-level** | Different rollouts have very different lengths |

In modern agentic-RL, **token-level is the safer default.**

## Why it matters

GRPO's standard formulation aggregates loss across response tokens then
*averages over rollouts*. Long rollouts contribute disproportionately
to the gradient if you sum over tokens but average across the batch.

Token-level loss aggregates per-token then averages, which decouples
update magnitude from sequence length.

## DAPO and Dr.GRPO inside the corpus

DAPO and Dr.GRPO are not standalone repos — they live inside veRL and
its consumers as algorithm options.

> **veRL** — github: `https://github.com/volcengine/verl`,
> paper: `https://arxiv.org/abs/2409.19256`, ByteDance Seed, date: 2024.9.
> Why: ships `loss_agg_mode` (token-mean / seq-mean variants)
> and the Dr.GRPO toggle `norm_adv_by_std_in_grpo=False` as first-class
> config flags, not a fork.

> **verl-agent** — github: `https://github.com/langfengQ/verl-agent`,
> paper: `https://arxiv.org/abs/2505.10978`, org: NTU/Skywork, date: 2025.5.
> Why: agentic fork of veRL; documents `PPO/GRPO/GIGPO/DAPO/RLOO/...`
> all aggregating at token level by default for multi-turn rollouts.

> **slime** — github: `https://github.com/THUDM/slime`, org: Tsinghua University (THUDM).
> Why: lightweight framework supporting `GRPO/GSPO/REINFORCE++` —
> reference for sequence-level GSPO when you want the contrast against
> token-level DAPO.

## Implementation note

veRL's `loss_agg_mode` knob controls aggregation:

- `token-mean`: token-level (recommended for agentic).
- `seq-mean-token-mean`: sequence-level mean of token-level mean.
- `seq-mean-token-sum`: sequence-level mean of token-level sum.

For agentic tasks: `loss_agg_mode=token-mean`.

## Symptom to switch from sequence to token

- `mean_response_length` rising monotonically.
- Most rollouts in batch are extreme lengths (very short or very long).
- Variance in length within a group is high.

## Paper / repo references

- `veRL` paper (above) covers the mechanics; the verl repo's algorithm
  config exposes the exact loss-aggregation knobs.
- For algorithm intuition on **DAPO clip-higher** vs **GSPO sequence
  ratio**, the verl-agent and slime READMEs discuss each estimator
  option side-by-side.

