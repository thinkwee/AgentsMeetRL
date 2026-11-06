# Offline inspection before a training run

Start with one real successful trajectory and one failure, exported via an adapter
from the framework's native dump. The checker consumes a diagnostic JSONL schema,
not a native slime/veRL/AReaL format. It does not repair or retokenize samples.

Each line has `sample_id`, `episode_id`, `group_id`, `end_reason`, and equal-length
arrays `token_ids`, `origins`, `loss_mask`, `behavior_logprobs`, `policy_versions`.
Allowed origins: `context`, `assistant`, `tool`, `padding`. All arrays are aligned
to **target tokens**, before a backend-specific next-token shift. For this checker,
all sampled assistant targets are selected; use context for inserted markers.
Masked logprobs/versions may be null; selected values must be finite/nonempty.
An optional `attention_mask` selects valid positions. End reasons are `terminal`,
`truncated`, `tool_error`, or `infrastructure_error`. Explain native-to-diagnostic
mapping rather than relabeling failures to pass checks.

```bash
python scripts/check_trajectory.py /path/to/export.jsonl
python scripts/check_trajectory.py --demo
```

The demo checks a synthetic multi-turn fixture and hand-computed reduction/ratio
examples. It proves neither native adapter correctness nor training quality.
For real data, also compare exported IDs to learner tensors, validate masks at the
loss boundary, and inspect the original model-visible messages. The script cannot
infer whether a token was genuinely sampled or whether a tool output leaked an answer.

For a fixed batch, compute token-mean and sequence-mean results by hand, then compare
the learner under different microbatch partitions. Keep old/behavior logprobs fixed
while changing current logprobs to distinguish update clipping from correction.
Log per-component rewards before normalization and rejected-attempt counts; compare
quality on the same evaluation tasks using task-level paired uncertainty estimates.
