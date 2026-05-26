# Problem: outcome reward is too sparse — most rollouts get 0

## Symptoms

- > 70% of rollouts have reward = 0; the rest are scattered.
- GRPO advantage is mostly zeros (no within-group variance) — see
  `zero-variance-rollouts.md` for the GRPO-specific symptom.
- Training is slow, and most prompts contribute no gradient.
- The model collapses to "safe" trivial outputs early because the
  exploration budget rarely succeeds.

## Root causes

1. **Task is genuinely hard at the model's current level.** No partial
   reward = no learning gradient.
2. **Reward is binary by design** (e.g. SWE-bench pass/fail).
3. **Cold-start (SFT) was insufficient** — the policy can't reach reward
   territory from scratch.

## Diagnosis trees

```
Most rollouts get 0?
├── Did SFT cold-start match the RL distribution?
│   └─ No → fix SFT first, before changing reward.
├── Are some prompts always-zero? (filter those out)
│   └─ Yes → curriculum / filter unsolvable prompts.
└── Is your task long-horizon?
    └─ Yes → add per-turn info-gain or PRM signal.
```

## Fixes

### Fix 1: stronger SFT cold-start

Long-horizon agentic-RL almost never works from a non-instruct base
without SFT. Most papers in the corpus do **multi-stage** SFT:

> **Tool-Star** — github: `https://github.com/dongguanting/Tool-Star`,
> paper: `https://arxiv.org/abs/2505.16410`, RUC, date: 2025.5.
> Multi-stage SFT before RL.

> **MobileRL** — github: `https://github.com/THUDM/MobileRL`,
> paper: `https://arxiv.org/abs/2509.18119`, THUDM, date: 2025.9.
> Three-stage: SFT → offline RL → online RL.

> **Mano-P** — github: `https://github.com/Mininglamp-AI/Mano-P`,
> paper: `https://arxiv.org/abs/2509.17336`, Mininglamp AI, date: 2025.9.
> Same SFT → offline → online pipeline for OSWorld.

> **MedResearcher-R1** — github: `https://github.com/AQ-MedAI/MedResearcher-R1`,
> paper: `https://arxiv.org/abs/2508.14880`, Ant Group AQ-MedAI, date: 2025.8.
> SFT + Online RL.

> **Doctor-R1** — github: `https://github.com/thu-unicorn/Doctor-R1`,
> paper: `https://arxiv.org/abs/2510.04284`, Tsinghua, date: 2025.10.
> Experiential agentic RL after SFT.

### Fix 2: per-turn information-gain reward

Even when outcome is 0, info-gain reward gives signal across turns.

> **IGPO** — github: `https://github.com/GuoqingWang1/IGPO`,
> paper: `https://arxiv.org/abs/2510.14967`, Ant Group, date: 2025.10
> (ICLR 2026).

> Per-turn reward = log-prob delta of gold answer.

> **DR-Venus** — github: `https://github.com/inclusionAI/DR-Venus`,
> paper: `https://arxiv.org/abs/2604.19859`, Ant Group, date: 2026.4.
> IGPO scaled to 200+ turn deep research.

> **LegalDelta** — github: `https://github.com/NEUIR/LegalDelta`,
> paper: `https://arxiv.org/abs/2508.12281`, NEUIR, date: 2025.8.
> CoT-guided info-gain.

### Fix 3: process reward (PRM)

Train a PRM on labelled intermediate states. Use as auxiliary reward.

> **AgentPRM** (`https://github.com/sanjibanc/agent_prm`,
> paper: `https://arxiv.org/abs/2502.10325`).
> **AgentRM** (`https://github.com/thunlp/AgentRM`,
> paper: `https://arxiv.org/abs/2502.18407`).
> **MASPRM** (`https://github.com/milad1378yz/MASPRM`,
> paper: `https://arxiv.org/abs/2510.24803`) — PRM trained from MCTS.
> **AgentProg / ProgRM** (`https://github.com/MobileLLM/AgentProg`,
> paper: `https://arxiv.org/abs/2505.18121`).

### Fix 4: reward shaping into intermediate signals

Add task-specific intermediate signals:

- **SWE-Swiss** — `https://github.com/zhenyuhe00/SWE-Swiss`. Decompose
  into Localization + Repair + Test Generation, each with its own
  reward.
- **Doctor-R1** — clinical inquiry + diagnosis split.
- **CUDA-L1** — `https://github.com/deepreinforce-ai/CUDA-L1`,
  paper: `https://arxiv.org/abs/2507.14111`. Hardware-grounded TFLOPs
  reward gives continuous signal.

### Fix 5: difficulty-curriculum / learnability-sampling

Train preferentially on prompts in the "learnable" zone (success rate
in [0.1, 0.9]).

> **Absolute-Zero-Reasoner** — github:
> `https://github.com/LeapLabTHU/Absolute-Zero-Reasoner`,
> paper: `https://arxiv.org/abs/2505.03335`, Tsinghua, date: 2025.5.
> Learnability weighting in TRR++.

> **R-Zero** — github: `https://github.com/Chengsong-Huang/R-Zero`,
> paper: `https://arxiv.org/abs/2508.05004`, Tencent AI Seattle, date: 2025.8.
> Challenger model generates progressively harder problems for the solver.

> **AdaGRPO** in MobileRL —
> `https://github.com/THUDM/MobileRL`. Difficulty-Adaptive GRPO.

### Fix 6: TTRL / self-consistency-as-reward (no labels)

When you have no labels at all, majority-vote across N rollouts can
provide a noisy reward signal:

> **R-Zero** uses majority-voting reward.
> **MARTI** — github: `https://github.com/TsinghuaC3I/MARTI`,
> Tsinghua, date: 2025.5. Includes TTRL recipe.

### Fix 7: hindsight relabeling / replay buffer

Adapt RL from goal-conditioned RL: when a rollout fails the original
goal, relabel it as succeeding at *what it actually did*. Use as warm
training data. Less common in the LLM corpus (mostly used in robotics)
but applicable.

## Paper / repo references

- All papers above. Most relevant ranking by sparsity severity:
  1. `IGPO` — pure outcome → info-gain; no extra label.
  2. `AgentPRM` / `AgentRM` — train a PRM (needs labelled states).
  3. SFT-first multi-stage — Tool-Star, MobileRL, MedResearcher-R1.
  4. Curriculum / R-Zero / AZR — when even SFT can't get you off zero.
