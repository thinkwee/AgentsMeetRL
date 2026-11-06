# AReaL implementation card

Commit: `d38268e1bb57cfddf10e5491c9df19b05432dd89`. Reviewed: 2026-11-06. Evidence: **source-inspected**; runtime: **not run**.

## Data path and extension boundary

`RolloutWorkflow.arun_episode(engine, data)` returns trajectory data or `None`
for rejection. A separate SDK-compatible `async run(data, **extra_kwargs)` path
returns a scalar reward or rewards keyed by response ID; inheriting the old
`AgentWorkflow` class is deprecated in this snapshot. These two return contracts
must not be confused.

`InteractionWithTokenLogpReward.to_tensor_dict()` emits `input_ids`, `loss_mask`,
`logprobs`, `versions`, `attention_mask`, and `rewards`. In its concat path, it
carries parent masks/logprobs/versions and adds masked context between generations.
If the child input length is not greater than the parent length, it logs a warning
and falls back to masking the parent. This fallback is not proof of exact prefix
identity; inspect actual tokens and template mode in a real integration.

The PPO actor shifts target masks for next-token scoring and selects behavior or
proximal probabilities depending on decoupled-loss/recompute settings. It applies
reward transformations, reference KL rewards, and masked GAE. Do not independently
shift already-shifted arrays in an adapter.

`StalenessManager.get_capacity()` combines concurrency with a version/batch-based
admission bound. It tracks accepted/running/rejected work. This bounds production
under its scheduling assumptions; still measure actual consumed versions and
resume behavior rather than treating it as a per-token lag verifier.

## Verify in an integration

Trace SDK completion IDs to rewards and tensor rows. Preserve generated versions
across a partial episode. Check the configured proximal policy branch and mask
shift. Exercise rejection and restart with an episode consumption ledger.

## Pinned source evidence

- [areal/api/workflow_api.py](https://github.com/inclusionAI/AReaL/blob/d38268e1bb57cfddf10e5491c9df19b05432dd89/areal/api/workflow_api.py) — RolloutWorkflow.arun_episode and SDK-compatible run protocol.
- [areal/experimental/openai/types.py](https://github.com/inclusionAI/AReaL/blob/d38268e1bb57cfddf10e5491c9df19b05432dd89/areal/experimental/openai/types.py) — InteractionWithTokenLogpReward.to_tensor_dict: concat, masks, versions.
- [areal/trainer/ppo/actor.py](https://github.com/inclusionAI/AReaL/blob/d38268e1bb57cfddf10e5491c9df19b05432dd89/areal/trainer/ppo/actor.py) — reward scaling, proximal/behavior logprob branch, mask shift and GAE.
- [areal/infra/staleness_manager.py](https://github.com/inclusionAI/AReaL/blob/d38268e1bb57cfddf10e5491c9df19b05432dd89/areal/infra/staleness_manager.py) — StalenessManager: version-aware admission capacity.
