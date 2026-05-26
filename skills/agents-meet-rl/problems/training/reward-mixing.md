# Problem: mixing multiple reward terms — weights, normalization, curriculum

## When this matters

Your reward is `r = α*outcome + β*format + γ*tool_validity + δ*length_pen + ...`.

Setting α/β/γ/δ poorly leads to:
- One term dominating, others noise.
- Format/length terms gamed before outcome learns.
- Curriculum unable to "fade out" auxiliary signals.

## Patterns from the corpus

### Outcome dominates (≥ 0.8 of total)

The default. Auxiliary terms (format, length) at most 10% of total.

> **Search-R1** — outcome ≥ format ≥ tool-validity. Format weight small.

> **ZeroSearch** — outcome only. No format reward needed because the
> simulated env enforces format.

### Curriculum: intrinsic → outcome over training

Start info-gain or PRM heavy; fade to outcome heavy. The model needs
the intrinsic signal early when outcomes are sparse; later, outcome
signal is robust.

> **IGPO** — github: `https://github.com/GuoqingWang1/IGPO`,
> paper: `https://arxiv.org/abs/2510.14967`, Ant Group, date: 2025.10.
> Curriculum schedule, e.g.:
> ```bash
> +algorithm.curriculum_f1_init=0.5
> +algorithm.curriculum_f1_final=1.0
> +algorithm.curriculum_ig_init=1.0
> +algorithm.curriculum_ig_final=0.5
> ```
> Outcome (F1) starts at 0.5, ends at 1.0 (increasing).
> Info-gain (IG) starts at 1.0, ends at 0.5 (decreasing).

### Skill-decomposed reward

Decompose the task into skills, each with its own reward.

> **SWE-Swiss** — github: `https://github.com/zhenyuhe00/SWE-Swiss`.
> Localization + Repair + Test Generation, each with separate reward.

> **Doctor-R1** — clinical inquiry + diagnosis split.

### Dual-level (utility + safety)

> **SafeSearch** — github: `https://github.com/amazon-science/SafeSearch`,
> paper: `https://arxiv.org/abs/2510.17017`. Final-answer reward + safe
> intermediate query reward.

### Outcome + efficiency + preference

> **ToolOrchestra** — github: `https://github.com/NVlabs/ToolOrchestra`,
> paper: `https://arxiv.org/abs/2511.21689`, NVIDIA/HKU, date: 2025.11.
> End-to-end RL with outcome+efficiency+preference rewards.

## Normalization

Don't combine raw values. Normalize each term to [0, 1] (or [-1, 1])
before weighting. Otherwise a 0-100 raw outcome and a 0-1 format reward
need very different weights to balance.

## Common bugs

### Bug 1: bug in one component zeroes everything

If `tool_validity` always returns 0 because of a parser bug, the
weighted sum still works — but you've effectively reduced reward dim.
Log each component separately.

### Bug 2: components disagree

If format reward says "perfect" but outcome reward says "wrong", you
have a meaningful signal. If they always agree, one is redundant.

### Bug 3: curriculum schedule too fast

Linearly fading info-gain to 0 over 1000 steps when outcome reward is
still sparse breaks training. Tie schedule to *observed* outcome
variance, not step count.

## Recommended starting setup

```python
reward = (
    1.0 * outcome
    + 0.05 * format_correct
    + 0.05 * tool_call_valid
    - 0.001 * max(0, length - target_length)
    # optional intrinsic
    + curriculum(step) * 0.3 * info_gain
)
```

Log each component separately to wandb. Audit component contributions
periodically.

## Paper / repo references

- `IGPO` — github: `https://github.com/GuoqingWang1/IGPO`,
  paper: `https://arxiv.org/abs/2510.14967`, Ant Group, date: 2025.10.
- `SafeSearch` — github: `https://github.com/amazon-science/SafeSearch`,
  paper: `https://arxiv.org/abs/2510.17017`, Amazon, date: 2025.10.
- `SWE-Swiss` — github: `https://github.com/zhenyuhe00/SWE-Swiss`.
- `ToolOrchestra` — github: `https://github.com/NVlabs/ToolOrchestra`,
  paper: `https://arxiv.org/abs/2511.21689`, date: 2025.11.

**Other corpus entries:**

- `s3` — Gain-Beyond-RAG reward — only credit retrieval gains over a strong RAG baseline (avoids reward gaming where any retrieval looks helpful).
  github: `https://github.com/pat-jj/s3`, paper: `https://arxiv.org/abs/2505.14146`, UIUC, date: 2025.5

- `Alpha-R1` — portfolio returns + LLM judge for finance alpha factor screening.
  github: `https://github.com/FinStep-AI/Alpha-R1`, paper: `https://arxiv.org/abs/2512.23515`, SJTU / FinStep.AI / StepFun, date: 2025.12

- `AutoVLA` — PDMS (planning driving metric) reward for autonomous driving.
  github: `https://github.com/ucla-mobility/AutoVLA`, paper: `https://arxiv.org/abs/2506.13757`, UCLA Mobility Lab, date: 2025.6

- `AlphaDrive` — 4 separate planning rewards combined for driving.
  github: `https://github.com/hustvl/AlphaDrive`, paper: `https://arxiv.org/abs/2503.07608`, HUST/Horizon Robotics, date: 2025.3

- `Embodied-R1` — rule-based grounding/waypoint reward for embodied agents.
  github: `https://github.com/pickxiguapi/Embodied-R1`, paper: `http://arxiv.org/abs/2508.13998`, Tianjing University, date: 2025.8

- `MemRL` — Q-value retrieval reward for memory-augmented agents.
  github: `https://github.com/MemTensor/MemRL`, paper: `https://arxiv.org/abs/2601.03192`, SJTU/Xidian/NUS/USTC/MemTensor, date: 2026.1

- `WebRL` — outcome reward model (ORM) for web navigation.
  github: `https://github.com/THUDM/WebRL`, paper: `https://arxiv.org/abs/2411.02337`, Tsinghua/Zhipu AI, date: 2024.11

- `RLVR-World` — verifiable reward for world modeling (language/video).
  github: `https://github.com/thuml/RLVR-World`, paper: `https://arxiv.org/abs/2505.13934`, THU ML Group, date: 2025.5

- `MemSkill` — reward derived from learned skill library.
  github: `https://github.com/ViktorAxelsen/MemSkill`, paper: `https://arxiv.org/abs/2602.02474`, NTU/UIUC/UIC/Tsinghua, date: 2026.2

- `GRIT` — GRPO-GR with bbox reward for grounded visual reasoning.
  github: `https://github.com/eric-ai-lab/GRIT`, paper: `https://arxiv.org/abs/2505.15879`, UC Santa Cruz (eric-ai-lab), date: 2025.5
