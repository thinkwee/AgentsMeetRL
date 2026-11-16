# Memory Agents

Agents that learn to manage persistent memory beyond a fixed context window.

_Total: 10 entries._

### MemPilot
- **Idea:** An RL-trained orchestrator decides which multimodal memory actions to take, with a resource-aware reward over answer quality, cost and latency.
- `https://github.com/ViktorAxelsen/MemPilot` · org: NTU / THU / UIUC · date: 2026.10
- Paper(s): [Paper](https://arxiv.org/abs/2610.06830)
- Algorithm: GDPO/GRPO (resource-aware) · Framework: veRL · Agent: Single · Turns: Multi · Tools: Yes (memory-access tools)
- Reward phase: Outcome · Reward type: Model/Rule (quality, cost, latency)
- Task: On-demand multimodal memory curation/orchestration

### AMBER
- **Idea:** Keeps an append-only memory of browser evidence across steps and compares it against overwrite (MEM1-style) and reasoning-only memory under identical RL on WebArena.
- `https://github.com/agentic-foundation-modeling-research/amber` · org: Academic · date: 2026.10
- Paper(s): [Paper](https://arxiv.org/abs/2610.07118)
- Algorithm: GRPO (after SFT) · Framework: Miles · Agent: Single · Turns: Multi · Tools: Yes (browser)
- Reward phase: Outcome · Reward type: External Verifier (WebArena)
- Task: Long-horizon WebArena agents with append-only browser-evidence memory

### MemPrism
- **Idea:** Makes memory composition itself the action space — a policy picks relation/window/granularity to build a task-conditioned view — so memory is trained by RL rather than fixed retrieval heuristics.
- `https://github.com/Feld-maxiu/MemPrism` · org: Academic · date: 2026.8
- Paper(s): [Paper](https://arxiv.org/abs/2608.06745)
- Algorithm: GRPO/GiGPO · Framework: veRL (GiGPO extension) · Agent: Single · Turns: Multi · Tools: Yes (memory-view action + env actions)
- Reward phase: Both · Reward type: Rule-Based
- Task: Memory-view selection for ALFWorld/ALFRED + Mind2Web

### Supersede
- **Idea:** Isolates the memory-update gap - agents citing superseded facts - as a verifiable RL task, rewarding current answers and penalizing stale ones across multi-session notes.
- `https://github.com/Vrin-cloud/supersede` · org: Vrin · date: 2026.6
- Paper(s): [Paper](https://arxiv.org/abs/2606.27472)
- Algorithm: GRPO (+ LoRA) · Framework: verifiers + prime-rl · Agent: Single · Turns: Multi · Tools: Yes (capped notes memory as action space)
- Reward phase: Outcome · Reward type: Rule-Based (answered_current / stale_penalty)
- Task: Memory-update gap: keeping notes current across sessions (LongMemEval knowledge-update)

### AgeMem
- **Idea:** Exposes store/retrieve/update/summarize/discard as tool actions in the agent's policy, trained with step-wise GRPO to handle sparse memory-op rewards.
- `https://github.com/y1y5/AgeMem` · org: Multi-institution (incl. Alibaba DAMO) · date: 2026.1
- Paper(s): [Paper](https://arxiv.org/abs/2601.01885)
- Algorithm: Step-wise GRPO (3-stage progressive RL) · Framework: Trinity-RFT · Agent: Single · Turns: Multi · Tools: Yes (store/retrieve/update/summarize/discard memory tools)
- Reward phase: Process · Reward type: Rule (task accuracy + memory quality)
- Task: Unified LTM/STM management (memory ops as tools)

### Mem-alpha
- **Idea:** RL teaches agents what to store, how to structure, and when to update memory, optimized via downstream QA reward instead of fixed memory heuristics.
- `https://github.com/wangyu-ustc/Mem-alpha` · org: UCSD / USTC · date: 2025.9
- Paper(s): [Paper](https://arxiv.org/abs/2509.25911)
- Algorithm: GRPO · Framework: veRL · Agent: Single · Turns: Multi · Tools: Yes (memory tools)
- Reward phase: Outcome · Reward type: Rule (downstream QA)
- Task: Long-context QA + Memory Construction

### MEM1
- **Idea:** Maintains a constant-size shared internal state that consolidates memory and reasoning, discarding irrelevant context for efficient long-horizon agents.
- `https://github.com/MIT-MI/MEM1` · org: MIT · date: 2025.6
- Paper(s): [Paper](https://arxiv.org/abs/2506.15841)
- Algorithm: PPO/GRPO · Framework: veRL (based on Search-R1) · Agent: Single · Turns: Multi · Tools: Yes
- Reward phase: Outcome · Reward type: Rule/Model
- Task: WebShop/GSM8K/QA

### M3-Agent
- **Idea:** Builds entity-centric multimodal episodic and semantic memory from streaming audio-visual input, retrieved during multi-turn reasoning for long-video QA.
- `https://github.com/bytedance-seed/m3-agent` · org: ByteDance Seed / Zhejiang University · date: 2025.8
- Paper(s): [Paper](https://arxiv.org/abs/2508.09736)
- Algorithm: RL-based · Framework: Custom · Agent: Single · Turns: Multi · Tools: Yes (multimodal memory graph)
- Reward phase: Outcome · Reward type: Rule/Model
- Task: Long-video QA (M3-Bench)

### Memento
- **Idea:** Memory-augmented MDP that adapts via episodic case retrieval and a learned case-selection policy, with no gradient updates to the underlying LLM.
- `https://github.com/Agent-on-the-Fly/Memento` · org: UCL, Huawei · date: 2025.8
- Paper(s): [Paper](https://arxiv.org/abs/2508.16153)
- Algorithm: soft Q-Learning · Framework: Custom · Agent: Single · Turns: Multi · Tools: Yes
- Reward phase: Outcome · Reward type: External/Rule
- Task: Research/QA/Code/Web

### MemAgent
- **Idea:** RL-trains an overwrite-based segment memory (DAPO extended to multi-conversation generation), extrapolating from 8K to 3.5M tokens with little degradation.
- `https://github.com/BytedTsinghua-SIA/MemAgent` · org: Bytedance, Tsinghua-SIA · date: 2025.7
- Paper(s): [Paper](https://arxiv.org/abs/2507.02259)
- Algorithm: PPO, GRPO, DPO · Framework: veRL · Agent: Multi · Turns: Multi · Tools: Yes
- Reward phase: Outcome · Reward type: Rule/Model/External
- Task: Long-context QA
