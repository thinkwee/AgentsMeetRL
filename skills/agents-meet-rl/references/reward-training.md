# Reward Models & Training Methodology

Process/outcome reward models, PRM benchmarks, training recipes.

_Total: 6 entries._

### ToolPRMBench
- **Idea:** Benchmark for process reward models in tool use: step-level test cases (history, correct vs wrong action, tool metadata) via offline+online sampling.
- `https://github.com/David-Li0406/ToolPRMBench` · org: Arizona State University · date: 2026.1
- Paper(s): [Paper](https://arxiv.org/abs/2601.12294)
- Algorithm: N/A (Benchmark) · Framework: — · Agent: Single · Turns: Multi · Tools: Yes
- Reward phase: Process · Reward type: Rule/Model
- Task: Tool-Use
- Focus: PRM Benchmark for Tool-Use

### RLVR-World
- **Idea:** Trains world models with RLVR by treating decoded-prediction metrics (accuracy, perceptual quality) as verifiable rewards, fixing MLE-metric misalignment.
- `https://github.com/thuml/RLVR-World` · org: THU ML Group · date: 2025.5
- Paper(s): [Paper](https://arxiv.org/abs/2505.13934)
- Algorithm: RLVR · Framework: — · Agent: Single · Turns: Multi · Tools: No
- Reward phase: Outcome · Reward type: Model (verifiable)
- Task: World Modeling (Language/Video)
- Focus: RLVR for World Models

### AgentProg
- **Idea:** ProgRM predicts per-step task-completion progress (LCS self-annotation of key steps) as dense reward, beating outcome RMs that over-penalize failed GUI trajectories.
- `https://github.com/MobileLLM/AgentProg` · org: MobileLLM · date: 2025.5
- Paper(s): [Paper](https://arxiv.org/abs/2505.18121)
- Algorithm: Online RL w/ progress reward · Framework: — · Agent: Single · Turns: Multi · Tools: Yes
- Reward phase: Process · Reward type: Model (ProgRM)
- Task: GUI Agent Training
- Focus: Progress Reward Model (ProgRM)

### AgentPRM
- **Idea:** Lightweight actor-critic PRM via Monte Carlo rollouts (plus InversePRM learning process rewards from demos), bolting onto existing RLHF pipelines.
- `https://github.com/sanjibanc/agent_prm` · org: Cornell · date: 2025.2
- Paper(s): [Paper](https://arxiv.org/abs/2502.10325)
- Algorithm: PPO/DPO + PRM · Framework: — · Agent: Single · Turns: Multi · Tools: Yes
- Reward phase: Process · Reward type: Model (PRM)
- Task: ALFWorld/General
- Focus: Process Reward for Agents

### Agentic-Reward-Modeling
- **Idea:** RewardAgent fuses human-preference RM with verifiable factuality and instruction-following signals for more reliable rewards in best-of-n and DPO.
- `https://github.com/THU-KEG/Agentic-Reward-Modeling` · org: THU-KEG · date: 2025.2
- Paper(s): [Paper](https://arxiv.org/abs/2502.19328)
- Algorithm: DPO/Best-of-N · Framework: — · Agent: Single · Turns: Single · Tools: Yes (Verification)
- Reward phase: Outcome · Reward type: Model (Reward Agent)
- Task: General Instruction
- Focus: Agentic Reward Agent

### AgentRM
- **Idea:** Finetuning a reward model to guide policy at test time (best-of-N, step-level beam search) generalizes better across agent tasks than finetuning the policy.
- `https://github.com/thunlp/AgentRM` · org: THUNLP/Tsinghua · date: 2025.2
- Paper(s): [Paper](https://arxiv.org/abs/2502.18407)
- Algorithm: MCTS/RM-guided · Framework: — · Agent: Single · Turns: Multi · Tools: Yes
- Reward phase: Outcome · Reward type: Model (regression PRM)
- Task: 9 Agent Tasks
- Focus: Generalizable Agent RM
