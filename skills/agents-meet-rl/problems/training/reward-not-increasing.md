# Problem: reward never moves off zero — training plateaus immediately

## Symptoms

- After 1000+ steps, train reward is still ≈ 0.
- Loss decreases slightly (KL term, entropy term) but reward doesn't
  change.
- Model outputs look reasonable but never get rewarded.
- Diagnostic: per-batch reward histogram is concentrated at 0.

## Root causes (in order of likelihood)

1. **Reward function bug.** It's not actually awarding anything.
2. **Tool-call parse failures eating rollouts.** See
   `tool-call-parse-failures.md`.
3. **Format mismatch SFT vs RL** so format reward never triggers. See
   `sft-to-rl-transition.md`.
4. **Task too hard for current model.** See `sparse-reward-credit.md`.
5. **Zero-variance group problem.** GRPO advantage is 0 even when
   reward is positive. See `zero-variance-rollouts.md`.
6. **Reward gating on something the model never produces** (e.g.
   `<answer>` tag never closed).

## Diagnosis

Run this checklist before changing anything else:

1. **Reward-function unit test.** Hand-craft 5 obviously-good rollouts
   and 5 obviously-bad. Reward should be ≈1 and ≈0 respectively.
2. **Sample 20 train rollouts.** What fraction reach the answer
   format? What fraction parse correctly? What fraction would *deserve*
   reward by your spec?
3. **Log reward components separately.** If using
   `reward = α*outcome + β*format + γ*length`, log each. If outcome is
   always 0 but format >0, you might have a working signal already.
4. **Check the index/grouping.** GRPO needs a `prompt_id` to group N
   rollouts. If it's accidentally unique-per-rollout, every group has
   N=1 and advantage is 0.

## Fixes

### Fix 1: fix the reward function

Sounds dumb. Most often the issue. Add unit tests **before changing
anything else**:

```python
def test_reward_function():
    good = [
        "<answer>42</answer>",
        "The answer is 42. <answer>42</answer>",
        "Long reasoning... <answer>42</answer>",
    ]
    bad = [
        "I don't know.",
        "<answer></answer>",
        "<answer>43</answer>",         # wrong number
        "42 <answer>42</answer> 42",   # answer outside tags too
        "<answer>4 2</answer>",        # whitespace inside answer
    ]
    for r in good:
        assert reward_fn(r, gold="42") > 0.5, f"good not rewarded: {r!r}"
    for r in bad:
        assert reward_fn(r, gold="42") < 0.5, f"bad rewarded: {r!r}"
    # parser must not crash on garbage
    assert reward_fn("",         gold="42") <= 0.0
    assert reward_fn("\x00\x01", gold="42") <= 0.0
```

If this test passes but training reward is still 0, the problem is
downstream of the reward function — go check root causes 2-6.

### Fix 2: warmup format

If the model never emits the format the reward parser expects, run a
short SFT pass with 100–500 in-format examples. Then resume RL.

### Fix 3: make outcome reward easier to earn (warm-up, not permanent)

For initial training, accept partial credit (substring match instead of
exact match, e.g.). Once reward is moving, tighten.

### Fix 4: stronger SFT cold-start

See `sft-to-rl-transition.md`. Multi-stage SFT is the corpus default
for hard tasks.

### Fix 5: smaller, easier dataset first

If full training set has 30% impossible prompts, you'll see lots of 0s.
Filter to learnable subset first.

### Fix 6: switch to info-gain or PRM reward

When outcome alone is too sparse to learn from. See
`sparse-reward-credit.md`.

## Diagnostic shortcut

Inspect the GRPO trace: scores get computed per-prompt-group, and if
each prompt-id only has one rollout in its group, advantage is silently 0.

In particular: if your prompt-id grouping is unique per rollout, every
group is size 1, and the all-equal-reward branch fires — group mean and
std collapse to a degenerate case so advantage is forced to 0.

This is a common silent bug when integrating custom dataloaders.

## Paper / repo references

> **Search-R1** — github: `https://github.com/PeterGriffinJin/Search-R1`,
> paper: `https://arxiv.org/abs/2503.09516`, org: UIUC/Google, date: 2025.3.
> Why: canonical reward-from-zero recipe for search agents; public wandb
> shows the training-reward curve actually moving — useful baseline to
> compare your own zero-reward run against.

> **RAGEN** — github: `https://github.com/RAGEN-AI/RAGEN`,
> paper: `https://arxiv.org/abs/2504.20073`, org: RAGEN-AI, date: 2025.4.
> Why: the StarPO framework explicitly diagnoses why agentic reward
> stalls (template collapse, info-bottleneck on prompt). Read its
> diagnostics before assuming the reward function alone is at fault.

> **veRL** — github: `https://github.com/volcengine/verl`,
> paper: `https://arxiv.org/abs/2409.19256`, ByteDance Seed, date: 2024.9.
> Why: the all-equal-reward edge case in GRPO advantage
> computation — every group with identical rewards silently gives 0
> gradient — is the most common silent reason advantages stay 0 even
> when reward is non-zero.

- See `sparse-reward-credit.md` and `sft-to-rl-transition.md` for the
  actual recipes.
