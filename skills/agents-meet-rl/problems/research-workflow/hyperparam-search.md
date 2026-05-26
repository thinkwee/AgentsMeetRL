# Question: how to search hyperparameters for agentic RL

## Why this is its own topic

Agentic RL has more knobs than typical SFT/PPO:

- KL coefficient β.
- Group size N (GRPO).
- Clip ε (PPO).
- Reward weights (outcome / format / length / info-gain / PRM / ...).
- Learning rate.
- Temperature, top-p (during rollout).
- Curriculum schedule (intrinsic → outcome fade-out shape).

A naive grid search across these is N^7 runs. Most teams can't afford
that. This file is the practical heuristics for which knobs to tune,
in what order, and with what budget.

## Rule 1: most knobs don't need tuning

For 80% of agentic-RL projects, you can copy these defaults and they'll
work:

```yaml
algorithm:
  adv_estimator: grpo
  kl_loss_coef: 1e-3
  kl_target: null
  loss_agg_mode: token-mean
  norm_adv_by_std_in_grpo: true
  clip_ratio: 0.2
  entropy_coef: 0.0
  group_n: 8
optim:
  lr: 1e-6
  warmup_ratio: 0.03
  lr_scheduler: cosine
data:
  temperature: 0.7
  top_p: 0.95
reward:
  outcome_weight: 1.0
  format_weight: 0.05
```

Don't search across these. **Search only the knobs your task is
sensitive to.**

## Which knobs actually matter

In rough order of frequency they need tuning per task:

1. **Reward weights (α/β/γ/δ on multi-component reward)** — Almost
   always need tuning. See `../training/reward-mixing.md`.
2. **KL coefficient β** — Sensitive to your task's reward density. See
   `../training/kl-penalty-tuning.md`.
3. **Group size N** — Capability ceiling vs. compute trade. N=16 if
   you can afford it; N=8 default.
4. **Curriculum schedule** — When to fade intrinsic reward.
5. **LR** — Usually 1e-6 to 5e-7 works; tune if you see KL blow-up or
   stagnation.
6. **Clip ε** — Tighten if importance ratios blow up.
7. **Temperature** — Almost never. Use 0.7 unless you have a specific
   reason.

The other knobs (warmup ratio, scheduler shape, entropy coef) you can
leave at defaults forever.

## Search strategies

### Strategy A: ablation, not grid

Don't sweep across N×M combinations. Hold all knobs fixed at default,
vary one at a time:

```
Step 1: lr ∈ {3e-7, 1e-6, 3e-6}      → pick best.
Step 2: kl_coef ∈ {3e-4, 1e-3, 3e-3}  → pick best (with new lr).
Step 3: group_n ∈ {8, 16}             → pick best.
Step 4: format_weight ∈ {0.0, 0.05, 0.1} → pick best.
```

4 sweeps × 3 values = 12 runs total instead of 81. **You miss
interactions** but you afford it.

### Strategy B: random search

For tighter compute budget, random search beats grid search in
high-dim spaces:

- Define ranges for each knob.
- Sample N (e.g., 20) configurations randomly.
- Run all; pick best.

Random search captures the "best knob is somewhere unusual" cases that
grid misses.

### Strategy C: Bayesian (Optuna, Ax)

For expensive runs (>$500 each):

```python
import optuna

def objective(trial):
    lr = trial.suggest_loguniform("lr", 1e-7, 1e-5)
    kl = trial.suggest_loguniform("kl", 1e-4, 1e-2)
    n  = trial.suggest_categorical("n", [8, 16])
    return run_experiment(lr=lr, kl=kl, n=n)

study = optuna.create_study(direction="maximize")
study.optimize(objective, n_trials=20)
```

Bayesian optimization wins big when:

- Each run takes >12 hours.
- You have >5 dimensions.
- You can afford only 20-50 total runs.

Doesn't help for short, cheap runs where random search is competitive.

### Strategy D: small-model proxy

Tune on a smaller model first:

```
1. Tune on 1.5B or 3B model.
2. Take best config.
3. Run final on 7B / 32B with that config.
```

Most knobs *transfer* across scale: optimal LR shifts predictably,
KL coef is roughly stable, group size is task-dependent (not
size-dependent).

Caveat: capacity-related knobs (LoRA rank, attention type) may not
transfer.

### Strategy E: short-horizon proxy

Tune on a short training run:

```
1. 200 steps × 12 configurations.
2. Look at trajectory shape (is reward moving? KL stable? entropy
   reasonable?).
3. Pick top 3; run 1000 steps each.
4. Pick best; run full training.
```

Trades early-stopping risk for compute. Some knobs only show their
effect at convergence (LR schedule); others show in 200 steps (KL
coef).

## What you should *not* search over

### Reference model

Always SFT/Instruct, not base. This isn't a tuning question.

### Tokenizer / chat template

These are correctness, not tuning. Get them right; never touch.

### Training framework defaults

Whether to use FSDP vs Megatron, optimizer fused vs not, attention
implementation — these are infrastructure, not RL knobs. Pick once,
move on.

### Reward function structure

The shape of the reward (e.g., "outcome + format + length") is a
*design* decision. Don't search over "what terms to include" — search
over weights given a fixed structure.

## Per-task starting points

### Math/reasoning TIR

```yaml
group_n: 16
kl_loss_coef: 1e-3
lr: 1e-6
loss_agg_mode: token-mean
norm_adv_by_std_in_grpo: false  # Dr.GRPO for length
format_weight: 0.05
```

Tune: `kl_loss_coef`, `lr`.

### Search/RAG

```yaml
group_n: 8
kl_loss_coef: 1e-3
lr: 5e-7
format_weight: 0.05
tool_validity_weight: 0.05
```

Tune: `format_weight`, `tool_validity_weight` (most sensitive to
reward design here).

### Code/SWE

```yaml
group_n: 8
kl_loss_coef: 5e-4               # weak anchor; reward is strong
lr: 1e-6
clip_ratio: 0.15                  # tight; long sequences
```

Tune: `lr`, `kl_loss_coef`. Test pass rate is signal — don't add
format reward.

### GUI/Web

```yaml
group_n: 8
kl_loss_coef: 1e-2                # strong anchor; partial reward
lr: 5e-7
click_reward: continuous          # not binary
```

Tune: `kl_loss_coef`, `click_reward` shape (Gaussian σ).

### Long-horizon agents

```yaml
group_n: 8
kl_loss_coef: 1e-3
lr: 5e-7
gamma: 0.99
algorithm: gigpo                  # not vanilla GRPO
```

Tune: `gamma`, `info_gain_weight` if using IGPO.

## Pitfalls

### "We tried 100 configs and one worked great"

Likely overfit to noise. Test the winner with 3 seeds; if it doesn't
hold, it was lucky.

### "Best HP is at the boundary of the search range"

The optimum is outside your range. Extend.

### "Different HP at 7B vs 70B"

Some knobs scale with model size:

- LR: roughly 1/sqrt(model_size) — smaller LR for larger models.
- Group N: usually stable.
- KL coef: usually stable.
- Reward weights: usually stable.

Don't assume identical config; do a quick recheck at the new scale.

### "HP search masks a reward function bug"

If your reward function has a bug, no HP fixes it long-term. The
"magic LR" you found gets you to a local optimum the bug allows;
fixing the bug reveals a different optimal LR.

Audit reward before tuning.

### "We tuned on dev, eval on test"

Standard ML hygiene. Use a separate held-out set for final reporting.
Don't fish in test.

## Compute budget rules of thumb

| Total budget | Strategy |
|---|---|
| < 1 week, 1 GPU | Just use defaults. |
| 1-2 weeks, 8 GPUs | Strategy A (ablation, 12 runs). |
| 2-4 weeks, 8 GPUs | Strategy B (random search, 20-30 runs). |
| > 4 weeks, 64+ GPUs | Strategy C (Bayesian, 50-100 runs); use small-model proxy. |

For 1-week sprints: trust the corpus defaults + tune reward weights
only. Most projects don't have time for systematic search.

## Reporting HP search

In your paper:

- State the search strategy (grid / random / Bayesian / ablation).
- State the search range per knob.
- State the search budget (number of trials, total compute).
- State the final config.
- Cross-validate: does the same config work on a different seed?

This is what reviewers ask. Not stating it implies cherry-picking.

## Paper / repo references

> **veRL** — github: `https://github.com/volcengine/verl`,
> paper: `https://arxiv.org/abs/2409.19256`, ByteDance Seed, date: 2024.9.
> Why: documented config defaults are the reference
> "no-search" starting point.

> **Search-R1** — github: `https://github.com/PeterGriffinJin/Search-R1`,
> paper: `https://arxiv.org/abs/2503.09516`, UIUC, date: 2025.3.
> Why: published wandb logs let you compare your sweep against an
> external baseline shape.

> **Skywork-OR1** — github: `https://github.com/SkyworkAI/Skywork-OR1`,
> paper: `https://arxiv.org/abs/2505.22312`, Skywork, date: 2025.5.
> Why: large-scale ablations document HP sensitivity at scale; useful
> for "does this knob matter" prior.

## See also

- `../training/kl-penalty-tuning.md` — deep dive on β.
- `../training/grpo-knobs.md` — GRPO-specific knobs.
- `../training/ppo-knobs.md` — PPO-specific knobs.
- `../training/reward-mixing.md` — multi-component reward weighting.
- `../evaluation/statistical-significance.md` — is your "best HP" actually
  significant?
- `ablation-design.md` — ablations vs HP search.
