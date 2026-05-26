# Problem: compute budget — rollout vs train vs eval split

## TL;DR for typical agentic-RL

- **Rollout: 60-80%** of total compute.
- **Training: 15-30%**.
- **Eval: 5-10%**.

Long-horizon agents push rollout share even higher (80-90%).

## Why rollout dominates

For agentic RL:

- Each prompt generates N rollouts (group size).
- Each rollout is K turns (multi-turn).
- Each turn invokes a tool (some fast, some slow).
- vLLM/SGLang generates tokens.
- Trainer sits idle during rollout (in sync mode).

Total = N × K × (gen_tokens + tool_latency) per prompt.

## Concrete numbers from corpus

These are rough guides; real numbers depend on hardware.

### Search-R1 7B on 8xH100

- ~24 hours for ~1000 steps.
- ~70% rollout, 25% train, 5% eval.

### IGPO 7B (BrowseComp + multiple)

- Larger because of search latency.
- ~80% rollout.

### SWE-Swiss 32B on 8xH100

- Training time dominated by long context + sandbox spin-up.
- ~85% rollout.

## How to reduce rollout cost

### Async rollout

> **AReaL** — github: `https://github.com/inclusionAI/AReaL`,
> paper: `https://arxiv.org/abs/2505.24298`. Decouples rollout and train.

Trade-off: staleness (see `../training/async-rollout-staleness.md`).

### Pre-cached search / tool outputs

For deterministic tools, cache. Search-R1 caches Wikipedia retrieval.
ZeroSearch simulates the engine entirely.

### Smaller group N

N=8 is often enough. N=16 doubles rollout cost.

### Bound max turns

Catastrophic episodes burn budget without learning.

### Shorter response length

Cap at 4K instead of 8K if your task allows.

### Fewer eval runs

Run full eval at end of run, not every step. Use small lite subset for
checkpoint comparison.

## How to scale up

Most published agentic-RL is 7B on 8 GPUs. To go larger:

- 32B+ usually needs 8-16 H100 with FSDP/Megatron.
- 70B needs sharding + careful memory tuning.
- 100B+ requires LoRA RL (see `../training/lora-rl.md`).

## Compute-vs-results trade-offs in the corpus

- **DR-Venus 4B** beats much larger models on BrowseComp. Edge-scale
  efficiency.
- **Skywork-OR1** uses large-scale rule-based RL. Compute-heavy but
  competitive without PRM.
- **CUDA-L1 / L2** uses contrastive RL with hardware-grounded reward.
  Cheap reward, focused training.

## Compute reporting

In your paper:

- Report total GPU-hours.
- Report hardware used (H100, A100, etc.).
- Report split between rollout and train.

Most papers under-report this. Reviewers can't compare methods without
it.

## See also

- `../training/rollout-throughput.md`
- `../training/oom-during-training.md`
- `../training/lora-rl.md`
