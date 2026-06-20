# Search & RAG Agents

Agents that interleave reasoning and retrieval. Most use rule-based EM/F1 outcome rewards or info-gain process rewards.

_Total: 45 entries._

## Contents

Harness-1, SlimSearcher, DeepRubric, SAAS, CuSearch, ORBIT, LiteResearcher, DR-Venus, MR-Search, ProRAG, O-Researcher, Agentic-RAG-R1, MemSearcher, DR Tulu, IGPO, ReSeek, AutoGraph-R1, DeepResearch, WebSeer, HiPRAG, Tree-GRPO, DeepDive, ASearcher, SSRL, Research-Venus, Graph-R1, Kimi-Researcher, R-Search, R1-Searcher-plus, StepSearch, AutoRefine, ZeroSearch, ReasonRAG, VRAG, MaskSearch, R3-RAG, O2-Searcher, s3, knowledge-r1, WebThinker, DeepResearcher, Search-R1, R1-Searcher, DeepRetrieval, C-3PO.

### Harness-1
- **Idea:** Externalizes search state (candidate pool, evidence, verification records) into a stateful harness so a small 20B policy can run long-horizon retrieval.
- `https://github.com/pat-jj/harness-1` · org: UIUC · date: 2026.6
- Paper(s): [Paper](https://arxiv.org/abs/2606.02373)
- Algorithm: GRPO · Framework: Custom · Agent: Single · Turns: Multi · Tools: Yes (search/retrieval/rerank)
- Reward phase: Outcome · Reward type: External + Rule
- Task: Long-horizon search (web/finance/patents) w/ state-externalizing harness

### SlimSearcher
- **Idea:** Adaptive reward gating cascades a correctness gate with tool/token-efficiency rewards, cutting deep-research tool-call rounds 17-58% without losing accuracy.
- `https://github.com/AQ-MedAI/AntAFu-DeepResearch` · org: Ant Group / ZJU · date: 2026.6
- Paper(s): [Paper](https://arxiv.org/abs/2606.07074)
- Algorithm: GRPO + Adaptive Reward Gating · Framework: Custom (agentic RL) · Agent: Single · Turns: Multi · Tools: Yes (web search, browse)
- Reward phase: Outcome · Reward type: Custom + Rule
- Task: Efficiency-aware deep research (GAIA/BrowseComp/xBench)

### DeepRubric
- **Idea:** Recursive sub-question expansion turns deep-research supervision into an evidence tree of atomic verifiable rubric leaves, cutting RL GPU-hours ~13x.
- `https://github.com/ZMingHang/DeepRubric-Code` · org: Shandong University · date: 2026.6
- Paper(s): [Paper](https://arxiv.org/abs/2606.17029)
- Algorithm: GRPO + rubric rewards · Framework: verl-tool · Agent: Single · Turns: Multi · Tools: Yes (search/browse/scholar)
- Reward phase: Process · Reward type: Model + Rule (rubric)
- Task: Deep research report synthesis (evidence-tree rubric)

### SAAS
- **Idea:** Boundary-aware reward teaches the agent when NOT to search, mitigating over-search while keeping minimal sufficient retrieval.
- `https://github.com/XMUDeepLIT/SAAS` · org: Xiamen University · date: 2026.5
- Paper(s): [Paper](https://arxiv.org/abs/2605.29796)
- Algorithm: RL w/ boundary-aware reward (2-stage curriculum) · Framework: slime · Agent: Single · Turns: Multi · Tools: Yes (search)
- Reward phase: Outcome · Reward type: Rule-Based
- Task: Self-aware agentic search (over-search mitigation, 7 QA sets)

### CuSearch
- **Idea:** Search-depth-aware curriculum rollout reallocates RL update budget toward deeper-search trajectories, lifting multi-hop EM from outcome-only supervision.
- `https://github.com/MrToser/CuSearch` · org: Academic · date: 2026.5
- Paper(s): [Paper](https://arxiv.org/abs/2605.11611)
- Algorithm: GRPO + Search-Depth curriculum rollout · Framework: Custom · Agent: Single · Turns: Multi · Tools: Yes (retrieval/search)
- Reward phase: Outcome · Reward type: Rule-Based (EM)
- Task: Agentic RAG multi-hop QA

### ORBIT
- **Idea:** Generates 20K verifiable reasoning-intensive web-QA queries at near-zero API cost to train search agents with GRPO on a tight budget.
- `https://github.com/castorini/orbit` · org: University of Waterloo · date: 2026.4
- Paper(s): [Paper](https://arxiv.org/abs/2604.01195)
- Algorithm: GRPO · Framework: Custom · Agent: Single · Turns: Multi · Tools: Yes (web search)
- Reward phase: Outcome · Reward type: External + Rule
- Task: Verifiable data-gen + RL for web search (Qwen3-4B)

### LiteResearcher
- **Idea:** Trains deep-research agents in a 'lite virtual world' mirroring real search dynamics, avoiding the instability and cost of live-search RL.
- `https://github.com/simplex-ai-inc/LiteResearcher` · org: Simplex AI / ZJU / PolyU · date: 2026.4
- Paper(s): [Paper](https://arxiv.org/abs/2604.17931)
- Algorithm: Scalable Agentic RL (curriculum w/ lite virtual world) · Framework: Custom · Agent: Single · Turns: Multi · Tools: Yes (local search/browse env, Milvus+PostgreSQL)
- Reward phase: Outcome · Reward type: Rule/External
- Task: Deep Research (GAIA 71.3% / Xbench-DS 78.0%, 4B SOTA)

### DR-Venus
- **Idea:** Edge-scale (4B) deep-research agent trained with info-gain turn-level rewards plus format-aware regularization to densify supervision and credit assignment.
- `https://github.com/inclusionAI/DR-Venus` · org: Ant Group (inclusionAI) · date: 2026.4
- Paper(s): [Paper](https://arxiv.org/abs/2604.19859)
- Algorithm: GRPO + IGPO (info-gain turn-level) w/ agentic SFT · Framework: veRL (IGPO-based) · Agent: Single · Turns: Multi · Tools: Yes (Search/Browse)
- Reward phase: Both · Reward type: Intrinsic (info-gain) + Rule (format)
- Task: Edge-scale Deep Research (4B)

### MR-Search
- **Idea:** In-context meta-RL conditions each search episode on past episodes plus a self-generated reflection, giving fine-grained multi-episode credit.
- `https://github.com/tengxiao1/MR-Search` · org: Academic · date: 2026.3
- Paper(s): [Paper](https://arxiv.org/abs/2603.11327)
- Algorithm: In-context Meta-RL (multi-episode credit) · Framework: Custom · Agent: Single · Turns: Multi · Tools: Yes (search)
- Reward phase: Outcome · Reward type: Rule-Based
- Task: Agentic search w/ self-reflection

### ProRAG
- **Idea:** GRPO with dual-granularity advantage combining PRM step-level process rewards and global outcome signals to curb process hallucinations in multi-hop RAG.
- `https://github.com/lilinwz/ProRAG` · org: RUC · date: 2026.1
- Paper(s): [Paper](https://arxiv.org/abs/2601.21912)
- Algorithm: GRPO + DGA (dual-granularity advantage) · Framework: Custom · Agent: Single · Turns: Multi · Tools: Yes (Retrieval)
- Reward phase: Both · Reward type: Model (PRM via MCTS)
- Task: Multi-hop RAG

### O-Researcher
- **Idea:** Two-stage SFT-then-RL pipeline over multi-agent synthesized data to boost open-source deep-research agents, combining GRPO with RLAIF for alignment.
- `https://github.com/OPPO-PersonalAI/O-Researcher` · org: OPPO PersonalAI Lab · date: 2026.1
- Paper(s): [Paper](https://arxiv.org/abs/2601.03743)
- Algorithm: GRPO + RLAIF · Framework: Custom · Agent: Multi · Turns: Multi · Tools: Yes (Search/Crawl)
- Reward phase: Process · Reward type: Model (LLM-as-Judge)
- Task: Deep Research (Zhihu-KOL/WideSearch/ELI5)

### Agentic-RAG-R1
- **Idea:** Applies GRPO with composite accuracy/format/RAGAS rewards to jointly optimize when to retrieve and which reasoning steps to take in knowledge-intensive QA.
- `https://github.com/jiangxinke/Agentic-RAG-R1` · org: PKU · date: 2025.12
- Paper(s): —
- Algorithm: GRPO · Framework: Custom · Agent: Single · Turns: Multi · Tools: Yes (Wiki/Doc search)
- Reward phase: Outcome · Reward type: Rule/Model
- Task: Knowledge-intensive QA

### MemSearcher
- **Idea:** Maintains a compact question-relevant memory across turns (stable context length), trained with multi-context GRPO propagating advantages across all turns.
- `https://github.com/icip-cas/MemSearcher` · org: CAS · date: 2025.11
- Paper(s): [Paper](https://arxiv.org/abs/2511.02805)
- Algorithm: Multi-context GRPO · Framework: Custom · Agent: Single · Turns: Multi · Tools: Yes (Web search + Memory)
- Reward phase: Outcome · Reward type: Rule/Model
- Task: Search/QA + Memory

### DR Tulu
- **Idea:** Reinforcement Learning with Evolving Rubrics (RLER): evaluation rubrics co-evolve with the policy to give discriminative on-policy feedback for long-form research without verifiable answers.
- `https://github.com/rlresearch/dr-tulu` · org: AI2 / UW / CMU / MIT · date: 2025.11
- Paper(s): [Paper](https://arxiv.org/abs/2511.19399)
- Algorithm: GRPO + evolving rubrics · Framework: Open-Instruct · Agent: Single · Turns: Multi · Tools: Yes (Search/MCP)
- Reward phase: Outcome · Reward type: Model (rubrics)
- Task: Long-form Deep Research

### IGPO
- **Idea:** Derives dense intrinsic turn-level rewards from the policy's own belief update (gain in P(correct answer)), curing advantage collapse in multi-turn search RL.
- `https://github.com/GuoqingWang1/IGPO` · org: Ant Group · date: 2025.10
- Paper(s): [Paper](https://arxiv.org/abs/2510.14967)
- Algorithm: GRPO + IGPO (Information Gain turn-level reward) · Framework: veRL · Agent: Single · Turns: Multi · Tools: Yes (Search)
- Reward phase: Both · Reward type: Intrinsic (belief Δ) + Outcome
- Task: Multi-turn Search Agent (BrowseComp/-ZH)

### ReSeek
- **Idea:** Adds a JUDGE self-correction action plus decomposed correctness+utility dense rewards so search agents can re-plan mid-episode instead of locking into bad paths.
- `https://github.com/TencentBAC/ReSeek` · org: Tencent PCG BAC/Tsinghua University · date: 2025.10
- Paper(s): [Paper](https://arxiv.org/abs/2510.00568)
- Algorithm: GRPO/PPO · Framework: veRL · Agent: Single · Turns: Multi · Tools: Search/JUDGE
- Reward phase: Both · Reward type: Rule
- Task: QA/Search

### AutoGraph-R1
- **Idea:** Trains an LLM KG constructor with RL where reward is the graph's downstream RAG utility, optimizing for usefulness rather than intrinsic graph quality.
- `https://github.com/HKUST-KnowComp/AutoGraph-R1` · org: HKUST KnowComp · date: 2025.10
- Paper(s): [Paper](https://arxiv.org/abs/2510.15339)
- Algorithm: GRPO (via VeRL) · Framework: Custom · Agent: Single · Turns: Multi · Tools: Yes (Graph retrieval)
- Reward phase: Outcome · Reward type: Rule
- Task: KG Construction for QA

### DeepResearch
- **Idea:** Tongyi DeepResearch couples agentic mid-training and post-training with a fully automatic data-synthesis pipeline, removing human annotation for long-horizon research RL.
- `https://github.com/Alibaba-NLP/DeepResearch` · org: Alibaba/Tongyi Lab · date: 2025.10
- Paper(s): [Paper](https://arxiv.org/abs/2510.24701)
- Algorithm: RL-based · Framework: Custom · Agent: Single · Turns: Multi · Tools: Yes (Search, Browse)
- Reward phase: Outcome · Reward type: Model
- Task: Deep Research

### WebSeer
- **Idea:** Self-reflection-enhanced RL with a unified cold-start + RL two-stage framework that lengthens tool-use trajectories while reducing accumulated errors.
- `https://github.com/99hgz/WebSeer` · org: Individual · date: 2025.10
- Paper(s): [Paper](https://arxiv.org/abs/2510.18798)
- Algorithm: GRPO-style · Framework: veRL · Agent: Single · Turns: Multi · Tools: Yes (Search)
- Reward phase: Outcome · Reward type: Rule/Model
- Task: Web Search QA (w/ self-reflection)

### HiPRAG
- **Idea:** Hierarchical process rewards judge the necessity of each search step on-the-fly, adding a bonus for optimal search/non-search ratio to curb over- and under-search.
- `https://github.com/qualidea1217/HiPRAG` · org: Individual · date: 2025.10
- Paper(s): [Paper](https://arxiv.org/abs/2510.07794)
- Algorithm: PPO · Framework: veRL · Agent: Single · Turns: Multi · Tools: Yes (Retrieval)
- Reward phase: Process · Reward type: Model/Rule
- Task: Efficient Agentic RAG

### Tree-GRPO
- **Idea:** Tree-structured rollouts share prefixes to fit more trajectories per budget and yield step-wise process signals from outcome-only rewards via dual-level advantages.
- `https://github.com/AMAP-ML/Tree-GRPO` · org: AMAP · date: 2025.9
- Paper(s): [Paper](https://arxiv.org/abs/2509.21240)
- Algorithm: GRPO/Tree-GRPO · Framework: veRL · Agent: Single · Turns: Multi · Tools: Search
- Reward phase: Outcome · Reward type: Rule
- Task: Search

### DeepDive
- **Idea:** End-to-end multi-turn RL for web-browsing agents with a redundancy penalty that discourages repeated similar queries, enabling longer reasoning chains.
- `https://github.com/THUDM/DeepDive` · org: Tsinghua/THUDM · date: 2025.9
- Paper(s): [Paper](https://arxiv.org/abs/2509.10446)
- Algorithm: GRPO · Framework: Custom · Agent: Single · Turns: Multi · Tools: Yes (KG + Search)
- Reward phase: Outcome · Reward type: Rule
- Task: KG-augmented Search

### ASearcher
- **Idea:** Fully asynchronous RL plus autonomous QA synthesis enables 100+ turn, 400k-token search training, showing horizon length beats architecture complexity.
- `https://github.com/inclusionAI/ASearcher` · org: Ant Research RL Lab  /  Tsinghua University & UW · date: 2025.8
- Paper(s): [Paper](https://arxiv.org/abs/2508.07976)
- Algorithm: PPO/GRPO + Decoupled PPO · Framework: RealHF/AReaL · Agent: Single · Turns: Multi · Tools: Yes
- Reward phase: Outcome · Reward type: External/Rule
- Task: Math/Code/SearchQA

### SSRL
- **Idea:** Self-Search RL elicits the LLM's own internal knowledge as a simulated search engine via format/rule rewards, cutting external API cost with sim-to-real transfer.
- `https://github.com/TsinghuaC3I/SSRL` · org: Tsinghua · date: 2025.8
- Paper(s): [Paper](https://arxiv.org/abs/2508.10874)
- Algorithm: GRPO · Framework: Custom · Agent: Single · Turns: Multi · Tools: Yes (Self-search)
- Reward phase: Outcome · Reward type: Rule
- Task: Self-Search

### Research-Venus
- **Idea:** Atomic Thought Rewards decompose agent reasoning into functional units scored by reasoning reward models, giving process-level signal early before switching to outcome rewards.
- `https://github.com/antgroup/Research-Venus` · org: Ant Group · date: 2025.8
- Paper(s): [Paper](https://arxiv.org/abs/2508.12800)
- Algorithm: GRPO · Framework: Custom · Agent: Single · Turns: Multi · Tools: Yes (Search)
- Reward phase: Both · Reward type: Model (atomic thought)
- Task: Deep Research

### Graph-R1
- **Idea:** Treats hypergraph RAG retrieval as a multi-turn agent-environment loop optimized end-to-end by RL, replacing fixed one-shot GraphRAG lookups.
- `https://github.com/LHRLAB/Graph-R1` · org: BUPT/NTU/NUS · date: 2025.7
- Paper(s): [Paper](https://arxiv.org/abs/2507.21892)
- Algorithm: GRPO/REINFORCE++/PPO · Framework: veRL · Agent: Single · Turns: Multi · Tools: Yes (Graph retrieval)
- Reward phase: Outcome · Reward type: Rule (EM/F1)
- Task: KGQA

### Kimi-Researcher
- **Idea:** End-to-end REINFORCE research agent with strict on-policy rollouts, negative-sample dropping to avoid entropy collapse, and gamma-decay rewards favoring shorter paths.
- `https://github.com/moonshotai/Kimi-Researcher` · org: Moonshot AI · date: 2025.6
- Paper(s): [blog](https://moonshotai.github.io/Kimi-Researcher/)
- Algorithm: REINFORCE · Framework: Custom · Agent: Single · Turns: Multi · Tools: Search, Browse, Coding
- Reward phase: Outcome · Reward type: Outcome
- Task: Research

### R-Search
- **Idea:** Learns optimal reasoning-search trajectories via multi-reward RL (GRPO/PPO) that jointly balances reasoning quality and search effectiveness.
- `https://github.com/QingFei1/R-Search` · org: Individual · date: 2025.6
- Paper(s): —
- Algorithm: PPO/GRPO · Framework: veRL · Agent: Single · Turns: Multi · Tools: Yes
- Reward phase: Both · Reward type: All
- Task: QA/Search

### R1-Searcher-plus
- **Idea:** SFT cold-start then RL that rewards using internal knowledge and memorizes retrieved facts, so the agent learns when to search vs. recall and needs less retrieval over time.
- `https://github.com/RUCAIBox/R1-Searcher-plus` · org: RUC · date: 2025.5
- Paper(s): [Paper](https://arxiv.org/abs/2505.17005)
- Algorithm: Custom · Framework: Custom · Agent: Single · Turns: Multi · Tools: Search
- Reward phase: Outcome · Reward type: Model
- Task: Search

### StepSearch
- **Idea:** Step-wise PPO with sub-question trajectories and token-level information-gain plus redundancy-penalty rewards to fix sparse rewards in multi-hop search QA.
- `https://github.com/Zillwang/StepSearch` · org: SenseTime · date: 2025.5
- Paper(s): [Paper](https://arxiv.org/abs/2505.15107)
- Algorithm: PPO · Framework: veRL · Agent: Single · Turns: Multi · Tools: Search
- Reward phase: Process · Reward type: Model
- Task: QA

### AutoRefine
- **Idea:** Search-and-refine-during-think: inserts explicit knowledge-refinement steps between searches, trained with GRPO using both retrieval and answer rewards.
- `https://github.com/syr-cn/AutoRefine` · org: USTC · date: 2025.5
- Paper(s): [Paper](https://www.arxiv.org/abs/2505.11277)
- Algorithm: PPO/GRPO · Framework: veRL · Agent: Multi · Turns: Multi · Tools: Search
- Reward phase: Both · Reward type: Rule
- Task: RAG QA

### ZeroSearch
- **Idea:** Replaces costly live search APIs during RL with an SFT'd LLM that generates documents whose quality is curriculum-degraded to progressively elicit reasoning.
- `https://github.com/Alibaba-NLP/ZeroSearch` · org: Alibaba · date: 2025.5
- Paper(s): [Paper](https://arxiv.org/abs/2505.04588)
- Algorithm: PPO/GRPO/REINFORCE · Framework: veRL · Agent: Single · Turns: Multi · Tools: Yes
- Reward phase: Outcome · Reward type: Rule
- Task: QA/Search

### ReasonRAG
- **Idea:** Uses an auto-built process-level reward dataset (query/evidence/answer stages) for process-supervised RAG policy optimization, beating Search-R1 with ~5k vs 90k instances.
- `https://github.com/wlzhang2020/ReasonRAG` · org: CityU HK / Huawei · date: 2025.5
- Paper(s): [Paper](https://arxiv.org/abs/2505.14069)
- Algorithm: DPO + MCTS-based PRM · Framework: Custom · Agent: Single · Turns: Multi · Tools: Yes (Wikipedia search)
- Reward phase: Process · Reward type: Model (PRM)
- Task: Multi-hop QA

### VRAG
- **Idea:** RL for VLMs over visually-rich docs with a crop/scale action space and a reward fusing query rewriting and retrieval performance for coarse-to-fine evidence gathering.
- `https://github.com/Alibaba-NLP/VRAG` · org: USTC / Tongyi Lab, Alibaba · date: 2025.5
- Paper(s): [Paper](https://arxiv.org/abs/2505.22019)
- Algorithm: GRPO · Framework: veRL · Agent: Single · Turns: Multi · Tools: Yes (Visual retrieval)
- Reward phase: Both · Reward type: Rule/Model
- Task: Visually-rich RAG

### MaskSearch
- **Idea:** RAMP pre-training: agents learn to call search to fill masked spans at scale, acquiring universal retrieval-and-reasoning skill before DAPO fine-tuning.
- `https://github.com/Alibaba-NLP/MaskSearch` · org: Tongyi Lab, Alibaba · date: 2025.5
- Paper(s): [Paper](https://arxiv.org/abs/2505.20285)
- Algorithm: DAPO · Framework: DAPO / veRL · Agent: Single · Turns: Multi · Tools: Yes (Search)
- Reward phase: Outcome · Reward type: Rule/Model
- Task: RAMP Pretraining + QA

### R3-RAG
- **Idea:** Multi-hop RAG RL combining outcome reward (answer correctness) with a process reward from relevance-based document verification to learn iterative reason-retrieve loops.
- `https://github.com/Yuan-Li-FNLP/R3-RAG` · org: Fudan NLP · date: 2025.5
- Paper(s): [Paper](https://arxiv.org/abs/2505.23794)
- Algorithm: PPO · Framework: OpenRLHF · Agent: Single · Turns: Multi · Tools: Yes (Retrieval)
- Reward phase: Both · Reward type: Rule
- Task: Multi-hop QA

### O2-Searcher
- **Idea:** Unified reward design trains a 3B agent to distinguish open- vs closed-ended questions and adapt its search/answer strategy, trained in a local simulated search environment.
- `https://github.com/KnowledgeXLab/O2-Searcher` · org: KnowledgeXLab · date: 2025.5
- Paper(s): [Paper](https://arxiv.org/abs/2505.16582)
- Algorithm: GRPO · Framework: veRL · Agent: Single · Turns: Multi · Tools: Yes (Search)
- Reward phase: Outcome · Reward type: Rule/Model
- Task: Open-ended QA

### s3
- **Idea:** Trains a decoupled search-only agent with a Gain-Beyond-RAG reward (accuracy improvement over naive RAG), leaving the generator LLM frozen.
- `https://github.com/pat-jj/s3` · org: UIUC · date: 2025.5
- Paper(s): [Paper](https://arxiv.org/abs/2505.14146)
- Algorithm: GRPO · Framework: veRL · Agent: Single · Turns: Multi · Tools: Yes (Retrieval)
- Reward phase: Outcome · Reward type: Model (Gain-Beyond-RAG)
- Task: RAG / Medical QA

### knowledge-r1
- **Idea:** Knowledge-boundary-aware reward (IKEA) rewards using internal parametric knowledge first and searching only when insufficient, reducing over-retrieval.
- `https://github.com/hzy312/knowledge-r1` · org: CAS / UCAS · date: 2025.5
- Paper(s): [Paper](https://arxiv.org/abs/2505.07596)
- Algorithm: GRPO · Framework: veRL · Agent: Single · Turns: Multi · Tools: Yes (Retrieval)
- Reward phase: Outcome · Reward type: Rule
- Task: Knowledge-intensive QA (KB-aware)

### WebThinker
- **Idea:** Deep Web Explorer with autonomous think-search-draft, trained via iterative online DPO so a reasoning model fills knowledge gaps mid-reasoning.
- `https://github.com/RUC-NLPIR/WebThinker` · org: RUC · date: 2025.4
- Paper(s): [Paper](https://arxiv.org/abs/2504.21776)
- Algorithm: DPO · Framework: Custom · Agent: Single · Turns: Multi · Tools: Web Browsing
- Reward phase: Outcome · Reward type: Model/External
- Task: Reasoning/QA/Research

### DeepResearcher
- **Idea:** End-to-end RL trained directly in the noisy live open web (not a fixed corpus), with browsing agents that cross-validate and self-reflect for robust research.
- `https://github.com/GAIR-NLP/DeepResearcher` · org: SJTU · date: 2025.4
- Paper(s): [Paper](https://arxiv.org/abs/2504.03160)
- Algorithm: PPO/GRPO · Framework: veRL · Agent: Multi · Turns: Multi · Tools: Yes
- Reward phase: Outcome · Reward type: All
- Task: Research

### Search-R1
- **Idea:** RL teaches LLMs to interleave multi-turn search queries with reasoning, using retrieved-token masking to keep training stable.
- `https://github.com/PeterGriffinJin/Search-R1` · org: UIUC/Google · date: 2025.3
- Paper(s): [paper1](https://arxiv.org/abs/2503.09516), [paper2](https://arxiv.org/abs/2505.15117)
- Algorithm: PPO/GRPO · Framework: veRL · Agent: Single · Turns: Multi · Tools: Search
- Reward phase: Outcome · Reward type: All
- Task: Search

### R1-Searcher
- **Idea:** Two-stage outcome-only RL that incentivizes external search without any process rewards or distillation cold-start.
- `https://github.com/RUCAIBox/R1-Searcher` · org: RUC · date: 2025.3
- Paper(s): [Paper](https://arxiv.org/abs/2503.05592)
- Algorithm: PPO/DPO · Framework: OpenRLHF · Agent: Single · Turns: Multi · Tools: Yes
- Reward phase: Both · Reward type: All
- Task: Search

### DeepRetrieval
- **Idea:** RL trains query-generation LLMs using retrieval metrics (e.g. recall) directly as reward, no supervised query data, with a 3B model beating GPT-4o on most IR tasks.
- `https://github.com/pat-jj/DeepRetrieval` · org: UIUC · date: 2025.3
- Paper(s): [Paper](https://arxiv.org/abs/2503.00223)
- Algorithm: GRPO · Framework: veRL · Agent: Single · Turns: Multi · Tools: Yes (Search)
- Reward phase: Outcome · Reward type: Rule
- Task: Query Generation/IR

### C-3PO
- **Idea:** Lightweight proxy-centric multi-agent layer over a frozen retriever+LLM, trained via tree-structured rollouts for RL credit assignment across the agents.
- `https://github.com/Chen-GX/C-3PO` · org: Alibaba · date: 2025.2
- Paper(s): [Paper](https://arxiv.org/abs/2502.06205)
- Algorithm: PPO · Framework: OpenRLHF · Agent: Multi · Turns: Multi · Tools: Yes
- Reward phase: Outcome · Reward type: Model
- Task: Search
