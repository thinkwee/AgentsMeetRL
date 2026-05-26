# Problem: outputs collapse to very short answers

## Symptoms

- `mean_response_length` decreases over training.
- Model emits 1-token "Yes"/"No" or single-word answers regardless of
  prompt complexity.
- Reward stays high because the trivial answer happens to match common
  ground truth (e.g. "True" / yes-no QA).

## Root causes

1. **Eval set has many trivially-short ground truths** and the model
   exploits this.
2. **No length floor in the reward.** Short answers get full credit when
   correct; long ones get same credit + cost.
3. **Token-level loss without length normalization** — short rollouts
   contribute small loss per rollout but per-token loss is comparable;
   if the gradient prefers being-correct-fast, length collapses.
4. **Format reward rewards `<answer></answer>` with bare answer**, no
   reasoning required.

## Diagnosis

- Plot length distribution by prompt difficulty bucket. Hard prompts
  should produce longer outputs; if they don't, the model is taking
  shortcuts.
- Compare length on easy vs hard prompts. If both are short, length
  collapse is real.

## Fixes

### Fix 1: require thinking content

Make `<think>...</think>` mandatory and gate format reward on non-empty
thinking.

> **Search-R1** — github: `https://github.com/PeterGriffinJin/Search-R1`,
> paper: `https://arxiv.org/abs/2503.09516`, org: UIUC/Google, date: 2025.3.
> Why: format reward gates on non-empty `<think>` block.

> **ReTool** — github: `https://github.com/ReTool-RL/ReTool`,
> paper: `https://arxiv.org/abs/2504.11536`, org: ByteDance, date:
> 2025.4. Why: enforces structured think/tool-call/answer with hard
> reward gating.

### Fix 2: include reasoning in outcome reward

Some tasks reward the *process*, not just the final answer. If yours
allows it, score thinking chain quality (with LLM-judge or PRM).

### Fix 3: distill long-form CoT into SFT

If the model never produces long reasoning, RL won't teach it. Cold-
start SFT on long-CoT data.

### Fix 4: reward calibration on hard prompts

Filter training set to non-trivial prompts (those needing > 50 tokens
of reasoning). Easy yes/no prompts hide the problem.

## Note

Length collapse is rarer than length blow-up in this corpus. When you
see it, it's usually a reward-spec issue (no penalty for wrong
trivially-short answers, or the eval set is too easy).

## Paper / repo references

> **RAGEN** — github: `https://github.com/RAGEN-AI/RAGEN`,
> paper: `https://arxiv.org/abs/2504.20073`, org: RAGEN-AI, date: 2025.4.
> Why: StarPO documents the dual failure mode where models collapse
> either to trivially-short answers or over-long ones — both fall under
> the same template/mode collapse umbrella.

> **Skywork-OR1** — github: `https://github.com/SkyworkAI/Skywork-OR1`,
> paper: `https://arxiv.org/abs/2505.22312`, org: Skywork AI, date: 2025.5.
> Why: large-scale rule-based RL with strict format gating that
> prevents trivial-answer reward hacking.
