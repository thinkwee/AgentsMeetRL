# Problem: multi-agent training — one role gets all the credit, others don't learn

## Symptoms

- In a multi-agent system (planner + coder + tester, or doctor + patient,
  or self-play A vs B), only one role's loss decreases meaningfully.
- The other roles' outputs become deterministic / collapse / never
  change.
- Joint task success doesn't improve even though one role's "specialized
  metric" improves.
- Self-play: strategy converges to a degenerate equilibrium (e.g. always
  fold).

## Root causes

1. **Trajectory reward is global** — every agent gets the same scalar.
   Without role-conditioning, advantage is identical across roles; the
   agent that mostly contributed and the one that piggybacked are
   indistinguishable.
2. **Role symmetry / shared parameters** — if planner and coder share a
   single set of weights, gradients from one role can erase another.
3. **Self-play opponent is always the latest snapshot** — strategies
   cycle without progress.
4. **One role has trivial "easy wins"** that earn reward without
   contributing to the joint task.

## Diagnosis

- Plot per-role loss; one flat = credit collapse.
- Plot per-role advantage histogram. If one role's advantage is always
  ~0, credit isn't reaching it.
- Read 20 high-reward joint episodes. Was every role contributing? Or
  was one role doing everything?
- For self-play: track win-rate vs *fixed* baseline opponent over time.
  If it cycles, you have rock-paper-scissors instability — opponent pool
  is the fix.

## Fixes

### Fix 1: role-conditioned advantage (RAE)

> **SPIRAL** — github: `https://github.com/spiral-rl/spiral`,
> paper: `https://arxiv.org/abs/2506.24119`, NUS/A*STAR/Sea AI, date: 2025.6.
> Single policy plays both roles in zero-sum games. Computes separate
> $A_0(s,a)$ and $A_1(s,a)$ per role.

### Fix 2: action+token level credit

> **MARFT** — github: `https://github.com/jwliao-ai/MARFT`,
> paper: `https://arxiv.org/abs/2504.16129`, SII/SJTU, date: 2025.4.
> Action+token level multi-agent RL paradigm.

### Fix 3: per-agent reward shaping

> **MarsRL** — github: `https://github.com/liushulinle/MarsRL`,
> paper: `https://arxiv.org/abs/2511.11373`, date: 2025.11. Agent-specific
> rewards in multi-agent reasoning.

> **MrlX** — github: `https://github.com/AQ-MedAI/MrlX`,
> paper: `https://arxiv.org/abs/2511.13288`, Ant Group AQ-MedAI, date: 2025.11.
> Hierarchical M-GRPO for deep research multi-agent.

### Fix 4: agent-wise GRPO

> **DrMAS** — github: `https://github.com/langfengQ/DrMAS`,
> paper: `https://arxiv.org/abs/2602.08847`, NTU, date: 2026.2.
> Agent-wise GRPO for stable multi-agent post-training.

### Fix 5: variants — MAGRPO / MAREINFORCE / MARLOO

> **CoMLRL** — github: `https://github.com/OpenMLRL/CoMLRL`,
> paper: `https://arxiv.org/abs/2508.04652`, OpenMLRL, date: 2025.8.

### Fix 6: AT-GRPO

> **PettingLLMs** — github: `https://github.com/pettingllms-ai/PettingLLMs`,
> paper: `https://arxiv.org/abs/2510.11062`, Intel/UCSD, date: 2025.10.
> Game/code/math/planning with verifiable rewards.

### Fix 7: opponent pool (for self-play)

Instead of always playing the current snapshot, sample from a pool of
past checkpoints.

> **SPIRAL** uses opponent pooling.
> **R-Zero** — github: `https://github.com/Chengsong-Huang/R-Zero`,
> paper: `https://arxiv.org/abs/2508.05004`, Tencent AI Seattle, date: 2025.8.
> Challenger + Solver co-evolution with curriculum.

### Fix 8: separate parameters per role

Don't share parameters across roles unless your specific algorithm calls
for it (RAE-style self-play does, but most collaborative MAS shouldn't).

### Fix 9: PRM trained from MCTS for multi-agent

> **MASPRM** — github: `https://github.com/milad1378yz/MASPRM`,
> paper: `https://arxiv.org/abs/2510.24803`, UBC/Huawei, date: 2025.10.
> PRM trained from MCTS rollouts; multi-agent reasoning.

## Paper / repo references

(All cited above.)

**Other corpus entries:**

- `ARIA` — REINFORCE for negotiation/bargaining (illustrates instability of REINFORCE in multi-agent).
  github: `https://github.com/rhyang2021/ARIA`, paper: `https://arxiv.org/abs/2506.00539`, Fudan University, date: 2025.6

- `AMPO` — BC + AMPO (GRPO improvement) for social interaction tasks.
  github: `https://github.com/MozerWang/AMPO`, paper: `https://arxiv.org/abs/2505.02156`, Tongyi Lab, Alibaba, date: 2025.5

- `MAPoRL` — PPO for collaborative LLM tasks.
  github: `https://github.com/chanwoo-park-official/MAPoRL`, Academic, date: 2025.8

- `FlowReasoner` — GRPO for multi-agent workflow design.
  github: `https://github.com/sail-sg/FlowReasoner`, paper: `https://arxiv.org/abs/2504.15257`, Sea AI Lab / NUS, date: 2025.4

- `VIKI-R` — GRPO RFT after SFT for embodied multi-robot cooperation.
  github: `https://github.com/MARS-EAI/VIKI-R`, paper: `https://arxiv.org/abs/2506.09049`, MARS-EAI (NeurIPS 2025 D&B), date: 2025.6
