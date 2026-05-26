# Problem: search agent learns to game retriever, not solve task

## Symptoms

- High train reward on cached corpus.
- Eval on real engine drops sharply.
- Queries look weird (literal phrases that match retriever quirks).
- Retrieved passages contain the answer literally; agent just
  paraphrases.

## Root causes

1. **Cached corpus / static retriever** lets the policy find brittle
   query patterns.
2. **Outcome-only reward** without query-quality signal.
3. **Retriever is the same at train and eval** — no distribution shift
   pressure.

## Diagnosis

- **Retrieval-quality vs answer-quality correlation**. If queries are
  bad but answers are good, the retriever is being fooled (or has
  cached answers).
- **Train cached vs train live**: gap > 5 points at eval = hacking.
- **Query length**: hacked queries often have unusual lengths (very
  short or very long).

## Fixes

### Fix 1: dual-level reward (utility + safety/quality)

> **SafeSearch** — github: `https://github.com/amazon-science/SafeSearch`,
> paper: `https://arxiv.org/abs/2510.17017`, Amazon, date: 2025.10.
> Reward both the final answer *and* the safety/quality of the
> intermediate query. Built on Search-R1 + veRL.

### Fix 2: simulate the retriever with adversarial noise

> **ZeroSearch** — github: `https://github.com/Alibaba-NLP/ZeroSearch`,
> paper: `https://arxiv.org/abs/2505.04588`, Alibaba, date: 2025.5.
> Simulates a noisy / wrong retriever to force the policy to be robust.

### Fix 3: change retriever between train and eval

If you have multiple retrievers (BM25, dense, GPT-Search), train on one
mix and eval on another. Forces transferable query strategies.

### Fix 4: query-quality reward

Score the query (separately from answer): is it on-topic? proper
length? specific?

### Fix 5: penalize literal-copying

If retrieved passage and final answer have very high token overlap
(say > 0.8 ROUGE), penalize. Forces the model to actually reason.

### Fix 6: train against real engine for some epochs

Search-R1 supports this:

Train on cached for warm-up, then on live for robustness.

### Fix 7: query rewrite training (not just retrieval)

> **DeepRetrieval** — github: `https://github.com/pat-jj/DeepRetrieval`,
> paper: `https://arxiv.org/abs/2503.00223`, UIUC, date: 2025.3. GRPO
> for query generation specifically.

## Paper / repo references

- `SafeSearch` — github: `https://github.com/amazon-science/SafeSearch`,
  paper: `https://arxiv.org/abs/2510.17017`, Amazon, date: 2025.10.
- `ZeroSearch` — github: `https://github.com/Alibaba-NLP/ZeroSearch`,
  paper: `https://arxiv.org/abs/2505.04588`, Alibaba, date: 2025.5.
- `DeepRetrieval` — github: `https://github.com/pat-jj/DeepRetrieval`,
  paper: `https://arxiv.org/abs/2503.00223`, UIUC, date: 2025.3.

**Other corpus entries:**

- `ReSeek` — GRPO/PPO QA search agent.
  github: `https://github.com/TencentBAC/ReSeek`, paper: `https://arxiv.org/abs/2510.00568`, Tencent PCG BAC/Tsinghua University, date: 2025.10

- `R-Search` — PPO/GRPO QA/search corpus.
  github: `https://github.com/QingFei1/R-Search`, Individual, date: 2025.6

- `R3-RAG` — PPO multi-hop QA.
  github: `https://github.com/Yuan-Li-FNLP/R3-RAG`, paper: `https://arxiv.org/abs/2505.23794`, Fudan NLP, date: 2025.5

- `AutoRefine` — PPO/GRPO RAG QA with refinement.
  github: `https://github.com/syr-cn/AutoRefine`, paper: `https://www.arxiv.org/abs/2505.11277`, USTC, date: 2025.5

- `R1-Searcher-plus` — custom algorithm with model-based reward for search.
  github: `https://github.com/RUCAIBox/R1-Searcher-plus`, paper: `https://arxiv.org/abs/2505.17005`, RUC, date: 2025.5

- `DeepResearcher` — PPO/GRPO research agent.
  github: `https://github.com/GAIR-NLP/DeepResearcher`, paper: `https://arxiv.org/abs/2504.03160`, SJTU, date: 2025.4

- `DeepDive` — GRPO KG-augmented search.
  github: `https://github.com/THUDM/DeepDive`, paper: `https://arxiv.org/abs/2509.10446`, Tsinghua/THUDM, date: 2025.9

- `WebSeer` — GRPO-style with self-reflection on web search QA.
  github: `https://github.com/99hgz/WebSeer`, paper: `https://arxiv.org/abs/2510.18798`, Individual, date: 2025.10

- `O2-Searcher` — GRPO open-ended QA.
  github: `https://github.com/KnowledgeXLab/O2-Searcher`, paper: `https://arxiv.org/abs/2505.16582`, KnowledgeXLab, date: 2025.5

- `knowledge-r1` — GRPO knowledge-base-aware QA.
  github: `https://github.com/hzy312/knowledge-r1`, paper: `https://arxiv.org/abs/2505.07596`, CAS / UCAS, date: 2025.5

- `O-Researcher` — GRPO + RLAIF on Zhihu-KOL/WideSearch/ELI5 deep research.
  github: `https://github.com/OPPO-PersonalAI/O-Researcher`, paper: `https://arxiv.org/abs/2601.03743`, OPPO PersonalAI Lab, date: 2026.1

- `C-3PO` — PPO with model-based reward for search.
  github: `https://github.com/Chen-GX/C-3PO`, paper: `https://arxiv.org/abs/2502.06205`, Alibaba, date: 2025.2

- `Agentic-RAG-R1` — GRPO with rule + model reward for knowledge-intensive QA.
  github: `https://github.com/jiangxinke/Agentic-RAG-R1`, PKU, date: 2025.12

- `WebThinker` — DPO for reasoning/QA/research.
  github: `https://github.com/RUC-NLPIR/WebThinker`, paper: `https://arxiv.org/abs/2504.21776`, RUC, date: 2025.4

- `AutoGraph-R1` — GRPO via veRL for KG construction.
  github: `https://github.com/HKUST-KnowComp/AutoGraph-R1`, paper: `https://arxiv.org/abs/2510.15339`, HKUST KnowComp, date: 2025.10

- `Graph-R1` — GRPO/REINFORCE++/PPO for KG-QA with rule (EM/F1) reward.
  github: `https://github.com/LHRLAB/Graph-R1`, paper: `https://arxiv.org/abs/2507.21892`, BUPT/NTU/NUS, date: 2025.7

- `KG-R1` — GRPO/PPO for KG-QA.
  github: `https://github.com/Jinyeop3110/KG-R1`, UIUC/Google, date: 2025.9
