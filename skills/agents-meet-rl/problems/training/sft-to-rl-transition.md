# Problem: RL diverges immediately after SFT cold start

## Symptoms

- After SFT, model performs well on dev set.
- First few hundred steps of RL: reward is 0, KL explodes, training is
  unstable.
- Model "forgets" SFT behavior fast (length, format, tool calls).
- Sometimes reward looks fine for 1000 steps then collapses (delayed
  forgetting).

## Root causes

1. **SFT format ≠ RL format.** Tokens, tags, special boundaries differ.
2. **KL anchor too weak / strong.** β too small ⇒ drift; β too large ⇒
   policy can't move at all.
3. **Reference model is the SFT model — but it shouldn't be.** Or vice
   versa. Both choices have implications.
4. **SFT data is too narrow.** RL exposes model to states the SFT
   distribution didn't cover.
5. **SFT was on different tokenizer / chat template** than RL pipeline.
6. **Optimizer state mishandling.** Loading SFT checkpoint but resetting
   optimizer can cause early instability.

## Multi-stage pattern (the corpus's consensus)

Almost every successful long-horizon agentic-RL paper uses **multi-stage**
training:

```
Stage 1: SFT on demonstrations (often distilled from a strong model)
Stage 2: Offline RL or rejection-sampling fine-tuning (RFT/DPO) on labeled trajectories
Stage 3: Online RL (PPO/GRPO) with verifiable reward
```

References:

> **MobileRL** — github: `https://github.com/THUDM/MobileRL`,
> paper: `https://arxiv.org/abs/2509.18119`, THUDM, date: 2025.9.
> SFT → offline RL → online RL pipeline. Mobile GUI.

> **Mano-P** — github: `https://github.com/Mininglamp-AI/Mano-P`,
> paper: `https://arxiv.org/abs/2509.17336`, Mininglamp AI, date: 2025.9.
> Same three-stage pipeline for OSWorld.

> **Tool-Star** — github: `https://github.com/dongguanting/Tool-Star`,
> paper: `https://arxiv.org/abs/2505.16410`, RUC, date: 2025.5.
> Multi-stage SFT, then PPO/DPO/ORPO/SimPO/KTO mix.

> **MedResearcher-R1** — github:
> `https://github.com/AQ-MedAI/MedResearcher-R1`,
> paper: `https://arxiv.org/abs/2508.14880`, Ant Group, date: 2025.8.
> SFT + Online RL.

> **AgentCPM-GUI** — github: `https://github.com/OpenBMB/AgentCPM-GUI`,
> paper: `https://arxiv.org/abs/2506.01391`, OpenBMB/Tsinghua/RUC, date: 2025.6.
> SFT + GRPO for mobile GUI.

> **Doctor-R1** — github: `https://github.com/thu-unicorn/Doctor-R1`,
> paper: `https://arxiv.org/abs/2510.04284`, Tsinghua, date: 2025.10.
> Experiential agentic RL after SFT.

> **ToolMaster** — github: `https://github.com/NEUIR/ToolMaster`,
> paper: `https://arxiv.org/abs/2601.12762`, NEUIR, date: 2026.1.
> SFT + GRPO trial-then-execute.

## Diagnosis

- Compute KL at init (step 0). Must be exactly 0. Non-zero = template
  mismatch.
- For each rollout in step 1, compute reward. If 100% have 0 reward,
  there's a format bug between SFT and RL.
- Plot reward, KL, entropy on the same x-axis for the first 500 steps.
  Healthy: reward starts moderate, climbs slowly; KL stays < 1; entropy
  decreases gently. Sick: reward 0 throughout, KL spikes, entropy
  collapses.

## Fixes

### Fix 1: SFT must produce trajectories in RL parser format

If SFT produced `<search>foo</search>` and RL parser wants
`<tool_call>{"name": "search", ...}</tool_call>`, the model effectively
restarts. Match exactly.

This is the most common silent killer.

### Fix 2: tune β / KL coefficient

Start with β around 1e-3 (most papers in the corpus). If KL still
blows up: 1e-2. If model can't learn: 1e-4.

> veRL exposes this via the `KLControlConfig` knobs (`kl_loss_coef`,
> `kl_penalty`).

For partial-reward tasks: use higher β (GUI-Libra-style):

> **GUI-Libra** — github: `https://github.com/GUI-Libra/GUI-Libra`,
> paper: `https://arxiv.org/abs/2602.22190`, date: 2026.2.

### Fix 3: reference model = SFT model (not base)

For agentic RL, the reference model should be the SFT-trained checkpoint
— that's the behavior you want to anchor against. Setting
reference=base will let the policy drift away from SFT into junk
quickly.

### Fix 4: warm up with rejection-sampling / RFT

Before online RL, run *one* offline pass:

- Sample N rollouts per prompt with the SFT model.
- Filter to high-reward ones.
- Fine-tune SFT on filtered set.

Cheaper than RL, often gives most of the gains. Many papers (Mano-P,
MobileRL) put this between SFT and online RL.

### Fix 5: keep entropy bonus during early RL

Small entropy coefficient (e.g. 0.001) early helps avoid premature
collapse. Decay later.

### Fix 6: smaller learning rate at RL start

Standard SFT LR is ~1e-5; RL LR often 1e-6 to 5e-6. Larger LR at RL
start commonly causes early divergence.

## Paper / repo references

- All multi-stage references above. The consensus pattern is universal
  in long-horizon agentic-RL.

**Other corpus entries:**

- `STeCa` — DPO-style RFT for embodied/household.
  github: `https://github.com/WangHanLinHenry/STeCa`, paper: `https://arxiv.org/abs/2502.14276`, The Hong Kong Polytechnic University, date: 2025.2

- `Embodied-R1` — GRPO RFT after SFT for grounding/waypoint.
  github: `https://github.com/pickxiguapi/Embodied-R1`, paper: `http://arxiv.org/abs/2508.13998`, Tianjing University, date: 2025.8

- `AutoVLA` — GRPO RFT after SFT for autonomous driving.
  github: `https://github.com/ucla-mobility/AutoVLA`, paper: `https://arxiv.org/abs/2506.13757`, UCLA Mobility Lab, date: 2025.6

- `VIKI-R` — GRPO RFT after SFT for multi-robot cooperation.
  github: `https://github.com/MARS-EAI/VIKI-R`, paper: `https://arxiv.org/abs/2506.09049`, MARS-EAI (NeurIPS 2025 D&B), date: 2025.6

- `agent-distillation` — supervised distillation as RL warmup baseline.
  github: `https://github.com/Nardien/agent-distillation`, paper: `https://arxiv.org/abs/2505.17612`, KAIST, date: 2025.5
