# VLM Agents

Vision-language model agents (visual tool-use, chart QA, autonomous driving, image-based search).

_Total: 27 entries._

## Contents

HyperEyes, ODE, ParaVT, OpenSearch-VL, MTA-Agent, Gen-Searcher, MM-DeepResearch, PyVision-RL, Vision-DeepResearch, ARM-Thinker, CodeDance, DeepEyesV2, Mini-o3, VisionThink, multimodal-search-r1, AutoVLA, VDeepEyes, CoSo, Pixel-Reasoner, Visual-ARFT, VTool-R1, OpenThinkIMG, Chain-of-Focus, GRIT, AlphaDrive, VSC-RL, RL4VLM.

### HyperEyes
- **Idea:** Fuses visual grounding and retrieval into one Unified Grounded Search action and searches multiple entities concurrently, training inference efficiency as an objective.
- `https://github.com/DeepExperience/HyperEyes` · org: DeepExperience · date: 2026.5
- Paper(s): [Paper](https://arxiv.org/abs/2605.07177)
- Algorithm: Dual-grained efficiency-aware RL · Framework: Custom · Agent: Single · Turns: Multi · Tools: Yes (visual grounding + retrieval)
- Reward phase: Both · Reward type: Custom + Rule
- Task: Parallel multimodal search (unified grounded search)

### ODE
- **Idea:** On-policy data evolution over a 9-tool visual-native harness (visual search, zoom, code) with an image-bank memory for multimodal deep search.
- `https://github.com/JoeYing1019/ODE` · org: HKUST / CUHK / PKU · date: 2026.5
- Paper(s): [Paper](https://arxiv.org/abs/2605.10832)
- Algorithm: GRPO (async) + SFT cold-start · Framework: verl + rllm · Agent: Single · Turns: Multi · Tools: Yes (web/image/visual search, code)
- Reward phase: Both · Reward type: External + Rule
- Task: Visual-native multimodal deep search (9-tool harness)

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

### Gen-Searcher
- **Idea:** Reinforces multi-hop web + visual-reference search before grounded image synthesis, with dual text and image rewards.
- `https://github.com/tulerfeng/Gen-Searcher` · org: Academic · date: 2026.3
- Paper(s): [Paper](https://arxiv.org/abs/2603.28767)
- Algorithm: GRPO (after SFT) · Framework: rllm + verl · Agent: Single · Turns: Multi · Tools: Yes (search, image search, browse, image-gen)
- Reward phase: Both · Reward type: Model (dual text+image)
- Task: Search-augmented image-generation deep research

### MM-DeepResearch
- **Idea:** A simple multimodal agentic-search baseline that learns when/how to call image-to-image, text-to-image, and text-to-text retrieval engines via GRPO.
- `https://github.com/HJYao00/MM-DeepResearch` · org: Academic · date: 2026.3
- Paper(s): [Paper](https://arxiv.org/abs/2603.01050)
- Algorithm: Multi-turn agentic GRPO · Framework: veRL · Agent: Single · Turns: Multi · Tools: Yes (image/text search engines)
- Reward phase: Both · Reward type: Model (judge) + Rule
- Task: Multimodal agentic search baseline

### PyVision-RL
- **Idea:** Writes Python-as-tool on the fly for agentic image and video understanding, with an accumulative per-turn tool reward to prevent interaction collapse.
- `https://github.com/agents-x-project/PyVision-RL` · org: agents-x-project · date: 2026.2
- Paper(s): [Paper](https://arxiv.org/abs/2602.20739)
- Algorithm: GRPO · Framework: veRL · Agent: Single · Turns: Multi · Tools: Yes (Python-as-tool, frame sampling)
- Reward phase: Both · Reward type: External + Custom
- Task: Agentic image+video understanding w/ dynamic Python tooling

### Vision-DeepResearch
- **Idea:** Incentivizes long-horizon multimodal deep research (dozens of turns, hundreds of searches) in an MLLM via cold-start SFT then GRPO.
- `https://github.com/Osilly/Vision-DeepResearch` · org: Academic (ICML 2026) · date: 2026.1
- Paper(s): [Paper](https://arxiv.org/abs/2601.22060)
- Algorithm: GRPO (after cold-start SFT) · Framework: rllm + verl · Agent: Single · Turns: Multi · Tools: Yes (visual+textual search, browse)
- Reward phase: Both · Reward type: External + Rule
- Task: Multimodal deep-research MLLM (dozens of turns)

### ARM-Thinker
- **Idea:** A multimodal generative reward model that thinks, acts (zoom/crop, doc retrieval, validators), and verifies in an iterative loop, trained with two-stage GRPO.
- `https://github.com/InternLM/ARM-Thinker` · org: Shanghai AI Lab / InternLM · date: 2025.12
- Paper(s): [Paper](https://arxiv.org/abs/2512.05111)
- Algorithm: GRPO (two-stage) · Framework: veRL · Agent: Single · Turns: Multi · Tools: Yes (zoom/crop, doc retrieval, validators)
- Reward phase: Both · Reward type: External + Rule
- Task: Agentic multimodal reward modeling (Think-Act-Verify)

### CodeDance
- **Idea:** A dynamic tool-integrated MLLM that composes code-as-tools (crop, draw, count, plot) over multiple turns for executable visual reasoning, with a balanced adaptive tool-call reward.
- `https://github.com/CodeDance-VL/CodeDance` · org: ByteDance · date: 2025.12
- Paper(s): [Paper](https://arxiv.org/abs/2512.17312)
- Algorithm: GRPO/DAPO (agent-loop) · Framework: veRL · Agent: Single · Turns: Multi · Tools: Yes (Python sandbox: crop/draw/plot)
- Reward phase: Both · Reward type: External + Custom
- Task: Executable visual reasoning (visual search/math/chart via code)

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
