# VLM Agents

Vision-language model agents (visual tool-use, chart QA, autonomous driving, image-based search).

_Total: 19 entries._

## Contents

ParaVT, OpenSearch-VL, MTA-Agent, DeepEyesV2, Mini-o3, VisionThink, multimodal-search-r1, AutoVLA, VDeepEyes, CoSo, Pixel-Reasoner, Visual-ARFT, VTool-R1, OpenThinkIMG, Chain-of-Focus, GRIT, AlphaDrive, VSC-RL, RL4VLM.

### ParaVT
- `https://github.com/EvolvingLMMs-Lab/ParaVT` · org: NTU / HKU / Tsinghua / MiroMind (LMMs-Lab) · date: 2026.5
- Paper(s): [Paper](https://arxiv.org/abs/2605.20342)
- Algorithm: PARA-GRPO (Parseability-Anchored, Ratio-gAted) · Framework: AReaL · Agent: Multi (main + parallel sub-agents w/ shared weights) · Turns: Single-turn parallel · Tools: Yes (parallel video-window crop tools)
- Reward phase: Both (outcome + targeted format) · Reward type: Rule + Model
- Task: Long-video understanding (VideoMME/LongVideoBench/LVBench/MLVU/MMVU/Charades-STA)

### OpenSearch-VL
- `https://github.com/shawn0728/OpenSearch-VL` · org: CUHK / NTU / HKU / Multi-institution · date: 2026.5
- Paper(s): [Paper](https://arxiv.org/abs/2605.05185)
- Algorithm: Multi-turn fatal-aware GRPO · Framework: rLLM/veRL/Megatron-LM · Agent: Single · Turns: Multi · Tools: Yes (text/image search, OCR, crop, sharpen, SR, perspective)
- Reward phase: Outcome · Reward type: Rule + Model (LLM judge)
- Task: Multimodal Deep Search (Qwen3-VL base)

### MTA-Agent
- `https://github.com/SalesforceAIResearch/MTA-Agent` · org: Salesforce AI Research · date: 2026.4
- Paper(s): [Paper](https://arxiv.org/abs/2604.06376)
- Algorithm: DAPO (w/ cached tool interactions) · Framework: Custom · Agent: Single · Turns: Multi · Tools: Yes (web search, web read, Google Lens, image search)
- Reward phase: Outcome · Reward type: Rule/External
- Task: Multimodal Deep Search (21K MTA-Vision-DeepSearch; 32B beats GPT-5 54.63%)

### DeepEyesV2
- `https://github.com/Visual-Agent/DeepEyesV2` · org: Xiaohongshu · date: 2025.11
- Paper(s): [Paper](https://arxiv.org/abs/2511.05271)
- Algorithm: Outcome RL · Framework: Custom · Agent: Single · Turns: Multi · Tools: Yes (Code exec, Web search)
- Reward phase: Outcome · Reward type: Rule
- Task: Multimodal Reasoning

### Mini-o3
- `https://github.com/Mini-o3/Mini-o3` · org: Mini-o3 team · date: 2025.9
- Paper(s): [Paper](https://arxiv.org/abs/2509.07969)
- Algorithm: GRPO · Framework: veRL · Agent: Single · Turns: Multi · Tools: Yes (image crop)
- Reward phase: Outcome · Reward type: Rule
- Task: Visual Search (V*/HR-Bench)

### VisionThink
- `https://github.com/dvlab-research/VisionThink` · org: CUHK (dvlab-research) · date: 2025.7
- Paper(s): [Paper](https://arxiv.org/abs/2507.13348)
- Algorithm: GRPO w/ LLM-as-Judge · Framework: veRL + EasyR1 · Agent: Single · Turns: Multi · Tools: Yes (hi-res request)
- Reward phase: Outcome · Reward type: Model (LLM-Judge)
- Task: Efficient VQA

### multimodal-search-r1
- `https://github.com/EvolvingLMMs-Lab/multimodal-search-r1` · org: ByteDance/NTU · date: 2025.6
- Paper(s): [Paper](https://arxiv.org/abs/2506.20670)
- Algorithm: GRPO · Framework: Custom · Agent: Single · Turns: Multi · Tools: Yes (Search)
- Reward phase: Outcome · Reward type: Rule
- Task: Multimodal Search

### AutoVLA
- `https://github.com/ucla-mobility/AutoVLA` · org: UCLA Mobility Lab · date: 2025.6
- Paper(s): [Paper](https://arxiv.org/abs/2506.13757)
- Algorithm: GRPO (RFT after SFT) · Framework: Custom · Agent: Single · Turns: Multi · Tools: No
- Reward phase: Outcome · Reward type: Rule (PDMS)
- Task: Autonomous Driving (nuScenes/nuPlan/Waymo)

### VDeepEyes
- `https://github.com/Visual-Agent/DeepEyes` · org: Xiaohongshu/XJTU · date: 2025.5
- Paper(s): [Paper](https://arxiv.org/abs/2505.14362)
- Algorithm: PPO/GRPO · Framework: veRL · Agent: Multi · Turns: Multi · Tools: Yes
- Reward phase: Process · Reward type: All
- Task: VQA

### CoSo
- `https://github.com/langfengQ/CoSo` · org: NTU/Alibaba · date: 2025.5
- Paper(s): [Paper](https://arxiv.org/abs/2505.03792)
- Algorithm: Soft RL (counterfactual) · Framework: Custom · Agent: Single · Turns: Multi · Tools: Yes
- Reward phase: Outcome · Reward type: Rule
- Task: Android/Card/Embodied

### Pixel-Reasoner
- `https://github.com/TIGER-AI-Lab/Pixel-Reasoner` · org: University of Waterloo (TIGER-AI-Lab) · date: 2025.5
- Paper(s): [Paper](https://arxiv.org/abs/2505.15966)
- Algorithm: Curiosity-driven GRPO · Framework: OpenRLHF · Agent: Single · Turns: Multi · Tools: Yes (zoom/select-frame)
- Reward phase: Both · Reward type: Rule + Model
- Task: Visual Reasoning (V*/TallyQA/Info-VQA)

### Visual-ARFT
- `https://github.com/Liuziyu77/Visual-RFT` · org: Shanghai AI Lab / SJTU · date: 2025.5
- Paper(s): [Paper](https://arxiv.org/abs/2505.14246)
- Algorithm: GRPO (agentic RFT) · Framework: Custom · Agent: Single · Turns: Multi · Tools: Yes (Search/Python)
- Reward phase: Outcome · Reward type: Rule
- Task: Multimodal Agentic Tool Use (MAT-Search/Coding)

### VTool-R1
- `https://github.com/VTOOL-R1/vtool-r1` · org: UIUC · date: 2025.5
- Paper(s): [Paper](https://arxiv.org/abs/2505.19255)
- Algorithm: RFT (GRPO-based) · Framework: veRL + EasyR1 · Agent: Single · Turns: Multi · Tools: Yes (Python visual tools)
- Reward phase: Outcome · Reward type: Rule
- Task: Chart/Table VQA

### OpenThinkIMG
- `https://github.com/zhaochen0110/OpenThinkIMG` · org: Academic (zhaochen0110) · date: 2025.5
- Paper(s): [Paper](https://arxiv.org/abs/2505.08617)
- Algorithm: V-ToolRL (GRPO) · Framework: OpenR1 · Agent: Single · Turns: Multi · Tools: Yes (GroundingDINO/SAM/OCR/crop)
- Reward phase: Outcome · Reward type: Rule
- Task: Chart Reasoning

### Chain-of-Focus
- `https://github.com/xtong-zhang/Chain-of-Focus` · org: Multi-institution · date: 2025.5
- Paper(s): [Paper](https://arxiv.org/abs/2505.15436)
- Algorithm: AGAR (GRPO) · Framework: veRL · Agent: Single · Turns: Multi · Tools: Yes (zoom-in)
- Reward phase: Outcome · Reward type: Rule (outcome+format)
- Task: Visual Reasoning (V*)

### GRIT
- `https://github.com/eric-ai-lab/GRIT` · org: UC Santa Cruz (eric-ai-lab) · date: 2025.5
- Paper(s): [Paper](https://arxiv.org/abs/2505.15879)
- Algorithm: GRPO-GR (Grounded Reasoning) · Framework: trl · Agent: Single · Turns: Single · Tools: Yes (bbox)
- Reward phase: Outcome · Reward type: Rule
- Task: Visual Reasoning (bbox)

### AlphaDrive
- `https://github.com/hustvl/AlphaDrive` · org: HUST/Horizon Robotics · date: 2025.3
- Paper(s): [Paper](https://arxiv.org/abs/2503.07608)
- Algorithm: GRPO · Framework: Custom · Agent: Single · Turns: Multi · Tools: No
- Reward phase: Outcome · Reward type: Rule (4 planning rewards)
- Task: Autonomous Driving

### VSC-RL
- `https://github.com/ai-agents-2030/VSC_RL` · org: Liverpool/Huawei/Tianjin/UCL · date: 2025.2
- Paper(s): [Paper](https://arxiv.org/abs/2502.07949)
- Algorithm: Variational RL · Framework: Custom · Agent: Single · Turns: Multi · Tools: Yes
- Reward phase: Outcome · Reward type: Rule
- Task: Mobile Device Control

### RL4VLM
- `https://github.com/RL4VLM/RL4VLM` · org: UC Berkeley · date: 2024.5
- Paper(s): [Paper](https://arxiv.org/abs/2405.10292)
- Algorithm: PPO · Framework: Custom · Agent: Single · Turns: Multi · Tools: Yes
- Reward phase: Outcome · Reward type: Rule
- Task: GymCards/ALFWorld
