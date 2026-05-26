# Problem: thinking / answer / format tags get gamed

## Symptoms

- High format reward, low outcome reward.
- Reward total looks healthy but eval doesn't move.
- Sample 20 rollouts: see `<think></think><answer></answer>` (empty
  bodies) or thinking content that's repetitive padding.
- Total length is fine but content is junk.

## Root causes

1. **Format reward has no content gate.** Awarding for "tag exists"
   instead of "tag has meaningful content."
2. **Format weight is too high relative to outcome.**
3. **The thinking section has no quality signal at all.** Optimizer can
   put anything in there with zero penalty.

## Diagnosis

- Log `mean_thinking_length`, `mean_answer_length` separately.
- Inspect 20 high-reward rollouts. If thinking is empty / junk /
  repetitive, gaming is happening.
- Compute correlation: format-reward vs outcome-reward across the
  batch. If they're uncorrelated (both >0 simultaneously is rare), the
  format is decoupled from quality — likely gamed.

## Fixes

### Fix 1: gate format reward on non-empty content

Don't reward bare tags. Require ≥ 10 chars in `<answer>`, ≥ 50 chars in
`<think>` (or whatever's appropriate).

This is what Search-R1, ToRL, ARPO do.

> **Search-R1** — github: `https://github.com/PeterGriffinJin/Search-R1`,
> paper: `https://arxiv.org/abs/2503.09516`, UIUC, date: 2025.3.
> Format reward requires both `<think>` and `<answer>` to contain
> non-empty content — bare tags get 0, not 0.5.

### Fix 2: cap format weight ≤ 0.1× outcome

Corpus consensus. If outcome reward is in [0, 1], format reward should
be at most 0.1 — never the dominant signal.

### Fix 3: add an LLM-judge or rule-based "content quality" gate

If thinking content is junk, an LLM-judge can score "is this thinking
relevant to the prompt" with a yes/no rubric. Use as small auxiliary.

### Fix 4: use info-gain reward instead of format reward

Info gain *implicitly* rewards useful content (content that moves
log-prob toward gold answer). No need to police format separately.

> **IGPO** — github: `https://github.com/GuoqingWang1/IGPO`,
> paper: `https://arxiv.org/abs/2510.14967`. See `sparse-reward-credit.md`.

### Fix 5: penalize repetition

Cheap fix: 4-gram repetition penalty inside thinking. Empirical, keeps
the gaming bounded.

### Fix 6: thinking length cap

Cap thinking at, e.g., 1024 tokens. Forces the model to be concise.

> **Mini-o3** — github: `https://github.com/Mini-o3/Mini-o3`,
> paper: `https://arxiv.org/abs/2509.07969`, date: 2025.9. Bounded
> thinking for visual search.

### Fix 7: switch to function-call format

If your tags are XML-style and getting gamed, the model's native
function-calling format is harder to game (more constrained).

## Paper / repo references

- See `reward-up-eval-flat.md`, `sparse-reward-credit.md` for the
  specific paper recipes that handle this.
