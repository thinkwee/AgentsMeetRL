# Problem: reasoning-mode RL — DeepSeek-R1 / Qwen3 thinking / GLM-Z1 specifics

## Why this is its own topic

Reasoning models (DeepSeek-R1 family, Qwen3 with thinking mode, GLM-Z1,
Nemotron Nano reasoning) have a special token-level structure:

```
<think>
... long internal reasoning ...
</think>
<answer> ... </answer>
```

This shape changes the RL setup. Vanilla GRPO tuned for
non-reasoning models will misbehave; the standard fixes from
`length-blowup.md` and `format-reward-gaming.md` apply but with
reasoning-model-specific twists.

## Symptoms

- Thinking content trivial / repetitive / circular ("Let me think...
  Let me think...").
- Reasoning budget unbounded → length blowup at the thinking phase.
- After RL, model "forgets" how to *not* think (always emits `<think>`
  even on trivial questions).
- Toggle-mode model (Qwen3 with `enable_thinking=True/False`) works
  in one mode but not the other after training.
- Answer-section becomes terse and skips justification because
  reasoning happened in the thinking section.
- Eval scores at greedy (T=0) different from sampling (T=0.6) by 5+
  points because reasoning-trace path is bimodal.

## Root causes

1. **No reasoning budget constraint.** `<think>` section can grow to
   max-context.
2. **Format reward applied to thinking content with no quality gate.**
   Empty / junk thinking gets full credit.
3. **Tokenizer's `<think>` and `</think>` are *single tokens*** (special
   tokens) in some chat templates and *multiple tokens* in others.
   Mismatch → KL spikes, retokenization drift.
4. **Mixed-mode training** (some prompts use thinking, some don't)
   without a clear signal to the model. Model learns to always think.
5. **No reasoning-specific format spec.** Model emits malformed
   thinking (no `</think>`, or mixes thinking content into answer).
6. **Cold-start used base instruction-following data**, not reasoning
   model data. Behavior collides with the reasoning-mode prior.

## Diagnosis

### Decode rollouts with `skip_special_tokens=False`

The `<think>` and `</think>` special tokens are often hidden in
default decoding. Print raw to see what the model actually emits.
Common findings:

- Model uses `<think>` but never closes with `</think>`.
- Model emits `<think>` *inside* `<answer>`.
- Model emits double-thinking: `<think>...</think><think>...</think>`.

### Length partition

Compute `mean_thinking_length`, `mean_answer_length`, `total_length`
separately. Healthy ratio depends on task:

| Task type | Thinking : Answer | Notes |
|---|---|---|
| Math (AIME) | 5:1 to 10:1 | Long reasoning, short numeric answer |
| Code | 2:1 to 4:1 | Reasoning then code |
| Search/QA | 1:2 to 1:1 | Reasoning interleaved with retrieval |
| Tool-call | 1:3 | Reasoning brief, action takes the space |

If thinking dwarfs answer by 50:1 you have unbounded reasoning.

### Format-correctness rate

Per-batch fraction of rollouts with:

- Both `<think>` and `</think>` present in correct order.
- `<answer>` follows `</think>`.
- No nested `<think>` inside `<answer>` or vice versa.

Healthy after warmup: > 95%. < 80% = format reward isn't disciplined.

## Fixes

### Fix 1: cap thinking length (Mini-o3 style)

Hard cap on thinking section:

```python
def shape_thinking_length(response_tokens, max_thinking=1024):
    think_open  = tokenize("<think>")[0]
    think_close = tokenize("</think>")[0]

    open_idx = response_tokens.find(think_open)
    close_idx = response_tokens.find(think_close)

    if open_idx >= 0 and close_idx < 0:
        # never closed — force-close at max_thinking
        if len(response_tokens) - open_idx > max_thinking:
            response_tokens.insert(open_idx + max_thinking, think_close)
```

Or apply a soft penalty to the reward for thinking length above a
target:

```
reward -= max(0, thinking_len - target_thinking_len) * 0.001
```

### Fix 2: gate format reward on **non-empty, non-trivial** thinking

```python
def format_reward(response):
    has_think  = "<think>" in response and "</think>" in response
    has_answer = "<answer>" in response and "</answer>" in response
    think_body = extract_between(response, "<think>", "</think>")

    if not (has_think and has_answer): return 0.0
    if len(think_body) < 20:            return 0.0   # trivial
    if is_repetitive(think_body):       return 0.0   # 4-gram repetition
    return 0.05                                       # cap at 0.05× outcome
```

Rule of thumb: format reward should never exceed 5% of total.

### Fix 3: pin `<think>` / `</think>` as single tokens

Configure the tokenizer to treat reasoning markers as special tokens:

```python
tokenizer.add_special_tokens({
    "additional_special_tokens": ["<think>", "</think>"]
})
```

This prevents BPE from splitting them into multiple sub-tokens, which
is the most common retokenization-drift source for reasoning models.
Verify:

```python
ids = tokenizer.encode("<think>", add_special_tokens=False)
assert len(ids) == 1, f"<think> tokenized into {len(ids)} pieces"
```

### Fix 4: reasoning-mode toggle: dual-format SFT

For models with toggleable thinking (Qwen3, DeepSeek-V3.1):

- Half of SFT data: thinking mode enabled.
- Half: thinking mode disabled (regular instruct).
- Each example has the matching format.

During RL, the prompt's chat template determines mode; reward respects
mode (no format reward in non-thinking mode).

### Fix 5: thinking-mode-specific reward shape

```
reward = outcome_correct                              # main signal
       + 0.05 * format_reward                          # tag well-formed
       - 0.001 * max(0, thinking_len - target_think)   # bound thinking
       - 0.0001 * max(0, total_len - target_total)     # bound total
```

`target_thinking_len` ≈ task-dependent: 1024 for math, 512 for tool-use,
256 for routine QA.

### Fix 6: outcome reward includes only the answer section

Don't include thinking content in outcome reward computation. If the
gold answer is "42", reward should match against:

```python
extracted = extract_between(response, "<answer>", "</answer>")
reward = (extracted.strip() == gold_answer)
```

Not against the full response. Otherwise the model can game outcome
reward by stuffing "42" into the thinking section.

### Fix 7: cold-start with reasoning-style data

If your model is reasoning-capable (DeepSeek-R1-distill, Qwen3-thinking):

- Use distilled long-CoT data for SFT, not generic instruct data.
- Match the format the base model already produces.
- Don't fight the prior — leverage it.

If your base is non-reasoning (Llama-3 base): SFT on R1-distill data
first, then RL. Otherwise the reasoning behavior never appears.

### Fix 8: bounded thinking via generation kwargs

Engine-side bound, complementary to reward-side bound:

```python
# vLLM / SGLang
sampling_params = SamplingParams(
    max_tokens=8192,                  # total
    stop=["</think>"],                # one approach: stop at close-think
    stop_token_ids=[think_close_id],
    ...
)
```

But: a hard stop at `</think>` means the model never gets to the
answer. Better: separate "phase 1: think" and "phase 2: answer"
generations with phase 1 capped at K tokens.

### Fix 9: don't always think

Add a `no_think_required` flag to easy prompts in training data:

```
[easy prompt] → no thinking expected. Reward = outcome only.
[hard prompt] → thinking expected. Reward = outcome + format.
```

Without this signal, the model defaults to "always think" and burns
compute on trivial questions.

## Reasoning-budget control (advanced)

Train the model to *adapt* its thinking length to question difficulty:

- Reward = outcome - α × thinking_tokens.
- Easy questions where outcome = 1 with short thinking: maximum reward.
- Hard questions where long thinking is needed: bigger thinking
  acceptable since outcome dominates.

Open question; few corpus papers do this cleanly. Watch:

> **Mini-o3** — github: `https://github.com/Mini-o3/Mini-o3`,
> paper: `https://arxiv.org/abs/2509.07969`, date: 2025.9.
> Bounded-thinking visual search; explicit thinking-budget reward.

> **VisionThink** — github:
> `https://github.com/dvlab-research/VisionThink`,
> paper: `https://arxiv.org/abs/2507.13348`, CUHK, date: 2025.7.
> Efficient VQA with adaptive thinking length.

## Reasoning-format pitfalls by model family

### DeepSeek-R1 family

- `<think>...</think>` is the canonical format.
- Distill-base models often produce no thinking when given a normal
  chat template. Force the format with a system prompt or SFT.
- Avoid mixing instruct chat template with `<think>` reasoning —
  attention pattern breaks.

### Qwen3 (thinking-mode)

- `enable_thinking=True/False` toggle in the chat template.
- Tokenizer treats `<think>` as a special token only with the right
  template.
- After RL, the toggle can break: model thinks even with
  `enable_thinking=False`. Train both modes (Fix 4).

### GLM-Z1

- Different reasoning markers; check the model card.
- Reasoning section is not always wrapped — sometimes interleaved.
  Reward function must adapt.

### Nemotron Nano reasoning

- Reasoning-budget controllable at inference. Less common in training
  recipes.

## What a healthy reasoning-RL training looks like

```
Step    1: think_len=1200  ans_len=80   format_ok=78%  outcome=0.12
Step  500: think_len=1100  ans_len=85   format_ok=92%  outcome=0.34
Step 1000: think_len= 950  ans_len=80   format_ok=97%  outcome=0.51
Step 2000: think_len= 850  ans_len=75   format_ok=98%  outcome=0.62
Step 3000: think_len= 800  ans_len=72   format_ok=98%  outcome=0.66
```

Note: thinking length **decreases** as the model gets better — it's
solving harder problems with less reasoning. Increasing thinking length
late in training is a red flag.

## Paper / repo references

> **Mini-o3** — github: `https://github.com/Mini-o3/Mini-o3`,
> paper: `https://arxiv.org/abs/2509.07969`, date: 2025.9.
> Why: explicit thinking-budget reward for visual search; the cleanest
> reference for bounded reasoning in agentic settings.

> **VisionThink** — github:
> `https://github.com/dvlab-research/VisionThink`,
> paper: `https://arxiv.org/abs/2507.13348`, CUHK, date: 2025.7.
> Why: efficient VQA pattern; adaptive thinking length for VLM agents.

> **RAGEN** — github: `https://github.com/RAGEN-AI/RAGEN`,
> paper: `https://arxiv.org/abs/2504.20073`, RAGEN-AI, date: 2025.4.
> Why: StarPO framework documents template collapse — the failure mode
> where reasoning becomes input-independent — as the reasoning-mode-
> specific manifestation of collapse.

> **Skywork-OR1** — github: `https://github.com/SkyworkAI/Skywork-OR1`,
> paper: `https://arxiv.org/abs/2505.22312`, Skywork, date: 2025.5.
> Why: large-scale rule-based RL on reasoning models; reference for
> stable thinking-mode training at scale.

> **DeepAnalyze** — github:
> `https://github.com/ruc-datalab/DeepAnalyze`,
> paper: `https://arxiv.org/abs/2510.16872`, RUC/Tsinghua,
> date: 2025.10. Why: curriculum RL on data-science reasoning;
> shows multi-stage pacing for reasoning-mode training.

**Other corpus entries:**

- `VAGEN` — PPO/GRPO with world-modeling RL for navigation/text-game/multimodal.
  github: `https://github.com/mll-lab-nu/VAGEN`, paper: `https://arxiv.org/abs/2510.16907`, Northwestern University (mll-lab-nu), date: 2025.10

- `Agent0` — ADPO (advantage-decoupled policy optimization) for math/visual reasoning.
  github: `https://github.com/aiming-lab/Agent0`, paper: `https://arxiv.org/abs/2511.16043`, UNC‑Chapel Hill / Salesforce Research / Stanford University, date: 2025.11

- `AgentFlow` — Flow-GRPO with model+external reward for search/math/QA workflows.
  github: `https://github.com/lupantech/AgentFlow`, paper: `https://arxiv.org/abs/2510.05592`, Stanford University, date: 2025.10

- `Open-AgentRL` — GRPO-TCR (turn-conditioned reward) variant for reasoning/GUI/coding.
  github: `https://github.com/Gen-Verse/Open-AgentRL`, paper: `https://arxiv.org/abs/2602.02488`, Gen-Verse, date: 2026.2

- `EasyR1` — GRPO with model reward for vision-language reasoning.
  github: `https://github.com/hiyouga/EasyR1`, Individual, date: 2025.4

## See also

- `length-blowup.md` — generic length issues; thinking-budget is a
  special case.
- `format-reward-gaming.md` — empty thinking is the canonical gaming.
- `entropy-collapse.md` — template collapse on reasoning traces.
- `retokenization-drift.md` — `<think>` / `</think>` tokenization
  pitfalls.
- `sft-to-rl-transition.md` — reasoning-mode SFT preparation.
