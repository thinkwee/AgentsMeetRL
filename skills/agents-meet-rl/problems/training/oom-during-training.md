# Problem: OOM during training (actor / rollout / value-net memory peaks)

## Symptoms

- CUDA OOM mid-training, often at first GAE/value-loss computation.
- OOM only on long rollouts; short ones fit.
- OOM at rollout time when many rollouts run in parallel.
- Memory fragmentation: free memory exists but allocation fails.

## Root causes

1. **Large response length × group size N × micro-batch** swamps actor
   activations.
2. **vLLM/SGLang KV cache** competing with training-side allocator.
3. **Long context window** (32K+ for agentic).
4. **VLM image tokens** add huge overhead.
5. **No gradient checkpointing.**
6. **No sequence packing.**

## Diagnosis

- `nvidia-smi` during training to find peak memory step.
- veRL has `gpu_memory_utilization` option; tune to leave headroom.
- Debug OOM at rollout vs train: which phase peaks?

## Fixes

### Fix: gradient checkpointing

veRL supports it. Cuts activation memory ~40%, costs ~30% extra compute.
Default for any model > 7B.

### Fix: sequence packing

Pack short rollouts together to reduce padding waste. veRL uses
flash-attn 2 with sequence packing enabled.

### Fix: micro-batch tuning

Reduce per-GPU micro-batch. Compensate with gradient accumulation.

### Fix: separate vLLM/SGLang from trainer (different GPUs)

Most production setups put rollout engine on different GPUs from
trainer to avoid memory conflict. veRL supports this via flexible
device mapping.

### Fix: FSDP / FSDP2

Shards the model + optimizer state across GPUs. Necessary for >7B.
veRL supports FSDP, FSDP2, Megatron-LM.

### Fix: LoRA RL

Massive memory reduction by training adapters only.

> **veRL** — github: `https://github.com/volcengine/verl`,
> paper: `https://arxiv.org/abs/2409.19256`, ByteDance Seed, date: 2024.9.
> See veRL's LoRA-RL configuration. Useful for trillion-parameter models
> or memory-constrained setups. See `lora-rl.md`.

### Fix: Megatron backend for huge models

For 70B+ MoE: veRL + Megatron-Bridge.

### Fix: cap response length

If most OOMs are at long-rollout time, cap response length (e.g. 4K)
and accept the trade-off.

### Fix: cap N (group size)

GRPO's N=16 doubles memory vs N=8. Often N=8 is enough.

### Fix: bf16 or fp8 for activations

Most agentic-RL papers use bf16. fp8 (with care) is possible on H100.

## Paper / repo references

- `slime` — github: `https://github.com/THUDM/slime`,
  blog: `https://lmsys.org/blog/2025-07-09-slime/`, Tsinghua, date: 2025.6.
- `NeMo-RL` — github: `https://github.com/NVIDIA-NeMo/RL`, NVIDIA,
  date: 2026.1. Megatron-native, designed for huge models.
