# Async rollout and training/inference mismatch

## Name the four policies

| Symbol | Meaning | Typical stored quantity |
|---|---|---|
| mu | Behavior distribution that sampled a token | rollout logprob, generation version |
| pi_old | Fixed proximal policy for the update | old/prox logprob, recomputation version |
| pi_theta | Policy being optimized | differentiable current logprob |
| pi_ref | Reference for a regularizer | reference logprob |

In ordinary synchronized PPO, behavior and old policy can coincide. A decoupled
trainer may recompute old/prox logprobs under another snapshot or backend. This
is a deliberate estimator choice when paired with appropriate correction, not
inherently an implementation error. Do not overwrite the only behavior record.

At a sampled action and its recorded history:

`r_update = exp(log pi_theta - log pi_old)`

`w_behavior = exp(log pi_old - log mu)`

Unclipped, their product is `pi_theta / mu`. PPO clipping acts on the update ratio;
TIS-style correction truncates a behavior weight. Neither replaces the other.
Weights used as sampling corrections are normally stop-gradient; confirm the
chosen implementation. Token-local truncated weights do not constitute exact
unbiased sequence/state-distribution importance sampling for an entire episode.

Check whether engine logprobs describe the raw model softmax or the actual
sampling distribution after temperature/top-k/top-p. If support was truncated,
a model-softmax ratio alone cannot recover actions that were never sampled.

## Timeline and partial rollout

```text
rollout: snapshot 10 -> turn 1 -> tool wait -> snapshot 11 -> turn 2
trainer:                 update 11             update 12 -> consume episode
```

One episode-level generation version cannot describe both turns. Either pin the
episode to one snapshot or retain version and behavior logprobs per generation
span (per token when interruptions can occur inside a generation). Queue depth
is not policy lag: measure lag against the relevant consumed model version.

Persist accepted/in-flight/consumed IDs around restart. Do not replay an already
consumed episode by accident, or let resumed partial work appear freshly sampled.

## Diagnosis in order

1. Validate actual tokens, contexts, masks, logprob convention, and model versions.
2. Compare rollout versus trainer at fixed weights to isolate implementation
   mismatch from temporal staleness. Precision and MoE routing can still differ.
3. Inspect lag distribution, log-ratio quantiles, correction/clip fractions,
   effective sample size, and rejection rate by task and length.
4. Bound queue admission and refresh latency; compare a synchronous baseline
   only if an experiment is authorized.
5. Apply the estimator's correction and record bias/variance tradeoffs. There
   is no universal safe maximum ratio. Switching to a critic-free algorithm
   does not itself remove off-policy bias.

Router replay can align selected experts but does not by itself align all
numerical kernels, sampling distributions, or input histories.

## Code evidence

[slime](../implementations/slime.md) separates TIS from policy loss;
[veRL](../implementations/verl.md) has correction and bypass paths;
[AReaL](../implementations/areal.md) has proximal-logprob choices and a staleness
manager. These source snapshots were inspected, not benchmarked against one another.
