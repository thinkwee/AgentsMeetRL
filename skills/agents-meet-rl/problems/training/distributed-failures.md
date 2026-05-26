# Problem: distributed training fails — NCCL hangs, partial-rank failures, allreduce slowness

## Symptoms

- Training looks fine for hours, then deadlocks. No progress; no error.
- One rank reports OOM; the others wait forever.
- Allreduce is 10× slower than nominal interconnect bandwidth.
- Multi-node run loses tokens silently between nodes.
- Reward, loss, KL diverge across ranks (each rank sees a different
  number).

## Root causes

1. **Per-rank state divergence.** One rank skipped a step due to OOM /
   NaN, others waited at the next collective.
2. **Async rollout puts ranks at different policy versions.** When the
   trainer collects, ranks have inconsistent old_log_probs.
3. **NCCL timeout too long.** Default is 30 minutes; deadlock manifests
   only after long delay.
4. **InfiniBand vs Ethernet mis-config.** Bandwidth degrades silently.
5. **GPU topology mismatch.** PCIe-isolated ranks doing P2P collective.
6. **FSDP shard misalignment** when model architecture changes between
   restart and original run.

## Diagnosis

### Per-rank logging

Log per-rank metrics (not just rank 0):

```python
import torch.distributed as dist

local_loss = loss.item()
all_losses = [None] * dist.get_world_size()
dist.all_gather_object(all_losses, local_loss)
if dist.get_rank() == 0:
    print({i: v for i, v in enumerate(all_losses)})
```

Healthy: all ranks within 1% of mean. Sick: one rank outlier (sign of
divergence) or one rank `None` (rank stalled).

### NCCL debug

```bash
export NCCL_DEBUG=INFO
export NCCL_DEBUG_SUBSYS=COLL,P2P,NET
```

Logs every collective. Spot the first divergence (rank A starts
allreduce at step T; rank B never starts).

### NCCL timeout reduction

Default NCCL timeout is 30 minutes (1800 seconds). Reduce to expose
hangs faster:

```bash
export NCCL_TIMEOUT=120          # 2 minutes
```

Now hangs raise an error in 2 minutes, not 30. Stack trace reveals
which collective deadlocked.

### Bandwidth check

```bash
# Single-node, multi-GPU bandwidth
nccl-tests/build/all_reduce_perf -b 8 -e 256M -f 2 -g 8

# Multi-node
mpirun ... ./build/all_reduce_perf ...
```

H100 NVLink should hit ~600 GB/s on 8 GPUs. PCIe < 32 GB/s. If your
measured number is half nominal, your topology or NCCL config is off.

### Topology

```bash
nvidia-smi topo -m
```

Look for `NV4` (NVLink 4 hops) or `PHB` (PCIe through host bridge) on
adjacent ranks. PHB-only rings are slow; force NCCL to use a tree
topology in that case.

## Fixes

### Fix 1: per-rank skip-step is poison

If your training loop has:

```python
if loss.isnan().any():
    continue   # this rank skips, others wait at allreduce → deadlock
```

Don't. Either:

- All ranks decide collectively to skip:

  ```python
  any_nan = loss.isnan().any().int()
  dist.all_reduce(any_nan)
  if any_nan.item() > 0:
      optimizer.zero_grad()
      continue   # all ranks
  ```

- Or have the bad rank raise, terminate the whole job, and rely on
  job-restart logic.

### Fix 2: NCCL_ALGO and NCCL_NTHREADS

For specific topologies:

```bash
export NCCL_ALGO=Tree            # or Ring; experiment
export NCCL_NTHREADS=512         # default is 256
export NCCL_PROTO=Simple         # or LL, LL128
```

Trial-and-error — what works depends on your fabric.

### Fix 3: pin NCCL version

NCCL bugs across versions are real. Pin the specific NCCL that worked
for the framework version you use.

```bash
# in container
pip install torch==2.4.0 --index-url ...
# torch 2.4 ships NCCL 2.20; some agentic-RL frameworks need 2.18 or
# 2.22 specifically.
```

veRL, OpenRLHF Dockerfiles encode the working NCCL version.

### Fix 4: timeouts and graceful failure

```python
# At process start
dist.init_process_group(
    backend="nccl",
    timeout=datetime.timedelta(seconds=600),
)

# In training loop
try:
    dist.all_reduce(grad)
except RuntimeError as e:
    if "NCCL" in str(e):
        # log diagnostic state, then exit
        save_diagnostic()
        os._exit(1)
```

Better to fail loudly than hang silently.

### Fix 5: FSDP vs Megatron pick

| Model size | Recommended |
|---|---|
| ≤ 7B | FSDP1 or FSDP2 |
| 7-30B | FSDP2 |
| 30-70B | FSDP2 with CPU offload, or Megatron-LM |
| 70B+ MoE | Megatron-LM via veRL's Megatron-Bridge |

FSDP is simpler; Megatron is more efficient on big models.

### Fix 6: gradient sync correctness check

Before long training, verify gradients are actually synchronized:

```python
# Identical input on all ranks → identical gradient after sync
fixed_input = ...   # same on all ranks
fixed_input = fixed_input.to(device)

loss = compute_loss(model, fixed_input)
loss.backward()

grad_sum = torch.tensor(0.0, device=device)
for p in model.parameters():
    if p.grad is not None:
        grad_sum += p.grad.abs().sum()

all_grad_sums = [None] * world_size
dist.all_gather_object(all_grad_sums, grad_sum.item())
assert all(abs(x - all_grad_sums[0]) < 1e-3 for x in all_grad_sums), \
    f"Gradient mismatch across ranks: {all_grad_sums}"
```

Run as smoke test at job start. If this fails, FSDP / DeepSpeed
config is broken.

### Fix 7: separate vLLM/SGLang on dedicated GPUs

Mixing inference and training on the same GPUs causes:

- Allocator fragmentation.
- Stream synchronization races.
- vLLM's KV cache competes with FSDP shards.

Most production setups put rollout on different GPUs:

```
Trainer:    GPUs 0-3
vLLM:       GPUs 4-7
```

veRL supports this via flexible device mapping.

### Fix 8: bound async-rollout staleness

In async pipelines, ranks at different policy versions cause subtle
divergence. Bound the gap:

```python
if generation_step - latest_train_step > MAX_STALENESS:
    wait_for_train_to_catch_up()
```

See `async-rollout-staleness.md`.

## Common bug patterns

### Bug 1: rank 0 saves checkpoint, others wait

Most checkpoint code is rank-0-only. If rank 0 hits an error, the rest
hang at the next allreduce. Wrap checkpointing in try/except + barrier:

```python
try:
    if rank == 0:
        save_checkpoint(...)
finally:
    dist.barrier()    # all ranks must reach this
```

### Bug 2: dataloader worker has rank-specific seed but shared dataset

If multiple ranks read from a non-rank-aware dataset, they may get
overlapping data → optimizer sees same example twice. Use
`DistributedSampler`:

```python
sampler = DistributedSampler(dataset, num_replicas=world_size, rank=rank)
loader = DataLoader(dataset, sampler=sampler, ...)
```

### Bug 3: tensor of different shape on different ranks → allreduce hang

Common when sequence length varies and you forgot to pad:

```python
# Each rank has different shape
local_logits = ...    # [batch, seq_len_local, vocab]
dist.all_reduce(local_logits)   # HANGS if shapes differ
```

Pad to a common length before any allreduce.

### Bug 4: model architecture differs across ranks

If you accidentally load a different LoRA adapter on different ranks
(or have some ranks with extra modules), FSDP shards align wrong.
Catastrophic. Always load the same model on all ranks; verify with
parameter count check.

### Bug 5: NCCL_BLOCKING_WAIT vs NCCL_ASYNC_ERROR_HANDLING

```bash
export TORCH_NCCL_BLOCKING_WAIT=1          # wait for completion
export TORCH_NCCL_ASYNC_ERROR_HANDLING=1   # raise on error
```

Without these, some errors silently corrupt. With these, errors raise.
Use them.

## Debugging recipe when training hangs

1. Run with `NCCL_TIMEOUT=120` to force fast failure.
2. Check `dmesg` for NCCL or driver errors.
3. Check `nvidia-smi` to see if any GPU is at 0% util while others are
   at 100% — that rank stalled.
4. Get the stack trace at hang time:
   ```bash
   pyspy dump --pid <python_pid>
   ```
5. Look at "first divergent step" between ranks; whatever happened
   that step is the cause.

## Paper / repo references

> **veRL** — github: `https://github.com/volcengine/verl`,
> paper: `https://arxiv.org/abs/2409.19256`, ByteDance Seed, date: 2024.9.
> Why: production-grade FSDP/Megatron support; reference
> Dockerfiles encode working NCCL versions.

> **OpenRLHF** — github: `https://github.com/OpenRLHF/OpenRLHF`,
> paper: `https://arxiv.org/abs/2405.11143`, OpenLLMAI, date: 2024.5.
> Why: independent reference for distributed PPO training.

> **slime** — github: `https://github.com/THUDM/slime`, THUDM.
> Why: lightweight; simpler distributed setup makes debugging easier.

> **NeMo-RL** — github: `https://github.com/NVIDIA-NeMo/RL`, NVIDIA,
> date: 2026.1. Why: Megatron-native, designed for the trillion-
> parameter regime where distributed correctness matters most.

> **AReaL** — github: `https://github.com/inclusionAI/AReaL`,
> paper: `https://arxiv.org/abs/2505.24298`, AntGroup/Tsinghua,
> date: 2025.5. Why: documents async rollout staleness handling, which
> is a major distributed-correctness concern.

## See also

- `oom-during-training.md` — OOM is a frequent precursor to NCCL hang.
- `async-rollout-staleness.md` — async-specific distributed issue.
- `nan-grads.md` — NaN handling must be collective, not per-rank.
- `../evaluation/reproducibility.md` — determinism flags interact with
  distributed.
