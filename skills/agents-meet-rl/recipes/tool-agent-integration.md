# Integrate a multi-turn tool task

Use this recipe with the user's existing framework, model, and launch recipe.
It specifies implementation boundaries, not a universal runnable training command.
Read the matching [implementation card](../implementations/_INDEX.md) first.

1. **Data:** map one training row to a task ID, starting messages, environment
   reset payload, and private scoring metadata. Keep scoring answers out of
   student-visible messages. Declare the evaluation split independently.
2. **Environment adapter:** implement reset/action/cleanup and structured status
   events as described in [runtime](../mechanisms/environment-runtime.md).
3. **Agent loop:** preserve actual request IDs and generation IDs/logprobs;
   resolve calls by ID; append exactly the tool observations seen by the policy;
   terminate on declared task or budget conditions.
4. **Sample adapter:** map the logical [trajectory contract](../mechanisms/trajectory-contract.md)
   to native fields. Choose concatenated or per-turn representation based on
   actual prefix identity, not convenience. Keep episode/group identity.
5. **Reward adapter:** return task score, components, and validity separately;
   convert to the framework's scalar training reward only at its documented hook.
6. **Loss wiring:** explicitly record estimator, normalization, reduction, masks,
   old/behavior logprob source, correction, and handling of incomplete attempts.
7. **Verification:** exercise deterministic fake tools, inspect one successful and
   one failed trajectory, check masked loss on a tiny fixed batch, then run a
   single update only within the user's authorized experiment scope.

An integration is reviewable when it includes the adapters, a representative
serialized fixture, the concrete launch configuration, and expected observations.
A job reaching RUNNING is not proof: show consumed samples, finite loss/gradients,
a changed student checkpoint, and teacher/reference immutability where required.
