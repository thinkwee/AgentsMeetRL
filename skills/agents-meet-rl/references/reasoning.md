# Reasoning Agents

Tool-integrated reasoning (TIR) agents — math/QA + search/code. Common starting point for new agentic-RL projects.

_Total: 18 entries._

## Contents

Agent0, KG-R1, AgentFlow, THOR, Tool-Light, ARPO, terminal-bench-rl, AutoTIR, MOTIF, cmriat/l0, agent-distillation, EasyR1, AutoCoA, ToRL, ReMA, Agentic-Reasoning, SimpleTIR, openrlhf_async_pipline.

### Agent0
- **Idea:** Symbiotic co-evolution: a curriculum agent proposes harder tool-aware tasks while an executor agent learns to solve them, from zero external data.
- `https://github.com/aiming-lab/Agent0` · org: UNC‑Chapel Hill / Salesforce Research / Stanford University · date: 2025.11
- Paper(s): [Paper](https://arxiv.org/abs/2511.16043)
- Algorithm: ADPO · Framework: veRL · Agent: Multi · Turns: Multi · Tools: Yes
- Reward phase: Process · Reward type: Model/Verifier
- Task: Math/Visual

### KG-R1
- **Idea:** Single unified LLM agent with four KG operations trained by GRPO, giving schema-agnostic train-once-transfer-anywhere KGQA at low token cost.
- `https://github.com/Jinyeop3110/KG-R1` · org: UIUC/Google · date: 2025.9
- Paper(s): [Paper1](https://arxiv.org/abs/2503.09516), [Paper2](https://arxiv.org/abs/2505.15117)
- Algorithm: GRPO/PPO · Framework: veRL · Agent: Single · Turns: Multi · Tools: KG Retrieval
- Reward phase: Both · Reward type: Rule/Model
- Task: KGQA

### AgentFlow
- **Idea:** Flow-GRPO trains the planner inside a live multi-turn loop by converting it to single-turn updates and broadcasting the trajectory outcome to every turn.
- `https://github.com/lupantech/AgentFlow` · org: Stanford University · date: 2025.10
- Paper(s): [arXiv](https://arxiv.org/abs/2510.05592)
- Algorithm: Flow-GRPO · Framework: veRL · Agent: Single · Turns: Multi · Tools: Yes
- Reward phase: Outcome · Reward type: Model/External
- Task: Search/Math/QA

### THOR
- **Idea:** Hierarchical GRPO jointly optimizing episode-level solving and step-level code, exploiting that intermediate tool-call success predicts final-answer correctness.
- `https://github.com/JingMog/THOR` · org: USTC / iFLYTEK · date: 2025.9
- Paper(s): [Paper](https://arxiv.org/abs/2509.13761)
- Algorithm: Hierarchical GRPO (trajectory+step) · Framework: veRL · Agent: Single · Turns: Multi · Tools: Yes (Python)
- Reward phase: Both · Reward type: External (SandboxFusion)
- Task: Math (MATH500/AIME/Olympiad)

### Tool-Light
- **Idea:** Self-evolved DPO using entropy-guided self-sampling to teach efficient tool use, fixing insufficient/excessive tool calls and overthinking via the model's own pairs.
- `https://github.com/RUC-NLPIR/Tool-Light` · org: RUC (RUC-NLPIR) · date: 2025.9
- Paper(s): [Paper](https://arxiv.org/abs/2509.23285)
- Algorithm: Self-Evolved DPO · Framework: LLaMA-Factory · Agent: Single · Turns: Multi · Tools: Yes (FlashRAG/Python)
- Reward phase: Outcome · Reward type: Model (preference)
- Task: Tool-Integrated Reasoning

### ARPO
- **Idea:** Entropy-based adaptive rollout that adds step-level sampling after high-uncertainty tool calls, matching baselines with half the tool-use budget.
- `https://github.com/dongguanting/ARPO` · org: RUC, Kuaishou · date: 2025.7
- Paper(s): [Paper](https://arxiv.org/abs/2507.19849)
- Algorithm: GRPO · Framework: veRL · Agent: Single · Turns: Multi · Tools: Yes
- Reward phase: Outcome · Reward type: Model/Rule
- Task: Math/Coding

### terminal-bench-rl
- **Idea:** GRPO terminal-agent training with a hybrid reward: 65% Docker-verified weighted unit tests plus 35% LLM-judge scoring of planning and tool-use process.
- `https://github.com/Danau5tin/terminal-bench-rl` · org: Individual (Danau5tin) · date: 2025.7
- Paper(s): —
- Algorithm: GRPO · Framework: rLLM · Agent: Single · Turns: Multi · Tools: Yes
- Reward phase: Outcome · Reward type: Model+External Verifier
- Task: Coding/Terminal

### AutoTIR
- **Idea:** PPO with a hybrid reward (answer correctness + format + wrong-tool penalty) lets the model autonomously decide whether and which tool to invoke without fixed patterns.
- `https://github.com/weiyifan1023/AutoTIR` · org: Beihang University / BAAI · date: 2025.7
- Paper(s): [Paper](https://arxiv.org/abs/2507.21836)
- Algorithm: PPO · Framework: veRL · Agent: Single · Turns: Multi · Tools: Yes (Search/Python)
- Reward phase: Outcome · Reward type: Rule
- Task: Autonomous Tool Selection (QA/Math/IF)

### MOTIF
- **Idea:** Multi-round GRPO that generates thinking tokens across several sequential rounds to expand effective reasoning beyond the context-window limit.
- `https://github.com/purbeshmitra/MOTIF` · org: University of Maryland · date: 2025.7
- Paper(s): [Paper](https://arxiv.org/abs/2507.02851)
- Algorithm: GRPO · Framework: trl · Agent: Single · Turns: Multi · Tools: No
- Reward phase: Outcome · Reward type: Rule
- Task: QA

### cmriat/l0
- **Idea:** Code-as-action NB-Agent (REPL) trained purely with RLVR via a low-cost sandboxed concurrent worker pool, lifting factuality QA from a base model with no SFT.
- `https://github.com/cmriat/l0` · org: CMRIAT · date: 2025.6
- Paper(s): [Paper](https://arxiv.org/abs/2506.23667)
- Algorithm: PPO · Framework: veRL · Agent: Multi · Turns: Multi · Tools: Yes
- Reward phase: Process · Reward type: All
- Task: QA

### agent-distillation
- **Idea:** Distills full tool-using agent behavior (not just CoT) into small LMs via first-thought prefix prompting and self-consistent action generation.
- `https://github.com/Nardien/agent-distillation` · org: KAIST · date: 2025.5
- Paper(s): [Paper](https://arxiv.org/abs/2505.17612)
- Algorithm: PPO · Framework: Custom · Agent: Single · Turns: Multi · Tools: Yes
- Reward phase: Process · Reward type: External
- Task: QA/Math

### EasyR1
- **Idea:** Efficient multi-modal RL framework (HybridEngine + vLLM SPMD) supporting GRPO/DAPO/RLOO/GSPO etc. for text and vision-language models with padding-free training and LoRA.
- `https://github.com/hiyouga/EasyR1` · org: Individual · date: 2025.4
- Paper(s): [paper2](https://arxiv.org/abs/2409.19256), [repo1](https://github.com/hiyouga/EasyR1)
- Algorithm: GRPO · Framework: veRL · Agent: Single · Turns: Multi · Tools: Yes
- Reward phase: Process · Reward type: Model
- Task: Vision-Language

### AutoCoA
- **Idea:** SFT+RL trains agent models to internalize Chain-of-Action, using step-level action triggers and an internal world model to cut real-environment interaction cost.
- `https://github.com/ADaM-BJTU/AutoCoA` · org: BJTU · date: 2025.3
- Paper(s): [Paper](https://arxiv.org/abs/2503.06580)
- Algorithm: GRPO · Framework: veRL · Agent: Multi · Turns: Multi · Tools: Yes
- Reward phase: Outcome · Reward type: All
- Task: Reasoning/Math/QA

### ToRL
- **Idea:** Tool-integrated RL from a base model lets LLMs discover when to invoke code via reward alone, emergently self-regulating ineffective code and switching reasoning modes.
- `https://github.com/GAIR-NLP/ToRL` · org: SJTU · date: 2025.3
- Paper(s): [Paper](https://arxiv.org/abs/2503.23383)
- Algorithm: GRPO · Framework: veRL · Agent: Single · Turns: Single · Tools: Yes
- Reward phase: Outcome · Reward type: Rule/External
- Task: Math

### ReMA
- **Idea:** Decouples reasoning into a high-level meta-thinking agent and a low-level reasoning agent, co-trained via multi-agent RL to elicit metacognitive planning.
- `https://github.com/ziyuwan/ReMA-public` · org: SJTU, UCL · date: 2025.3
- Paper(s): [Paper](https://arxiv.org/abs/2503.09501)
- Algorithm: PPO · Framework: veRL · Agent: Multi · Turns: Multi · Tools: No
- Reward phase: Outcome · Reward type: Rule
- Task: Math

### Agentic-Reasoning
- **Idea:** Augments LLM reasoning with a Mind-Map knowledge-graph agent plus web-search and code agents to keep long tool-heavy reasoning chains coherent.
- `https://github.com/theworldofagents/Agentic-Reasoning` · org: Oxford · date: 2025.2
- Paper(s): [Paper](https://arxiv.org/abs/2502.04644)
- Algorithm: Custom · Framework: Custom · Agent: Single · Turns: Multi · Tools: Web Browsing
- Reward phase: Process · Reward type: External
- Task: QA/Math

### SimpleTIR
- **Idea:** Stabilizes multi-turn tool-integrated RL by filtering out 'void' trajectories that yield neither a code block nor a final answer, curbing error accumulation and drift.
- `https://github.com/ltzheng/SimpleTIR` · org: NTU, Bytedance · date: 2025.2
- Paper(s): [Notion Blog](https://simpletir.notion.site/report)
- Algorithm: PPO/GRPO (with extensions) · Framework: veRL · Agent: Single · Turns: Multi · Tools: Yes
- Reward phase: Outcome · Reward type: All
- Task: Math, Coding

### openrlhf_async_pipline
- **Idea:** Asynchronous RLHF pipeline decoupling rollout from training (vLLM hybrid engine, dynamic batch size) to remove GPU idling, since generation is ~80% of RLHF time.
- `https://github.com/yyht/openrlhf_async_pipline` · org: OpenRLHF · date: 2024.5
- Paper(s): [Paper](https://arxiv.org/abs/2405.11143)
- Algorithm: PPO/REINFORCE++/DPO/RLOO · Framework: OpenRLHF · Agent: Single · Turns: Multi · Tools: No
- Reward phase: Outcome · Reward type: All
- Task: Dialogue/Reasoning/QA
