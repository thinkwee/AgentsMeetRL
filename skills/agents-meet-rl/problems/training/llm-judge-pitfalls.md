# Problem: LLM-as-judge reward is inconsistent / biased / drifts during training

## Symptoms

- Same rollout, judged twice, gets different scores (test-retest
  variance high).
- Train reward climbs but eval doesn't — see `reward-up-eval-flat.md`.
- Reward correlates with response length, formality, or specific phrases
  rather than correctness.
- After many training steps, judge keeps giving high scores to outputs
  that look subtly wrong on inspection.
- New version of judge model gives totally different scores.

## Root causes

1. **Judge variance.** LLMs are stochastic; a single judge call has
   noise.
2. **Length bias.** Most LLM judges prefer longer answers.
3. **Position bias.** When judging "A vs B," the position of A or B
   affects the score.
4. **Family bias.** Judge from same family as policy underrates other
   families' style.
5. **Drift over training.** The policy learns the judge's biases, not
   the task. Same judge, growing reward, no real improvement.
6. **Static rubric in a dynamic task.** Rubric was right at step 0;
   doesn't capture what "good" means after step 5000.
7. **Prompt-injection by policy.** Policy learns to inject text the
   judge interprets as "high score."

## Diagnosis

### Test-retest variance

Run the same judge on the same 100 rollouts, twice. Compute
score-correlation. Healthy ≥ 0.8. < 0.6 = high variance, fix or replace.

### Length bias check

Plot judge score vs response length on held-out set. Spearman ρ should
be < 0.3. > 0.5 = strong length bias.

### Cross-judge agreement

Re-judge a held-out batch with a *different* judge family. If
disagreement rate is > 30% on near-threshold cases, you have judge-
specific biases.

### Drift check

Save 500 step-0 rollouts (before any RL training). Re-judge them at
step 500, 1000, 2000 *with the same judge*. Scores should be stable.
If scores drift up, either you have a prompt issue or the judge is
giving different scores to historical data.

## Fixes

### Fix 1: ensemble / cross-judge

Average over 2-3 judges from different families (e.g.
GPT-4o + Claude-Sonnet + Qwen). Cuts variance significantly. Costs
3× compute but is worth it if the signal is otherwise unusable.

> **calculator_agent_rl** —
> github: `https://github.com/Danau5tin/calculator_agent_rl`. Uses
> Claude as judge with explicit rubric; small clean reference.

### Fix 2: evolving rubrics

The rubric updates as the model improves. Rubric staleness is the
machine's problem, not yours.

> **DR Tulu** —
> github: `https://github.com/rlresearch/dr-tulu`,
> paper: `https://arxiv.org/abs/2511.19399`, AI2/UW/CMU/MIT, date: 2025.5.
> Long-form deep research with rubric evolution.

### Fix 3: rule-based + LLM-judge blend

Even if main signal is LLM-judge, mix in:

- Rule-based format floor (small weight).
- Rule-based length normalization or cap.
- Domain rule (citation present, code compiles, etc.).

This prevents judge biases from dominating.

### Fix 4: use a trained reward model instead of zero-shot judge

When you can afford it, train a reward model on a curated preference
dataset. More stable than zero-shot judging but requires upfront
investment.

> **Agentic-Reward-Modeling** — github:
> `https://github.com/THU-KEG/Agentic-Reward-Modeling`,
> paper: `https://arxiv.org/abs/2502.19328`, THU-KEG, date: 2025.2.
> Reward Agent with verification.

### Fix 5: verifier-grounded judge

Judge contributes only when the answer matches some external
verifier (e.g., domain-specific tool). Otherwise outcome reward is 0.

> **CompassVerifier** —
> github: `https://github.com/open-compass/CompassVerifier`,
> Shanghai AI Lab, date: 2025.7. Reasoning verification benchmark and
> tooling.

### Fix 6: explicit length normalization in the prompt

When judging open-ended answers, instruct the judge to ignore length:

```
Evaluate this answer for {criterion}. Score 0-10.
Ignore length, formality, and verbosity — score only on whether the
answer is correct and complete.
```

Helps but doesn't eliminate length bias entirely.

### Fix 7: position-randomization for pairwise

If you do pairwise judging (A vs B), randomize position. Helps with
the pairwise position bias inherent to GPT-style judges.

### Fix 8: VisionThink-style efficient VQA pattern

> **VisionThink** —
> github: `https://github.com/dvlab-research/VisionThink`,
> paper: `https://arxiv.org/abs/2507.13348`, CUHK, date: 2025.7.
> Reports judge-bias issues for VQA + offers patterns to mitigate.

## When NOT to use LLM-judge

- Tasks with closed-form verification (code, math, exact-match QA). Use
  rule-based.
- Tasks where the judge would be the same as the policy family. Don't
  let the model judge itself.
- High-stakes deployment scoring. LLM-judge is fine for *training*
  signal; *evaluation* should also have human or verifier grounding.

## Paper / repo references

- `DR Tulu` — github: `https://github.com/rlresearch/dr-tulu`,
  paper: `https://arxiv.org/abs/2511.19399`, AI2/UW/CMU/MIT, date: 2025.11.
- `Agentic-Reward-Modeling` — github:
  `https://github.com/THU-KEG/Agentic-Reward-Modeling`,
  paper: `https://arxiv.org/abs/2502.19328`, THU-KEG, date: 2025.2.
- `CompassVerifier` — github:
  `https://github.com/open-compass/CompassVerifier`,
  Shanghai AI Lab, date: 2025.7.
- `VisionThink` — github: `https://github.com/dvlab-research/VisionThink`,
  paper: `https://arxiv.org/abs/2507.13348`, CUHK, date: 2025.7.
- `GuardReasoner-VL` — github:
  `https://github.com/yueliu1999/GuardReasoner-VL`,
  paper: `https://arxiv.org/abs/2505.11049`, NUS, date: 2025.5.
