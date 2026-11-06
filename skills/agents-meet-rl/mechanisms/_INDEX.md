# Engineering mechanisms

Read only the topic needed for the question. These are engineering explanations,
not claims of measured training improvements. Source-backed implementation details
are versioned in [implementation cards](../implementations/_INDEX.md).

| Question | Topic |
|---|---|
| How does an episode become training samples? | [Trajectory contract](trajectory-contract.md) |
| Which tokens get loss, attention, and logprobs? | [Token and mask alignment](token-mask-alignment.md) |
| What objective does splitting/reducing a trajectory implement? | [Multi-turn objectives](multi-turn-objectives.md) |
| Which policy is in each ratio? How do async and partial rollouts work? | [Async and mismatch](async-and-mismatch.md) |
| How should tools, termination, retries, and sandboxes behave? | [Environment runtime](environment-runtime.md) |
| What changes when rewards or filtering change? | [Reward and selection](reward-and-selection.md) |
| How do teacher-only hints enter OPD/OPSD? | [Distillation boundaries](distillation-boundaries.md) |
| What must survive compaction, replay, evaluation, and resume? | [Long-horizon evaluation](long-horizon-evaluation.md) |
