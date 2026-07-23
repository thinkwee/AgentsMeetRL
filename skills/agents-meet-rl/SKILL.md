---
name: agents-meet-rl
description: "Troubleshooter for agentic-RL training, evaluation, and experiment design on LLM agents (single or multi-agent, multi-turn, tool-augmented). Routes a user's symptom to fixes anchored in the corpus. TRIGGER when: user is training, evaluating, or designing experiments for an RL-trained LLM agent; symptoms like reward not moving, eval flat, KL/entropy/length blow-ups, retokenization drift, tool-call parse failures, credit assignment, async-rollout staleness, judge inconsistency, benchmark contamination, pass@k vs pass@1; choices about ablation, baseline, framework, algorithm, reward, or data curation; user names GRPO, PPO, DAPO, veRL, OpenRLHF, slime, AReaL, RAGEN, or similar. SKIP: generic supervised LLM fine-tuning with no RL component; classical RL theory or tabular RL; non-LLM agents. Distilled from the AgentsMeetRL awesome list, snapshot 2026-07-23."
---

## What this is

A corpus-anchored handbook for diagnosis and selection. It supplies
knowledge — it does **not** read or run your training: it can't inspect
your logs, wandb, or live metrics. You bring the symptom; it returns
likely causes, checks, and cited fixes for you to apply.

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
- **`database.json`** — machine-readable, 368 entries (each with a
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

**Cite at the idea level**, not paper sections or file paths inside
repos — they rot. If an entry isn't in the corpus, say so; don't
fabricate.

If two corpus entries share a name (e.g. `ARPO` appears as both a
reasoning RL method and a GUI-agent training method), disambiguate by
including the org and paper URL — they are different works.

## Staleness

Snapshot date: **2026-07-23**. If the user mentions a project or paper
released after that, flag explicitly that this skill's corpus may not
cover it.
