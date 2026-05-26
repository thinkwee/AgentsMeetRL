# Question: online RL vs offline RL vs DPO — which one for my project

## Decision tree

```
Have only static preference pairs (chosen, rejected),
no env, no rollouts? .................................... DPO / IPO / SimPO

Have rollouts from an existing policy + outcome
labels (success/failure) on each? ........................ RFT / KTO / ORPO

Need to *explore* — i.e., the policy must discover
behaviors not in the existing data? ...................... Online RL (PPO/GRPO)

Want corpus best practice for non-trivial agents? ........ SFT → RFT/DPO → Online RL
                                                            (3-stage pipeline)
```

## What each method does

### DPO / IPO / SimPO (static preference)

Given a dataset of `(prompt, chosen, rejected)` triples:

```
L_DPO = -log σ( β [ log(π(chosen)/π_ref(chosen))
                   - log(π(rejected)/π_ref(rejected)) ] )
```

Maximize the log-prob ratio of chosen over rejected. Variants:

- **DPO**: as above. β controls how aggressive.
- **IPO**: replaces sigmoid with squared-error; less likely to push
  log-probs to ±∞ on noisy preferences.
- **SimPO**: drops the reference model; uses length-normalized
  log-prob. Cheaper, sometimes worse on capability preservation.
- **KTO** (Kahneman-Tversky Optimization): treats binary labels (good /
  bad) without requiring pairs. Good when you have ratings, not
  comparisons.
- **ORPO** (Odds-Ratio Preference Optimization): combines SFT loss
  with preference loss in a single pass; one-stage training.

### RFT (Rejection-sampling Fine-Tuning)

```
1. Run weak policy on prompts; collect rollouts.
2. Filter to outcome=success.
3. SFT on filtered set.
```

Pure imitation of the policy's own best behavior. Cheap. Doesn't
explore; converges to "best of what we've already seen."

### Online RL (PPO / GRPO / ...)

```
1. Sample rollouts from current policy.
2. Compute reward.
3. Update policy.
4. Repeat.
```

Full exploration; expensive; staleness issues; KL drift risks.

## Cost / capability tradeoff

| Method | Compute | Exploration | Best-case quality |
|---|---|---|---|
| DPO | 1× SFT | None | ~70% of online |
| IPO | 1× SFT | None | ~70% of online |
| KTO | 1× SFT | None | ~70% of online |
| ORPO | 1× SFT | None | ~75% (one-stage) |
| RFT | 2× SFT | Limited (only filtered) | ~80% of online |
| Online | 5-20× SFT | Full | 100% (definition) |

The "70% of online" is empirical; varies by task. For some tasks
(safety alignment, format following) DPO is *competitive* with online.
For exploration-heavy agentic tasks (long-horizon search, multi-tool
reasoning), DPO leaves substantial gains on the table.

## Decision rationale

### "I have only static preferences"

Use DPO. If your preferences came from:

- A stronger teacher's pairwise judgments → DPO works well.
- Self-distilled (current model judging itself) → DPO may overfit;
  prefer IPO.
- Human labels → DPO is the standard.

Avoid online RL unless you can produce live rewards. RL on stale
preferences without env feedback is just slow DPO.

### "I have rollouts and outcomes"

You can:

- **DPO** if your "preferences" are constructed by pairing
  high-outcome with low-outcome rollouts.
- **RFT** if you just want to imitate the best.
- **KTO** if you have binary good/bad labels per single rollout
  (no pairing).

RFT is cheapest. DPO is cheapest with comparable signal. KTO is best
when pair construction is awkward.

### "I need to explore"

Online RL. Period. DPO and RFT don't explore. If you trained DPO and
saw plateauing, online RL is what unlocks the next 20-30%.

But: don't skip the SFT-then-DPO cold start. Every successful
agentic-RL paper does it.

## The "3-stage pipeline" (corpus consensus)

```
Stage 1: SFT on demonstrations
  - 1k-10k high-quality trajectories.
  - Use distilled-from-teacher data or expert traces.
  - Get the model into the right format and recipe.

Stage 2: Offline preference / rejection-sampling FT
  - Choose one: DPO, IPO, KTO, RFT.
  - Cheap, stable.
  - Captures most of the gain that's reachable from existing data.

Stage 3: Online RL (GRPO or PPO)
  - The expensive step.
  - Discovers behaviors not in the static data.
  - Needs careful KL anchoring (β ~ 1e-3).
```

Skipping Stage 2 is wasteful: online RL converges much slower from a
weak SFT model than from a DPO-warmed model.

Skipping Stage 3 caps your headline number well below what's achievable.

## Examples from the corpus

| Pipeline | Project |
|---|---|
| SFT → DPO/PPO/ORPO/SimPO/KTO mix → online RL | Tool-Star (`https://github.com/dongguanting/Tool-Star`) |
| SFT → Offline RL → Online RL | MobileRL (`https://github.com/THUDM/MobileRL`) |
| SFT → Offline RL → Online RL (OSWorld) | Mano-P (`https://github.com/Mininglamp-AI/Mano-P`) |
| SFT + Online RL (PPO/GRPO) | Search-R1 |
| SFT + DPO + MCTS-PRM | ReasonRAG (`https://github.com/wlzhang2020/ReasonRAG`) |
| SFT/DPO/PPO/GRPO on medical code | MedAgentGym (`https://github.com/wshi83/MedAgentGym`) |
| Self-evolved (no SFT) → online RL | Absolute-Zero-Reasoner, R-Zero |
| Online RL only (DeepSeek-R1-Zero pattern) | Skywork-OR1, parts of RAGEN |

The "online RL only" cases are math/code with rule-based reward —
the only setting where the format-finding-without-SFT pattern works.

## When DPO/RFT are good enough

- **Format alignment** (teaching the model to use a specific output
  shape).
- **Safety / refusal** behavior.
- **Style transfer** (formal vs casual; a specific persona).
- **Distillation from a stronger model.**

In these, DPO often hits within 1-2 points of online RL with 1/10 the
compute. Take the win.

## When DPO/RFT are NOT good enough

- **Multi-turn agent reasoning.** DPO can't simulate the env.
- **Long-horizon planning.** RFT only imitates the best path the weak
  policy found; doesn't discover better paths.
- **Tool-use composition.** Compositional behaviors emerge in online
  RL; DPO misses them.
- **Verifiable tasks where you have a rule-based reward.** Online RL
  is cheap to set up and dominates.

## Common pitfalls

### "We compared DPO vs PPO at fixed compute"

Usually unfair: PPO needed cold-start, DPO didn't. Match the *recipe*
not just the algo.

### "DPO on noisy preferences"

DPO pushes log-prob to extremes when preferences are noisy. Use IPO
or apply label smoothing. KTO is more robust on noisy single-point
ratings.

### "DPO collapses to overconfidence"

Symptom: log-prob of chosen → 1, of rejected → 0; eval gets *worse*.
Fix: lower β; use IPO; add SFT regularization (ORPO is one-stage).

### "RFT plateaus quickly"

By definition. RFT can't surpass the policy that generated the
training rollouts. Combine with online RL afterward.

### "Online RL after DPO destabilizes"

DPO model has very confident log-probs. KL anchor must reference the
DPO model, not the original SFT model. Set
`reference_model = dpo_checkpoint`.

## Practical numbers (corpus)

- DPO 7B on 1M preference pairs: 1-2 days on 8x H100.
- KTO same scale: similar.
- RFT: 1 day to generate rollouts + 1 day SFT.
- Online RL 7B: 3-7 days on 8x H100 for ~1000 steps.
- 3-stage pipeline end-to-end: 1-2 weeks.

## Paper / repo references

> **Tool-Star** — github: `https://github.com/dongguanting/Tool-Star`,
> paper: `https://arxiv.org/abs/2505.16410`, RUC, date: 2025.5.
> Why: multi-stage SFT then PPO/DPO/ORPO/SimPO/KTO mix; the canonical
> reference for "all the offline algorithms before online RL."

> **MobileRL** — github: `https://github.com/THUDM/MobileRL`,
> paper: `https://arxiv.org/abs/2509.18119`, THUDM, date: 2025.9.
> Why: clean SFT → Offline RL → Online RL pipeline for mobile GUI;
> reference for the 3-stage pattern.

> **Mano-P** — github: `https://github.com/Mininglamp-AI/Mano-P`,
> paper: `https://arxiv.org/abs/2509.17336`, Mininglamp AI,
> date: 2025.9. Why: same 3-stage pipeline applied to OSWorld.

> **ReasonRAG** — github: `https://github.com/wlzhang2020/ReasonRAG`,
> paper: `https://arxiv.org/abs/2505.14069`, CityU HK / Huawei,
> date: 2025.5. Why: DPO + MCTS-based PRM for multi-hop QA; an example
> of mixing DPO and PRM-guided online steps.

> **MedAgentGym** — github: `https://github.com/wshi83/MedAgentGym`,
> paper: `https://arxiv.org/abs/2506.04405`, Emory, date: 2025.6.
> Why: SFT/DPO/PPO/GRPO on medical code; useful for direct comparison
> of these algorithms on the same task.

## See also

- `../training/algorithm-choice.md` — once you've picked online,
  which online RL algorithm.
- `../training/sft-to-rl-transition.md` — Stage 1 → Stage 3 transition.
- `../training/sparse-reward-credit.md` — when online needs Stage 2 to
  bootstrap.
- `data-curation.md` — preferences and trajectories
  are data; curation matters.
