# Problem: GUI agents — screenshot diff cost, action grounding, click accuracy

## Symptoms

- Each turn requires a fresh screenshot (high data cost).
- Click reward is binary (hit/miss) which doesn't capture "close
  enough."
- Multi-platform (mobile + desktop + web) training conflicts.
- Continuous-coordinate predictions are noisy.

## Patterns from the corpus

### Continuous click reward (Gaussian / continuous rule)

Strict pixel-exact reward gives sparse gradient.

> **GUI-G2** — github: `https://github.com/ZJU-REAL/GUI-G2`,
> paper: `https://arxiv.org/abs/2507.15846`, ZJU, date: 2025.7. Gaussian
> reward for click accuracy.

> **UI-AGILE** — github: `https://github.com/KDEGroup/UI-AGILE`,
> paper: `https://arxiv.org/abs/2507.22025`, Xiamen, date: 2025.7.
> Continuous rule reward.

> **GTA1** — github: `https://github.com/Yan98/GTA1`,
> paper: `https://arxiv.org/abs/2507.05791`, Salesforce/ANU, date: 2025.7.
> Click-success reward in custom DeepSpeed setup.

### Difficulty-adaptive

Tasks have widely varying difficulty (one click vs 20-step workflow).

> **AdaGRPO** in **MobileRL** — github: `https://github.com/THUDM/MobileRL`,
> paper: `https://arxiv.org/abs/2509.18119`, THUDM, date: 2025.9.
> Difficulty-Adaptive GRPO. AndroidWorld + AndroidLab.

### Decoupled GRPO for OS-level

> **DART-GUI** — github: `https://github.com/Computer-use-agents/dart-gui`,
> paper: `https://arxiv.org/abs/2509.23866`, date: 2025.9. Decoupled
> GRPO; OSWorld.

### Self-supervised reward (no labels)

> **gui-rcpo** — github: `https://github.com/zju-real/gui-rcpo`,
> paper: `https://arxiv.org/abs/2508.05615`, ZJU, date: 2025.8. Self-
> supervised reward.

### Three-stage SFT → offline RL → online RL

> **MobileRL** — three-stage pipeline.

> **Mano-P** — github: `https://github.com/Mininglamp-AI/Mano-P`,
> paper: `https://arxiv.org/abs/2509.17336`, Mininglamp AI, date: 2025.9.
> Three-stage on OSWorld.

> **AgentCPM-GUI** — github: `https://github.com/OpenBMB/AgentCPM-GUI`,
> paper: `https://arxiv.org/abs/2506.01391`, OpenBMB/Tsinghua/RUC, date: 2025.6.
> SFT + GRPO mobile.

### Cross-platform (one model, mobile + desktop + web)

> **UI-TARS / UI-TARS-2** — github: `https://github.com/bytedance/UI-TARS`,
> papers: `https://arxiv.org/abs/2501.12326` (UI-TARS),
> `https://arxiv.org/abs/2509.02544` (UI-TARS-2), ByteDance Seed.
> Cross-platform multi-turn RL.

### Online RL on GUI

> **ZeroGUI** — github: `https://github.com/OpenGVLab/ZeroGUI`,
> paper: `https://arxiv.org/abs/2505.23762`, Shanghai AI Lab, date: 2025.5.
> Online RL.

### Sub-goal guidance for complex workflows

> **InfiGUI-R1** — github: `https://github.com/Reallm-Labs/InfiGUI-R1`,
> paper: `https://arxiv.org/abs/2504.14239`, ZJU, date: 2025.4. RL +
> sub-goal guidance for GUI reasoning.

### Partial-verifiable reward + strong KL

> **GUI-Libra** — github: `https://github.com/GUI-Libra/GUI-Libra`,
> paper: `https://arxiv.org/abs/2602.22190`, date: 2026.2. KL-regularized
> GRPO for partial-verifiable RL on AndroidWorld/WebArena/Online-Mind2Web.

### M-GRPO for web agents

> **WebAgent-R1** — github: `https://github.com/weizhepei/WebAgent-R1`,
> paper: `https://arxiv.org/abs/2505.16421`, Amazon/UVA, date: 2025.5.
> M-GRPO for web navigation (WebArena-Lite).

### Value-based offline RL

> **DigiQ** — github: `https://github.com/DigiRL-agent/digiq`,
> paper: `https://arxiv.org/abs/2502.15760`, UCB/CMU/Amazon, date: 2025.2.
> Value-based offline RL for Android device control.

> **GUI-Agent-RL (VEM)** — github: `https://github.com/microsoft/GUI-Agent-RL`,
> paper: `https://arxiv.org/abs/2502.18906`, Microsoft, date: 2025.2.
> Value-based RL.

### Test-time interaction (TTI)

> **TTI** — github: `https://github.com/test-time-interaction/TTI`,
> paper: `https://arxiv.org/abs/2506.07976`, CMU, date: 2025.6.
> REINFORCE/BC web browsing.

### Coordinate handling gotcha

> **UI-TARS** — github: `https://github.com/bytedance/UI-TARS`,
> paper: `https://arxiv.org/abs/2509.02544`, ByteDance Seed, date: 2025.1.
> Qwen2.5-VL-based models use absolute (not normalized) pixel
> coordinates; mixing the two conventions silently corrupts every click
> reward. UI-TARS's documentation pins the convention explicitly.

## Common bugs

### Bug 1: Screenshot tokenization changes between rollout and train

VLM tokenization of images is brittle. See `vlm-specific.md`.

### Bug 2: Action parser fails on slight format variations

GUI actions look like `click(x, y)` but training data may have
`Action: click(start_box='(100, 200)')`. Use UI-TARS's robust
`ui_tars.action_parser` library.

### Bug 3: env determinism

A click at the wrong moment hits a different element (network latency,
async UI). Seed/wait for stable state.

## Paper / repo references

(All cited above.)

**Other corpus entries:**

- `MobileAgent` — semi-online RL for mobile GUI automation.
  github: `https://github.com/X-PLUG/MobileAgent`, paper: `https://arxiv.org/abs/2509.11543`, X-PLUG (TongyiQwen), date: 2025.9

- `Grounding-R1` — GRPO with model reward for GUI grounding.
  github: `https://github.com/Yan98/Grounding-R1`, paper: `https://huggingface.co/blog/HelloKKMe/grounding-r1`, Salesforce, date: 2025.6

- `GUI-G1` — GRPO single-turn GUI.
  github: `https://github.com/Yuqi-Zhou/GUI-G1`, paper: `https://arxiv.org/abs/2505.15810`, RUC, date: 2025.5

- `GUI-R1` — GRPO multi-turn GUI.
  github: `https://github.com/ritzz-ai/GUI-R1`, paper: `https://arxiv.org/abs/2504.10458`, CAS/NUS, date: 2025.4

- `UI-R1` — GRPO single+multi-turn GUI.
  github: `https://github.com/lll6gg/UI-R1`, paper: `https://arxiv.org/abs/2503.21620`, vivo/CUHK, date: 2025.3

- `CollabUIAgents` — DPO with credit re-assignment for mobile/web GUI.
  github: `https://github.com/THUNLP-MT/CollabUIAgents`, paper: `https://arxiv.org/abs/2502.14496`, Tsinghua/Alibaba/HKUST, date: 2025.2

- `SEAgent` — GRPO with model reward on OSWorld computer-use.
  github: `https://github.com/SunzeY/SEAgent`, paper: `https://arxiv.org/abs/2508.04700`, Shanghai AI Lab / CUHK, date: 2025.8
