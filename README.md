<div align="center">
  <img src="logo.png" alt="NOVER Logo" width="500">
</div>

# When LLM Agents Meet Reinforcement Learning

This is an awesome list that summarizes open-source repositories for training LLM Agents using reinforcement learning:
 - The criteria for identifying an agent project is that it must have at least one of the following: multi-turn interactions or tool use.
 - This project is based on code analysis from open-source repositories using GitHub Copilot Agent, which may contain unfaithful cases. Although manually reviewed, there may still be omissions. If you find any errors, please don't hesitate to let us know immediately through issues or PRs - we warmly welcome them!
 - We particularly focus on the reinforcement learning frameworks, RL algorithms, rewards, and environments that projects depend on, for everyone's reference on how these excellent open-source projects make their technical choices.
 - Enumeration for Reward Type: External Verifier/Simple Rule/Model Based/Custom.
 - Feel free to submit your own projects anytime - we welcome contributions!

---

## Base Framework
| Github Repo | Stars | Date | Org | Paper Link | RL Framework |  RL Algorithm | Single/Multi Agent | Outcome/Process Reward | Single/Multi Turn | Task | Reward Type | Tool usage |
| :----: | :----: | :----: |  :----: | :----: | :----: | :----: | :----: | :----: | :----: | :----: | :----: | :----: |
| [AReaL](https://github.com/inclusionAI/AReaL) | ![](https://img.shields.io/github/stars/inclusionAI/AReaL.svg?color=F4B0A5&logo=Undertale&logoColor=FB6571) | 2025.6 | AntGroup/Tsinghua | [paper](https://arxiv.org/pdf/2505.24298) | Custom | PPO | Both | Outcome | Both | Math/Code | External | Yes |
| [ROLL](https://github.com/alibaba/ROLL) | ![](https://img.shields.io/github/stars/alibaba/ROLL.svg?color=F4B0A5&logo=Undertale&logoColor=FB6571) | 2025.6 | Alibaba | [paper](https://arxiv.org/pdf/2506.06122) | Custom | PPO/GRPO/Reinforce++/TOPR/RAFT++ | Multi | Both | Multi | Math/QA/Code/Alignment | All | Yes |
| [MARTI](https://github.com/TsinghuaC3I/MARTI) | ![](https://img.shields.io/github/stars/TsinghuaC3I/MARTI.svg?color=F4B0A5&logo=Undertale&logoColor=FB6571) | 2025.5 | Tsinghua | -- | Custom | PPO/GRPO/REINFORCE++/TTRL | Multi | Both | Multi | Math | All | Yes |
| [verifiers](https://github.com/willccbb/verifiers) | ![](https://img.shields.io/github/stars/willccbb/verifiers.svg?color=F4B0A5&logo=Undertale&logoColor=FB6571) | 2025.3 | Individual | -- | HuggingFace | GRPO | Multi | Outcome | Both | Reasoning/Math/Code | All | Code |
| [oat](https://github.com/sail-sg/oat) | ![](https://img.shields.io/github/stars/sail-sg/oat.svg?color=F4B0A5&logo=Undertale&logoColor=FB6571) | 2024.11 | NUS/Sea AI | [paper](https://arxiv.org/pdf/2411.01493) | Custom | PPO/GRPO | Single | Outcome | Multi | Math/Alignment | External | No |
| [verl](https://github.com/volcengine/verl) | ![](https://img.shields.io/github/stars/volcengine/verl.svg?color=F4B0A5&logo=Undertale&logoColor=FB6571) | 2024.10 | ByteDance | [paper](https://arxiv.org/pdf/2409.19256) | veRL | PPO/GRPO | Single | Outcome | Both | Math/QA/Reasoning/Search | All | Yes |
| [trl](https://github.com/huggingface/trl) | ![](https://img.shields.io/github/stars/huggingface/trl.svg?color=F4B0A5&logo=Undertale&logoColor=FB6571) | 2019.11 | HuggingFace | -- | TRL | PPO/GRPO/DPO | Single | Both | Single | QA | Custom | No |

## Search/Research/Web
| Github Repo | Stars | Date | Org | Paper Link | RL Framework |  RL Algorithm | Single/Multi Agent | Outcome/Process Reward | Single/Multi Turn | Task | Reward Type | Tool usage |
| :----: | :----: | :----: |  :----: | :----: | :----: | :----: | :----: | :----: | :----: | :----: | :----: | :----: |
| [TTI](https://github.com/test-time-interaction/TTI) | ![](https://img.shields.io/github/stars/test-time-interaction/TTI.svg?color=F4B0A5&logo=Undertale&logoColor=FB6571) | 2025.6 | CMU | [paper](https://arxiv.org/abs/2506.07976) | Custom | REINFORCE/BC | Single | Outcome | Multi | Web | External | Web Browsing |
| [R-Search](https://github.com/QingFei1/R-Search) | ![](https://img.shields.io/github/stars/QingFei1/R-Search.svg?color=F4B0A5&logo=Undertale&logoColor=FB6571) | 2025.6 | Individual | -- | veRL | PPO/GRPO | Single | Both | Multi | QA/Search | All | Yes |
| [R1-Searcher-plus](https://github.com/RUCAIBox/R1-Searcher-plus) | ![](https://img.shields.io/github/stars/RUCAIBox/R1-Searcher-plus.svg?color=F4B0A5&logo=Undertale&logoColor=FB6571) | 2025.5 | RUC | [paper](https://arxiv.org/pdf/2505.17005) | Custom | Custom | Single | Outcome | Multi | Search | Model | Search |
| [StepSearch](https://github.com/Zillwang/StepSearch) | ![](https://img.shields.io/github/stars/Zillwang/StepSearch.svg?color=F4B0A5&logo=Undertale&logoColor=FB6571) | 2025.5 | SenseTime | [paper](https://arxiv.org/pdf/2505.15107) | veRL | PPO | Single | Process | Multi | QA | Model | Search |
| [AutoRefine](https://github.com/syr-cn/AutoRefine) | ![](https://img.shields.io/github/stars/syr-cn/AutoRefine.svg?color=F4B0A5&logo=Undertale&logoColor=FB6571) | 2025.5 | USTC | [paper](https://www.arxiv.org/pdf/2505.11277) | veRL | PPO/GRPO | Multi | Both | Multi | RAG QA | Rule | Search |
| [ZeroSearch](https://github.com/Alibaba-NLP/ZeroSearch) | ![](https://img.shields.io/github/stars/Alibaba-NLP/ZeroSearch.svg?color=F4B0A5&logo=Undertale&logoColor=FB6571) | 2025.5 | Alibaba |[paper](https://arxiv.org/pdf/2505.04588) | veRL | PPO/GRPO/REINFORCE | Single | Outcome | Multi | QA/Search | Rule | Yes |
| [WebThinker](https://github.com/RUC-NLPIR/WebThinker) | ![](https://img.shields.io/github/stars/RUC-NLPIR/WebThinker.svg?color=F4B0A5&logo=Undertale&logoColor=FB6571) | 2025.4 | RUC | [paper](https://arxiv.org/pdf/2504.21776) | Custom | DPO | Single | Outcome | Multi | Reasoning/QA/Research | Model/External | Web Browsing |
| [DeepResearcher](https://github.com/GAIR-NLP/DeepResearcher) | ![](https://img.shields.io/github/stars/GAIR-NLP/DeepResearcher.svg?color=F4B0A5&logo=Undertale&logoColor=FB6571) | 2025.4 | SJTU | [paper](https://arxiv.org/pdf/2504.03160) | veRL | PPO/GRPO | Multi | Outcome | Multi | Research | All | Yes |
| [Search-R1](https://github.com/PeterGriffinJin/Search-R1) | ![](https://img.shields.io/github/stars/PeterGriffinJin/Search-R1.svg?color=F4B0A5&logo=Undertale&logoColor=FB6571) | 2025.3 | UIUC/Google | [paper1](https://arxiv.org/pdf/2503.09516), [paper2](https://arxiv.org/pdf/2505.15117) | veRL | PPO/GRPO | Single | Outcome | Multi | Search | All | Search |
| [R1-Searcher](https://github.com/RUCAIBox/R1-Searcher) | ![](https://img.shields.io/github/stars/RUCAIBox/R1-Searcher.svg?color=F4B0A5&logo=Undertale&logoColor=FB6571) | 2025.3 | RUC | [paper](https://arxiv.org/pdf/2503.05592) | OpenRLHF | PPO/DPO | Single | Both | Multi | Search | All | Yes |
| [WebAgent](https://github.com/Alibaba-NLP/WebAgent) | ![](https://img.shields.io/github/stars/Alibaba-NLP/WebAgent.svg?color=F4B0A5&logo=Undertale&logoColor=FB6571) | 2025.1 | Alibaba | [paper1](https://arxiv.org/pdf/2501.07572), [paper2](https://arxiv.org/pdf/2505.22648) | LLaMA-Factory | DAPO | Multi | Process | Multi | Web | Model | Yes |


## GUI
| Github Repo | Stars | Date | Org | Paper Link | RL Framework |  RL Algorithm | Single/Multi Agent | Outcome/Process Reward | Single/Multi Turn | Task | Reward Type | Tool usage |
| :----: | :----: | :----: |  :----: | :----: | :----: | :----: | :----: | :----: | :----: | :----: | :----: | :----: |
| [Grounding-R1](https://github.com/Yan98/Grounding-R1) | ![](https://img.shields.io/github/stars/Yan98/Grounding-R1.svg?color=F4B0A5&logo=Undertale&logoColor=FB6571) | 2025.6 | Salesforce | [blog](https://huggingface.co/blog/HelloKKMe/grounding-r1) | trl | GRPO | Single | Outcome | Multi | GUI Grounding | Model | Yes |
| [AgentCPM-GUI](https://github.com/OpenBMB/AgentCPM-GUI) | ![](https://img.shields.io/github/stars/OpenBMB/AgentCPM-GUI.svg?color=F4B0A5&logo=Undertale&logoColor=FB6571) | 2025.6 | OpenBMB/Tsinghua/RUC | [paper](https://arxiv.org/pdf/2506.01391) | Huggingface | GRPO | Single | Outcome | Multi | Mobile GUI | Model | Yes |
| [ARPO](https://github.com/dvlab-research/ARPO) | ![](https://img.shields.io/github/stars/dvlab-research/ARPO.svg?color=F4B0A5&logo=Undertale&logoColor=FB6571) | 2025.5 | CUHK/HKUST | [paper](https://arxiv.org/pdf/2505.16282) | veRL | GRPO | Single | Outcome | Multi | GUI | External | Computer Use |
| [GUI-G1](https://github.com/Yuqi-Zhou/GUI-G1) | ![](https://img.shields.io/github/stars/Yuqi-Zhou/GUI-G1.svg?color=F4B0A5&logo=Undertale&logoColor=FB6571) | 2025.5 | RUC | [paper](https://arxiv.org/pdf/2505.15810) | TRL | GRPO | Single | Outcome | Single | GUI | Rule/External | No |
| [GUI-R1](https://github.com/ritzz-ai/GUI-R1) | ![](https://img.shields.io/github/stars/ritzz-ai/GUI-R1.svg?color=F4B0A5&logo=Undertale&logoColor=FB6571) | 2025.4 | CAS/NUS | [paper](https://arxiv.org/pdf/2504.10458) | veRL | GRPO | Single | Outcome | Multi | GUI | Rule | No |
| [UI-R1](https://github.com/lll6gg/UI-R1) | ![](https://img.shields.io/github/stars/lll6gg/UI-R1.svg?color=F4B0A5&logo=Undertale&logoColor=FB6571) | 2025.3 | vivo/CUHK | [paper](https://arxiv.org/pdf/2503.21620) | TRL | GRPO | Single | Process | Both | GUI | Rule | Computer/Phone Use |

## Tool
| Github Repo | Stars | Date | Org | Paper Link | RL Framework |  RL Algorithm | Single/Multi Agent | Outcome/Process Reward | Single/Multi Turn | Task | Reward Type | Tool usage |
| :----: | :----: | :----: |  :----: | :----: | :----: | :----: | :----: | :----: | :----: | :----: | :----: | :----: |
| [verl-tool](https://github.com/TIGER-AI-Lab/verl-tool) | ![](https://img.shields.io/github/stars/TIGER-AI-Lab/verl-tool.svg?color=F4B0A5&logo=Undertale&logoColor=FB6571) | 2025.6 | TIGER-Lab | [X](https://x.com/DongfuJiang/status/1929198238017720379) | veRL | PPO/GRPO | Single | Both | Both | Math/Code | Rule/External | Yes |
| [Multi-Turn-RL-Agent](https://github.com/SiliangZeng/Multi-Turn-RL-Agent) | ![](https://img.shields.io/github/stars/SiliangZeng/Multi-Turn-RL-Agent.svg?color=F4B0A5&logo=Undertale&logoColor=FB6571) | 2025.5 | University of Minnesota | [paper](https://arxiv.org/pdf/2505.11821) | Custom | GRPO | Single | Both | Multi | Tool-use/Math | Rule/External | Yes |
| [Tool-N1](https://github.com/NVlabs/Tool-N1) | ![](https://img.shields.io/github/stars/NVlabs/Tool-N1.svg?color=F4B0A5&logo=Undertale&logoColor=FB6571) | 2025.5 | NVIDIA | [paper](https://arxiv.org/pdf/2505.00024) | veRL | PPO | Single | Outcome | Multi | Math/Dialogue | All | Yes |
| [Tool-Star](https://github.com/dongguanting/Tool-Star) | ![](https://img.shields.io/github/stars/dongguanting/Tool-Star.svg?color=F4B0A5&logo=Undertale&logoColor=FB6571) | 2025.5 | RUC | [paper](https://arxiv.org/pdf/2505.16410) | LLaMA-Factory | PPO/DPO/ORPO/SimPO/KTO | Single | Outcome | Multi | Multi-modal/Tool Use/Dialogue | Model/External | Yes |
| [RL-Factory](https://github.com/Simple-Efficient/RL-Factory) | ![](https://img.shields.io/github/stars/Simple-Efficient/RL-Factory.svg?color=F4B0A5&logo=Undertale&logoColor=FB6571) | 2025.5 | Simple-Efficient | [model](https://huggingface.co/Simple-Efficient/RLFactory-Qwen3-8B-GRPO) | veRL | GRPO | Multi | Both | Multi | Tool-use/NL2SQL | All | MCP |
| [ReTool](https://github.com/ReTool-RL/ReTool) | ![](https://img.shields.io/github/stars/ReTool-RL/ReTool.svg?color=F4B0A5&logo=Undertale&logoColor=FB6571) | 2025.4 | ByteDance | [paper](https://arxiv.org/pdf/2504.11536) | veRL | PPO | Single | Outcome | Multi | Math | External | Code |
| [Agent-R1](https://github.com/0russwest0/Agent-R1) | ![](https://img.shields.io/github/stars/0russwest0/Agent-R1.svg?color=F4B0A5&logo=Undertale&logoColor=FB6571) | 2025.3 | USTC | -- | veRL | PPO/GRPO | Single | Both | Multi | Tool-use/QA | Model | Yes |
| [ReCall](https://github.com/Agent-RL/ReCall) | ![](https://img.shields.io/github/stars/Agent-RL/ReCall.svg?color=F4B0A5&logo=Undertale&logoColor=FB6571) | 2025.3 | BaiChuan | [paper](https://arxiv.org/pdf/2503.19470) | veRL | PPO/GRPO/RLOO/REINFORCE++/ReMax | Single | Outcome | Multi | Tool-use/Math/QA | All | Yes |


## TextGame
| Github Repo | Stars | Date | Org | Paper Link | RL Framework |  RL Algorithm | Single/Multi Agent | Outcome/Process Reward | Single/Multi Turn | Task | Reward Type | Tool usage |
| :----: | :----: | :----: |  :----: | :----: | :----: | :----: | :----: | :----: | :----: | :----: | :----: | :----: |
| [ARIA](https://github.com/rhyang2021/ARIA) | ![](https://img.shields.io/github/stars/rhyang2021/ARIA.svg?color=F4B0A5&logo=Undertale&logoColor=FB6571) | 2025.6 | Fudan University | [paper](https://arxiv.org/abs/2506.00539) | Custom | REINFORCE | Both | Process | Multi | Negotiation/Bargaining | Other | No |
| [verl-agent](https://github.com/langfengQ/verl-agent) | ![](https://img.shields.io/github/stars/langfengQ/verl-agent.svg?color=F4B0A5&logo=Undertale&logoColor=FB6571) | 2025.5 | NTU/Skywork | [paper](https://arxiv.org/pdf/2505.10978) | veRL | PPO/GRPO/GiGPO/DAPO/RLOO/REINFORCE++ | Multi | Both | Multi | Phone Use/Math/Code/Web/TextGame | All | Yes |
| [SPA-RL-Agent](https://github.com/WangHanLinHenry/SPA-RL-Agent) | ![](https://img.shields.io/github/stars/WangHanLinHenry/SPA-RL-Agent.svg?color=F4B0A5&logo=Undertale&logoColor=FB6571) | 2025.5 | PolyU | [paper](https://arxiv.org/pdf/2505.20732) | TRL | PPO | Single | Process | Multi | Navigation/Web/TextGame | Model | No |
| [Trinity-RFT](https://github.com/modelscope/Trinity-RFT) | ![](https://img.shields.io/github/stars/modelscope/Trinity-RFT.svg?color=F4B0A5&logo=Undertale&logoColor=FB6571) | 2025.5 | Alibaba | [paper](https://arxiv.org/pdf/2505.17826) | veRL | PPO/GRPO | Single | Outcome | Both | Math/TextGame/Web | All | Yes |
| [VAGEN](https://github.com/RAGEN-AI/VAGEN) | ![](https://img.shields.io/github/stars/RAGEN-AI/VAGEN.svg?color=F4B0A5&logo=Undertale&logoColor=FB6571) | 2025.3 | RAGEN-AI | [paper](https://www.notion.so/VAGEN-Training-VLM-Agents-with-Multi-Turn-Reinforcement-Learning-1bfde13afb6e80b792f6d80c7c2fcad0) | veRL | PPO/GRPO | Single | Both | Multi | TextGame/Navigation | All | Yes |
| [ART](https://github.com/OpenPipe/ART) | ![](https://img.shields.io/github/stars/OpenPipe/ART.svg?color=F4B0A5&logo=Undertale&logoColor=FB6571) | 2025.3 | OpenPipe | [paper](https://github.com/OpenPipe/ART#-citation) | TRL | GRPO | Multi | Both | Multi | TextGame | All | Yes |
| [OpenManus-RL](https://github.com/OpenManus/OpenManus-RL) | ![](https://img.shields.io/github/stars/OpenManus/OpenManus-RL.svg?color=F4B0A5&logo=Undertale&logoColor=FB6571) | 2025.3 | UIUC/MetaGPT | -- | Custom | PPO/DPO/GRPO | Multi | Outcome | Multi | TextGame | All | Yes |
| [RAGEN](https://github.com/RAGEN-AI/RAGEN) | ![](https://img.shields.io/github/stars/RAGEN-AI/RAGEN.svg?color=F4B0A5&logo=Undertale&logoColor=FB6571) | 2025.1 | RAGEN-AI | [paper](https://arxiv.org/pdf/2504.20073) | veRL |PPO/GRPO | Single | Both | Multi | TextGame | All | Yes |

## QA(Reasoning/Math/Code)
| Github Repo | Stars | Date | Org | Paper Link | RL Framework |  RL Algorithm | Single/Multi Agent | Outcome/Process Reward | Single/Multi Turn | Task | Reward Type | Tool usage |
| :----: | :----: | :----: |  :----: | :----: | :----: | :----: | :----: | :----: | :----: | :----: | :----: | :----: |
| [MedAgentGym](https://github.com/wshi83/MedAgentGym) | ![](https://img.shields.io/github/stars/wshi83/MedAgentGym.svg?color=F4B0A5&logo=Undertale&logoColor=FB6571) | 2025.6 | Emory/Georgia Tech | [paper](https://arxiv.org/pdf/2506.04405) | Hugginface | SFT/DPO/PPO/GRPO | Single | Outcome | Multi | Medical/Code | External | Yes |
| [CURE](https://github.com/Gen-Verse/CURE) | ![](https://img.shields.io/github/stars/Gen-Verse/CURE.svg?color=F4B0A5&logo=Undertale&logoColor=FB6571) | 2025.6 | University of Chicago/Princeton/ByteDance | [paper](https://arxiv.org/pdf/2506.03136) | Huggingface | PPO | Single | Outcome | Single | Code | External | No |
| [MASLab](https://github.com/MASWorks/MASLab) | ![](https://img.shields.io/github/stars/MASWorks/MASLab.svg?color=F4B0A5&logo=Undertale&logoColor=FB6571) | 2025.5 | MASWorks | [paper](https://arxiv.org/pdf/2505.16988) | Custom | NO RL | Multi | Outcome | Multi | Code/Math/Reasoning | External | Yes |
| [Time-R1](https://github.com/ulab-uiuc/Time-R1) | ![](https://img.shields.io/github/stars/ulab-uiuc/Time-R1.svg?color=F4B0A5&logo=Undertale&logoColor=FB6571) | 2025.5 | UIUC | [paper](https://arxiv.org/pdf/2505.13508) | veRL | PPO/GRPO/DPO | Multi | Outcome | Multi | Temporal | All | Code |
| [agent-distillation](https://github.com/Nardien/agent-distillation) | ![](https://img.shields.io/github/stars/Nardien/agent-distillation.svg?color=F4B0A5&logo=Undertale&logoColor=FB6571) | 2025.5 | KAIST | [paper](https://arxiv.org/pdf/2505.17612) | Custom | PPO | Single | Process | Multi | QA/Math | External | Yes |
| [VDeepEyes](https://github.com/Visual-Agent/DeepEyes) | ![](https://img.shields.io/github/stars/Visual-Agent/DeepEyes.svg?color=F4B0A5&logo=Undertale&logoColor=FB6571) | 2025.5 | Xiaohongshu/XJTU | [paper](https://arxiv.org/pdf/2505.14362) | veRL | PPO/GRPO | Multi | Process | Multi | VQA | All | Yes |
| [ML-Agent](https://github.com/MASWorks/ML-Agent) | ![](https://img.shields.io/github/stars/MASWorks/ML-Agent.svg?color=F4B0A5&logo=Undertale&logoColor=FB6571) | 2025.5 | MASWorks | [paper](https://arxiv.org/pdf/2505.23723) | Custom | Custom | Single | Process | Multi | Code | All | Yes |
| [SkyRL](https://github.com/NovaSky-AI/SkyRL) | ![](https://img.shields.io/github/stars/NovaSky-AI/SkyRL.svg?color=F4B0A5&logo=Undertale&logoColor=FB6571) | 2025.4 | NovaSky | -- | veRL | PPO/GRPO | Single | Outcome | Multi | Math/Code | All | Code |
| [EasyR1](https://github.com/hiyouga/EasyR1) | ![](https://img.shields.io/github/stars/hiyouga/EasyR1.svg?color=F4B0A5&logo=Undertale&logoColor=FB6571) | 2025.4 | Individual | [repo1](https://github.com/hiyouga/EasyR1)/[paper2](https://arxiv.org/pdf/2409.19256) | veRL | GRPO | Single | Process | Multi | Vision-Language | Model | Yes |
| [sweet_rl](https://github.com/facebookresearch/sweet_rl) | ![](https://img.shields.io/github/stars/facebookresearch/sweet_rl.svg?color=F4B0A5&logo=Undertale&logoColor=FB6571) | 2025.3 | Meta/UCB | [paper](https://arxiv.org/pdf/2503.15478) | OpenRLHF | DPO | Multi | Process | Multi | Design/Code | Model | Web Browsing |
| [AutoCoA](https://github.com/ADaM-BJTU/AutoCoA) | ![](https://img.shields.io/github/stars/ADaM-BJTU/AutoCoA.svg?color=F4B0A5&logo=Undertale&logoColor=FB6571) | 2025.3 | BJTU | [paper](https://arxiv.org/pdf/2503.06580) | veRL | GRPO | Multi | Outcome | Multi | Reasoning/Math/QA | All | Yes |
| [ToRL](https://github.com/GAIR-NLP/ToRL) | ![](https://img.shields.io/github/stars/GAIR-NLP/ToRL.svg?color=F4B0A5&logo=Undertale&logoColor=FB6571) | 2025.3 | SJTU | [paper](https://arxiv.org/pdf/2503.23383) | veRL | GRPO | Single | Outcome | Single | Math | Rule/External | Yes |
| [Agentic-Reasoning](https://github.com/theworldofagents/Agentic-Reasoning) | ![](https://img.shields.io/github/stars/theworldofagents/Agentic-Reasoning.svg?color=F4B0A5&logo=Undertale&logoColor=FB6571) | 2025.2 | Oxford | [paper](https://arxiv.org/pdf/2502.04644) | Custom | Custom | Single | Process | Multi | QA/Math | External | Web Browsing |
| [open-r1](https://github.com/huggingface/open-r1) | ![](https://img.shields.io/github/stars/huggingface/open-r1.svg?color=F4B0A5&logo=Undertale&logoColor=FB6571) | 2025.1 | HuggingFace | -- | TRL | GRPO | Single | Outcome | Single | Math/Code | All | Yes |
| [openrlhf_async_pipline](https://github.com/yyht/openrlhf_async_pipline) | ![](https://img.shields.io/github/stars/yyht/openrlhf_async_pipline.svg?color=F4B0A5&logo=Undertale&logoColor=FB6571) | 2024.5 | OpenRLHF | [paper](https://arxiv.org/pdf/2405.11143) | OpenRLHF | PPO/REINFORCE++/DPO/RLOO | Single | Outcome | Multi | Dialogue/Reasoning/QA | All | No |



## Environment
| Github Repo | Stars | Date | Org | Paper Link | RL Framework |  RL Algorithm | Single/Multi Agent | Outcome/Process Reward | Single/Multi Turn | Task | Reward Type | Tool usage |
| :----: | :----: | :----: |  :----: | :----: | :----: | :----: | :----: | :----: | :----: | :----: | :----: | :----: |
| [InternBootcamp](https://github.com/InternLM/InternBootcamp) | ![](https://img.shields.io/github/stars/InternLM/InternBootcamp.svg?color=F4B0A5&logo=Undertale&logoColor=FB6571) | 2025.4 | InternBootcamp | -- | Environment | -- | -- | -- | -- | Reasoning/Code/Puzzle/Algorithm/TextGame | Rule/External | yes |

