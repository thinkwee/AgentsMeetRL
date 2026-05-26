# Problem: history exceeds context window after N turns

## Symptoms

- Agent runs fine for first N turns, then context overflows on turn N+1.
- Truncating earlier turns silently loses information; agent makes
  decisions inconsistent with earlier observations.
- Especially common in: deep research (50+ turns), long-form coding
  (repo-scale SWE), multi-step GUI sessions.

## Root causes

1. **Token-stream rollout** that concatenates everything into one
   growing prompt. Hits hard context cap.
2. **Tool outputs are huge** (100KB HTML, large JSON, file contents).
3. **No memory abstraction** — every observation is a "new fact" added
   to the prompt.
4. **Truncation strategy is naive** (drop oldest, drop random).

## Diagnosis

- Log per-rollout `total_input_tokens` and `total_response_tokens`. If
  > 80% of context cap, you'll overflow soon.
- Log per-turn observation length. Tail (p95) tells you which tools are
  the offenders.
- Histogram episodes by termination reason: "completed", "max_turns",
  "context_overflow". Should be mostly "completed".

## Fixes

### Fix 1: step-based rollout with explicit memory management

Stop concatenating raw tokens. Use a step abstraction where each step
carries (prompt, response) and you decide *between steps* what to
preserve.

> **verl-agent** — github: `https://github.com/langfengQ/verl-agent`,
> paper: `https://arxiv.org/abs/2505.10978`, NTU/Skywork, date: 2025.5
> (NeurIPS 2025).

> "Step-independent multi-turn rollout" with customizable history mgmt.

> **Agent-R1** — github: `https://github.com/0russwest0/Agent-R1`,
> paper: `https://arxiv.org/abs/2511.14460`, org: USTC, date: 2025.11.
> Step-level MDP allows per-step **truncation, summarization,
> rewriting, augmentation**.

### Fix 2: trained memory module (MemAgent / MEM1 / Mem-alpha)

Train the model to compress past observations into a memory token.

> **MemAgent** — github: `https://github.com/BytedTsinghua-SIA/MemAgent`,
> paper: `https://arxiv.org/abs/2507.02259`, ByteDance/Tsinghua, date: 2025.7.
> Multi-conv RL: chain context-independent conversations through a
> memory token. Trained on 8K context, generalizes to 3.5M tokens.

> **MEM1** — github: `https://github.com/MIT-MI/MEM1`,
> paper: `https://arxiv.org/abs/2506.15841`, MIT, date: 2025.6. PPO/GRPO
> on WebShop/GSM8K/QA. Built on Search-R1.

> **Mem-alpha** — github: `https://github.com/wangyu-ustc/Mem-alpha`,
> paper: `https://arxiv.org/abs/2509.25911`, UCSD/USTC, date: 2025.9.
> GRPO with downstream-QA reward; learns memory construction.

> **Memento** — github: `https://github.com/Agent-on-the-Fly/Memento`,
> paper: `https://arxiv.org/abs/2508.16153`, UCL/Huawei, date: 2025.8.
> Soft Q-Learning over memory.

> **M3-Agent** — github: `https://github.com/bytedance-seed/m3-agent`,
> paper: `https://arxiv.org/abs/2508.09736`, ByteDance Seed, date: 2025.8.
> Long-video QA with multimodal memory graph.

> **MemSearcher** — github: `https://github.com/icip-cas/MemSearcher`,
> paper: `https://arxiv.org/abs/2511.02805`, CAS, date: 2025.11.
> Multi-context GRPO + memory.

### Fix 3: tool-side filtering / summarization

Tool returns less, instead of agent forgetting more.

- **Search**: return top-k chunks instead of raw HTML; rerank.
- **Code**: return diff, not full file.
- **GUI**: return UI tree summary, not raw screenshot.

> **multimodal-search-r1** —
> github: `https://github.com/EvolvingLMMs-Lab/multimodal-search-r1`,
> paper: `https://arxiv.org/abs/2506.20670`, ByteDance/NTU, date: 2025.6.
> Returns top-k chunks for multimodal search.

### Fix 4: explicit summarization step

Insert a summarization turn every K steps. The agent compresses recent
history into a small note, then proceeds. Adds latency but keeps
context bounded.

> **DR-Venus** — github: `https://github.com/inclusionAI/DR-Venus`,
> paper: `https://arxiv.org/abs/2604.19859`, Ant Group, date: 2026.4.
> Edge-scale 4B deep research with 200+ turns. Uses summarization +
> IGPO.

> **Kimi-Researcher** — github:
> `https://github.com/moonshotai/Kimi-Researcher`,
> blog: `https://moonshotai.github.io/Kimi-Researcher/`, Moonshot,
> date: 2025.6. REINFORCE with summarization.

### Fix 5: pixel-level / region-level filtering for VLMs

For VLM agents, image tokens are expensive. Crop/zoom to relevant
regions.

> **Pixel-Reasoner** — github: `https://github.com/TIGER-AI-Lab/Pixel-Reasoner`,
> paper: `https://arxiv.org/abs/2505.15966`, Waterloo TIGER-Lab, date: 2025.5.
> Curiosity-driven GRPO with zoom/select-frame tools.

> **Mini-o3** — github: `https://github.com/Mini-o3/Mini-o3`,
> paper: `https://arxiv.org/abs/2509.07969`, date: 2025.9. Visual search
> with image cropping.

> **Chain-of-Focus** — github: `https://github.com/xtong-zhang/Chain-of-Focus`,
> paper: `https://arxiv.org/abs/2505.15436`, date: 2025.5. AGAR (GRPO)
> with zoom-in actions.

## Practical numbers

- **MemAgent**: 8K context training, 3.5M token tasks, < 5% perf loss.
- **DR-Venus 4B**: 200+ turn edge-scale deep research.
- **verl-agent + ALFWorld**: 50 steps per episode is the design point.

## Paper / repo references

(All listed above.)

**Other corpus entries:**

- `MemSkill` — PPO with learned-skill reward for QA/ALFWorld.
  github: `https://github.com/ViktorAxelsen/MemSkill`, paper: `https://arxiv.org/abs/2602.02474`, NTU/UIUC/UIC/Tsinghua, date: 2026.2

- `MemRL` — Q-value retrieval-based RL on HLE/BigCodeBench/ALFWorld.
  github: `https://github.com/MemTensor/MemRL`, paper: `https://arxiv.org/abs/2601.03192`, SJTU/Xidian/NUS/USTC/MemTensor, date: 2026.1

- `EvolveR` — GRPO closed-loop online+offline for multi-hop QA.
  github: `https://github.com/Edaizi/EvolveR`, paper: `https://arxiv.org/abs/2510.16079`, KnowledgeXLab / Shanghai AI Lab, date: 2025.10

- `WebRL` — Actor-Critic + outcome reward model for web navigation.
  github: `https://github.com/THUDM/WebRL`, paper: `https://arxiv.org/abs/2411.02337`, Tsinghua/Zhipu AI, date: 2024.11
