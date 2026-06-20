# Self-Evolution Agents

Agents that improve themselves through closed-loop feedback (challenger/solver, MCTS-driven self-training).

_Total: 13 entries._

### SIRI
- **Idea:** Self-internalizing RL discovers, validates (paired skill-augmented vs skill-free rollouts), and distills the agent's own skills without any external skill bank.
- `https://github.com/kirito618/SIRI` · org: Academic · date: 2026.6
- Paper(s): [Paper](https://arxiv.org/abs/2606.02355)
- Algorithm: GiGPO + self-skill mining/distillation · Framework: Custom (GiGPO) · Agent: Single · Turns: Multi · Tools: Yes (interactive actions)
- Reward phase: Both · Reward type: External + Custom
- Task: Self-internalizing intrinsic skills (ALFWorld/WebShop)

### world-knowledge
- **Idea:** Outcome reward measures how much an agent's self-generated world knowledge raises downstream success, enabling reward-free spontaneous adaptation to unseen environments at inference.
- `https://github.com/Bklight999/world-knowledge` · org: HKUST / Tencent · date: 2026.4
- Paper(s): [Paper](https://arxiv.org/abs/2604.18131)
- Algorithm: Outcome-based RL (reward-free self-evolution) · Framework: Custom · Agent: Single · Turns: Multi · Tools: Yes (web pipeline for env-specific knowledge construction)
- Reward phase: Outcome · Reward type: Model (intrinsic; world-knowledge gain)
- Task: Web Agents (WebVoyager/WebWalker; +20% on Qwen3-30B & Seed-OSS-36B)

### ARISE
- **Idea:** Hierarchical RL with a persistent skill library that co-evolves with reasoning, using counterfactual credit to reward skill quality.
- `https://github.com/Skylanding/ARISE` · org: George Washington University · date: 2026.3
- Paper(s): [Paper](https://arxiv.org/abs/2603.16060)
- Algorithm: Hierarchical RL (options + intra-option) w/ skill evolution · Framework: veRL · Agent: Single · Turns: Multi · Tools: No (skill reuse over multi-step reasoning)
- Reward phase: Both · Reward type: External + Custom (skill-quality)
- Task: Reasoning w/ intrinsic skill library (7 Olympiad benchmarks)

### Tool-R0
- **Idea:** Self-play from zero data: a Generator proposes frontier-difficulty tool-use tasks while a Solver learns to solve them, forming a self-improving loop.
- `https://github.com/emrecanacikgoz/Tool-R0` · org: UIUC / ETH Zurich · date: 2026.2
- Paper(s): [Paper](https://arxiv.org/abs/2602.21320)
- Algorithm: Self-play RL (generator+solver co-evolution) · Framework: veRL · Agent: Multi · Turns: Multi · Tools: Yes (real tool/function calls)
- Reward phase: Both · Reward type: External + Custom
- Task: Self-evolving tool-learning from zero data

### MemSkill
- **Idea:** Treats memory operations as learnable evolvable skills: a controller learns skill selection while a designer reviews failures and refines the skill set in a closed loop.
- `https://github.com/ViktorAxelsen/MemSkill` · org: NTU/UIUC/UIC/Tsinghua · date: 2026.2
- Paper(s): [Paper](https://arxiv.org/abs/2602.02474)
- Algorithm: PPO · Framework: Custom · Agent: Single · Turns: Multi · Tools: Yes
- Reward phase: Process · Reward type: Model (learned skills)
- Task: QA/ALFWorld

### MemRL
- **Idea:** Non-parametric memory RL decouples stable reasoning from plastic episodic memory, using two-phase retrieval and environmental feedback to surface high-utility strategies without weight updates.
- `https://github.com/MemTensor/MemRL` · org: SJTU/Xidian/NUS/USTC/MemTensor · date: 2026.1
- Paper(s): [Paper](https://arxiv.org/abs/2601.03192)
- Algorithm: RL-based (Q-value) · Framework: Custom · Agent: Single · Turns: Multi · Tools: Yes
- Reward phase: Process · Reward type: Model (retrieval)
- Task: HLE/BigCodeBench/ALFWorld

### AgentEvolver
- **Idea:** Self-questioning (task generation), self-navigating (experience-reuse exploration), and self-attributing (per-action differentiated rewards) make agent RL self-sufficient and sample-efficient.
- `https://github.com/modelscope/AgentEvolver` · org: Alibaba/Tongyi Lab · date: 2025.11
- Paper(s): [Paper](https://arxiv.org/abs/2511.10395)
- Algorithm: ADCA-GRPO · Framework: Custom · Agent: Single · Turns: Multi · Tools: Yes
- Reward phase: Outcome · Reward type: Rule
- Task: Social Game/Tool-use

### EvolveR
- **Idea:** Closed-loop self-improvement: offline self-distillation builds a repository of reusable strategic principles, then online retrieval of those principles drives RL policy updates.
- `https://github.com/Edaizi/EvolveR` · org: KnowledgeXLab / Shanghai AI Lab · date: 2025.10
- Paper(s): [Paper](https://arxiv.org/abs/2510.16079)
- Algorithm: GRPO (closed-loop online+offline) · Framework: veRL · Agent: Single · Turns: Multi · Tools: Yes (experience retrieval)
- Reward phase: Outcome · Reward type: Rule
- Task: Multi-hop QA (NQ/HotpotQA)

### SEAgent
- **Idea:** Self-evolving computer-use agent: a World State Model scores trajectories and a curriculum generates tasks, with GRPO on successes plus adversarial imitation of failure actions.
- `https://github.com/SunzeY/SEAgent` · org: Shanghai AI Lab / CUHK · date: 2025.8
- Paper(s): [Paper](https://arxiv.org/abs/2508.04700)
- Algorithm: GRPO · Framework: Custom · Agent: Single · Turns: Multi · Tools: Yes (Screenshot-based)
- Reward phase: Outcome · Reward type: Model
- Task: Computer Use (OSWorld)

### R-Zero
- **Idea:** Co-evolutionary GRPO where a Challenger is rewarded for posing tasks at the edge of Solver ability and the Solver for solving them, no human data.
- `https://github.com/Chengsong-Huang/R-Zero` · org: Tencent AI Seattle Lab / WashU / UMD · date: 2025.8
- Paper(s): [Paper](https://arxiv.org/abs/2508.05004)
- Algorithm: GRPO (Challenger + Solver co-evolution) · Framework: EasyR1 · Agent: Multi · Turns: Multi · Tools: No
- Reward phase: Outcome · Reward type: Rule (majority voting)
- Task: Math/SuperGPQA/MMLU-Pro/BBEH

### Absolute-Zero-Reasoner
- **Idea:** Single model proposes its own tasks and learns from code-execution-verified rewards via TRR++, a self-play loop needing zero external datasets.
- `https://github.com/LeapLabTHU/Absolute-Zero-Reasoner` · org: Tsinghua (LeapLabTHU) / BIGAI / PSU · date: 2025.5
- Paper(s): [Paper](https://arxiv.org/abs/2505.03335)
- Algorithm: TRR++ (Task-Relative REINFORCE++) · Framework: veRL · Agent: Single · Turns: Single · Tools: Yes (Python exec)
- Reward phase: Outcome · Reward type: Rule + learnability
- Task: Code/Math Reasoning (HumanEval/MBPP/LiveCodeBench)

### RAGEN
- **Idea:** StarPO does trajectory-level agent RL; StarPO-S adds trajectory filtering, critic, and gradient stabilization to escape the 'Echo Trap' reward-variance/gradient-spike failure mode.
- `https://github.com/RAGEN-AI/RAGEN` · org: RAGEN-AI · date: 2025.4
- Paper(s): [Paper](https://arxiv.org/abs/2504.20073)
- Algorithm: PPO/GRPO (StarPO) · Framework: veRL · Agent: Single · Turns: Multi · Tools: Yes
- Reward phase: Both · Reward type: All
- Task: TextGame

### WebRL
- **Idea:** Self-evolving online curriculum RL generates new tasks from failed attempts, paired with an outcome-supervised reward model and adaptive RL to train open-source web agents.
- `https://github.com/THUDM/WebRL` · org: Tsinghua/Zhipu AI · date: 2024.11
- Paper(s): [Paper](https://arxiv.org/abs/2411.02337)
- Algorithm: Actor-Critic RL + ORM · Framework: Custom · Agent: Single · Turns: Multi · Tools: Yes (Web browsing)
- Reward phase: Outcome · Reward type: Model (ORM)
- Task: Web Navigation (WebArena)
