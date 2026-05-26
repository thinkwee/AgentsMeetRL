# Web & GUI Agents

Agents that drive browsers, mobile UIs, or desktop OSes. Grounding accuracy and long-horizon planning dominate.

_Total: 29 entries._

## Contents

ToolCUA, ClawGUI, GUI-Libra, MobileAgent, UI-TARS, MobileRL, DART-GUI, Mano-P, InfiGUI-G1, gui-rcpo, UI-AGILE, GUI-G2, MagicGUI, Grounding-R1, AgentCPM-GUI, TTI, GTA1, SE-GUI, ARPO, GUI-G1, WebAgent-R1, ZeroGUI, GUI-R1, InfiGUI-R1, UI-R1, CollabUIAgents, DigiQ, GUI-Agent-RL, WebAgent.

### ToolCUA
- **Idea:** Staged GUI+tool training: synthesized interleaved trajectories, tool-bootstrapped RFT warmup, then online RL with a Tool-Efficient Path Reward for when to switch GUI vs tool calls.
- `https://github.com/X-PLUG/ToolCUA` · org: Alibaba Tongyi Lab (X-PLUG) · date: 2026.5
- Paper(s): [Paper](https://arxiv.org/abs/2605.12481)
- Algorithm: Tool-Bootstrapped GUI RFT + Online Agentic RL (Tool-Efficient Path Reward) · Framework: Custom · Agent: Single · Turns: Multi · Tools: Yes (GUI actions + structured tool calls)
- Reward phase: Both · Reward type: Rule (path-efficiency)
- Task: Computer Use (OSWorld-MCP, hybrid GUI+tool)

### ClawGUI
- **Idea:** Combines GiGPO with a Process Reward Model for dense step-level supervision to stabilize mobile-GUI agent RL against environment instability.
- `https://github.com/ZJU-REAL/ClawGUI` · org: Zhejiang University (ZJU-REAL) · date: 2026.4
- Paper(s): [Paper](https://arxiv.org/abs/2604.11784)
- Algorithm: GiGPO + Process Reward Model · Framework: Custom (veRL-based) · Agent: Single · Turns: Multi · Tools: Yes (GUI + hybrid CLI-GUI + persistent memory)
- Reward phase: Both · Reward type: Rule + Model (PRM)
- Task: Mobile GUI (Android/HarmonyOS/iOS, MobileWorld)

### GUI-Libra
- **Idea:** Action-aware SFT plus partially-verifiable KL-trust-region GRPO to handle GUI states where multiple actions are correct but only one is demonstrated.
- `https://github.com/GUI-Libra/GUI-Libra` · org: GUI-Libra (MS-affiliated) · date: 2026.2
- Paper(s): [Paper](https://arxiv.org/abs/2602.22190)
- Algorithm: KL-regularized GRPO (Partially Verifiable RL) · Framework: Custom · Agent: Single · Turns: Multi · Tools: Yes
- Reward phase: Outcome · Reward type: Rule
- Task: GUI (AndroidWorld/WebArena/Online-Mind2Web)

### MobileAgent
- **Idea:** Semi-online RL simulates online training on offline trajectories via a Patch Module that corrects rollout-vs-expert divergence, plus discounted future returns for episode-level signal.
- `https://github.com/X-PLUG/MobileAgent` · org: X-PLUG (TongyiQwen) · date: 2025.9
- Paper(s): [paper](https://arxiv.org/abs/2509.11543)
- Algorithm: semi-online RL · Framework: veRL · Agent: Single · Turns: Multi · Tools: Yes
- Reward phase: Both · Reward type: Rule
- Task: MobileGUI/Automation

### UI-TARS
- **Idea:** Native cross-platform GUI agent bootstrapped by iteratively collecting, filtering, and reflectively refining online traces on hundreds of VMs, with System-2 reasoning.
- `https://github.com/bytedance/UI-TARS` · org: ByteDance Seed · date: 2025.1
- Paper(s): [Paper](https://arxiv.org/abs/2501.12326)
- Algorithm: Multi-turn RL · Framework: Custom · Agent: Single · Turns: Multi · Tools: Yes (GUI actions)
- Reward phase: Both · Reward type: Model
- Task: GUI (Cross-platform)

### MobileRL
- **Idea:** AdaGRPO with difficulty-adaptive positive replay, failure curriculum filtering, and shortest-path reward reshaping to stabilize multi-turn mobile GUI RL.
- `https://github.com/THUDM/MobileRL` · org: Tsinghua / Zhipu AI (THUDM) · date: 2025.9
- Paper(s): [Paper](https://arxiv.org/abs/2509.18119)
- Algorithm: AdaGRPO (Difficulty-Adaptive) · Framework: Custom · Agent: Single · Turns: Multi · Tools: Yes (Android)
- Reward phase: Outcome · Reward type: Rule
- Task: Mobile GUI (AndroidWorld/AndroidLab)

### DART-GUI
- **Idea:** Decoupled async RL (env/rollout/data-manager/trainer modules) plus adaptive data curation training on high-entropy decision steps for OSWorld agents.
- `https://github.com/Computer-use-agents/dart-gui` · org: Computer-use-agents · date: 2025.9
- Paper(s): [Paper](https://arxiv.org/abs/2509.23866)
- Algorithm: Decoupled GRPO · Framework: veRL · Agent: Single · Turns: Multi · Tools: Yes
- Reward phase: Outcome · Reward type: Rule
- Task: GUI (OSWorld)

### Mano-P
- **Idea:** Three-stage SFT to offline RL to online RL pipeline with a simulated data-generation environment and a verification-based error-recovery module.
- `https://github.com/Mininglamp-AI/Mano-P` · org: Mininglamp AI · date: 2025.9
- Paper(s): [Paper](https://arxiv.org/abs/2509.17336)
- Algorithm: Three-stage SFT→Offline RL→Online RL · Framework: Mano-SDK · Agent: Single · Turns: Multi · Tools: Yes
- Reward phase: Both · Reward type: Rule
- Task: GUI (OSWorld)

### InfiGUI-G1
- **Idea:** Adaptive Exploration Policy Optimization (AEPO) uses multi-answer generation plus a theoretically grounded Adaptive Exploration Reward to improve semantic GUI grounding.
- `https://github.com/InfiXAI/InfiGUI-G1` · org: InfiX AI · date: 2025.8
- Paper(s): [Paper](https://arxiv.org/abs/2508.05731)
- Algorithm: AEPO · Framework: veRL · Agent: Single · Turns: Single · Tools: No
- Reward phase: Outcome · Reward type: Rule
- Task: GUI/Grounding

### gui-rcpo
- **Idea:** Label-free test-time RL: spatial voting grids over multiple sampled predictions yield consensus-region rewards (RCPO) to self-improve GUI grounding without ground truth.
- `https://github.com/zju-real/gui-rcpo` · org: Zhejiang University · date: 2025.8
- Paper(s): [Paper](https://arxiv.org/abs/2508.05615)
- Algorithm: RCPO · Framework: Custom · Agent: Single · Turns: Single · Tools: No
- Reward phase: Outcome · Reward type: Rule (self-supervised)
- Task: GUI Grounding

### UI-AGILE
- **Idea:** Continuous grounding reward plus a 'Simple Thinking' reward balancing planning quality vs speed, with cropping-based resampling to fix sparse rewards in GUI grounding.
- `https://github.com/KDEGroup/UI-AGILE` · org: Xiamen University · date: 2025.7
- Paper(s): [Paper](https://arxiv.org/abs/2507.22025)
- Algorithm: GRPO · Framework: Custom · Agent: Single · Turns: Single · Tools: No
- Reward phase: Outcome · Reward type: Rule (continuous)
- Task: GUI Grounding

### GUI-G2
- **Idea:** Replaces sparse binary grounding rewards with continuous Gaussian point + coverage rewards giving dense gradients toward optimal click positions.
- `https://github.com/ZJU-REAL/GUI-G2` · org: Zhejiang University (ZJU-REAL) · date: 2025.7
- Paper(s): [Paper](https://arxiv.org/abs/2507.15846)
- Algorithm: GRPO (Gaussian Reward) · Framework: Custom (VLM-R1) · Agent: Single · Turns: Single · Tools: No
- Reward phase: Outcome · Reward type: Rule (continuous)
- Task: GUI Grounding

### MagicGUI
- **Idea:** Iterative two-stage training: large-scale continue-pretrain then RFT with a spatially-enhanced composite reward and dual filtering of RL signals.
- `https://github.com/MagicAgent-GUI/MagicGUI` · org: Honor (MagicAgent-GUI) · date: 2025.8
- Paper(s): [Paper](https://arxiv.org/abs/2508.03700)
- Algorithm: Reinforcement Fine-Tuning (RFT) · Framework: Custom · Agent: Single · Turns: Multi · Tools: Yes
- Reward phase: Outcome · Reward type: Model/Rule
- Task: Mobile GUI

### Grounding-R1
- **Idea:** GRPO rewards any click landing inside the target element's bounding box rather than the exact center as SFT does, aligning the objective with real user interaction.
- `https://github.com/Yan98/Grounding-R1` · org: Salesforce · date: 2025.6
- Paper(s): [blog](https://huggingface.co/blog/HelloKKMe/grounding-r1)
- Algorithm: GRPO · Framework: trl · Agent: Single · Turns: Multi · Tools: Yes
- Reward phase: Outcome · Reward type: Model
- Task: GUI Grounding

### AgentCPM-GUI
- **Idea:** Applies GRPO reinforcement fine-tuning after imitation learning to improve reasoning and generalization to unseen mobile-GUI layouts.
- `https://github.com/OpenBMB/AgentCPM-GUI` · org: OpenBMB/Tsinghua/RUC · date: 2025.6
- Paper(s): [Paper](https://arxiv.org/abs/2506.01391)
- Algorithm: GRPO · Framework: Huggingface · Agent: Single · Turns: Multi · Tools: Yes
- Reward phase: Outcome · Reward type: Model
- Task: Mobile GUI

### TTI
- **Idea:** Test-Time Interaction: curriculum-based online RL that adaptively grows rollout length, scaling 'doing' (exploration/backtracking) instead of just 'thinking' for web agents.
- `https://github.com/test-time-interaction/TTI` · org: CMU · date: 2025.6
- Paper(s): [Paper](https://arxiv.org/abs/2506.07976)
- Algorithm: REINFORCE/BC · Framework: Custom · Agent: Single · Turns: Multi · Tools: Web Browsing
- Reward phase: Outcome · Reward type: External
- Task: Web

### GTA1
- **Idea:** Pairs test-time scaling (sample multiple action proposals, judge-model selection) with click-success RL for GUI grounding without explicit thinking.
- `https://github.com/Yan98/GTA1` · org: Salesforce / ANU · date: 2025.7
- Paper(s): [Paper](https://arxiv.org/abs/2507.05791)
- Algorithm: GRPO-style (click-success reward) · Framework: Custom (DeepSpeed) · Agent: Single · Turns: Multi · Tools: Yes
- Reward phase: Outcome · Reward type: Rule
- Task: GUI Grounding (OSWorld/ScreenSpot-Pro)

### SE-GUI
- **Idea:** Self-evolutionary RFT for GUI grounding: dense continuous-accuracy policy gradient plus attention-map-guided iterative refinement from a small seed set.
- `https://github.com/YXB-NKU/SE-GUI` · org: Nankai University/vivo · date: 2025.5
- Paper(s): [Paper](https://arxiv.org/abs/2505.12370)
- Algorithm: GRPO · Framework: trl · Agent: Single · Turns: Single · Tools: Yes
- Reward phase: Both · Reward type: Rule
- Task: GUI Grounding

### ARPO
- **Idea:** Augments GRPO with a replay buffer of successful trajectories plus baseline-performance task filtering to stabilize long-horizon GUI-agent RL.
- `https://github.com/dvlab-research/ARPO` · org: CUHK/HKUST · date: 2025.5
- Paper(s): [Paper](https://arxiv.org/abs/2505.16282)
- Algorithm: GRPO · Framework: veRL · Agent: Single · Turns: Multi · Tools: Computer Use
- Reward phase: Outcome · Reward type: External
- Task: GUI

### GUI-G1
- **Idea:** Fixes R1-Zero GUI RL failure modes via fast-thinking template, box-size reward constraint to block reward hacking, and difficulty-aware objective scaling.
- `https://github.com/Yuqi-Zhou/GUI-G1` · org: RUC · date: 2025.5
- Paper(s): [Paper](https://arxiv.org/abs/2505.15810)
- Algorithm: GRPO · Framework: TRL · Agent: Single · Turns: Single · Tools: No
- Reward phase: Outcome · Reward type: Rule/External
- Task: GUI

### WebAgent-R1
- **Idea:** End-to-end multi-turn web RL using only binary task-success rewards with asynchronous diverse trajectory generation, avoiding reward shaping.
- `https://github.com/weizhepei/WebAgent-R1` · org: Amazon/UVA · date: 2025.5
- Paper(s): [Paper](https://arxiv.org/abs/2505.16421)
- Algorithm: M-GRPO · Framework: Custom · Agent: Single · Turns: Multi · Tools: Yes (Web browsing)
- Reward phase: Outcome · Reward type: Rule (task success)
- Task: Web Navigation (WebArena-Lite)

### ZeroGUI
- **Idea:** Zero-human-cost online GUI RL using VLMs for automatic task generation and reward estimation, plus two-stage online learning.
- `https://github.com/OpenGVLab/ZeroGUI` · org: Shanghai AI Lab · date: 2025.5
- Paper(s): [Paper](https://arxiv.org/abs/2505.23762)
- Algorithm: Online RL · Framework: Custom · Agent: Single · Turns: Multi · Tools: Yes (GUI actions)
- Reward phase: Outcome · Reward type: Rule
- Task: GUI Agent

### GUI-R1
- **Idea:** Unified action-space rule-based GRPO for GUI agents, matching prior SOTA with only ~3K curated examples vs 13M.
- `https://github.com/ritzz-ai/GUI-R1` · org: CAS/NUS · date: 2025.4
- Paper(s): [Paper](https://arxiv.org/abs/2504.10458)
- Algorithm: GRPO · Framework: veRL · Agent: Single · Turns: Multi · Tools: No
- Reward phase: Outcome · Reward type: Rule
- Task: GUI

### InfiGUI-R1
- **Idea:** Deliberation enhancement via sub-goal-guidance rewards plus constructed error-recovery scenarios, moving GUI agents from reactive to planning behavior.
- `https://github.com/Reallm-Labs/InfiGUI-R1` · org: Zhejiang University · date: 2025.4
- Paper(s): [Paper](https://arxiv.org/abs/2504.14239)
- Algorithm: RL + sub-goal guidance · Framework: Custom · Agent: Single · Turns: Multi · Tools: Yes
- Reward phase: Both · Reward type: Rule
- Task: GUI Reasoning

### UI-R1
- **Idea:** First to adapt DeepSeek-R1-style rule-based RL to multimodal GUI agents via a rule-based action reward optimized with GRPO.
- `https://github.com/lll6gg/UI-R1` · org: vivo/CUHK · date: 2025.3
- Paper(s): [Paper](https://arxiv.org/abs/2503.21620)
- Algorithm: GRPO · Framework: TRL · Agent: Single · Turns: Both · Tools: Computer/Phone Use
- Reward phase: Process · Reward type: Rule
- Task: GUI

### CollabUIAgents
- **Idea:** Multi-agent credit re-assignment using LLM-assigned process rewards (not env rewards) so role-free agents learn collaboration that generalizes across environments.
- `https://github.com/THUNLP-MT/CollabUIAgents` · org: Tsinghua/Alibaba/HKUST · date: 2025.2
- Paper(s): [Paper](https://arxiv.org/abs/2502.14496)
- Algorithm: DPO (credit re-assignment) · Framework: Custom · Agent: Multi · Turns: Multi · Tools: Yes (GUI interaction)
- Reward phase: Process · Reward type: Model (LLM)
- Task: GUI (Mobile + Web)

### DigiQ
- **Idea:** Offline TD-learned VLM Q-function on frozen intermediate features, then Best-of-N policy extraction, enabling Android-agent improvement without env interaction.
- `https://github.com/DigiRL-agent/digiq` · org: UC Berkeley/CMU/Amazon · date: 2025.2
- Paper(s): [Paper](https://arxiv.org/abs/2502.15760)
- Algorithm: Value-based offline RL · Framework: Custom · Agent: Single · Turns: Multi · Tools: Yes
- Reward phase: Outcome · Reward type: Model (Q-function)
- Task: Android Device Control

### GUI-Agent-RL
- **Idea:** VEM: a pretrained Value Environment Model estimates state-action values from offline data to guide policy without env interaction or next-state prediction.
- `https://github.com/microsoft/GUI-Agent-RL` · org: Microsoft · date: 2025.2
- Paper(s): [Paper](https://arxiv.org/abs/2502.18906)
- Algorithm: Value-based RL (VEM) · Framework: Custom · Agent: Single · Turns: Multi · Tools: Yes
- Reward phase: Outcome · Reward type: Model
- Task: GUI (Web Shopping)

### WebAgent
- **Idea:** Strictly on-policy GRPO with token-level gradients, leave-one-out advantage, and negative-sample filtering to stabilize RL in non-stationary web info-seeking.
- `https://github.com/Alibaba-NLP/WebAgent` · org: Alibaba · date: 2025.1
- Paper(s): [paper1](https://arxiv.org/abs/2501.07572), [paper2](https://arxiv.org/abs/2505.22648)
- Algorithm: DAPO · Framework: LLaMA-Factory · Agent: Multi · Turns: Multi · Tools: Yes
- Reward phase: Process · Reward type: Model
- Task: Web
