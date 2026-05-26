# General / MultiTask Agents

Agents trained across many tasks/environments. Useful when you want one model that handles search + tool + code etc.

_Total: 21 entries._

## Contents

T2PO, StraTA, SDAR, SkillZero, MetaClaw, SkillRL, LLM-in-Sandbox, youtu-agent, DEPO, SPEAR, DeepAgent, AgentRL, AgentGym-RL, Agent_Foundation_Models, Trinity-RFT, SPA-RL-Agent, verl-agent, SkyRL, VAGEN, ART, OpenManus-RL.

### T2PO
- `https://github.com/WillDreamer/T2PO` · org: Academic (ICML 2026 Spotlight) · date: 2026.5
- Paper(s): [Paper](https://arxiv.org/abs/2605.02178)
- Algorithm: T²PO (token+turn uncertainty-guided) · Framework: veRL · Agent: Single · Turns: Multi · Tools: Yes (search, web, embodied)
- Reward phase: Both · Reward type: Rule
- Task: WebShop/ALFWorld/SearchQA/Embody/Game

### StraTA
- `https://github.com/xxyQwQ/StraTA` · org: Shanghai AI Lab / Oxford / Multi-institution · date: 2026.5
- Paper(s): [Paper](https://arxiv.org/abs/2605.06642)
- Algorithm: Hierarchical GRPO + Strategic Trajectory Abstraction · Framework: rLLM · Agent: Single · Turns: Multi · Tools: Yes (interactive long-horizon envs)
- Reward phase: Outcome · Reward type: Rule + Model (self-judge)
- Task: ALFWorld (93.1%)/WebShop (84.2%)/SciWorld (63.5%)

### SDAR
- `https://github.com/ZJU-REAL/SDAR` · org: Zhejiang University (ZJU-REAL) · date: 2026.5
- Paper(s): [Paper](https://arxiv.org/abs/2605.15155)
- Algorithm: Self-Distilled Agentic RL (GRPO + gated OPSD) · Framework: veRL (GiGPO-based) · Agent: Single · Turns: Multi · Tools: Yes (interactive envs)
- Reward phase: Outcome · Reward type: Rule
- Task: ALFWorld/WebShop/Search-QA

### SkillZero
- `https://github.com/ZJU-REAL/SkillZero` · org: Zhejiang University (ZJU-REAL) · date: 2026.4
- Paper(s): [Paper](https://arxiv.org/abs/2604.02268)
- Algorithm: In-Context Agentic RL (GRPO + skill-context curriculum withdrawal) · Framework: veRL (GiGPO-based) · Agent: Single · Turns: Multi · Tools: Yes (interactive envs + skill library)
- Reward phase: Outcome · Reward type: Rule
- Task: ALFWorld/WebShop/Search-QA

### MetaClaw
- `https://github.com/aiming-lab/MetaClaw` · org: UNC-Chapel Hill (AIMING Lab) · date: 2026.3
- Paper(s): [Paper](https://arxiv.org/abs/2603.17187)
- Algorithm: GRPO (LoRA) · Framework: Custom · Agent: Single · Turns: Multi · Tools: Yes (Skill-augmented)
- Reward phase: Process · Reward type: Model (PRM)
- Task: General Agentic

### SkillRL
- `https://github.com/aiming-lab/SkillRL` · org: UNC-Chapel Hill (AIMING Lab) · date: 2026.2
- Paper(s): [Paper](https://arxiv.org/abs/2602.08234)
- Algorithm: GRPO · Framework: Custom · Agent: Single · Turns: Multi · Tools: Yes (Web search, actions)
- Reward phase: Outcome · Reward type: Rule
- Task: ALFWorld/WebShop/Search

### LLM-in-Sandbox
- `https://github.com/llm-in-sandbox/llm-in-sandbox` · org: RUC/MSRA/THU · date: 2026.1
- Paper(s): [Paper](https://huggingface.co/papers/2601.16206)
- Algorithm: GRPO++ · Framework: rllm (w/ veRL) · Agent: Single · Turns: Multi · Tools: Yes (Code Sandbox w/ Terminal, File, Internet)
- Reward phase: Outcome · Reward type: Rule
- Task: Math/Physics/Chemistry/Biomedicine/Long-context/IF/SWE

### youtu-agent
- `https://github.com/TencentCloudADP/youtu-agent` · org: Tencent Youtu Lab · date: 2025.12
- Paper(s): [Paper](https://arxiv.org/abs/2512.24615)
- Algorithm: Training-Free GRPO · Framework: Custom · Agent: Single · Turns: Multi · Tools: Yes (Web search, code, file)
- Reward phase: Outcome · Reward type: Model/External
- Task: Deep Research/Data Analysis/Tool-use

### DEPO
- `https://github.com/OpenCausaLab/DEPO` · org: HKUST/SJTU · date: 2025.11
- Paper(s): [Paper](https://arxiv.org/abs/2511.15392)
- Algorithm: KTO + Efficiency Loss · Framework: LLaMA-Factory · Agent: Single · Turns: Multi · Tools: Yes
- Reward phase: Both · Reward type: Rule
- Task: Agent (BabyAI/WebShop)

### SPEAR
- `https://github.com/TencentYoutuResearch/SPEAR` · org: Tencent Youtu Lab · date: 2025.9
- Paper(s): [Paper](https://arxiv.org/abs/2509.22601)
- Algorithm: GRPO/GiGPO + SIL · Framework: veRL/verl-agent · Agent: Single · Turns: Multi · Tools: Yes (Search, Sandbox, Browser)
- Reward phase: Both · Reward type: Rule/External
- Task: Math/Agent

### DeepAgent
- `https://github.com/RUC-NLPIR/DeepAgent` · org: RUC/Xiaohongshu · date: 2025.10
- Paper(s): [Paper](https://arxiv.org/abs/2510.21618)
- Algorithm: ToolPO · Framework: Custom · Agent: Single · Turns: Multi · Tools: Yes (16,000+ RapidAPIs)
- Reward phase: Outcome · Reward type: Model
- Task: ToolBench/ALFWorld/WebShop/GAIA/HLE

### AgentRL
- `https://github.com/THUDM/AgentRL` · org: Tsinghua · date: 2025.10
- Paper(s): [Paper](https://arxiv.org/abs/2510.04206)
- Algorithm: GRPO/REINFORCE++/RLOO/ReMax/GAE · Framework: veRL · Agent: Single · Turns: Multi · Tools: Yes
- Reward phase: Outcome · Reward type: External
- Task: Agent Tasks

### AgentGym-RL
- `https://github.com/WooooDyy/AgentGym-RL` · org: Fudan University · date: 2025.9
- Paper(s): [Paper](https://arxiv.org/abs/2509.08755)
- Algorithm: PPO/GRPO/RLOO/REINFORCE++ · Framework: veRL · Agent: Single · Turns: Multi · Tools: Yes (Web, Search, Env APIs)
- Reward phase: Outcome · Reward type: Rule/Model/External
- Task: Web/Search/Game/Embodied/Science

### Agent_Foundation_Models
- `https://github.com/OPPO-PersonalAI/Agent_Foundation_Models` · org: OPPO Personal AI Lab · date: 2025.8
- Paper(s): [Paper](https://arxiv.org/abs/2508.13167)
- Algorithm: DAPO/PPO · Framework: veRL · Agent: Single · Turns: Single · Tools: Yes
- Reward phase: Outcome · Reward type: Rule/External
- Task: QA/Code/Math

### Trinity-RFT
- `https://github.com/modelscope/Trinity-RFT` · org: Alibaba · date: 2025.5
- Paper(s): [Paper](https://arxiv.org/abs/2505.17826)
- Algorithm: PPO/GRPO · Framework: veRL · Agent: Single · Turns: Both · Tools: Yes
- Reward phase: Outcome · Reward type: All
- Task: Math/TextGame/Web

### SPA-RL-Agent
- `https://github.com/WangHanLinHenry/SPA-RL-Agent` · org: PolyU · date: 2025.5
- Paper(s): [Paper](https://arxiv.org/abs/2505.20732)
- Algorithm: PPO · Framework: TRL · Agent: Single · Turns: Multi · Tools: No
- Reward phase: Process · Reward type: Model
- Task: Navigation/Web/TextGame

### verl-agent
- `https://github.com/langfengQ/verl-agent` · org: NTU/Skywork · date: 2025.5
- Paper(s): [Paper](https://arxiv.org/abs/2505.10978)
- Algorithm: PPO/GRPO/GiGPO/DAPO/RLOO/REINFORCE++ · Framework: veRL · Agent: Multi · Turns: Multi · Tools: Yes
- Reward phase: Both · Reward type: All
- Task: Phone Use/Math/Code/Web/TextGame

### SkyRL
- `https://github.com/NovaSky-AI/SkyRL` · org: UC Berkeley / NovaSky-AI · date: 2025.11
- Paper(s): [Paper](https://arxiv.org/abs/2511.16108)
- Algorithm: GRPO/PPO · Framework: Self (skyrl-train) · Agent: Single · Turns: Multi · Tools: Yes
- Reward phase: Both · Reward type: Rule/External/Custom
- Task: Long-horizon Agents (SWE-Bench/Search/Math/SQL)

### VAGEN
- `https://github.com/mll-lab-nu/VAGEN` · org: Northwestern University (mll-lab-nu) · date: 2025.10
- Paper(s): [Paper](https://arxiv.org/abs/2510.16907)
- Algorithm: PPO/GRPO (World Modeling RL) · Framework: veRL · Agent: Single · Turns: Multi · Tools: Yes
- Reward phase: Both · Reward type: All
- Task: Navigation/TextGame/Multimodal

### ART
- `https://github.com/OpenPipe/ART` · org: OpenPipe · date: 2025.3
- Paper(s): [Paper](https://github.com/OpenPipe/ART#-citation)
- Algorithm: GRPO · Framework: TRL · Agent: Multi · Turns: Multi · Tools: Yes
- Reward phase: Both · Reward type: All
- Task: TextGame

### OpenManus-RL
- `https://github.com/OpenManus/OpenManus-RL` · org: UIUC/MetaGPT · date: 2025.3
- Paper(s): —
- Algorithm: PPO/DPO/GRPO · Framework: Custom · Agent: Multi · Turns: Multi · Tools: Yes
- Reward phase: Outcome · Reward type: All
- Task: TextGame
