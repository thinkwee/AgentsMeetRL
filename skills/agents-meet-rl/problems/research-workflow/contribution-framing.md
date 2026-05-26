# Problem: novel algorithm vs engineering — when is the contribution worth a paper

## The honest taxonomy

### Tier 1: novel algorithm

A new method or principled extension. Examples from the corpus (each
with at least one paper or repo entry):

- **GiGPO** — github: `https://github.com/langfengQ/verl-agent`, paper:
  `https://arxiv.org/abs/2505.10978`, org: NTU, date: 2025.5.
  Hierarchical advantage for long-horizon agents.
- **IGPO** — github: `https://github.com/GuoqingWang1/IGPO`, paper:
  `https://arxiv.org/abs/2510.14967`, date: 2025.10. Info-gain reward
  as a turn-level signal.
- **StarPO** (in RAGEN) — github: `https://github.com/RAGEN-AI/RAGEN`,
  paper: `https://arxiv.org/abs/2504.20073`, date: 2025.4. Unified
  multi-turn agent RL framework.
- **RAE** (in SPIRAL) — github: `https://github.com/spiral-rl/spiral`,
  paper: `https://arxiv.org/abs/2506.24119`, date: 2025.6.
  Role-conditioned advantage for self-play.

These typically: 1 page of method, 5+ ablations, 3+ benchmarks, OOD
transfer.

### Tier 2: novel application / integration

Existing algorithms applied to a new domain or combination.

- **DoctorAgent-RL** — github:
  `https://github.com/JarvisUSTC/DoctorAgent-RL`, paper:
  `https://arxiv.org/abs/2505.19630`, date: 2025.5. Experiential
  agentic RL for clinical inquiry.
- **WebAgent-R1** — github: `https://github.com/weizhepei/WebAgent-R1`,
  paper: `https://arxiv.org/abs/2505.16421`, date: 2025.5. End-to-end
  RL for web navigation.
- **multimodal-search-r1** — github:
  `https://github.com/EvolvingLMMs-Lab/multimodal-search-r1`, paper:
  `https://arxiv.org/abs/2506.20670`, date: 2025.6. Multimodal RAG
  with visual search.

These typically: 1 page application setup, ablations of the new
component, comparison vs naive transfer of existing methods.

### Tier 3: empirical study / benchmark

Systematic study of a phenomenon, or a new benchmark.

- **RAGEN** — github: `https://github.com/RAGEN-AI/RAGEN`, paper:
  `https://arxiv.org/abs/2504.20073`, date: 2025.4. Diagnostic
  instrument (MI / reasoning entropy / template collapse) is the
  contribution.
- **R-Zero** — github: `https://github.com/Chengsong-Huang/R-Zero`,
  paper: `https://arxiv.org/abs/2508.05004`, date: 2025.8. Challenger-
  solver self-play.
- **Absolute-Zero-Reasoner** — github:
  `https://github.com/LeapLabTHU/Absolute-Zero-Reasoner`, paper:
  `https://arxiv.org/abs/2505.03335`, date: 2025.5. Learnability-
  weighted curriculum self-generation.

### Tier 4: engineering / infra

Important but harder to publish in top conferences.

- **veRL** — github: `https://github.com/volcengine/verl`, paper:
  `https://arxiv.org/abs/2409.19256`, ByteDance Seed, date: 2024.9.
- **OpenRLHF** — github: `https://github.com/OpenRLHF/OpenRLHF`, paper:
  `https://arxiv.org/abs/2405.11143`, date: 2024.5.
- **slime** — github: `https://github.com/THUDM/slime`,
  org: Tsinghua University (THUDM), date: 2025.6.
- **AReaL** — github: `https://github.com/inclusionAI/AReaL`, paper:
  `https://arxiv.org/abs/2505.24298`, date: 2025.5.
- **SkyRL** — github: `https://github.com/NovaSky-AI/SkyRL`, paper:
  `https://arxiv.org/abs/2511.16108`, date: 2025.11.

## When your work is publishable

Ask:

1. **Algorithm**: Does it work in cases existing methods don't? On
   what specific failure mode?
2. **Application**: Does it require non-trivial adaptation? Did naive
   transfer fail?
3. **Empirical**: Did you discover a new phenomenon, or just confirm a
   known one?
4. **Benchmark**: Does it surface a gap in current methods?

If yes to one of these, you have a paper.

## The "GRPO + minor tweak" trap

Many papers on arxiv are "GRPO + small tweak on benchmark X." Most are
not significant. If your tweak gets <2 points improvement and isn't
ablated against a strong baseline, the contribution is unclear.

Reviewers ask: **does the field need this?**

## What makes a strong agentic-RL paper

### Method papers

- Clear failure mode in prior work.
- Ablations that isolate the contribution.
- 3+ benchmarks; OOD transfer.
- Open code, reproducible.

### Application papers

- Domain expertise that informs design.
- Comparison vs strong general-domain baseline (e.g. a general agent
  on the same task).
- Ablation of domain-specific components.

### Empirical papers

- Diagnostic instrument (e.g. RAGEN's MI metrics).
- Multiple methods analyzed under the lens.
- Practical recommendations.

### Benchmark papers

- Beyond saturation of existing benchmarks.
- Design for anti-contamination.
- Diverse models evaluated, with public leaderboard.

## What to do with negative results

The field needs them. "We tried X on Y; it didn't help over Z" is
useful. Publishable in workshops or as a section of a methods paper.

## See also

- `ablation-design.md`
- `baseline-selection.md`
