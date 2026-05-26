# Problem: RL from base model (no SFT) — DeepSeek-R1-Zero style

## When you'd want this

- You're trying to reproduce R1-Zero / Absolute-Zero-Reasoner style
  results: skip SFT entirely, RL from base.
- You don't have SFT data and don't want to distill.
- You're studying whether the model can find the format on its own.
- You're doing research on emergent behavior, not maximizing benchmark.

## Why this is hard

A base model (Llama-3 base, Qwen-2.5 base, no instruct) has never seen:

- A chat template.
- An agentic format like `<think><answer>` or `<tool_call>`.
- A multi-turn conversation structure.
- Reward-following behavior at all.

So:

- The first 1000 RL steps, reward is 0 (model doesn't even produce the
  format).
- KL stays low or drifts in random directions.
- Entropy is high — every rollout is different junk.
- Even when reward starts moving, the format is brittle.

## Common failure modes

1. **Reward never moves.** Format-gated reward + base model = stuck.
2. **Format emerges then collapses.** Model finds the format briefly,
   then drifts away when reward variance is too low.
3. **Tokenizer collision.** Base model uses different chat template
   than your reward-parser expects.
4. **Garbage outputs.** Base model emits non-natural sequences (long
   `\n\n\n`, code-like patterns, repetitions). Reward 0 across the
   board.
5. **High variance, no signal.** Without SFT, every prompt's rollouts
   are bimodal: a few succeed wildly, most fail completely. Group
   advantage is dominated by variance.

## What actually works

### Pattern 1: rule-based reward only (R1-Zero pattern)

Pure rule-based outcome reward. **No format reward.** No PRM. No
LLM-judge.

```
reward = 1.0 if extract_answer(response) == gold_answer else 0.0
```

The bet: the model finds *some* way to express the answer, the rule
accepts a permissive extraction, and over thousands of steps the
format emerges. R1-Zero does this for math: the regex accepts boxed
answers, plain digits, common formatting.

Critical: the extraction rule must be **lenient on format, strict on
content**. Examples that should all extract correctly:

```
"the answer is 42"
"\\boxed{42}"
"42"
"42 is the answer"
"<answer>42</answer>"
```

If your extractor only accepts one of these, the model will fail to
find the format.

### Pattern 2: 100-500 example "format SFT" cold-start

Not full SFT — just enough to teach the format. Instead of distilling
1000s of long-CoT trajectories, distill 100-500 that demonstrate:

- The chat template format.
- The expected answer wrapping (e.g. `<answer>...</answer>`).
- Tool-call format if applicable.

This is much cheaper than full SFT and unblocks RL signal. Almost
every paper in the corpus that "trains from base" actually does some
flavor of this.

### Pattern 3: Instruct model instead of base

By far the most common shortcut. Replace `Llama-3-8B-base` with
`Llama-3-8B-Instruct`. Reward starts moving in 50 steps instead of
5000. **Most papers that claim "RL on Llama" actually mean Instruct.**

If your contribution doesn't *require* base, use Instruct. Save the
weeks.

### Pattern 4: self-bootstrap (Absolute-Zero, R-Zero)

Use the base model itself to generate training data:

- Sample many rollouts; filter to high-reward ones.
- SFT on filtered self-rollouts.
- Then RL.

Or: use a **challenger** model to generate problems, **solver** model
to solve them, with a curriculum of difficulty:

> **Absolute-Zero-Reasoner** — github:
> `https://github.com/LeapLabTHU/Absolute-Zero-Reasoner`,
> paper: `https://arxiv.org/abs/2505.03335`, Tsinghua, date: 2025.5.
> Why: TRR++ uses learnability weighting on self-generated problems
> for code/math reasoning — no external SFT data required.

> **R-Zero** — github: `https://github.com/Chengsong-Huang/R-Zero`,
> paper: `https://arxiv.org/abs/2508.05004`, Tencent AI Seattle,
> date: 2025.8. Why: challenger-solver self-evolution with GRPO; the
> challenger generates problems just-hard-enough for the solver.

### Pattern 5: stronger KL anchor, conservative LR

If you must train from base:

```yaml
algorithm:
  kl_loss_coef: 1e-2          # 10x default
  loss_agg_mode: token-mean
  entropy_coef: 1e-3          # keep some exploration
  norm_adv_by_std_in_grpo: false   # Dr.GRPO
optim:
  lr: 1e-7                    # very low
  warmup_ratio: 0.1           # long warmup
  lr_scheduler: cosine
data:
  group_n: 16                 # high N for variance
filter_groups:
  enable: true
  threshold: 1e-4             # drop zero-variance groups
```

### Pattern 6: lenient parser + explicit feedback

If outcome reward is binary, format-gating fails. Use a lenient
parser that accepts many formats and gives feedback:

```python
def parse(response):
    candidates = []
    candidates.extend(re.findall(r"\\boxed\{([^}]+)\}", response))
    candidates.extend(re.findall(r"<answer>([^<]+)</answer>", response))
    candidates.extend(re.findall(r"the answer is ([^\n]+)", response))
    candidates.extend(extract_last_number(response))
    return candidates  # try all
```

Reward = max over candidates. Lets the model find any of several
format paths.

## Diagnosis: is RL from base actually working?

After 500 steps:

- Format-correctness rate ≥ 30%? Good — RL is finding the format.
- Format ≥ 90% but reward < 5%? Format learned, content not.
- Format < 5% and reward < 5%? RL stuck. Diagnose:
  - Sample 20 rollouts. Are they natural language? Or junk?
  - If junk: KL anchor too weak; model drifted to gibberish.
  - If natural but wrong format: extractor too strict, or
    format-gate-only reward.

After 2000 steps with no movement: stop. Add format SFT cold-start
(100-500 examples) and restart.

## Recipe: "RL from base" minimum viable setup

```yaml
model:
  base: Qwen/Qwen2.5-7B          # base, not Instruct
  reference: same
training:
  algorithm: grpo                 # not PPO; no critic
  kl_loss_coef: 1e-2              # high anchor
  group_n: 16                     # high N
  filter_groups: true             # drop zero-var
  loss_agg_mode: token-mean
  norm_adv_by_std: false          # Dr.GRPO
  lr: 1e-7
  warmup_steps: 200
  total_steps: 5000
reward:
  outcome: lenient_extract        # accept many formats
  format: 0.0                     # no format reward
  punish_parse_failure: false     # silent 0
data:
  task: math                      # rule-based reward only
  difficulty_filter: success_rate ∈ [0.05, 0.5]   # learnable zone
```

Math/code/exact-match QA are the only tasks where this is realistic.

## When to give up

- 5000 steps with reward < 5% and format-correctness flat → you need
  cold-start SFT. Distill 100-500 trajectories from a stronger model
  in your target format. Then resume.
- Eval shows the model can't follow simple instructions any more →
  forgetting (see `catastrophic-forgetting.md`). This sometimes
  happens when KL is too weak in RL-from-base.
- Format collapses after early progress → entropy-collapse pattern.
  Filter low-variance groups (`FilterGroupsConfig` in veRL) and add an
  entropy bonus.

## Why most papers don't do this

The corpus tells the truth: almost every successful agentic-RL paper
uses **multi-stage SFT then RL**. R1-Zero is the exception, not the
rule, and even R1-Zero only works on math/code where verification is
mechanical.

For agentic tasks (search, tool-use, GUI):

- Base model has no idea what `<tool_call>` means.
- Reward doesn't fire until the format is correct.
- Without SFT, you're betting on emergent format discovery — usually
  doesn't happen at typical agent budgets.

## Paper / repo references

> **Absolute-Zero-Reasoner** — github:
> `https://github.com/LeapLabTHU/Absolute-Zero-Reasoner`,
> paper: `https://arxiv.org/abs/2505.03335`, Tsinghua, date: 2025.5.
> Why: TRR++ pattern with self-bootstrap + learnability-weighted
> curriculum; no external SFT.

> **R-Zero** — github: `https://github.com/Chengsong-Huang/R-Zero`,
> paper: `https://arxiv.org/abs/2508.05004`, Tencent AI Seattle,
> date: 2025.8. Why: challenger-solver self-evolution; produces
> RL-from-base trajectories without distillation.

> **RAGEN** — github: `https://github.com/RAGEN-AI/RAGEN`,
> paper: `https://arxiv.org/abs/2504.20073`, RAGEN-AI, date: 2025.4.
> Why: StarPO documents the "template collapse" failure mode that
> base→RL hits hardest; reward-variance-based prompt filtering is the
> recommended counter.

> **Skywork-OR1** — github: `https://github.com/SkyworkAI/Skywork-OR1`,
> paper: `https://arxiv.org/abs/2505.22312`, Skywork, date: 2025.5.
> Why: scale + rule-based reward; one of the few demonstrations of
> RL-from-base-ish working at scale.

> **veRL** — github: `https://github.com/volcengine/verl`,
> paper: `https://arxiv.org/abs/2409.19256`, ByteDance Seed, date: 2024.9.
> Why: `KLControlConfig` and `FilterGroupsConfig` are
> the knobs you need; the framework supports the high-anchor / high-N
> setup directly.

**Other corpus entries:**

- `agent-distillation` — PPO with distillation-based external reward.
  github: `https://github.com/Nardien/agent-distillation`, paper: `https://arxiv.org/abs/2505.17612`, KAIST, date: 2025.5

- `AutoCoA` — GRPO for reasoning/math/QA — chain-of-action distillation.
  github: `https://github.com/ADaM-BJTU/AutoCoA`, paper: `https://arxiv.org/abs/2503.06580`, BJTU, date: 2025.3

- `ReMA` — PPO with rule reward for math.
  github: `https://github.com/ziyuwan/ReMA-public`, paper: `https://arxiv.org/abs/2503.09501`, SJTU, UCL, date: 2025.3

- `SimpleTIR` — PPO/GRPO with extensions for math/coding tool-integrated reasoning.
  github: `https://github.com/ltzheng/SimpleTIR`, NTU, Bytedance, date: 2025.2

- `AutoTIR` — PPO with rule reward for autonomous tool selection.
  github: `https://github.com/weiyifan1023/AutoTIR`, paper: `https://arxiv.org/abs/2507.21836`, Beihang University / BAAI, date: 2025.7

- `Tool-Light` — self-evolved DPO for tool-integrated reasoning.
  github: `https://github.com/RUC-NLPIR/Tool-Light`, paper: `https://arxiv.org/abs/2509.23285`, RUC (RUC-NLPIR), date: 2025.9

- `MOTIF` — GRPO with rule reward for QA.
  github: `https://github.com/purbeshmitra/MOTIF`, paper: `https://arxiv.org/abs/2507.02851`, University of Maryland, date: 2025.7

- `terminal-bench-rl` — GRPO with verifier reward for coding/terminal tasks.
  github: `https://github.com/Danau5tin/terminal-bench-rl`, Individual (Danau5tin), date: 2025.7

- `Agentic-Reasoning` — custom-RL with external reward for QA/math.
  github: `https://github.com/theworldofagents/Agentic-Reasoning`, paper: `https://arxiv.org/abs/2502.04644`, Oxford, date: 2025.2

- `cmriat/l0` — PPO for QA.
  github: `https://github.com/cmriat/l0`, paper: `https://arxiv.org/abs/2506.23667`, CMRIAT, date: 2025.6

## See also

- `sft-to-rl-transition.md` — for the "with SFT" path (default).
- `sparse-reward-credit.md` — what to do when reward never moves.
- `zero-variance-rollouts.md` — bimodal-reward symptom of RL-from-base.
- `entropy-collapse.md` — template collapse during RL-from-base.
- `catastrophic-forgetting.md` — late-RL forgetting risk.
