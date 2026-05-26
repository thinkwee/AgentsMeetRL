# Question: bf16 / fp16 / fp32 / fp8 — what to use where

## TL;DR matrix

| Component | Recommended | Why |
|---|---|---|
| Model weights (forward) | bf16 | Standard; minimal accuracy loss |
| Model weights (master copy in optimizer) | fp32 | Adam needs precision |
| Forward activations | bf16 | Fits memory; fine numerically |
| Gradient computation | bf16 | Same |
| Gradient accumulation | fp32 | Many small updates compound errors |
| **Log-prob computation** | **fp32** | **bf16 underflows on extreme logits** |
| Reward | fp32 | Trivial cost; safer |
| KL divergence | fp32 | Differences are small; bf16 cancels them |
| Advantage normalization | fp32 | Same |
| vLLM/SGLang inference | bf16 default | Fine for generation |
| Loss reduction | fp32 | Accumulate in fp32 |
| fp8 weights | only on H100+ with care | Saves memory but watch numerics |

## Where bf16 silently kills agentic RL

### 1. Log-prob computation

The model emits logits in bf16. Computing log-prob requires:

```python
log_probs = log_softmax(logits / temperature, dim=-1)  # bf16: WRONG
```

When `logits` has values like `-30` for low-prob tokens, the softmax
denominator is dominated by the `+10`-range tokens, and the
log-softmax for the `-30` token underflows to `-inf` in bf16. Then:

- Importance ratio `exp(log_p_new - log_p_old)` is `inf` or NaN.
- Gradient contains NaN.
- Training crashes.

**Fix**: cast to fp32 *before* log_softmax.

```python
log_probs = log_softmax(logits.float(), dim=-1)  # fp32: CORRECT
```

veRL ships this by default (`compute_log_probs` runs in fp32). When
you fork a custom training loop, this is the first thing to verify.

### 2. KL divergence

```python
# bf16: small KL values get rounded to 0
kl = (log_p - log_q).sum(dim=-1)

# fp32: preserves the gradient
kl = (log_p.float() - log_q.float()).sum(dim=-1)
```

KL between two close distributions has tiny values (1e-3 range). bf16
has ~3 decimal digits of precision; KL of 0.001 may round to 0 or to
0.005 — either way, your KL signal is corrupted.

### 3. Gradient accumulation

For large effective batch:

```python
for micro_batch in range(N):
    loss = compute_loss(...)
    loss.backward()           # accumulates into .grad
optimizer.step()
```

If `.grad` is bf16, summing N micro-batch gradients accumulates
bf16-rounding errors. Use:

```python
optimizer = AdamW(model.parameters(),
                  ...,
                  master_weights_dtype=torch.float32)  # fp32 master
```

Most frameworks (DeepSpeed, FSDP, Megatron) handle this if you set
`bf16=True, master_weights=True`.

## Symptoms of mixed-precision bugs

| Symptom | Suspect |
|---|---|
| NaN gradients after specific batches | Log-prob in bf16 |
| KL stuck at exactly 0 | KL computed in bf16, underflowed |
| Importance ratio occasionally 1e10 | Same |
| Reward looks correct but loss is huge | Numerator/denom in different precisions |
| Training fine on small model, NaN on large | Activations in bf16 + extreme logits |
| Eval differs slightly between runs on same hardware | Reduction non-determinism |

## fp8 (H100-only, advanced)

Saves memory and compute on H100. Two formats:

- E4M3: better for forward (more precision around 0).
- E5M2: better for gradients (more dynamic range).

```python
# transformer_engine
from transformer_engine.pytorch import fp8_autocast, DelayedScaling

fp8_recipe = DelayedScaling(margin=0, interval=1, fp8_format=Format.HYBRID)
with fp8_autocast(enabled=True, fp8_recipe=fp8_recipe):
    output = model(input)
```

Only worth it for:

- Very large models (70B+) where memory is the bottleneck.
- Production training runs that have been validated.
- Stable, well-understood loss curves.

For agentic-RL research where you're iterating, fp8 adds debugging
complexity that usually isn't worth the speedup.

## Determinism flags (when you need exact reproducibility)

bf16 reductions are inherently non-deterministic across rank counts
and hardware. To force bit-identical reproduction:

```python
import torch
import os

torch.use_deterministic_algorithms(True)
torch.backends.cudnn.deterministic = True
torch.backends.cudnn.benchmark = False
os.environ["CUBLAS_WORKSPACE_CONFIG"] = ":4096:8"
os.environ["NCCL_ALGO"] = "Tree"   # forces deterministic NCCL
```

Cost: 10-30% throughput hit. Use for ablation runs where you need
seed-controlled comparison; turn off for production.

## Per-component config

### Model

```yaml
model:
  dtype: bfloat16              # weights and activations
  use_fast_attention: true     # flash-attn 2
```

### Optimizer

```yaml
optim:
  type: adamw
  master_weights_dtype: float32   # fp32 master copy
  use_fused: true
```

### Loss / log-prob

```python
def compute_logprob(logits, labels):
    log_probs = F.log_softmax(logits.float(), dim=-1)   # fp32
    return log_probs.gather(-1, labels.unsqueeze(-1)).squeeze(-1)

def compute_kl(log_p, log_q):
    return (log_p.float() - log_q.float()).sum(dim=-1)
```

### vLLM / SGLang

```python
llm = LLM(
    model=model_path,
    dtype="bfloat16",            # same as training
    kv_cache_dtype="auto",        # bf16 by default
    quantization=None,            # avoid for RL training
)
```

If you quantize for inference (e.g. AWQ, GPTQ), the inference logits
will not match training logits — your `old_log_probs` are corrupted.
Match precision exactly between training and rollout.

## Hardware notes

| GPU | bf16 | fp16 | fp8 | Notes |
|---|---|---|---|---|
| A100 | Yes | Yes | No | bf16 standard |
| H100 | Yes | Yes | Yes (E4M3/E5M2) | Tensor cores accelerate fp8 |
| H200 | Yes | Yes | Yes | More memory than H100 |
| L40 | Yes | Yes | Limited | bf16 standard |
| MI300X (AMD) | Yes | Yes | No | Different ecosystem; fewer optimized kernels |

bf16 ops are not bit-identical across A100/H100 even with same code.
Document your hardware in the run config.

## Common bugs

### Bug 1: forgot to cast log-prob to fp32

By far the most common. Symptom: NaN gradients after random batches.
Fix: `logits.float()` before any softmax / log-softmax.

### Bug 2: vLLM in fp16, training in bf16

vLLM defaults to bf16 if model card says bf16. If you forced
`dtype=float16`, log-probs computed at rollout will not match
training-side log-probs. KL / ratio bugs follow.

### Bug 3: quantized inference in RL

AWQ/GPTQ-quantized model emits different logits than the unquantized
one. Don't quantize the rollout engine during RL.

### Bug 4: gradient checkpointing + bf16 + MoE

Specific failure mode at MoE training: bf16 + grad-checkpoint +
expert-parallel can lose precision in activation recomputation. Test
with a smoke run.

### Bug 5: master weight init from bf16 checkpoint

Loading a bf16 checkpoint as the fp32 master loses precision before
training even starts. Load weights in fp32 directly:

```python
model = AutoModel.from_pretrained(path, torch_dtype=torch.float32)
```

Then convert activations / forward to bf16 in the training loop.

## Numerical sanity check

Run before any long training:

```python
# 1. Same prompt, two engines, compare log-probs.
prompt_ids = tokenizer.encode("Tell me a joke.")
logp_train = trainer_compute_logprob(model, prompt_ids)
logp_vllm  = vllm_compute_logprob(prompt_ids)
delta = (logp_train - logp_vllm).abs().max()
assert delta < 0.01, f"Precision mismatch: max delta {delta}"

# 2. KL of policy vs itself = 0.
kl_self = compute_kl(model, model, sample_batch)
assert kl_self.abs().max() < 1e-6, f"KL self-mismatch: {kl_self}"
```

Both checks should pass at training start. If not, you have a precision
bug.

## Paper / repo references

> **veRL** — github: `https://github.com/volcengine/verl`,
> paper: `https://arxiv.org/abs/2409.19256`, ByteDance Seed, date: 2024.9.
> Why: production-grade mixed-precision training; ships
> fp32 log-prob, fp32 master weights, fp32 KL by default. Fork these
> defaults rather than rolling your own.

> **OpenRLHF** — github: `https://github.com/OpenRLHF/OpenRLHF`,
> paper: `https://arxiv.org/abs/2405.11143`, OpenLLMAI, date: 2024.5.
> Why: independent reference; cross-check when veRL behaves
> unexpectedly under mixed precision.

> **AReaL** — github: `https://github.com/inclusionAI/AReaL`,
> paper: `https://arxiv.org/abs/2505.24298`, AntGroup/Tsinghua,
> date: 2025.5. Why: documents staleness + numerics issues for async
> pipelines specifically.

> **slime** — github: `https://github.com/THUDM/slime`, THUDM.
> Why: lightweight framework; clean reference for mixed-precision
> defaults.

> **NeMo-RL** — github: `https://github.com/NVIDIA-NeMo/RL`, NVIDIA,
> date: 2026.1. Why: Megatron-native; supports fp8 training for huge
> models with care.

## See also

- `nan-grads.md` — when mixed-precision causes NaNs.
- `kl-explosion.md` — when KL is corrupted by precision.
- `importance-ratio-blowup.md` — common downstream symptom.
- `../evaluation/reproducibility.md` — determinism flags for exact
  reproduction.
- `oom-during-training.md` — fp8 trade-offs at scale.
