# Problem: LLM-judge gives different scores each run

## When you're using LLM-judge for evaluation (not training)

This is a sibling of `../training/llm-judge-pitfalls.md` but eval-specific.

## Symptoms

- Same rollout judged twice gets different scores.
- Method A scores higher than B with judge X, but lower with judge Y.
- Reviewer asks why your judge is the right choice.

## Mitigations

### Use ensemble of judges

Average over 2-3 judges from different families. Standard for
high-stakes eval.

### Report inter-judge agreement

Cohen's κ or Fleiss' κ across judges. > 0.6 = decent. < 0.4 = your
judges disagree, results aren't trustworthy.

### Pre-register the judge

Don't switch judge after seeing results.

### Use rubric-style judging

Specific rubric > zero-shot "is this good?". Lower variance.

### LLM-judge + verifier hybrid

Score = LLM-judge score, but only counted if rule-based verifier also
passes.

> **CompassVerifier** — github:
> `https://github.com/open-compass/CompassVerifier`, Shanghai AI Lab,
> date: 2025.7. Reasoning verification.

### Run multiple times, report variance

Just judge each example 3 times; report mean ± std as part of eval.
Most papers don't.

### Different judge family from policy

If your policy is Qwen-based, a Qwen judge will be biased. Use Claude
or GPT judge.

### Length-normalized judge prompt

```
Evaluate the answer for {criterion}. Score 0-10.
Ignore length, formality, and verbosity — score only on {what matters}.
```

Helps but doesn't eliminate length bias.

## Calibration

Run the judge on a held-out set with known correct/incorrect labels.
Report:

- Accuracy (judge agrees with ground truth).
- False-positive rate (judge says correct, actually wrong).
- False-negative rate.

If accuracy < 80%, your judge is too noisy.

## What papers do

- **DR Tulu** uses evolving rubrics —
  `https://github.com/rlresearch/dr-tulu`,
  paper: `https://arxiv.org/abs/2511.19399`. Rubrics adapt; judge stays
  fresh.
- **calculator_agent_rl** uses Claude as judge with explicit rubric —
  `https://github.com/Danau5tin/calculator_agent_rl`. Small, clean.
- **VisionThink** discusses judge bias in VQA —
  `https://github.com/dvlab-research/VisionThink`,
  paper: `https://arxiv.org/abs/2507.13348`.

## When NOT to use LLM-judge

- Tasks with closed-form verification — rule-based is better.
- Tasks where the policy and judge are from same model family.
- High-stakes deployment scoring — LLM-judge is for *training* signal;
  *evaluation* needs human or verifier grounding.

## See also

- `../training/llm-judge-pitfalls.md` — same issues during training.
- `reproducibility.md` — judge model version drift.
