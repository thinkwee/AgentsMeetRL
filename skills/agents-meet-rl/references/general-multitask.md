# General / MultiTask Agents

Agents trained across many tasks/environments. Useful when you want one model that handles search + tool + code etc.

_Total: 21 entries._

## Contents

T2PO, StraTA, SDAR, SkillZero, MetaClaw, SkillRL, LLM-in-Sandbox, youtu-agent, DEPO, SPEAR, DeepAgent, AgentRL, AgentGym-RL, Agent_Foundation_Models, Trinity-RFT, SPA-RL-Agent, verl-agent, SkyRL, VAGEN, ART, OpenManus-RL.

### T2PO
- **Idea:** Two-level uncertainty control: triggers thinking interventions when token-level uncertainty gains plateau and resamples turns with negligible progress to cut wasted rollouts.
- `https://github.com/WillDreamer/T2PO` · org: Academic (ICML 2026 Spotlight) · date: 2026.5
- Paper(s): [Paper](https://arxiv.org/abs/2605.02178)
- Algorithm: T²PO (token+turn uncertainty-guided) · Framework: veRL · Agent: Single · Turns: Multi · Tools: Yes (search, web, embodied)
- Reward phase: Both · Reward type: Rule
- Task: WebShop/ALFWorld/SearchQA/Embody/Game

### StraTA
- **Idea:** Samples a compact high-level strategy from the initial state, conditions all actions on it, and jointly trains both via hierarchical GRPO rollouts for consistent long-horizon plans.
- `https://github.com/xxyQwQ/StraTA` · org: Shanghai AI Lab / Oxford / Multi-institution · date: 2026.5
- Paper(s): [Paper](https://arxiv.org/abs/2605.06642)
- Algorithm: Hierarchical GRPO + Strategic Trajectory Abstraction · Framework: rLLM · Agent: Single · Turns: Multi · Tools: Yes (interactive long-horizon envs)
- Reward phase: Outcome · Reward type: Rule + Model (self-judge)
- Task: ALFWorld (93.1%)/WebShop (84.2%)/SciWorld (63.5%)

### SDAR
- **Idea:** On-policy self-distillation as a sigmoid-gated auxiliary objective, amplifying teacher endorsements while softening rejections to stabilize multi-turn agent RL.
- `https://github.com/ZJU-REAL/SDAR` · org: Zhejiang University (ZJU-REAL) · date: 2026.5
- Paper(s): [Paper](https://arxiv.org/abs/2605.15155)
- Algorithm: Self-Distilled Agentic RL (GRPO + gated OPSD) · Framework: veRL (GiGPO-based) · Agent: Single · Turns: Multi · Tools: Yes (interactive envs)
- Reward phase: Outcome · Reward type: Rule
- Task: ALFWorld/WebShop/Search-QA

### SkillZero
- **Idea:** Dynamic curriculum that progressively withdraws in-context skill guidance during RL so skills internalize into model weights for zero-shot agent behavior.
- `https://github.com/ZJU-REAL/SkillZero` · org: Zhejiang University (ZJU-REAL) · date: 2026.4
- Paper(s): [Paper](https://arxiv.org/abs/2604.02268)
- Algorithm: In-Context Agentic RL (GRPO + skill-context curriculum withdrawal) · Framework: veRL (GiGPO-based) · Agent: Single · Turns: Multi · Tools: Yes (interactive envs + skill library)
- Reward phase: Outcome · Reward type: Rule
- Task: ALFWorld/WebShop/Search-QA

### MetaClaw
- **Idea:** Continual meta-learning co-evolving LLM policy and skill library: LLM-evolver synthesizes skills from failures plus gradient updates in idle windows.
- `https://github.com/aiming-lab/MetaClaw` · org: UNC-Chapel Hill (AIMING Lab) · date: 2026.3
- Paper(s): [Paper](https://arxiv.org/abs/2603.17187)
- Algorithm: GRPO (LoRA) · Framework: Custom · Agent: Single · Turns: Multi · Tools: Yes (Skill-augmented)
- Reward phase: Process · Reward type: Model (PRM)
- Task: General Agentic

### SkillRL
- **Idea:** Distills agent experience into a hierarchical, recursively-evolving SkillBank with adaptive retrieval that co-improves the RL policy while cutting token usage.
- `https://github.com/aiming-lab/SkillRL` · org: UNC-Chapel Hill (AIMING Lab) · date: 2026.2
- Paper(s): [Paper](https://arxiv.org/abs/2602.08234)
- Algorithm: GRPO · Framework: Custom · Agent: Single · Turns: Multi · Tools: Yes (Web search, actions)
- Reward phase: Outcome · Reward type: Rule
- Task: ALFWorld/WebShop/Search

### LLM-in-Sandbox
- **Idea:** RL trains LLMs to explore inside a code sandbox using only non-agentic data, eliciting general agentic ability across math/science/long-context/IF domains.
- `https://github.com/llm-in-sandbox/llm-in-sandbox` · org: RUC/MSRA/THU · date: 2026.1
- Paper(s): [Paper](https://huggingface.co/papers/2601.16206)
- Algorithm: GRPO++ · Framework: rllm (w/ veRL) · Agent: Single · Turns: Multi · Tools: Yes (Code Sandbox w/ Terminal, File, Internet)
- Reward phase: Outcome · Reward type: Rule
- Task: Math/Physics/Chemistry/Biomedicine/Long-context/IF/SWE

### youtu-agent
- **Idea:** Meta-agent auto-generates agent tools/prompts/configs, plus hybrid in-context practice and training-free GRPO that improves agents without weight updates.
- `https://github.com/TencentCloudADP/youtu-agent` · org: Tencent Youtu Lab · date: 2025.12
- Paper(s): [Paper](https://arxiv.org/abs/2512.24615)
- Algorithm: Training-Free GRPO · Framework: Custom · Agent: Single · Turns: Multi · Tools: Yes (Web search, code, file)
- Reward phase: Outcome · Reward type: Model/External
- Task: Deep Research/Data Analysis/Tool-use

### DEPO
- **Idea:** Dual-efficiency preference optimization jointly minimizing tokens-per-step and number-of-steps, rewarding concise reasoning and fewer actions in agent tasks.
- `https://github.com/OpenCausaLab/DEPO` · org: HKUST/SJTU · date: 2025.11
- Paper(s): [Paper](https://arxiv.org/abs/2511.15392)
- Algorithm: KTO + Efficiency Loss · Framework: LLaMA-Factory · Agent: Single · Turns: Multi · Tools: Yes
- Reward phase: Both · Reward type: Rule
- Task: Agent (BabyAI/WebShop)

### SPEAR
- **Idea:** Self-imitation with curriculum-scheduled entropy: intrinsic-reward exploration early, exploiting successful trajectories later, avoiding entropy collapse.
- `https://github.com/TencentYoutuResearch/SPEAR` · org: Tencent Youtu Lab · date: 2025.9
- Paper(s): [Paper](https://arxiv.org/abs/2509.22601)
- Algorithm: GRPO/GiGPO + SIL · Framework: veRL/verl-agent · Agent: Single · Turns: Multi · Tools: Yes (Search, Sandbox, Browser)
- Reward phase: Both · Reward type: Rule/External
- Task: Math/Agent

### DeepAgent
- **Idea:** End-to-end tool-reasoning agent with autonomous memory folding, trained via ToolPO using simulated APIs and tool-call advantage attribution for credit.
- `https://github.com/RUC-NLPIR/DeepAgent` · org: RUC/Xiaohongshu · date: 2025.10
- Paper(s): [Paper](https://arxiv.org/abs/2510.21618)
- Algorithm: ToolPO · Framework: Custom · Agent: Single · Turns: Multi · Tools: Yes (16,000+ RapidAPIs)
- Reward phase: Outcome · Reward type: Model
- Task: ToolBench/ALFWorld/WebShop/GAIA/HLE

### AgentRL
- **Idea:** Fully-asynchronous generation-training pipeline plus cross-policy sampling and task advantage normalization for stable multi-turn, multi-task agent RL.
- `https://github.com/THUDM/AgentRL` · org: Tsinghua · date: 2025.10
- Paper(s): [Paper](https://arxiv.org/abs/2510.04206)
- Algorithm: GRPO/REINFORCE++/RLOO/ReMax/GAE · Framework: veRL · Agent: Single · Turns: Multi · Tools: Yes
- Reward phase: Outcome · Reward type: External
- Task: Agent Tasks

### AgentGym-RL
- **Idea:** Trains agents via pure RL without SFT using ScalingInter-RL, which starts with restricted interactions then grows the horizon to prevent behavior collapse.
- `https://github.com/WooooDyy/AgentGym-RL` · org: Fudan University · date: 2025.9
- Paper(s): [Paper](https://arxiv.org/abs/2509.08755)
- Algorithm: PPO/GRPO/RLOO/REINFORCE++ · Framework: veRL · Agent: Single · Turns: Multi · Tools: Yes (Web, Search, Env APIs)
- Reward phase: Outcome · Reward type: Rule/Model/External
- Task: Web/Search/Game/Embodied/Science

### Agent_Foundation_Models
- **Idea:** Consolidates multi-agent systems into one model via multi-agent distillation into SFT trajectories plus agentic RL on chain-of-agents reasoning.
- `https://github.com/OPPO-PersonalAI/Agent_Foundation_Models` · org: OPPO Personal AI Lab · date: 2025.8
- Paper(s): [Paper](https://arxiv.org/abs/2508.13167)
- Algorithm: DAPO/PPO · Framework: veRL · Agent: Single · Turns: Single · Tools: Yes
- Reward phase: Outcome · Reward type: Rule/External
- Task: QA/Code/Math

### Trinity-RFT
- **Idea:** Unified modular RFT framework spanning sync/async, on/off-policy, and online/offline modes with integrated agent-environment data pipelines.
- `https://github.com/modelscope/Trinity-RFT` · org: Alibaba · date: 2025.5
- Paper(s): [Paper](https://arxiv.org/abs/2505.17826)
- Algorithm: PPO/GRPO · Framework: veRL · Agent: Single · Turns: Both · Tools: Yes
- Reward phase: Outcome · Reward type: All
- Task: Math/TextGame/Web

### SPA-RL-Agent
- **Idea:** Stepwise Progress Attribution: a learned progress estimator decomposes delayed task reward into per-step intermediate rewards for credit assignment in agent RL.
- `https://github.com/WangHanLinHenry/SPA-RL-Agent` · org: PolyU · date: 2025.5
- Paper(s): [Paper](https://arxiv.org/abs/2505.20732)
- Algorithm: PPO · Framework: TRL · Agent: Single · Turns: Multi · Tools: No
- Reward phase: Process · Reward type: Model
- Task: Navigation/Web/TextGame

### verl-agent
- **Idea:** GiGPO: two-level advantage (episode groups + anchor-state step groups) for fine-grained multi-turn credit assignment without extra models or rollouts.
- `https://github.com/langfengQ/verl-agent` · org: NTU/Skywork · date: 2025.5
- Paper(s): [Paper](https://arxiv.org/abs/2505.10978)
- Algorithm: PPO/GRPO/GiGPO/DAPO/RLOO/REINFORCE++ · Framework: veRL · Agent: Multi · Turns: Multi · Tools: Yes
- Reward phase: Both · Reward type: All
- Task: Phone Use/Math/Code/Web/TextGame

### SkyRL
- **Idea:** Optimized async pipeline dispatcher (1.55x speedup) plus AST-based tool-enhanced training, cutting long-horizon agent RL cost over 2x.
- `https://github.com/NovaSky-AI/SkyRL` · org: UC Berkeley / NovaSky-AI · date: 2025.11
- Paper(s): [Paper](https://arxiv.org/abs/2511.16108)
- Algorithm: GRPO/PPO · Framework: Self (skyrl-train) · Agent: Single · Turns: Multi · Tools: Yes
- Reward phase: Both · Reward type: Rule/External/Custom
- Task: Long-horizon Agents (SWE-Bench/Search/Math/SQL)

### VAGEN
- **Idea:** VLM agents trained as POMDP with explicit state-estimation/transition reasoning, a World Modeling Reward, and Bi-Level GAE for turn-aware credit assignment.
- `https://github.com/mll-lab-nu/VAGEN` · org: Northwestern University (mll-lab-nu) · date: 2025.10
- Paper(s): [Paper](https://arxiv.org/abs/2510.16907)
- Algorithm: PPO/GRPO (World Modeling RL) · Framework: veRL · Agent: Single · Turns: Multi · Tools: Yes
- Reward phase: Both · Reward type: All
- Task: Navigation/TextGame/Multimodal

### ART
- **Idea:** Client-server GRPO trainer adding RL to existing agents without GPU-infra hassle, plus RULER for automatic LLM-judged reward generation.
- `https://github.com/OpenPipe/ART` · org: OpenPipe · date: 2025.3
- Paper(s): [Paper](https://github.com/OpenPipe/ART#-citation)
- Algorithm: GRPO · Framework: TRL · Agent: Multi · Turns: Multi · Tools: Yes
- Reward phase: Both · Reward type: All
- Task: TextGame

### OpenManus-RL
- **Idea:** Open RL framework for LLM agents combining reasoning paradigms, diverse rollouts, agent reward models, and test-time trajectory scaling (PPO/DPO/GRPO).
- `https://github.com/OpenManus/OpenManus-RL` · org: UIUC/MetaGPT · date: 2025.3
- Paper(s): —
- Algorithm: PPO/DPO/GRPO · Framework: Custom · Agent: Multi · Turns: Multi · Tools: Yes
- Reward phase: Outcome · Reward type: All
- Task: TextGame
