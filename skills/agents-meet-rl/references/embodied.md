# Embodied Agents

Agents in physical/simulated robotic environments.

_Total: 6 entries._

### Embodied-R1.5
- **Idea:** A single 8B embodied foundation model plays Planner-Grounder-Corrector in a closed loop, RFT-tuned with a multi-task balanced recipe to self-correct long-horizon real-robot tasks.
- `https://github.com/pickxiguapi/Embodied-R1.5` · org: Tianjin University · date: 2026.6
- Paper(s): [Paper](https://arxiv.org/abs/2606.11324)
- Algorithm: RFT (GRPO-family multimodal) · Framework: EasyR1 / veRL · Agent: Single · Turns: Multi · Tools: No (closed-loop PGC)
- Reward phase: Outcome · Reward type: Rule-Based
- Task: Embodied foundation model w/ Planner-Grounder-Corrector closed-loop

### AVA-VLA
- **Idea:** Casts latent reasoning as a sequential decision process and adds adaptive early-exit, optimizing VLA reasoning trajectories with task and trajectory-consistency rewards.
- `https://github.com/LeiDQ/AVA-VLA` · org: UCAS · date: 2026.6
- Paper(s): [Paper](https://arxiv.org/abs/2606.15099)
- Algorithm: PPO (latent reasoning as sequential decision) · Framework: Custom (PPO) · Agent: Single · Turns: Multi · Tools: No (closed-loop manipulation)
- Reward phase: Both · Reward type: External (task success) + Custom
- Task: VLA manipulation (LIBERO/ALOHA), latent CoT w/ early-exit

### WorldVLN
- **Idea:** Action-aware GRPO on an autoregressive world-action model closes the loop for aerial vision-language navigation by re-encoding observations after each action.
- `https://github.com/EmbodiedCity/WorldVLN.code` · org: Tsinghua (EmbodiedCity) · date: 2026.5
- Paper(s): [Paper](https://arxiv.org/abs/2605.15964)
- Algorithm: Action-aware GRPO · Framework: Custom · Agent: Single · Turns: Multi · Tools: No (closed-loop UAV control)
- Reward phase: Both · Reward type: Rule + Model
- Task: Aerial (UAV) vision-language navigation (closed-loop)

### Embodied-R1
- **Idea:** Uses embodiment-agnostic 'pointing' as intermediate action representation, trained via two-stage RFT with multi-task rewards for cross-robot transfer.
- `https://github.com/pickxiguapi/Embodied-R1` · org: Tianjing University · date: 2025.8
- Paper(s): [Paper](http://arxiv.org/abs/2508.13998)
- Algorithm: GRPO · Framework: veRL · Agent: Single · Turns: Single · Tools: No
- Reward phase: Outcome · Reward type: Rule
- Task: Grounding/Waypoint

### VIKI-R
- **Idea:** SFT on CoT-annotated demos then GRPO under multi-level rewards, grounding multi-robot cooperative reasoning directly in visual input.
- `https://github.com/MARS-EAI/VIKI-R` · org: MARS-EAI (NeurIPS 2025 D&B) · date: 2025.6
- Paper(s): [Paper](https://arxiv.org/abs/2506.09049)
- Algorithm: GRPO (RFT after SFT) · Framework: veRL + LLaMA-Factory · Agent: Multi · Turns: Multi · Tools: No
- Reward phase: Outcome · Reward type: Rule + Model
- Task: Embodied Multi-Robot Cooperation (VIKI-Bench)

### STeCa
- **Idea:** Detects bad steps via step-level reward comparison during exploration and uses LLM reflection to build corrected trajectories for calibration before RFT.
- `https://github.com/WangHanLinHenry/STeCa` · org: The Hong Kong Polytechnic University · date: 2025.2
- Paper(s): [Paper](https://arxiv.org/abs/2502.14276)
- Algorithm: DPO (RFT) · Framework: FastChat/TRL · Agent: Single · Turns: Multi · Tools: Environment Actions
- Reward phase: Both · Reward type: Rule/MC
- Task: Embodied/Household
