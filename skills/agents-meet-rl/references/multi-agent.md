# Multi-Agent RL

Multi-agent collaboration, negotiation, or self-play. Watch for credit assignment and role-conditioned advantage.

_Total: 14 entries._

### Maestro
- **Idea:** Outcome-only RL trains a lightweight orchestrator over a frozen expert ensemble to decide which model-skill to invoke and when to stop, generalizing to unseen experts.
- `https://github.com/jinyangwu/Maestro` · org: Tsinghua / Multi-institution · date: 2026.5
- Paper(s): [Paper](https://arxiv.org/abs/2605.22177)
- Algorithm: Outcome RL (lightweight orchestrator over frozen expert ensembles) · Framework: veRL + verl-tool · Agent: Multi (orchestrator + frozen experts) · Turns: Multi · Tools: Yes (expert models + 2-tier skill library: OCR/detection/visual)
- Reward phase: Outcome · Reward type: External
- Task: 10 multimodal benchmarks (math/chart/HR/domain — 70.1% avg, beats GPT-5 & Gemini-2.5-Pro)

### DrMAS
- **Idea:** Agent-wise advantage normalization using each agent's own reward stats, fixing the gradient-norm instability that global GRPO baselines cause in multi-agent LLM systems.
- `https://github.com/langfengQ/DrMAS` · org: NTU · date: 2026.2
- Paper(s): [Paper](https://arxiv.org/abs/2602.08847)
- Algorithm: GRPO (agent-wise) · Framework: Custom · Agent: Multi · Turns: Multi · Tools: No
- Reward phase: Outcome · Reward type: Rule
- Task: Multi-agent LLM Systems

### MarsRL
- **Idea:** Jointly RL-trains Solver/Verifier/Corrector agents using agent-specific rewards to cut reward noise plus pipeline-style training for long math trajectories.
- `https://github.com/liushulinle/MarsRL` · org: Academic · date: 2025.11
- Paper(s): [Paper](https://arxiv.org/abs/2511.11373)
- Algorithm: RLVR (agent-specific rewards) · Framework: veRL · Agent: Multi · Turns: Multi · Tools: No
- Reward phase: Both · Reward type: Rule (verifiable)
- Task: Math Reasoning (AIME/BeyondAIME)

### PettingLLMs
- **Idea:** AT-GRPO adds agent- and turn-wise advantage grouping because standard GRPO grouping breaks when prompts vary by role and turn, enabling stable multi-agent RL.
- `https://github.com/pettingllms-ai/PettingLLMs` · org: Intel / UCSD · date: 2025.10
- Paper(s): [Paper](https://arxiv.org/abs/2510.11062)
- Algorithm: AT-GRPO · Framework: Custom · Agent: Multi · Turns: Multi · Tools: No
- Reward phase: Both · Reward type: Rule (verifiable)
- Task: Game/Code/Math/Planning

### MASPRM
- **Idea:** Process reward model for multi-agent systems trained from MCTS rollouts with only terminal rewards propagated to local targets, scoring partial transcripts to guide search.
- `https://github.com/milad1378yz/MASPRM` · org: UBC / Huawei · date: 2025.10
- Paper(s): [Paper](https://arxiv.org/abs/2510.24803)
- Algorithm: PRM (trained from MCTS rollouts) · Framework: Custom · Agent: Multi · Turns: Multi · Tools: No
- Reward phase: Process · Reward type: Learned PRM
- Task: Reasoning (GSM8K/MATH/MMLU)

### MrlX
- **Idea:** M-GRPO optimizes main- and sub-agents separately via group-relative advantages plus trajectory alignment for fixed-size batches, no end-to-end backprop.
- `https://github.com/AQ-MedAI/MrlX` · org: Ant Group (AQ-MedAI) · date: 2025.11
- Paper(s): [Paper](https://arxiv.org/abs/2511.13288)
- Algorithm: M-GRPO (hierarchical) · Framework: Custom (SGLang + Megatron) · Agent: Multi · Turns: Multi · Tools: Yes (Search)
- Reward phase: Outcome · Reward type: Rule + Model
- Task: Deep Research (GAIA/XBench)

### CoMAS
- **Idea:** Agents co-evolve via RL using LLM-as-judge intrinsic rewards mined from peer discussion dynamics, needing no external reward signal.
- `https://github.com/xxyQwQ/CoMAS` · org: Shanghai AI Lab / CUHK / Oxford / NUS · date: 2025.10
- Paper(s): [Paper](https://arxiv.org/abs/2510.08529)
- Algorithm: RL w/ LLM-Judge intrinsic reward · Framework: Custom · Agent: Multi · Turns: Multi · Tools: No
- Reward phase: Process · Reward type: Model
- Task: Co-evolving Reasoning

### MAPoRL
- **Idea:** Cooperative multi-agent RL co-training heterogeneous LLMs via PPO with a verifier reward, so different models specialize and learn from each other on collaborative tasks.
- `https://github.com/chanwoo-park-official/MAPoRL` · org: Academic · date: 2025.8
- Paper(s): —
- Algorithm: PPO · Framework: Custom · Agent: Multi · Turns: Multi · Tools: No
- Reward phase: Outcome · Reward type: Rule
- Task: Collaborative LLM Tasks

### CoMLRL
- **Idea:** Casts LLM collaboration as cooperative MARL and fine-tunes the system with group-level RL (MAGRPO) instead of hand-engineering per-agent rewards.
- `https://github.com/OpenMLRL/CoMLRL` · org: OpenMLRL · date: 2025.8
- Paper(s): [Paper](https://arxiv.org/abs/2508.04652)
- Algorithm: MAGRPO / MAREINFORCE / MARLOO · Framework: TRL · Agent: Multi · Turns: Multi · Tools: Minimal
- Reward phase: Outcome · Reward type: Custom
- Task: Writing / Code / Minecraft

### ARIA
- **Idea:** Projects language actions into a low-dimensional intention space so semantically similar actions share rewards, densifying sparse signals and cutting gradient variance.
- `https://github.com/rhyang2021/ARIA` · org: Fudan University · date: 2025.6
- Paper(s): [Paper](https://arxiv.org/abs/2506.00539)
- Algorithm: REINFORCE · Framework: Custom · Agent: Both · Turns: Multi · Tools: No
- Reward phase: Process · Reward type: Other
- Task: Negotiation/Bargaining

### SPIRAL
- **Idea:** Self-play on zero-sum games as an auto-curriculum, stabilized by Role-conditioned Advantage Estimation that accounts for each player's role.
- `https://github.com/spiral-rl/spiral` · org: NUS / A*STAR / Sea AI Lab · date: 2025.6
- Paper(s): [Paper](https://arxiv.org/abs/2506.24119)
- Algorithm: Role-conditioned Advantage Estimation (RAE) · Framework: Oat · Agent: Multi · Turns: Multi · Tools: No
- Reward phase: Outcome · Reward type: Rule
- Task: Zero-sum Games (TicTacToe/Kuhn/Negotiation)

### AMPO
- **Idea:** Adaptive Mode Policy Optimization lets social agents switch reasoning depth (intuitive to deliberate) per context, yielding 33% shorter chains with higher performance.
- `https://github.com/MozerWang/AMPO` · org: Tongyi Lab, Alibaba · date: 2025.5
- Paper(s): [Paper](https://arxiv.org/abs/2505.02156)
- Algorithm: BC/AMPO(GRPO improvement) · Framework: veRL · Agent: Multi · Turns: Multi · Tools: No
- Reward phase: Outcome · Reward type: Model-based
- Task: Social Interaction

### FlowReasoner
- **Idea:** Reasoning meta-agent (distilled from R1) that generates a per-query multi-agent workflow, refined by RL on execution feedback over performance/complexity/efficiency rewards.
- `https://github.com/sail-sg/FlowReasoner` · org: Sea AI Lab / NUS · date: 2025.4
- Paper(s): [Paper](https://arxiv.org/abs/2504.15257)
- Algorithm: GRPO · Framework: Custom · Agent: Multi · Turns: Multi · Tools: Yes
- Reward phase: Outcome · Reward type: Rule
- Task: Multi-agent Workflow Design

### MARFT
- **Idea:** Reformulates multi-agent fine-tuning as a Flex-MG game with an algorithm tailored to LLM-based MAS rather than directly porting classical MARL.
- `https://github.com/jwliao-ai/MARFT` · org: SII / SJTU · date: 2025.4
- Paper(s): [Paper](https://arxiv.org/abs/2504.16129)
- Algorithm: MARFT paradigm (action+token level) · Framework: Custom · Agent: Multi · Turns: Multi · Tools: Yes
- Reward phase: Both · Reward type: Rule
- Task: Research / Math
