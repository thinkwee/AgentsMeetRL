# Question: PPO vs GRPO vs DPO vs REINFORCE++ vs RLOO — which?

## When this matters

You're starting a new agentic-RL project (or porting an existing
recipe) and need to pick the RL algorithm. Picking wrong wastes 1-2
weeks before the symptoms make it obvious.

## TL;DR decision tree

```
Have only preference pairs (chosen/rejected), no env? .... DPO / IPO / SimPO
Have outcome reward + can sample N rollouts per prompt? .. GRPO  (default)
Dense per-step / PRM reward + long trajectories? ......... PPO with critic
Async rollout pipeline (bigger staleness)? ............... REINFORCE++
Episodes ≥ 50 turns, single outcome reward? .............. GiGPO  (hierarchical GRPO)
Length blowing up / token-aggregation matters? ........... DAPO   (token-level + clip-higher)
Sequence-level ratio preferred (math-style traces)? ...... GSPO
Want GRPO but simpler (no group std)? .................... RLOO   (leave-one-out)
```

## What each algorithm actually does

### PPO with critic (GAE)

The classic actor-critic. Loss:

```
L = -E[ min(ratio * Â, clip(ratio, 1-ε, 1+ε) * Â) ] + c1*L_value + c2*L_entropy
ratio = π_new(a|s) / π_old(a|s)
Â = δ_t + (γλ)δ_{t+1} + ...   (GAE advantage)
δ_t = r_t + γ V(s_{t+1}) - V(s_t)
```

Cost: critic ≈ +50% activation memory. Worth it when the critic gives
a useful per-step value estimate (dense reward, or PRM signal).

### GRPO (Group Relative Policy Optimization)

Drop the critic. Sample N rollouts per prompt, compute group-relative
advantage:

```
Â_i = (r_i - μ_group) / (σ_group + ε)
```

with `μ_group` and `σ_group` over the N rollouts. Keep PPO's clipped
surrogate for the policy update. Two big consequences:

- No critic → -50% memory.
- All-equal-reward groups give Â = 0 → silently lose those gradients.
  See `zero-variance-rollouts.md`.

This is the **default for math/code/search agents in 2025**. Pick GRPO
unless you have a reason not to.

### DAPO

GRPO + three changes that matter at long-sequence training:

1. **Token-level loss aggregation**: each token contributes equally,
   regardless of sequence length. Stops length blowup.
2. **Clip-higher (asymmetric ε)**: positive-advantage tokens allowed
   larger ratio steps than negative — exploration without instability.
3. **Overlong-shaping reward**: anticipatory length penalty before the
   max-length cap is hit.

DAPO lives as a config flip in veRL and verl-agent. See
`length-blowup.md`, `token-vs-sequence-loss.md`.

### Dr.GRPO

GRPO without the std normalization:

```
Â_i = r_i - μ_group       # no σ in denominator
```

Decouples advantage magnitude from sequence length. veRL exposes this
as `norm_adv_by_std_in_grpo=False`. Use when length is creeping up.

### GSPO

GRPO with **sequence-level** importance ratio instead of token-level:

```
ratio_seq = exp( Σ_t log_π_new(a_t) - Σ_t log_π_old(a_t) )
```

Less noisy than per-token ratios when traces are long but coherent
(math-style reasoning). Available as a config option in slime, NeMo-RL,
and verl-agent.

### RLOO (REINFORCE Leave-One-Out)

Sample N rollouts, advantage for rollout i is:

```
Â_i = r_i - (1/(N-1)) Σ_{j≠i} r_j
```

Equivalent to GRPO without the std term and without σ. Simpler to
implement; a fine starting point if you want GRPO's structure but
hate the all-equal-reward edge case.

### REINFORCE++

Vanilla REINFORCE with a few stability tricks:

- KL penalty in the loss.
- Standard advantage normalization.
- Clipping for very large advantages.

No importance ratio. Less sensitive to off-policy gap. Used in async
pipelines where staleness is hard to bound.

### DPO / IPO / SimPO (offline preference)

No env, no rollouts. Given pairs `(prompt, chosen, rejected)`:

```
L_DPO = -log σ( β [ log(π(chosen)/π_ref(chosen)) - log(π(rejected)/π_ref(rejected)) ] )
```

DPO maximizes margin between chosen and rejected log-prob ratios.
Variants:

- **IPO**: replaces sigmoid with a different loss, less aggressive on
  the margin (less likely to overconfidence).
- **SimPO**: drops the reference model; uses length-normalized
  log-prob.

When to use: you have preference data (e.g. distilled from a stronger
teacher's pairwise judgments) and don't want to spin up env / RL infra.

Trade-off: DPO **doesn't explore**. The model can only get better at
imitating your chosen samples; it won't discover behaviors not in the
preference set.

### GiGPO (hierarchical GRPO)

For long-horizon agents (50+ turns):

- **Outer group**: standard GRPO across the N rollouts of a prompt.
- **Inner group**: cluster turns *across* rollouts that share an
  observation prefix; compute a *step-level* advantage inside each
  cluster.

End result: per-step credit even when only the trajectory has reward.
Combined with a step-discounted return:

```python
for t in reversed(range(len(traj_rewards))):
    running_return = traj_rewards[t] + gamma * running_return
    traj_returns[t] = running_return
```

`gamma` is per *turn*, not per token. See `discount-factor.md`,
`credit-assignment-long-horizon.md`.

### IGPO (info-gain GRPO)

GRPO with an additional per-turn signal:

```
intrinsic_reward(turn t) = log P(answer | history + turn t)
                         - log P(answer | history)
```

Gives dense per-turn signal even when outcome reward is 0. Annealing
curriculum: info-gain weight high early, outcome weight high late.
See `sparse-reward-credit.md`.

## Decision tree explained

### "Have only preference pairs?"

If you have `(prompt, chosen, rejected)` data and no env, DPO is the
right default. Spin up an offline pass; takes 1-3 days on 8x A100 for
a 7B model. SimPO if you want to skip the reference model; IPO if
DPO collapses to high confidence on noisy preferences.

But: if you can build an env (rule-based reward, or LLM-judge), don't
stop at DPO. Online RL after DPO usually adds another 5-10 points.

### "Outcome reward + can sample N rollouts?"

Default to GRPO. The corpus consensus is N=8 to N=16. Smaller N=4 only
if compute is tight. See `grpo-knobs.md`.

If your task is *structurally* long (50+ turns) — switch to GiGPO so
per-turn credit isn't lost.

### "Dense per-step / PRM reward?"

PPO with critic earns its memory cost when the value head gives useful
per-step value estimates. Examples: trained PRM, dense format reward,
hardware-grounded reward (CUDA-L1 TFLOPs).

If your reward is sparse (only at the end), the critic adds variance
without much signal. Use GRPO instead.

### "Async pipeline?"

When rollout is decoupled from training (vLLM/SGLang separate from
trainer), staleness corrupts importance ratios. REINFORCE++ doesn't
have a per-token ratio mechanism, so it's more robust. See
`async-rollout-staleness.md`.

Alternative: keep GRPO/PPO but bound staleness explicitly (AReaL's
decoupled PPO does this).

### "Length blowing up?"

Switch to **DAPO** (token-level + clip-higher + overlong-shaping
reward) or at least flip `loss_agg_mode=token-mean` and
`norm_adv_by_std_in_grpo=False` (Dr.GRPO). See `length-blowup.md`.

### "Sequence-level ratio?"

GSPO is a reasonable choice for math/reasoning traces where the trace
is one coherent thing, not a sequence of decisions. Gives smoother
gradient than token-level on long monolithic outputs.

## What papers in the corpus actually use

| Algorithm | Where you see it |
|---|---|
| **GRPO** (vanilla) | Search-R1, R1-Searcher, Tool-Star, ReTool, Tool-N1, Skywork-OR1, RAGEN, IGPO, MobileRL/AdaGRPO |
| **DAPO** | DAPO recipe in veRL, MaskSearch, Agent_Foundation_Models |
| **Dr.GRPO** | many; especially when length matters |
| **GiGPO** | verl-agent on ALFWorld/WebShop |
| **IGPO** | IGPO on BrowseComp/HotpotQA |
| **PPO+critic** | AReaL, ReasonRAG, AgentPRM (with PRM) |
| **REINFORCE++** | OpenRLHF + async pipelines |
| **DPO/IPO/SimPO/KTO/ORPO** | Tool-Star multi-stage, MedAgentGym, ReasonRAG |
| **RLOO** | exposed as a config flag in veRL alongside GRPO |
| **GSPO** | slime as `GRPO/GSPO/REINFORCE++` toggle |

## When to mix algorithms

Most successful long-horizon agentic-RL papers use **a pipeline**:

```
SFT (cold-start)
  ↓
Rejection-sampling FT  /  DPO  /  KTO    (offline, cheap)
  ↓
Online RL (GRPO/PPO)                      (expensive, unlocks final gains)
```

DPO does not replace online RL — it pre-conditions the model so online
RL converges faster and more stably.

## Anti-patterns

### "Vanilla PPO on agentic, no critic warm-up"

Critic outputs are noise for the first ~100 steps. Reduce policy LR
or freeze policy until value head stabilizes. See `ppo-knobs.md`.

### "GRPO with N=2"

Effectively a dueling baseline. Variance reduction is poor; sparse
reward doesn't get exploited. N=8 minimum.

### "DPO on distilled-from-self preferences"

If chosen/rejected come from the same model you're training, DPO
converges to "more confident on its existing preferences" without
adding skill. Use a stronger teacher.

### "Switch algorithm mid-training to fix instability"

The fix is rarely the algorithm. Audit reward, KL, retokenization
first.

## Paper / repo references

> **veRL** — github: `https://github.com/volcengine/verl`,
> paper: `https://arxiv.org/abs/2409.19256`, ByteDance Seed, date: 2024.9.
> Why: implementations of PPO, GRPO, RLOO, REINFORCE++, plus DAPO and
> Dr.GRPO as config toggles, side by side. Reference taxonomy for the
> algorithms above.

> **OpenRLHF** — github: `https://github.com/OpenRLHF/OpenRLHF`,
> paper: `https://arxiv.org/abs/2405.11143`, OpenLLMAI, date: 2024.5.
> Why: independent reference implementation; strong REINFORCE++.

> **verl-agent** — github: `https://github.com/langfengQ/verl-agent`,
> paper: `https://arxiv.org/abs/2505.10978`, NTU, date: 2025.5.
> Why: agentic fork that exposes `PPO/GRPO/GIGPO/DAPO/RLOO/...` as
> side-by-side estimators — useful for direct comparison.

> **slime** — github: `https://github.com/THUDM/slime`, THUDM.
> Why: lightweight framework with `GRPO/GSPO/REINFORCE++` as a single
> toggle.

> **DAPO** — paper: `https://arxiv.org/abs/2503.14476`,
> blog: `https://dapo-sia.github.io/`, ByteDance Seed, date: 2025.3.
> Why: token-level loss + clip-higher + overlong-shaping reward.

> **Dr.GRPO** — paper: `https://arxiv.org/abs/2503.20783`. Length-
> stable GRPO via removing advantage std-normalization.

> **GiGPO** — github: `https://github.com/langfengQ/verl-agent`,
> paper: `https://arxiv.org/abs/2505.10978`, NTU, date: 2025.5.
> Hierarchical GRPO for long-horizon agents.

> **IGPO** — github: `https://github.com/GuoqingWang1/IGPO`,
> paper: `https://arxiv.org/abs/2510.14967`, Ant Group, date: 2025.10.
> Per-turn info-gain reward.

> **AReaL** — github: `https://github.com/inclusionAI/AReaL`,
> paper: `https://arxiv.org/abs/2505.24298`, AntGroup/Tsinghua,
> date: 2025.5. Decoupled PPO for async; reference for staleness
> handling.

**Other corpus entries:**

> **trl** — HuggingFace's PPO/GRPO/DPO; default starting reference for new researchers. github: `https://github.com/huggingface/trl`, HuggingFace, date: 2019.11.

> **RLinf** — supports PPO/GRPO/DAPO/SAC/REINFORCE++/CrossQ/RLPD in one stack — useful for A/B-ing algorithms. github: `https://github.com/RLinf/RLinf`, paper: `https://arxiv.org/abs/2509.15965`, Tsinghua/Infinigence AI/PKU, date: 2025.9.

> **siiRL** — adds CPGD and MARFT (multi-agent RL fine-tuning) alongside PPO/GRPO. github: `https://github.com/sii-research/siiRL`, paper: `https://arxiv.org/abs/2507.13833`, Shanghai Innovation Institute, date: 2025.7.

> **oat** — minimal PPO/GRPO impl; popular for math/alignment baselines. github: `https://github.com/sail-sg/oat`, paper: `https://arxiv.org/abs/2411.01493`, NUS/Sea AI, date: 2024.11.

> **RL2** — Dr.GRPO/PPO/DPO across QA and dialogue. github: `https://github.com/ChenmienTan/RL2`, Accio, date: 2025.4.

> **Open-AgentRL** — GRPO-TCR (turn-conditioned reward) variant for multi-step reasoning/GUI/coding. github: `https://github.com/Gen-Verse/Open-AgentRL`, paper: `https://arxiv.org/abs/2602.02488`, Gen-Verse, date: 2026.2.

> **OpenClaw-RL** — GRPO + OPD for terminal/GUI/SWE/tool-call. github: `https://github.com/Gen-Verse/OpenClaw-RL`, paper: `https://arxiv.org/abs/2603.10165`, Gen-Verse, date: 2026.3.

> **Trinity-RFT** — Alibaba's PPO/GRPO framework spanning math/text-game/web. github: `https://github.com/modelscope/Trinity-RFT`, paper: `https://arxiv.org/abs/2505.17826`, Alibaba, date: 2025.5.

> **AgentRL** — comparison of GRPO/REINFORCE++/RLOO/ReMax/GAE on agent tasks. github: `https://github.com/THUDM/AgentRL`, paper: `https://arxiv.org/abs/2510.04206`, Tsinghua, date: 2025.10.

> **AgentGym-RL** — runs PPO/GRPO/RLOO/REINFORCE++ across 5 task families (web/search/game/embodied/science). github: `https://github.com/WooooDyy/AgentGym-RL`, paper: `https://arxiv.org/abs/2509.08755`, Fudan University, date: 2025.9.

> **Agent0** — ADPO (advantage-decoupled policy optimization) variant. github: `https://github.com/aiming-lab/Agent0`, paper: `https://arxiv.org/abs/2511.16043`, UNC‑Chapel Hill / Salesforce Research / Stanford University, date: 2025.11.

> **AgentFlow** — Flow-GRPO for search/math/QA workflows. github: `https://github.com/lupantech/AgentFlow`, paper: `https://arxiv.org/abs/2510.05592`, Stanford University, date: 2025.10.

> **Tree-GRPO** — tree-structured GRPO over multi-step search trajectories. github: `https://github.com/AMAP-ML/Tree-GRPO`, paper: `https://arxiv.org/abs/2509.21240`, AMAP, date: 2025.9.

> **DEPO** — KTO + Efficiency Loss; useful when token-efficiency matters more than raw success. github: `https://github.com/OpenCausaLab/DEPO`, paper: `https://arxiv.org/abs/2511.15392`, HKUST/SJTU, date: 2025.11.

> **DeepAgent** — ToolPO algorithm on ToolBench/ALFWorld/WebShop/GAIA. github: `https://github.com/RUC-NLPIR/DeepAgent`, paper: `https://arxiv.org/abs/2510.21618`, RUC/Xiaohongshu, date: 2025.10.

> **AgentEvolver** — ADCA-GRPO with self-evolving curriculum. github: `https://github.com/modelscope/AgentEvolver`, paper: `https://arxiv.org/abs/2511.10395`, Alibaba/Tongyi Lab, date: 2025.11.

> **youtu-agent** — Training-Free GRPO baseline (no gradient updates) — sanity check before launching real training. github: `https://github.com/TencentCloudADP/youtu-agent`, paper: `https://arxiv.org/abs/2512.24615`, Tencent Youtu Lab, date: 2025.12.

> **MATPO** — multi-agent variant of GRPO for tool-use. github: `https://github.com/mzf666/MATPO`, paper: `https://arxiv.org/abs/2510.04678`, MiroMind AI, date: 2025.10.

> **ReCall** — side-by-side PPO/GRPO/RLOO/REINFORCE++/ReMax on tool-use/math/QA. github: `https://github.com/Agent-RL/ReCall`, paper: `https://arxiv.org/abs/2503.19470`, BaiChuan, date: 2025.3.

> **agent-lightning** — automatic prompt optimization combined with PPO. github: `https://github.com/microsoft/agent-lightning`, paper: `https://arxiv.org/abs/2508.03680`, Microsoft Research, date: 2025.8.

## See also

- `grpo-knobs.md` — once you've picked GRPO.
- `ppo-knobs.md` — once you've picked PPO.
- `kl-penalty-tuning.md` — β across algorithms.
- `token-vs-sequence-loss.md` — DAPO/Dr.GRPO/GSPO toggles.
- `credit-assignment-long-horizon.md` — when to switch to GiGPO/IGPO.
- `../research-workflow/online-vs-offline-rl.md` — DPO vs online tradeoff.
