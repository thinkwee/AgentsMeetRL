# Problem: VLM agent — image obs, grounding, multi-image multi-turn issues

## Symptoms

- Image-input rollouts cost dramatically more compute / memory than
  text-only.
- Agent's grounding (clicks, bounding boxes) is wrong despite "looking"
  right.
- Multi-image multi-turn rollouts hit context-window OOM.
- Continuous-coordinate clicks are noisy.

## Patterns from the corpus

### Image observation cost reduction

> **Pixel-Reasoner** — github: `https://github.com/TIGER-AI-Lab/Pixel-Reasoner`,
> paper: `https://arxiv.org/abs/2505.15966`, Waterloo TIGER-Lab, date: 2025.5.
> Curiosity-driven GRPO with zoom/select-frame tools — agent picks the
> region.

> **Mini-o3** — github: `https://github.com/Mini-o3/Mini-o3`,
> paper: `https://arxiv.org/abs/2509.07969`, date: 2025.9. Visual search
> with image cropping.

> **Chain-of-Focus** — github: `https://github.com/xtong-zhang/Chain-of-Focus`,
> paper: `https://arxiv.org/abs/2505.15436`, date: 2025.5. AGAR (GRPO)
> with zoom-in actions.

> **DeepEyes / DeepEyesV2** —
> github: `https://github.com/Visual-Agent/DeepEyes`,
> paper: `https://arxiv.org/abs/2505.14362`, Xiaohongshu, date: 2025.5.
> Outcome RL with code-exec + web search.

### Grounding accuracy

GUI grounding is the #1 use case in the VLM corpus.

> **GTA1** — github: `https://github.com/Yan98/GTA1`,
> paper: `https://arxiv.org/abs/2507.05791`, Salesforce/ANU, date: 2025.7.
> GRPO-style click-success reward.

> **GUI-G2** — github: `https://github.com/ZJU-REAL/GUI-G2`,
> paper: `https://arxiv.org/abs/2507.15846`, ZJU, date: 2025.7. Gaussian
> reward (continuous) for click accuracy.

> **UI-AGILE** — github: `https://github.com/KDEGroup/UI-AGILE`,
> paper: `https://arxiv.org/abs/2507.22025`, Xiamen, date: 2025.7.
> GRPO with continuous rule reward.

> **InfiGUI-G1** — github: `https://github.com/InfiXAI/InfiGUI-G1`,
> paper: `https://arxiv.org/abs/2508.05731`, InfiX AI, date: 2025.8.
> AEPO algorithm.

> **gui-rcpo** — github: `https://github.com/zju-real/gui-rcpo`,
> paper: `https://arxiv.org/abs/2508.05615`, ZJU, date: 2025.8. RCPO
> with self-supervised reward.

> **SE-GUI** — github: `https://github.com/YXB-NKU/SE-GUI`,
> paper: `https://arxiv.org/abs/2505.12370`, Nankai/vivo, date: 2025.5.

### Continuous click reward (smoother gradient)

A click 5 pixels off is mostly correct; a strict {0,1} reward ignores
this. Continuous reward (Gaussian, rectified) gives smoother gradient.

> **GUI-G2** — Gaussian-based reward (above).
> **UI-AGILE** — continuous rule reward.

### Multi-image / multi-turn

> **Visual-ARFT / Visual-RFT** —
> github: `https://github.com/Liuziyu77/Visual-RFT`,
> paper: `https://arxiv.org/abs/2505.14246`, Shanghai AI Lab/SJTU, date: 2025.7.
> Multimodal agentic tool use.

> **VTool-R1** — github: `https://github.com/VTOOL-R1/vtool-r1`,
> paper: `https://arxiv.org/abs/2505.19255`, UIUC, date: 2025.5. Chart/
> table VQA with Python visual tools.

> **OpenThinkIMG** — github: `https://github.com/zhaochen0110/OpenThinkIMG`,
> paper: `https://arxiv.org/abs/2505.08617`, date: 2025.5. Chart
> reasoning with GroundingDINO/SAM/OCR/crop tools.

### Bounded thinking for visual

> **Mini-o3** — bounded thinking for visual search.
> **VisionThink** — github: `https://github.com/dvlab-research/VisionThink`,
> paper: `https://arxiv.org/abs/2507.13348`, CUHK, date: 2025.7. LLM-as-
> judge for efficient VQA.

## Common bugs

### Bug 1: image-token math doesn't match training format

VLM models (Qwen2.5-VL, Llava) use specific token patterns for images.
Mis-tokenizing images → drift, OOM, weird outputs. veRL has explicit
VLM support (image preprocessing, multimodal data flow); fork from a
VLM-tested veRL recipe rather than retrofitting a text-only one.

### Bug 2: image-coordinates absolute vs relative

> **UI-TARS** — github: `https://github.com/bytedance/UI-TARS`,
> paper: `https://arxiv.org/abs/2509.02544`, ByteDance Seed, date: 2025.1.
> Qwen2.5-VL-based models use absolute pixel coordinates, not
> normalized [0, 1]. Mixing the two silently corrupts every click
> reward.

### Bug 3: VLM rollout doesn't share VRAM efficiently

VLM with vLLM has KV cache + image cache. Memory tuning matters more
than text-only.

## Paper / repo references

(All cited above.)

**Other corpus entries:**

- `VDeepEyes` — PPO/GRPO for VQA.
  github: `https://github.com/Visual-Agent/DeepEyes`, paper: `https://arxiv.org/abs/2505.14362`, Xiaohongshu/XJTU, date: 2025.5

- `CoSo` — soft RL with counterfactual reasoning for Android/card/embodied.
  github: `https://github.com/langfengQ/CoSo`, paper: `https://arxiv.org/abs/2505.03792`, NTU/Alibaba, date: 2025.5

- `RL4VLM` — PPO on GymCards/ALFWorld — early VLM-RL baseline.
  github: `https://github.com/RL4VLM/RL4VLM`, paper: `https://arxiv.org/abs/2405.10292`, UC Berkeley, date: 2024.5

- `VSC-RL` — variational RL for mobile device control.
  github: `https://github.com/ai-agents-2030/VSC_RL`, paper: `https://arxiv.org/abs/2502.07949`, Liverpool/Huawei/Tianjin/UCL, date: 2025.2

- `AlphaDrive` — GRPO with 4-component rule reward for autonomous driving.
  github: `https://github.com/hustvl/AlphaDrive`, paper: `https://arxiv.org/abs/2503.07608`, HUST/Horizon Robotics, date: 2025.3

- `AutoVLA` — GRPO RFT after SFT for autonomous driving (nuScenes/nuPlan/Waymo).
  github: `https://github.com/ucla-mobility/AutoVLA`, paper: `https://arxiv.org/abs/2506.13757`, UCLA Mobility Lab, date: 2025.6

- `GRIT` — GRPO-GR with bbox reward for visual reasoning.
  github: `https://github.com/eric-ai-lab/GRIT`, paper: `https://arxiv.org/abs/2505.15879`, UC Santa Cruz (eric-ai-lab), date: 2025.5

- `VRAG` — GRPO for visually-rich RAG; bridges VLM + retrieval.
  github: `https://github.com/Alibaba-NLP/VRAG`, paper: `https://arxiv.org/abs/2505.22019`, USTC / Tongyi Lab, Alibaba, date: 2025.5
