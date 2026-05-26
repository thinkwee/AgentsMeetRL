# VLM Agents

Vision-language model agents (visual tool-use, chart QA, autonomous driving, image-based search).

_Total: 19 entries._

## Contents

ParaVT, OpenSearch-VL, MTA-Agent, DeepEyesV2, Mini-o3, VisionThink, multimodal-search-r1, AutoVLA, VDeepEyes, CoSo, Pixel-Reasoner, Visual-ARFT, VTool-R1, OpenThinkIMG, Chain-of-Focus, GRIT, AlphaDrive, VSC-RL, RL4VLM.

### ParaVT
- **Idea:** PARA-GRPO for long-video agents: targeted format reward at fragile structural tokens plus frame-budget randomization to stop tool-prior-induced format collapse.
- `https://github.com/EvolvingLMMs-Lab/ParaVT` · org: NTU / HKU / Tsinghua / MiroMind (LMMs-Lab) · date: 2026.5
- Paper(s): [Paper](https://arxiv.org/abs/2605.20342)
- Algorithm: PARA-GRPO (Parseability-Anchored, Ratio-gAted) · Framework: AReaL · Agent: Multi (main + parallel sub-agents w/ shared weights) · Turns: Single-turn parallel · Tools: Yes (parallel video-window crop tools)
- Reward phase: Both (outcome + targeted format) · Reward type: Rule + Model
- Task: Long-video understanding (VideoMME/LongVideoBench/LVBench/MLVU/MMVU/Charades-STA)

### OpenSearch-VL
- **Idea:** Multi-turn fatal-aware GRPO masks post-tool-failure tokens while keeping pre-failure reasoning via one-sided advantage clamping for multimodal deep search.
- `https://github.com/shawn0728/OpenSearch-VL` · org: CUHK / NTU / HKU / Multi-institution · date: 2026.5
- Paper(s): [Paper](https://arxiv.org/abs/2605.05185)
- Algorithm: Multi-turn fatal-aware GRPO · Framework: rLLM/veRL/Megatron-LM · Agent: Single · Turns: Multi · Tools: Yes (text/image search, OCR, crop, sharpen, SR, perspective)
- Reward phase: Outcome · Reward type: Rule + Model (LLM judge)
- Task: Multimodal Deep Search (Qwen3-VL base)

### MTA-Agent
- **Idea:** DAPO trained by replaying cached tool interactions (no live API calls) on 21K multi-hop data, deepening multimodal search reasoning from 2.27 to 4.28 steps.
- `https://github.com/SalesforceAIResearch/MTA-Agent` · org: Salesforce AI Research · date: 2026.4
- Paper(s): [Paper](https://arxiv.org/abs/2604.06376)
- Algorithm: DAPO (w/ cached tool interactions) · Framework: Custom · Agent: Single · Turns: Multi · Tools: Yes (web search, web read, Google Lens, image search)
- Reward phase: Outcome · Reward type: Rule/External
- Task: Multimodal Deep Search (21K MTA-Vision-DeepSearch; 32B beats GPT-5 54.63%)

### DeepEyesV2
- **Idea:** Shows direct RL alone fails to induce robust tool use; needs cold-start then RL to get task-adaptive tool invocation (image ops for perception, code for math).
- `https://github.com/Visual-Agent/DeepEyesV2` · org: Xiaohongshu · date: 2025.11
- Paper(s): [Paper](https://arxiv.org/abs/2511.05271)
- Algorithm: Outcome RL · Framework: Custom · Agent: Single · Turns: Multi · Tools: Yes (Code exec, Web search)
- Reward phase: Outcome · Reward type: Rule
- Task: Multimodal Reasoning

### Mini-o3
- **Idea:** Over-turn masking avoids penalizing responses that hit the turn cap during GRPO, letting models trained on ~6 turns scale to tens of turns of visual search at inference.
- `https://github.com/Mini-o3/Mini-o3` · org: Mini-o3 team · date: 2025.9
- Paper(s): [Paper](https://arxiv.org/abs/2509.07969)
- Algorithm: GRPO · Framework: veRL · Agent: Single · Turns: Multi · Tools: Yes (image crop)
- Reward phase: Outcome · Reward type: Rule
- Task: Visual Search (V*/HR-Bench)

### VisionThink
- **Idea:** Model starts at low resolution and emits a special token to request a high-res image only when needed; RL with LLM-as-Judge trains this adaptive token-compression behavior.
- `https://github.com/dvlab-research/VisionThink` · org: CUHK (dvlab-research) · date: 2025.7
- Paper(s): [Paper](https://arxiv.org/abs/2507.13348)
- Algorithm: GRPO w/ LLM-as-Judge · Framework: veRL + EasyR1 · Agent: Single · Turns: Multi · Tools: Yes (hi-res request)
- Reward phase: Outcome · Reward type: Model (LLM-Judge)
- Task: Efficient VQA

### multimodal-search-r1
- **Idea:** First end-to-end RL (GRPO) teaching LMMs on-demand multi-turn image+text search, with search penalty and search-balanced data cutting calls >30%.
- `https://github.com/EvolvingLMMs-Lab/multimodal-search-r1` · org: ByteDance/NTU · date: 2025.6
- Paper(s): [Paper](https://arxiv.org/abs/2506.20670)
- Algorithm: GRPO · Framework: Custom · Agent: Single · Turns: Multi · Tools: Yes (Search)
- Reward phase: Outcome · Reward type: Rule
- Task: Multimodal Search

### AutoVLA
- **Idea:** Unifies reasoning and action in one autoregressive model by tokenizing trajectories into discrete actions, then uses GRPO RFT to drop unnecessary reasoning in easy driving scenes.
- `https://github.com/ucla-mobility/AutoVLA` · org: UCLA Mobility Lab · date: 2025.6
- Paper(s): [Paper](https://arxiv.org/abs/2506.13757)
- Algorithm: GRPO (RFT after SFT) · Framework: Custom · Agent: Single · Turns: Multi · Tools: No
- Reward phase: Outcome · Reward type: Rule (PDMS)
- Task: Autonomous Driving (nuScenes/nuPlan/Waymo)

### VDeepEyes
- **Idea:** RL trains a VLM to use its own grounding as an intrinsic tool, deciding when/where to zoom into images for active perception, with no SFT cold-start or external APIs.
- `https://github.com/Visual-Agent/DeepEyes` · org: Xiaohongshu/XJTU · date: 2025.5
- Paper(s): [Paper](https://arxiv.org/abs/2505.14362)
- Algorithm: PPO/GRPO · Framework: veRL · Agent: Multi · Turns: Multi · Tools: Yes
- Reward phase: Process · Reward type: All
- Task: VQA

### CoSo
- **Idea:** Counterfactual soft RL uses causal influence of each token on the post-processed action to focus exploration on action-critical tokens and suppress redundant ones.
- `https://github.com/langfengQ/CoSo` · org: NTU/Alibaba · date: 2025.5
- Paper(s): [Paper](https://arxiv.org/abs/2505.03792)
- Algorithm: Soft RL (counterfactual) · Framework: Custom · Agent: Single · Turns: Multi · Tools: Yes
- Reward phase: Outcome · Reward type: Rule
- Task: Android/Card/Embodied

### Pixel-Reasoner
- **Idea:** Adds pixel-space operations (zoom-in, select-frame) to VLM reasoning, using a curiosity-driven reward to balance exploring these visual ops against text reasoning.
- `https://github.com/TIGER-AI-Lab/Pixel-Reasoner` · org: University of Waterloo (TIGER-AI-Lab) · date: 2025.5
- Paper(s): [Paper](https://arxiv.org/abs/2505.15966)
- Algorithm: Curiosity-driven GRPO · Framework: OpenRLHF · Agent: Single · Turns: Multi · Tools: Yes (zoom/select-frame)
- Reward phase: Both · Reward type: Rule + Model
- Task: Visual Reasoning (V*/TallyQA/Info-VQA)

### Visual-ARFT
- **Idea:** Agentic RFT teaches LVLMs multimodal tool use, browsing the web and writing code to manipulate input images for adaptive multi-step reasoning.
- `https://github.com/Liuziyu77/Visual-RFT` · org: Shanghai AI Lab / SJTU · date: 2025.5
- Paper(s): [Paper](https://arxiv.org/abs/2505.14246)
- Algorithm: GRPO (agentic RFT) · Framework: Custom · Agent: Single · Turns: Multi · Tools: Yes (Search/Python)
- Reward phase: Outcome · Reward type: Rule
- Task: Multimodal Agentic Tool Use (MAT-Search/Coding)

### VTool-R1
- **Idea:** Integrates Python visual-editing tools into RFT so VLMs learn when/how to insert visual steps in multimodal CoT, trained with outcome-only rewards (no process supervision).
- `https://github.com/VTOOL-R1/vtool-r1` · org: UIUC · date: 2025.5
- Paper(s): [Paper](https://arxiv.org/abs/2505.19255)
- Algorithm: RFT (GRPO-based) · Framework: veRL + EasyR1 · Agent: Single · Turns: Multi · Tools: Yes (Python visual tools)
- Reward phase: Outcome · Reward type: Rule
- Task: Chart/Table VQA

### OpenThinkIMG
- **Idea:** V-ToolRL lets LVLMs discover tool-use strategies by directly optimizing task success from tool-interaction feedback, packaged in an open framework with standardized vision-tool interfaces.
- `https://github.com/zhaochen0110/OpenThinkIMG` · org: Academic (zhaochen0110) · date: 2025.5
- Paper(s): [Paper](https://arxiv.org/abs/2505.08617)
- Algorithm: V-ToolRL (GRPO) · Framework: OpenR1 · Agent: Single · Turns: Multi · Tools: Yes (GroundingDINO/SAM/OCR/crop)
- Reward phase: Outcome · Reward type: Rule
- Task: Chart Reasoning

### Chain-of-Focus
- **Idea:** Two-stage SFT-then-RL pipeline trains a VLM to iteratively zoom into key image regions, using only answer accuracy and format as outcome rewards.
- `https://github.com/xtong-zhang/Chain-of-Focus` · org: Multi-institution · date: 2025.5
- Paper(s): [Paper](https://arxiv.org/abs/2505.15436)
- Algorithm: AGAR (GRPO) · Framework: veRL · Agent: Single · Turns: Multi · Tools: Yes (zoom-in)
- Reward phase: Outcome · Reward type: Rule (outcome+format)
- Task: Visual Reasoning (V*)

### GRIT
- **Idea:** Grounded reasoning interleaves natural language with explicit bbox coordinates; GRPO-GR trains it from only answer-accuracy and format rewards, no reasoning-chain or bbox labels.
- `https://github.com/eric-ai-lab/GRIT` · org: UC Santa Cruz (eric-ai-lab) · date: 2025.5
- Paper(s): [Paper](https://arxiv.org/abs/2505.15879)
- Algorithm: GRPO-GR (Grounded Reasoning) · Framework: trl · Agent: Single · Turns: Single · Tools: Yes (bbox)
- Reward phase: Outcome · Reward type: Rule
- Task: Visual Reasoning (bbox)

### AlphaDrive
- **Idea:** Brings GRPO to driving planning with four planning-tailored rewards plus a two-stage SFT-then-RL recipe, yielding emergent multimodal planning behaviors.
- `https://github.com/hustvl/AlphaDrive` · org: HUST/Horizon Robotics · date: 2025.3
- Paper(s): [Paper](https://arxiv.org/abs/2503.07608)
- Algorithm: GRPO · Framework: Custom · Agent: Single · Turns: Multi · Tools: No
- Reward phase: Outcome · Reward type: Rule (4 planning rewards)
- Task: Autonomous Driving

### VSC-RL
- **Idea:** Recasts VLM agent control as variational subgoal-conditioned RL via an SGC-ELBO objective that maximizes subgoal return while staying near a reference goal policy for sparse long-horizon tasks.
- `https://github.com/ai-agents-2030/VSC_RL` · org: Liverpool/Huawei/Tianjin/UCL · date: 2025.2
- Paper(s): [Paper](https://arxiv.org/abs/2502.07949)
- Algorithm: Variational RL · Framework: Custom · Agent: Single · Turns: Multi · Tools: Yes
- Reward phase: Outcome · Reward type: Rule
- Task: Mobile Device Control

### RL4VLM
- **Idea:** Fine-tunes a whole VLM with PPO by prompting CoT reasoning, parsing the text into executable actions, and using environment task rewards as the RL signal.
- `https://github.com/RL4VLM/RL4VLM` · org: UC Berkeley · date: 2024.5
- Paper(s): [Paper](https://arxiv.org/abs/2405.10292)
- Algorithm: PPO · Framework: Custom · Agent: Single · Turns: Multi · Tools: Yes
- Reward phase: Outcome · Reward type: Rule
- Task: GymCards/ALFWorld
