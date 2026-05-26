# Problem: suspect data contamination on eval benchmark

## Symptoms

- Eval scores are surprisingly high.
- Score gap between similar prompts (one in pretrain corpus, one not)
  is huge.
- Held-out subset eval is much lower than full eval.
- Model knows answer-specific details that wouldn't be plausible from
  generalization.

## Root causes

1. **Benchmark in pretrain corpus.** GSM8K, MATH, HumanEval all
   leaked into many pretrain corpora.
2. **SFT data overlapping benchmark.** Common when SFT data was distilled
   from a strong model that also saw the benchmark.
3. **Training rollouts on tasks similar to eval.** Even if not identical
   prompts, near-duplicates count.

## Diagnosis

### Test 1: paraphrase resistance

Take 20 eval questions, paraphrase them by hand or via LLM. If the
paraphrased version drops dramatically in score, the model memorized
the surface form, not the content.

### Test 2: subset comparison

Split eval into "likely-in-pretrain" and "likely-fresh" (e.g. AIME
2018 vs AIME 2024). Score gap > 5 points = contamination on older.

### Test 3: completion under partial prompt

Show the model only the first half of the prompt; ask it to predict
the second half. If it can predict ground-truth answer or distinctive
benchmark phrasing, it has seen it.

### Test 4: explicit memorization probe

Show a benchmark question slightly malformed. A non-memorized model
fails consistently; a memorized one might still produce the gold answer
because it pattern-matched the surface form.

## Fixes

### Use post-cutoff benchmarks

For math: AIME 2024 / 2025, MathArena. Recent enough to avoid most
pretrain corpora.

For code: LiveCodeBench (date-stamped tasks).

For deep research: BrowseComp / BrowseComp-Plus (anti-contamination
design).

### Held-out splits

Some benchmarks have explicit held-out subsets. Use them.

### Decontamination

Remove training rollouts whose prompts are textually similar to eval.
N-gram overlap > 8 is a reasonable filter.

### Report multiple benchmarks

If your model is great on GSM8K but bad on a fresh benchmark,
contamination is likely. Reporting multiple benchmarks of varying
freshness exposes this.

## What benchmarks in this corpus are anti-contamination

- **BrowseComp / BrowseComp-Plus / BrowseComp-ZH** — designed against
  contamination.
- **MCP-Bench / MCP-Universe** — MCP tools and tasks too recent.
- **OSWorld** — real OS, hard to embed in pretrain.
- **SWE-Bench Verified** — careful curation; partial protection.
- **MathArena**, **AIME 2024+** — recent.

## Mitigation by task family

| Family | Anti-contam strategy |
|---|---|
| Math | AIME 2024+, MathArena |
| Code | LiveCodeBench, SWE-Bench Verified |
| Research/Search | BrowseComp-Plus, GAIA |
| GUI | OSWorld, AndroidWorld (live UI) |
| Tool-use | MCP-Bench, tau2-bench |

## Paper / repo references

- `BrowseComp-Plus` — github: `https://github.com/texttron/BrowseComp-Plus`,
  University of Waterloo, date: 2025.8.
- `MCP-Bench` — github: `https://github.com/Accenture/mcp-bench`,
  paper: `https://arxiv.org/abs/2508.20453`, Accenture, date: 2025.8.
- `tau2-bench` — github: `https://github.com/sierra-research/tau2-bench`,
  Sierra Research, date: 2025.6.

**Other corpus entries:**

- `PaperArena` — scientific literature QA — high contamination risk for arxiv-trained models.
  github: `https://github.com/Melmaphother/PaperArena`, University of Science and Technology of China, date: 2025.9
