# Problem: can't reproduce my own / others' numbers

## Symptoms

- Re-run same training, get different result.
- Re-run someone else's open-source recipe, get worse number than they
  reported.
- Eval today gives different result than eval yesterday.

## Common reasons (in this corpus)

### 1. Library version drift

Most agentic-RL repos pin loose version ranges. Different commit/version
of vLLM, SGLang, transformers, flash-attn → different output.

**Fix**: pin everything. Use the exact tag from the paper. veRL ships
release tags; use them.

### 2. Tokenizer / chat template drift

Tokenizer config changes between model checkpoints (Qwen 2.5 to 3, Llama
3 to 3.1) silently. Chat templates are a moving target.

**Fix**: pin tokenizer version. Save tokenizer with checkpoint.

### 3. Inference engine version

vLLM 0.4 vs 0.5 vs 0.6 produce different outputs in edge cases. SGLang
similar.

**Fix**: pin inference engine. Search-R1's README pins specific vLLM
versions per recipe — copy the version they used.

### 4. Sampling seed

Random seed not pinned. Eval with T>0 will vary.

**Fix**: pin seed in eval. Run with multiple seeds for proper CI.

### 5. Env / Docker drift

Docker base images change. SWE-Bench specifically requires per-task
Docker images that drift.

**Fix**: pin Docker SHA, not tag.

### 6. API drift

GPT-4o, Claude get model updates. Anthropic / OpenAI deprecate
versions.

**Fix**: pin model snapshot string when used as judge.

### 7. Hardware-specific

A100 vs H100 vs L40 — flash-attn behaves slightly differently. Bf16
ops aren't bit-identical across hardware.

**Fix**: report hardware. Don't expect 100% reproducibility across
GPU types.

### 8. Determinism flags

PyTorch determinism is not on by default. NCCL is non-deterministic.
Bf16 reductions vary.

**Fix**:
```python
torch.use_deterministic_algorithms(True)
os.environ["CUBLAS_WORKSPACE_CONFIG"] = ":4096:8"
```
Slows training but reproducible.

### 9. Data preprocessing

Same dataset, different preprocessing → different effective training
data.

**Fix**: ship preprocessed data alongside model.

### 10. Wandb / log conflation

Reading wrong wandb run as your "result." Always commit code with
result; tag run.

## Reproducibility checklist

- [ ] Pinned library versions (requirements.lock).
- [ ] Tokenizer + chat template saved with model.
- [ ] Random seeds pinned.
- [ ] Docker images pinned by SHA.
- [ ] Judge model snapshot pinned.
- [ ] Hardware reported.
- [ ] Determinism flags set.
- [ ] Preprocessed data shipped or recipe pinned.
- [ ] Code commit hash in eval log.

## Reproducing others' work

When trying to reproduce a paper:

1. Use their exact setup (library versions, model, data).
2. Don't change hyperparameters yet. Hit their number first.
3. Then ablate from there.

If you can't reach their number with their setup, check:

- Did they cherry-pick best of multiple runs?
- Is there a hidden init / SFT they didn't release?
- Are you using the same evaluation harness?

## Paper / repo references

> **Search-R1** — github: `https://github.com/PeterGriffinJin/Search-R1`,
> paper: `https://arxiv.org/abs/2503.09516`, org: UIUC/Google, date: 2025.3.
> Why: best-in-class reproducibility — versioned recipe scripts (v0.1,
> v0.2, v0.3), public wandb logs, and pinned vLLM version in the README.
> Use it as the bar to clear when releasing your own work.

> **RAGEN** — github: `https://github.com/RAGEN-AI/RAGEN`,
> paper: `https://arxiv.org/abs/2504.20073`, org: RAGEN-AI, date: 2025.4.
> Why: ships public wandb dashboard with metric-level breakdown
> across runs.

> **veRL** — github: `https://github.com/volcengine/verl`,
> paper: `https://arxiv.org/abs/2409.19256`, ByteDance Seed, date: 2024.9.
> Why: release tags + Docker images make library-version
> drift fixable; pin to a tag, not main.

> **SkyRL** — github: `https://github.com/NovaSky-AI/SkyRL`,
> paper: `https://arxiv.org/abs/2511.16108`, org: UC Berkeley / NovaSky-AI, date:
> 2025.11. Why: split into `skyrl-train`/`skyrl-tx`/`skyrl-agent`/
> `skyrl-gym` — each has its own pinned version, easier to lock down.

## See also

- `data-contamination.md`
- `../research-workflow/reproducing-papers.md`
- `../training/unstable-curves.md`
