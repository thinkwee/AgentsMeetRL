# Problem: I want a process reward model (PRM) — how do I train one?

## When you actually want a PRM

- Outcome reward is too sparse (most rollouts get 0). See
  `sparse-reward-credit.md`.
- Long-horizon trajectories where credit needs to flow back to specific
  steps. See `credit-assignment-long-horizon.md`.
- Tool-use where intermediate calls have value beyond final answer.
- You have, or can generate, labelled intermediate states.

## When you DON'T want a PRM

- You can use info-gain reward instead (no labelling needed).
- Outcome verifier is cheap and reliable (math, code, exact match).
- You can't audit the PRM — it'll go stale fast.

## Recipes from the corpus

### Recipe 1: PRM trained from MCTS rollouts

> **MASPRM** — github: `https://github.com/milad1378yz/MASPRM`,
> paper: `https://arxiv.org/abs/2510.24803`, UBC/Huawei, date: 2025.10.
> PRM trained from MCTS rollouts. Use when you can run MCTS on training
> tasks (the labels come for free from MCTS visit counts / win rates).

> **ReasonRAG** — github: `https://github.com/wlzhang2020/ReasonRAG`,
> paper: `https://arxiv.org/abs/2505.14069`, CityU HK / Huawei, date: 2025.5.
> DPO + MCTS-based PRM for multi-hop QA.

> **AgentRM** — github: `https://github.com/thunlp/AgentRM`,
> paper: `https://arxiv.org/abs/2502.18407`, THUNLP, date: 2025.2.
> Generalizable regression PRM across 9 agent tasks; trained as a
> single model that transfers across ALFWorld/WebShop/SciWorld/etc.

### Recipe 2: PRM as PPO reward signal

> **AgentPRM** — github: `https://github.com/sanjibanc/agent_prm`,
> paper: `https://arxiv.org/abs/2502.10325`, Cornell, date: 2025.2.
> PPO/DPO + PRM template. Reference for ALFWorld and general agents.

### Recipe 3: Progress reward (ProgRM)

Train the model to score "how much closer is this state to success."

> **AgentProg** — github: `https://github.com/MobileLLM/AgentProg`,
> paper: `https://arxiv.org/abs/2505.18121`, MobileLLM, date: 2025.5.
> ProgRM for GUI agent training.

### Recipe 4: Atomic-thought reward

Score per-thought reward.

> **Atom-Searcher / Research-Venus** — github:
> `https://github.com/antgroup/Research-Venus`,
> paper: `https://arxiv.org/abs/2508.12800`, Ant Group, date: 2025.8.
> Atomic-thought reward for deep research.

### Recipe 5: Step search PRM

> **StepSearch** — github: `https://github.com/Zillwang/StepSearch`,
> paper: `https://arxiv.org/abs/2505.15107`, SenseTime, date: 2025.5.
> Process reward via a learned model on QA-search.

## PRM training data sources

- **MCTS rollouts** (MASPRM, ReasonRAG): outcome-aware labels per step.
- **Distill from a stronger teacher**: ask GPT-4 to score steps; train
  PRM to match. Cheap, biased.
- **Self-generated**: rollouts from an early policy + outcome reward
  back-propagated as approximate per-step labels.
- **Human annotation**: gold standard, expensive, slow.

## Validation: don't skip

A PRM that's wrong on held-out data will pollute your RL training.
Validate before integrating.

> **ToolPRMBench** — github: `https://github.com/David-Li0406/ToolPRMBench`,
> paper: `https://arxiv.org/abs/2601.12294`, Arizona State, date: 2026.1.
> A benchmark to evaluate PRMs in tool-use specifically. Use it.

## Common PRM pitfalls

1. **PRM goes stale.** Policy improves past PRM's training distribution.
   Refresh on recent rollouts every N steps.
2. **PRM scores correlate with length / formality, not quality.** Same
   pitfalls as LLM-judge. See `llm-judge-pitfalls.md`.
3. **Policy learns to game the PRM.** Same pattern as reward hacking
   on outcome reward. Audit by reading rollouts.
4. **PRM weight too high.** PRM signal should be auxiliary, not
   replace outcome. Use curriculum to fade it out.
5. **PRM disagrees with outcome.** When this happens persistently on
   rollouts that *did* succeed, retrain.

## Curriculum: fade out PRM as outcome variance grows

When outcome reward starts producing useful signal, reduce PRM weight.
This is the IGPO pattern (info-gain → outcome curriculum):

```bash
# IGPO/train.sh
+algorithm.curriculum_ig_init=1.0
+algorithm.curriculum_ig_final=0.5
+algorithm.curriculum_f1_init=0.5
+algorithm.curriculum_f1_final=1.0
```

Apply the same shape to PRM weights.

## Paper / repo references

(All cited above.)
