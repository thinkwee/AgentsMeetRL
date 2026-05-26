# Problem: rollout phase keeps GPUs idle

## Symptoms

- Trainer GPUs are idle during rollout.
- Rollout takes 60–80% of step time.
- Throughput far below theoretical max.

## Root causes

1. Synchronous rollout: trainer waits for all N rollouts to finish.
2. Slow env (real-time API, sandbox spin-up).
3. Long rollouts with bursty completion.
4. vLLM/SGLang batch-size too small.
5. Network or disk bottleneck on env outputs.

## Diagnosis

- Wandb panels for `rollout_time / step_time`. Should be < 0.5 for
  good utilization.
- vLLM/SGLang has its own metrics for queue depth, batch fill rate.
- Profile end-to-end with `py-spy` or NVIDIA Nsight.

## Fixes

### Fix: async rollout

Decouple rollout from training; the trainer doesn't wait. Trade-off:
staleness (see `async-rollout-staleness.md`).

> **AReaL** — `https://github.com/inclusionAI/AReaL`,
> paper: `https://arxiv.org/abs/2505.24298`. Built for this.

> **prime-rl** — `https://github.com/PrimeIntellect-ai/prime-rl`.

> **veRL fully_async_policy** — github: `https://github.com/volcengine/verl`,
> ByteDance Seed. veRL ships an experimental fully-async policy mode
> that decouples actor rollout from training; useful when you want
> async without leaving the veRL ecosystem.

> **openrlhf_async_pipline** — github:
> `https://github.com/yyht/openrlhf_async_pipline`,
> paper: `https://arxiv.org/abs/2405.11143`, date: 2024.5.

### Fix: separate rollout engine on dedicated GPUs

Run vLLM/SGLang on a dedicated set of GPUs, trainer on another set.
Eliminates allocator conflict.

### Fix: increase vLLM/SGLang batch size

If your rollout is bottlenecked by individual prompts, larger batch =
more throughput. vLLM auto-batches.

### Fix: continuous batching

vLLM ≥ 0.5 supports continuous batching (paged attention). Free
performance.

### Fix: pre-fetch tools

If env makes external API calls, pre-fetch / cache. Most ZeroSearch-
style simulated envs do this implicitly.

### Fix: parallel envs per rollout worker

If env is slow (Docker spin-up), run multiple envs concurrently per
worker.

### Fix: smaller groups for slow envs

If env is the bottleneck and N is large, reduce N. The variance hit is
often less than the throughput gain.

## Practical numbers

- veRL + vLLM on 8 H100: ~15-30K token/s policy generation.
- SkyRL-Agent with concurrency: many concurrent envs per worker.
- If you're seeing < 5K token/s, something is wrong.

## Paper / repo references

- `AReaL` — github: `https://github.com/inclusionAI/AReaL`,
  paper: `https://arxiv.org/abs/2505.24298`, AntGroup/Tsinghua, date: 2025.5.
- `prime-rl` — github: `https://github.com/PrimeIntellect-ai/prime-rl`,
  Prime Intellect, date: 2025.2.
- `OpenRLHF` — github: `https://github.com/OpenRLHF/OpenRLHF`,
  paper: `https://arxiv.org/abs/2405.11143`, date: 2024.5.

**Other corpus entries:**

- `youtu-agent` — Training-Free GRPO removes rollout cost entirely — useful as throughput upper bound.
  github: `https://github.com/TencentCloudADP/youtu-agent`, paper: `https://arxiv.org/abs/2512.24615`, Tencent Youtu Lab, date: 2025.12

- `DEPO` — KTO + Efficiency Loss reduces tokens-per-update.
  github: `https://github.com/OpenCausaLab/DEPO`, paper: `https://arxiv.org/abs/2511.15392`, HKUST/SJTU, date: 2025.11

- `MobileAgent` — semi-online RL pattern for GUI.
  github: `https://github.com/X-PLUG/MobileAgent`, paper: `https://arxiv.org/abs/2509.11543`, X-PLUG (TongyiQwen), date: 2025.9

- `Claw-R1` — generic RL framework on multi-turn agent tasks.
  github: `https://github.com/AgentR1/Claw-R1`, USTC, date: 2026.3
