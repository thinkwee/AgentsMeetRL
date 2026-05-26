# Problem: outputs grow longer every step until they hit the context limit

## Symptoms

- `mean_response_length` rises monotonically across training.
- Eventually rollouts truncate at `max_response_length`; reward drops.
- Many rollouts have `<eos>` never emitted; instead they stop because of
  length cap.
- Often co-occurs with reward-hacking (longer answer = higher LLM-judge
  score) or template collapse (longer rollout = more chances for the
  rewarded template to appear).

## Root causes

1. **Sequence-level loss bias.** Vanilla GRPO sums per-token loss over
   the response — longer sequences contribute more update magnitude per
   rollout, biasing the optimizer toward verbose outputs.
2. **LLM judge length bias.** Most LLM judges prefer longer answers
   (false signal of "thoroughness").
3. **Format reward gaming.** If `<think>...</think>` gets format-reward
   independent of content quality, the model maximizes thinking length.
4. **No EOS shaping.** No reward signal for emitting EOS at the right
   place.

## Diagnosis

- Plot `response_length_mean` and `response_length_p95` over time.
  Healthy training is flat or only slightly increasing.
- Log `truncated_fraction` (fraction of rollouts that hit
  max_response_length without EOS).
- If LLM-judge based: re-judge a batch with length normalization, check
  if reward correlates strongly with length.
- Sample 20 long rollouts. Are they verbose because the task warrants
  it, or because of repetition / padding?

## Fixes

### Fix 1: token-level loss (DAPO / Dr.GRPO)

This is the canonical fix. Replace sequence-level loss with token-level
loss so that each token contributes equally regardless of sequence
length.

> **DAPO** — paper: `https://arxiv.org/abs/2503.14476`,
> blog: `https://dapo-sia.github.io/`, ByteDance Seed, date: 2025.3.
> Adds:
>
> 1. Token-level loss
> 2. Dynamic clipping (different ε for positive vs negative advantage)
> 3. Overlong-shaping reward (penalty before length blows up)
>
> Achieved 50pt on AIME-2024 from Qwen2.5-32B base, surpassing DeepSeek's
> GRPO. Trained with veRL.

> **Dr.GRPO** — `https://arxiv.org/abs/2503.20783`, supported by veRL
> and Tunix. Length-stable GRPO. veRL exposes it via the
> `norm_adv_by_std_in_grpo=False` toggle.

The idea: with `norm_adv_by_std_in_grpo=True` (original GRPO),
advantage is scaled by group std, which couples reward magnitude to
sequence length. With `False` (Dr.GRPO), advantage is `r - μ`
unscaled — length and reward magnitude become independent.

### Fix 2: explicit length penalty

Add a soft length penalty to the reward:

- Hard cap: `reward -= max(0, length - L_target) * 0.001`.
- Smooth: `reward *= sigmoid((L_target - length) / scale)`.

DAPO's "overlong-shaping reward" is this idea applied before the cap is
hit (anticipatory penalty).

### Fix 3: LLM-judge length normalization

If you use an LLM judge:

- Truncate or summarize answers above a length threshold before judging.
- Add a "length-equity" prompt: "Score on correctness only, ignore
  length and verbosity."
- Use a different judge family that's known to be less length-biased.

### Fix 4: EOS shaping

Reward emitting `<answer>...</answer><eos>` cleanly. Penalize rollouts
that hit length cap without `<eos>`.

> Most projects in the corpus that use a `<think>...</think><answer>...
> </answer>` template enforce a strict format reward that *requires*
> closing `<answer>` tag, not just opening it.

### Fix 5: cap thinking length

If thinking is unbounded, cap it:

- Hard cap on `</think>` tag emission (e.g. truncate after 1024 thinking
  tokens, force-emit `<answer>`).
- Apply only thinking-section length penalty.

> **Mini-o3** — github: `https://github.com/Mini-o3/Mini-o3`,
> paper: `https://arxiv.org/abs/2509.07969`, Mini-o3 team, date: 2025.9.
> Visual search/V*; bounded thinking.

### Fix 6: contrastive RL (when reward is hardware-grounded)

For tasks where length doesn't matter (CUDA TFLOPs, code test pass), use
the env's signal directly without intermediate length pressure.

> **CUDA-L1** — github: `https://github.com/deepreinforce-ai/CUDA-L1`,
> paper: `https://arxiv.org/abs/2507.14111`, DeepReinforce AI, date: 2025.7.
> Performance reward in TFLOPs; sidesteps length issues entirely.

## Paper / repo references

- `DAPO` — paper: `https://arxiv.org/abs/2503.14476`,
  blog: `https://dapo-sia.github.io/`, ByteDance Seed, 2025.3.
- `Dr.GRPO` — `https://arxiv.org/abs/2503.20783`.
- `Mini-o3` — github: `https://github.com/Mini-o3/Mini-o3`,
  paper: `https://arxiv.org/abs/2509.07969`, date: 2025.9.
- `MaskSearch` (DAPO-based) — github:
  `https://github.com/Alibaba-NLP/MaskSearch`,
  paper: `https://arxiv.org/abs/2505.20285`, Tongyi Lab, date: 2025.5.
- `Agent_Foundation_Models` (DAPO/PPO) — github:
  `https://github.com/OPPO-PersonalAI/Agent_Foundation_Models`,
  paper: `https://arxiv.org/abs/2508.13167`, OPPO, date: 2025.8.
