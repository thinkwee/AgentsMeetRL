# Problem: how to evaluate multi-agent systems

## Why this is hard

- Win-rate vs other agents has the rock-paper-scissors problem.
- Joint-task success doesn't tell you per-agent contribution.
- Per-agent metrics may be uncorrelated with system success.

## Patterns

### Win-rate vs *fixed* baseline

For self-play: maintain a fixed reference opponent. Track win-rate vs
that fixed opponent over training. If it grows monotonically, real
progress.

> **SPIRAL** — github: `https://github.com/spiral-rl/spiral`,
> paper: `https://arxiv.org/abs/2506.24119`, NUS/A*STAR/Sea AI, date: 2025.6.
> 1) Win rate against fixed opponent on training game.
> 2) Win rate against fixed opponent on OOD game.
> 3) Math reasoning accuracy (transfer).

### Joint task success + per-agent metrics

For collaborative MAS: report both joint and per-agent.

> **MrlX** — github: `https://github.com/AQ-MedAI/MrlX`,
> paper: `https://arxiv.org/abs/2511.13288`, Ant Group, date: 2025.11.
> GAIA / XBench joint, plus per-agent specialization.

### Tournament eval

For a fleet of agents, run tournament (round-robin or Swiss). Get
relative ranking.

### Evaluate transfer to single-agent

Self-play / multi-agent training often produces a model that's better
at single-agent reasoning. Test on standard math/code benchmarks.

> **SPIRAL** reports math reasoning gains from zero-sum self-play.
> **R-Zero** — github: `https://github.com/Chengsong-Huang/R-Zero`,
> paper: `https://arxiv.org/abs/2508.05004`. Solver evaluated on Math/
> SuperGPQA/MMLU-Pro/BBEH.
> **Absolute-Zero-Reasoner** — paper:
> `https://arxiv.org/abs/2505.03335`. Code/Math benchmarks.

### Cooperative game

For cooperative tasks (planning + coding), evaluate end-to-end
deliverable, not individual agent quality.

## Pitfalls

### Pitfall 1: only evaluating against current snapshot

Always evaluate against fixed reference for trend.

### Pitfall 2: ignoring transfer

Multi-agent that works on training game but doesn't transfer is rarely
publishable. Always include OOD eval.

### Pitfall 3: per-agent metric divergent from system success

If planner accuracy goes up but task success goes down, your metric is
wrong.

## Paper / repo references

- `SPIRAL` — github: `https://github.com/spiral-rl/spiral`,
  paper: `https://arxiv.org/abs/2506.24119`, date: 2025.6.
- `R-Zero` — github: `https://github.com/Chengsong-Huang/R-Zero`,
  paper: `https://arxiv.org/abs/2508.05004`, date: 2025.8.
- `Absolute-Zero-Reasoner` — github:
  `https://github.com/LeapLabTHU/Absolute-Zero-Reasoner`,
  paper: `https://arxiv.org/abs/2505.03335`, date: 2025.5.
- `MrlX` — github: `https://github.com/AQ-MedAI/MrlX`,
  paper: `https://arxiv.org/abs/2511.13288`, date: 2025.11.

**Other corpus entries:**

- `meta-agents-research-environments` — Gaia2 / multi-universe — multi-agent eval framework.
  github: `https://github.com/facebookresearch/meta-agents-research-environments`, Meta (FAIR), date: 2025.9
