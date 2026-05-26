# Question: how to detect training problems early — canary eval

## What canary eval is

A small, **fixed** set of prompts that you eval at every step (or every
N steps), with full deterministic decoding, saving outputs to logs.

Different from full benchmark eval which runs at end of training. The
purpose isn't to measure final quality — it's to **catch problems early**.

## Why this matters

Most training failures (collapse, drift, format breakage) become
visible 100s of steps before the next benchmark eval would catch them.
Catching them via canary saves days of compute on a doomed run.

## The canary set

A canary set has 5-20 prompts. Each prompt is:

- **Representative** of the training distribution (not OOD).
- **Diverse** across difficulty / format / topic.
- **Stable** — never changed during training (the whole point is
  reproducible comparison).
- **Fast** — total decode time < 1 minute on rollout hardware.

Example agentic canary set (search agent, 5 prompts):

```
1. "What is the capital of France?"   (trivial; tests format)
2. "Who won the 2023 NBA Finals?"     (factual, single search)
3. "Compare GDP of Japan and Germany in 2023." (multi-search)
4. "Find the molecular weight of caffeine." (tool-use, format)
5. "What's a recent paper on agentic RL?"   (open-ended, latest)
```

For each, you also have a "gold" or expected pattern (not necessarily
exact answer; could be "should mention X").

## What to log

Per canary prompt, every check:

- The full decoded response (with special tokens visible).
- Token count.
- Format-correctness (does it match expected shape).
- Tool-call count if agentic.
- Any custom metric you care about.

```python
canary_results = {
    "step": current_step,
    "prompt": prompt,
    "response": tokenizer.decode(output, skip_special_tokens=False),
    "response_tokens": len(output),
    "format_ok": is_well_formed(output),
    "answer_extracted": extract_answer(output),
    "tool_calls": count_tool_calls(output),
}
wandb.log(canary_results)
```

Store as a long-running table you can scroll. Sometimes you only see
the problem in the *trajectory* (step 1000 was fine, step 1500 broke).

## What canary catches

### Pattern 1: format collapse

Step 1: response well-formed.
Step 2000: response has lost the closing `</answer>` tag entirely.

Without canary, you'd notice at the next benchmark eval (way later).
With canary, you saw it at step 2050 and rolled back.

### Pattern 2: template / mode collapse

Step 1: 5 different responses across 5 prompts.
Step 2000: all 5 responses start with the same boilerplate.

Template collapse — formal diagnosis needs MI between prompt and
trace; canary catches the visible side: different prompts producing
similar responses.

### Pattern 3: length drift

Step 1: response_tokens ≈ 200.
Step 1500: response_tokens ≈ 800.
Step 2500: response_tokens ≈ 4000 (hitting cap).

Slow length blowup is hard to see in averaged metrics; visible in
canary.

### Pattern 4: capability loss

Step 1: trivial canary "What is 2+2?" answers correctly.
Step 2000: canary fails, model launches into long tool-call about
arithmetic.

Capability loss / over-specialization. Caught by canary; missed by
agentic eval.

### Pattern 5: tokenizer drift

Step 1: response uses `<think>` correctly.
Step 1500: response uses `<thi nk>` (broken tokenization).

Tokenizer or template drift. Visible immediately in canary.

### Pattern 6: catastrophic refusal

Step 1: responds.
Step 2000: refuses with "I cannot do that" on prompts where it
previously responded.

Drift from KL anchor in unexpected direction. Visible in canary.

## Cadence

Cheap canary (5 prompts, < 30 sec per eval): every step.
Heavier canary (20 prompts with tool use, 5 minutes): every 50 steps.

Don't go heavier than that — canary should never be a substantial
fraction of training compute.

## Comparing to wandb metrics

Canary complements aggregate metrics, doesn't replace:

| Signal | Catches |
|---|---|
| Mean reward | Is training improving on average? |
| KL | Is policy drifting? |
| Entropy | Is mode collapse happening? |
| Canary | What does the model *actually output* now? |

Aggregate metrics tell you "what's happening." Canary tells you
"what does that look like."

## Comparison view

Best practice: side-by-side diff of canary outputs across two adjacent
checkpoints.

```
                         step 1500             step 1600
prompt 1: format_ok       True                 False
prompt 1: tokens          234                  234
prompt 1: snippet         "The capital..."     "The cap"
prompt 2: format_ok       True                 True
...
```

If between 1500 and 1600 the canary regressed, the change happened
there. Bisect from there.

## Public canary dashboards

Some corpus papers ship public wandb logs that include canary-style
generations:

> **Search-R1** — github: `https://github.com/PeterGriffinJin/Search-R1`,
> paper: `https://arxiv.org/abs/2503.09516`, UIUC, date: 2025.3.
> Why: public wandb across versions (v0.1/v0.2/v0.3); useful comparison
> baseline for what healthy run trajectory looks like.

> **RAGEN** — github: `https://github.com/RAGEN-AI/RAGEN`,
> paper: `https://arxiv.org/abs/2504.20073`, RAGEN-AI, date: 2025.4.
> Why: public wandb dashboard; demonstrates canary-style logging at
> per-prompt level.

## Implementation pattern

```python
class CanaryEvaluator:
    def __init__(self, prompts, sampling_params):
        self.prompts = prompts
        self.params = sampling_params

    def evaluate(self, model, step):
        outputs = []
        for p in self.prompts:
            out = model.generate(p, self.params)
            outputs.append({
                "step": step,
                "prompt": p,
                "response": tokenizer.decode(out),
                "tokens": len(out),
                "format_ok": is_well_formed(out),
            })
        return outputs

# In training loop
canary = CanaryEvaluator(canary_prompts, eval_sampling_params)

for step in range(num_steps):
    train_step()
    if step % canary_freq == 0:
        results = canary.evaluate(model, step)
        wandb.log({"canary": wandb.Table(data=results)})
        if regression_detected(results):
            send_alert(step, results)
```

`regression_detected` can be as simple as "format_ok dropped > 20%
from last canary."

## Anti-patterns

### "Canary on a single prompt"

One prompt, even unchanged, gives noisy signal. Use 5-20.

### "Canary changes during training"

Defeats the purpose. The canary set must be **frozen**.

### "Canary on training prompts"

Pick prompts that are representative but **not in the training set**.
Otherwise you're measuring memorization.

### "Canary every step at high cadence + heavy generation"

> 5 minutes per canary eval at high cadence eats compute. 1 minute, 5
prompts, every 50-100 steps is plenty.

### "Canary with T>0 sampling"

Use T=0 (greedy). You want determinism for comparison across steps.

## Beyond canary: rollback automation

When canary regresses by >K points / >K% format-failure spike:

```python
if format_ok_rate < last_good_rate - threshold:
    save_diagnostic(model, optimizer, recent_logs)
    send_alert()
    # optionally:
    rollback_to(last_good_checkpoint)
    optimizer.lr *= 0.5
    continue_training()
```

Some teams automate rollback; most flag for human review. Either way,
catching the regression at step N+50 is much better than catching at
step N+5000.

## Paper / repo references

> **Search-R1** — see above. Public wandb for canary-style comparison.

> **RAGEN** — see above. Public dashboard.

> **Skywork-OR1** — github: `https://github.com/SkyworkAI/Skywork-OR1`,
> paper: `https://arxiv.org/abs/2505.22312`, Skywork, date: 2025.5.
> Why: large-scale stability study; documents what "stable trajectory"
> looks like — useful as a comparison baseline.

> **veRL** — github: `https://github.com/volcengine/verl`,
> paper: `https://arxiv.org/abs/2409.19256`, ByteDance Seed, date: 2024.9.
> Why: ships an `eval_during_training` hook; canary fits
> as a custom evaluator.

## See also

- `../training/training-collapse.md` — what canary helps catch.
- `../training/entropy-collapse.md` — template collapse signal in canary.
- `../training/unstable-curves.md` — variance vs collapse, distinguishable via
  canary.
- `reproducibility.md` — canary needs deterministic eval.
- `long-horizon-eval.md` — full benchmark complement.
