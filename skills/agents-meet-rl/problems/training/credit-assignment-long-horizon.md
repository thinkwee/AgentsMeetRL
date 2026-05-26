# Problem: 50+ step episodes, single outcome reward — turns get equal credit

## Symptoms

- Episodes are very long (10–200+ turns).
- Final reward is binary (success/failure) or near-binary.
- Learning is slow; the model doesn't seem to "credit" individual turns.
- Specifically: useful early-turn actions don't get reinforced; useless
  late-turn actions don't get punished.
- GRPO on long trajectories effectively trains every turn the same — the
  same scalar advantage broadcasts over all tokens of the rollout.

## Root causes

1. **Trajectory-level reward only**: every turn shares the final scalar
   advantage. The optimizer can't tell which turn earned it.
2. **No per-turn process reward**: even if you wanted to credit
   individual turns, you have no signal.
3. **No discount factor**: if you set γ=1 (or no γ at all), the temporal
   structure is destroyed.
4. **Wrong rollout abstraction**: a single token-stream rollout with all
   turns concatenated obscures the per-turn structure.

## Diagnosis

- For each rollout, plot per-turn observation length vs reward
  contribution. If they're uncorrelated for both successful and failed
  rollouts, credit isn't reaching the right turns.
- Compare success rate at turn $t$ to `advantage at turn $t$`. Should
  correlate. If they don't, your credit scheme is broken.
- Inspect: do failed rollouts have visibly bad steps that the loss is
  *not* punishing more than the good steps?

## Fixes

### Fix 1: hierarchical advantage (GiGPO)

Outer-group advantage across rollouts (standard GRPO). **Inner-group**
advantage across turns within a rollout, by clustering turns that share
the same observation prefix.

> **GiGPO (verl-agent)** — github:
> `https://github.com/langfengQ/verl-agent`,
> paper: `https://arxiv.org/abs/2505.10978`, NTU, date: 2025.5.

Key ideas:

- **Step-discounted return per trajectory** — propagate per-step rewards
  end-to-start with γ.
- **Inner step-grouping** — cluster turns that share the same (or
  similar) observation prefix across rollouts in the same outer GRPO
  group; each cluster becomes an inner step-level group.
- **Two-level advantage** — outer GRPO across rollouts, inner GRPO
  across the step-clusters. Toggle for cross-step normalization.

The recurrence (γ-discounted return, in pseudo-code):

```python
for t in reversed(range(len(traj_rewards))):
    running_return = traj_rewards[t] + gamma * running_return
    traj_returns[t] = running_return
```

### Fix 2: per-turn information-gain reward (IGPO)

Use the policy's log-prob of the gold answer *before vs after* observing
turn $t$ as the per-turn reward. No PRM training data needed.

> **IGPO** — github: `https://github.com/GuoqingWang1/IGPO`,
> paper: `https://arxiv.org/abs/2510.14967`, Ant Group, date: 2025.10
> (ICLR 2026).

Two info_gain modes (configured via `algorithm.info_gain_type`):

- `"log_prob_diff"`: per-turn reward = `log P(answer | history+turn) -
  log P(answer | history)`.
- `"prob_diff"`: same in probability space.

Curriculum is critical: schedule the info-gain weight high early
(when outcome reward is sparse) and decay it as outcome accuracy
improves. IGPO's recipe roughly:

- F1 (outcome) weight: 0.5 → 1.0 over training.
- Info-gain weight: 1.0 → 0.5 over training.

Start info-gain-heavy, end outcome-heavy. The corpus's other long-
horizon papers do the same.

### Fix 3: train a process reward model (PRM) and use PPO

If your task has structured intermediate state (ALFWorld, code states,
tool outputs), a PRM can score each turn directly.

> **AgentPRM** — github: `https://github.com/sanjibanc/agent_prm`,
> paper: `https://arxiv.org/abs/2502.10325`, Cornell, date: 2025.2.

> **AgentRM** — github: `https://github.com/thunlp/AgentRM`,
> paper: `https://arxiv.org/abs/2502.18407`, THUNLP, date: 2025.2.

> **MASPRM** — github: `https://github.com/milad1378yz/MASPRM`,
> paper: `https://arxiv.org/abs/2510.24803`, UBC/Huawei, date: 2025.10.
> PRM trained from MCTS rollouts.

> **AgentProg / ProgRM** — github: `https://github.com/MobileLLM/AgentProg`,
> paper: `https://arxiv.org/abs/2505.18121`, MobileLLM, date: 2025.5.
> Progress reward model.

Caveat: PRM goes stale as policy improves; refresh on recent rollouts.

### Fix 4: choose discount γ < 1 even for outcome-only reward

If you have *any* per-turn signal at all (tool-call validity, format),
γ < 1 propagates credit toward earlier turns. veRL's GAE supports γ
out of the box; the underlying recurrence is the standard:

```python
delta = token_level_rewards[t] + gamma * nextvalues - values[t]
```

For 50+ step rollouts, γ ∈ [0.95, 0.99] is typical.

### Fix 5: switch rollout abstraction so steps are first-class

Token-stream rollouts make per-turn credit hard. A step-based rollout
abstraction stores each (prompt, response) tuple separately and lets you
compute per-step advantages cleanly.

> **verl-agent** — see fix 1.
> **Agent-R1** — github: `https://github.com/0russwest0/Agent-R1`,
> paper: `https://arxiv.org/abs/2511.14460`, org: USTC, date: 2025.11.
> Step-level MDP.
> **SkyRL-Agent** — `https://github.com/NovaSky-AI/SkyRL`,
> paper: `https://arxiv.org/abs/2511.16108`, date: 2025.11.

## When NOT to add per-turn credit

- Episodes ≤ 5 turns and reward already varies — vanilla GRPO is fine.
- Tasks where the "intermediate steps" are essentially noise (any path
  works, as long as you arrive at the answer) — per-turn rewards reinforce
  spurious intermediate behavior.

## Paper / repo references

- `GiGPO` — github: `https://github.com/langfengQ/verl-agent`,
  paper: `https://arxiv.org/abs/2505.10978`, NTU/Skywork, date: 2025.5
  (NeurIPS 2025).
- `IGPO` — github: `https://github.com/GuoqingWang1/IGPO`,
  paper: `https://arxiv.org/abs/2510.14967`, Ant Group, date: 2025.10
  (ICLR 2026).
- `DR-Venus` — github: `https://github.com/inclusionAI/DR-Venus`,
  paper: `https://arxiv.org/abs/2604.19859`, Ant Group, date: 2026.4.
  IGPO scaled to 200+ turns.
- `AgentPRM` — github: `https://github.com/sanjibanc/agent_prm`,
  paper: `https://arxiv.org/abs/2502.10325`, Cornell, date: 2025.2.
- `AgentRM` — github: `https://github.com/thunlp/AgentRM`,
  paper: `https://arxiv.org/abs/2502.18407`, THUNLP, date: 2025.2.
- `Agent-R1` — github: `https://github.com/0russwest0/Agent-R1`,
  paper: `https://arxiv.org/abs/2511.14460`, org: USTC, date: 2025.11.

**Other corpus entries:**

- `DeepAgent` — ToolPO for long-horizon ToolBench/ALFWorld/WebShop/GAIA/HLE.
  github: `https://github.com/RUC-NLPIR/DeepAgent`, paper: `https://arxiv.org/abs/2510.21618`, RUC/Xiaohongshu, date: 2025.10

- `VAGEN` — world-modeling RL — addresses credit assignment via predicted next state.
  github: `https://github.com/mll-lab-nu/VAGEN`, paper: `https://arxiv.org/abs/2510.16907`, Northwestern University (mll-lab-nu), date: 2025.10

- `AgentEvolver` — ADCA-GRPO with self-evolving curriculum aimed at credit assignment.
  github: `https://github.com/modelscope/AgentEvolver`, paper: `https://arxiv.org/abs/2511.10395`, Alibaba/Tongyi Lab, date: 2025.11
