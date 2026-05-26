# Problem: reproducing a paper from this corpus — common failure modes

## Why reproduction often fails

1. **Hyperparameter omission.** Paper says "GRPO with standard hyperparams"
   but the recipe used custom values.
2. **Data leak / preprocessing.** Paper's preprocessing isn't in the
   release.
3. **Engine version pinning.** vLLM / transformers version matters more
   than the paper admits.
4. **Hidden SFT.** Paper claims "from base model" but actually used a
   public SFT model that has been fine-tuned.
5. **Reward function nuances.** Paper describes reward in prose;
   implementation has small but consequential details.
6. **Stochastic rollouts not seeded.** Different runs give different
   results; paper reports best-of-N implicitly.

## Workflow

### Step 1: clone and build

```bash
git clone <paper repo>
cd <paper repo>
# Read README carefully. Note Python version, vLLM version, etc.
```

### Step 2: run the unit tests / sanity check

Most repos in this corpus ship a smoke test:

> **Search-R1** — `bash example/run_qwen2.5-3b.sh` is a sanity check.
> **Agent-R1** — `examples/run_qwen2.5-3b.sh` similarly.

If the smoke test fails, fix that before going to full training.

### Step 3: replicate their training data

If they preprocessed:

- Look for a `data_process/` or `scripts/data/` directory.
- Run their preprocessing on raw data.
- Verify file checksums if provided.

### Step 4: replicate their model

If they have a HuggingFace model release, use it as init.
**Don't substitute "similar" SFT models** — they often differ
materially.

### Step 5: replicate eval first

Before retraining, run their eval on their released model.

If your number matches theirs: env is correctly set up. If not:
something's different. Fix before training.

### Step 6: train

Run training. Compare wandb metrics to their published wandb (if
public — Search-R1, RAGEN do).

### Step 7: identify divergence early

If by step 1000 your run looks different from theirs, **stop**.
Diagnose:

- Tokenizer / chat template?
- Library versions?
- Hardware (BF16 vs FP16)?
- Hyperparameters not in paper but in code?

## Best-in-class reproducibility

> **Search-R1** — github: `https://github.com/PeterGriffinJin/Search-R1`.
> Public wandb logs across versions (v0.1, v0.2, v0.3). Recipe scripts
> for each. Documented multinode setup.

> **veRL recipe folder** — `https://github.com/volcengine/verl`.
> Concrete recipes for DAPO, Dr.GRPO, GSPO, KL_Cov, PRIME with
> instructions.

> **RAGEN** — public wandb:
> `https://api.wandb.ai/links/zihanwang-ai-northwestern-university/a8er8l7b`.

> **SkyRL** — released `skyrl-train`, `skyrl-tx`, `skyrl-agent`,
> `skyrl-gym` separately for fork-and-adapt.

## Worst-in-class signs

- No code release.
- Code release without instructions.
- "v0.1.0" tag but main branch only.
- Hyperparameters in slides/blog only.
- Dependencies on internal infra (Ray cluster, custom Docker).

For these papers, citing the reported number with a footnote is OK;
trying to reproduce will burn time.

## When to give up

- > 1 week reproducing without progress.
- Original authors don't respond to issues.
- The paper's claim doesn't replicate even on their released model.

In these cases, take the published number with a grain of salt and
move on. Don't sink a month into someone else's bug.

## Documentation as you go

When you reproduce someone, write up:

- Exact commands you ran.
- Library versions.
- Hardware.
- Surprises you hit.

This is reusable for your team and for follow-on work.

## See also

- `../evaluation/reproducibility.md` — env / Docker drift specifically.
- `baseline-selection.md` — picking a target paper.
