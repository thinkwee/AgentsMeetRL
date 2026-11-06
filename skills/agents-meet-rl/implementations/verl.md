# verl implementation card

Commit: `00cd5b44ec59b46a5d3ece5f9da41fdb01b890a8`. Reviewed: 2026-11-06. Evidence: **source-inspected**; runtime: **not run**.

## Data path and extension boundary

`AgentLoopOutput` separates `prompt_ids`, `response_ids`, `response_mask`, and
optional `response_logprobs`. `as_dict()` converts these to training tensors and
maps response logprobs to `rollout_log_probs`. Response regions in a tool loop
can contain tool/context tokens; response length is not the count of actions.

`ToolAgentLoop` merges assistant tokens and context messages through distinct
chat-template helpers, retains response masks, and enforces length/turn limits.
For a custom task, inspect the existing loop and its tool interfaces; do not
assume arbitrary text concatenation reproduces the engine's token prefix.

`compute_grpo_outcome_advantage` uses group indices and configurable std
normalization. `agg_loss` implements token-mean, sequence-mean of token-mean,
and sequence-mean of token-sum variants, with global denominator inputs for
distributed execution. Their meanings are derived in
[multi-turn objectives](../mechanisms/multi-turn-objectives.md).

`rollout_corr_helper` distinguishes correction/rejection from bypass mode.
Bypass assigns rollout logprobs as old logprobs and uses its corresponding loss
path; it is not identical to recomputing a separate proximal policy plus correction.

## Verify in an integration

Trace one native loop output through padded tensors and the loss mask. Check
which config selects the actual actor loss and correction path, and verify
aggregation under unequal response lengths and microbatch partitions. Do not
infer that disabling GRPO std normalization alone reproduces Dr.GRPO.

## Pinned source evidence

- [verl/experimental/agent_loop/agent_loop.py](https://github.com/verl-project/verl/blob/00cd5b44ec59b46a5d3ece5f9da41fdb01b890a8/verl/experimental/agent_loop/agent_loop.py) — AgentLoopOutput: prompt/response IDs, response mask, logprobs, tensor conversion.
- [verl/experimental/agent_loop/tool_agent_loop.py](https://github.com/verl-project/verl/blob/00cd5b44ec59b46a5d3ece5f9da41fdb01b890a8/verl/experimental/agent_loop/tool_agent_loop.py) — ToolAgentLoop: assistant and tool-context merges, turn/length termination.
- [verl/trainer/ppo/core_algos.py](https://github.com/verl-project/verl/blob/00cd5b44ec59b46a5d3ece5f9da41fdb01b890a8/verl/trainer/ppo/core_algos.py) — compute_grpo_outcome_advantage and agg_loss: grouping and reduction.
- [verl/trainer/ppo/rollout_corr_helper.py](https://github.com/verl-project/verl/blob/00cd5b44ec59b46a5d3ece5f9da41fdb01b890a8/verl/trainer/ppo/rollout_corr_helper.py) — correction weights, rejection and bypass mode.
