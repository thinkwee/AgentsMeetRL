# Environment and Agent runtime

Treat the environment as part of the training distribution. Record tool schemas,
parser, sandbox image, environment revision, and the observations actually seen.
This is an interface design checklist, not a claim that all frameworks implement it.

## State and event contract

A reset establishes a fresh task state and seed. An action produces an observation,
status, and optional reward components. Distinguish:

- Task terminal success or failure: the task actually ended.
- Budget truncation: max turns/tokens/time reached without a task terminal.
- Tool-level failure: visible observation such as invalid arguments; may be part
  of the task the policy should learn to recover from.
- Infrastructure failure: unavailable worker or lost sandbox; do not silently
  turn it into a semantic task failure without declaring that evaluation policy.

With a critic, truncation may require a bootstrap value for a valid continuation
state. With outcome-only GRPO, decide explicitly whether an incomplete attempt
is scored, rejected, or resumed. Neither choice is universally correct.

## Tool lifecycle

Assign call IDs and capture arguments, output, latency, retry count, and state
revision. Preserve model-visible result order for parallel calls. Bound output
size with an explicit truncation event rather than silently altering history.
A retry after a lost response may repeat an already executed side effect: use
idempotency keys or query the resulting state before retrying.

Reset filesystem/database/session state between independent attempts. Share a
cache only if its contents cannot leak another attempt's state or answers.
Close resources on success, exceptions, cancellation, and budget exhaustion.
For executable code, use resource/time/network controls matching the task.

## Verification cases

Use a deterministic fake tool to test success, parse failure, timeout before
execution, lost response after execution, out-of-order parallel completion, and
cancelled episodes. Verify both the visible observation and the final validity
classification. See [the integration recipe](../recipes/tool-agent-integration.md)
and existing [environment failures](../problems/training/env-flakiness.md).
