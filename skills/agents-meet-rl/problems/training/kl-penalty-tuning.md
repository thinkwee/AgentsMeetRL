# Problem: how do I tune KL penalty (β) — what value, when

## TL;DR

- Default β around 1e-3 (loss form). Most papers in the corpus.
- For partial-reward / weak-reward tasks, β can be 1e-2 (GUI-Libra).
- For very-tight tasks, β can be 1e-4 (more drift allowed).

## How to choose

### Step 1: target KL trajectory

Decide what KL trajectory is acceptable:

- KL ≈ 0.1 at convergence: very anchored to ref. Use for safety-critical
  fine-tuning.
- KL ≈ 1–5: typical. Strong learning signal, model still recognizable.
- KL > 10: significant drift; only OK if eval improves.

### Step 2: start at β = 1e-3, observe

- KL too high → β up by 10x.
- KL too low (model not learning) → β down by 10x.

### Step 3: validate with eval

KL is a means, not an end. The real metric is eval. β too high =
slow improvement. β too low = drift. Eval tells you which.

## Per-task heuristics

| Task | β suggestion | Rationale |
|---|---|---|
| Math/code with hard verifiers | 1e-4 to 1e-3 | Strong reward; let policy move |
| Search/QA with rule reward | 1e-3 | Standard |
| Tool-use with mixed reward | 1e-3 | Standard |
| Open-ended w/ LLM-judge | 5e-3 to 1e-2 | Judge is biased; anchor more |
| GUI w/ partial reward | 1e-2 (GUI-Libra) | Reward is incomplete |
| Multi-agent | 1e-3 to 1e-2 | Higher to keep roles aligned |
| Self-play | 1e-3 | Standard |

## Penalty form vs loss form

veRL exposes both:

- **Loss form** (`kl_loss_coef`): adds β*KL to total loss. Smoother
  gradient. Default in most papers.
- **Penalty form** (`kl_penalty`): subtracts β*KL from per-token reward.
  Cleaner conceptual separation.

Functionally similar; pick whichever your framework defaults to.

## KL approximators

- `kl1`: log(p/q). Standard, low-variance estimator.
- `kl3`: (p/q - 1)^2 / 2. Symmetric, sometimes preferred for stability.
- `mse`: (log p - log q)^2. Squared form.

veRL allows choosing via `kl_penalty` field.

## Adaptive β

Some recipes adapt β based on observed KL:

```
if KL > target_KL * 1.5: β *= 1.5
if KL < target_KL / 1.5: β /= 1.5
```

Use when you have no good prior on β. Adds overhead.

## Strong-KL example

> **GUI-Libra** — github: `https://github.com/GUI-Libra/GUI-Libra`,
> paper: `https://arxiv.org/abs/2602.22190`, date: 2026.2. Specifically
> motivates strong-KL ("Partially Verifiable RL") for GUI tasks where
> reward is partial.

## Why β too small fails

The policy drifts into reward-hacking attractors (template collapse,
length blow-up, search hacking). KL anchor stops these.

## Why β too large fails

The policy can't move. Reward stays flat. Model "outputs SFT model
exactly" and only minor changes happen.

## Paper / repo references

- `GUI-Libra` — github: `https://github.com/GUI-Libra/GUI-Libra`,
  paper: `https://arxiv.org/abs/2602.22190`, date: 2026.2.
