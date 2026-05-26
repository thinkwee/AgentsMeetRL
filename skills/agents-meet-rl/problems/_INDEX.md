# Problems Index — Agentic RL Researcher's Troubleshooter

This is **the** entry point. Every file here answers a specific symptom or
question a researcher hits while training, evaluating, or iterating on an
agentic-RL project. Each file follows the same shape:

> **Symptoms → Root causes → Diagnosis → Fixes → Paper / repo references**

If you came here to *pick a framework / algorithm / environment* (technical
selection), the routing tables in this index will still take you to the
problem file that matches your symptom — which is what most "selection"
questions actually reduce to.

## Starting from scratch (no symptom yet)

If you don't have a symptom yet — you're spinning up a new agentic-RL
project — pick four things in order, then come back here on the first
symptom:

1. **Base framework** → `../references/base-frameworks.md` (veRL,
   OpenRLHF, slime, AReaL, NeMo-RL, …). Pick by training scale,
   sync vs async, multi-modality support.
2. **Algorithm** → [training/algorithm-choice.md](training/algorithm-choice.md).
   Corpus default is GRPO for math/code/search; switch by task shape.
3. **Environment / benchmark** → `../references/environments.md`. Pick
   a benchmark in the family you ultimately want to be evaluated on;
   train on its **training split**, not its eval split.
4. **Reward design** → start with **rule-based outcome reward** (EM /
   F1 / test-pass) + tiny format reward (≤ 5% of total). Tune later
   per [training/reward-mixing.md](training/reward-mixing.md).

Forkable starter recipes (each cited in `../references/<cat>.md`):

| Task | Fork from |
|---|---|
| Search agent (single/multi-hop QA) | Search-R1 |
| Tool-integrated reasoning (math + code interpreter) | ReTool, Tool-Star |
| SWE / repo edits | SWE-Gym, SWE-Swiss |
| GUI / web | UI-TARS, AgentNet |
| Long-horizon multi-turn agent | verl-agent (GiGPO) |
| Reasoning-mode RL from R1-distill base | Skywork-OR1 |

## Training-time problems (`training/`)

### Loss / reward dynamics

| Symptom | File |
|---|---|
| Reward never moves off zero / training plateaus immediately | [training/reward-not-increasing.md](training/reward-not-increasing.md) |
| Train reward grows but eval is flat or drops | [training/reward-up-eval-flat.md](training/reward-up-eval-flat.md) |
| Reward climbs, then collapses (training crash) | [training/training-collapse.md](training/training-collapse.md) |
| Output entropy / diversity drops; outputs all look the same | [training/entropy-collapse.md](training/entropy-collapse.md) |
| KL divergence to ref model explodes | [training/kl-explosion.md](training/kl-explosion.md) |
| NaN / inf in loss or grads | [training/nan-grads.md](training/nan-grads.md) |
| Importance ratios become huge (PPO ratio > 5+) | [training/importance-ratio-blowup.md](training/importance-ratio-blowup.md) |
| Curves are noisy / unstable run-to-run | [training/unstable-curves.md](training/unstable-curves.md) |
| Eval on training task ↑ but general capabilities (math/code) ↓ | [training/catastrophic-forgetting.md](training/catastrophic-forgetting.md) |

### Output shape

| Symptom | File |
|---|---|
| Outputs grow longer every step, hit context limit | [training/length-blowup.md](training/length-blowup.md) |
| Outputs collapse to very short answers | [training/length-collapse.md](training/length-collapse.md) |
| Format/thinking tags get gamed (empty `<answer>`, junk thinking) | [training/format-reward-gaming.md](training/format-reward-gaming.md) |
| Model never emits EOS / never stops | [training/no-eos.md](training/no-eos.md) |
| Reasoning-mode (DeepSeek-R1 / Qwen3 thinking / GLM-Z1) RL specifics | [training/reasoning-mode-rl.md](training/reasoning-mode-rl.md) |

### Rollout layer

| Symptom | File |
|---|---|
| Tool-call parse failure rate is high | [training/tool-call-parse-failures.md](training/tool-call-parse-failures.md) |
| All N rollouts in a group share the same reward (zero variance) | [training/zero-variance-rollouts.md](training/zero-variance-rollouts.md) |
| Observations get truncated mid-trajectory and credit is wrong | [training/observation-truncation.md](training/observation-truncation.md) |
| Logits don't match sampled tokens — retokenization drift | [training/retokenization-drift.md](training/retokenization-drift.md) |
| Env API rate-limits / times out / returns garbage during training | [training/env-flakiness.md](training/env-flakiness.md) |
| Async rollout off-policy bias | [training/async-rollout-staleness.md](training/async-rollout-staleness.md) |
| Tool / env layer architecture — design principles | [training/tool-api-design.md](training/tool-api-design.md) |

### Reward design

| Symptom | File |
|---|---|
| Outcome reward is too sparse — most rollouts get 0 | [training/sparse-reward-credit.md](training/sparse-reward-credit.md) |
| Need a process reward / PRM, not sure how to train one | [training/prm-training.md](training/prm-training.md) |
| LLM-as-judge is inconsistent / biased / drifts during training | [training/llm-judge-pitfalls.md](training/llm-judge-pitfalls.md) |
| Mixing multiple reward terms — weights, normalization, curriculum | [training/reward-mixing.md](training/reward-mixing.md) |
| Search agent learns query-hacking, not task-solving | [training/search-hacking.md](training/search-hacking.md) |

### Credit assignment

| Symptom | File |
|---|---|
| 50+ step episodes, single outcome reward — turns get equal credit | [training/credit-assignment-long-horizon.md](training/credit-assignment-long-horizon.md) |
| Multi-agent: one role gets all the credit, others don't learn | [training/multi-agent-credit-collapse.md](training/multi-agent-credit-collapse.md) |
| Self-play: strategy collapses / cycles | [training/self-play-collapse.md](training/self-play-collapse.md) |

### SFT → RL transition

| Symptom | File |
|---|---|
| RL diverges immediately after SFT cold start | [training/sft-to-rl-transition.md](training/sft-to-rl-transition.md) |
| RL from base model (no SFT) — DeepSeek-R1-Zero pattern | [training/rl-from-base.md](training/rl-from-base.md) |

### Algorithm choice (before tuning)

| Question | File |
|---|---|
| PPO vs GRPO vs DPO vs REINFORCE++ vs RLOO — which to pick | [training/algorithm-choice.md](training/algorithm-choice.md) |

### Algorithm knobs (when you've already picked one)

| Symptom / Question | File |
|---|---|
| GRPO group size, normalization, advantage baseline tuning | [training/grpo-knobs.md](training/grpo-knobs.md) |
| PPO clip ε, GAE λ, value-loss coefficient tuning | [training/ppo-knobs.md](training/ppo-knobs.md) |
| KL penalty vs KL constraint, β scheduling | [training/kl-penalty-tuning.md](training/kl-penalty-tuning.md) |
| Token-level vs sequence-level loss — which and why | [training/token-vs-sequence-loss.md](training/token-vs-sequence-loss.md) |
| Discount factor γ for multi-turn — why ≠ 1 hurts you | [training/discount-factor.md](training/discount-factor.md) |

### Memory & long context

| Symptom | File |
|---|---|
| History exceeds context window after N turns | [training/memory-context-overflow.md](training/memory-context-overflow.md) |
| Multi-turn dialogue history pruning / summarization | [training/conversation-history-truncation.md](training/conversation-history-truncation.md) |

### Infrastructure

| Symptom | File |
|---|---|
| Rollout phase keeps GPUs idle | [training/rollout-throughput.md](training/rollout-throughput.md) |
| OOM during training / actor-rollout memory peaks | [training/oom-during-training.md](training/oom-during-training.md) |
| LoRA RL — when it works and what it loses | [training/lora-rl.md](training/lora-rl.md) |
| bf16 / fp16 / fp32 / fp8 — what to use where | [training/mixed-precision.md](training/mixed-precision.md) |
| NCCL hangs, partial-rank failures, allreduce slowness | [training/distributed-failures.md](training/distributed-failures.md) |
| Sandbox security — isolating untrusted code execution | [training/sandbox-security.md](training/sandbox-security.md) |

### Modality-specific

| Symptom | File |
|---|---|
| VLM agent — image obs, grounding, multi-image multi-turn | [training/vlm-specific.md](training/vlm-specific.md) |
| Code/SWE — sandbox flakiness, test-pass reward gaming | [training/code-swe-specific.md](training/code-swe-specific.md) |
| GUI — screenshot diff cost, action grounding | [training/gui-specific.md](training/gui-specific.md) |

## Evaluation-time problems (`evaluation/`)

| Symptom / Question | File |
|---|---|
| Which benchmark — and what's wrong with each? | [evaluation/benchmark-pitfalls.md](evaluation/benchmark-pitfalls.md) |
| Suspect data contamination | [evaluation/data-contamination.md](evaluation/data-contamination.md) |
| pass@1 vs pass@k vs majority@k — what to report | [evaluation/pass-at-k.md](evaluation/pass-at-k.md) |
| My number is high but variance huge — sample-size question | [evaluation/statistical-significance.md](evaluation/statistical-significance.md) |
| My eval differs from training because of sampling params | [evaluation/train-eval-mismatch.md](evaluation/train-eval-mismatch.md) |
| Should I do best-of-N / tree search / self-consistency? | [evaluation/inference-time-scaling.md](evaluation/inference-time-scaling.md) |
| LLM-judge gives different scores each run | [evaluation/llm-judge-evaluation.md](evaluation/llm-judge-evaluation.md) |
| Can't reproduce my own / others' numbers | [evaluation/reproducibility.md](evaluation/reproducibility.md) |
| OOD / distribution-shift evaluation design | [evaluation/ood-evaluation.md](evaluation/ood-evaluation.md) |
| Long-horizon: episodes too costly, partial credit, failure-mode breakdown | [evaluation/long-horizon-eval.md](evaluation/long-horizon-eval.md) |
| Multi-agent evaluation protocol | [evaluation/multi-agent-eval.md](evaluation/multi-agent-eval.md) |
| Canary eval — catch training problems early (small fixed eval set) | [evaluation/canary-eval.md](evaluation/canary-eval.md) |

## Research-workflow problems (`research-workflow/`)

| Question | File |
|---|---|
| What ablations to run; how to isolate the contribution | [research-workflow/ablation-design.md](research-workflow/ablation-design.md) |
| What baseline to compare against (and how to make it strong) | [research-workflow/baseline-selection.md](research-workflow/baseline-selection.md) |
| Reproducing a paper from this corpus — common failure modes | [research-workflow/reproducing-papers.md](research-workflow/reproducing-papers.md) |
| Compute budget: rollout vs train vs eval split | [research-workflow/compute-budget.md](research-workflow/compute-budget.md) |
| Generating / curating training data | [research-workflow/data-curation.md](research-workflow/data-curation.md) |
| When to publish / when the bar is "novel algorithm" vs "engineering" | [research-workflow/contribution-framing.md](research-workflow/contribution-framing.md) |
| Online RL vs offline RL vs DPO — pipeline choice | [research-workflow/online-vs-offline-rl.md](research-workflow/online-vs-offline-rl.md) |
| Hyperparameter search strategy (which knobs to tune, in what order) | [research-workflow/hyperparam-search.md](research-workflow/hyperparam-search.md) |
| Applying agentic-RL to a vertical domain (medical, finance, OS, biology, …) | [research-workflow/domain-application.md](research-workflow/domain-application.md) |

## How problem files are structured

Most files in `training/` and `evaluation/` follow this five-section
template:

```
# Problem: <symptom in plain English>

## Symptoms          What you see in logs / metrics / outputs.
## Root causes       The 2–4 things that actually cause this. Most-likely first.
## Diagnosis         Concrete checks that narrow root cause to one.
## Fixes             Per root cause: what to change. Each fix names the
                     algorithm/idea and the repo/paper it comes from.
## Paper / repo references
                     <Algorithm or idea> — github URL · arXiv URL · org · YYYY.MM.
```

Some files use a task-appropriate structure instead:

- All `research-workflow/` files follow a step-by-step decision flow
  rather than the five-section template.
- **Knob / tuning files** iterate over parameters and don't have a
  single symptom: `grpo-knobs`, `ppo-knobs`, `kl-penalty-tuning`,
  `discount-factor`, `token-vs-sequence-loss`, `reward-mixing`,
  `lora-rl`.
- **Survey / decision files** iterate over options or levels:
  `algorithm-choice`, `benchmark-pitfalls`, `sandbox-security`,
  `mixed-precision`, `prm-training`, `rl-from-base`, `tool-api-design`.
- **Modality-specific files** are mini-handbooks for a setting rather
  than one symptom: `code-swe-specific`, `gui-specific`, `vlm-specific`.
- **Eval-side reference files** are checklists / catalogues:
  `canary-eval`, `inference-time-scaling`, `llm-judge-evaluation`,
  `long-horizon-eval`, `multi-agent-eval`, `ood-evaluation`,
  `pass-at-k`, `reproducibility`, `statistical-significance`.

Same citation rule applies to all: name the algorithm or idea, anchor
with one paper URL + one repo URL.

## Citation rule

See `SKILL.md` for the three citation templates (project with both
repo and paper, paper-only algorithm, repo-only tool/environment).

**Reference at the idea level, not at the file/line or section level.**
Repos restructure, papers get revised; the algorithm name and its top-
level URL are stable. The corpus has 294 entries in `database.json`
(274 open-source repos + 20 under-review papers) plus 3 paper-only
algorithms whitelisted in `scripts/lint_skill.py`, for 297 citable
items total. Pick the canonical one; don't pin to its current
internals.
