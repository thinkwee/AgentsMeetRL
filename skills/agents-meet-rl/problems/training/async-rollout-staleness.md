# Problem: async rollout creates policy lag or training/inference mismatch

## Symptoms

- Rollout-to-consumption version lag grows or differs strongly by task length.
- Behavior-correction or update ratios develop heavy tails; ESS falls and
  rejection/clipping increases.
- Reward/eval changes alongside queue or backend changes. This is a diagnostic
  correlation, not sufficient proof that async is the cause.

## Root causes

Behavior, old/proximal, current, and reference policies have different roles.
Read [async and mismatch](../../mechanisms/async-and-mismatch.md) before interpreting
`old_log_probs`: a trainer may intentionally recompute a proximal policy distinct
from the behavior policy. Other causes include mismatched contexts/tokenization,
sampling conventions, precision, and MoE routing. Even equal weight versions do
not guarantee identical probabilities across implementations.

## Diagnosis

1. Verify actual learner tokens and masks against engine requests and outputs.
2. Retain behavior logprobs and generation versions; record proximal recompute
   versions separately. Use per-span provenance for mixed-version episodes.
3. Compare fixed-weight engine/trainer probabilities before attributing all
   differences to lag. Inspect sampled versus raw-softmax logprob conventions.
4. Measure lag, log-ratio quantiles, ESS, correction/rejection fractions, and
   queue wait time by task and length. No universal maximum-ratio threshold applies.

## Fixes

Bound admission/queue depth and refresh delay when stale work accumulates. Preserve
behavior provenance through recomputation. Match the estimator's correction to the
selected proximal policy; PPO clipping and TIS address distinct ratios. Truncation
trades variance for bias and token-local correction is not exact full-trajectory IS.

A synchronous comparison can isolate scheduling effects when running experiments
is authorized. Changing to REINFORCE++ or another critic-free method does not by
itself remove off-policy bias. Verify restart/partial-rollout consumption as well
as steady-state behavior.

## Paper / repo references

- [AReaL implementation card](../../implementations/areal.md): version-aware
  admission and proximal-logprob branches, with pinned source links.
- [veRL implementation card](../../implementations/verl.md): correction and bypass paths.
- [slime implementation card](../../implementations/slime.md): separate policy loss and TIS.
- [AReaL paper](https://arxiv.org/abs/2505.24298).
