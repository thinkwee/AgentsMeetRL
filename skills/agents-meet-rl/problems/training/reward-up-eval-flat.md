# Problem: train reward grows but eval is flat (or drops) — reward hacking

## Symptoms

- Train reward (or even held-out reward on the same env) climbs steadily.
- Eval metric (the *real* thing you care about — task success on a
  benchmark, human eval, downstream task) is flat or drops.
- Read 20 rollouts: they look "off" in some specific way — too long,
  use the same template, game the format, etc.
- Often correlates with very low entropy / template collapse (see
  `entropy-collapse.md`).

## Root causes

1. **Format reward gaming** — the model learns to satisfy a parser, not
   produce content (e.g. emits `<answer></answer>` tags with empty body).
2. **Tool-loop hacking** — each tool call is rewarded, so the model
   spams tool calls regardless of usefulness.
3. **LLM-judge hacking** — the policy learns the judge's biases (length,
   politeness, certain phrasings) rather than the task signal.
4. **Search-engine hacking** — the model finds queries that fool the
   retriever into returning a passage that contains the answer literally
   (works on cached corpus, fails on real engine).
5. **PRM staleness** — the policy outpaces the PRM's training
   distribution; the PRM rewards behaviors that look "good" but no longer
   are.
6. **Reward-spec bug** — the reward function doesn't actually compute
   what you intended (off-by-one, wrong key, wrong scoring rule).

## Diagnosis

### Read the rollouts

There is no substitute. Pick 20 high-reward rollouts. Are they solving
the task or gaming the reward? If you can't tell within 5 minutes, your
reward signal is too noisy.

### Compare train/eval reward, train/eval task accuracy

| Train reward ↑, Train accuracy ↑, Eval accuracy ↑ | Healthy. |
|---|---|
| **Train reward ↑, Train accuracy ↑, Eval accuracy ↓** | Train/eval distribution mismatch (env or sampling). |
| **Train reward ↑, Train accuracy ↓** | Reward hacking. Read rollouts. |

### Audit the reward function

- For LLM-judge: re-judge a held-out batch with a *different* judge (a
  different family — if you used GPT-4o, try Claude-Sonnet, or vice
  versa). Disagreement rate spike across training = hacking.
- For PRM: freeze the PRM, run a fresh policy against it; if PRM scores
  diverge from outcome reward, retrain it.
- For rule-based: write 5 unit tests of the reward against known
  good/bad rollouts.

## Fixes by root cause

### Format reward gaming

> **Cap format weight ≤ 0.1 of outcome.** Most papers in the corpus do
> this.
>
> **Require non-empty content gates.** Don't reward bare tags — only
> reward tags with non-trivial content (e.g. ≥ 10 chars in `<answer>`).
>
> Example: Search-R1's reward function gives format reward only when
> both `<think>` and `<answer>` contain non-empty content — see its
> github (`https://github.com/PeterGriffinJin/Search-R1`).

### Tool-loop hacking

> **Reward only outcome, not the call.** Tool calls cost compute and
> latency — don't pay for them.
>
> **Add efficiency reward.**
> **HiPRAG** — github: `https://github.com/qualidea1217/HiPRAG`,
> paper: `https://arxiv.org/abs/2510.07794`, date: 2025.10. Process
> reward for *efficient* agentic RAG.
>
> **Tool budget.** Cap turns or tool calls per episode; reward 0 on
> overflow.

### LLM-judge hacking

> **Alternate judges.**
> Use a different judge family for some fraction of batches (Claude vs
> GPT vs Qwen).
>
> **Evolving rubrics.**
> **DR Tulu** — github: `https://github.com/rlresearch/dr-tulu`,
> paper: `https://arxiv.org/abs/2511.19399`, AI2/UW/CMU/MIT, date: 2025.11.
> The rubric *itself* updates as the model improves — staleness becomes
> the system's job, not yours.
>
> **Rubric-based + rule-based blend.** Even if the main signal is
> LLM-judge, mix in a small rule-based component (length cap, format
> floor) so that the easy hacks don't dominate.
>
> **Length normalization.** Most LLM judges prefer longer answers.
> **VisionThink** — github:
> `https://github.com/dvlab-research/VisionThink`,
> paper: `https://arxiv.org/abs/2507.13348`, CUHK, date: 2025.7. Reports
> the LLM-judge bias pattern in VQA.

### Search hacking

> **SafeSearch** — github: `https://github.com/amazon-science/SafeSearch`,
> paper: `https://arxiv.org/abs/2510.17017`, Amazon, date: 2025.10.
> Dual-level reward: reward both the final answer *and* the safety of the
> intermediate query. Built on Search-R1+veRL.
>
> **Test against real engine before reporting.** If you trained against a
> cached corpus, eval at least once on live search.
>
> **ZeroSearch's adversarial-style simulator** —
> github: `https://github.com/Alibaba-NLP/ZeroSearch`,
> paper: `https://arxiv.org/abs/2505.04588`, Alibaba, date: 2025.5.
> Simulates noisy/wrong search results to make the model robust.

### PRM staleness

- Refresh PRM on recent rollouts every N steps.
- Down-weight PRM contribution as outcome-reward variance grows
  (curriculum).
- Use PRM for off-policy ranking only; supply outcome reward as the
  ground truth in RL loss.
- Validate PRM separately:
  **ToolPRMBench** — github: `https://github.com/David-Li0406/ToolPRMBench`,
  paper: `https://arxiv.org/abs/2601.12294`, Arizona State, date: 2026.1.

### Reward-spec bug

- Write unit tests for the reward function. Run on:
  - 5 known-good full-credit rollouts → reward should ≈ 1.
  - 5 obviously-wrong rollouts → reward should ≈ 0.
  - 5 partial rollouts → reward should be in between.
- Log the reward function's component breakdown
  (`outcome=0.7, format=0.05, length_pen=-0.02, tool_valid=0.1`) to wandb;
  if any component dominates without you intending, that's the leak.

## Fix patterns by task family

| Family | Anti-hack pattern | Reference |
|---|---|---|
| Search/QA | Dual-level (utility+safety) reward; held-out engine eval | SafeSearch |
| Tool-use | Outcome-only main reward + small tool-validity term | Tool-N1, ReTool |
| Code | Test execution (no proxy); separate localization/repair/test rewards | SWE-Swiss |
| Long-form research | Evolving rubrics | DR Tulu |
| GUI | Click-success + state-progress; not "did the click parse" | UI-TARS, ZeroGUI |

## Paper / repo references

- `SafeSearch` — github: `https://github.com/amazon-science/SafeSearch`,
  paper: `https://arxiv.org/abs/2510.17017`, Amazon, date: 2025.10.
- `DR Tulu` — github: `https://github.com/rlresearch/dr-tulu`,
  paper: `https://arxiv.org/abs/2511.19399`, AI2/UW/CMU/MIT, date: 2025.11.
- `HiPRAG` — github: `https://github.com/qualidea1217/HiPRAG`,
  paper: `https://arxiv.org/abs/2510.07794`, date: 2025.10.
- `ZeroSearch` — github: `https://github.com/Alibaba-NLP/ZeroSearch`,
  paper: `https://arxiv.org/abs/2505.04588`, Alibaba, date: 2025.5.
- `VisionThink` — github: `https://github.com/dvlab-research/VisionThink`,
  paper: `https://arxiv.org/abs/2507.13348`, CUHK, date: 2025.7.
- `ToolPRMBench` — github: `https://github.com/David-Li0406/ToolPRMBench`,
  paper: `https://arxiv.org/abs/2601.12294`, Arizona State, date: 2026.1.
