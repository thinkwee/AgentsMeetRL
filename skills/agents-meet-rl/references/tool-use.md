# Tool-Use Agents

Agents that call external APIs/MCP/code interpreters. Reward usually mixes correctness + format + tool-call validity.

_Total: 23 entries._

## Contents

SPADER, APPO, AgenticQwen, Agent-STAR, ToolMaster, Agent-R1, ToolOrchestra, MATPO, ToolBrain, CodeGym, UserRL, Tool-R1, MiroRL, AWorld, verl-tool, Multi-Turn-RL-Agent, Tool-N1, Tool-Star, RL-Factory, calculator_agent_rl, ReTool, ToolRL, ReCall.

### SPADER
- **Idea:** Step-wise Peer Advantage gives critic-free step-level credit, plus a diversity-aware exploration reward for comprehensive multi-answer QA.
- `https://github.com/KhanCold/spader` · org: Zhejiang University · date: 2026.6
- Paper(s): [Paper](https://arxiv.org/abs/2606.00593)
- Algorithm: GRPO + Step-wise Peer Advantage (SPA) · Framework: veRL · Agent: Single · Turns: Multi · Tools: Yes (search)
- Reward phase: Both · Reward type: Rule-Based (entity-match + diversity)
- Task: Long-horizon tool-augmented multi-answer QA (QAMPARI)

### APPO
- **Idea:** Procedure-aware branching extends ARPO with fine-grained credit at tool-call decision points across reasoning, search, and code.
- `https://github.com/AMAP-ML/APPO` · org: Alibaba AMAP (AMAP-ML) · date: 2026.6
- Paper(s): [Paper](https://arxiv.org/abs/2606.12384)
- Algorithm: APPO (procedure-aware branching; extends ARPO/GRPO) · Framework: veRL · Agent: Single · Turns: Multi · Tools: Yes (search + code)
- Reward phase: Process · Reward type: Rule-Based
- Task: Multi-turn TIR (reasoning+search+code, 13 benchmarks)

### AgenticQwen
- **Idea:** Dual data flywheels (reasoning learns from errors; agentic expands linear workflows into branching behavior trees) auto-generate harder tasks for tool-use RL.
- `https://github.com/haruhi-sudo/data_synth_and_rl` · org: Alibaba PAI · date: 2026.4
- Paper(s): [Paper](https://arxiv.org/abs/2604.21590)
- Algorithm: Multi-round RL (Reasoning RL + Agentic RL w/ dual data flywheels) · Framework: veRL (w/ EasyDistill) · Agent: Single · Turns: Multi · Tools: Yes (Python interpreter, web search, mock tools)
- Reward phase: Outcome · Reward type: Rule + Model (rubric)
- Task: Industrial Tool Use (search, data analysis, tau-bench airline/retail/telecom)

### Agent-STAR
- **Idea:** A full data-synthesis to SFT to RL recipe with dense curriculum rewards for long-horizon (up to 60-turn) ReAct tool agents on TravelPlanner.
- `https://github.com/WxxShirley/Agent-STAR` · org: CUHK · date: 2026.3
- Paper(s): [Paper](https://arxiv.org/abs/2603.21972)
- Algorithm: GRPO + dense/curriculum reward (STAR recipe) · Framework: veRL · Agent: Single · Turns: Multi · Tools: Yes (planning APIs)
- Reward phase: Both · Reward type: Rule + External
- Task: Long-horizon tool-using agents (TravelPlanner, ReAct up to 60 turns)

### ToolMaster
- **Idea:** Combines imitation of teacher trajectories with a trial-then-execute phase, then RL, to generalize tool use to novel and unseen tools.
- `https://github.com/NEUIR/ToolMaster` · org: Northeastern University (NEUIR) · date: 2026.1
- Paper(s): [Paper](https://arxiv.org/abs/2601.12762)
- Algorithm: SFT + GRPO (trial-then-execute) · Framework: Custom · Agent: Single · Turns: Multi · Tools: Yes (Simulated tools)
- Reward phase: Outcome · Reward type: Rule/External
- Task: Tool trialing + execution (ToolHop/TMDB/StableToolBench)

### Agent-R1
- **Idea:** Formalizes LLM-agent components as an extended MDP and provides a modular, extensible end-to-end RL training framework across diverse task scenarios.
- `https://github.com/0russwest0/Agent-R1` · org: USTC · date: 2025.11
- Paper(s): [Paper](https://arxiv.org/abs/2511.14460)
- Algorithm: PPO/GRPO · Framework: veRL · Agent: Single · Turns: Multi · Tools: Yes
- Reward phase: Both · Reward type: Model
- Task: Tool-use/QA

### ToolOrchestra
- **Idea:** RL with outcome-, efficiency-, and preference-aware rewards trains a small 8B orchestrator to coordinate tools and larger models more cost-effectively.
- `https://github.com/NVlabs/ToolOrchestra` · org: NVIDIA / HKU · date: 2025.11
- Paper(s): [Paper](https://arxiv.org/abs/2511.21689)
- Algorithm: End-to-end RL (outcome+efficiency+preference) · Framework: Custom (veRL-based) · Agent: Single · Turns: Multi · Tools: Yes (Search/Code/LLMs)
- Reward phase: Both · Reward type: All
- Task: Tool orchestration / agentic workflows

### MATPO
- **Idea:** Trains planner and worker roles within a single LLM via role-specific prompts and principled cross-role credit assignment, avoiding separate models.
- `https://github.com/mzf666/MATPO` · org: MiroMind AI · date: 2025.10
- Paper(s): [Paper](https://arxiv.org/abs/2510.04678)
- Algorithm: GRPO (multi-agent) · Framework: Custom · Agent: Multi · Turns: Multi · Tools: Yes (MCP: Serper, Web scraping)
- Reward phase: Outcome · Reward type: Rule
- Task: Tool-use/Search

### ToolBrain
- **Idea:** Unified tool-use RL framework with LLM-as-a-judge automated reward generation plus GRPO/DPO, distillation, and efficient fine-tuning to avoid manual reward engineering.
- `https://github.com/ToolBrain/ToolBrain` · org: ToolBrain (AAMAS 2026) · date: 2025.10
- Paper(s): [Paper](https://arxiv.org/abs/2510.00023)
- Algorithm: GRPO/DPO · Framework: Custom · Agent: Single · Turns: Multi · Tools: Yes (User-defined tools)
- Reward phase: Outcome · Reward type: Rule/Model
- Task: Agentic tool training

### CodeGym
- **Idea:** Converts static coding problems into interactive multi-turn tool-use environments so agents learn diverse tool workflows via RL rather than static-trajectory SFT.
- `https://github.com/StigLidu/CodeGym` · org: Academic · date: 2025.9
- Paper(s): [Paper](https://arxiv.org/abs/2509.17325)
- Algorithm: GRPO-family · Framework: Custom · Agent: Single · Turns: Multi · Tools: Yes (Synthesized tools)
- Reward phase: Outcome · Reward type: Rule (verifiable)
- Task: Synthetic Multi-turn Tool-Use

### UserRL
- **Idea:** Standardized gym with simulated users shows reward-shaping and user-simulator choice matter as much as model scale for training interactive user-facing agents.
- `https://github.com/SalesforceAIResearch/UserRL` · org: Salesforce AI Research · date: 2025.9
- Paper(s): [Paper](https://arxiv.org/abs/2509.19736)
- Algorithm: GRPO (multi-turn credit) · Framework: veRL · Agent: Single · Turns: Multi · Tools: Yes
- Reward phase: Both · Reward type: Model/External
- Task: User-centric (Function/Persuade/Search/Tau Gyms)

### Tool-R1
- **Idea:** Maintains a dynamic sample queue caching and reusing high-quality trajectories to cut online sampling cost while RL-training agents to emit executable Python tool code.
- `https://github.com/YBYBZhang/Tool-R1` · org: Individual (YBYBZhang) · date: 2025.9
- Paper(s): [Paper](https://arxiv.org/abs/2509.12867)
- Algorithm: Policy optimization (PPO-style) · Framework: Custom · Agent: Single · Turns: Multi · Tools: Yes (Python exec)
- Reward phase: Outcome · Reward type: Model + External
- Task: Agentic Tool Use (GAIA)

### MiroRL
- **Idea:** First RL framework supporting multi-turn MCP tool calls for deep-research agents, integrating search, web, file, and code execution directly into training.
- `https://github.com/MiroMindAI/MiroRL` · org: MiroMindAI · date: 2025.8
- Paper(s): [HF Repo](https://huggingface.co/miromind-ai)
- Algorithm: GRPO · Framework: veRL · Agent: Single · Turns: Multi · Tools: MCP
- Reward phase: Both · Reward type: Rule-based
- Task: Reasoning/Planning/ToolUse

### AWorld
- **Idea:** Tackles experience-generation bottleneck by distributing agent rollouts across a cluster for 14.6x faster experience collection, enabling large-scale agent RL.
- `https://github.com/inclusionAI/AWorld` · org: Ant Group (inclusionAI) · date: 2025.8
- Paper(s): [Paper](https://arxiv.org/abs/2508.20404)
- Algorithm: GRPO · Framework: veRL · Agent: Both · Turns: Multi · Tools: Yes
- Reward phase: Outcome · Reward type: External/Rule
- Task: Search/Web/Code

### verl-tool
- **Idea:** Tool-as-environment paradigm fully decoupling actor rollout from environment via a unified tool API for native multi-turn tool-calling RL.
- `https://github.com/TIGER-AI-Lab/verl-tool` · org: TIGER-Lab · date: 2025.6
- Paper(s): [X](https://x.com/DongfuJiang/status/1929198238017720379)
- Algorithm: PPO/GRPO · Framework: veRL · Agent: Single · Turns: Both · Tools: Yes
- Reward phase: Both · Reward type: Rule/External
- Task: Math/Code

### Multi-Turn-RL-Agent
- **Idea:** First systematic study of turn-level reward design for multi-turn agent RL, showing intermediate rewards give finer credit assignment, faster convergence, higher accuracy.
- `https://github.com/SiliangZeng/Multi-Turn-RL-Agent` · org: University of Minnesota · date: 2025.5
- Paper(s): [Paper](https://arxiv.org/abs/2505.11821)
- Algorithm: GRPO · Framework: Custom · Agent: Single · Turns: Multi · Tools: Yes
- Reward phase: Both · Reward type: Rule/External
- Task: Tool-use/Math

### Tool-N1
- **Idea:** Trains tool-use with a binary rule-based reward judging only format validity and call correctness, letting reasoning emerge without annotated trajectories.
- `https://github.com/NVlabs/Tool-N1` · org: NVIDIA · date: 2025.5
- Paper(s): [Paper](https://arxiv.org/abs/2505.00024)
- Algorithm: PPO · Framework: veRL · Agent: Single · Turns: Multi · Tools: Yes
- Reward phase: Outcome · Reward type: All
- Task: Math/Dialogue

### Tool-Star
- **Idea:** Pairs tool-integrated data synthesis with multi-tool self-critic RL and hierarchical reward design (cold-start SFT then staged RL) for multi-tool coordination.
- `https://github.com/dongguanting/Tool-Star` · org: RUC · date: 2025.5
- Paper(s): [Paper](https://arxiv.org/abs/2505.16410)
- Algorithm: PPO/DPO/ORPO/SimPO/KTO · Framework: LLaMA-Factory · Agent: Single · Turns: Multi · Tools: Yes
- Reward phase: Outcome · Reward type: Model/External
- Task: Multi-modal/Tool Use/Dialogue

### RL-Factory
- **Idea:** Decouples environment from RL post-training with async tool-calling, needing only a tool config and reward function while doubling training throughput.
- `https://github.com/Simple-Efficient/RL-Factory` · org: Simple-Efficient · date: 2025.5
- Paper(s): [model](https://huggingface.co/Simple-Efficient/RLFactory-Qwen3-8B-GRPO)
- Algorithm: GRPO · Framework: veRL · Agent: Multi · Turns: Multi · Tools: MCP
- Reward phase: Both · Reward type: All
- Task: Tool-use/NL2SQL

### calculator_agent_rl
- **Idea:** Hybrid reward pairing LLM-as-judge process scoring with code-based answer verification yields large calculator-tool accuracy gains on a 3B model via GRPO.
- `https://github.com/Danau5tin/calculator_agent_rl` · org: Individual (Danau5tin) · date: 2025.5
- Paper(s): —
- Algorithm: GRPO · Framework: Verifiers · Agent: Single · Turns: Multi · Tools: Yes
- Reward phase: Outcome · Reward type: Model (Claude-judge)
- Task: Calculator Tool Use

### ReTool
- **Idea:** Uses outcome-reward RL to interleave real-time code execution within reasoning, letting the model learn strategically when and how to invoke the code tool.
- `https://github.com/ReTool-RL/ReTool` · org: ByteDance · date: 2025.4
- Paper(s): [Paper](https://arxiv.org/abs/2504.11536)
- Algorithm: PPO · Framework: veRL · Agent: Single · Turns: Multi · Tools: Code
- Reward phase: Outcome · Reward type: External
- Task: Math

### ToolRL
- **Idea:** Shows coarse answer-matching rewards fail for tool use; principled fine-grained reward design over tools and parameters is essential for effective GRPO training.
- `https://github.com/qiancheng0/ToolRL` · org: UIUC · date: 2025.4
- Paper(s): [Paper](https://arxiv.org/abs/2504.13958)
- Algorithm: GRPO/PPO · Framework: veRL · Agent: Single · Turns: Multi · Tools: Yes
- Reward phase: Outcome · Reward type: Rule/External
- Task: Tool Learning

### ReCall
- **Idea:** Treats search/retrieval as integral reasoning steps trained via RL (ReSearch), learning when and how to retrieve without supervised reasoning annotations.
- `https://github.com/Agent-RL/ReCall` · org: BaiChuan · date: 2025.3
- Paper(s): [Paper](https://arxiv.org/abs/2503.19470)
- Algorithm: PPO/GRPO/RLOO/REINFORCE++/ReMax · Framework: veRL · Agent: Single · Turns: Multi · Tools: Yes
- Reward phase: Outcome · Reward type: All
- Task: Tool-use/Math/QA
