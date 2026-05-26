# Problem: generating / curating training data for agentic RL

## What "training data" means

For agentic RL, you have *two* data layers:

1. **Prompts / tasks** — what the agent has to solve.
2. **SFT trajectories** — example multi-turn traces showing how to
   solve them.

Both need curation.

## Sources of prompts

### Existing benchmarks (with care for contamination)

- HotpotQA, NaturalQuestions for search.
- GSM8K, MATH for math.
- SWE-bench (training partition: SWE-Gym).
- ALFWorld, WebShop for embodied.

### Distill from a stronger teacher

Use GPT-4 / Claude to solve tasks; filter to high-quality completions.

### Synthetic generation

> **CodeGym** — github: `https://github.com/StigLidu/CodeGym`,
> paper: `https://arxiv.org/abs/2509.17325`. Synthetic multi-turn
> tool-use data.

> **SWE-smith** — github: `https://github.com/SWE-bench/SWE-smith`,
> Princeton/Stanford, date: 2025.4. Programmatic SWE training data.

> **MCP-Bench / MCPVerse** as task generators.

### Self-evolved (challenger generates problems)

> **R-Zero** — github: `https://github.com/Chengsong-Huang/R-Zero`,
> paper: `https://arxiv.org/abs/2508.05004`, date: 2025.8.

> **Absolute-Zero-Reasoner** — github:
> `https://github.com/LeapLabTHU/Absolute-Zero-Reasoner`,
> paper: `https://arxiv.org/abs/2505.03335`, date: 2025.5.

## Sources of SFT trajectories

### Distill from teacher

GPT-4 solves task; record full trajectory; SFT on it.

### Filter from earlier policy rollouts

Run weak policy on prompts; keep only successful trajectories. SFT on
those.

### Bootstrap from RFT (Rejection-sampling Fine-Tuning)

> **Mano-P** — github: `https://github.com/Mininglamp-AI/Mano-P`,
> paper: `https://arxiv.org/abs/2509.17336`, date: 2025.9. Three-stage
> SFT → Offline RL → Online RL.

> **MobileRL** — github: `https://github.com/THUDM/MobileRL`,
> paper: `https://arxiv.org/abs/2509.18119`, date: 2025.9. Same pattern.

## Data quality > quantity

Common pitfall: scraping huge SFT corpora. The corpus's pattern is
**curation > scale**.

> **Tool-Star** — github: `https://github.com/dongguanting/Tool-Star`,
> paper: `https://arxiv.org/abs/2505.16410`, date: 2025.5. Multi-stage
> SFT with carefully filtered data.

> **MedResearcher-R1** — github:
> `https://github.com/AQ-MedAI/MedResearcher-R1`,
> paper: `https://arxiv.org/abs/2508.14880`, date: 2025.8. Curated
> medical browse-comp prompts.

## Filtering SFT trajectories

### Filter 1: outcome-correct

Drop trajectories that didn't solve the task.

### Filter 2: format-clean

Drop trajectories with malformed tool calls or missing tags.

### Filter 3: diverse

Avoid duplicate or near-duplicate trajectories. SFT on 10k unique > 100k
near-duplicates.

### Filter 4: difficulty-appropriate

If too many examples are trivial, the model won't learn the hard
behaviors.

## Filtering prompts for RL

### Filter 1: learnable (not all-pass, not all-fail)

Track per-prompt success rate during training. Drop prompts in the
extremes.

> **Absolute-Zero-Reasoner** — learnability-weighted training.
> **R-Zero** — challenger generates progressively harder.

### Filter 2: contamination check

Decontaminate against eval set. N-gram overlap > 8 = drop.

### Filter 3: license / safety

Especially when distilling from a teacher.

## Data scale heuristics

For agentic RL:

- **Cold-start SFT**: 1k–10k high-quality trajectories. More if base
  model is weaker.
- **RL prompts**: 10k–100k diverse prompts. Larger = more exploration.
- **Held-out eval**: 200–1000 prompts (see
  `../evaluation/statistical-significance.md`).

## Paper / repo references

(All cited above.)

**Other corpus entries:**

- `SPEAR` — GRPO/GiGPO + Self-Imitation Learning (SIL) for math/agent — illustrates data-augmentation via successful traces.
  github: `https://github.com/TencentYoutuResearch/SPEAR`, paper: `https://arxiv.org/abs/2509.22601`, Tencent Youtu Lab, date: 2025.9

- `LLM-in-Sandbox` — GRPO++ across 7 domains (math/physics/chemistry/biomedicine/long-context/IF/SWE) — multi-domain curation pattern.
  github: `https://github.com/llm-in-sandbox/llm-in-sandbox`, paper: `https://huggingface.co/papers/2601.16206`, RUC/MSRA/THU, date: 2026.1

- `OpenManus-RL` — PPO/DPO/GRPO across text-game corpus.
  github: `https://github.com/OpenManus/OpenManus-RL`, UIUC/MetaGPT, date: 2025.3

- `ART` — OpenPipe's GRPO for text-game with full reward stack.
  github: `https://github.com/OpenPipe/ART`, OpenPipe, date: 2025.3

- `SPA-RL-Agent` — PPO with model reward for navigation/web/text-game.
  github: `https://github.com/WangHanLinHenry/SPA-RL-Agent`, paper: `https://arxiv.org/abs/2505.20732`, PolyU, date: 2025.5

- `digitalhuman` — PPO/GRPO/ReMax/RLOO across empathy/math/code/multimodal.
  github: `https://github.com/Tencent/digitalhuman`, paper: `https://arxiv.org/abs/2507.03112`, Tencent, date: 2025.7

- `enterprise-deep-research` — Salesforce deep research env — illustrates curated enterprise-research data.
  github: `https://github.com/SalesforceAIResearch/enterprise-deep-research`, Salesforce AI Research, date: 2025.9

- `Simia-Agent-Training` — synthetic agent training data via tool-use simulation.
  github: `https://github.com/microsoft/Simia-Agent-Training`, Microsoft, date: 2025.10
