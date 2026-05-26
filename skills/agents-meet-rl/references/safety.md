# Safety / Red-Teaming

RL for jailbreak attack/defense, tool-call safety, agent guardrails.

_Total: 9 entries._

### ToolSafe
- **Idea:** TS-Guard, a multi-task RL guardrail that judges tool-call safety from interaction history at each step, cutting harmful invocations ~65% under prompt injection.
- `https://github.com/MurrayTom/ToolSafe` · org: Academic (MurrayTom) · date: 2026.1
- Paper(s): [Paper](https://arxiv.org/abs/2601.10156)
- Algorithm: Multi-task GRPO · Framework: veRL · Agent: Single · Turns: Multi · Tools: Yes (tool monitoring)
- Reward phase: Process · Reward type: Rule + Model
- Task: Tool-Invocation Safety Guardrail

### TROJail
- **Idea:** Trajectory-level RL for multi-turn jailbreaks: final-turn harmfulness as outcome reward plus refusal-penalty and semantic-steering process rewards for sparse signal.
- `https://github.com/xxiqiao/TROJail` · org: Academic (ACL 2026) · date: 2025.12
- Paper(s): [Paper](https://arxiv.org/abs/2512.07761)
- Algorithm: Multi-turn GRPO variant · Framework: RAGEN + vLLM · Agent: Single · Turns: Multi · Tools: Yes (target LLM)
- Reward phase: Both · Reward type: Model (harmfulness judge) + Rule
- Task: Multi-turn Jailbreak Attack

### SafeSearch
- **Idea:** Multi-objective RL adding a query-level shaping term that penalizes unsafe search queries, cutting harmfulness >90% while keeping QA utility for search agents.
- `https://github.com/amazon-science/SafeSearch` · org: Amazon Science · date: 2025.10
- Paper(s): [Paper](https://arxiv.org/abs/2510.17017)
- Algorithm: PPO (GAE/GRPO) · Framework: veRL · Agent: Single · Turns: Multi · Tools: Search
- Reward phase: Both · Reward type: Rule + Model
- Task: Safe QA/Search

### Jailbreak-R1
- **Idea:** Three-stage GRPO red-teaming (imitation cold-start, diversity+consistency warm-up, progressive jailbreak reward) to balance attack effectiveness and diversity.
- `https://github.com/yuki-younai/Jailbreak-R1` · org: Academic (yuki-younai) · date: 2025.6
- Paper(s): [Paper](https://arxiv.org/abs/2506.00782)
- Algorithm: GRPO (3-stage: imitation→warm-up→progressive) · Framework: Custom · Agent: Single · Turns: Multi · Tools: Yes (target LLM)
- Reward phase: Both · Reward type: Model (judge)
- Task: Red-teaming Prompt Generation

### GuardReasoner-VL
- **Idea:** Reasoning-based VLM safety guard: SFT cold-start then online RL with length-aware safety reward and dynamic clipping for deliberative multimodal moderation.
- `https://github.com/yueliu1999/GuardReasoner-VL` · org: NUS (yueliu1999) · date: 2025.5
- Paper(s): [Paper](https://arxiv.org/abs/2505.11049)
- Algorithm: Online RL w/ rejection sampling · Framework: Custom · Agent: Single · Turns: Multi · Tools: No
- Reward phase: Both · Reward type: Rule + Model
- Task: VLM Safety Guard (multimodal)

### xJailbreak
- **Idea:** RL jailbreak guided by embedding proximity between benign and malicious prompts, giving a denser reward that preserves intent while maximizing attack success.
- `https://github.com/Aegis1863/xJailbreak` · org: Academic · date: 2025.1
- Paper(s): [Paper](https://arxiv.org/abs/2501.16727)
- Algorithm: RL · Framework: Custom · Agent: Single · Turns: Multi · Tools: Yes (iterative)
- Reward phase: Outcome · Reward type: Model (embedding)
- Task: Jailbreaking

### Auto-RT
- **Idea:** RL red-teaming that optimizes multi-step attack strategies via early-terminated exploration and progressive reward tracking with intermediate downgrade models.
- `https://github.com/icip-cas/Auto-RT` · org: ICIP-CAS · date: 2025.1
- Paper(s): [Paper](https://arxiv.org/abs/2501.01830)
- Algorithm: PPO · Framework: Custom · Agent: Single · Turns: Multi · Tools: Yes (strategy exploration)
- Reward phase: Outcome · Reward type: Model
- Task: Red Teaming

### RLbreaker
- **Idea:** Frames jailbreaking as RL-guided search (customized PPO + bespoke reward) instead of random genetic mutation, yielding transferable black-box attacks.
- `https://github.com/XuanChen-xc/RLbreaker` · org: Purdue · date: 2024.6
- Paper(s): [Paper](https://arxiv.org/abs/2406.08705)
- Algorithm: Custom PPO · Framework: Custom · Agent: Single · Turns: Multi · Tools: Yes (mutator selection)
- Reward phase: Outcome · Reward type: Model
- Task: Jailbreaking

### curiosity_redteam
- **Idea:** Adds curiosity/novelty bonuses to RL red-teaming so the attacker covers a far more diverse span of prompts instead of collapsing to a few effective test cases.
- `https://github.com/Improbable-AI/curiosity_redteam` · org: MIT · date: 2024.2
- Paper(s): [Paper](https://arxiv.org/abs/2402.19464)
- Algorithm: RL + Curiosity · Framework: Custom · Agent: Single · Turns: Multi · Tools: Yes (iterative query)
- Reward phase: Outcome · Reward type: Model
- Task: Red Teaming
