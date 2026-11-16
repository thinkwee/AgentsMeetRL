# Reward Models & Training Methodology

Process/outcome reward models, PRM benchmarks, training recipes.

_Total: 17 entries._

### Mosaic
- **Idea:** When rollouts are split across compaction/sub-agent sessions, assigns session-level advantages instead of broadcasting one trajectory advantage to every session.
- `https://github.com/LARK-AI-Lab/Mosaic` · org: LARK-AI-Lab · date: 2026.10
- Paper(s): [Paper](https://arxiv.org/abs/2610.22174)
- Algorithm: GRPO with per-session advantages · Agent: Both · Turns: Multi · Tools: Yes (search, compaction, sub-agent)
- Reward phase: Both · Reward type: Rule-Based
- Task: Search agents with context compaction & sub-agent forking
- Focus: Multi-session credit assignment

### ConCal
- **Idea:** Shares continuation evidence across repeated visits to the same task state and propagates calibrated action values backward for finer step-level advantages than GiGPO.
- `https://github.com/Yingjian-Chen/ConCal` · org: Academic · date: 2026.10
- Paper(s): [Paper](https://arxiv.org/abs/2610.37195)
- Algorithm: GiGPO extension (continuation sharing) · Agent: Single · Turns: Multi · Tools: Yes (env actions)
- Reward phase: Both · Reward type: Rule-Based
- Task: ALFWorld/WebShop/Sokoban/AppWorld
- Focus: Step-level action-value calibration

### FocalRL
- **Idea:** Locates the consequential error in a long trajectory, branches from the pre-error state, and rewards short rubric-checked repairs instead of re-running the whole episode.
- `https://github.com/microsoft/FocalRL` · org: Microsoft · date: 2026.10
- Algorithm: GRPO (Miles) with branching from pre-error states · Agent: Single · Turns: Multi · Tools: Yes (web search/browse, SWE sandbox)
- Reward phase: Both · Reward type: Model + External Verifier
- Task: Ultra-long-horizon deep research (BrowseComp) & SWE
- Focus: Focal credit assignment / local repair rewards

### DARS
- **Idea:** Tracks verified/broken/repaired task requirements in a dependency graph and converts changes in graph potential into step rewards.
- `https://github.com/JianhuiWei7/DARS` · org: Zhejiang University · date: 2026.10
- Paper(s): [Paper](https://arxiv.org/abs/2610.01207)
- Algorithm: GRPO/GiGPO/RLOO + potential-based shaping · Agent: Single · Turns: Multi · Tools: Yes (env actions)
- Reward phase: Process · Reward type: Custom
- Task: ALFWorld/WebShop step-level credit
- Focus: Dependency-aware reward shaping

### SAPO
- **Idea:** Single-rollout PPO-style agentic RL with a shared policy/value model, avoiding both GRPO group sampling and a separate critic.
- `https://github.com/dy-liang/SAPO` · org: NTU · date: 2026.8
- Paper(s): [Paper](https://arxiv.org/abs/2608.19842)
- Algorithm: SAPO (single-rollout, shared policy/value) · Agent: Single · Turns: Multi · Tools: No (env actions)
- Reward phase: Outcome · Reward type: Rule-Based
- Task: Long-horizon agent RL (ALFWorld/WebShop)
- Focus: Single-rollout policy optimization

### DRACO
- **Idea:** In the outcome-blind setting, dynamically generated rubrics are scored once per trajectory and the judge's per-rubric citations redistribute the GRPO advantage across responsible steps in closed form — beating sparse ground-truth-reward GRPO on AppWorld without any verifier.
- `https://github.com/IBM/draco` · org: CMU / IBM Research · date: 2026.9
- Paper(s): [Paper](https://arxiv.org/abs/2609.04094)
- Algorithm: GRPO w/ rubric-attributed step-level advantages · Agent: Single · Turns: Multi · Tools: Yes
- Reward phase: Process · Reward type: Model (LLM judge on dynamic rubrics)
- Task: AppWorld / τ-Bench (tool use)
- Focus: Outcome-blind rubric rewards with step-level credit assignment

### Agent-G²
- **Idea:** Schedules how much of an expert trajectory to retain before each GRPO rollout via an online-estimated Gaussian, annealing guidance away as competence grows to beat sparse-reward exploration failure.
- `https://github.com/ZJU-REAL/Agent-G2` · org: Zhejiang University / Baidu (EMNLP'26) · date: 2026.8
- Paper(s): [Paper](https://arxiv.org/abs/2608.23318)
- Algorithm: GRPO + Gaussian-guided adaptive-depth exploration · Agent: Single · Turns: Multi · Tools: Yes (interactive env actions)
- Reward phase: Outcome · Reward type: Rule-Based/External
- Task: ALFWorld / WebShop
- Focus: Exploration guidance under sparse reward

### AgentV-RL
- **Idea:** Turns reward modeling into a multi-turn tool-augmented deliberative process with forward+backward verifier agents; a 4B verifier beats SOTA ORMs by 25%.
- `https://github.com/JiazhengZhang/AgentV-RL` · org: Academic · date: 2026.4
- Paper(s): [Paper](https://arxiv.org/abs/2604.16004)
- Algorithm: RL (verl) training an agentic verifier · Framework: veRL · Agent: Single · Turns: Multi · Tools: Yes (verifier invokes tools, e.g. code)
- Reward phase: Process · Reward type: Model-Based
- Task: Tool-augmented deliberative verifier (reward model)
- Focus: Agentic Verifier Reward Model

### DataMind
- **Idea:** An environment-aware generative process reward model (DataPRM) scores intermediate Python/SQL steps and plugs into RL for data-analysis agents.
- `https://github.com/zjunlp/DataMind` · org: Zhejiang University (ZJUNLP) · date: 2026.4
- Paper(s): [Paper](https://arxiv.org/abs/2604.24198)
- Algorithm: RL w/ generative PRM (DataPRM) · Framework: veRL · Agent: Single · Turns: Multi · Tools: Yes (code-based multi-turn)
- Reward phase: Process · Reward type: Model (PRM) + External (execution)
- Task: Agentic data analysis (Python/SQL; ScienceAgentBench/DABench)
- Focus: Process Reward Model (DataPRM)

### ARLArena
- **Idea:** Decomposes the agentic policy gradient into four design axes and proposes SAMPO to prevent training collapse across web, embodied, math, game, and search.
- `https://github.com/WillDreamer/ARL-Arena` · org: UCLA · date: 2026.2
- Paper(s): [Paper](https://arxiv.org/abs/2602.21534)
- Algorithm: SAMPO (Stable Agentic Policy Optimization) · Framework: veRL · Agent: Single · Turns: Multi · Tools: Yes (code/web/search/embodied)
- Reward phase: Outcome · Reward type: External + Rule
- Task: Stable agentic RL across web/embodied/math/game/search
- Focus: Stable Agentic RL (SAMPO)

### Agent-RRM
- **Idea:** Trains a reasoning reward model that emits structured trajectory critiques and scores, then uses it to train multi-turn tool-use agents.
- `https://github.com/kxfan2002/Reagent` · org: Academic · date: 2026.1
- Paper(s): [Paper](https://arxiv.org/abs/2601.22154)
- Algorithm: Agentic RL w/ trained reasoning RM · Framework: veRL / rLLM · Agent: Single · Turns: Multi · Tools: Yes (agentic trajectories)
- Reward phase: Process · Reward type: Model-Based (RRM)
- Task: Reward model for agents (web nav, multi-hop QA)
- Focus: Reasoning Reward Model for Agents

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
