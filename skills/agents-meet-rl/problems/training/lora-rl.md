# Problem: when to use LoRA RL — and what you lose

## When LoRA RL is worth it

- Memory budget is tight (single 80GB GPU for 30B+ model).
- You want to train trillion-parameter model on small cluster.
- Iterating on reward design / data — quick experiments.
- Multiple parallel runs of similar experiments.

## When LoRA RL hurts

- You need maximum eval performance — full fine-tuning typically wins
  by 1–3 points.
- Multi-stage training: LoRA-on-LoRA accumulates approximation error.
- Very long training runs — LoRA's expressivity ceiling matters.

## Implementation

> **veRL multi-GPU LoRA RL** —
> `https://verl.readthedocs.io/en/latest/advance/ppo_lora.html`. Native
> support.

> **Mind Lab trillion-parameter GRPO LoRA on 64 H800** —
> `https://macaron.im/mindlab/research/building-trillion-parameter-reasoning-rl-with-10-gpus`.
> Demonstrates the pattern.

> **MetaClaw** — github: `https://github.com/aiming-lab/MetaClaw`,
> paper: `https://arxiv.org/abs/2603.17187`, UNC Chapel Hill (AIMING Lab),
> date: 2026.3. GRPO (LoRA) general agentic. In the corpus, MetaClaw
> uses LoRA + GRPO explicitly.

## Common gotchas

### LoRA rank

Most agentic-RL with LoRA uses rank 16–64. Too small → expressivity
gap; too large → memory savings disappear.

### Target modules

For Llama/Qwen: `q_proj, k_proj, v_proj, o_proj` is the safest set.
Adding `gate_proj, up_proj, down_proj` (FFN LoRA) adds capacity but
~2x parameters.

### LoRA + GRPO with reference model

Reference model can be the SFT model with LoRA frozen. Or the SFT
model without LoRA — depends on your warm-start setup.

### Saving / loading LoRA mid-RL

Save LoRA weights frequently. Continuing from an interrupted run with
optimizer state is harder; LoRA mid-run rollback is more common.

## Memory math

Full fine-tune Llama-3-70B FSDP: ≥ 8x80GB minimum, painful.
LoRA Llama-3-70B FSDP: 4x80GB comfortable.

For 100B+ models, LoRA is essentially mandatory at small-cluster scale.

## Paper / repo references

- `MetaClaw` — github: `https://github.com/aiming-lab/MetaClaw`,
  paper: `https://arxiv.org/abs/2603.17187`, UNC-Chapel Hill (AIMING Lab),
  date: 2026.3. GRPO (LoRA) for general agentic.
