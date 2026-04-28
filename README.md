<div align="center">
  <img src="logo.png" alt="NOVER Logo" width="500">
</div>

<div align="center">

![Base Framework](https://img.shields.io/badge/Base_Framework-19-BFA2DB?style=for-the-badge)
![General](https://img.shields.io/badge/General-17-4E6813?style=for-the-badge)
![Search & RAG](https://img.shields.io/badge/Search_&_RAG-37-845C40?style=for-the-badge)
![Web & GUI](https://img.shields.io/badge/Web_&_GUI-27-A259FF?style=for-the-badge)
<br>
![Tool](https://img.shields.io/badge/Tool-19-D89F7B?style=for-the-badge)
![Code & SWE](https://img.shields.io/badge/Code_&_SWE-22-A47B67?style=for-the-badge)
![Reasoning](https://img.shields.io/badge/Reasoning-18-FF69B4?style=for-the-badge)
![Multi-Agent](https://img.shields.io/badge/Multi--Agent-13-1F4CAD?style=for-the-badge)
<br>
![Memory](https://img.shields.io/badge/Memory-5-007a88?style=for-the-badge)
![Embodied](https://img.shields.io/badge/Embodied-3-C0C5CE?style=for-the-badge)
![Domain-Specific](https://img.shields.io/badge/Domain--Specific-9-ffc884?style=for-the-badge)
![Reward & Training](https://img.shields.io/badge/Reward_&_Training-6-9B59B6?style=for-the-badge)
<br>
![Safety](https://img.shields.io/badge/Safety-9-E74C3C?style=for-the-badge)
![VLM Agent](https://img.shields.io/badge/VLM_Agent-16-2ECC71?style=for-the-badge)
![Self-Evolution](https://img.shields.io/badge/Self--Evolution-9-F39C12?style=for-the-badge)
![Environment](https://img.shields.io/badge/Environment-46-FA5A4C?style=for-the-badge)

</div>

<div align="center">

[![Interactive Dashboard](https://img.shields.io/badge/📊_Interactive_Dashboard-Visit_Website-blue?style=for-the-badge)](https://thinkwee.top/amr/)

</div>

# When LLM Agents Meet Reinforcement Learning

**AgentsMeetRL** is an awesome list that summarizes **open-source repositories** for training LLM Agents using reinforcement learning:
 - 🤖 The criteria for identifying an agent project are that it must have at least one of the following: multi-turn interactions or tool use (so TIR projects, Tool-Integrated Reasoning, are considered in this repo).
 - ⚠️ This project is based on code analysis from open-source repositories using LLM coding agents, which may contain unfaithful cases. Although manually reviewed, there may still be omissions. If you find any errors, please don't hesitate to let us know immediately through issues or PRs - we warmly welcome them!
 - 🚀 We particularly focus on the reinforcement learning frameworks, RL algorithms, rewards, and environments that projects depend on, for everyone's reference on how these excellent open-source projects make their technical choices. See [Click to view technical details] under each table.
 - 📅 Last updated: 2026-04-28
 - 🤗 Feel free to submit your own projects anytime - we welcome contributions!

Taxonomy:
 - **Base Framework**: General-purpose RL training frameworks for LLM agents (e.g., veRL, OpenRLHF, trl)
 - **General/MultiTask**: Agent systems trained/evaluated across multiple tasks or environments
 - **Search & RAG**: Search-augmented reasoning agents that use retrieval tools to enhance LLM reasoning
 - **Web & GUI**: Agents that interact with web browsers, mobile/desktop GUIs, or operating systems
 - **Tool-Use**: Agents trained to invoke external tools (APIs, code executors, MCP, etc.)
 - **Code & SWE**: Software engineering and code generation agents
 - **Reasoning**: Reasoning agents with tool-integrated or multi-turn reasoning (math, QA, visual)
 - **Multi-Agent RL**: Multi-agent collaboration, negotiation, or credit assignment via RL
 - **Memory**: Agents that learn to manage, retrieve, or evolve memory
 - **Embodied**: Agents operating in embodied/physical simulation environments
 - **Domain-Specific**: RL agents for specialized domains (medical, OS tuning, etc.)
 - **Reward & Training**: Process/outcome reward models and training methodologies for agents
 - **Safety**: RL for agent safety alignment, adversarial red-teaming, and jailbreak defense/attack
 - **VLM Agent**: Vision-language model agents trained with RL for multimodal interaction
 - **Self-Evolution**: Agents that self-evolve via RL feedback loops (⚠️ definition still evolving in the community)
 - **Environment**: Benchmarks, gyms, and sandbox environments for agent training/evaluation

Some Enumeration:
 - Enumeration for Reward Type:
   - External Verifier: e.g., a compiler or math solver
   - Rule-Based: e.g., a LaTeX parser with exact match scoring
   - Model-Based: e.g., a trained verifier LLM or reward LLM
   - Custom

---

## Updates
- 📢 **2026-04 Update**: Added 67 new repositories covering Apr 2025 – Apr 2026 across nearly every category (notably VLM Agent +9, Search & RAG +10, Web & GUI +7, Tool-Use +7). Also reclassified SkyRL (→ General) and SPIRAL (→ Multi-Agent), and updated the VAGEN entry to its NeurIPS'25 upstream repo.
- 📢 **2026-03 Update**: Restructured taxonomy from 12 to 16 categories (added Multi-Agent RL, Reward & Training, Safety, VLM Agent, Self-Evolution, Domain-Specific; merged GUI into Web & GUI; retired TextGame/Biomedical). Added ~70 new repositories covering Sep 2025 – Mar 2026, growing the total from ~134 to 205.

## 🔧 Base Framework


| Github Repo | 🌟 Stars | Date | Org | Paper Link |
| :----: | :----: | :----: |  :----: | :----: |
| [Open-AgentRL](https://github.com/Gen-Verse/Open-AgentRL) | <img src="https://img.shields.io/github/stars/Gen-Verse/Open-AgentRL?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2026.2 | Gen-Verse | [Paper](https://arxiv.org/abs/2602.02488) |
| [OpenClaw-RL](https://github.com/Gen-Verse/OpenClaw-RL) | <img src="https://img.shields.io/github/stars/Gen-Verse/OpenClaw-RL?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2026.3 | Gen-Verse | [Paper](https://arxiv.org/abs/2603.10165) |
| [Claw-R1](https://github.com/AgentR1/Claw-R1) | <img src="https://img.shields.io/github/stars/AgentR1/Claw-R1?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2026.3 | USTC | -- |
| [prime-rl](https://github.com/PrimeIntellect-ai/prime-rl) | <img src="https://img.shields.io/github/stars/PrimeIntellect-ai/prime-rl?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.2 | Prime Intellect | -- |
| [NeMo-RL](https://github.com/NVIDIA-NeMo/RL) | <img src="https://img.shields.io/github/stars/NVIDIA-NeMo/RL?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2026.1 | NVIDIA | -- |
| [RLinf](https://github.com/RLinf/RLinf) | <img src="https://img.shields.io/github/stars/RLinf/RLinf?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.8 | Tsinghua/Infinigence AI/PKU | [Paper](https://arxiv.org/abs/2509.15965) |
| [siiRL](https://github.com/sii-research/siiRL) | <img src="https://img.shields.io/github/stars/sii-research/siiRL?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.7 | Shanghai Innovation Institute | [Paper](https://arxiv.org/abs/2507.13833) |
| [slime](https://github.com/THUDM/slime) | ![](https://img.shields.io/github/stars/THUDM/slime?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700) | 2025.6 | Tsinghua University (THUDM) | [blog](https://lmsys.org/blog/2025-07-09-slime/) |
| [agent-lightning](https://github.com/microsoft/agent-lightning) | <img src="https://img.shields.io/github/stars/microsoft/agent-lightning?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.6 | Microsoft Research | [Paper](https://arxiv.org/abs/2508.03680) |
| [AReaL](https://github.com/inclusionAI/AReaL) | <img src="https://img.shields.io/github/stars/inclusionAI/AReaL?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.6 | AntGroup/Tsinghua | [Paper](https://arxiv.org/pdf/2505.24298) |
| [ROLL](https://github.com/alibaba/ROLL) | <img src="https://img.shields.io/github/stars/alibaba/ROLL?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.6 | Alibaba | [Paper](https://arxiv.org/pdf/2506.06122) |
| [MARTI](https://github.com/TsinghuaC3I/MARTI) | <img src="https://img.shields.io/github/stars/TsinghuaC3I/MARTI?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.5 | Tsinghua | -- |
| [Tunix](https://github.com/google/tunix) | <img src="https://img.shields.io/github/stars/google/tunix?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.4 | Google | -- |
| [RL2](https://github.com/ChenmienTan/RL2) | <img src="https://img.shields.io/github/stars/ChenmienTan/RL2?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.4 | Accio | – |
| [verifiers](https://github.com/willccbb/verifiers) | <img src="https://img.shields.io/github/stars/willccbb/verifiers?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.3 | Individual | -- |
| [oat](https://github.com/sail-sg/oat) | <img src="https://img.shields.io/github/stars/sail-sg/oat?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2024.11 | NUS/Sea AI | [Paper](https://arxiv.org/pdf/2411.01493) |
| [veRL](https://github.com/volcengine/verl) | <img src="https://img.shields.io/github/stars/volcengine/verl?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2024.10 | ByteDance | [Paper](https://arxiv.org/pdf/2409.19256) |
| [OpenRLHF](https://github.com/OpenRLHF/OpenRLHF) | <img src="https://img.shields.io/github/stars/OpenRLHF/OpenRLHF?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2023.7 | OpenRLHF | [Paper](https://arxiv.org/abs/2405.11143) |
| [trl](https://github.com/huggingface/trl) | <img src="https://img.shields.io/github/stars/huggingface/trl?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2019.11 | HuggingFace | -- |

<details>
<summary>📋 Click to view technical details</summary>

| Github Repo | RL Algorithm | Single/Multi Agent | Outcome/Process Reward | Single/Multi Turn | Task | Reward Type | Tool usage |
| :----: | :----: | :----: | :----: | :----: | :----: | :----: | :----: |
| [Open-AgentRL](https://github.com/Gen-Verse/Open-AgentRL) | GRPO-TCR | Single | Both | Multi | Reasoning/GUI/Coding | Model (PRM) | Yes (SandboxFusion) |
| [OpenClaw-RL](https://github.com/Gen-Verse/OpenClaw-RL) | GRPO/OPD | Both | Both | Multi | Terminal/GUI/SWE/Tool-call | Model/External | Yes |
| [Claw-R1](https://github.com/AgentR1/Claw-R1) | Generic RL Framework | Multi | Both | Multi | General Agent | All | Yes (Framework-agnostic) |
| [prime-rl](https://github.com/PrimeIntellect-ai/prime-rl) | GRPO/PPO | Multi | Outcome | Multi | Math/Code/Search | Model/External | Yes |
| [NeMo-RL](https://github.com/NVIDIA-NeMo/RL) | GRPO/DAPO/GDPO/DPO | Single | Outcome | Multi | Math/Reasoning/Code | Rule/External | No |
| [RLinf](https://github.com/RLinf/RLinf) | PPO/GRPO/DAPO/SAC/REINFORCE++/CrossQ/RLPD | Both | Both | Multi | Robotics/Math/Code/QA/VQA | All (Rule/Model/External) | Yes |
| [siiRL](https://github.com/sii-research/siiRL) | PPO/GRPO/CPGD/MARFT | Multi | Both | Multi | LLM/VLM/LLM-MAS PostTraining | Model/Rule | Planned |
| [slime](https://github.com/THUDM/slime) | GRPO/GSPO/REINFORCE++ | Single | Both | Both | Math/Code | External Verifier | Yes |
| [agent-lightning](https://github.com/microsoft/agent-lightning) | PPO/Custom/Automatic Prompt Optimization | Multi | Outcome | Multi | Calculator/SQL | Model/External/Rule | Yes |
| [AReaL](https://github.com/inclusionAI/AReaL) | PPO | Both | Outcome | Both | Math/Code | External | Yes |
| [ROLL](https://github.com/alibaba/ROLL) | PPO/GRPO/Reinforce++/TOPR/RAFT++ | Multi | Both | Multi | Math/QA/Code/Alignment | All | Yes |
| [MARTI](https://github.com/TsinghuaC3I/MARTI) | PPO/GRPO/REINFORCE++/TTRL | Multi | Both | Multi | Math | All | Yes |
| [Tunix](https://github.com/google/tunix) | PPO/GRPO/GSPO-Token/DAPO/Dr.GRPO | Single | Outcome | Multi | Math/Code/Game | Rule/External | Yes |
| [RL2](https://github.com/ChenmienTan/RL2) | Dr. GRPO/PPO/DPO | Single | Both | Both | QA/Dialogue | Rule/Model/External | Yes |
| [verifiers](https://github.com/willccbb/verifiers) | GRPO | Multi | Outcome | Both | Reasoning/Math/Code | All | Code |
| [oat](https://github.com/sail-sg/oat) | PPO/GRPO | Single | Outcome | Multi | Math/Alignment | External | No |
| [veRL](https://github.com/volcengine/verl) | PPO/GRPO | Single | Outcome | Both | Math/QA/Reasoning/Search | All | Yes |
| [OpenRLHF](https://github.com/OpenRLHF/OpenRLHF) | PPO/REINFORCE++/GRPO/DPO/IPO/KTO/RLOO | Multi | Both | Both | Dialogue/Chat/Completion | Rule/Model/External | Yes |
| [trl](https://github.com/huggingface/trl) | PPO/GRPO/DPO | Single | Both | Single | QA | Custom | No |

</details>

## 💪 General/MultiTask

| Github Repo | 🌟 Stars | Date | Org | Paper Link | RL Framework |
| :----: | :----: | :----: |  :----: | :----: | :----: |
| [MetaClaw](https://github.com/aiming-lab/MetaClaw) | <img src="https://img.shields.io/github/stars/aiming-lab/MetaClaw?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2026.3 | UNC-Chapel Hill (AIMING Lab) | [Paper](https://arxiv.org/abs/2603.17187) | Custom |
| [SkillRL](https://github.com/aiming-lab/SkillRL) | <img src="https://img.shields.io/github/stars/aiming-lab/SkillRL?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2026.2 | UNC-Chapel Hill (AIMING Lab) | [Paper](https://arxiv.org/abs/2602.08234) | Custom |
| [LLM-in-Sandbox](https://github.com/llm-in-sandbox/llm-in-sandbox) | <img src="https://img.shields.io/github/stars/llm-in-sandbox/llm-in-sandbox?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2026.1 | RUC/MSRA/THU | [Paper](https://huggingface.co/papers/2601.16206) | rllm (w/ veRL) |
| [youtu-agent](https://github.com/TencentCloudADP/youtu-agent) | <img src="https://img.shields.io/github/stars/TencentCloudADP/youtu-agent?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.12 | Tencent Youtu Lab | [Paper](https://arxiv.org/abs/2512.24615) | Custom |
| [DEPO](https://github.com/OpenCausaLab/DEPO) | <img src="https://img.shields.io/github/stars/OpenCausaLab/DEPO?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.11 | HKUST/SJTU | [Paper](https://arxiv.org/abs/2511.15392) | LLaMA-Factory |
| [SPEAR](https://github.com/TencentYoutuResearch/SPEAR) | <img src="https://img.shields.io/github/stars/TencentYoutuResearch/SPEAR?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.10 | Tencent Youtu Lab | [Paper](https://arxiv.org/abs/2509.22601) | veRL/verl-agent |
| [DeepAgent](https://github.com/RUC-NLPIR/DeepAgent) | <img src="https://img.shields.io/github/stars/RUC-NLPIR/DeepAgent?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.10 | RUC/Xiaohongshu | [Paper](https://arxiv.org/abs/2510.21618) | Custom |
| [AgentRL](https://github.com/THUDM/AgentRL) | <img src="https://img.shields.io/github/stars/THUDM/AgentRL?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.9 | Tsinghua | [Paper](https://arxiv.org/abs/2510.04206) | veRL |
| [AgentGym-RL](https://github.com/WooooDyy/AgentGym-RL) | <img src="https://img.shields.io/github/stars/WooooDyy/AgentGym-RL?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.9 | Fudan University | [Paper](https://arxiv.org/abs/2509.08755) | veRL |
| [Agent_Foundation_Models](https://github.com/OPPO-PersonalAI/Agent_Foundation_Models) | <img src="https://img.shields.io/github/stars/OPPO-PersonalAI/Agent_Foundation_Models?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.8 | OPPO Personal AI Lab | [Paper](https://arxiv.org/abs/2508.13167) | veRL |
| [Trinity-RFT](https://github.com/modelscope/Trinity-RFT) | <img src="https://img.shields.io/github/stars/modelscope/Trinity-RFT?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.5 | Alibaba | [Paper](https://arxiv.org/pdf/2505.17826) | veRL |
| [SPA-RL-Agent](https://github.com/WangHanLinHenry/SPA-RL-Agent) | <img src="https://img.shields.io/github/stars/WangHanLinHenry/SPA-RL-Agent?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.5 | PolyU | [Paper](https://arxiv.org/pdf/2505.20732) | TRL |
| [verl-agent](https://github.com/langfengQ/verl-agent) | <img src="https://img.shields.io/github/stars/langfengQ/verl-agent?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.5 | NTU/Skywork | [Paper](https://arxiv.org/pdf/2505.10978) | veRL |
| [SkyRL](https://github.com/NovaSky-AI/SkyRL) | <img src="https://img.shields.io/github/stars/NovaSky-AI/SkyRL?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.4 | UC Berkeley / NovaSky-AI | [Paper](https://arxiv.org/abs/2511.16108) | Self (skyrl-train) |
| [VAGEN](https://github.com/mll-lab-nu/VAGEN) | <img src="https://img.shields.io/github/stars/mll-lab-nu/VAGEN?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.3 | Northwestern University (mll-lab-nu) | [Paper](https://arxiv.org/abs/2510.16907) | veRL |
| [ART](https://github.com/OpenPipe/ART) | <img src="https://img.shields.io/github/stars/OpenPipe/ART?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.3 | OpenPipe | [Paper](https://github.com/OpenPipe/ART#-citation) | TRL |
| [OpenManus-RL](https://github.com/OpenManus/OpenManus-RL) | <img src="https://img.shields.io/github/stars/OpenManus/OpenManus-RL?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.3 | UIUC/MetaGPT | -- | Custom |

<details>
<summary>📋 Click to view technical details</summary>

| Github Repo | RL Algorithm | Single/Multi Agent | Outcome/Process Reward | Single/Multi Turn | Task | Reward Type | Tool usage |
| :----: | :----: | :----: | :----: | :----: | :----: | :----: | :----: |
| [MetaClaw](https://github.com/aiming-lab/MetaClaw) | GRPO (LoRA) | Single | Process | Multi | General Agentic | Model (PRM) | Yes (Skill-augmented) |
| [SkillRL](https://github.com/aiming-lab/SkillRL) | GRPO | Single | Outcome | Multi | ALFWorld/WebShop/Search | Rule | Yes (Web search, actions) |
| [LLM-in-Sandbox](https://github.com/llm-in-sandbox/llm-in-sandbox) | GRPO++ | Single | Outcome | Multi | Math/Physics/Chemistry/Biomedicine/Long-context/IF/SWE | Rule | Yes (Code Sandbox w/ Terminal, File, Internet) |
| [youtu-agent](https://github.com/TencentCloudADP/youtu-agent) | Training-Free GRPO | Single | Outcome | Multi | Deep Research/Data Analysis/Tool-use | Model/External | Yes (Web search, code, file) |
| [DEPO](https://github.com/OpenCausaLab/DEPO) | KTO + Efficiency Loss | Single | Both | Multi | Agent (BabyAI/WebShop) | Rule | Yes |
| [SPEAR](https://github.com/TencentYoutuResearch/SPEAR) | GRPO/GiGPO + SIL | Single | Both | Multi | Math/Agent | Rule/External | Yes (Search, Sandbox, Browser) |
| [DeepAgent](https://github.com/RUC-NLPIR/DeepAgent) | ToolPO | Single | Outcome | Multi | ToolBench/ALFWorld/WebShop/GAIA/HLE | Model | Yes (16,000+ RapidAPIs) |
| [AgentRL](https://github.com/THUDM/AgentRL) | GRPO/REINFORCE++/RLOO/ReMax/GAE | Single | Outcome | Multi | Agent Tasks | External | Yes |
| [AgentGym-RL](https://github.com/WooooDyy/AgentGym-RL) | PPO/GRPO/RLOO/REINFORCE++ | Single | Outcome | Multi | Web/Search/Game/Embodied/Science | Rule/Model/External | Yes (Web, Search, Env APIs) |
| [Agent_Foundation_Models](https://github.com/OPPO-PersonalAI/Agent_Foundation_Models) | DAPO/PPO | Single | Outcome | Single | QA/Code/Math | Rule/External | Yes |
| [Trinity-RFT](https://github.com/modelscope/Trinity-RFT) | PPO/GRPO | Single | Outcome | Both | Math/TextGame/Web | All | Yes |
| [SPA-RL-Agent](https://github.com/WangHanLinHenry/SPA-RL-Agent) | PPO | Single | Process | Multi | Navigation/Web/TextGame | Model | No |
| [verl-agent](https://github.com/langfengQ/verl-agent) | PPO/GRPO/GiGPO/DAPO/RLOO/REINFORCE++ | Multi | Both | Multi | Phone Use/Math/Code/Web/TextGame | All | Yes |
| [SkyRL](https://github.com/NovaSky-AI/SkyRL) | GRPO/PPO | Single | Both | Multi | Long-horizon Agents (SWE-Bench/Search/Math/SQL) | Rule/External/Custom | Yes |
| [VAGEN](https://github.com/mll-lab-nu/VAGEN) | PPO/GRPO (World Modeling RL) | Single | Both | Multi | Navigation/TextGame/Multimodal | All | Yes |
| [ART](https://github.com/OpenPipe/ART) | GRPO | Multi | Both | Multi | TextGame | All | Yes |
| [OpenManus-RL](https://github.com/OpenManus/OpenManus-RL) | PPO/DPO/GRPO | Multi | Outcome | Multi | TextGame | All | Yes |

</details>

## 🔍 Search & RAG Agent


| Github Repo | 🌟 Stars | Date | Org | Paper Link | RL Framework |
| :----: | :----: | :----: |  :----: | :----: | :----: |
| [ProRAG](https://github.com/lilinwz/ProRAG) | <img src="https://img.shields.io/github/stars/lilinwz/ProRAG?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2026.1 | RUC | [Paper](https://arxiv.org/abs/2601.21912) | Custom |
| [MemSearcher](https://github.com/icip-cas/MemSearcher) | <img src="https://img.shields.io/github/stars/icip-cas/MemSearcher?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.11 | CAS | [Paper](https://arxiv.org/abs/2511.02805) | Custom |
| [DR-Venus](https://github.com/inclusionAI/DR-Venus) | <img src="https://img.shields.io/github/stars/inclusionAI/DR-Venus?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2026.4 | Ant Group (inclusionAI) | [Paper](https://arxiv.org/abs/2604.19859) | veRL (IGPO-based) |
| [IGPO](https://github.com/GuoqingWang1/IGPO) | <img src="https://img.shields.io/github/stars/GuoqingWang1/IGPO?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.10 | Ant Group | [Paper](https://arxiv.org/abs/2510.14967) (ICLR 2026) | veRL |
| [ReSeek](https://github.com/TencentBAC/ReSeek) | <img src="https://img.shields.io/github/stars/TencentBAC/ReSeek?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.10 | Tencent PCG BAC/Tsinghua University | [Paper](https://arxiv.org/abs/2510.00568) | veRL |
| [AutoGraph-R1](https://github.com/HKUST-KnowComp/AutoGraph-R1) | <img src="https://img.shields.io/github/stars/HKUST-KnowComp/AutoGraph-R1?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.10 | HKUST KnowComp | [Paper](https://arxiv.org/abs/2510.15339) | Custom |
| [Tree-GRPO](https://github.com/AMAP-ML/Tree-GRPO) | <img src="https://img.shields.io/github/stars/AMAP-ML/Tree-GRPO?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.9 | AMAP | [Paper](https://arxiv.org/abs/2509.21240) | veRL |
| [ASearcher](https://github.com/inclusionAI/ASearcher) | <img src="https://img.shields.io/github/stars/inclusionAI/ASearcher?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.8 | Ant Research RL Lab <br> Tsinghua University & UW | [Paper](https://arxiv.org/abs/2508.07976) | RealHF/AReaL |
| [Graph-R1](https://github.com/LHRLAB/Graph-R1) | <img src="https://img.shields.io/github/stars/LHRLAB/Graph-R1?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.7 | BUPT/NTU/NUS | [Paper](https://arxiv.org/abs/2507.21892) | veRL |
| [Kimi-Researcher](https://github.com/moonshotai/Kimi-Researcher) | <img src="https://img.shields.io/github/stars/moonshotai/Kimi-Researcher?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.6 | Moonshot AI | [blog](https://moonshotai.github.io/Kimi-Researcher/) | Custom |
| [R-Search](https://github.com/QingFei1/R-Search) | <img src="https://img.shields.io/github/stars/QingFei1/R-Search?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.6 | Individual | -- | veRL |
| [R1-Searcher-plus](https://github.com/RUCAIBox/R1-Searcher-plus) | <img src="https://img.shields.io/github/stars/RUCAIBox/R1-Searcher-plus?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.5 | RUC | [Paper](https://arxiv.org/pdf/2505.17005) | Custom |
| [StepSearch](https://github.com/Zillwang/StepSearch) | <img src="https://img.shields.io/github/stars/Zillwang/StepSearch?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.5 | SenseTime | [Paper](https://arxiv.org/pdf/2505.15107) | veRL |
| [AutoRefine](https://github.com/syr-cn/AutoRefine) | <img src="https://img.shields.io/github/stars/syr-cn/AutoRefine?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.5 | USTC | [Paper](https://www.arxiv.org/pdf/2505.11277) | veRL |
| [ZeroSearch](https://github.com/Alibaba-NLP/ZeroSearch) | <img src="https://img.shields.io/github/stars/Alibaba-NLP/ZeroSearch?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.5 | Alibaba |[Paper](https://arxiv.org/pdf/2505.04588) | veRL |
| [ReasonRAG](https://github.com/wlzhang2020/ReasonRAG) | <img src="https://img.shields.io/github/stars/wlzhang2020/ReasonRAG?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.5 | CityU HK / Huawei | [Paper](https://arxiv.org/abs/2505.14069) | Custom |
| [Agentic-RAG-R1](https://github.com/jiangxinke/Agentic-RAG-R1) | <img src="https://img.shields.io/github/stars/jiangxinke/Agentic-RAG-R1?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.12 | PKU | -- | Custom |
| [WebThinker](https://github.com/RUC-NLPIR/WebThinker) | <img src="https://img.shields.io/github/stars/RUC-NLPIR/WebThinker?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.4 | RUC | [Paper](https://arxiv.org/pdf/2504.21776) | Custom |
| [DeepResearcher](https://github.com/GAIR-NLP/DeepResearcher) | <img src="https://img.shields.io/github/stars/GAIR-NLP/DeepResearcher?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.4 | SJTU | [Paper](https://arxiv.org/pdf/2504.03160) | veRL |
| [Search-R1](https://github.com/PeterGriffinJin/Search-R1) | <img src="https://img.shields.io/github/stars/PeterGriffinJin/Search-R1?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.3 | UIUC/Google | [paper1](https://arxiv.org/pdf/2503.09516), [paper2](https://arxiv.org/pdf/2505.15117) | veRL |
| [R1-Searcher](https://github.com/RUCAIBox/R1-Searcher) | <img src="https://img.shields.io/github/stars/RUCAIBox/R1-Searcher?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.3 | RUC | [Paper](https://arxiv.org/pdf/2503.05592) | OpenRLHF |
| [C-3PO](https://github.com/Chen-GX/C-3PO) | <img src="https://img.shields.io/github/stars/Chen-GX/C-3PO?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.2 | Alibaba | [Paper](https://arxiv.org/pdf/2502.06205) | OpenRLHF |
| [DeepRetrieval](https://github.com/pat-jj/DeepRetrieval) | <img src="https://img.shields.io/github/stars/pat-jj/DeepRetrieval?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.2 | UIUC | [Paper](https://arxiv.org/abs/2503.00223) | veRL |
| [SSRL](https://github.com/TsinghuaC3I/SSRL) | <img src="https://img.shields.io/github/stars/TsinghuaC3I/SSRL?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.8 | Tsinghua | [Paper](https://arxiv.org/abs/2508.10874) | Custom |
| [Research-Venus](https://github.com/antgroup/Research-Venus) | <img src="https://img.shields.io/github/stars/antgroup/Research-Venus?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.8 | Ant Group | [Paper](https://arxiv.org/abs/2508.12800) | Custom |
| [DeepResearch](https://github.com/Alibaba-NLP/DeepResearch) | <img src="https://img.shields.io/github/stars/Alibaba-NLP/DeepResearch?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.9 | Alibaba/Tongyi Lab | [Paper](https://arxiv.org/abs/2510.24701) | Custom |
| [DeepDive](https://github.com/THUDM/DeepDive) | <img src="https://img.shields.io/github/stars/THUDM/DeepDive?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.9 | Tsinghua/THUDM | [Paper](https://arxiv.org/abs/2509.10446) | Custom |
| [O-Researcher](https://github.com/OPPO-PersonalAI/O-Researcher) | <img src="https://img.shields.io/github/stars/OPPO-PersonalAI/O-Researcher?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2026.1 | OPPO PersonalAI Lab | [Paper](https://arxiv.org/abs/2601.03743) | Custom |
| [DR Tulu](https://github.com/rlresearch/dr-tulu) | <img src="https://img.shields.io/github/stars/rlresearch/dr-tulu?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.11 | AI2 / UW / CMU / MIT | [Paper](https://arxiv.org/abs/2511.19399) | Open-Instruct |
| [WebSeer](https://github.com/99hgz/WebSeer) | <img src="https://img.shields.io/github/stars/99hgz/WebSeer?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.10 | Individual | [Paper](https://arxiv.org/abs/2510.18798) | veRL |
| [HiPRAG](https://github.com/qualidea1217/HiPRAG) | <img src="https://img.shields.io/github/stars/qualidea1217/HiPRAG?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.10 | Individual | [Paper](https://arxiv.org/abs/2510.07794) | veRL |
| [VRAG](https://github.com/Alibaba-NLP/VRAG) | <img src="https://img.shields.io/github/stars/Alibaba-NLP/VRAG?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.5 | USTC / Tongyi Lab, Alibaba | [Paper](https://arxiv.org/abs/2505.22019) | veRL |
| [MaskSearch](https://github.com/Alibaba-NLP/MaskSearch) | <img src="https://img.shields.io/github/stars/Alibaba-NLP/MaskSearch?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.5 | Tongyi Lab, Alibaba | [Paper](https://arxiv.org/abs/2505.20285) | DAPO / veRL |
| [R3-RAG](https://github.com/Yuan-Li-FNLP/R3-RAG) | <img src="https://img.shields.io/github/stars/Yuan-Li-FNLP/R3-RAG?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.5 | Fudan NLP | [Paper](https://arxiv.org/abs/2505.23794) | OpenRLHF |
| [O2-Searcher](https://github.com/KnowledgeXLab/O2-Searcher) | <img src="https://img.shields.io/github/stars/KnowledgeXLab/O2-Searcher?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.5 | KnowledgeXLab | [Paper](https://arxiv.org/abs/2505.16582) | veRL |
| [s3](https://github.com/pat-jj/s3) | <img src="https://img.shields.io/github/stars/pat-jj/s3?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.5 | UIUC | [Paper](https://arxiv.org/abs/2505.14146) | veRL |
| [knowledge-r1](https://github.com/hzy312/knowledge-r1) | <img src="https://img.shields.io/github/stars/hzy312/knowledge-r1?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.5 | CAS / UCAS | [Paper](https://arxiv.org/abs/2505.07596) | veRL |

<details>
<summary>📋 Click to view technical details</summary>

| Github Repo | RL Algorithm | Single/Multi Agent | Outcome/Process Reward | Single/Multi Turn | Task | Reward Type | Tool usage |
| :----: | :----: | :----: | :----: | :----: | :----: | :----: | :----: |
| [ProRAG](https://github.com/lilinwz/ProRAG) | GRPO + DGA (dual-granularity advantage) | Single | Both | Multi | Multi-hop RAG | Model (PRM via MCTS) | Yes (Retrieval) |
| [MemSearcher](https://github.com/icip-cas/MemSearcher) | Multi-context GRPO | Single | Outcome | Multi | Search/QA + Memory | Rule/Model | Yes (Web search + Memory) |
| [DR-Venus](https://github.com/inclusionAI/DR-Venus) | GRPO + IGPO (info-gain turn-level) w/ agentic SFT | Single | Both | Multi | Edge-scale Deep Research (4B) | Intrinsic (info-gain) + Rule (format) | Yes (Search/Browse) |
| [IGPO](https://github.com/GuoqingWang1/IGPO) | GRPO + IGPO (Information Gain turn-level reward) | Single | Both | Multi | Multi-turn Search Agent (BrowseComp/-ZH) | Intrinsic (belief Δ) + Outcome | Yes (Search) |
| [ReSeek](https://github.com/TencentBAC/ReSeek) | GRPO/PPO | Single | Both | Multi | QA/Search | Rule | Search/JUDGE |
| [AutoGraph-R1](https://github.com/HKUST-KnowComp/AutoGraph-R1) | GRPO (via VeRL) | Single | Outcome | Multi | KG Construction for QA | Rule | Yes (Graph retrieval) |
| [Tree-GRPO](https://github.com/AMAP-ML/Tree-GRPO) | GRPO/Tree-GRPO | Single | Outcome | Multi | Search | Rule | Search |
| [ASearcher](https://github.com/inclusionAI/ASearcher) | PPO/GRPO + Decoupled PPO | Single | Outcome | Multi | Math/Code/SearchQA | External/Rule | Yes |
| [Graph-R1](https://github.com/LHRLAB/Graph-R1) | GRPO/REINFORCE++/PPO | Single | Outcome | Multi | KGQA | Rule (EM/F1) | Yes (Graph retrieval) |
| [Kimi-Researcher](https://github.com/moonshotai/Kimi-Researcher) | REINFORCE | Single | Outcome | Multi | Research | Outcome | Search, Browse, Coding |
| [R-Search](https://github.com/QingFei1/R-Search) | PPO/GRPO | Single | Both | Multi | QA/Search | All | Yes |
| [R1-Searcher-plus](https://github.com/RUCAIBox/R1-Searcher-plus) | Custom | Single | Outcome | Multi | Search | Model | Search |
| [StepSearch](https://github.com/Zillwang/StepSearch) | PPO | Single | Process | Multi | QA | Model | Search |
| [AutoRefine](https://github.com/syr-cn/AutoRefine) | PPO/GRPO | Multi | Both | Multi | RAG QA | Rule | Search |
| [ZeroSearch](https://github.com/Alibaba-NLP/ZeroSearch) | PPO/GRPO/REINFORCE | Single | Outcome | Multi | QA/Search | Rule | Yes |
| [ReasonRAG](https://github.com/wlzhang2020/ReasonRAG) | DPO + MCTS-based PRM | Single | Process | Multi | Multi-hop QA | Model (PRM) | Yes (Wikipedia search) |
| [Agentic-RAG-R1](https://github.com/jiangxinke/Agentic-RAG-R1) | GRPO | Single | Outcome | Multi | Knowledge-intensive QA | Rule/Model | Yes (Wiki/Doc search) |
| [WebThinker](https://github.com/RUC-NLPIR/WebThinker) | DPO | Single | Outcome | Multi | Reasoning/QA/Research | Model/External | Web Browsing |
| [DeepResearcher](https://github.com/GAIR-NLP/DeepResearcher) | PPO/GRPO | Multi | Outcome | Multi | Research | All | Yes |
| [Search-R1](https://github.com/PeterGriffinJin/Search-R1) | PPO/GRPO | Single | Outcome | Multi | Search | All | Search |
| [R1-Searcher](https://github.com/RUCAIBox/R1-Searcher) | PPO/DPO | Single | Both | Multi | Search | All | Yes |
| [C-3PO](https://github.com/Chen-GX/C-3PO) | PPO | Multi | Outcome | Multi | Search | Model | Yes |
| [DeepRetrieval](https://github.com/pat-jj/DeepRetrieval) | GRPO | Single | Outcome | Multi | Query Generation/IR | Rule | Yes (Search) |
| [SSRL](https://github.com/TsinghuaC3I/SSRL) | GRPO | Single | Outcome | Multi | Self-Search | Rule | Yes (Self-search) |
| [Research-Venus](https://github.com/antgroup/Research-Venus) | GRPO | Single | Both | Multi | Deep Research | Model (atomic thought) | Yes (Search) |
| [DeepResearch](https://github.com/Alibaba-NLP/DeepResearch) | RL-based | Single | Outcome | Multi | Deep Research | Model | Yes (Search, Browse) |
| [DeepDive](https://github.com/THUDM/DeepDive) | GRPO | Single | Outcome | Multi | KG-augmented Search | Rule | Yes (KG + Search) |
| [O-Researcher](https://github.com/OPPO-PersonalAI/O-Researcher) | GRPO + RLAIF | Multi | Process | Multi | Deep Research (Zhihu-KOL/WideSearch/ELI5) | Model (LLM-as-Judge) | Yes (Search/Crawl) |
| [DR Tulu](https://github.com/rlresearch/dr-tulu) | GRPO + evolving rubrics | Single | Outcome | Multi | Long-form Deep Research | Model (rubrics) | Yes (Search/MCP) |
| [WebSeer](https://github.com/99hgz/WebSeer) | GRPO-style | Single | Outcome | Multi | Web Search QA (w/ self-reflection) | Rule/Model | Yes (Search) |
| [HiPRAG](https://github.com/qualidea1217/HiPRAG) | PPO | Single | Process | Multi | Efficient Agentic RAG | Model/Rule | Yes (Retrieval) |
| [VRAG](https://github.com/Alibaba-NLP/VRAG) | GRPO | Single | Both | Multi | Visually-rich RAG | Rule/Model | Yes (Visual retrieval) |
| [MaskSearch](https://github.com/Alibaba-NLP/MaskSearch) | DAPO | Single | Outcome | Multi | RAMP Pretraining + QA | Rule/Model | Yes (Search) |
| [R3-RAG](https://github.com/Yuan-Li-FNLP/R3-RAG) | PPO | Single | Both | Multi | Multi-hop QA | Rule | Yes (Retrieval) |
| [O2-Searcher](https://github.com/KnowledgeXLab/O2-Searcher) | GRPO | Single | Outcome | Multi | Open-ended QA | Rule/Model | Yes (Search) |
| [s3](https://github.com/pat-jj/s3) | GRPO | Single | Outcome | Multi | RAG / Medical QA | Model (Gain-Beyond-RAG) | Yes (Retrieval) |
| [knowledge-r1](https://github.com/hzy312/knowledge-r1) | GRPO | Single | Outcome | Multi | Knowledge-intensive QA (KB-aware) | Rule | Yes (Retrieval) |

</details>

## 🌐 Web & GUI Agent


| Github Repo | 🌟 Stars | Date | Org | Paper Link | RL Framework |
| :----: | :----: | :----: |  :----: | :----: | :----: |
| [MobileAgent](https://github.com/X-PLUG/MobileAgent) | <img src="https://img.shields.io/github/stars/X-PLUG/MobileAgent?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.9 | X-PLUG (TongyiQwen) | [paper](https://arxiv.org/abs/2509.11543) | veRL |
| [InfiGUI-G1](https://github.com/InfiXAI/InfiGUI-G1) | <img src="https://img.shields.io/github/stars/InfiXAI/InfiGUI-G1?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.8 | InfiX AI | [Paper](https://arxiv.org/abs/2508.05731) | veRL |
| [UI-AGILE](https://github.com/KDEGroup/UI-AGILE) | <img src="https://img.shields.io/github/stars/KDEGroup/UI-AGILE?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.7 | Xiamen University | [Paper](https://arxiv.org/abs/2507.22025) | Custom |
| [gui-rcpo](https://github.com/zju-real/gui-rcpo) | <img src="https://img.shields.io/github/stars/zju-real/gui-rcpo?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.8 | Zhejiang University | [Paper](https://arxiv.org/abs/2508.05615) | Custom |
| [Grounding-R1](https://github.com/Yan98/Grounding-R1) | <img src="https://img.shields.io/github/stars/Yan98/Grounding-R1?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.6 | Salesforce | [blog](https://huggingface.co/blog/HelloKKMe/grounding-r1) | trl |
| [AgentCPM-GUI](https://github.com/OpenBMB/AgentCPM-GUI) | <img src="https://img.shields.io/github/stars/OpenBMB/AgentCPM-GUI?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.6 | OpenBMB/Tsinghua/RUC | [Paper](https://arxiv.org/pdf/2506.01391) | Huggingface |
| [TTI](https://github.com/test-time-interaction/TTI) | <img src="https://img.shields.io/github/stars/test-time-interaction/TTI?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.6 | CMU | [Paper](https://arxiv.org/abs/2506.07976) | Custom |
| [SE-GUI](https://github.com/YXB-NKU/SE-GUI) | <img src="https://img.shields.io/github/stars/YXB-NKU/SE-GUI?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.5 | Nankai University/vivo | [Paper](https://arxiv.org/pdf/2505.12370) | trl |
| [ARPO](https://github.com/dvlab-research/ARPO) | <img src="https://img.shields.io/github/stars/dvlab-research/ARPO?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.5 | CUHK/HKUST | [Paper](https://arxiv.org/pdf/2505.16282) | veRL |
| [GUI-G1](https://github.com/Yuqi-Zhou/GUI-G1) | <img src="https://img.shields.io/github/stars/Yuqi-Zhou/GUI-G1?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.5 | RUC | [Paper](https://arxiv.org/pdf/2505.15810) | TRL |
| [WebAgent-R1](https://github.com/weizhepei/WebAgent-R1) | <img src="https://img.shields.io/github/stars/weizhepei/WebAgent-R1?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.5 | Amazon/UVA | [Paper](https://arxiv.org/abs/2505.16421) | Custom |
| [GUI-R1](https://github.com/ritzz-ai/GUI-R1) | <img src="https://img.shields.io/github/stars/ritzz-ai/GUI-R1?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.4 | CAS/NUS | [Paper](https://arxiv.org/pdf/2504.10458) | veRL |
| [UI-R1](https://github.com/lll6gg/UI-R1) | <img src="https://img.shields.io/github/stars/lll6gg/UI-R1?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.3 | vivo/CUHK | [Paper](https://arxiv.org/pdf/2503.21620) | TRL |
| [CollabUIAgents](https://github.com/THUNLP-MT/CollabUIAgents) | <img src="https://img.shields.io/github/stars/THUNLP-MT/CollabUIAgents?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.2 | Tsinghua/Alibaba/HKUST | [Paper](https://arxiv.org/abs/2502.14496) | Custom |
| [WebAgent](https://github.com/Alibaba-NLP/WebAgent) | <img src="https://img.shields.io/github/stars/Alibaba-NLP/WebAgent?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.1 | Alibaba | [paper1](https://arxiv.org/pdf/2501.07572), [paper2](https://arxiv.org/pdf/2505.22648) | LLaMA-Factory |
| [UI-TARS](https://github.com/bytedance/UI-TARS) | <img src="https://img.shields.io/github/stars/bytedance/UI-TARS?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.9 | ByteDance Seed | [Paper](https://arxiv.org/abs/2509.02544) | Custom |
| [DigiQ](https://github.com/DigiRL-agent/digiq) | <img src="https://img.shields.io/github/stars/DigiRL-agent/digiq?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.2 | UC Berkeley/CMU/Amazon | [Paper](https://arxiv.org/abs/2502.15760) | Custom |
| [ZeroGUI](https://github.com/OpenGVLab/ZeroGUI) | <img src="https://img.shields.io/github/stars/OpenGVLab/ZeroGUI?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.5 | Shanghai AI Lab | [Paper](https://arxiv.org/abs/2505.23762) | Custom |
| [InfiGUI-R1](https://github.com/Reallm-Labs/InfiGUI-R1) | <img src="https://img.shields.io/github/stars/Reallm-Labs/InfiGUI-R1?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.4 | Zhejiang University | [Paper](https://arxiv.org/abs/2504.14239) | Custom |
| [GUI-Agent-RL](https://github.com/microsoft/GUI-Agent-RL) | <img src="https://img.shields.io/github/stars/microsoft/GUI-Agent-RL?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.2 | Microsoft | [Paper](https://arxiv.org/abs/2502.18906) | Custom |
| [GUI-Libra](https://github.com/GUI-Libra/GUI-Libra) | <img src="https://img.shields.io/github/stars/GUI-Libra/GUI-Libra?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2026.2 | GUI-Libra (MS-affiliated) | [Paper](https://arxiv.org/abs/2602.22190) | Custom |
| [MobileRL](https://github.com/THUDM/MobileRL) | <img src="https://img.shields.io/github/stars/THUDM/MobileRL?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.9 | Tsinghua / Zhipu AI (THUDM) | [Paper](https://arxiv.org/abs/2509.18119) | Custom |
| [DART-GUI](https://github.com/Computer-use-agents/dart-gui) | <img src="https://img.shields.io/github/stars/Computer-use-agents/dart-gui?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.9 | Computer-use-agents | [Paper](https://arxiv.org/abs/2509.23866) | veRL |
| [Mano-P](https://github.com/Mininglamp-AI/Mano-P) | <img src="https://img.shields.io/github/stars/Mininglamp-AI/Mano-P?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.9 | Mininglamp AI | [Paper](https://arxiv.org/abs/2509.17336) | Mano-SDK |
| [GUI-G2](https://github.com/ZJU-REAL/GUI-G2) | <img src="https://img.shields.io/github/stars/ZJU-REAL/GUI-G2?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.7 | Zhejiang University (ZJU-REAL) | [Paper](https://arxiv.org/abs/2507.15846) | Custom (VLM-R1) |
| [MagicGUI](https://github.com/MagicAgent-GUI/MagicGUI) | <img src="https://img.shields.io/github/stars/MagicAgent-GUI/MagicGUI?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.7 | Honor (MagicAgent-GUI) | [Paper](https://arxiv.org/abs/2508.03700) | Custom |
| [GTA1](https://github.com/Yan98/GTA1) | <img src="https://img.shields.io/github/stars/Yan98/GTA1?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.6 | Salesforce / ANU | [Paper](https://arxiv.org/abs/2507.05791) | Custom (DeepSpeed) |

<details>
<summary>📋 Click to view technical details</summary>

| Github Repo | RL Algorithm | Single/Multi Agent | Outcome/Process Reward | Single/Multi Turn | Task | Reward Type | Tool usage |
| :----: | :----: | :----: | :----: | :----: | :----: | :----: | :----: |
| [MobileAgent](https://github.com/X-PLUG/MobileAgent) | semi-online RL | Single | Both | Multi | MobileGUI/Automation | Rule | Yes |
| [InfiGUI-G1](https://github.com/InfiXAI/InfiGUI-G1) | AEPO | Single | Outcome | Single | GUI/Grounding | Rule | No |
| [UI-AGILE](https://github.com/KDEGroup/UI-AGILE) | GRPO | Single | Outcome | Single | GUI Grounding | Rule (continuous) | No |
| [gui-rcpo](https://github.com/zju-real/gui-rcpo) | RCPO | Single | Outcome | Single | GUI Grounding | Rule (self-supervised) | No |
| [Grounding-R1](https://github.com/Yan98/Grounding-R1) | GRPO | Single | Outcome | Multi | GUI Grounding | Model | Yes |
| [AgentCPM-GUI](https://github.com/OpenBMB/AgentCPM-GUI) | GRPO | Single | Outcome | Multi | Mobile GUI | Model | Yes |
| [TTI](https://github.com/test-time-interaction/TTI) | REINFORCE/BC | Single | Outcome | Multi | Web | External | Web Browsing |
| [SE-GUI](https://github.com/YXB-NKU/SE-GUI) | GRPO | Single | Both | Single | GUI Grounding | Rule | Yes |
| [ARPO](https://github.com/dvlab-research/ARPO) | GRPO | Single | Outcome | Multi | GUI | External | Computer Use |
| [GUI-G1](https://github.com/Yuqi-Zhou/GUI-G1) | GRPO | Single | Outcome | Single | GUI | Rule/External | No |
| [WebAgent-R1](https://github.com/weizhepei/WebAgent-R1) | M-GRPO | Single | Outcome | Multi | Web Navigation (WebArena-Lite) | Rule (task success) | Yes (Web browsing) |
| [GUI-R1](https://github.com/ritzz-ai/GUI-R1) | GRPO | Single | Outcome | Multi | GUI | Rule | No |
| [UI-R1](https://github.com/lll6gg/UI-R1) | GRPO | Single | Process | Both | GUI | Rule | Computer/Phone Use |
| [CollabUIAgents](https://github.com/THUNLP-MT/CollabUIAgents) | DPO (credit re-assignment) | Multi | Process | Multi | GUI (Mobile + Web) | Model (LLM) | Yes (GUI interaction) |
| [WebAgent](https://github.com/Alibaba-NLP/WebAgent) | DAPO | Multi | Process | Multi | Web | Model | Yes |
| [UI-TARS](https://github.com/bytedance/UI-TARS) | Multi-turn RL | Single | Both | Multi | GUI (Cross-platform) | Model | Yes (GUI actions) |
| [DigiQ](https://github.com/DigiRL-agent/digiq) | Value-based offline RL | Single | Outcome | Multi | Android Device Control | Model (Q-function) | Yes |
| [ZeroGUI](https://github.com/OpenGVLab/ZeroGUI) | Online RL | Single | Outcome | Multi | GUI Agent | Rule | Yes (GUI actions) |
| [InfiGUI-R1](https://github.com/Reallm-Labs/InfiGUI-R1) | RL + sub-goal guidance | Single | Both | Multi | GUI Reasoning | Rule | Yes |
| [GUI-Agent-RL](https://github.com/microsoft/GUI-Agent-RL) | Value-based RL (VEM) | Single | Outcome | Multi | GUI (Web Shopping) | Model | Yes |
| [GUI-Libra](https://github.com/GUI-Libra/GUI-Libra) | KL-regularized GRPO (Partially Verifiable RL) | Single | Outcome | Multi | GUI (AndroidWorld/WebArena/Online-Mind2Web) | Rule | Yes |
| [MobileRL](https://github.com/THUDM/MobileRL) | AdaGRPO (Difficulty-Adaptive) | Single | Outcome | Multi | Mobile GUI (AndroidWorld/AndroidLab) | Rule | Yes (Android) |
| [DART-GUI](https://github.com/Computer-use-agents/dart-gui) | Decoupled GRPO | Single | Outcome | Multi | GUI (OSWorld) | Rule | Yes |
| [Mano-P](https://github.com/Mininglamp-AI/Mano-P) | Three-stage SFT→Offline RL→Online RL | Single | Both | Multi | GUI (OSWorld) | Rule | Yes |
| [GUI-G2](https://github.com/ZJU-REAL/GUI-G2) | GRPO (Gaussian Reward) | Single | Outcome | Single | GUI Grounding | Rule (continuous) | No |
| [MagicGUI](https://github.com/MagicAgent-GUI/MagicGUI) | Reinforcement Fine-Tuning (RFT) | Single | Outcome | Multi | Mobile GUI | Model/Rule | Yes |
| [GTA1](https://github.com/Yan98/GTA1) | GRPO-style (click-success reward) | Single | Outcome | Multi | GUI Grounding (OSWorld/ScreenSpot-Pro) | Rule | Yes |

</details>

## 🔨 Tool-Use Agent


| Github Repo | 🌟 Stars | Date | Org | Paper Link | RL Framework |
| :----: | :----: | :----: |  :----: | :----: | :----: |
| [MATPO](https://github.com/mzf666/MATPO) | <img src="https://img.shields.io/github/stars/mzf666/MATPO?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.10 | MiroMind AI | [Paper](https://arxiv.org/abs/2510.04678) | Custom |
| [MiroRL](https://github.com/MiroMindAI/MiroRL) | <img src="https://img.shields.io/github/stars/MiroMindAI/MiroRL?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.8 | MiroMindAI | [HF Repo](https://huggingface.co/miromind-ai) | veRL |
| [verl-tool](https://github.com/TIGER-AI-Lab/verl-tool) | <img src="https://img.shields.io/github/stars/TIGER-AI-Lab/verl-tool?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.6 | TIGER-Lab | [X](https://x.com/DongfuJiang/status/1929198238017720379) | veRL |
| [Multi-Turn-RL-Agent](https://github.com/SiliangZeng/Multi-Turn-RL-Agent) | <img src="https://img.shields.io/github/stars/SiliangZeng/Multi-Turn-RL-Agent?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.5 | University of Minnesota | [Paper](https://arxiv.org/pdf/2505.11821) | Custom |
| [Tool-N1](https://github.com/NVlabs/Tool-N1) | <img src="https://img.shields.io/github/stars/NVlabs/Tool-N1?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.5 | NVIDIA | [Paper](https://arxiv.org/pdf/2505.00024) | veRL |
| [Tool-Star](https://github.com/dongguanting/Tool-Star) | <img src="https://img.shields.io/github/stars/dongguanting/Tool-Star?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.5 | RUC | [Paper](https://arxiv.org/pdf/2505.16410) | LLaMA-Factory |
| [RL-Factory](https://github.com/Simple-Efficient/RL-Factory) | <img src="https://img.shields.io/github/stars/Simple-Efficient/RL-Factory?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.5 | Simple-Efficient | [model](https://huggingface.co/Simple-Efficient/RLFactory-Qwen3-8B-GRPO) | veRL |
| [ReTool](https://github.com/ReTool-RL/ReTool) | <img src="https://img.shields.io/github/stars/ReTool-RL/ReTool?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.4 | ByteDance | [Paper](https://arxiv.org/pdf/2504.11536) | veRL |
| [AWorld](https://github.com/inclusionAI/AWorld) | <img src="https://img.shields.io/github/stars/inclusionAI/AWorld?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.3 | Ant Group (inclusionAI) | [Paper](https://arxiv.org/abs/2508.20404) | veRL |
| [Agent-R1](https://github.com/0russwest0/Agent-R1) | <img src="https://img.shields.io/github/stars/0russwest0/Agent-R1?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.3 | USTC | [Paper](https://arxiv.org/abs/2511.14460) | veRL |
| [ReCall](https://github.com/Agent-RL/ReCall) | <img src="https://img.shields.io/github/stars/Agent-RL/ReCall?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.3 | BaiChuan | [Paper](https://arxiv.org/pdf/2503.19470) | veRL |
| [ToolRL](https://github.com/qiancheng0/ToolRL) | <img src="https://img.shields.io/github/stars/qiancheng0/ToolRL?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.4 | UIUC | [Paper](https://arxiv.org/abs/2504.13958) | veRL |
| [ToolOrchestra](https://github.com/NVlabs/ToolOrchestra) | <img src="https://img.shields.io/github/stars/NVlabs/ToolOrchestra?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.11 | NVIDIA / HKU | [Paper](https://arxiv.org/abs/2511.21689) | Custom (veRL-based) |
| [ToolMaster](https://github.com/NEUIR/ToolMaster) | <img src="https://img.shields.io/github/stars/NEUIR/ToolMaster?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.11 | Northeastern University (NEUIR) | [Paper](https://arxiv.org/abs/2601.12762) | Custom |
| [CodeGym](https://github.com/StigLidu/CodeGym) | <img src="https://img.shields.io/github/stars/StigLidu/CodeGym?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.9 | Academic | [Paper](https://arxiv.org/abs/2509.17325) | Custom |
| [UserRL](https://github.com/SalesforceAIResearch/UserRL) | <img src="https://img.shields.io/github/stars/SalesforceAIResearch/UserRL?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.9 | Salesforce AI Research | [Paper](https://arxiv.org/abs/2509.19736) | veRL |
| [ToolBrain](https://github.com/ToolBrain/ToolBrain) | <img src="https://img.shields.io/github/stars/ToolBrain/ToolBrain?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.9 | ToolBrain (AAMAS 2026) | [Paper](https://arxiv.org/abs/2510.00023) | Custom |
| [Tool-R1](https://github.com/YBYBZhang/Tool-R1) | <img src="https://img.shields.io/github/stars/YBYBZhang/Tool-R1?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.9 | Individual (YBYBZhang) | [Paper](https://arxiv.org/abs/2509.12867) | Custom |
| [calculator_agent_rl](https://github.com/Danau5tin/calculator_agent_rl) | <img src="https://img.shields.io/github/stars/Danau5tin/calculator_agent_rl?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.5 | Individual (Danau5tin) | -- | Verifiers |

<details>
<summary>📋 Click to view technical details</summary>

| Github Repo | RL Algorithm | Single/Multi Agent | Outcome/Process Reward | Single/Multi Turn | Task | Reward Type | Tool usage |
| :----: | :----: | :----: | :----: | :----: | :----: | :----: | :----: |
| [MATPO](https://github.com/mzf666/MATPO) | GRPO (multi-agent) | Multi | Outcome | Multi | Tool-use/Search | Rule | Yes (MCP: Serper, Web scraping) |
| [MiroRL](https://github.com/MiroMindAI/MiroRL) | GRPO | Single | Both | Multi | Reasoning/Planning/ToolUse | Rule-based | MCP |
| [verl-tool](https://github.com/TIGER-AI-Lab/verl-tool) | PPO/GRPO | Single | Both | Both | Math/Code | Rule/External | Yes |
| [Multi-Turn-RL-Agent](https://github.com/SiliangZeng/Multi-Turn-RL-Agent) | GRPO | Single | Both | Multi | Tool-use/Math | Rule/External | Yes |
| [Tool-N1](https://github.com/NVlabs/Tool-N1) | PPO | Single | Outcome | Multi | Math/Dialogue | All | Yes |
| [Tool-Star](https://github.com/dongguanting/Tool-Star) | PPO/DPO/ORPO/SimPO/KTO | Single | Outcome | Multi | Multi-modal/Tool Use/Dialogue | Model/External | Yes |
| [RL-Factory](https://github.com/Simple-Efficient/RL-Factory) | GRPO | Multi | Both | Multi | Tool-use/NL2SQL | All | MCP |
| [ReTool](https://github.com/ReTool-RL/ReTool) | PPO | Single | Outcome | Multi | Math | External | Code |
| [AWorld](https://github.com/inclusionAI/AWorld) | GRPO | Both | Outcome | Multi | Search/Web/Code | External/Rule | Yes |
| [Agent-R1](https://github.com/0russwest0/Agent-R1) | PPO/GRPO | Single | Both | Multi | Tool-use/QA | Model | Yes |
| [ReCall](https://github.com/Agent-RL/ReCall) | PPO/GRPO/RLOO/REINFORCE++/ReMax | Single | Outcome | Multi | Tool-use/Math/QA | All | Yes |
| [ToolRL](https://github.com/qiancheng0/ToolRL) | GRPO/PPO | Single | Outcome | Multi | Tool Learning | Rule/External | Yes |
| [ToolOrchestra](https://github.com/NVlabs/ToolOrchestra) | End-to-end RL (outcome+efficiency+preference) | Single | Both | Multi | Tool orchestration / agentic workflows | All | Yes (Search/Code/LLMs) |
| [ToolMaster](https://github.com/NEUIR/ToolMaster) | SFT + GRPO (trial-then-execute) | Single | Outcome | Multi | Tool trialing + execution (ToolHop/TMDB/StableToolBench) | Rule/External | Yes (Simulated tools) |
| [CodeGym](https://github.com/StigLidu/CodeGym) | GRPO-family | Single | Outcome | Multi | Synthetic Multi-turn Tool-Use | Rule (verifiable) | Yes (Synthesized tools) |
| [UserRL](https://github.com/SalesforceAIResearch/UserRL) | GRPO (multi-turn credit) | Single | Both | Multi | User-centric (Function/Persuade/Search/Tau Gyms) | Model/External | Yes |
| [ToolBrain](https://github.com/ToolBrain/ToolBrain) | GRPO/DPO | Single | Outcome | Multi | Agentic tool training | Rule/Model | Yes (User-defined tools) |
| [Tool-R1](https://github.com/YBYBZhang/Tool-R1) | Policy optimization (PPO-style) | Single | Outcome | Multi | Agentic Tool Use (GAIA) | Model + External | Yes (Python exec) |
| [calculator_agent_rl](https://github.com/Danau5tin/calculator_agent_rl) | GRPO | Single | Outcome | Multi | Calculator Tool Use | Model (Claude-judge) | Yes |

</details>

## 💻 Code & SWE Agent


| Github Repo | 🌟 Stars | Date | Org | Paper Link | RL Framework |
| :----: | :----: | :----: |  :----: | :----: | :----: |
| [CUDA-Agent](https://github.com/BytedTsinghua-SIA/CUDA-Agent) | <img src="https://img.shields.io/github/stars/BytedTsinghua-SIA/CUDA-Agent?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2026.2 | ByteDance/Tsinghua | [Paper](https://arxiv.org/abs/2602.24286) | Custom |
| [LLM-in-Sandbox](https://github.com/llm-in-sandbox/llm-in-sandbox) | <img src="https://img.shields.io/github/stars/llm-in-sandbox/llm-in-sandbox?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2026.1 | RUC/MSRA/THU | [Paper](https://huggingface.co/papers/2601.16206) | rllm (w/ veRL) |
| [PPP-Agent](https://github.com/sunnweiwei/PPP-Agent) | <img src="https://img.shields.io/github/stars/sunnweiwei/PPP-Agent?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.11 | CMU/OpenHands | [Paper](https://arxiv.org/abs/2511.02208) | veRL |
| [RepoDeepSearch](https://github.com/Mizersy/RepoDeepSearch) | <img src="https://img.shields.io/github/stars/Mizersy/RepoDeepSearch?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.8 | PKU, Bytedance, BIT | [Paper](https://arxiv.org/abs/2508.03012) | veRL |
| [CUDA-L1](https://github.com/deepreinforce-ai/CUDA-L1) | <img src="https://img.shields.io/github/stars/deepreinforce-ai/CUDA-L1?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.7 | DeepReinforce AI | [Paper](https://arxiv.org/abs/2507.14111) | Custom |
| [MedAgentGym](https://github.com/wshi83/MedAgentGym) | <img src="https://img.shields.io/github/stars/wshi83/MedAgentGym?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.6 | Emory/Georgia Tech | [Paper](https://arxiv.org/pdf/2506.04405) | Hugginface |
| [CURE](https://github.com/Gen-Verse/CURE) | <img src="https://img.shields.io/github/stars/Gen-Verse/CURE?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.6 | University of Chicago <br> Princeton/ByteDance | [Paper](https://arxiv.org/pdf/2506.03136) | Huggingface |
| [Time-R1](https://github.com/ulab-uiuc/Time-R1) | <img src="https://img.shields.io/github/stars/ulab-uiuc/Time-R1?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.5 | UIUC | [Paper](https://arxiv.org/pdf/2505.13508) | veRL |
| [ML-Agent](https://github.com/MASWorks/ML-Agent) | <img src="https://img.shields.io/github/stars/MASWorks/ML-Agent?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.5 | MASWorks | [Paper](https://arxiv.org/pdf/2505.23723) | Custom |
| [digitalhuman](https://github.com/Tencent/digitalhuman) | <img src="https://img.shields.io/github/stars/Tencent/digitalhuman?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.4 | Tencent | [Paper](https://arxiv.org/abs/2507.03112) | veRL |
| [sweet_rl](https://github.com/facebookresearch/sweet_rl) | <img src="https://img.shields.io/github/stars/facebookresearch/sweet_rl?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.3 | Meta/UCB | [Paper](https://arxiv.org/pdf/2503.15478) | OpenRLHF |
| [swe-rl](https://github.com/facebookresearch/swe-rl) | <img src="https://img.shields.io/github/stars/facebookresearch/swe-rl?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.2 | Meta/UIUC/CMU | [Paper](https://arxiv.org/abs/2502.18449) | Custom |
| [rllm](https://github.com/agentica-project/rllm) | <img src="https://img.shields.io/github/stars/agentica-project/rllm?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.1 | Berkeley Sky Computing Lab <br> BAIR / Together AI | [Notion Blog](https://pretty-radio-b75.notion.site/rLLM-A-Framework-for-Post-Training-Language-Agents-21b81902c146819db63cd98a54ba5f31) | veRL |
| [open-r1](https://github.com/huggingface/open-r1) | <img src="https://img.shields.io/github/stars/huggingface/open-r1?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.1 | HuggingFace | -- | TRL |
| [R1-Code-Interpreter](https://github.com/yongchao98/R1-Code-Interpreter) | <img src="https://img.shields.io/github/stars/yongchao98/R1-Code-Interpreter?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.5 | MIT | [Paper](https://arxiv.org/abs/2505.21668) | Custom |
| [CTRL](https://github.com/HKUNLP/critic-rl) | <img src="https://img.shields.io/github/stars/HKUNLP/critic-rl?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.2 | HKU/ByteDance | [Paper](https://arxiv.org/abs/2502.03492) | Custom |
| [DeepAnalyze](https://github.com/ruc-datalab/DeepAnalyze) | <img src="https://img.shields.io/github/stars/ruc-datalab/DeepAnalyze?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.10 | RUC/Tsinghua | [Paper](https://arxiv.org/abs/2510.16872) | Custom |
| [AceCoder](https://github.com/TIGER-AI-Lab/AceCoder) | <img src="https://img.shields.io/github/stars/TIGER-AI-Lab/AceCoder?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.2 | Waterloo (TIGER-Lab) | [Paper](https://arxiv.org/abs/2502.01718) | Custom |
| [SWE-World](https://github.com/RUCAIBox/SWE-World) | <img src="https://img.shields.io/github/stars/RUCAIBox/SWE-World?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2026.2 | RUC (RUCAIBox) | [Paper](https://arxiv.org/abs/2602.03419) | OpenRLHF + veRL |
| [CUDA-L2](https://github.com/deepreinforce-ai/CUDA-L2) | <img src="https://img.shields.io/github/stars/deepreinforce-ai/CUDA-L2?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2026.1 | DeepReinforce AI | [Paper](https://arxiv.org/abs/2512.02551) | Custom |
| [SWE-Swiss](https://github.com/zhenyuhe00/SWE-Swiss) | <img src="https://img.shields.io/github/stars/zhenyuhe00/SWE-Swiss?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.7 | Tsinghua / ByteDance | -- | veRL |
| [Skywork-OR1](https://github.com/SkyworkAI/Skywork-OR1) | <img src="https://img.shields.io/github/stars/SkyworkAI/Skywork-OR1?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.4 | Skywork AI | [Paper](https://arxiv.org/abs/2505.22312) | Custom (veRL fork) |

<details>
<summary>📋 Click to view technical details</summary>

| Github Repo | RL Algorithm | Single/Multi Agent | Outcome/Process Reward | Single/Multi Turn | Task | Reward Type | Tool usage |
| :----: | :----: | :----: | :----: | :----: | :----: | :----: | :----: |
| [CUDA-Agent](https://github.com/BytedTsinghua-SIA/CUDA-Agent) | Agentic RL (staged) | Single | Outcome | Multi | CUDA Kernel Generation | Rule (correctness + performance) | Yes (compile/verify/profile) |
| [LLM-in-Sandbox](https://github.com/llm-in-sandbox/llm-in-sandbox) | GRPO++ | Single | Outcome | Multi | Code/SWE + General (Math/Sci/Bio) | Rule | Yes (Code Sandbox w/ Terminal, File, Internet) |
| [PPP-Agent](https://github.com/sunnweiwei/PPP-Agent) | PPP-RL | Single | Both | Multi | SWE/Research | Rule+Model | Search, Ask, Browse |
| [RepoDeepSearch](https://github.com/Mizersy/RepoDeepSearch) | GRPO | Single | Both | Multi | Search/Repair | Rule/External | Yes |
| [CUDA-L1](https://github.com/deepreinforce-ai/CUDA-L1) | Contrastive RL | Single | Outcome | Single | CUDA Optimization | Rule (performance) | No |
| [MedAgentGym](https://github.com/wshi83/MedAgentGym) | SFT/DPO/PPO/GRPO | Single | Outcome | Multi | Medical/Code | External | Yes |
| [CURE](https://github.com/Gen-Verse/CURE) | PPO | Single | Outcome | Single | Code | External | No |
| [Time-R1](https://github.com/ulab-uiuc/Time-R1) | PPO/GRPO/DPO | Multi | Outcome | Multi | Temporal | All | Code |
| [ML-Agent](https://github.com/MASWorks/ML-Agent) | Custom | Single | Process | Multi | Code | All | Yes |
| [digitalhuman](https://github.com/Tencent/digitalhuman) | PPO/GRPO/ReMax/RLOO | Multi | Outcome | Multi | Empathy/Math/Code/MultimodalQA | Rule/Model/External | Yes |
| [sweet_rl](https://github.com/facebookresearch/sweet_rl) | DPO | Multi | Process | Multi | Design/Code | Model | Web Browsing |
| [swe-rl](https://github.com/facebookresearch/swe-rl) | RL-based | Single | Outcome | Single | SWE (SWE-bench) | Rule (similarity) | No |
| [rllm](https://github.com/agentica-project/rllm) | PPO/GRPO | Single | Outcome | Multi | Code Edit | External | Yes |
| [open-r1](https://github.com/huggingface/open-r1) | GRPO | Single | Outcome | Single | Math/Code | All | Yes |
| [R1-Code-Interpreter](https://github.com/yongchao98/R1-Code-Interpreter) | GRPO | Single | Outcome | Multi | Code Interpretation | Rule/External | Yes (Code exec) |
| [CTRL](https://github.com/HKUNLP/critic-rl) | RL (critique-revision) | Single | Process | Multi | Code Refinement | Model | Yes (Code exec) |
| [DeepAnalyze](https://github.com/ruc-datalab/DeepAnalyze) | Curriculum RL | Single | Outcome | Multi | Data Science | Rule/External | Yes (Code exec) |
| [AceCoder](https://github.com/TIGER-AI-Lab/AceCoder) | GRPO | Single | Outcome | Single | Code Generation | External (test cases) | Yes |
| [SWE-World](https://github.com/RUCAIBox/SWE-World) | RL with learned world model (SWT + SWR) | Single | Both | Multi | Docker-free SWE (SWE-Bench Verified) | Model (surrogate) + Rule | Yes |
| [CUDA-L2](https://github.com/deepreinforce-ai/CUDA-L2) | Contrastive RL | Single | Outcome | Single | HGEMM / CUDA Matmul | Rule (TFLOPs) | Yes (compile/benchmark) |
| [SWE-Swiss](https://github.com/zhenyuhe00/SWE-Swiss) | Two-stage RL curriculum | Single | Outcome | Multi | SWE (Localization/Repair/Unit-Test) | Rule (test-based) | Yes |
| [Skywork-OR1](https://github.com/SkyworkAI/Skywork-OR1) | Large-scale rule-based RL (GRPO variant) | Single | Outcome | Single | Math + Code (AIME/LiveCodeBench) | Rule (verifiable) | No |

</details>

## 🤔 Reasoning Agent


| Github Repo | 🌟 Stars | Date | Org | Paper Link | RL Framework |
| :----: | :----: | :----: |  :----: | :----: | :----: |
| [Agent0](https://github.com/aiming-lab/Agent0) | <img src="https://img.shields.io/github/stars/aiming-lab/Agent0?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.10 | UNC‑Chapel Hill / Salesforce Research / Stanford University | [Paper](https://arxiv.org/abs/2511.16043) | veRL |
| [KG-R1](https://github.com/Jinyeop3110/KG-R1) | <img src="https://img.shields.io/github/stars/Jinyeop3110/KG-R1?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.9 | UIUC/Google | [Paper1](https://arxiv.org/pdf/2503.09516), [Paper2](https://arxiv.org/abs/2505.15117) | veRL |
| [AgentFlow](https://github.com/lupantech/AgentFlow) | <img src="https://img.shields.io/github/stars/lupantech/AgentFlow?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.09 | Stanford University | [arXiv](https://arxiv.org/abs/2510.05592) | veRL |
| [ARPO](https://github.com/dongguanting/ARPO) | <img src="https://img.shields.io/github/stars/dongguanting/ARPO?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.7 | RUC, Kuaishou | [Paper](https://arxiv.org/abs/2507.19849) | veRL |
| [terminal-bench-rl](https://github.com/Danau5tin/terminal-bench-rl) | <img src="https://img.shields.io/github/stars/Danau5tin/terminal-bench-rl?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.7 | Individual (Danau5tin) | N/A | rLLM |
| [MOTIF](https://github.com/purbeshmitra/MOTIF) | <img src="https://img.shields.io/github/stars/purbeshmitra/MOTIF?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.6 | University of Maryland | [Paper](https://arxiv.org/abs/2507.02851) | trl |
| [cmriat/l0](https://github.com/cmriat/l0) | <img src="https://img.shields.io/github/stars/cmriat/l0?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.6 | CMRIAT | [Paper](https://arxiv.org/abs/2506.23667) | veRL |
| [agent-distillation](https://github.com/Nardien/agent-distillation) | <img src="https://img.shields.io/github/stars/Nardien/agent-distillation?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.5 | KAIST | [Paper](https://arxiv.org/pdf/2505.17612) | Custom |
| [EasyR1](https://github.com/hiyouga/EasyR1) | <img src="https://img.shields.io/github/stars/hiyouga/EasyR1?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.4 | Individual | [repo1](https://github.com/hiyouga/EasyR1)/[paper2](https://arxiv.org/pdf/2409.19256) | veRL |
| [AutoCoA](https://github.com/ADaM-BJTU/AutoCoA) | <img src="https://img.shields.io/github/stars/ADaM-BJTU/AutoCoA?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.3 | BJTU | [Paper](https://arxiv.org/pdf/2503.06580) | veRL |
| [ToRL](https://github.com/GAIR-NLP/ToRL) | <img src="https://img.shields.io/github/stars/GAIR-NLP/ToRL?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.3 | SJTU | [Paper](https://arxiv.org/pdf/2503.23383) | veRL |
| [ReMA](https://github.com/ziyuwan/ReMA-public) | <img src="https://img.shields.io/github/stars/ziyuwan/ReMA-public?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.3 | SJTU, UCL | [Paper](https://arxiv.org/pdf/2503.09501) | veRL |
| [Agentic-Reasoning](https://github.com/theworldofagents/Agentic-Reasoning) | <img src="https://img.shields.io/github/stars/theworldofagents/Agentic-Reasoning?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.2 | Oxford | [Paper](https://arxiv.org/pdf/2502.04644) | Custom |
| [SimpleTIR](https://github.com/ltzheng/SimpleTIR) | <img src="https://img.shields.io/github/stars/ltzheng/SimpleTIR?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.2 | NTU, Bytedance | [Notion Blog](https://simpletir.notion.site/report) | veRL |
| [openrlhf_async_pipline](https://github.com/yyht/openrlhf_async_pipline) | <img src="https://img.shields.io/github/stars/yyht/openrlhf_async_pipline?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2024.5 | OpenRLHF | [Paper](https://arxiv.org/pdf/2405.11143) | OpenRLHF |
| [THOR](https://github.com/JingMog/THOR) | <img src="https://img.shields.io/github/stars/JingMog/THOR?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.9 | USTC / iFLYTEK | [Paper](https://arxiv.org/abs/2509.13761) | veRL |
| [Tool-Light](https://github.com/RUC-NLPIR/Tool-Light) | <img src="https://img.shields.io/github/stars/RUC-NLPIR/Tool-Light?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.9 | RUC (RUC-NLPIR) | [Paper](https://arxiv.org/abs/2509.23285) | LLaMA-Factory |
| [AutoTIR](https://github.com/weiyifan1023/AutoTIR) | <img src="https://img.shields.io/github/stars/weiyifan1023/AutoTIR?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.7 | Beihang University / BAAI | [Paper](https://arxiv.org/abs/2507.21836) | veRL |

<details>
<summary>📋 Click to view technical details</summary>

| Github Repo | RL Algorithm | Single/Multi Agent | Outcome/Process Reward | Single/Multi Turn | Task | Reward Type | Tool usage |
| :----: | :----: | :----: | :----: | :----: | :----: | :----: | :----: |
| [Agent0](https://github.com/aiming-lab/Agent0) | ADPO | Multi | Process | Multi | Math/Visual | Model/Verifier | Yes |
| [KG-R1](https://github.com/Jinyeop3110/KG-R1) | GRPO/PPO | Single | Both | Multi | KGQA | Rule/Model | KG Retrieval |
| [AgentFlow](https://github.com/lupantech/AgentFlow) | Flow-GRPO | Single | Outcome | Multi | Search/Math/QA | Model/External | Yes |
| [ARPO](https://github.com/dongguanting/ARPO) | GRPO | Single | Outcome | Multi | Math/Coding | Model/Rule | Yes |
| [terminal-bench-rl](https://github.com/Danau5tin/terminal-bench-rl) | GRPO | Single | Outcome | Multi | Coding/Terminal | Model+External Verifier | Yes |
| [MOTIF](https://github.com/purbeshmitra/MOTIF) | GRPO | Single | Outcome | Multi | QA | Rule | No |
| [cmriat/l0](https://github.com/cmriat/l0) | PPO | Multi | Process | Multi | QA | All | Yes |
| [agent-distillation](https://github.com/Nardien/agent-distillation) | PPO | Single | Process | Multi | QA/Math | External | Yes |
| [EasyR1](https://github.com/hiyouga/EasyR1) | GRPO | Single | Process | Multi | Vision-Language | Model | Yes |
| [AutoCoA](https://github.com/ADaM-BJTU/AutoCoA) | GRPO | Multi | Outcome | Multi | Reasoning/Math/QA | All | Yes |
| [ToRL](https://github.com/GAIR-NLP/ToRL) | GRPO | Single | Outcome | Single | Math | Rule/External | Yes |
| [ReMA](https://github.com/ziyuwan/ReMA-public) | PPO | Multi | Outcome | Multi | Math | Rule | No |
| [Agentic-Reasoning](https://github.com/theworldofagents/Agentic-Reasoning) | Custom | Single | Process | Multi | QA/Math | External | Web Browsing |
| [SimpleTIR](https://github.com/ltzheng/SimpleTIR) | PPO/GRPO (with extensions) | Single | Outcome | Multi | Math, Coding | All | Yes |
| [openrlhf_async_pipline](https://github.com/yyht/openrlhf_async_pipline) | PPO/REINFORCE++/DPO/RLOO | Single | Outcome | Multi | Dialogue/Reasoning/QA | All | No |
| [THOR](https://github.com/JingMog/THOR) | Hierarchical GRPO (trajectory+step) | Single | Both | Multi | Math (MATH500/AIME/Olympiad) | External (SandboxFusion) | Yes (Python) |
| [Tool-Light](https://github.com/RUC-NLPIR/Tool-Light) | Self-Evolved DPO | Single | Outcome | Multi | Tool-Integrated Reasoning | Model (preference) | Yes (FlashRAG/Python) |
| [AutoTIR](https://github.com/weiyifan1023/AutoTIR) | PPO | Single | Outcome | Multi | Autonomous Tool Selection (QA/Math/IF) | Rule | Yes (Search/Python) |

</details>

## 👥 Multi-Agent RL


| Github Repo | 🌟 Stars | Date | Org | Paper Link | RL Framework |
| :----: | :----: | :----: |  :----: | :----: | :----: |
| [PettingLLMs](https://github.com/pettingllms-ai/PettingLLMs) | <img src="https://img.shields.io/github/stars/pettingllms-ai/PettingLLMs?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.10 | Intel / UCSD | [Paper](https://arxiv.org/abs/2510.11062) | Custom |
| [MASPRM](https://github.com/milad1378yz/MASPRM) | <img src="https://img.shields.io/github/stars/milad1378yz/MASPRM?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.10 | UBC / Huawei | [Paper](https://arxiv.org/abs/2510.24803) | Custom |
| [ARIA](https://github.com/rhyang2021/ARIA) | <img src="https://img.shields.io/github/stars/rhyang2021/ARIA?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.6 | Fudan University | [Paper](https://arxiv.org/abs/2506.00539) | Custom |
| [AMPO](https://github.com/MozerWang/AMPO) | <img src="https://img.shields.io/github/stars/MozerWang/AMPO?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.5 | Tongyi Lab, Alibaba | [Paper](https://arxiv.org/abs/2505.02156) | veRL |
| [MAPoRL](https://github.com/chanwoo-park-official/MAPoRL) | <img src="https://img.shields.io/github/stars/chanwoo-park-official/MAPoRL?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.8 | Academic | -- | Custom |
| [FlowReasoner](https://github.com/sail-sg/FlowReasoner) | <img src="https://img.shields.io/github/stars/sail-sg/FlowReasoner?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.4 | Sea AI Lab / NUS | [Paper](https://arxiv.org/abs/2504.15257) | Custom |
| [DrMAS](https://github.com/langfengQ/DrMAS) | <img src="https://img.shields.io/github/stars/langfengQ/DrMAS?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2026.2 | NTU | [Paper](https://arxiv.org/abs/2602.08847) | Custom |
| [MarsRL](https://github.com/liushulinle/MarsRL) | <img src="https://img.shields.io/github/stars/liushulinle/MarsRL?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.11 | Academic | [Paper](https://arxiv.org/abs/2511.11373) | veRL |
| [MrlX](https://github.com/AQ-MedAI/MrlX) | <img src="https://img.shields.io/github/stars/AQ-MedAI/MrlX?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.10 | Ant Group (AQ-MedAI) | [Paper](https://arxiv.org/abs/2511.13288) | Custom (SGLang + Megatron) |
| [CoMAS](https://github.com/xxyQwQ/CoMAS) | <img src="https://img.shields.io/github/stars/xxyQwQ/CoMAS?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.10 | Shanghai AI Lab / CUHK / Oxford / NUS | [Paper](https://arxiv.org/abs/2510.08529) | Custom |
| [CoMLRL](https://github.com/OpenMLRL/CoMLRL) | <img src="https://img.shields.io/github/stars/OpenMLRL/CoMLRL?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.8 | OpenMLRL | [Paper](https://arxiv.org/abs/2508.04652) | TRL |
| [SPIRAL](https://github.com/spiral-rl/spiral) | <img src="https://img.shields.io/github/stars/spiral-rl/spiral?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.6 | NUS / A*STAR / Sea AI Lab | [Paper](https://arxiv.org/abs/2506.24119) | Oat |
| [MARFT](https://github.com/jwliao-ai/MARFT) | <img src="https://img.shields.io/github/stars/jwliao-ai/MARFT?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.4 | SII / SJTU | [Paper](https://arxiv.org/abs/2504.16129) | Custom |

<details>
<summary>📋 Click to view technical details</summary>

| Github Repo | RL Algorithm | Single/Multi Agent | Outcome/Process Reward | Single/Multi Turn | Task | Reward Type | Tool usage |
| :----: | :----: | :----: | :----: | :----: | :----: | :----: | :----: |
| [PettingLLMs](https://github.com/pettingllms-ai/PettingLLMs) | AT-GRPO | Multi | Both | Multi | Game/Code/Math/Planning | Rule (verifiable) | No |
| [MASPRM](https://github.com/milad1378yz/MASPRM) | PRM (trained from MCTS rollouts) | Multi | Process | Multi | Reasoning (GSM8K/MATH/MMLU) | Learned PRM | No |
| [ARIA](https://github.com/rhyang2021/ARIA) | REINFORCE | Both | Process | Multi | Negotiation/Bargaining | Other | No |
| [AMPO](https://github.com/MozerWang/AMPO) | BC/AMPO(GRPO improvement) | Multi | Outcome | Multi | Social Interaction | Model-based | No |
| [MAPoRL](https://github.com/chanwoo-park-official/MAPoRL) | PPO | Multi | Outcome | Multi | Collaborative LLM Tasks | Rule | No |
| [FlowReasoner](https://github.com/sail-sg/FlowReasoner) | GRPO | Multi | Outcome | Multi | Multi-agent Workflow Design | Rule | Yes |
| [DrMAS](https://github.com/langfengQ/DrMAS) | GRPO (agent-wise) | Multi | Outcome | Multi | Multi-agent LLM Systems | Rule | No |
| [MarsRL](https://github.com/liushulinle/MarsRL) | RLVR (agent-specific rewards) | Multi | Both | Multi | Math Reasoning (AIME/BeyondAIME) | Rule (verifiable) | No |
| [MrlX](https://github.com/AQ-MedAI/MrlX) | M-GRPO (hierarchical) | Multi | Outcome | Multi | Deep Research (GAIA/XBench) | Rule + Model | Yes (Search) |
| [CoMAS](https://github.com/xxyQwQ/CoMAS) | RL w/ LLM-Judge intrinsic reward | Multi | Process | Multi | Co-evolving Reasoning | Model | No |
| [CoMLRL](https://github.com/OpenMLRL/CoMLRL) | MAGRPO / MAREINFORCE / MARLOO | Multi | Outcome | Multi | Writing / Code / Minecraft | Custom | Minimal |
| [SPIRAL](https://github.com/spiral-rl/spiral) | Role-conditioned Advantage Estimation (RAE) | Multi | Outcome | Multi | Zero-sum Games (TicTacToe/Kuhn/Negotiation) | Rule | No |
| [MARFT](https://github.com/jwliao-ai/MARFT) | MARFT paradigm (action+token level) | Multi | Both | Multi | Research / Math | Rule | Yes |

</details>

## 🧠 Memory


| Github Repo | 🌟 Stars | Date | Org | Paper Link | RL Framework |
| :----: | :----: | :----: |  :----: | :----: | :----: |
| [MEM1](https://github.com/MIT-MI/MEM1) | <img src="https://img.shields.io/github/stars/MIT-MI/MEM1?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.7 | MIT | [Paper](https://arxiv.org/abs/2506.15841) | veRL (based on Search-R1) |
| [Memento](https://github.com/Agent-on-the-Fly/Memento) | <img src="https://img.shields.io/github/stars/Agent-on-the-Fly/Memento?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.6 | UCL, Huawei | [Paper](https://arxiv.org/abs/2508.16153) | Custom |
| [MemAgent](https://github.com/BytedTsinghua-SIA/MemAgent) | <img src="https://img.shields.io/github/stars/BytedTsinghua-SIA/MemAgent?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.6 | Bytedance, Tsinghua-SIA | [Paper](https://arxiv.org/abs/2507.02259) | veRL |
| [Mem-alpha](https://github.com/wangyu-ustc/Mem-alpha) | <img src="https://img.shields.io/github/stars/wangyu-ustc/Mem-alpha?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.9 | UCSD / USTC | [Paper](https://arxiv.org/abs/2509.25911) | veRL |
| [M3-Agent](https://github.com/bytedance-seed/m3-agent) | <img src="https://img.shields.io/github/stars/bytedance-seed/m3-agent?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.7 | ByteDance Seed / Zhejiang University | [Paper](https://arxiv.org/abs/2508.09736) | Custom |

<details>
<summary>📋 Click to view technical details</summary>

| Github Repo | RL Algorithm | Single/Multi Agent | Outcome/Process Reward | Single/Multi Turn | Task | Reward Type | Tool usage |
| :----: | :----: | :----: | :----: | :----: | :----: | :----: | :----: |
| [MEM1](https://github.com/MIT-MI/MEM1) | PPO/GRPO | Single | Outcome | Multi | WebShop/GSM8K/QA | Rule/Model | Yes |
| [Memento](https://github.com/Agent-on-the-Fly/Memento) | soft Q-Learning | Single | Outcome | Multi | Research/QA/Code/Web | External/Rule | Yes |
| [MemAgent](https://github.com/BytedTsinghua-SIA/MemAgent) | PPO, GRPO, DPO | Multi | Outcome | Multi | Long-context QA | Rule/Model/External | Yes |
| [Mem-alpha](https://github.com/wangyu-ustc/Mem-alpha) | GRPO | Single | Outcome | Multi | Long-context QA + Memory Construction | Rule (downstream QA) | Yes (memory tools) |
| [M3-Agent](https://github.com/bytedance-seed/m3-agent) | RL-based | Single | Outcome | Multi | Long-video QA (M3-Bench) | Rule/Model | Yes (multimodal memory graph) |

</details>

## 🦾 Embodied


| Github Repo | 🌟 Stars | Date | Org | Paper Link | RL Framework |
| :----: | :----: | :----: |  :----: | :----: | :----: |
| [Embodied-R1](https://github.com/pickxiguapi/Embodied-R1) | <img src="https://img.shields.io/github/stars/pickxiguapi/Embodied-R1?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.6 | Tianjing University | [Paper](http://arxiv.org/abs/2508.13998) | veRL |
| [STeCa](https://github.com/WangHanLinHenry/STeCa) | <img src="https://img.shields.io/github/stars/WangHanLinHenry/STeCa?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.2 | The Hong Kong Polytechnic University | [Paper](https://arxiv.org/abs/2502.14276) | FastChat/TRL |
| [VIKI-R](https://github.com/MARS-EAI/VIKI-R) | <img src="https://img.shields.io/github/stars/MARS-EAI/VIKI-R?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.6 | MARS-EAI (NeurIPS 2025 D&B) | [Paper](https://arxiv.org/abs/2506.09049) | veRL + LLaMA-Factory |

<details>
<summary>📋 Click to view technical details</summary>

| Github Repo | RL Algorithm | Single/Multi Agent | Outcome/Process Reward | Single/Multi Turn | Task | Reward Type | Tool usage |
| :----: | :----: | :----: | :----: | :----: | :----: | :----: | :----: |
| [Embodied-R1](https://github.com/pickxiguapi/Embodied-R1) | GRPO | Single | Outcome | Single | Grounding/Waypoint | Rule | No |
| [STeCa](https://github.com/WangHanLinHenry/STeCa) | DPO (RFT) | Single | Both | Multi | Embodied/Household | Rule/MC | Environment Actions |
| [VIKI-R](https://github.com/MARS-EAI/VIKI-R) | GRPO (RFT after SFT) | Multi | Outcome | Multi | Embodied Multi-Robot Cooperation (VIKI-Bench) | Rule + Model | No |

</details>

## 🏷️ Domain-Specific


| Github Repo | 🌟 Stars | Date | Org | Paper Link | RL Framework | Domain |
| :----: | :----: | :----: |  :----: | :----: | :----: | :----: |
| [MedSAM-Agent](https://github.com/CUHK-AIM-Group/MedSAM-Agent) | <img src="https://img.shields.io/github/stars/CUHK-AIM-Group/MedSAM-Agent?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2026.2 | CUHK/Tencent | [Paper](https://arxiv.org/abs/2602.03320) | Custom | Medical |
| [OS-R1](https://github.com/LHY-24/OS-R1) | <img src="https://img.shields.io/github/stars/LHY-24/OS-R1?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.8 | ISCAS | [Paper](https://arxiv.org/abs/2508.12551) | Custom | OS/Systems |
| [MMedAgent-RL](https://github.com/JanerhYang/MMedAgent-RL) | <img src="https://img.shields.io/github/stars/JanerhYang/MMedAgent-RL?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.8 | Unknown | [paper](https://arxiv.org/abs/2506.00555) | Unknown | Medical |
| [DoctorAgent-RL](https://github.com/JarvisUSTC/DoctorAgent-RL) | <img src="https://img.shields.io/github/stars/JarvisUSTC/DoctorAgent-RL?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.5 | UCAS/CAS/USTC | [Paper](https://arxiv.org/pdf/2505.19630) | RAGEN | Medical |
| [Biomni](https://github.com/snap-stanford/Biomni) | <img src="https://img.shields.io/github/stars/snap-stanford/Biomni?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.3 | Stanford University (SNAP) | [Paper](https://www.biorxiv.org/content/10.1101/2025.05.30.656746v1) | Custom | Biomedical |
| [Doctor-R1](https://github.com/thu-unicorn/Doctor-R1) | <img src="https://img.shields.io/github/stars/thu-unicorn/Doctor-R1?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.12 | Tsinghua (thu-unicorn) | [Paper](https://arxiv.org/abs/2510.04284) | veRL | Medical |
| [Alpha-R1](https://github.com/FinStep-AI/Alpha-R1) | <img src="https://img.shields.io/github/stars/FinStep-AI/Alpha-R1?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.12 | SJTU / FinStep.AI / StepFun | [Paper](https://arxiv.org/abs/2512.23515) | Custom | Financial |
| [MedResearcher-R1](https://github.com/AQ-MedAI/MedResearcher-R1) | <img src="https://img.shields.io/github/stars/AQ-MedAI/MedResearcher-R1?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.8 | Ant Group (AQ-MedAI) | [Paper](https://arxiv.org/abs/2508.14880) | Custom | Medical |
| [LegalDelta](https://github.com/NEUIR/LegalDelta) | <img src="https://img.shields.io/github/stars/NEUIR/LegalDelta?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.8 | Northeastern University (NEUIR) | [Paper](https://arxiv.org/abs/2508.12281) | Custom | Legal |

<details>
<summary>📋 Click to view technical details</summary>

| Github Repo | RL Algorithm | Single/Multi Agent | Outcome/Process Reward | Single/Multi Turn | Task | Reward Type | Tool usage |
| :----: | :----: | :----: | :----: | :----: | :----: | :----: | :----: |
| [MedSAM-Agent](https://github.com/CUHK-AIM-Group/MedSAM-Agent) | GRPO (via veRL) | Single | Both | Multi | Medical Image Segmentation | Model (clinical fidelity) | Yes (SAM/MedSAM2) |
| [OS-R1](https://github.com/LHY-24/OS-R1) | GRPO (via veRL) | Single | Outcome | Multi | Linux Kernel Tuning | Rule | Yes (LightRAG, kernel config) |
| [MMedAgent-RL](https://github.com/JanerhYang/MMedAgent-RL) | Unknown | Multi | Unknown | Unknown | Unknown | Unknown | Unknown |
| [DoctorAgent-RL](https://github.com/JarvisUSTC/DoctorAgent-RL) | GRPO | Multi | Both | Multi | Consultation/Diagnosis | Model/Rule | No |
| [Biomni](https://github.com/snap-stanford/Biomni) | TBD | Single | TBD | Single | scRNAseq/CRISPR/ADMET/Knowledge | TBD | Yes |
| [Doctor-R1](https://github.com/thu-unicorn/Doctor-R1) | Experiential Agentic RL | Multi | Both | Multi | Clinical inquiry & diagnosis | Model + Rule + safety veto | No |
| [Alpha-R1](https://github.com/FinStep-AI/Alpha-R1) | GRPO | Single | Outcome | Multi | Alpha factor screening (with real-time news) | External (portfolio returns) + Model | Yes |
| [MedResearcher-R1](https://github.com/AQ-MedAI/MedResearcher-R1) | GRPO-based (SFT + Online RL) | Single | Outcome | Multi | Medical Deep Research (MedBrowseComp) | Rule + Model | Yes (Search/KG) |
| [LegalDelta](https://github.com/NEUIR/LegalDelta) | GRPO (CoT-guided info-gain) | Single | Process | Multi | Legal Reasoning | Model + Rule | No |

</details>

## 🎯 Reward & Training Methodology


| Github Repo | 🌟 Stars | Date | Org | Paper Link | Focus |
| :----: | :----: | :----: |  :----: | :----: | :----: |
| [ToolPRMBench](https://github.com/David-Li0406/ToolPRMBench) | <img src="https://img.shields.io/github/stars/David-Li0406/ToolPRMBench?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2026.1 | Arizona State University | [Paper](https://arxiv.org/abs/2601.12294) | PRM Benchmark for Tool-Use |
| [RLVR-World](https://github.com/thuml/RLVR-World) | <img src="https://img.shields.io/github/stars/thuml/RLVR-World?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.5 | THU ML Group | [Paper](https://arxiv.org/abs/2505.13934) | RLVR for World Models |
| [AgentPRM](https://github.com/sanjibanc/agent_prm) | <img src="https://img.shields.io/github/stars/sanjibanc/agent_prm?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.2 | Cornell | [Paper](https://arxiv.org/abs/2502.10325) | Process Reward for Agents |
| [Agentic-Reward-Modeling](https://github.com/THU-KEG/Agentic-Reward-Modeling) | <img src="https://img.shields.io/github/stars/THU-KEG/Agentic-Reward-Modeling?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.2 | THU-KEG | [Paper](https://arxiv.org/abs/2502.19328) | Agentic Reward Agent |
| [AgentRM](https://github.com/thunlp/AgentRM) | <img src="https://img.shields.io/github/stars/thunlp/AgentRM?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.2 | THUNLP/Tsinghua | [Paper](https://arxiv.org/abs/2502.18407) | Generalizable Agent RM |
| [AgentProg](https://github.com/MobileLLM/AgentProg) | <img src="https://img.shields.io/github/stars/MobileLLM/AgentProg?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.5 | MobileLLM | [Paper](https://arxiv.org/abs/2505.18121) | Progress Reward Model (ProgRM) |

<details>
<summary>📋 Click to view technical details</summary>

| Github Repo | RL Algorithm | Single/Multi Agent | Outcome/Process Reward | Single/Multi Turn | Task | Reward Type | Tool usage |
| :----: | :----: | :----: | :----: | :----: | :----: | :----: | :----: |
| [ToolPRMBench](https://github.com/David-Li0406/ToolPRMBench) | N/A (Benchmark) | Single | Process | Multi | Tool-Use | Rule/Model | Yes |
| [RLVR-World](https://github.com/thuml/RLVR-World) | RLVR | Single | Outcome | Multi | World Modeling (Language/Video) | Model (verifiable) | No |
| [AgentPRM](https://github.com/sanjibanc/agent_prm) | PPO/DPO + PRM | Single | Process | Multi | ALFWorld/General | Model (PRM) | Yes |
| [Agentic-Reward-Modeling](https://github.com/THU-KEG/Agentic-Reward-Modeling) | DPO/Best-of-N | Single | Outcome | Single | General Instruction | Model (Reward Agent) | Yes (Verification) |
| [AgentRM](https://github.com/thunlp/AgentRM) | MCTS/RM-guided | Single | Outcome | Multi | 9 Agent Tasks | Model (regression PRM) | Yes |
| [AgentProg](https://github.com/MobileLLM/AgentProg) | Online RL w/ progress reward | Single | Process | Multi | GUI Agent Training | Model (ProgRM) | Yes |

</details>

## 🛡️ Safety


| Github Repo | 🌟 Stars | Date | Org | Paper Link | RL Framework |
| :----: | :----: | :----: |  :----: | :----: | :----: |
| [SafeSearch](https://github.com/amazon-science/SafeSearch) | <img src="https://img.shields.io/github/stars/amazon-science/SafeSearch?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.11 | Amazon Science | [Paper](https://arxiv.org/abs/2510.17017) | veRL |
| [curiosity_redteam](https://github.com/Improbable-AI/curiosity_redteam) | <img src="https://img.shields.io/github/stars/Improbable-AI/curiosity_redteam?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2024.2 | MIT | [Paper](https://arxiv.org/abs/2402.19464) | Custom |
| [RLbreaker](https://github.com/XuanChen-xc/RLbreaker) | <img src="https://img.shields.io/github/stars/XuanChen-xc/RLbreaker?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2024.6 | Purdue | [Paper](https://arxiv.org/abs/2406.08705) | Custom |
| [xJailbreak](https://github.com/Aegis1863/xJailbreak) | <img src="https://img.shields.io/github/stars/Aegis1863/xJailbreak?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.1 | Academic | [Paper](https://arxiv.org/abs/2501.16727) | Custom |
| [Auto-RT](https://github.com/icip-cas/Auto-RT) | <img src="https://img.shields.io/github/stars/icip-cas/Auto-RT?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.1 | ICIP-CAS | [Paper](https://arxiv.org/abs/2501.01830) | Custom |
| [ToolSafe](https://github.com/MurrayTom/ToolSafe) | <img src="https://img.shields.io/github/stars/MurrayTom/ToolSafe?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2026.1 | Academic (MurrayTom) | [Paper](https://arxiv.org/abs/2601.10156) | veRL |
| [TROJail](https://github.com/xxiqiao/TROJail) | <img src="https://img.shields.io/github/stars/xxiqiao/TROJail?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.12 | Academic (ACL 2026) | [Paper](https://arxiv.org/abs/2512.07761) | RAGEN + vLLM |
| [Jailbreak-R1](https://github.com/yuki-younai/Jailbreak-R1) | <img src="https://img.shields.io/github/stars/yuki-younai/Jailbreak-R1?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.6 | Academic (yuki-younai) | [Paper](https://arxiv.org/abs/2506.00782) | Custom |
| [GuardReasoner-VL](https://github.com/yueliu1999/GuardReasoner-VL) | <img src="https://img.shields.io/github/stars/yueliu1999/GuardReasoner-VL?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.5 | NUS (yueliu1999) | [Paper](https://arxiv.org/abs/2505.11049) | Custom |

<details>
<summary>📋 Click to view technical details</summary>

| Github Repo | RL Algorithm | Single/Multi Agent | Outcome/Process Reward | Single/Multi Turn | Task | Reward Type | Tool usage |
| :----: | :----: | :----: | :----: | :----: | :----: | :----: | :----: |
| [SafeSearch](https://github.com/amazon-science/SafeSearch) | PPO (GAE/GRPO) | Single | Both | Multi | Safe QA/Search | Rule + Model | Search |
| [curiosity_redteam](https://github.com/Improbable-AI/curiosity_redteam) | RL + Curiosity | Single | Outcome | Multi | Red Teaming | Model | Yes (iterative query) |
| [RLbreaker](https://github.com/XuanChen-xc/RLbreaker) | Custom PPO | Single | Outcome | Multi | Jailbreaking | Model | Yes (mutator selection) |
| [xJailbreak](https://github.com/Aegis1863/xJailbreak) | RL | Single | Outcome | Multi | Jailbreaking | Model (embedding) | Yes (iterative) |
| [Auto-RT](https://github.com/icip-cas/Auto-RT) | PPO | Single | Outcome | Multi | Red Teaming | Model | Yes (strategy exploration) |
| [ToolSafe](https://github.com/MurrayTom/ToolSafe) | Multi-task GRPO | Single | Process | Multi | Tool-Invocation Safety Guardrail | Rule + Model | Yes (tool monitoring) |
| [TROJail](https://github.com/xxiqiao/TROJail) | Multi-turn GRPO variant | Single | Both | Multi | Multi-turn Jailbreak Attack | Model (harmfulness judge) + Rule | Yes (target LLM) |
| [Jailbreak-R1](https://github.com/yuki-younai/Jailbreak-R1) | GRPO (3-stage: imitation→warm-up→progressive) | Single | Both | Multi | Red-teaming Prompt Generation | Model (judge) | Yes (target LLM) |
| [GuardReasoner-VL](https://github.com/yueliu1999/GuardReasoner-VL) | Online RL w/ rejection sampling | Single | Both | Multi | VLM Safety Guard (multimodal) | Rule + Model | No |

</details>

## 👁️ VLM Agent


| Github Repo | 🌟 Stars | Date | Org | Paper Link | RL Framework |
| :----: | :----: | :----: |  :----: | :----: | :----: |
| [multimodal-search-r1](https://github.com/EvolvingLMMs-Lab/multimodal-search-r1) | <img src="https://img.shields.io/github/stars/EvolvingLMMs-Lab/multimodal-search-r1?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.6 | ByteDance/NTU | [Paper](https://arxiv.org/abs/2506.20670) | Custom |
| [DeepEyesV2](https://github.com/Visual-Agent/DeepEyesV2) | <img src="https://img.shields.io/github/stars/Visual-Agent/DeepEyesV2?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.11 | Xiaohongshu | [Paper](https://arxiv.org/abs/2511.05271) | Custom |
| [VDeepEyes](https://github.com/Visual-Agent/DeepEyes) | <img src="https://img.shields.io/github/stars/Visual-Agent/DeepEyes?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.5 | Xiaohongshu/XJTU | [Paper](https://arxiv.org/pdf/2505.14362) | veRL |
| [CoSo](https://github.com/langfengQ/CoSo) | <img src="https://img.shields.io/github/stars/langfengQ/CoSo?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.5 | NTU/Alibaba | [Paper](https://arxiv.org/abs/2505.03792) | Custom |
| [RL4VLM](https://github.com/RL4VLM/RL4VLM) | <img src="https://img.shields.io/github/stars/RL4VLM/RL4VLM?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2024.5 | UC Berkeley | [Paper](https://arxiv.org/abs/2405.10292) | Custom |
| [VSC-RL](https://github.com/ai-agents-2030/VSC_RL) | <img src="https://img.shields.io/github/stars/ai-agents-2030/VSC_RL?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.2 | Liverpool/Huawei/Tianjin/UCL | [Paper](https://arxiv.org/abs/2502.07949) | Custom |
| [AlphaDrive](https://github.com/hustvl/AlphaDrive) | <img src="https://img.shields.io/github/stars/hustvl/AlphaDrive?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.3 | HUST/Horizon Robotics | [Paper](https://arxiv.org/abs/2503.07608) | Custom |
| [Mini-o3](https://github.com/Mini-o3/Mini-o3) | <img src="https://img.shields.io/github/stars/Mini-o3/Mini-o3?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.9 | Mini-o3 team | [Paper](https://arxiv.org/abs/2509.07969) | veRL |
| [VisionThink](https://github.com/dvlab-research/VisionThink) | <img src="https://img.shields.io/github/stars/dvlab-research/VisionThink?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.7 | CUHK (dvlab-research) | [Paper](https://arxiv.org/abs/2507.13348) | veRL + EasyR1 |
| [AutoVLA](https://github.com/ucla-mobility/AutoVLA) | <img src="https://img.shields.io/github/stars/ucla-mobility/AutoVLA?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.6 | UCLA Mobility Lab | [Paper](https://arxiv.org/abs/2506.13757) | Custom |
| [Pixel-Reasoner](https://github.com/TIGER-AI-Lab/Pixel-Reasoner) | <img src="https://img.shields.io/github/stars/TIGER-AI-Lab/Pixel-Reasoner?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.5 | University of Waterloo (TIGER-AI-Lab) | [Paper](https://arxiv.org/abs/2505.15966) | OpenRLHF |
| [Visual-ARFT](https://github.com/Liuziyu77/Visual-RFT) | <img src="https://img.shields.io/github/stars/Liuziyu77/Visual-RFT?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.5 | Shanghai AI Lab / SJTU | [Paper](https://arxiv.org/abs/2505.14246) | Custom |
| [VTool-R1](https://github.com/VTOOL-R1/vtool-r1) | <img src="https://img.shields.io/github/stars/VTOOL-R1/vtool-r1?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.5 | UIUC | [Paper](https://arxiv.org/abs/2505.19255) | veRL + EasyR1 |
| [OpenThinkIMG](https://github.com/zhaochen0110/OpenThinkIMG) | <img src="https://img.shields.io/github/stars/zhaochen0110/OpenThinkIMG?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.5 | Academic (zhaochen0110) | [Paper](https://arxiv.org/abs/2505.08617) | OpenR1 |
| [Chain-of-Focus](https://github.com/xtong-zhang/Chain-of-Focus) | <img src="https://img.shields.io/github/stars/xtong-zhang/Chain-of-Focus?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.5 | Multi-institution | [Paper](https://arxiv.org/abs/2505.15436) | veRL |
| [GRIT](https://github.com/eric-ai-lab/GRIT) | <img src="https://img.shields.io/github/stars/eric-ai-lab/GRIT?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.5 | UC Santa Cruz (eric-ai-lab) | [Paper](https://arxiv.org/abs/2505.15879) | trl |

<details>
<summary>📋 Click to view technical details</summary>

| Github Repo | RL Algorithm | Single/Multi Agent | Outcome/Process Reward | Single/Multi Turn | Task | Reward Type | Tool usage |
| :----: | :----: | :----: | :----: | :----: | :----: | :----: | :----: |
| [multimodal-search-r1](https://github.com/EvolvingLMMs-Lab/multimodal-search-r1) | GRPO | Single | Outcome | Multi | Multimodal Search | Rule | Yes (Search) |
| [DeepEyesV2](https://github.com/Visual-Agent/DeepEyesV2) | Outcome RL | Single | Outcome | Multi | Multimodal Reasoning | Rule | Yes (Code exec, Web search) |
| [VDeepEyes](https://github.com/Visual-Agent/DeepEyes) | PPO/GRPO | Multi | Process | Multi | VQA | All | Yes |
| [CoSo](https://github.com/langfengQ/CoSo) | Soft RL (counterfactual) | Single | Outcome | Multi | Android/Card/Embodied | Rule | Yes |
| [RL4VLM](https://github.com/RL4VLM/RL4VLM) | PPO | Single | Outcome | Multi | GymCards/ALFWorld | Rule | Yes |
| [VSC-RL](https://github.com/ai-agents-2030/VSC_RL) | Variational RL | Single | Outcome | Multi | Mobile Device Control | Rule | Yes |
| [AlphaDrive](https://github.com/hustvl/AlphaDrive) | GRPO | Single | Outcome | Multi | Autonomous Driving | Rule (4 planning rewards) | No |
| [Mini-o3](https://github.com/Mini-o3/Mini-o3) | GRPO | Single | Outcome | Multi | Visual Search (V*/HR-Bench) | Rule | Yes (image crop) |
| [VisionThink](https://github.com/dvlab-research/VisionThink) | GRPO w/ LLM-as-Judge | Single | Outcome | Multi | Efficient VQA | Model (LLM-Judge) | Yes (hi-res request) |
| [AutoVLA](https://github.com/ucla-mobility/AutoVLA) | GRPO (RFT after SFT) | Single | Outcome | Multi | Autonomous Driving (nuScenes/nuPlan/Waymo) | Rule (PDMS) | No |
| [Pixel-Reasoner](https://github.com/TIGER-AI-Lab/Pixel-Reasoner) | Curiosity-driven GRPO | Single | Both | Multi | Visual Reasoning (V*/TallyQA/Info-VQA) | Rule + Model | Yes (zoom/select-frame) |
| [Visual-ARFT](https://github.com/Liuziyu77/Visual-RFT) | GRPO (agentic RFT) | Single | Outcome | Multi | Multimodal Agentic Tool Use (MAT-Search/Coding) | Rule | Yes (Search/Python) |
| [VTool-R1](https://github.com/VTOOL-R1/vtool-r1) | RFT (GRPO-based) | Single | Outcome | Multi | Chart/Table VQA | Rule | Yes (Python visual tools) |
| [OpenThinkIMG](https://github.com/zhaochen0110/OpenThinkIMG) | V-ToolRL (GRPO) | Single | Outcome | Multi | Chart Reasoning | Rule | Yes (GroundingDINO/SAM/OCR/crop) |
| [Chain-of-Focus](https://github.com/xtong-zhang/Chain-of-Focus) | AGAR (GRPO) | Single | Outcome | Multi | Visual Reasoning (V*) | Rule (outcome+format) | Yes (zoom-in) |
| [GRIT](https://github.com/eric-ai-lab/GRIT) | GRPO-GR (Grounded Reasoning) | Single | Outcome | Single | Visual Reasoning (bbox) | Rule | Yes (bbox) |

</details>

## 🔄 Self-Evolution

> ⚠️ **Note**: The definition of "Self-Evolution" in the context of RL for LLM agents is still evolving and not yet well-established. This category currently collects works whose paper titles explicitly contain "self-evolving" or "self-evolution", where the agent improves itself through RL-driven feedback loops.


| Github Repo | 🌟 Stars | Date | Org | Paper Link | RL Framework |
| :----: | :----: | :----: |  :----: | :----: | :----: |
| [AgentEvolver](https://github.com/modelscope/AgentEvolver) | <img src="https://img.shields.io/github/stars/modelscope/AgentEvolver?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.11 | Alibaba/Tongyi Lab | [Paper](https://arxiv.org/abs/2511.10395) | Custom |
| [SEAgent](https://github.com/SunzeY/SEAgent) | <img src="https://img.shields.io/github/stars/SunzeY/SEAgent?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.8 | Shanghai AI Lab / CUHK | [Paper](https://arxiv.org/abs/2508.04700) | Custom |
| [MemSkill](https://github.com/ViktorAxelsen/MemSkill) | <img src="https://img.shields.io/github/stars/ViktorAxelsen/MemSkill?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2026.2 | NTU/UIUC/UIC/Tsinghua | [Paper](https://arxiv.org/abs/2602.02474) | Custom |
| [MemRL](https://github.com/MemTensor/MemRL) | <img src="https://img.shields.io/github/stars/MemTensor/MemRL?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2026.1 | SJTU/Xidian/NUS/USTC/MemTensor | [Paper](https://arxiv.org/abs/2601.03192) | Custom |
| [RAGEN](https://github.com/RAGEN-AI/RAGEN) | <img src="https://img.shields.io/github/stars/RAGEN-AI/RAGEN?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.1 | RAGEN-AI | [Paper](https://arxiv.org/pdf/2504.20073) | veRL |
| [WebRL](https://github.com/THUDM/WebRL) | <img src="https://img.shields.io/github/stars/THUDM/WebRL?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2024.11 | Tsinghua/Zhipu AI | [Paper](https://arxiv.org/abs/2411.02337) | Custom |
| [EvolveR](https://github.com/Edaizi/EvolveR) | <img src="https://img.shields.io/github/stars/Edaizi/EvolveR?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.10 | KnowledgeXLab / Shanghai AI Lab | [Paper](https://arxiv.org/abs/2510.16079) | veRL |
| [R-Zero](https://github.com/Chengsong-Huang/R-Zero) | <img src="https://img.shields.io/github/stars/Chengsong-Huang/R-Zero?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.8 | Tencent AI Seattle Lab / WashU / UMD | [Paper](https://arxiv.org/abs/2508.05004) | EasyR1 |
| [Absolute-Zero-Reasoner](https://github.com/LeapLabTHU/Absolute-Zero-Reasoner) | <img src="https://img.shields.io/github/stars/LeapLabTHU/Absolute-Zero-Reasoner?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.5 | Tsinghua (LeapLabTHU) / BIGAI / PSU | [Paper](https://arxiv.org/abs/2505.03335) | veRL |

<details>
<summary>📋 Click to view technical details</summary>

| Github Repo | RL Algorithm | Single/Multi Agent | Outcome/Process Reward | Single/Multi Turn | Task | Reward Type | Tool usage |
| :----: | :----: | :----: | :----: | :----: | :----: | :----: | :----: |
| [AgentEvolver](https://github.com/modelscope/AgentEvolver) | ADCA-GRPO | Single | Outcome | Multi | Social Game/Tool-use | Rule | Yes |
| [SEAgent](https://github.com/SunzeY/SEAgent) | GRPO | Single | Outcome | Multi | Computer Use (OSWorld) | Model | Yes (Screenshot-based) |
| [MemSkill](https://github.com/ViktorAxelsen/MemSkill) | PPO | Single | Process | Multi | QA/ALFWorld | Model (learned skills) | Yes |
| [MemRL](https://github.com/MemTensor/MemRL) | RL-based (Q-value) | Single | Process | Multi | HLE/BigCodeBench/ALFWorld | Model (retrieval) | Yes |
| [RAGEN](https://github.com/RAGEN-AI/RAGEN) | PPO/GRPO (StarPO) | Single | Both | Multi | TextGame | All | Yes |
| [WebRL](https://github.com/THUDM/WebRL) | Actor-Critic RL + ORM | Single | Outcome | Multi | Web Navigation (WebArena) | Model (ORM) | Yes (Web browsing) |
| [EvolveR](https://github.com/Edaizi/EvolveR) | GRPO (closed-loop online+offline) | Single | Outcome | Multi | Multi-hop QA (NQ/HotpotQA) | Rule | Yes (experience retrieval) |
| [R-Zero](https://github.com/Chengsong-Huang/R-Zero) | GRPO (Challenger + Solver co-evolution) | Multi | Outcome | Multi | Math/SuperGPQA/MMLU-Pro/BBEH | Rule (majority voting) | No |
| [Absolute-Zero-Reasoner](https://github.com/LeapLabTHU/Absolute-Zero-Reasoner) | TRR++ (Task-Relative REINFORCE++) | Single | Outcome | Single | Code/Math Reasoning (HumanEval/MBPP/LiveCodeBench) | Rule + learnability | Yes (Python exec) |

</details>

## ⛰️ Environment

| Github Repo | 🌟 Stars | Date | Org | Task |
| :----: | :----: | :----: |  :----: | :----: |
| [OpenSandbox](https://github.com/alibaba/OpenSandbox) | <img src="https://img.shields.io/github/stars/alibaba/OpenSandbox?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2026.3 | Alibaba | Code/GUI/Agent Eval |
| [OpenEnv](https://github.com/meta-pytorch/OpenEnv) | <img src="https://img.shields.io/github/stars/meta-pytorch/OpenEnv?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2026.3 | Meta (PyTorch) | Chess/Arcade/Finance |
| [NeMo-Gym](https://github.com/NVIDIA-NeMo/Gym) | <img src="https://img.shields.io/github/stars/NVIDIA-NeMo/Gym?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2026.1 | NVIDIA | Multi-step/Multi-turn |
| [open-trajectory-gym](https://github.com/westonbrown/open-trajectory-gym) | <img src="https://img.shields.io/github/stars/westonbrown/open-trajectory-gym?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2026.3 | Individual | CTF/Security |
| [R2E-Gym](https://github.com/R2E-Gym/R2E-Gym) | <img src="https://img.shields.io/github/stars/R2E-Gym/R2E-Gym?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.4 | UC Berkeley/ANU | SWE |
| [LoCoBench-Agent](https://github.com/SalesforceAIResearch/LoCoBench-Agent) | ![](https://img.shields.io/github/stars/SalesforceAIResearch/LoCoBench-Agent.svg?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700) | 2025.11 | Salesforce AI Research | SWE |
| [Simia-Agent-Training](https://github.com/microsoft/Simia-Agent-Training) | ![](https://img.shields.io/github/stars/microsoft/Simia-Agent-Training.svg?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700) | 2025.10 | Microsoft | ToolUse/API |
| [PaperArena](https://github.com/Melmaphother/PaperArena) | <img src="https://img.shields.io/github/stars/Melmaphother/PaperArena?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.9 | University of Science and Technology of China | ScientificLiteratureQA |
| [enterprise-deep-research](https://github.com/SalesforceAIResearch/enterprise-deep-research) | ![](https://img.shields.io/github/stars/SalesforceAIResearch/enterprise-deep-research.svg?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700) | 2025.9 | Salesforce AI Research | DeepResearch |
| [meta-agents-research-environments](https://github.com/facebookresearch/meta-agents-research-environments) | <img src="https://img.shields.io/github/stars/facebookresearch/meta-agents-research-environments?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.9 | Meta (FAIR) | Gaia2 / Multi-universe |
| [BrowseComp-Plus](https://github.com/texttron/BrowseComp-Plus) | <img src="https://img.shields.io/github/stars/texttron/BrowseComp-Plus?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.8 | University of Waterloo | Deep Research Eval |
| [MCP-Bench](https://github.com/Accenture/mcp-bench) | <img src="https://img.shields.io/github/stars/Accenture/mcp-bench?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.8 | Accenture | MCP Tool-use (28 servers) |
| [MCPVerse](https://github.com/hailsham/mcpverse) | <img src="https://img.shields.io/github/stars/hailsham/mcpverse?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.8 | Individual | MCP Tools (550+) |
| [CompassVerifier](https://github.com/open-compass/CompassVerifier) | <img src="https://img.shields.io/github/stars/open-compass/CompassVerifier?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.7 | Shanghai AI Lab | Reasoning |
| [tau2-bench](https://github.com/sierra-research/tau2-bench) | <img src="https://img.shields.io/github/stars/sierra-research/tau2-bench?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.6 | Sierra Research | Tool-Agent-User |
| [MCP-Universe](https://github.com/SalesforceAIResearch/MCP-Universe) | <img src="https://img.shields.io/github/stars/SalesforceAIResearch/MCP-Universe?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.5 | Salesforce AI Research | MCP Tool-use |
| [SWE-smith](https://github.com/SWE-bench/SWE-smith) | <img src="https://img.shields.io/github/stars/SWE-bench/SWE-smith?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.4 | Princeton/Stanford/SWE-bench | SWE |
| [SWE-Gym](https://github.com/SWE-Gym/SWE-Gym) | <img src="https://img.shields.io/github/stars/SWE-Gym/SWE-Gym?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2024.12 | UC Berkeley/UIUC/CMU/Apple | SWE |
| [Mind2Web-2](https://github.com/OSU-NLP-Group/Mind2Web-2) | <img src="https://img.shields.io/github/stars/OSU-NLP-Group/Mind2Web-2?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.6 | Ohio State University | Web |
| [gem](https://github.com/axon-rl/gem) | <img src="https://img.shields.io/github/stars/axon-rl/gem?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.5 | Sea AI Lab | Math/Code/Game/QA |
| [MLE-Dojo](https://github.com/MLE-Dojo/MLE-Dojo) | <img src="https://img.shields.io/github/stars/MLE-Dojo/MLE-Dojo?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.5 | GIT, Stanford | MLE |
| [atropos](https://github.com/NousResearch/atropos) | <img src="https://img.shields.io/github/stars/NousResearch/atropos?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.4 | Nous Research | Game/Code/Tool |
| [InternBootcamp](https://github.com/InternLM/InternBootcamp) | <img src="https://img.shields.io/github/stars/InternLM/InternBootcamp?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.4 | InternBootcamp | Coding/QA/Game |
| [loong](https://github.com/camel-ai/loong) | <img src="https://img.shields.io/github/stars/camel-ai/loong?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.3 | CAMEL-AI.org | RLVR |
| [DataSciBench](https://github.com/THUDM/DataSciBench) | <img src="https://img.shields.io/github/stars/THUDM/DataSciBench?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.2 | Tsinghua | data analysis |
| [reasoning-gym](https://github.com/open-thought/reasoning-gym) | <img src="https://img.shields.io/github/stars/open-thought/reasoning-gym?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.1 | open-thought | Math/Game |
| [llmgym](https://github.com/tensorzero/llmgym) | <img src="https://img.shields.io/github/stars/tensorzero/llmgym?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2025.1 | tensorzero | TextGame/Tool |
| [debug-gym](https://github.com/microsoft/debug-gym) | <img src="https://img.shields.io/github/stars/microsoft/debug-gym?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2024.11 | Microsoft Research | Debugging/Game/Code |
| [gym-llm](https://github.com/rsanchezmo/gym-llm) | <img src="https://img.shields.io/github/stars/rsanchezmo/gym-llm?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2024.8 | Rodrigo Sánchez Molina | Control/Game |
| [AgentGym](https://github.com/WooooDyy/AgentGym) | <img src="https://img.shields.io/github/stars/WooooDyy/AgentGym?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2024.6 | Fudan | Web/Game |
| [tau-bench](https://github.com/sierra-research/tau-bench) | <img src="https://img.shields.io/github/stars/sierra-research/tau-bench?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2024.6 | Sierra | Tool |
| [appworld](https://github.com/StonyBrookNLP/appworld) | <img src="https://img.shields.io/github/stars/StonyBrookNLP/appworld?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2024.6 | Stony Brook University | Phone Use |
| [android_world](https://github.com/google-research/android_world) | <img src="https://img.shields.io/github/stars/google-research/android_world?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2024.5 | Google Research | Phone Use |
| [TheAgentCompany](https://github.com/TheAgentCompany/TheAgentCompany) | <img src="https://img.shields.io/github/stars/TheAgentCompany/TheAgentCompany?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2024.3 | CMU, Duke | Coding |
| [LlamaGym](https://github.com/KhoomeiK/LlamaGym) | <img src="https://img.shields.io/github/stars/KhoomeiK/LlamaGym?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2024.3 | Rohan Pandey | Game|
| [visualwebarena](https://github.com/web-arena-x/visualwebarena)   | <img src="https://img.shields.io/github/stars/web-arena-x/visualwebarena?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2024.1 | CMU | Web |
| [LMRL-Gym](https://github.com/abdulhaim/LMRL-Gym) | <img src="https://img.shields.io/github/stars/abdulhaim/LMRL-Gym?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2023.12 | UC Berkeley | Game |
| [OSWorld](https://github.com/xlang-ai/OSWorld) | <img src="https://img.shields.io/github/stars/xlang-ai/OSWorld?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2023.10 | HKU, CMU, Salesforce, Waterloo | Computer Use |
| [webarena](https://github.com/web-arena-x/webarena) | <img src="https://img.shields.io/github/stars/web-arena-x/webarena?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2023.7 | CMU | Web |
| [AgentBench](https://github.com/THUDM/AgentBench) | <img src="https://img.shields.io/github/stars/THUDM/AgentBench?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2023.7 | Tsinghua University | Game/Web/QA/Tool |
| [WebShop](https://github.com/princeton-nlp/WebShop) | <img src="https://img.shields.io/github/stars/princeton-nlp/WebShop?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2022.7 | Princeton-NLP | Web |
| [ScienceWorld](https://github.com/allenai/ScienceWorld) | <img src="https://img.shields.io/github/stars/allenai/ScienceWorld?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2022.3 | AllenAI | TextGame/ScienceQA |
| [alfworld](https://github.com/alfworld/alfworld) | <img src="https://img.shields.io/github/stars/alfworld/alfworld?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2020.10 | Microsoft, CMU, UW | Embodied |
| [factorio-learning-environment](https://github.com/JackHopkins/factorio-learning-environment) | <img src="https://img.shields.io/github/stars/JackHopkins/factorio-learning-environment?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2021.6 | JackHopkins | Game |
| [jericho](https://github.com/microsoft/jericho) | <img src="https://img.shields.io/github/stars/microsoft/jericho?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2018.10 | Microsoft, GIT | TextGame |
| [TextWorld](https://github.com/microsoft/TextWorld) | <img src="https://img.shields.io/github/stars/microsoft/TextWorld?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=ffd700" alt="Stars"> | 2018.6 | Microsoft Research | TextGame |

## Under Review/Waiting for Open Source
- [JoyAgents-R1: Joint Evolution Dynamics for Versatile Multi-LLM Agents with Reinforcement Learning](https://arxiv.org/abs/2506.19846)
- [Shop-R1: Rewarding LLMs to Simulate Human Behavior in Online Shopping via Reinforcement Learning](https://arxiv.org/abs/2507.17842)
- [Training Long-Context, Multi-Turn Software Engineering Agents with Reinforcement Learning](https://arxiv.org/abs/2508.03501)
- [Acting Less is Reasoning More! Teaching Model to Act Efficiently](https://arxiv.org/abs/2504.14870)
- [Agentic Reasoning and Tool Integration for LLMs via Reinforcement Learning](https://arxiv.org/abs/2505.01441)
- [ComputerRL: Scaling End-to-End Online Reinforcement Learning for Computer Use Agents](https://arxiv.org/abs/2508.14040)
- [Atom-Searcher: Enhancing Agentic Deep Research via Fine-Grained Atomic Thought Reward](https://github.com/antgroup/Research-Venus)
- [MUA-RL: MULTI-TURN USER-INTERACTING AGENTREINFORCEMENT LEARNING FOR AGENTIC TOOL USE](https://github.com/zzwkk/MUA-RL)
- [Understanding Tool-Integrated Reasoning](https://zhongwenxu.notion.site/Understanding-Tool-Integrated-Reasoning-2551c4e140e3805489fadcc802a1ea83)
- [Memory-R1: Enhancing Large Language Model Agents to Manage and Utilize Memories via Reinforcement Learning](https://arxiv.org/abs/2508.19828)
- [Encouraging Good Processes Without the Need for Good Answers: Reinforcement Learning for LLM Agent Planning](https://arxiv.org/abs/2508.19598)
- [SFR-DeepResearch: Towards Effective Reinforcement Learning for Autonomously Reasoning Single Agents](https://arxiv.org/abs/2509.06283)
- [WebExplorer: Explore and Evolve for Training Long-Horizon Web Agents](https://arxiv.org/abs/2509.06501)
- [EnvX: Agentize Everything with Agentic AI](https://arxiv.org/abs/2509.08088)
- [UI-TARS-2 Technical Report: Advancing GUI Agent with Multi-Turn Reinforcement Learning](https://arxiv.org/abs/2509.02544)
- [UI-Venus Technical Report: Building High-performance UI Agents with RFT](https://arxiv.org/abs/2508.10833)
- [Agent2 : An Agent-Generates-Agent Framework for Reinforcement Learning Automation](https://arxiv.org/abs/2509.13368)
- [Adversarial Reinforcement Learning for Large Language Model Agent Safety](https://arxiv.org/abs/2510.05442)
- [Learning to Refine: An Agentic RL Approach for Iterative SPARQL Query Construction](https://www.arxiv.org/abs/2511.11770)
- [InfoFlow: Reinforcing Search Agent Via Reward Density Optimization](https://arxiv.org/abs/2510.26575)

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=thinkwee/agentsMeetRL&type=Date)](https://www.star-history.com/#thinkwee/agentsMeetRL&Date)


## Citation

If you find this repository useful, please consider citing it:

```bibtex
@misc{agentsMeetRL,
  title={When LLM Agents Meet Reinforcement Learning: A Comprehensive Survey},
  author={AgentsMeetRL Contributors},
  year={2025},
  url={https://github.com/thinkwee/agentsMeetRL}
}
```

---

<div align="center">
  <p>Made with ❤️ by the AgentsMeetRL community</p>
</div>
