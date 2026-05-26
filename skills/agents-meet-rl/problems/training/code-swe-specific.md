# Problem: code/SWE agents — sandbox flakiness, test-pass reward gaming

## Symptoms

- Sandbox runs fail spuriously (Docker / container / port issues).
- Reward signal flaky because tests are flaky.
- Agent learns to pass weak tests but fails strong ones.
- Repository-level edits work in sandbox, fail in deployment.

## Patterns from the corpus

### Three-skill decomposition

> **SWE-Swiss** — github: `https://github.com/zhenyuhe00/SWE-Swiss`.
> Localization + Repair + Test Generation, each with its own reward.

### Patch-similarity reward (cheaper than test execution)

> **swe-rl** — github: `https://github.com/facebookresearch/swe-rl`,
> paper: `https://arxiv.org/abs/2502.18449`, Meta/UIUC/CMU, date: 2025.2.
> Patch-similarity reward — no test execution needed during training.
> Trade-off: signal is weaker than test pass/fail.

### Docker-free SWE training (when Docker is unreliable)

> **SWE-World** — github: `https://github.com/RUCAIBox/SWE-World`,
> paper: `https://arxiv.org/abs/2602.03419`, RUC, date: 2026.2. Learned
> world-model surrogate (SWT + SWR). Skip Docker entirely.

### Test execution as reward

> **CURE** — github: `https://github.com/Gen-Verse/CURE`,
> paper: `https://arxiv.org/abs/2506.03136`, UChicago/Princeton, date: 2025.6.
> External test-suite execution.

> **AceCoder** — github: `https://github.com/TIGER-AI-Lab/AceCoder`,
> paper: `https://arxiv.org/abs/2502.01718`, Waterloo, date: 2025.2.
> Test-case-based external reward.

### Curriculum / two-stage RL for SWE

> **SWE-Swiss two-stage RL curriculum** — train on easy first, then
> hard.

> **MedAgentGym** — github: `https://github.com/wshi83/MedAgentGym`,
> paper: `https://arxiv.org/abs/2506.04405`, Emory, date: 2025.6.
> SFT/DPO/PPO/GRPO on medical code.

### Repo-level search before edit

> **RepoDeepSearch** — github: `https://github.com/Mizersy/RepoDeepSearch`,
> paper: `https://arxiv.org/abs/2508.03012`, PKU/ByteDance/BIT, date: 2025.8.
> Search/Repair via GRPO.

> **PPP-Agent** — github: `https://github.com/sunnweiwei/PPP-Agent`,
> paper: `https://arxiv.org/abs/2511.02208`, CMU/OpenHands, date: 2025.11.
> SWE/Research with Search/Ask/Browse tools.

### Hardware-grounded reward (CUDA)

> **CUDA-L1** — github: `https://github.com/deepreinforce-ai/CUDA-L1`,
> paper: `https://arxiv.org/abs/2507.14111`, DeepReinforce, date: 2025.7.
> Performance reward in TFLOPs (continuous, no flakiness).

> **CUDA-L2** — github: `https://github.com/deepreinforce-ai/CUDA-L2`,
> paper: `https://arxiv.org/abs/2512.02551`, date: 2025.12. Successor;
> HGEMM / matmul.

> **CUDA-Agent** — github: `https://github.com/BytedTsinghua-SIA/CUDA-Agent`,
> paper: `https://arxiv.org/abs/2602.24286`, ByteDance/Tsinghua, date: 2026.2.
> Staged agentic RL for CUDA kernel generation.

### Code interpreter / tool-integrated reasoning

> **R1-Code-Interpreter** — github:
> `https://github.com/yongchao98/R1-Code-Interpreter`,
> paper: `https://arxiv.org/abs/2505.21668`, MIT, date: 2025.5.

> **DeepAnalyze** — github: `https://github.com/ruc-datalab/DeepAnalyze`,
> paper: `https://arxiv.org/abs/2510.16872`, RUC/Tsinghua, date: 2025.10.
> Curriculum RL for data science.

### Critic-based code refinement

> **CTRL** — github: `https://github.com/HKUNLP/critic-rl`,
> paper: `https://arxiv.org/abs/2502.03492`, HKU/ByteDance, date: 2025.2.
> Critique-revision RL for code.

## Sandbox flakiness fixes

See `env-flakiness.md`. Key:

- Per-rollout fresh container.
- Treat sandbox failures as missing data, not 0 reward.
- Cap tool output (some tests output huge logs).

## Test-pass reward gaming

If your reward is "tests pass," the model can:

- Edit the tests to pass (specify test files as read-only).
- Inject test stubs (verify tests are non-trivial).
- Game eval-time tests if known (use held-out tests).

> **SWE-Swiss enhanced self-consistency** uses similarity score for
> candidate selection — reduces gaming.

> **CURE** runs the actual official test suite.

## Paper / repo references

(All cited above.)

**Other corpus entries:**

- `rllm` — PPO/GRPO for code-edit (Berkeley/Together AI).
  github: `https://github.com/agentica-project/rllm`, Berkeley Sky Computing Lab  /  BAIR / Together AI, date: 2025.1

- `Time-R1` — PPO/GRPO/DPO with all-reward types for temporal reasoning code.
  github: `https://github.com/ulab-uiuc/Time-R1`, paper: `https://arxiv.org/abs/2505.13508`, UIUC, date: 2025.5

- `ML-Agent` — custom RL for code generation (MASWorks).
  github: `https://github.com/MASWorks/ML-Agent`, paper: `https://arxiv.org/abs/2505.23723`, MASWorks, date: 2025.5

- `digitalhuman` — PPO/GRPO/ReMax/RLOO across multimodal including code.
  github: `https://github.com/Tencent/digitalhuman`, paper: `https://arxiv.org/abs/2507.03112`, Tencent, date: 2025.7

- `sweet_rl` — DPO for design/code (Meta/UCB).
  github: `https://github.com/facebookresearch/sweet_rl`, paper: `https://arxiv.org/abs/2503.15478`, Meta/UCB, date: 2025.3

- `open-r1` — GRPO for math+code (HuggingFace's reproduction of R1-style training).
  github: `https://github.com/huggingface/open-r1`, HuggingFace, date: 2025.1

- `LLM-in-Sandbox` — GRPO++ multi-domain including SWE.
  github: `https://github.com/llm-in-sandbox/llm-in-sandbox`, paper: `https://huggingface.co/papers/2601.16206`, RUC/MSRA/THU, date: 2026.1
