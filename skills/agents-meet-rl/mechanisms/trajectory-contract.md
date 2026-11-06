# Trajectory to training sample

## Three units that must not be conflated

An **episode** is one task attempt in an environment. A **turn** is one model
generation followed by zero or more environment events. A **training sample** is
a tensor sequence consumed by the learner. One episode may produce several samples.
A GRPO **group** contains comparable attempts at the same starting task/state;
it is not the set of turns within one attempt.

Preserve these logical fields through framework adapters (names need not match):

| Field | Meaning and invariant |
|---|---|
| task_id, group_id, episode_id, sample_id | Task, comparison group, attempt, and training-row identities |
| parent/branch IDs, turn index | Recover causality when branching or splitting |
| input token IDs and generated spans | Actual generation history, including tool observations |
| loss mask, attention/segment information | Training targets versus visible context; packing boundaries |
| behavior logprobs and version per generated span | Probability provenance, including changes within an episode |
| reward components and final training score | Keep task success distinct from shaping and penalties |
| end reason and validity | Success/failure, budget truncation, or infrastructure error |
| tokenizer/template/environment revisions | Reconstruct the conditional inputs |

## Two valid representations, different hazards

**Concatenated:** `[prompt, assistant1, tool1, assistant2]`, with loss on the two
assistant spans. This is valid only if the second generation really conditioned
on that token prefix. Rendering the full conversation again may change it.

**Per-turn:** sample 1 is `[prompt, assistant1]`; sample 2 is
`[actual second prompt, assistant2]`. In sample 2, historical assistant1 is context,
not a second training target. Store its own actual prompt if memory compaction or
non-prefix templates changed history. Preserve episode identity for reduction.

Splitting a ten-turn episode into ten equally weighted rows makes it contribute
more than a one-turn episode under row-mean aggregation. Define episode weights
before splitting; see [objectives](multi-turn-objectives.md). Repeating terminal
reward on rows is not automatically a new per-turn reward.

## Boundary checks

- Join parallel tool results by call ID, not completion order. Persist the order
  actually shown to the model; do not reorder for training.
- Every trained token has exactly one owning generation, its input context, and
  probability provenance. Detect duplicate targets across split samples.
- Tool timeouts are distinguishable from task failure. Record dropped attempts
  and why, including attempts rejected before tensor construction.
- A truncated prefix is not automatically a completed episode or a terminal
  zero-value state. Bootstrap semantics depend on the estimator and task.

## Implementation evidence

See [slime](../implementations/slime.md), [veRL](../implementations/verl.md), and
[AReaL](../implementations/areal.md) for concrete native fields. The logical
contract above is a proposed diagnostic model, not a universal framework API.
