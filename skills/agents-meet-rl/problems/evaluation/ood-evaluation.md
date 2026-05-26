# Problem: how do I design OOD / distribution-shift evaluation

## Why this matters

Most papers in the corpus train on a narrow data distribution (e.g.
HotpotQA + NaturalQuestions for search). They report numbers on similar
benchmarks. But **agentic RL claims often don't transfer OOD**.

You should test:

- New tasks (different domain).
- New tools (different APIs / MCP servers).
- New languages (English ≠ Chinese ≠ multilingual).
- New users (different prompt styles).

## Patterns from the corpus

### OOD eval as paper contribution

> **SkillRL** — github: `https://github.com/aiming-lab/SkillRL`,
> paper: `https://arxiv.org/abs/2602.08234`, UNC-Chapel Hill, date: 2026.2.
> ALFWorld, WebShop, Search across categories.

> **MarsRL** — github: `https://github.com/liushulinle/MarsRL`,
> paper: `https://arxiv.org/abs/2511.11373`, date: 2025.11. AIME +
> "BeyondAIME" — explicit OOD slice.

> **AgentRM** — github: `https://github.com/thunlp/AgentRM`,
> paper: `https://arxiv.org/abs/2502.18407`, THUNLP, date: 2025.2.
> Generalizable across 9 agent tasks.

### Cross-platform GUI

> **UI-TARS** — single model, mobile + desktop + web.
> **GUI-Libra** — AndroidWorld + WebArena + Online-Mind2Web.

### Cross-language search

> **DeepSeek-style** OOD evals: train on English, test on Chinese.
> **BrowseComp-ZH** — Chinese variant of BrowseComp.

### MCP transfer

Train on N MCP servers, eval on held-out servers.

> **MCP-Universe** — github:
> `https://github.com/SalesforceAIResearch/MCP-Universe`, Salesforce,
> date: 2025.5. Diverse MCP coverage.

## Designing your OOD eval

### Step 1: choose a clean shift dimension

Don't conflate. Pick one:

- Domain (medical → legal).
- Tool (RapidAPI → MCP servers).
- Language (en → zh).
- Length (short Q → long-horizon).
- User style (instructions → conversation).

### Step 2: control for capacity

If you're claiming "trained model A beats baseline B OOD," make sure
both have seen comparable training. Otherwise capacity is the
confounder.

### Step 3: report multiple OOD splits

Pick 3-5 OOD slices. Show your method generalizes across most. A model
that wins one OOD by 10 points but loses 4 OODs by 5 points isn't
generalizing.

### Step 4: in-distribution control

Always report ID alongside OOD. ID-OOD gap shows how much your training
specialized.

## Common OOD failures

1. **Search-corpus shift**: trained on cached, eval on live → search
   hacking.
2. **Tool-API shift**: trained on simulated API, eval on real → broken
   tool calls.
3. **Length shift**: trained on 5-turn, eval on 50-turn → context
   overflow / credit collapse.
4. **Language shift**: bilingual eval drops 5-15 points.

## What to put in a paper

- **Headline ID number**: your benchmark.
- **OOD result**: at least 1-2 OOD benchmarks.
- **Ablation**: training without your method on OOD — to show your
  method, not the data, drives transfer.

## Paper / repo references

(All cited above.)
