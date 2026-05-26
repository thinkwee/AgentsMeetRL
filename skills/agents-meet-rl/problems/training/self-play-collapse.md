# Problem: self-play strategy collapses or cycles

## Symptoms

- In zero-sum self-play, win rate vs *fixed* baseline is flat or
  oscillating.
- Strategy moves between a few attractors without progress (rock-paper-
  scissors loop).
- One side dominates and the other can't recover.

## Root causes

1. **Always playing current snapshot of self.** No memory of past
   strategies.
2. **No diversity in starting position.** Same opening every time.
3. **Reward magnitude is symmetric and trajectory-only.** No signal for
   *how* you won.
4. **Single game / narrow distribution.** Easy to specialize, no
   transfer.

## Diagnosis

- Win rate vs *fixed* baseline: cycling = flat/oscillating; healthy =
  monotone increase.
- Strategy diversity (cluster behaviors over training); collapse =
  decreasing diversity.

## Fixes

### Fix 1: opponent pool

Sample opponent from a pool of past checkpoints, not just current.
Prevents rock-paper-scissors cycling.

> **SPIRAL** — github: `https://github.com/spiral-rl/spiral`,
> paper: `https://arxiv.org/abs/2506.24119`, NUS/A*STAR/Sea AI, date: 2025.6.
> Trains on multiple games (TicTacToe, Kuhn Poker, Negotiation) to avoid
> over-specialization.

### Fix 2: role-conditioned advantage (RAE)

Single policy plays both roles, but advantage is computed per role.

> **SPIRAL's RAE** — see above.

### Fix 3: challenger / solver separation

Use one model to *generate* problems and another to *solve* them. The
challenger gets harder as the solver improves — built-in curriculum.

> **R-Zero** — github: `https://github.com/Chengsong-Huang/R-Zero`,
> paper: `https://arxiv.org/abs/2508.05004`, Tencent AI Seattle,
> date: 2025.8. Challenger + Solver co-evolution with GRPO.

> **CoMAS** — github: `https://github.com/xxyQwQ/CoMAS`,
> paper: `https://arxiv.org/abs/2510.08529`, Shanghai AI Lab/CUHK, date: 2025.10.
> Co-evolving reasoning agents with LLM-judge intrinsic reward.

> **Absolute-Zero-Reasoner** — github:
> `https://github.com/LeapLabTHU/Absolute-Zero-Reasoner`,
> paper: `https://arxiv.org/abs/2505.03335`, Tsinghua, date: 2025.5.
> TRR++ for code/math reasoning, learnability-driven self-play.

### Fix 4: multi-game / multi-task

Train on a suite of related games. Forces general strategy, not
opponent-specific.

### Fix 5: cap max-cycle length

If you detect cycling (same strategy returning), reset opponent pool or
inject SFT on demonstrations.

## Paper / repo references

- `SPIRAL` — github: `https://github.com/spiral-rl/spiral`,
  paper: `https://arxiv.org/abs/2506.24119`, date: 2025.6.
- `R-Zero` — github: `https://github.com/Chengsong-Huang/R-Zero`,
  paper: `https://arxiv.org/abs/2508.05004`, date: 2025.8.
- `CoMAS` — github: `https://github.com/xxyQwQ/CoMAS`,
  paper: `https://arxiv.org/abs/2510.08529`, date: 2025.10.
- `Absolute-Zero-Reasoner` — github:
  `https://github.com/LeapLabTHU/Absolute-Zero-Reasoner`,
  paper: `https://arxiv.org/abs/2505.03335`, date: 2025.5.
