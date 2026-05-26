# Problem: my eval differs from training because of sampling params

## Symptoms

- During training (with T=1.0, top_p=0.95) the model looks great.
- Eval (with T=0, greedy) is much worse.
- Or the reverse: eval with high temperature looks great, T=0 collapses.

## Root causes

1. **Different sampling parameters.** Training uses high T to explore;
   eval uses T=0 for determinism. Behaviors that work at T=1.0 (long
   reasoning, exploratory tool use) may not occur at T=0.
2. **Different stop tokens.** vLLM uses different stop set than the HF
   tokenizer used for eval.
3. **Different chat template.** Subtle.
4. **Different inference engine.** vLLM vs SGLang vs HF — slight
   differences.
5. **Different rollout interface.** Training has env feedback after
   each tool call; eval may not.
6. **Train env caches; eval env is live.** Search hacking on cached
   corpus → fails on live.

## Diagnosis

### Same prompt, both pipelines

Run a fixed prompt through both rollout pipelines (training and eval).
Decode and compare. If outputs differ before any randomness, you have
a non-stochastic difference (template, tokenizer, stop tokens).

### Same prompt, both T=0

Train eval with T=0, training rollout with T=0 — outputs should be
near-identical for one decode.

### Inspect first divergence point

If outputs diverge after K tokens, what made them diverge? Tokenizer?
KV cache? Stop token list?

## Fixes

### Fix 1: match sampling params

Eval must use the same T, top_p, top_k, repetition_penalty as training
generation (at least for a "training-like" eval pass).

> Most papers report T=0 eval as the "headline" but include T=0.7
> rollouts elsewhere. Be explicit.

### Fix 2: use the same engine end-to-end

If training uses vLLM, eval should use vLLM (or at least be benchmarked
against vLLM-based eval).

### Fix 3: match chat template + stop tokens exactly

Common bug: training applies `add_generation_prompt=True`, eval
applies `False`. Output looks different.

### Fix 4: same env for train and eval (when possible)

If you trained against a cached corpus, eval at least once on the
live env to detect search hacking.

### Fix 5: report multiple sampling regimes

```
Method A:
  T=0, greedy:   72.3
  T=0.7, maj@8:  76.1
  T=0.7, pass@8: 81.5
```

This makes the eval setup transparent.

## Practice

- **Pin sampling params** in your eval script. Don't rely on
  framework defaults — they change.
- **Compute eval reward = train reward on same prompts** as a sanity
  check at start of training.
- **Run eval mid-training** to catch divergence early.

## Paper / repo references

> **Search-R1** — github: `https://github.com/PeterGriffinJin/Search-R1`,
> paper: `https://arxiv.org/abs/2503.09516`, org: UIUC/Google, date: 2025.3.
> Why: ships a separate `evaluate.sh` with pinned sampling params; lets
> you compare train-time and eval-time decoding side-by-side without
> framework-default drift.

> **Agent-R1** — github: `https://github.com/0russwest0/Agent-R1`,
> paper: `https://arxiv.org/abs/2511.14460`, org: USTC, date: 2025.11.
> Why: clean separation of `train_*.sh` and eval entry points with
> identical chat template / stop tokens — reference for fix 3.

> **veRL** — github: `https://github.com/volcengine/verl`,
> paper: `https://arxiv.org/abs/2409.19256`, ByteDance Seed, date: 2024.9.
> Why: `verl/utils/reward_score/` is shared between train and
> eval, eliminating one common source of train-eval mismatch.

## See also

- `reproducibility.md` — env / Docker drift.
