# Multi-Agent RL

Multi-agent collaboration, negotiation, or self-play. Watch for credit assignment and role-conditioned advantage.

_Total: 14 entries._

### Maestro
- `https://github.com/jinyangwu/Maestro` · org: Tsinghua / Multi-institution · date: 2026.5
- Paper(s): [Paper](https://arxiv.org/abs/2605.22177)
- Algorithm: Outcome RL (lightweight orchestrator over frozen expert ensembles) · Framework: veRL + verl-tool · Agent: Multi (orchestrator + frozen experts) · Turns: Multi · Tools: Yes (expert models + 2-tier skill library: OCR/detection/visual)
- Reward phase: Outcome · Reward type: External
- Task: 10 multimodal benchmarks (math/chart/HR/domain — 70.1% avg, beats GPT-5 & Gemini-2.5-Pro)

### DrMAS
- `https://github.com/langfengQ/DrMAS` · org: NTU · date: 2026.2
- Paper(s): [Paper](https://arxiv.org/abs/2602.08847)
- Algorithm: GRPO (agent-wise) · Framework: Custom · Agent: Multi · Turns: Multi · Tools: No
- Reward phase: Outcome · Reward type: Rule
- Task: Multi-agent LLM Systems

### MarsRL
- `https://github.com/liushulinle/MarsRL` · org: Academic · date: 2025.11
- Paper(s): [Paper](https://arxiv.org/abs/2511.11373)
- Algorithm: RLVR (agent-specific rewards) · Framework: veRL · Agent: Multi · Turns: Multi · Tools: No
- Reward phase: Both · Reward type: Rule (verifiable)
- Task: Math Reasoning (AIME/BeyondAIME)

### PettingLLMs
- `https://github.com/pettingllms-ai/PettingLLMs` · org: Intel / UCSD · date: 2025.10
- Paper(s): [Paper](https://arxiv.org/abs/2510.11062)
- Algorithm: AT-GRPO · Framework: Custom · Agent: Multi · Turns: Multi · Tools: No
- Reward phase: Both · Reward type: Rule (verifiable)
- Task: Game/Code/Math/Planning

### MASPRM
- `https://github.com/milad1378yz/MASPRM` · org: UBC / Huawei · date: 2025.10
- Paper(s): [Paper](https://arxiv.org/abs/2510.24803)
- Algorithm: PRM (trained from MCTS rollouts) · Framework: Custom · Agent: Multi · Turns: Multi · Tools: No
- Reward phase: Process · Reward type: Learned PRM
- Task: Reasoning (GSM8K/MATH/MMLU)

### MrlX
- `https://github.com/AQ-MedAI/MrlX` · org: Ant Group (AQ-MedAI) · date: 2025.11
- Paper(s): [Paper](https://arxiv.org/abs/2511.13288)
- Algorithm: M-GRPO (hierarchical) · Framework: Custom (SGLang + Megatron) · Agent: Multi · Turns: Multi · Tools: Yes (Search)
- Reward phase: Outcome · Reward type: Rule + Model
- Task: Deep Research (GAIA/XBench)

### CoMAS
- `https://github.com/xxyQwQ/CoMAS` · org: Shanghai AI Lab / CUHK / Oxford / NUS · date: 2025.10
- Paper(s): [Paper](https://arxiv.org/abs/2510.08529)
- Algorithm: RL w/ LLM-Judge intrinsic reward · Framework: Custom · Agent: Multi · Turns: Multi · Tools: No
- Reward phase: Process · Reward type: Model
- Task: Co-evolving Reasoning

### MAPoRL
- `https://github.com/chanwoo-park-official/MAPoRL` · org: Academic · date: 2025.8
- Paper(s): —
- Algorithm: PPO · Framework: Custom · Agent: Multi · Turns: Multi · Tools: No
- Reward phase: Outcome · Reward type: Rule
- Task: Collaborative LLM Tasks

### CoMLRL
- `https://github.com/OpenMLRL/CoMLRL` · org: OpenMLRL · date: 2025.8
- Paper(s): [Paper](https://arxiv.org/abs/2508.04652)
- Algorithm: MAGRPO / MAREINFORCE / MARLOO · Framework: TRL · Agent: Multi · Turns: Multi · Tools: Minimal
- Reward phase: Outcome · Reward type: Custom
- Task: Writing / Code / Minecraft

### ARIA
- `https://github.com/rhyang2021/ARIA` · org: Fudan University · date: 2025.6
- Paper(s): [Paper](https://arxiv.org/abs/2506.00539)
- Algorithm: REINFORCE · Framework: Custom · Agent: Both · Turns: Multi · Tools: No
- Reward phase: Process · Reward type: Other
- Task: Negotiation/Bargaining

### SPIRAL
- `https://github.com/spiral-rl/spiral` · org: NUS / A*STAR / Sea AI Lab · date: 2025.6
- Paper(s): [Paper](https://arxiv.org/abs/2506.24119)
- Algorithm: Role-conditioned Advantage Estimation (RAE) · Framework: Oat · Agent: Multi · Turns: Multi · Tools: No
- Reward phase: Outcome · Reward type: Rule
- Task: Zero-sum Games (TicTacToe/Kuhn/Negotiation)

### AMPO
- `https://github.com/MozerWang/AMPO` · org: Tongyi Lab, Alibaba · date: 2025.5
- Paper(s): [Paper](https://arxiv.org/abs/2505.02156)
- Algorithm: BC/AMPO(GRPO improvement) · Framework: veRL · Agent: Multi · Turns: Multi · Tools: No
- Reward phase: Outcome · Reward type: Model-based
- Task: Social Interaction

### FlowReasoner
- `https://github.com/sail-sg/FlowReasoner` · org: Sea AI Lab / NUS · date: 2025.4
- Paper(s): [Paper](https://arxiv.org/abs/2504.15257)
- Algorithm: GRPO · Framework: Custom · Agent: Multi · Turns: Multi · Tools: Yes
- Reward phase: Outcome · Reward type: Rule
- Task: Multi-agent Workflow Design

### MARFT
- `https://github.com/jwliao-ai/MARFT` · org: SII / SJTU · date: 2025.4
- Paper(s): [Paper](https://arxiv.org/abs/2504.16129)
- Algorithm: MARFT paradigm (action+token level) · Framework: Custom · Agent: Multi · Turns: Multi · Tools: Yes
- Reward phase: Both · Reward type: Rule
- Task: Research / Math
