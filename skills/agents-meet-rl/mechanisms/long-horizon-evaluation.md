# Long-horizon state, evaluation, and restart

## Compaction and branching

Compaction changes the policy's observed state. Store the exact compacted prompt
for the next generation, its source-event span, and compactor revision. Training
on an uncompressed reconstruction scores a different conditional policy. Do not
count a generated summary as an agent action unless it belongs to the objective;
if another model generated it, record that provenance.

Branches share prefixes and environment snapshots. Track branch IDs, state
revisions, and target ownership to avoid counting shared actions multiple times.
Replay from an old policy is off-policy data even when the environment is exactly
reproducible. See [async correction](async-and-mismatch.md).

## Evaluation protocol

Fix task split, model/template, environment and tool versions, sampling parameters,
max tokens/turns, retry rules, and inference-time selection budget. Report task
success, infrastructure failures, tool cost, tokens, and latency separately.
Do not compare pass@1 against best-of-N, or silently exclude timeouts from one
system's denominator. If exclusions are necessary, report their counts and policy.

For paired comparisons, use the same tasks and compatible seeds/environment
snapshots. Bootstrap or otherwise estimate uncertainty over independent task
units; turns and multiple attempts from one task are not independent tasks.
A confidence interval crossing zero does not establish an improvement.

## Resume contract

Checkpoint model/optimizer/scheduler and RNG state, data cursor, group assignment,
queue/consumption ledger, policy versions, reward/teacher revisions, and any
reusable environment state. If in-flight work cannot be restored, invalidate it
explicitly. Recreated tools with different state are not an exact continuation.

Validation has distinct levels: serialized fixture checks; one complete training
update; restart continuity; and independent quality evaluation. Passing one does
not imply the next. See [reproducibility](../problems/evaluation/reproducibility.md)
and [statistical significance](../problems/evaluation/statistical-significance.md).
