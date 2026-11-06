# slime implementation card

Commit: `58b0878679de339ec7844b45d884a87955a134be`. Reviewed: 2026-11-06. Evidence: **source-inspected**; runtime: **not run**.

## Data path and extension boundary

`Sample` stores the full `tokens` and a `response_length`; `loss_mask` and
`rollout_log_probs` cover the response region, including masked inserted content.
The source validates those lengths. `group_index` is distinct from `rollout_id`:
the latter identifies siblings when one execution produces multiple samples.
`teacher_log_probs` exists, but that alone does not establish a teacher-only
privileged-context implementation.

The SGLang rollout path dispatches `sample.generate_function_path` or
`args.custom_generate_function_path`. Use the existing native hook for an Agent
loop and preserve the Sample contract. Dataset-specific reward/generation hooks
exist in this snapshot; check their invocation signatures before adapting.

The Megatron policy loss selects old probabilities from trainer `log_probs` or
`rollout_log_probs` according to `use_rollout_logprobs`. `vanilla_tis_function`
computes `exp(train_log_probs - rollout_log_probs)` and multiplies the policy
loss by clamped weights. `importance_weights(mode="mis")` instead rejects ratios
outside an interval. These are different transformations, not interchangeable
names. The loss reducer also receives rollout mask sums; splitting samples can
change weighting unless episode identity and denominators are preserved.

## Verify in an integration

Export a response containing assistant/tool/assistant spans. Assert response
length, mask, and probability alignment; then trace the selected old-logprob
branch and correction arguments. Check native reduction on a split episode.
Do not copy every flag from this snapshot into another release or a custom fork.

## Pinned source evidence

- [slime/utils/types.py](https://github.com/THUDM/slime/blob/58b0878679de339ec7844b45d884a87955a134be/slime/utils/types.py) — Sample: tokens, response_length, loss_mask, rollout_log_probs, rollout_id, teacher_log_probs.
- [slime/backends/megatron_utils/loss.py](https://github.com/THUDM/slime/blob/58b0878679de339ec7844b45d884a87955a134be/slime/backends/megatron_utils/loss.py) — vanilla_tis_function and policy_loss_function: separate behavior correction and policy update.
- [slime/utils/ppo_utils.py](https://github.com/THUDM/slime/blob/58b0878679de339ec7844b45d884a87955a134be/slime/utils/ppo_utils.py) — importance_weights: clamp for tis, interval rejection for mis.
- [slime/rollout/sglang_rollout.py](https://github.com/THUDM/slime/blob/58b0878679de339ec7844b45d884a87955a134be/slime/rollout/sglang_rollout.py) — custom generation dispatch and reward hook.
