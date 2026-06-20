# References Index

Per-category catalogues parsed from the AgentsMeetRL awesome list
(`README.md` at the project root). Each entry includes GitHub URL,
arXiv URL, RL algorithm, framework, reward design, and turn mode so
Claude can cite specific work when giving recommendations — plus an
**`Idea:`** line distilling that project's distinctive contribution
(grounded in its paper/repo), so even projects not covered by a
`problems/` file still carry a usable one-line takeaway. In
`under-review.md` the same content is the table's `Idea` column.

**When to read which file:**

| Category | File | Count | Use When |
|---|---|---|---|
| Base Frameworks | [base-frameworks.md](base-frameworks.md) | 23 | RL training frameworks for LLM agents (e.g. veRL, OpenRLHF, slime). Pick one as the base of your training stack. |
| General / MultiTask Agents | [general-multitask.md](general-multitask.md) | 21 | Agents trained across many tasks/environments. Useful when you want one model that handles search + tool + code etc. |
| Search & RAG Agents | [search-rag.md](search-rag.md) | 45 | Agents that interleave reasoning and retrieval. Most use rule-based EM/F1 outcome rewards or info-gain process rewards. |
| Web & GUI Agents | [web-gui.md](web-gui.md) | 31 | Agents that drive browsers, mobile UIs, or desktop OSes. Grounding accuracy and long-horizon planning dominate. |
| Tool-Use Agents | [tool-use.md](tool-use.md) | 23 | Agents that call external APIs/MCP/code interpreters. Reward usually mixes correctness + format + tool-call validity. |
| Code & SWE Agents | [code-swe.md](code-swe.md) | 24 | Software-engineering agents that locate, repair, and test. Most use SWE-bench-style verifiable rewards. |
| Reasoning Agents | [reasoning.md](reasoning.md) | 18 | Tool-integrated reasoning (TIR) agents — math/QA + search/code. Common starting point for new agentic-RL projects. |
| Multi-Agent RL | [multi-agent.md](multi-agent.md) | 14 | Multi-agent collaboration, negotiation, or self-play. Watch for credit assignment and role-conditioned advantage. |
| Memory Agents | [memory.md](memory.md) | 6 | Agents that learn to manage persistent memory beyond a fixed context window. |
| Embodied Agents | [embodied.md](embodied.md) | 6 | Agents in physical/simulated robotic environments. |
| Domain-Specific Agents | [domain-specific.md](domain-specific.md) | 11 | Specialized verticals: medical, legal, finance, OS tuning. Reward usually mixes domain rules + LLM-judge. |
| Reward Models & Training Methodology | [reward-training.md](reward-training.md) | 10 | Process/outcome reward models, PRM benchmarks, training recipes. |
| Safety / Red-Teaming | [safety.md](safety.md) | 9 | RL for jailbreak attack/defense, tool-call safety, agent guardrails. |
| VLM Agents | [vlm-agent.md](vlm-agent.md) | 27 | Vision-language model agents (visual tool-use, chart QA, autonomous driving, image-based search). |
| Self-Evolution Agents | [self-evolution.md](self-evolution.md) | 13 | Agents that improve themselves through closed-loop feedback (challenger/solver, MCTS-driven self-training). |
| Environments / Benchmarks / Gyms | [environments.md](environments.md) | 53 | Sandbox environments and benchmarks. Pick one matching your task before designing rewards. |
| Under Review (Open-source pending) | [under-review.md](under-review.md) | 21 | Notable papers whose code is not yet open-source. Track these for future reference. |

## Citation conventions

When recommending a paper or repo from these references, **always cite the entry** in this form:

> `<Name>` (`<github_url>`, paper: `<arxiv_url>`, org: `<org>`, date: `<YYYY.MM>`) — <one-sentence why-relevant>.

Verify the URL still resolves before relying on it; the awesome list is a
snapshot and some repos may be archived or moved.

## When to switch to `problems/`

`references/` answers **which project / paper exists in this category**.
`problems/` answers **how to fix or design the thing once you've picked**.

| If references points you at... | The matching problem file is |
|---|---|
| Search agents (search-rag.md): Search-R1, R1-Searcher, ReSearch | `problems/training/reward-not-increasing.md`, `tool-call-parse-failures.md`, `search-hacking.md` |
| Tool agents (tool-use.md): ReTool, Tool-Star, Tool-N1 | `problems/training/tool-call-parse-failures.md`, `tool-api-design.md`, `reward-mixing.md` |
| SWE agents (code-swe.md): SWE-Gym, SWE-Swiss, swe-rl | `problems/training/code-swe-specific.md`, `sandbox-security.md`, `env-flakiness.md` |
| GUI / web agents (web-gui.md): UI-TARS, AgentNet | `problems/training/gui-specific.md`, `vlm-specific.md`, `observation-truncation.md` |
| Base frameworks (base-frameworks.md): veRL, OpenRLHF, slime, AReaL | `problems/training/algorithm-choice.md`, `grpo-knobs.md`, `ppo-knobs.md`, `rollout-throughput.md`, `oom-during-training.md` |
| General multitask (general-multitask.md): RAGEN, IGPO, GiGPO | `problems/training/training-collapse.md`, `entropy-collapse.md`, `credit-assignment-long-horizon.md` |
| Reasoning agents (reasoning.md): R1-distill, Skywork-OR1 | `problems/training/reasoning-mode-rl.md`, `rl-from-base.md`, `length-blowup.md` |
| Reward training (reward-training.md): PRM, AgentRM | `problems/training/prm-training.md`, `sparse-reward-credit.md` |
| Multi-agent (multi-agent.md) | `problems/training/multi-agent-credit-collapse.md`, `self-play-collapse.md`, `evaluation/multi-agent-eval.md` |
| Memory agents (memory.md): MemAgent | `problems/training/memory-context-overflow.md`, `conversation-history-truncation.md` |
| Environments / benchmarks (environments.md) | `problems/evaluation/benchmark-pitfalls.md`, `data-contamination.md`, `long-horizon-eval.md` |
| VLM agents (vlm-agent.md) | `problems/training/vlm-specific.md`, `gui-specific.md` |

Pick a project from `references/`, then jump to the problem file when
you hit a symptom.