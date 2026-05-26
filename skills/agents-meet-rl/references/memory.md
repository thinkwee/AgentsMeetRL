# Memory Agents

Agents that learn to manage persistent memory beyond a fixed context window.

_Total: 6 entries._

### AgeMem
- `https://github.com/y1y5/AgeMem` · org: Multi-institution (incl. Alibaba DAMO) · date: 2026.1
- Paper(s): [Paper](https://arxiv.org/abs/2601.01885)
- Algorithm: Step-wise GRPO (3-stage progressive RL) · Framework: Trinity-RFT · Agent: Single · Turns: Multi · Tools: Yes (store/retrieve/update/summarize/discard memory tools)
- Reward phase: Process · Reward type: Rule (task accuracy + memory quality)
- Task: Unified LTM/STM management (memory ops as tools)

### Mem-alpha
- `https://github.com/wangyu-ustc/Mem-alpha` · org: UCSD / USTC · date: 2025.9
- Paper(s): [Paper](https://arxiv.org/abs/2509.25911)
- Algorithm: GRPO · Framework: veRL · Agent: Single · Turns: Multi · Tools: Yes (memory tools)
- Reward phase: Outcome · Reward type: Rule (downstream QA)
- Task: Long-context QA + Memory Construction

### MEM1
- `https://github.com/MIT-MI/MEM1` · org: MIT · date: 2025.6
- Paper(s): [Paper](https://arxiv.org/abs/2506.15841)
- Algorithm: PPO/GRPO · Framework: veRL (based on Search-R1) · Agent: Single · Turns: Multi · Tools: Yes
- Reward phase: Outcome · Reward type: Rule/Model
- Task: WebShop/GSM8K/QA

### M3-Agent
- `https://github.com/bytedance-seed/m3-agent` · org: ByteDance Seed / Zhejiang University · date: 2025.8
- Paper(s): [Paper](https://arxiv.org/abs/2508.09736)
- Algorithm: RL-based · Framework: Custom · Agent: Single · Turns: Multi · Tools: Yes (multimodal memory graph)
- Reward phase: Outcome · Reward type: Rule/Model
- Task: Long-video QA (M3-Bench)

### Memento
- `https://github.com/Agent-on-the-Fly/Memento` · org: UCL, Huawei · date: 2025.8
- Paper(s): [Paper](https://arxiv.org/abs/2508.16153)
- Algorithm: soft Q-Learning · Framework: Custom · Agent: Single · Turns: Multi · Tools: Yes
- Reward phase: Outcome · Reward type: External/Rule
- Task: Research/QA/Code/Web

### MemAgent
- `https://github.com/BytedTsinghua-SIA/MemAgent` · org: Bytedance, Tsinghua-SIA · date: 2025.7
- Paper(s): [Paper](https://arxiv.org/abs/2507.02259)
- Algorithm: PPO, GRPO, DPO · Framework: veRL · Agent: Multi · Turns: Multi · Tools: Yes
- Reward phase: Outcome · Reward type: Rule/Model/External
- Task: Long-context QA
