# Problem: what baseline to compare against — and how to make it strong

## The reviewer will ask

"Why didn't you compare against X?" Where X is the strongest published
work on your benchmark.

If you can't show numbers vs X (that you ran yourself or X reported),
your contribution can't be evaluated.

## What "strong baseline" means

- **Strongest reasonable** open-source method on your benchmark.
- **Same compute budget** as your method.
- **Same data** as your method (when possible).
- **Re-tuned for your evaluation**, not their reported number from a
  different setup.

## What weak baselines look like

- Your reimplementation of "GRPO" without their tricks.
- A pre-trained model with no SFT.
- A model 10x smaller than your method.
- An old paper from 2023 when the field has moved.

## How to find the right baseline in this corpus

### Step 1: identify your task family

Common families in this corpus:

- Math/reasoning TIR
- Search / RAG
- Web/GUI
- SWE / code
- Tool-use / MCP
- Multi-agent
- Long-horizon deep research

### Step 2: pick top-of-leaderboard from that family

Look at `references/<family>.md`. Pick:

- **High stars** (community vetting).
- **Recent date** (within last 6 months ideally).
- **Same benchmark target** (otherwise it's not directly comparable).

### Step 3: verify it's reproducible

Many papers report numbers that aren't reproducible. Check:

- Is code released?
- Is recipe documented?
- Are wandb logs public? (Search-R1 publishes them — best-in-class.)

If not reproducible, you may need to use their reported number with a
caveat ("from original paper").

## Examples by family

### Math/reasoning TIR baseline

> **ARPO** — github: `https://github.com/dongguanting/ARPO`,
> paper: `https://arxiv.org/abs/2507.19849`, RUC/Kuaishou, date: 2025.7.

> **Tool-N1** — github: `https://github.com/NVlabs/Tool-N1`,
> paper: `https://arxiv.org/abs/2505.00024`, NVIDIA, date: 2025.5.

> **THOR** — github: `https://github.com/JingMog/THOR`,
> paper: `https://arxiv.org/abs/2509.13761`, date: 2025.9.

### Search/RAG baseline

> **Search-R1** —
> github: `https://github.com/PeterGriffinJin/Search-R1`,
> papers: `https://arxiv.org/abs/2503.09516`,
> `https://arxiv.org/abs/2505.15117`, UIUC/Google, date: 2025.3.

> **R1-Searcher** —
> github: `https://github.com/RUCAIBox/R1-Searcher`,
> paper: `https://arxiv.org/abs/2503.05592`, RUC, date: 2025.3.

> **IGPO** — github: `https://github.com/GuoqingWang1/IGPO`,
> paper: `https://arxiv.org/abs/2510.14967`, Ant Group, date: 2025.10.

### Web/GUI baseline

> **UI-TARS** — github: `https://github.com/bytedance/UI-TARS`,
> papers: `https://arxiv.org/abs/2501.12326`,
> `https://arxiv.org/abs/2509.02544`, ByteDance Seed.

> **GUI-Libra** — github: `https://github.com/GUI-Libra/GUI-Libra`,
> paper: `https://arxiv.org/abs/2602.22190`, date: 2026.2.

### SWE baseline

> **SWE-Swiss** — github: `https://github.com/zhenyuhe00/SWE-Swiss`.
> SOTA-tier 60.2% on SWE-Bench Verified.

> **SkyRL-Agent** — github: `https://github.com/NovaSky-AI/SkyRL`,
> paper: `https://arxiv.org/abs/2511.16108`, date: 2025.7.

### Tool-use baseline

> **ReTool** — github: `https://github.com/ReTool-RL/ReTool`,
> paper: `https://arxiv.org/abs/2504.11536`, ByteDance, date: 2025.4.

> **Tool-Star** — github: `https://github.com/dongguanting/Tool-Star`,
> paper: `https://arxiv.org/abs/2505.16410`, RUC, date: 2025.5.

### Multi-agent baseline

> **SPIRAL** — github: `https://github.com/spiral-rl/spiral`,
> paper: `https://arxiv.org/abs/2506.24119`, date: 2025.6.

> **MARFT** — github: `https://github.com/jwliao-ai/MARFT`,
> paper: `https://arxiv.org/abs/2504.16129`, date: 2025.4.

### Deep research baseline

> **DR-Venus** — github: `https://github.com/inclusionAI/DR-Venus`,
> paper: `https://arxiv.org/abs/2604.19859`, date: 2026.4.

> **DeepResearch (Tongyi)** — github:
> `https://github.com/Alibaba-NLP/DeepResearch`,
> paper: `https://arxiv.org/abs/2510.24701`, date: 2025.10.

## Reproducing the baseline

Most baselines need re-tuning to your data scale, model size, eval
protocol. Don't trust default config.

If reproduction is too expensive, at minimum cite their reported
number on the same benchmark and note the config gap.

## When to skip a baseline

- It doesn't apply to your task family (e.g. don't compare a search
  method to a code method).
- It's pre-DeepSeek-R1 and the field has moved.
- The original paper is closed-source and reproducing requires major
  engineering.

But in your paper, **say why you skipped**. Reviewers ask.

## See also

- `references/<your-task-family>.md` — full table.
- `reproducing-papers.md`.
