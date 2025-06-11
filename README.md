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
| Github Repo | Date | Org | Paper Link | RL Framework |  RL Algorithm | Single/Multi Agent | Outcome/Process Reward | Single/Multi Turn | Task | Reward Type | Tool usage |
| --------- | --------- | --------- |  --------- | --------- | --------- | --------- | --------- | --------- | --------- | --------- | --------- |
| [verl](https://github.com/volcengine/verl) | 2024-10 | ByteDance | [paper](https://arxiv.org/pdf/2409.19256) | veRL | PPO/GRPO | Single | Outcome | Both | Math/QA/Reasoning/Search | All | Yes |
| [trl](https://github.com/huggingface/trl) | 2019-11 | HuggingFace | -- | TRL | PPO/GRPO/DPO | Single | Both | Single | QA | Custom | No |
| [verifiers](https://github.com/willccbb/verifiers) | 2025-03 | Individual | -- | HuggingFace | GRPO | Multi | Outcome | Both | Reasoning/Math/Code | All | Code |
| [oat](https://github.com/sail-sg/oat) | 2024-11 | NUS/Sea AI | [paper](https://arxiv.org/pdf/2411.01493) | Custom | PPO/GRPO | Single | Outcome | Multi | Math/Alignment | External | No |
| [ROLL](https://github.com/alibaba/ROLL) | 2025-06 | Alibaba | [paper](https://arxiv.org/pdf/2506.06122) | Custom | PPO/GRPO/Reinforce++/TOPR/RAFT++ | Multi | Both | Multi | Math/QA/Code/Alignment | All | Yes |
| [MARTI](https://github.com/TsinghuaC3I/MARTI) | 2025-05 | Tsinghua | -- | Custom | PPO/GRPO/REINFORCE++/TTRL | Multi | Both | Multi | Math | All | Yes |
| [AReaL](https://github.com/inclusionAI/AReaL) | 2025-06 | AntGroup/Tsinghua | [paper](https://arxiv.org/pdf/2505.24298) | Custom | PPO | Both | Outcome | Both | Math/Code | External | Yes |

## Search/Research/Web
| Github Repo | Date | Org | Paper Link | RL Framework |  RL Algorithm | Single/Multi Agent | Outcome/Process Reward | Single/Multi Turn | Task | Reward Type | Tool usage |
| --------- | --------- | --------- |  --------- | --------- | --------- | --------- | --------- | --------- | --------- | --------- | --------- |
| [WebThinker](https://github.com/RUC-NLPIR/WebThinker) | 2025-04 | RUC | [paper](https://arxiv.org/pdf/2504.21776) | Custom | DPO | Single | Outcome | Multi | Reasoning/QA/Research | Model/External | Web Browsing |
| [DeepResearcher](https://github.com/GAIR-NLP/DeepResearcher) | 2025-04 | SJTU | [paper](https://arxiv.org/pdf/2504.03160) | veRL | PPO/GRPO | Multi | Outcome | Multi | Research | All | Yes |
| [Search-R1](https://github.com/PeterGriffinJin/Search-R1) | 2025-03 | UIUC/Google | [paper1](https://arxiv.org/pdf/2503.09516), [paper2](https://arxiv.org/pdf/2505.15117) | veRL | PPO/GRPO | Single | Outcome | Multi | Search | All | Search |
| [AutoRefine](https://github.com/syr-cn/AutoRefine) | 2025-05 | USTC | [paper](https://www.arxiv.org/pdf/2505.11277) | veRL | PPO/GRPO | Multi | Both | Multi | RAG QA | Rule | Search |
| [StepSearch](https://github.com/Zillwang/StepSearch) | 2025-05 | SenseTime | [paper](https://arxiv.org/pdf/2505.15107) | veRL | PPO | Single | Process | Multi | QA | Model | Search |
| [R1-Searcher-plus](https://github.com/RUCAIBox/R1-Searcher-plus) | 2025-05 | RUC | [paper](https://arxiv.org/pdf/2505.17005) | Custom | Custom | Single | Outcome | Multi | Search | Model | Search |
| [ZeroSearch](https://github.com/Alibaba-NLP/ZeroSearch) | 2025-05 | Alibaba |[paper](https://arxiv.org/pdf/2505.04588) | veRL | PPO/GRPO/REINFORCE | Single | Outcome | Multi | QA/Search | Rule | Yes |
| [R1-Searcher](https://github.com/RUCAIBox/R1-Searcher) | 2025-03 | RUC | [paper](https://arxiv.org/pdf/2503.05592) | OpenRLHF | PPO/DPO | Single | Both | Multi | Search | All | Yes |
| [WebAgent](https://github.com/Alibaba-NLP/WebAgent) | 2025-01 | Alibaba | [paper1](https://arxiv.org/pdf/2501.07572), [paper2](https://arxiv.org/pdf/2505.22648) | LLaMA-Factory | DAPO | Multi | Process | Multi | Web | Model | Yes |
| [R-Search](https://github.com/QingFei1/R-Search) | 2025-06 | Individual | -- | veRL | PPO/GRPO | Single | Both | Multi | QA/Search | All | Yes |
| [TTI](https://github.com/test-time-interaction/TTI) | 2025-06 | CMU | [paper](https://arxiv.org/abs/2506.07976) | Custom | REINFORCE/BC | Single | Outcome | Multi | Web | External | Web Browsing |


## GUI
| Github Repo | Date | Org | Paper Link | RL Framework |  RL Algorithm | Single/Multi Agent | Outcome/Process Reward | Single/Multi Turn | Task | Reward Type | Tool usage |
| --------- | --------- | --------- |  --------- | --------- | --------- | --------- | --------- | --------- | --------- | --------- | --------- |
| [GUI-R1](https://github.com/ritzz-ai/GUI-R1) | 2025-04 | CAS/NUS | [paper](https://arxiv.org/pdf/2504.10458) | veRL | GRPO | Single | Outcome | Multi | GUI | Rule | No |
| [UI-R1](https://github.com/lll6gg/UI-R1) | 2025-03 | vivo/CUHK | [paper](https://arxiv.org/pdf/2503.21620) | TRL | GRPO | Single | Process | Both | GUI | Rule | Computer/Phone Use |
| [AgentCPM-GUI](https://github.com/OpenBMB/AgentCPM-GUI) | 2025-06 | OpenBMB/Tsinghua/RUC | [paper](https://arxiv.org/pdf/2506.01391) | Huggingface | GRPO | Single | Outcome | Multi | Mobile GUI | Model | Yes |
| [GUI-G1](https://github.com/Yuqi-Zhou/GUI-G1) | 2025-05 | RUC | [paper](https://arxiv.org/pdf/2505.15810) | TRL | GRPO | Single | Outcome | Single | GUI | Rule/External | No |
| [ARPO](https://github.com/dvlab-research/ARPO) | 2025-05 | CUHK/HKUST | [paper](https://arxiv.org/pdf/2505.16282) | veRL | GRPO | Single | Outcome | Multi | GUI | External | Computer Use |


## Tool
| Github Repo | Date | Org | Paper Link | RL Framework |  RL Algorithm | Single/Multi Agent | Outcome/Process Reward | Single/Multi Turn | Task | Reward Type | Tool usage |
| --------- | --------- | --------- |  --------- | --------- | --------- | --------- | --------- | --------- | --------- | --------- | --------- |
| [ReTool](https://github.com/ReTool-RL/ReTool) | 2025-04 | ByteDance | [paper](https://arxiv.org/pdf/2504.11536) | veRL | PPO | Single | Outcome | Multi | Math | External | Code |
| [Tool-N1](https://github.com/NVlabs/Tool-N1) | 2025-05 | NVIDIA | [paper](https://arxiv.org/pdf/2505.00024) | veRL | PPO | Single | Outcome | Multi | Math/Dialogue | All | Yes |
| [Tool-Star](https://github.com/dongguanting/Tool-Star) | 2025-05 | RUC | [paper](https://arxiv.org/pdf/2505.16410) | LLaMA-Factory | PPO/DPO/ORPO/SimPO/KTO | Single | Outcome | Multi | Multi-modal/Tool Use/Dialogue | Model/External | Yes |
| [verl-tool](https://github.com/TIGER-AI-Lab/verl-tool) | 2025-06 | TIGER-Lab | [X](https://x.com/DongfuJiang/status/1929198238017720379) | veRL | PPO/GRPO | Single | Both | Both | Math/Code | Rule/External | Yes |
| [RL-Factory](https://github.com/Simple-Efficient/RL-Factory) | 2025-05 | Simple-Efficient | [model](https://huggingface.co/Simple-Efficient/RLFactory-Qwen3-8B-GRPO) | veRL | GRPO | Multi | Both | Multi | Tool-use/NL2SQL | All | MCP |
| [Agent-R1](https://github.com/0russwest0/Agent-R1) | 2025-03 | USTC | -- | veRL | PPO/GRPO | Single | Both | Multi | Tool-use/QA | Model | Yes |
| [Multi-Turn-RL-Agent](https://github.com/SiliangZeng/Multi-Turn-RL-Agent) | 2025-05 | University of Minnesota | [paper](https://arxiv.org/pdf/2505.11821) | Custom | GRPO | Single | Both | Multi | Tool-use/Math | Rule/External | Yes |
| [ReCall](https://github.com/Agent-RL/ReCall) | 2025-03 | BaiChuan | [paper](https://arxiv.org/pdf/2503.19470) | veRL | PPO/GRPO/RLOO/REINFORCE++/ReMax | Single | Outcome | Multi | Tool-use/Math/QA | All | Yes |


## TextGame
| Github Repo | Date | Org | Paper Link | RL Framework |  RL Algorithm | Single/Multi Agent | Outcome/Process Reward | Single/Multi Turn | Task | Reward Type | Tool usage |
| --------- | --------- | --------- |  --------- | --------- | --------- | --------- | --------- | --------- | --------- | --------- | --------- |
| [ART](https://github.com/OpenPipe/ART) | 2025-03 | OpenPipe | [paper](https://github.com/OpenPipe/ART#-citation) | TRL | GRPO | Multi | Both | Multi | TextGame | All | Yes |
| [verl-agent](https://github.com/langfengQ/verl-agent) | 2025-05 | NTU/Skywork | [paper](https://arxiv.org/pdf/2505.10978) | veRL | PPO/GRPO/GiGPO/DAPO/RLOO/REINFORCE++ | Multi | Both | Multi | Phone Use/Math/Code/Web/TextGame | All | Yes |
| [SPA-RL-Agent](https://github.com/WangHanLinHenry/SPA-RL-Agent) | 2025-05 | PolyU | [paper](https://arxiv.org/pdf/2505.20732) | TRL | PPO | Single | Process | Multi | Navigation/Web/TextGame | Model | No |
| [Trinity-RFT](https://github.com/modelscope/Trinity-RFT) | 2025-05 | Alibaba | [paper](https://arxiv.org/pdf/2505.17826) | veRL | PPO/GRPO | Single | Outcome | Both | Math/TextGame/Web | All | Yes |
| [RAGEN](https://github.com/RAGEN-AI/RAGEN) | 2025-01 | RAGEN-AI | [paper](https://arxiv.org/pdf/2504.20073) | veRL |PPO/GRPO | Single | Both | Multi | TextGame | All | Yes |
| [VAGEN](https://github.com/RAGEN-AI/VAGEN) | 2025-03 | RAGEN-AI | [paper](https://www.notion.so/VAGEN-Training-VLM-Agents-with-Multi-Turn-Reinforcement-Learning-1bfde13afb6e80b792f6d80c7c2fcad0) | veRL | PPO/GRPO | Single | Both | Multi | TextGame/Navigation | All | Yes |
| [OpenManus-RL](https://github.com/OpenManus/OpenManus-RL) | 2025-03 | UIUC/MetaGPT | -- | Custom | PPO/DPO/GRPO | Multi | Outcome | Multi | TextGame | All | Yes |


## QA(Reasoning/Math/Code)
| Github Repo | Date | Org | Paper Link | RL Framework |  RL Algorithm | Single/Multi Agent | Outcome/Process Reward | Single/Multi Turn | Task | Reward Type | Tool usage |
| --------- | --------- | --------- |  --------- | --------- | --------- | --------- | --------- | --------- | --------- | --------- | --------- |
| [sweet_rl](https://github.com/facebookresearch/sweet_rl) | 2025-03 | Meta/UCB | [paper](https://arxiv.org/pdf/2503.15478) | OpenRLHF | DPO | Multi | Process | Multi | Design/Code | Model | Web Browsing |
| [Agentic-Reasoning](https://github.com/theworldofagents/Agentic-Reasoning) | 2025-02 | Oxford | [paper](https://arxiv.org/pdf/2502.04644) | Custom | Custom | Single | Process | Multi | QA/Math | External | Web Browsing |
| [SkyRL](https://github.com/NovaSky-AI/SkyRL) | 2025-04 | NovaSky | -- | veRL | PPO/GRPO | Single | Outcome | Multi | Math/Code | All | Code |
| [openrlhf_async_pipline](https://github.com/yyht/openrlhf_async_pipline) | 2024-05 | OpenRLHF | [paper](https://arxiv.org/pdf/2405.11143) | OpenRLHF | PPO/REINFORCE++/DPO/RLOO | Single | Outcome | Multi | Dialogue/Reasoning/QA | All | No |
| [Time-R1](https://github.com/ulab-uiuc/Time-R1) | 2025-05 | UIUC | [paper](https://arxiv.org/pdf/2505.13508) | veRL | PPO/GRPO/DPO | Multi | Outcome | Multi | Temporal | All | Code |
| [agent-distillation](https://github.com/Nardien/agent-distillation) | 2025-05 | KAIST | [paper](https://arxiv.org/pdf/2505.17612) | Custom | PPO | Single | Process | Multi | QA/Math | External | Yes |
| [VDeepEyes](https://github.com/Visual-Agent/DeepEyes) | 2025-05 | Xiaohongshu/XJTU | [paper](https://arxiv.org/pdf/2505.14362) | veRL | PPO/GRPO | Multi | Process | Multi | VQA | All | Yes |
| [ML-Agent](https://github.com/MASWorks/ML-Agent) | 2025-05 | MASWorks | [paper](https://arxiv.org/pdf/2505.23723) | Custom | Custom | Single | Process | Multi | Code | All | Yes |
| [CURE](https://github.com/Gen-Verse/CURE) | 2025-06 | University of Chicago/Princeton/ByteDance | [paper](https://arxiv.org/pdf/2506.03136) | Huggingface | PPO | Single | Outcome | Single | Code | External | No |
| [MedAgentGym](https://github.com/wshi83/MedAgentGym) | 2025-06 | Emory/Georgia Tech | [paper](https://arxiv.org/pdf/2506.04405) | Hugginface | SFT/DPO/PPO/GRPO | Single | Outcome | Multi | Medical/Code | External | Yes |
| [open-r1](https://github.com/huggingface/open-r1) | 2025-01 | HuggingFace | -- | TRL | GRPO | Single | Outcome | Single | Math/Code | All | Yes |
| [EasyR1](https://github.com/hiyouga/EasyR1) | 2025-04 | Individual | [repo1](https://github.com/hiyouga/EasyR1)/[paper2](https://arxiv.org/pdf/2409.19256) | veRL | GRPO | Single | Process | Multi | Vision-Language | Model | Yes |
| [MASLab](https://github.com/MASWorks/MASLab) | 2025-05 | MASWorks | [paper](https://arxiv.org/pdf/2505.16988) | Custom | NO RL | Multi | Outcome | Multi | Code/Math/Reasoning | External | Yes |
| [AutoCoA](https://github.com/ADaM-BJTU/AutoCoA) | 2025-03 | BJTU | [paper](https://arxiv.org/pdf/2503.06580) | veRL | GRPO | Multi | Outcome | Multi | Reasoning/Math/QA | All | Yes |
| [ToRL](https://github.com/GAIR-NLP/ToRL) | 2025-03 | SJTU | [paper](https://arxiv.org/pdf/2503.23383) | veRL | GRPO | Single | Outcome | Single | Math | Rule/External | Yes |



## Environment
| Github Repo | Date | Org | Paper Link | RL Framework |  RL Algorithm | Single/Multi Agent | Outcome/Process Reward | Single/Multi Turn | Task | Reward Type | Tool usage |
| --------- | --------- | --------- |  --------- | --------- | --------- | --------- | --------- | --------- | --------- | --------- | --------- |
| [InternBootcamp](https://github.com/InternLM/InternBootcamp) | 2025-04 | InternBootcamp | -- | Environment | -- | -- | -- | -- | Reasoning/Code/Puzzle/Algorithm/TextGame | Rule/External | yes |

