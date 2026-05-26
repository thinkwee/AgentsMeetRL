# Problem: model forgets general capabilities after agentic RL

## Symptoms

- Eval on training task improves; eval on math / code / general
  benchmarks (MMLU, GSM8K, HumanEval) drops 5-15 points.
- Model can't follow generic instructions any more — only the agentic
  format works.
- Lost multilingual capability (English-trained model does worse on
  Chinese after RL).
- Hidden capability decay: model still scores well on agentic tasks
  but lost subtle reasoning that doesn't show in the benchmark.

This is **different from `sft-to-rl-transition.md`**, which is about
the early-RL instability when transitioning from SFT. Catastrophic
forgetting is a *late-RL* effect: thousands of steps in, your specialty
score is great but everything else is decaying.

## Root causes

1. **KL anchor too weak.** Policy drifts so far from reference that
   pre-training/SFT capabilities are overwritten.
2. **Training data too narrow.** Single-domain prompts → model
   re-allocates capacity away from general capability.
3. **No replay of general data.** The optimizer has no signal to
   preserve out-of-distribution behavior.
4. **LR not decayed in late training.** Same LR at step 5000 as at
   step 100 → continuing to overwrite.
5. **Format-specific format reward.** The model learns to *only*
   produce `<think>...</think><answer>...</answer>`, refuses other
   formats — that's a failure mode reviewers will catch.

## Diagnosis

### Snapshot eval on general benchmarks

Run a small fixed eval set — MMLU subset (200 prompts), GSM8K subset
(200 prompts), HumanEval subset (50) — every 500 steps. Plot:

```
General benchmark accuracy ↑     Healthy.
General benchmark accuracy flat  Specializing without forgetting.
General benchmark accuracy ↓ 5+  Forgetting; intervene.
```

Cheap (~10 min on 8x H100); catches forgetting 1000s of steps before
the agentic eval would.

### KL trajectory

If KL to ref grows monotonically past 5-10, your reference anchor is
too weak. KL ≈ 1-3 typical for a well-anchored agentic RL run.

### Capability probe

Save 50 "non-agentic" prompts (general instruction-following) at start
of training. Re-run them at step 1000, 2000, 5000. Read responses.
Healthy: still natural responses. Sick: forced into agent format
unconditionally, or refusing to answer.

## Fixes

### Fix 1: stronger KL anchor (reference = SFT/Instruct model)

The single biggest lever. For agentic RL prone to forgetting:

```yaml
algorithm:
  kl_loss_coef: 5e-3          # not 1e-3
  kl_penalty: kl              # loss form preferred
  kl_target: 1.0              # adaptive controller target
```

Increase β by 5-10× from default. KL stays in [0.5, 2.0] band; model
is anchored.

Pair with **reference = SFT / Instruct checkpoint**, not base. The
reference model is what you don't forget.

### Fix 2: replay general SFT data alongside RL

Mix in general instruction-following SFT batches every K steps:

```python
if step % 5 == 0:
    batch = sample_from(general_sft_pool, batch_size=...)
    sft_loss = compute_sft_loss(model, batch)
    optimizer.step(sft_loss * 0.3)
else:
    rl_step()
```

Keeps the gradient pulling towards general capability. Cost: ~10-20%
extra compute. Skywork-OR1 documents this pattern at scale.

### Fix 3: multi-task RL prompts

Train on a **mix** of agentic prompts + math + code + general
instruction-following. Tool-Star and Skywork-OR1 both follow this:
the policy never specializes into a single format because the data
won't let it.

Recipe shape:

```
60% domain-specific (your target task)
20% math/code (verifiable)
10% general instruction-following
10% multilingual / cross-domain
```

### Fix 4: LR decay in late training

```yaml
optim:
  lr_scheduler: cosine            # not constant
  warmup_ratio: 0.03
  total_steps: 5000
  end_lr_ratio: 0.1               # final LR = 10% of peak
```

Late-training high-LR is a major forgetting source — Adam keeps
overwriting in directions whose marginal utility is near zero.

### Fix 5: LoRA RL (constrained subspace)

If you can accept a small final-performance hit, LoRA forces all
updates into a low-rank subspace. The base weights aren't touched, so
they're guaranteed not to forget.

```yaml
peft_config:
  type: lora
  r: 32
  alpha: 64
  target_modules: q_proj,k_proj,v_proj,o_proj
```

Trade-off: 1-3 points lower headline number vs full fine-tune. See
`lora-rl.md`.

### Fix 6: snapshot-eval rollback

If general benchmark drops > 5 points: revert to last-known-good
checkpoint, lower LR, increase β. Don't try to "train through" it.
Forgetting is rarely self-correcting.

### Fix 7: format flexibility in rollouts

Don't *only* train on the agentic format. Mix in some plain-text
rollouts where reward only checks correctness (no format gate).
Prevents the model from collapsing to "I can only respond in
`<think>` tags."

### Fix 8: multi-task self-play / cross-game training

For self-play / multi-agent: train on a *suite* of related games
rather than one. Forces general strategy:

> **SPIRAL** — github: `https://github.com/spiral-rl/spiral`,
> paper: `https://arxiv.org/abs/2506.24119`, NUS/A*STAR/Sea AI,
> date: 2025.6. Trains on TicTacToe/Kuhn Poker/Negotiation jointly;
> reports transfer to math reasoning as a side benefit. The cross-task
> training itself protects against forgetting.

## Recipe: "minimum forgetting" agentic RL

```yaml
algorithm:
  adv_estimator: grpo
  kl_loss_coef: 5e-3              # high anchor
  kl_target: 1.5
  loss_agg_mode: token-mean
optim:
  lr: 5e-7                        # conservative
  lr_scheduler: cosine
  warmup_ratio: 0.03
  end_lr_ratio: 0.1
data:
  agentic_ratio: 0.6
  math_code_ratio: 0.2
  general_sft_ratio: 0.1
  multilingual_ratio: 0.1
training:
  reference_model: instruct       # not base
  multi_task: true
  general_eval_every: 500
  rollback_threshold: 5           # if general drops 5pt, revert
```

## When forgetting is acceptable

Sometimes you *want* the model to specialize:

- Production deployment where one task matters and you can't afford
  the multi-task tax.
- Research paper where the headline benchmark is your job; OOD is a
  separate concern.
- Capability ceiling reached: the model couldn't do the secondary task
  well anyway.

In those cases, document the forgetting (report ID-OOD gap) rather
than try to fix it.

## Paper / repo references

> **Skywork-OR1** — github: `https://github.com/SkyworkAI/Skywork-OR1`,
> paper: `https://arxiv.org/abs/2505.22312`, Skywork, date: 2025.5.
> Why: large-scale rule-based RL stability study; documents the
> intrinsic-vs-fixable variance distinction and the multi-task data
> mix that prevents specialization-induced collapse.

> **SPIRAL** — github: `https://github.com/spiral-rl/spiral`,
> paper: `https://arxiv.org/abs/2506.24119`, NUS/A*STAR/Sea AI,
> date: 2025.6. Why: zero-sum self-play across multiple games; reports
> transfer to math reasoning. Multi-game training is the
> forgetting-resistant pattern.

> **Tool-Star** — github: `https://github.com/dongguanting/Tool-Star`,
> paper: `https://arxiv.org/abs/2505.16410`, RUC, date: 2025.5.
> Why: multi-stage SFT/DPO/PPO/ORPO mix avoids specialization on a
> single tool-use format.

> **GUI-Libra** — github: `https://github.com/GUI-Libra/GUI-Libra`,
> paper: `https://arxiv.org/abs/2602.22190`, date: 2026.2.
> Why: KL-regularized GRPO with strong β; explicit motivation is
> partial-reward → strong KL → less drift.

> **veRL** — github: `https://github.com/volcengine/verl`,
> paper: `https://arxiv.org/abs/2409.19256`, ByteDance Seed, date: 2024.9.
> Why: `KLControlConfig` exposes the high-β knobs and
> adaptive controller cleanly.

## See also

- `kl-penalty-tuning.md` — what β to set.
- `kl-explosion.md` — the opposite failure mode.
- `lora-rl.md` — when LoRA is the right forgetting-mitigation.
- `sft-to-rl-transition.md` — early-RL forgetting (different).
- `../evaluation/ood-evaluation.md` — measuring forgetting across
  distributions.
