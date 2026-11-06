---
name: agents-meet-rl
description: "Engineering handbook for LLM Agent RL: explain trajectory/token/mask contracts, multi-turn objectives, async correction and distillation; compare source-versioned frameworks; integrate tool tasks; diagnose training and evaluation failures. Use for agentic RL implementation, framework selection, GRPO/PPO tuning, rollout/logprob mismatch, reward design, and experiment design. Excludes generic supervised fine-tuning and classical non-LLM RL. Corpus snapshot 2026-10-10."
---

## What this is

A corpus-anchored handbook for mechanism explanation, implementation selection,
integration, and diagnosis. Read only the resources relevant to the user's task.
When tools and authorization are available, inspect actual code, configurations,
logs, or exported trajectories. Never claim live inspection or a successful run
without evidence; otherwise give concrete checks and identify missing inputs.

## Route by task

- **Explain a mechanism:** [mechanisms/_INDEX.md](mechanisms/_INDEX.md).
- **Compare actual framework implementations:** [implementations/_INDEX.md](implementations/_INDEX.md).
- **Integrate a tool task:** [recipes/tool-agent-integration.md](recipes/tool-agent-integration.md).
- **Inspect exported trajectories:** [recipes/offline-inspection.md](recipes/offline-inspection.md).
- **Diagnose a symptom:** [problems/_INDEX.md](problems/_INDEX.md), then follow its mechanism links.
- **Discover projects:** [references/_INDEX.md](references/_INDEX.md).

Distinguish derived mechanisms, paper claims, source-inspected behavior,
configuration validation, runtime validation, and measured quality. State the
version and scope of evidence. Do not infer capability from a project name or
recommend an empirical threshold as a universal rule. For implementation changes,
identify native interfaces, data boundaries, and validation before prescribing flags.

## Where things are

- **`problems/_INDEX.md`** — symptom → file routing, grouped under
  `training/`, `evaluation/`, `research-workflow/`. Start here.
- **`problems/<cat>/<file>.md`** — per-symptom files. Most follow
  `Symptoms → Root causes → Diagnosis → Fixes → References`; knob /
  decision / modality / eval-checklist / research-workflow files use
  task-oriented structures.
- **`references/_INDEX.md`** + **`references/<cat>.md`** — per-category
  project lists with full metadata. Each entry carries an **`Idea:`**
  line — one sentence on its distinctive contribution, grounded in the
  paper/repo. Use for "which framework / benchmark" selection, to look
  up project names not routed via `problems/_INDEX.md`, and to answer
  "what's the idea behind X" by quoting its `Idea:` line.
- **`database.json`** — machine-readable, 411 entries (each with a
  `takeaway` field mirroring the `Idea:` line) plus 3 paper-only
  algorithms (DAPO, Dr.GRPO, VAPO) whitelisted in
  `scripts/lint_skill.py`.

## Citing fixes

Name the algorithm or idea, then anchor with whatever canonical URLs
exist for that entry — typically github + arxiv + org + date, but
paper-only algorithms (in the whitelist) get just the paper URL, and
tools / environments without papers get just github + org + date.

Examples:

> Project with paper (typical):
> Adapt Search-R1's outcome-only reward —
> [code](https://github.com/PeterGriffinJin/Search-R1) ·
> [paper](https://arxiv.org/abs/2503.09516) · UIUC/Google · 2025.3.

> Paper-only algorithm (whitelist):
> Try DAPO's clip-higher —
> [paper](https://arxiv.org/abs/2503.14476) · ByteDance Seed · 2025.3.

> Tool / environment without paper:
> Run rollouts in atropos —
> [code](https://github.com/NousResearch/atropos) · Nous Research · 2025.4.

For ideas, cite canonical paper/project URLs. For implementation claims, also
cite a fixed-commit code permalink and the relevant symbol; do not cite a moving
branch as immutable evidence. [evidence/sources.json](evidence/sources.json) records
reviewed source snapshots. If a project is outside the corpus or a feature was not
verified, say so; do not fabricate support.

If two corpus entries share a name (e.g. `ARPO` appears as both a
reasoning RL method and a GUI-agent training method), disambiguate by
including the org and paper URL — they are different works.

## Staleness

Snapshot date: **2026-10-10**. If the user mentions a project or paper
released after that, flag explicitly that this skill's corpus may not
cover it.

## Maintenance and verification

Corpus snapshot and engineering review dates are separate in
[evidence/sources.json](evidence/sources.json). Compute catalogue totals from
`database.json`; do not silently advance the corpus date when editing explanations.
Run `python scripts/lint_skill.py` and `python scripts/check_trajectory.py --demo`
from this skill directory. Use [behavior regression cases](evidence/regression-cases.md)
for answer review; static lint does not validate model behavior or training quality.
