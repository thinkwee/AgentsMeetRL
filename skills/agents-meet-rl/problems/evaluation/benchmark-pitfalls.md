# Problem: which benchmark — and what's wrong with each

This is the researcher's view: for the benchmark you've already chosen,
what are its known issues and how do you mitigate them?

## SWE-Bench / SWE-Bench Verified

The de-facto SWE benchmark. Known issues:

- **Test-set leakage.** Most SWE projects in the corpus train on
  SWE-Gym (paired training set). Make sure your training data hasn't
  leaked verified test instances.
- **Environment drift.** SWE-Bench requires Docker images for each
  task; image versions matter. Pin them.
- **Runtime variance.** Test execution time varies; OOM during eval.
  Run on consistent hardware.

Mitigations from corpus:

> **SWE-Swiss** — github: `https://github.com/zhenyuhe00/SWE-Swiss`.
> Enhanced self-consistency for candidate selection.

> **SWE-World** — github: `https://github.com/RUCAIBox/SWE-World`,
> paper: `https://arxiv.org/abs/2602.03419`, RUC, date: 2026.2. Docker-
> free SWE.

## WebArena / WebArena-Lite

- **WebArena** is realistic but slow (60+ seconds per task). Lite
  subset is faster but smaller.
- **Cookie state / login state** must be reset per task.
- **Score reporting**: success rate (binary) is standard but very noisy
  on small samples.

> **WebAgent-R1** — github: `https://github.com/weizhepei/WebAgent-R1`,
> paper: `https://arxiv.org/abs/2505.16421`, date: 2025.5. Recent
> WebArena-Lite recipe.

## OSWorld / TheAgentCompany

- Real desktop OS tasks. **Per-rollout sandbox spin-up is expensive.**
- **Determinism is hard** — UI may differ across machines.
- **Long episodes** (50+ steps); statistical power is low without many
  episodes.

Used by: UI-TARS, GTA1, ARPO, DART-GUI, Mano-P.

## AndroidWorld / appworld

- Android emulator with real apps.
- **Emulator state pollution** between tasks; reset carefully.
- **Network mocking** required for deterministic eval.

Used by: MobileRL, AgentCPM-GUI, GUI-Libra.

## ALFWorld

- Classic embodied / TextGame.
- **Saturated** at top of leaderboard (~95%); use only for warm-up.

## tau-bench / tau2-bench

- Tool-agent-user evaluation. Sierra Research.
- **LLM-judge based**; known judge variance.
- tau2 is harder, with better judges.

> **UserRL** — github: `https://github.com/SalesforceAIResearch/UserRL`,
> paper: `https://arxiv.org/abs/2509.19736`, Salesforce, date: 2025.9.
> Recipes for tau-style multi-turn user interactions.

## MCP-Bench / MCPVerse / MCP-Universe

- MCP tool-use benchmarks. Newer (2025.5+).
- **Tool stability** matters — some MCP servers go offline.
- Cache tool responses for reproducibility.

> **MCP-Bench** — github: `https://github.com/Accenture/mcp-bench`,
> paper: `https://arxiv.org/abs/2508.20453`, Accenture, date: 2025.8.
> 28 servers, NeurIPS 2025 Workshop.

## BrowseComp / BrowseComp-Plus / BrowseComp-ZH

- Hard real-web research questions.
- **Live web** = high variance; expensive.
- **Anti-contamination** is the explicit design goal.

> **DR-Venus** — github: `https://github.com/inclusionAI/DR-Venus`,
> paper: `https://arxiv.org/abs/2604.19859`. Strong baseline.
> **IGPO** — github: `https://github.com/GuoqingWang1/IGPO`,
> paper: `https://arxiv.org/abs/2510.14967`. Trains on BrowseComp.

## GAIA

- Hard real-world research questions. Used as eval target by many.
- **LLM-as-judge** with own variance.

## AIME / MATH-500 / Olympiad / GSM8K

- Math benchmarks. Mostly verifiable (rule-based).
- **AIME contamination** is real — recent papers use 2024 / 2025 AIME
  for fresh eval.
- **Pass@1 with high temperature** is unreliable; use majority@k or
  pass@k with care.

## HumanEval / MBPP / LiveCodeBench

- Code benchmarks.
- **Test contamination** is a known issue. LiveCodeBench is the recent
  go-to to avoid contamination.

## Diagnosis: how to detect benchmark issues in your run

1. **Run base (untrained) model on the benchmark.** Establishes
   baseline. Gap to your trained model is real signal; if base model
   already hits 80%, the benchmark is too easy or contaminated.
2. **Run on dev/test split separately.** If dev >> test, you may have
   over-fit to dev.
3. **Multiple seeds on the same benchmark.** High variance =
   small sample size = your improvement may be noise.

## See also

- `data-contamination.md` — contamination detection.
- `reproducibility.md` — env / Docker / API drift.
- `long-horizon-eval.md` — when episodes are too costly.

## Paper / repo references

**Other corpus entries:**

- `Mind2Web-2` — web benchmark — newer than Mind2Web, watch for contamination/protocol changes.
  github: `https://github.com/OSU-NLP-Group/Mind2Web-2`, Ohio State University, date: 2025.6
