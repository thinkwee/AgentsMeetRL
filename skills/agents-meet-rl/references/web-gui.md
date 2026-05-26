# Web & GUI Agents

Agents that drive browsers, mobile UIs, or desktop OSes. Grounding accuracy and long-horizon planning dominate.

_Total: 29 entries._

## Contents

ToolCUA, ClawGUI, GUI-Libra, MobileAgent, UI-TARS, MobileRL, DART-GUI, Mano-P, InfiGUI-G1, gui-rcpo, UI-AGILE, GUI-G2, MagicGUI, Grounding-R1, AgentCPM-GUI, TTI, GTA1, SE-GUI, ARPO, GUI-G1, WebAgent-R1, ZeroGUI, GUI-R1, InfiGUI-R1, UI-R1, CollabUIAgents, DigiQ, GUI-Agent-RL, WebAgent.

### ToolCUA
- `https://github.com/X-PLUG/ToolCUA` · org: Alibaba Tongyi Lab (X-PLUG) · date: 2026.5
- Paper(s): [Paper](https://arxiv.org/abs/2605.12481)
- Algorithm: Tool-Bootstrapped GUI RFT + Online Agentic RL (Tool-Efficient Path Reward) · Framework: Custom · Agent: Single · Turns: Multi · Tools: Yes (GUI actions + structured tool calls)
- Reward phase: Both · Reward type: Rule (path-efficiency)
- Task: Computer Use (OSWorld-MCP, hybrid GUI+tool)

### ClawGUI
- `https://github.com/ZJU-REAL/ClawGUI` · org: Zhejiang University (ZJU-REAL) · date: 2026.4
- Paper(s): [Paper](https://arxiv.org/abs/2604.11784)
- Algorithm: GiGPO + Process Reward Model · Framework: Custom (veRL-based) · Agent: Single · Turns: Multi · Tools: Yes (GUI + hybrid CLI-GUI + persistent memory)
- Reward phase: Both · Reward type: Rule + Model (PRM)
- Task: Mobile GUI (Android/HarmonyOS/iOS, MobileWorld)

### GUI-Libra
- `https://github.com/GUI-Libra/GUI-Libra` · org: GUI-Libra (MS-affiliated) · date: 2026.2
- Paper(s): [Paper](https://arxiv.org/abs/2602.22190)
- Algorithm: KL-regularized GRPO (Partially Verifiable RL) · Framework: Custom · Agent: Single · Turns: Multi · Tools: Yes
- Reward phase: Outcome · Reward type: Rule
- Task: GUI (AndroidWorld/WebArena/Online-Mind2Web)

### MobileAgent
- `https://github.com/X-PLUG/MobileAgent` · org: X-PLUG (TongyiQwen) · date: 2025.9
- Paper(s): [paper](https://arxiv.org/abs/2509.11543)
- Algorithm: semi-online RL · Framework: veRL · Agent: Single · Turns: Multi · Tools: Yes
- Reward phase: Both · Reward type: Rule
- Task: MobileGUI/Automation

### UI-TARS
- `https://github.com/bytedance/UI-TARS` · org: ByteDance Seed · date: 2025.1
- Paper(s): [Paper](https://arxiv.org/abs/2501.12326)
- Algorithm: Multi-turn RL · Framework: Custom · Agent: Single · Turns: Multi · Tools: Yes (GUI actions)
- Reward phase: Both · Reward type: Model
- Task: GUI (Cross-platform)

### MobileRL
- `https://github.com/THUDM/MobileRL` · org: Tsinghua / Zhipu AI (THUDM) · date: 2025.9
- Paper(s): [Paper](https://arxiv.org/abs/2509.18119)
- Algorithm: AdaGRPO (Difficulty-Adaptive) · Framework: Custom · Agent: Single · Turns: Multi · Tools: Yes (Android)
- Reward phase: Outcome · Reward type: Rule
- Task: Mobile GUI (AndroidWorld/AndroidLab)

### DART-GUI
- `https://github.com/Computer-use-agents/dart-gui` · org: Computer-use-agents · date: 2025.9
- Paper(s): [Paper](https://arxiv.org/abs/2509.23866)
- Algorithm: Decoupled GRPO · Framework: veRL · Agent: Single · Turns: Multi · Tools: Yes
- Reward phase: Outcome · Reward type: Rule
- Task: GUI (OSWorld)

### Mano-P
- `https://github.com/Mininglamp-AI/Mano-P` · org: Mininglamp AI · date: 2025.9
- Paper(s): [Paper](https://arxiv.org/abs/2509.17336)
- Algorithm: Three-stage SFT→Offline RL→Online RL · Framework: Mano-SDK · Agent: Single · Turns: Multi · Tools: Yes
- Reward phase: Both · Reward type: Rule
- Task: GUI (OSWorld)

### InfiGUI-G1
- `https://github.com/InfiXAI/InfiGUI-G1` · org: InfiX AI · date: 2025.8
- Paper(s): [Paper](https://arxiv.org/abs/2508.05731)
- Algorithm: AEPO · Framework: veRL · Agent: Single · Turns: Single · Tools: No
- Reward phase: Outcome · Reward type: Rule
- Task: GUI/Grounding

### gui-rcpo
- `https://github.com/zju-real/gui-rcpo` · org: Zhejiang University · date: 2025.8
- Paper(s): [Paper](https://arxiv.org/abs/2508.05615)
- Algorithm: RCPO · Framework: Custom · Agent: Single · Turns: Single · Tools: No
- Reward phase: Outcome · Reward type: Rule (self-supervised)
- Task: GUI Grounding

### UI-AGILE
- `https://github.com/KDEGroup/UI-AGILE` · org: Xiamen University · date: 2025.7
- Paper(s): [Paper](https://arxiv.org/abs/2507.22025)
- Algorithm: GRPO · Framework: Custom · Agent: Single · Turns: Single · Tools: No
- Reward phase: Outcome · Reward type: Rule (continuous)
- Task: GUI Grounding

### GUI-G2
- `https://github.com/ZJU-REAL/GUI-G2` · org: Zhejiang University (ZJU-REAL) · date: 2025.7
- Paper(s): [Paper](https://arxiv.org/abs/2507.15846)
- Algorithm: GRPO (Gaussian Reward) · Framework: Custom (VLM-R1) · Agent: Single · Turns: Single · Tools: No
- Reward phase: Outcome · Reward type: Rule (continuous)
- Task: GUI Grounding

### MagicGUI
- `https://github.com/MagicAgent-GUI/MagicGUI` · org: Honor (MagicAgent-GUI) · date: 2025.8
- Paper(s): [Paper](https://arxiv.org/abs/2508.03700)
- Algorithm: Reinforcement Fine-Tuning (RFT) · Framework: Custom · Agent: Single · Turns: Multi · Tools: Yes
- Reward phase: Outcome · Reward type: Model/Rule
- Task: Mobile GUI

### Grounding-R1
- `https://github.com/Yan98/Grounding-R1` · org: Salesforce · date: 2025.6
- Paper(s): [blog](https://huggingface.co/blog/HelloKKMe/grounding-r1)
- Algorithm: GRPO · Framework: trl · Agent: Single · Turns: Multi · Tools: Yes
- Reward phase: Outcome · Reward type: Model
- Task: GUI Grounding

### AgentCPM-GUI
- `https://github.com/OpenBMB/AgentCPM-GUI` · org: OpenBMB/Tsinghua/RUC · date: 2025.6
- Paper(s): [Paper](https://arxiv.org/abs/2506.01391)
- Algorithm: GRPO · Framework: Huggingface · Agent: Single · Turns: Multi · Tools: Yes
- Reward phase: Outcome · Reward type: Model
- Task: Mobile GUI

### TTI
- `https://github.com/test-time-interaction/TTI` · org: CMU · date: 2025.6
- Paper(s): [Paper](https://arxiv.org/abs/2506.07976)
- Algorithm: REINFORCE/BC · Framework: Custom · Agent: Single · Turns: Multi · Tools: Web Browsing
- Reward phase: Outcome · Reward type: External
- Task: Web

### GTA1
- `https://github.com/Yan98/GTA1` · org: Salesforce / ANU · date: 2025.7
- Paper(s): [Paper](https://arxiv.org/abs/2507.05791)
- Algorithm: GRPO-style (click-success reward) · Framework: Custom (DeepSpeed) · Agent: Single · Turns: Multi · Tools: Yes
- Reward phase: Outcome · Reward type: Rule
- Task: GUI Grounding (OSWorld/ScreenSpot-Pro)

### SE-GUI
- `https://github.com/YXB-NKU/SE-GUI` · org: Nankai University/vivo · date: 2025.5
- Paper(s): [Paper](https://arxiv.org/abs/2505.12370)
- Algorithm: GRPO · Framework: trl · Agent: Single · Turns: Single · Tools: Yes
- Reward phase: Both · Reward type: Rule
- Task: GUI Grounding

### ARPO
- `https://github.com/dvlab-research/ARPO` · org: CUHK/HKUST · date: 2025.5
- Paper(s): [Paper](https://arxiv.org/abs/2505.16282)
- Algorithm: GRPO · Framework: veRL · Agent: Single · Turns: Multi · Tools: Computer Use
- Reward phase: Outcome · Reward type: External
- Task: GUI

### GUI-G1
- `https://github.com/Yuqi-Zhou/GUI-G1` · org: RUC · date: 2025.5
- Paper(s): [Paper](https://arxiv.org/abs/2505.15810)
- Algorithm: GRPO · Framework: TRL · Agent: Single · Turns: Single · Tools: No
- Reward phase: Outcome · Reward type: Rule/External
- Task: GUI

### WebAgent-R1
- `https://github.com/weizhepei/WebAgent-R1` · org: Amazon/UVA · date: 2025.5
- Paper(s): [Paper](https://arxiv.org/abs/2505.16421)
- Algorithm: M-GRPO · Framework: Custom · Agent: Single · Turns: Multi · Tools: Yes (Web browsing)
- Reward phase: Outcome · Reward type: Rule (task success)
- Task: Web Navigation (WebArena-Lite)

### ZeroGUI
- `https://github.com/OpenGVLab/ZeroGUI` · org: Shanghai AI Lab · date: 2025.5
- Paper(s): [Paper](https://arxiv.org/abs/2505.23762)
- Algorithm: Online RL · Framework: Custom · Agent: Single · Turns: Multi · Tools: Yes (GUI actions)
- Reward phase: Outcome · Reward type: Rule
- Task: GUI Agent

### GUI-R1
- `https://github.com/ritzz-ai/GUI-R1` · org: CAS/NUS · date: 2025.4
- Paper(s): [Paper](https://arxiv.org/abs/2504.10458)
- Algorithm: GRPO · Framework: veRL · Agent: Single · Turns: Multi · Tools: No
- Reward phase: Outcome · Reward type: Rule
- Task: GUI

### InfiGUI-R1
- `https://github.com/Reallm-Labs/InfiGUI-R1` · org: Zhejiang University · date: 2025.4
- Paper(s): [Paper](https://arxiv.org/abs/2504.14239)
- Algorithm: RL + sub-goal guidance · Framework: Custom · Agent: Single · Turns: Multi · Tools: Yes
- Reward phase: Both · Reward type: Rule
- Task: GUI Reasoning

### UI-R1
- `https://github.com/lll6gg/UI-R1` · org: vivo/CUHK · date: 2025.3
- Paper(s): [Paper](https://arxiv.org/abs/2503.21620)
- Algorithm: GRPO · Framework: TRL · Agent: Single · Turns: Both · Tools: Computer/Phone Use
- Reward phase: Process · Reward type: Rule
- Task: GUI

### CollabUIAgents
- `https://github.com/THUNLP-MT/CollabUIAgents` · org: Tsinghua/Alibaba/HKUST · date: 2025.2
- Paper(s): [Paper](https://arxiv.org/abs/2502.14496)
- Algorithm: DPO (credit re-assignment) · Framework: Custom · Agent: Multi · Turns: Multi · Tools: Yes (GUI interaction)
- Reward phase: Process · Reward type: Model (LLM)
- Task: GUI (Mobile + Web)

### DigiQ
- `https://github.com/DigiRL-agent/digiq` · org: UC Berkeley/CMU/Amazon · date: 2025.2
- Paper(s): [Paper](https://arxiv.org/abs/2502.15760)
- Algorithm: Value-based offline RL · Framework: Custom · Agent: Single · Turns: Multi · Tools: Yes
- Reward phase: Outcome · Reward type: Model (Q-function)
- Task: Android Device Control

### GUI-Agent-RL
- `https://github.com/microsoft/GUI-Agent-RL` · org: Microsoft · date: 2025.2
- Paper(s): [Paper](https://arxiv.org/abs/2502.18906)
- Algorithm: Value-based RL (VEM) · Framework: Custom · Agent: Single · Turns: Multi · Tools: Yes
- Reward phase: Outcome · Reward type: Model
- Task: GUI (Web Shopping)

### WebAgent
- `https://github.com/Alibaba-NLP/WebAgent` · org: Alibaba · date: 2025.1
- Paper(s): [paper1](https://arxiv.org/abs/2501.07572), [paper2](https://arxiv.org/abs/2505.22648)
- Algorithm: DAPO · Framework: LLaMA-Factory · Agent: Multi · Turns: Multi · Tools: Yes
- Reward phase: Process · Reward type: Model
- Task: Web
