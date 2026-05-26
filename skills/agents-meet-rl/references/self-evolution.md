# Self-Evolution Agents

Agents that improve themselves through closed-loop feedback (challenger/solver, MCTS-driven self-training).

_Total: 10 entries._

### world-knowledge
- `https://github.com/Bklight999/world-knowledge` · org: HKUST / Tencent · date: 2026.4
- Paper(s): [Paper](https://arxiv.org/abs/2604.18131)
- Algorithm: Outcome-based RL (reward-free self-evolution) · Framework: Custom · Agent: Single · Turns: Multi · Tools: Yes (web pipeline for env-specific knowledge construction)
- Reward phase: Outcome · Reward type: Model (intrinsic; world-knowledge gain)
- Task: Web Agents (WebVoyager/WebWalker; +20% on Qwen3-30B & Seed-OSS-36B)

### MemSkill
- `https://github.com/ViktorAxelsen/MemSkill` · org: NTU/UIUC/UIC/Tsinghua · date: 2026.2
- Paper(s): [Paper](https://arxiv.org/abs/2602.02474)
- Algorithm: PPO · Framework: Custom · Agent: Single · Turns: Multi · Tools: Yes
- Reward phase: Process · Reward type: Model (learned skills)
- Task: QA/ALFWorld

### MemRL
- `https://github.com/MemTensor/MemRL` · org: SJTU/Xidian/NUS/USTC/MemTensor · date: 2026.1
- Paper(s): [Paper](https://arxiv.org/abs/2601.03192)
- Algorithm: RL-based (Q-value) · Framework: Custom · Agent: Single · Turns: Multi · Tools: Yes
- Reward phase: Process · Reward type: Model (retrieval)
- Task: HLE/BigCodeBench/ALFWorld

### AgentEvolver
- `https://github.com/modelscope/AgentEvolver` · org: Alibaba/Tongyi Lab · date: 2025.11
- Paper(s): [Paper](https://arxiv.org/abs/2511.10395)
- Algorithm: ADCA-GRPO · Framework: Custom · Agent: Single · Turns: Multi · Tools: Yes
- Reward phase: Outcome · Reward type: Rule
- Task: Social Game/Tool-use

### EvolveR
- `https://github.com/Edaizi/EvolveR` · org: KnowledgeXLab / Shanghai AI Lab · date: 2025.10
- Paper(s): [Paper](https://arxiv.org/abs/2510.16079)
- Algorithm: GRPO (closed-loop online+offline) · Framework: veRL · Agent: Single · Turns: Multi · Tools: Yes (experience retrieval)
- Reward phase: Outcome · Reward type: Rule
- Task: Multi-hop QA (NQ/HotpotQA)

### SEAgent
- `https://github.com/SunzeY/SEAgent` · org: Shanghai AI Lab / CUHK · date: 2025.8
- Paper(s): [Paper](https://arxiv.org/abs/2508.04700)
- Algorithm: GRPO · Framework: Custom · Agent: Single · Turns: Multi · Tools: Yes (Screenshot-based)
- Reward phase: Outcome · Reward type: Model
- Task: Computer Use (OSWorld)

### R-Zero
- `https://github.com/Chengsong-Huang/R-Zero` · org: Tencent AI Seattle Lab / WashU / UMD · date: 2025.8
- Paper(s): [Paper](https://arxiv.org/abs/2508.05004)
- Algorithm: GRPO (Challenger + Solver co-evolution) · Framework: EasyR1 · Agent: Multi · Turns: Multi · Tools: No
- Reward phase: Outcome · Reward type: Rule (majority voting)
- Task: Math/SuperGPQA/MMLU-Pro/BBEH

### Absolute-Zero-Reasoner
- `https://github.com/LeapLabTHU/Absolute-Zero-Reasoner` · org: Tsinghua (LeapLabTHU) / BIGAI / PSU · date: 2025.5
- Paper(s): [Paper](https://arxiv.org/abs/2505.03335)
- Algorithm: TRR++ (Task-Relative REINFORCE++) · Framework: veRL · Agent: Single · Turns: Single · Tools: Yes (Python exec)
- Reward phase: Outcome · Reward type: Rule + learnability
- Task: Code/Math Reasoning (HumanEval/MBPP/LiveCodeBench)

### RAGEN
- `https://github.com/RAGEN-AI/RAGEN` · org: RAGEN-AI · date: 2025.4
- Paper(s): [Paper](https://arxiv.org/abs/2504.20073)
- Algorithm: PPO/GRPO (StarPO) · Framework: veRL · Agent: Single · Turns: Multi · Tools: Yes
- Reward phase: Both · Reward type: All
- Task: TextGame

### WebRL
- `https://github.com/THUDM/WebRL` · org: Tsinghua/Zhipu AI · date: 2024.11
- Paper(s): [Paper](https://arxiv.org/abs/2411.02337)
- Algorithm: Actor-Critic RL + ORM · Framework: Custom · Agent: Single · Turns: Multi · Tools: Yes (Web browsing)
- Reward phase: Outcome · Reward type: Model (ORM)
- Task: Web Navigation (WebArena)
