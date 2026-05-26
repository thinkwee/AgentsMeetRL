# Tool-Use Agents

Agents that call external APIs/MCP/code interpreters. Reward usually mixes correctness + format + tool-call validity.

_Total: 20 entries._

## Contents

AgenticQwen, ToolOrchestra, ToolMaster, MATPO, CodeGym, UserRL, ToolBrain, Tool-R1, MiroRL, verl-tool, Multi-Turn-RL-Agent, Tool-N1, Tool-Star, RL-Factory, calculator_agent_rl, ReTool, ToolRL, AWorld, Agent-R1, ReCall.

### AgenticQwen
- `https://github.com/haruhi-sudo/data_synth_and_rl` · org: Alibaba PAI · date: 2026.4
- Paper(s): [Paper](https://arxiv.org/abs/2604.21590)
- Algorithm: Multi-round RL (Reasoning RL + Agentic RL w/ dual data flywheels) · Framework: veRL (w/ EasyDistill) · Agent: Single · Turns: Multi · Tools: Yes (Python interpreter, web search, mock tools)
- Reward phase: Outcome · Reward type: Rule + Model (rubric)
- Task: Industrial Tool Use (search, data analysis, tau-bench airline/retail/telecom)

### ToolOrchestra
- `https://github.com/NVlabs/ToolOrchestra` · org: NVIDIA / HKU · date: 2025.11
- Paper(s): [Paper](https://arxiv.org/abs/2511.21689)
- Algorithm: End-to-end RL (outcome+efficiency+preference) · Framework: Custom (veRL-based) · Agent: Single · Turns: Multi · Tools: Yes (Search/Code/LLMs)
- Reward phase: Both · Reward type: All
- Task: Tool orchestration / agentic workflows

### ToolMaster
- `https://github.com/NEUIR/ToolMaster` · org: Northeastern University (NEUIR) · date: 2026.1
- Paper(s): [Paper](https://arxiv.org/abs/2601.12762)
- Algorithm: SFT + GRPO (trial-then-execute) · Framework: Custom · Agent: Single · Turns: Multi · Tools: Yes (Simulated tools)
- Reward phase: Outcome · Reward type: Rule/External
- Task: Tool trialing + execution (ToolHop/TMDB/StableToolBench)

### MATPO
- `https://github.com/mzf666/MATPO` · org: MiroMind AI · date: 2025.10
- Paper(s): [Paper](https://arxiv.org/abs/2510.04678)
- Algorithm: GRPO (multi-agent) · Framework: Custom · Agent: Multi · Turns: Multi · Tools: Yes (MCP: Serper, Web scraping)
- Reward phase: Outcome · Reward type: Rule
- Task: Tool-use/Search

### CodeGym
- `https://github.com/StigLidu/CodeGym` · org: Academic · date: 2025.9
- Paper(s): [Paper](https://arxiv.org/abs/2509.17325)
- Algorithm: GRPO-family · Framework: Custom · Agent: Single · Turns: Multi · Tools: Yes (Synthesized tools)
- Reward phase: Outcome · Reward type: Rule (verifiable)
- Task: Synthetic Multi-turn Tool-Use

### UserRL
- `https://github.com/SalesforceAIResearch/UserRL` · org: Salesforce AI Research · date: 2025.9
- Paper(s): [Paper](https://arxiv.org/abs/2509.19736)
- Algorithm: GRPO (multi-turn credit) · Framework: veRL · Agent: Single · Turns: Multi · Tools: Yes
- Reward phase: Both · Reward type: Model/External
- Task: User-centric (Function/Persuade/Search/Tau Gyms)

### ToolBrain
- `https://github.com/ToolBrain/ToolBrain` · org: ToolBrain (AAMAS 2026) · date: 2025.10
- Paper(s): [Paper](https://arxiv.org/abs/2510.00023)
- Algorithm: GRPO/DPO · Framework: Custom · Agent: Single · Turns: Multi · Tools: Yes (User-defined tools)
- Reward phase: Outcome · Reward type: Rule/Model
- Task: Agentic tool training

### Tool-R1
- `https://github.com/YBYBZhang/Tool-R1` · org: Individual (YBYBZhang) · date: 2025.9
- Paper(s): [Paper](https://arxiv.org/abs/2509.12867)
- Algorithm: Policy optimization (PPO-style) · Framework: Custom · Agent: Single · Turns: Multi · Tools: Yes (Python exec)
- Reward phase: Outcome · Reward type: Model + External
- Task: Agentic Tool Use (GAIA)

### MiroRL
- `https://github.com/MiroMindAI/MiroRL` · org: MiroMindAI · date: 2025.8
- Paper(s): [HF Repo](https://huggingface.co/miromind-ai)
- Algorithm: GRPO · Framework: veRL · Agent: Single · Turns: Multi · Tools: MCP
- Reward phase: Both · Reward type: Rule-based
- Task: Reasoning/Planning/ToolUse

### verl-tool
- `https://github.com/TIGER-AI-Lab/verl-tool` · org: TIGER-Lab · date: 2025.6
- Paper(s): [X](https://x.com/DongfuJiang/status/1929198238017720379)
- Algorithm: PPO/GRPO · Framework: veRL · Agent: Single · Turns: Both · Tools: Yes
- Reward phase: Both · Reward type: Rule/External
- Task: Math/Code

### Multi-Turn-RL-Agent
- `https://github.com/SiliangZeng/Multi-Turn-RL-Agent` · org: University of Minnesota · date: 2025.5
- Paper(s): [Paper](https://arxiv.org/abs/2505.11821)
- Algorithm: GRPO · Framework: Custom · Agent: Single · Turns: Multi · Tools: Yes
- Reward phase: Both · Reward type: Rule/External
- Task: Tool-use/Math

### Tool-N1
- `https://github.com/NVlabs/Tool-N1` · org: NVIDIA · date: 2025.5
- Paper(s): [Paper](https://arxiv.org/abs/2505.00024)
- Algorithm: PPO · Framework: veRL · Agent: Single · Turns: Multi · Tools: Yes
- Reward phase: Outcome · Reward type: All
- Task: Math/Dialogue

### Tool-Star
- `https://github.com/dongguanting/Tool-Star` · org: RUC · date: 2025.5
- Paper(s): [Paper](https://arxiv.org/abs/2505.16410)
- Algorithm: PPO/DPO/ORPO/SimPO/KTO · Framework: LLaMA-Factory · Agent: Single · Turns: Multi · Tools: Yes
- Reward phase: Outcome · Reward type: Model/External
- Task: Multi-modal/Tool Use/Dialogue

### RL-Factory
- `https://github.com/Simple-Efficient/RL-Factory` · org: Simple-Efficient · date: 2025.5
- Paper(s): [model](https://huggingface.co/Simple-Efficient/RLFactory-Qwen3-8B-GRPO)
- Algorithm: GRPO · Framework: veRL · Agent: Multi · Turns: Multi · Tools: MCP
- Reward phase: Both · Reward type: All
- Task: Tool-use/NL2SQL

### calculator_agent_rl
- `https://github.com/Danau5tin/calculator_agent_rl` · org: Individual (Danau5tin) · date: 2025.5
- Paper(s): —
- Algorithm: GRPO · Framework: Verifiers · Agent: Single · Turns: Multi · Tools: Yes
- Reward phase: Outcome · Reward type: Model (Claude-judge)
- Task: Calculator Tool Use

### ReTool
- `https://github.com/ReTool-RL/ReTool` · org: ByteDance · date: 2025.4
- Paper(s): [Paper](https://arxiv.org/abs/2504.11536)
- Algorithm: PPO · Framework: veRL · Agent: Single · Turns: Multi · Tools: Code
- Reward phase: Outcome · Reward type: External
- Task: Math

### ToolRL
- `https://github.com/qiancheng0/ToolRL` · org: UIUC · date: 2025.4
- Paper(s): [Paper](https://arxiv.org/abs/2504.13958)
- Algorithm: GRPO/PPO · Framework: veRL · Agent: Single · Turns: Multi · Tools: Yes
- Reward phase: Outcome · Reward type: Rule/External
- Task: Tool Learning

### AWorld
- `https://github.com/inclusionAI/AWorld` · org: Ant Group (inclusionAI) · date: 2025.8
- Paper(s): [Paper](https://arxiv.org/abs/2508.20404)
- Algorithm: GRPO · Framework: veRL · Agent: Both · Turns: Multi · Tools: Yes
- Reward phase: Outcome · Reward type: External/Rule
- Task: Search/Web/Code

### Agent-R1
- `https://github.com/0russwest0/Agent-R1` · org: USTC · date: 2025.11
- Paper(s): [Paper](https://arxiv.org/abs/2511.14460)
- Algorithm: PPO/GRPO · Framework: veRL · Agent: Single · Turns: Multi · Tools: Yes
- Reward phase: Both · Reward type: Model
- Task: Tool-use/QA

### ReCall
- `https://github.com/Agent-RL/ReCall` · org: BaiChuan · date: 2025.3
- Paper(s): [Paper](https://arxiv.org/abs/2503.19470)
- Algorithm: PPO/GRPO/RLOO/REINFORCE++/ReMax · Framework: veRL · Agent: Single · Turns: Multi · Tools: Yes
- Reward phase: Outcome · Reward type: All
- Task: Tool-use/Math/QA
