# Base Frameworks

RL training frameworks for LLM agents (e.g. veRL, OpenRLHF, slime). Pick one as the base of your training stack.

_Total: 20 entries._

## Contents

uni-agent, OpenClaw-RL, Claw-R1, Open-AgentRL, NeMo-RL, RLinf, siiRL, slime, agent-lightning, AReaL, ROLL, MARTI, Tunix, RL2, verifiers, prime-rl, oat, veRL, OpenRLHF, trl.

### uni-agent
- `https://github.com/verl-project/uni-agent` · org: verl-project · date: 2026.4
- Paper(s): —
- Algorithm: GRPO/GSPO (partial rollout, fully-async) · Agent: Single · Turns: Multi · Tools: Yes (unified model/tool/env abstractions)
- Reward phase: Outcome · Reward type: All
- Task: SWE-Bench/Search/General Agent (1000+ concurrent)

### OpenClaw-RL
- `https://github.com/Gen-Verse/OpenClaw-RL` · org: Gen-Verse · date: 2026.3
- Paper(s): [Paper](https://arxiv.org/abs/2603.10165)
- Algorithm: GRPO/OPD · Agent: Both · Turns: Multi · Tools: Yes
- Reward phase: Both · Reward type: Model/External
- Task: Terminal/GUI/SWE/Tool-call

### Claw-R1
- `https://github.com/AgentR1/Claw-R1` · org: USTC · date: 2026.3
- Paper(s): —
- Algorithm: Generic RL Framework · Agent: Multi · Turns: Multi · Tools: Yes (Framework-agnostic)
- Reward phase: Both · Reward type: All
- Task: General Agent

### Open-AgentRL
- `https://github.com/Gen-Verse/Open-AgentRL` · org: Gen-Verse · date: 2026.2
- Paper(s): [Paper](https://arxiv.org/abs/2602.02488)
- Algorithm: GRPO-TCR · Agent: Single · Turns: Multi · Tools: Yes (SandboxFusion)
- Reward phase: Both · Reward type: Model (PRM)
- Task: Reasoning/GUI/Coding

### NeMo-RL
- `https://github.com/NVIDIA-NeMo/RL` · org: NVIDIA · date: 2026.1
- Paper(s): —
- Algorithm: GRPO/DAPO/GDPO/DPO · Agent: Single · Turns: Multi · Tools: No
- Reward phase: Outcome · Reward type: Rule/External
- Task: Math/Reasoning/Code

### RLinf
- `https://github.com/RLinf/RLinf` · org: Tsinghua/Infinigence AI/PKU · date: 2025.9
- Paper(s): [Paper](https://arxiv.org/abs/2509.15965)
- Algorithm: PPO/GRPO/DAPO/SAC/REINFORCE++/CrossQ/RLPD · Agent: Both · Turns: Multi · Tools: Yes
- Reward phase: Both · Reward type: All (Rule/Model/External)
- Task: Robotics/Math/Code/QA/VQA

### siiRL
- `https://github.com/sii-research/siiRL` · org: Shanghai Innovation Institute · date: 2025.7
- Paper(s): [Paper](https://arxiv.org/abs/2507.13833)
- Algorithm: PPO/GRPO/CPGD/MARFT · Agent: Multi · Turns: Multi · Tools: Planned
- Reward phase: Both · Reward type: Model/Rule
- Task: LLM/VLM/LLM-MAS PostTraining

### slime
- `https://github.com/THUDM/slime` · org: Tsinghua University (THUDM) · date: 2025.6
- Paper(s): [blog](https://lmsys.org/blog/2025-07-09-slime/)
- Algorithm: GRPO/GSPO/REINFORCE++ · Agent: Single · Turns: Both · Tools: Yes
- Reward phase: Both · Reward type: External Verifier
- Task: Math/Code

### agent-lightning
- `https://github.com/microsoft/agent-lightning` · org: Microsoft Research · date: 2025.8
- Paper(s): [Paper](https://arxiv.org/abs/2508.03680)
- Algorithm: PPO/Custom/Automatic Prompt Optimization · Agent: Multi · Turns: Multi · Tools: Yes
- Reward phase: Outcome · Reward type: Model/External/Rule
- Task: Calculator/SQL

### AReaL
- `https://github.com/inclusionAI/AReaL` · org: AntGroup/Tsinghua · date: 2025.5
- Paper(s): [Paper](https://arxiv.org/abs/2505.24298)
- Algorithm: PPO · Agent: Both · Turns: Both · Tools: Yes
- Reward phase: Outcome · Reward type: External
- Task: Math/Code

### ROLL
- `https://github.com/alibaba/ROLL` · org: Alibaba · date: 2025.6
- Paper(s): [Paper](https://arxiv.org/abs/2506.06122)
- Algorithm: PPO/GRPO/Reinforce++/TOPR/RAFT++ · Agent: Multi · Turns: Multi · Tools: Yes
- Reward phase: Both · Reward type: All
- Task: Math/QA/Code/Alignment

### MARTI
- `https://github.com/TsinghuaC3I/MARTI` · org: Tsinghua · date: 2025.5
- Paper(s): —
- Algorithm: PPO/GRPO/REINFORCE++/TTRL · Agent: Multi · Turns: Multi · Tools: Yes
- Reward phase: Both · Reward type: All
- Task: Math

### Tunix
- `https://github.com/google/tunix` · org: Google · date: 2025.4
- Paper(s): —
- Algorithm: PPO/GRPO/GSPO-Token/DAPO/Dr.GRPO · Agent: Single · Turns: Multi · Tools: Yes
- Reward phase: Outcome · Reward type: Rule/External
- Task: Math/Code/Game

### RL2
- `https://github.com/ChenmienTan/RL2` · org: Accio · date: 2025.4
- Paper(s): —
- Algorithm: Dr. GRPO/PPO/DPO · Agent: Single · Turns: Both · Tools: Yes
- Reward phase: Both · Reward type: Rule/Model/External
- Task: QA/Dialogue

### verifiers
- `https://github.com/willccbb/verifiers` · org: Individual · date: 2025.3
- Paper(s): —
- Algorithm: GRPO · Agent: Multi · Turns: Both · Tools: Code
- Reward phase: Outcome · Reward type: All
- Task: Reasoning/Math/Code

### prime-rl
- `https://github.com/PrimeIntellect-ai/prime-rl` · org: Prime Intellect · date: 2025.2
- Paper(s): —
- Algorithm: GRPO/PPO · Agent: Multi · Turns: Multi · Tools: Yes
- Reward phase: Outcome · Reward type: Model/External
- Task: Math/Code/Search

### oat
- `https://github.com/sail-sg/oat` · org: NUS/Sea AI · date: 2024.11
- Paper(s): [Paper](https://arxiv.org/abs/2411.01493)
- Algorithm: PPO/GRPO · Agent: Single · Turns: Multi · Tools: No
- Reward phase: Outcome · Reward type: External
- Task: Math/Alignment

### veRL
- `https://github.com/volcengine/verl` · org: ByteDance · date: 2024.9
- Paper(s): [Paper](https://arxiv.org/abs/2409.19256)
- Algorithm: PPO/GRPO · Agent: Single · Turns: Both · Tools: Yes
- Reward phase: Outcome · Reward type: All
- Task: Math/QA/Reasoning/Search

### OpenRLHF
- `https://github.com/OpenRLHF/OpenRLHF` · org: OpenRLHF · date: 2024.5
- Paper(s): [Paper](https://arxiv.org/abs/2405.11143)
- Algorithm: PPO/REINFORCE++/GRPO/DPO/IPO/KTO/RLOO · Agent: Multi · Turns: Both · Tools: Yes
- Reward phase: Both · Reward type: Rule/Model/External
- Task: Dialogue/Chat/Completion

### trl
- `https://github.com/huggingface/trl` · org: HuggingFace · date: 2019.11
- Paper(s): —
- Algorithm: PPO/GRPO/DPO · Agent: Single · Turns: Single · Tools: No
- Reward phase: Both · Reward type: Custom
- Task: QA
