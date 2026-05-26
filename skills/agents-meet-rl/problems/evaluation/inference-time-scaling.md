# Problem: should I do best-of-N / tree search / self-consistency?

## Decision tree

```
Cheap eval, low-stakes?               → pass@1 (T=0). Done.
Verifiable reward, moderate budget?   → maj@k (k=8 or 16).
Have a reward model / PRM?            → best-of-N with RM.
Long-horizon agentic, hard task?      → tree search / MCTS.
Long-form open-ended?                 → maj@k or LLM-judge ensemble.
```

## Patterns

### Self-consistency (maj@k)

Sample k rollouts, take majority answer. Cheap variance reduction.
Standard for math.

```
T=0.7 → sample 8 rollouts → vote → final answer
```

### Best-of-N with RM

Sample N, score each with RM, return highest.

> **AgentRM** — github: `https://github.com/thunlp/AgentRM`,
> paper: `https://arxiv.org/abs/2502.18407`, THUNLP, date: 2025.2.
> Trained for this exact use case.

### Tree search / MCTS

Expand promising rollout paths.

> **MASPRM** — github: `https://github.com/milad1378yz/MASPRM`,
> paper: `https://arxiv.org/abs/2510.24803`, UBC/Huawei, date: 2025.10.
> PRM trained from MCTS rollouts.

> **ReasonRAG** — github: `https://github.com/wlzhang2020/ReasonRAG`,
> paper: `https://arxiv.org/abs/2505.14069`, CityU HK / Huawei, date: 2025.5.
> MCTS-based PRM at training; can also be used at eval.

> **ProRAG** — github: `https://github.com/lilinwz/ProRAG`,
> paper: `https://arxiv.org/abs/2601.21912`, RUC, date: 2026.1. PRM via
> MCTS for multi-hop RAG.

### Self-search (no external retriever)

Sample multiple search paths internally; pick best.

> **SSRL** — github: `https://github.com/TsinghuaC3I/SSRL`,
> paper: `https://arxiv.org/abs/2508.10874`, Tsinghua, date: 2025.8.

### Test-time interaction

For agents: explicitly let the agent try multiple times with feedback.

> **TTI** — github: `https://github.com/test-time-interaction/TTI`,
> paper: `https://arxiv.org/abs/2506.07976`, CMU, date: 2025.6.
> REINFORCE/BC for test-time interaction.

## Compute trade-off

Inference-time scaling multiplies your eval cost:

- maj@8: 8x compute, +5–10 points typical.
- best-of-32 with RM: 32x compute, +5–15 points typical.
- MCTS: hard to bound (10–100x typical).

Compare your method's pass@1 against a baseline's pass@k under matched
compute budget. Otherwise comparisons are unfair.

## Pitfalls

### Pitfall 1: only reporting maj@k

Hides the underlying pass@1. Report both.

### Pitfall 2: reward model overfits to your policy

A RM trained on your model's rollouts may rate your model unfairly
high. Use RM trained on diverse rollouts.

### Pitfall 3: tree search at eval but not train

If training was rollout-based and eval uses tree search, results aren't
representative of *the trained model's* deployable performance.

## Paper / repo references

(All cited above.)
