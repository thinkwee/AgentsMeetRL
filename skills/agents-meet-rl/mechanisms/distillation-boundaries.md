# OPD / OPSD: teacher and student boundaries

Names and objectives vary across projects. Read the actual sampling and loss path
before equating on-policy distillation, self-distillation, and RL with a teacher
reward. This page specifies a design/audit procedure; it does not establish a
current capability matrix for all corpus projects.

## Conditional inputs

Let the student sample `y ~ pi_student(. | x)`. A privileged teacher may score
those same response tokens under `q(. | x, h)`, where h is a reference answer,
successful peer, or other teacher-only hint. Preserve the student's actual x and
y. Do not place h in student prompts, sample tokens, cached history, or evaluation
inputs. A same-checkpoint teacher with extra context is still a different
conditional distribution; record whether teacher parameters are frozen or updated.

For sampled tokens, `log pi_student(y_t | x,y_<t) - log q(y_t | x,h,y_<t)`
is a log-ratio statistic. Its appearance in a detached advantage, a differentiable
KL, or another surrogate yields different gradients. A full-distribution KL,
top-k approximation, and one sampled-token score are not interchangeable losses.
Record direction, temperature, reduction, stop-gradient choices, and support.

## Alignment and leakage audit

- Teacher prefixes may have different lengths. Align by the exact student response
  IDs and target offsets, not by absolute teacher sequence position.
- If tokenizers/vocabularies differ, sampled-token logprobs cannot be subtracted
  directly; an explicit sequence/distribution mapping is needed.
- Tool observations remain conditioning context. Mask non-generated tokens in
  student policy terms and teacher-derived action scores consistently.
- Build a sentinel hint fixture and verify it exists only in teacher requests.
  Check student inputs before and after serialization and sample conversion.
- Separate RL reward, teacher score, KL, and their weighted contributions in logs.
  Compare RL-only, distillation-only, and combined training at matched budgets
  before attributing improvement to a component.

See the corpus [self-evolution catalogue](../references/self-evolution.md) for
project discovery. The [slime card](../implementations/slime.md) confirms a teacher
logprob data field only; it does not prove a privileged-context OPSD integration.
