# Rewards, filtering, and the selected distribution

## Keep three quantities

Persist raw task reward, individual shaping/penalty components, and the final
training score after scaling/clipping/normalization. Evaluation should expose task
success and costs separately; a higher shaped score is not necessarily better
agent behavior. Version the judge prompt/model, rubric, and tool harness.

Use a declared formula, for example `score = task + alpha*format - beta*cost`,
with calibrated component ranges. A universal percentage for format reward is
not justified: inspect whether a failed task can outscore a successful one.
Avoid paying repeatedly for redundant calls or rewarding the presence of an
answer/evidence string without checking its validity.

## Selection changes what is learned

With acceptance probability a(x), accepted tasks follow
`p_selected(x) proportional to p_original(x)*a(x)`. Filtering all-fail groups,
long tasks, timeouts, or stale episodes changes this distribution. Log acceptance
rates by task family, difficulty, length, and failure reason against **all
attempted** tasks, not just the surviving batch.

A zero-variance outcome-GRPO group supplies zero centered outcome advantage.
Whether to keep, resample, or curriculum-filter it depends on cost and objective;
report effective groups and generated-token cost, not just accepted samples.
Removing the standard deviation denominator does not restore information in an
all-identical reward group.

## Judge and process rewards

Use a frozen labeled audit set with positive, negative, and adversarial examples.
Measure agreement/error slices, not only judge repeatability. Blind checkpoint
identity and keep train/eval judge revisions explicit. Process rewards can improve
credit resolution but can also teach a proxy; validate final outcomes independently.
Information-gain rewards require a precise scoring model and conditioning setup;
they are not universally available or leakage-free.

See [reward mixing](../problems/training/reward-mixing.md),
[zero variance](../problems/training/zero-variance-rollouts.md), and
[long-horizon evaluation](long-horizon-evaluation.md).
