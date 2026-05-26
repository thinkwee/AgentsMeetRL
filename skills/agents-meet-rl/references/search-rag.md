# Search & RAG Agents

Agents that interleave reasoning and retrieval. Most use rule-based EM/F1 outcome rewards or info-gain process rewards.

_Total: 38 entries._

## Contents

LiteResearcher, DR-Venus, ProRAG, O-Researcher, Agentic-RAG-R1, MemSearcher, DR Tulu, IGPO, ReSeek, AutoGraph-R1, WebSeer, HiPRAG, Tree-GRPO, DeepResearch, DeepDive, ASearcher, SSRL, Research-Venus, Graph-R1, Kimi-Researcher, R-Search, R1-Searcher-plus, StepSearch, AutoRefine, ZeroSearch, ReasonRAG, VRAG, MaskSearch, R3-RAG, O2-Searcher, s3, knowledge-r1, WebThinker, DeepResearcher, Search-R1, R1-Searcher, C-3PO, DeepRetrieval.

### LiteResearcher
- `https://github.com/simplex-ai-inc/LiteResearcher` · org: Simplex AI / ZJU / PolyU · date: 2026.4
- Paper(s): [Paper](https://arxiv.org/abs/2604.17931)
- Algorithm: Scalable Agentic RL (curriculum w/ lite virtual world) · Framework: Custom · Agent: Single · Turns: Multi · Tools: Yes (local search/browse env, Milvus+PostgreSQL)
- Reward phase: Outcome · Reward type: Rule/External
- Task: Deep Research (GAIA 71.3% / Xbench-DS 78.0%, 4B SOTA)

### DR-Venus
- `https://github.com/inclusionAI/DR-Venus` · org: Ant Group (inclusionAI) · date: 2026.4
- Paper(s): [Paper](https://arxiv.org/abs/2604.19859)
- Algorithm: GRPO + IGPO (info-gain turn-level) w/ agentic SFT · Framework: veRL (IGPO-based) · Agent: Single · Turns: Multi · Tools: Yes (Search/Browse)
- Reward phase: Both · Reward type: Intrinsic (info-gain) + Rule (format)
- Task: Edge-scale Deep Research (4B)

### ProRAG
- `https://github.com/lilinwz/ProRAG` · org: RUC · date: 2026.1
- Paper(s): [Paper](https://arxiv.org/abs/2601.21912)
- Algorithm: GRPO + DGA (dual-granularity advantage) · Framework: Custom · Agent: Single · Turns: Multi · Tools: Yes (Retrieval)
- Reward phase: Both · Reward type: Model (PRM via MCTS)
- Task: Multi-hop RAG

### O-Researcher
- `https://github.com/OPPO-PersonalAI/O-Researcher` · org: OPPO PersonalAI Lab · date: 2026.1
- Paper(s): [Paper](https://arxiv.org/abs/2601.03743)
- Algorithm: GRPO + RLAIF · Framework: Custom · Agent: Multi · Turns: Multi · Tools: Yes (Search/Crawl)
- Reward phase: Process · Reward type: Model (LLM-as-Judge)
- Task: Deep Research (Zhihu-KOL/WideSearch/ELI5)

### Agentic-RAG-R1
- `https://github.com/jiangxinke/Agentic-RAG-R1` · org: PKU · date: 2025.12
- Paper(s): —
- Algorithm: GRPO · Framework: Custom · Agent: Single · Turns: Multi · Tools: Yes (Wiki/Doc search)
- Reward phase: Outcome · Reward type: Rule/Model
- Task: Knowledge-intensive QA

### MemSearcher
- `https://github.com/icip-cas/MemSearcher` · org: CAS · date: 2025.11
- Paper(s): [Paper](https://arxiv.org/abs/2511.02805)
- Algorithm: Multi-context GRPO · Framework: Custom · Agent: Single · Turns: Multi · Tools: Yes (Web search + Memory)
- Reward phase: Outcome · Reward type: Rule/Model
- Task: Search/QA + Memory

### DR Tulu
- `https://github.com/rlresearch/dr-tulu` · org: AI2 / UW / CMU / MIT · date: 2025.11
- Paper(s): [Paper](https://arxiv.org/abs/2511.19399)
- Algorithm: GRPO + evolving rubrics · Framework: Open-Instruct · Agent: Single · Turns: Multi · Tools: Yes (Search/MCP)
- Reward phase: Outcome · Reward type: Model (rubrics)
- Task: Long-form Deep Research

### IGPO
- `https://github.com/GuoqingWang1/IGPO` · org: Ant Group · date: 2025.10
- Paper(s): [Paper](https://arxiv.org/abs/2510.14967)
- Algorithm: GRPO + IGPO (Information Gain turn-level reward) · Framework: veRL · Agent: Single · Turns: Multi · Tools: Yes (Search)
- Reward phase: Both · Reward type: Intrinsic (belief Δ) + Outcome
- Task: Multi-turn Search Agent (BrowseComp/-ZH)

### ReSeek
- `https://github.com/TencentBAC/ReSeek` · org: Tencent PCG BAC/Tsinghua University · date: 2025.10
- Paper(s): [Paper](https://arxiv.org/abs/2510.00568)
- Algorithm: GRPO/PPO · Framework: veRL · Agent: Single · Turns: Multi · Tools: Search/JUDGE
- Reward phase: Both · Reward type: Rule
- Task: QA/Search

### AutoGraph-R1
- `https://github.com/HKUST-KnowComp/AutoGraph-R1` · org: HKUST KnowComp · date: 2025.10
- Paper(s): [Paper](https://arxiv.org/abs/2510.15339)
- Algorithm: GRPO (via VeRL) · Framework: Custom · Agent: Single · Turns: Multi · Tools: Yes (Graph retrieval)
- Reward phase: Outcome · Reward type: Rule
- Task: KG Construction for QA

### WebSeer
- `https://github.com/99hgz/WebSeer` · org: Individual · date: 2025.10
- Paper(s): [Paper](https://arxiv.org/abs/2510.18798)
- Algorithm: GRPO-style · Framework: veRL · Agent: Single · Turns: Multi · Tools: Yes (Search)
- Reward phase: Outcome · Reward type: Rule/Model
- Task: Web Search QA (w/ self-reflection)

### HiPRAG
- `https://github.com/qualidea1217/HiPRAG` · org: Individual · date: 2025.10
- Paper(s): [Paper](https://arxiv.org/abs/2510.07794)
- Algorithm: PPO · Framework: veRL · Agent: Single · Turns: Multi · Tools: Yes (Retrieval)
- Reward phase: Process · Reward type: Model/Rule
- Task: Efficient Agentic RAG

### Tree-GRPO
- `https://github.com/AMAP-ML/Tree-GRPO` · org: AMAP · date: 2025.9
- Paper(s): [Paper](https://arxiv.org/abs/2509.21240)
- Algorithm: GRPO/Tree-GRPO · Framework: veRL · Agent: Single · Turns: Multi · Tools: Search
- Reward phase: Outcome · Reward type: Rule
- Task: Search

### DeepResearch
- `https://github.com/Alibaba-NLP/DeepResearch` · org: Alibaba/Tongyi Lab · date: 2025.10
- Paper(s): [Paper](https://arxiv.org/abs/2510.24701)
- Algorithm: RL-based · Framework: Custom · Agent: Single · Turns: Multi · Tools: Yes (Search, Browse)
- Reward phase: Outcome · Reward type: Model
- Task: Deep Research

### DeepDive
- `https://github.com/THUDM/DeepDive` · org: Tsinghua/THUDM · date: 2025.9
- Paper(s): [Paper](https://arxiv.org/abs/2509.10446)
- Algorithm: GRPO · Framework: Custom · Agent: Single · Turns: Multi · Tools: Yes (KG + Search)
- Reward phase: Outcome · Reward type: Rule
- Task: KG-augmented Search

### ASearcher
- `https://github.com/inclusionAI/ASearcher` · org: Ant Research RL Lab  /  Tsinghua University & UW · date: 2025.8
- Paper(s): [Paper](https://arxiv.org/abs/2508.07976)
- Algorithm: PPO/GRPO + Decoupled PPO · Framework: RealHF/AReaL · Agent: Single · Turns: Multi · Tools: Yes
- Reward phase: Outcome · Reward type: External/Rule
- Task: Math/Code/SearchQA

### SSRL
- `https://github.com/TsinghuaC3I/SSRL` · org: Tsinghua · date: 2025.8
- Paper(s): [Paper](https://arxiv.org/abs/2508.10874)
- Algorithm: GRPO · Framework: Custom · Agent: Single · Turns: Multi · Tools: Yes (Self-search)
- Reward phase: Outcome · Reward type: Rule
- Task: Self-Search

### Research-Venus
- `https://github.com/antgroup/Research-Venus` · org: Ant Group · date: 2025.8
- Paper(s): [Paper](https://arxiv.org/abs/2508.12800)
- Algorithm: GRPO · Framework: Custom · Agent: Single · Turns: Multi · Tools: Yes (Search)
- Reward phase: Both · Reward type: Model (atomic thought)
- Task: Deep Research

### Graph-R1
- `https://github.com/LHRLAB/Graph-R1` · org: BUPT/NTU/NUS · date: 2025.7
- Paper(s): [Paper](https://arxiv.org/abs/2507.21892)
- Algorithm: GRPO/REINFORCE++/PPO · Framework: veRL · Agent: Single · Turns: Multi · Tools: Yes (Graph retrieval)
- Reward phase: Outcome · Reward type: Rule (EM/F1)
- Task: KGQA

### Kimi-Researcher
- `https://github.com/moonshotai/Kimi-Researcher` · org: Moonshot AI · date: 2025.6
- Paper(s): [blog](https://moonshotai.github.io/Kimi-Researcher/)
- Algorithm: REINFORCE · Framework: Custom · Agent: Single · Turns: Multi · Tools: Search, Browse, Coding
- Reward phase: Outcome · Reward type: Outcome
- Task: Research

### R-Search
- `https://github.com/QingFei1/R-Search` · org: Individual · date: 2025.6
- Paper(s): —
- Algorithm: PPO/GRPO · Framework: veRL · Agent: Single · Turns: Multi · Tools: Yes
- Reward phase: Both · Reward type: All
- Task: QA/Search

### R1-Searcher-plus
- `https://github.com/RUCAIBox/R1-Searcher-plus` · org: RUC · date: 2025.5
- Paper(s): [Paper](https://arxiv.org/abs/2505.17005)
- Algorithm: Custom · Framework: Custom · Agent: Single · Turns: Multi · Tools: Search
- Reward phase: Outcome · Reward type: Model
- Task: Search

### StepSearch
- `https://github.com/Zillwang/StepSearch` · org: SenseTime · date: 2025.5
- Paper(s): [Paper](https://arxiv.org/abs/2505.15107)
- Algorithm: PPO · Framework: veRL · Agent: Single · Turns: Multi · Tools: Search
- Reward phase: Process · Reward type: Model
- Task: QA

### AutoRefine
- `https://github.com/syr-cn/AutoRefine` · org: USTC · date: 2025.5
- Paper(s): [Paper](https://www.arxiv.org/abs/2505.11277)
- Algorithm: PPO/GRPO · Framework: veRL · Agent: Multi · Turns: Multi · Tools: Search
- Reward phase: Both · Reward type: Rule
- Task: RAG QA

### ZeroSearch
- `https://github.com/Alibaba-NLP/ZeroSearch` · org: Alibaba · date: 2025.5
- Paper(s): [Paper](https://arxiv.org/abs/2505.04588)
- Algorithm: PPO/GRPO/REINFORCE · Framework: veRL · Agent: Single · Turns: Multi · Tools: Yes
- Reward phase: Outcome · Reward type: Rule
- Task: QA/Search

### ReasonRAG
- `https://github.com/wlzhang2020/ReasonRAG` · org: CityU HK / Huawei · date: 2025.5
- Paper(s): [Paper](https://arxiv.org/abs/2505.14069)
- Algorithm: DPO + MCTS-based PRM · Framework: Custom · Agent: Single · Turns: Multi · Tools: Yes (Wikipedia search)
- Reward phase: Process · Reward type: Model (PRM)
- Task: Multi-hop QA

### VRAG
- `https://github.com/Alibaba-NLP/VRAG` · org: USTC / Tongyi Lab, Alibaba · date: 2025.5
- Paper(s): [Paper](https://arxiv.org/abs/2505.22019)
- Algorithm: GRPO · Framework: veRL · Agent: Single · Turns: Multi · Tools: Yes (Visual retrieval)
- Reward phase: Both · Reward type: Rule/Model
- Task: Visually-rich RAG

### MaskSearch
- `https://github.com/Alibaba-NLP/MaskSearch` · org: Tongyi Lab, Alibaba · date: 2025.5
- Paper(s): [Paper](https://arxiv.org/abs/2505.20285)
- Algorithm: DAPO · Framework: DAPO / veRL · Agent: Single · Turns: Multi · Tools: Yes (Search)
- Reward phase: Outcome · Reward type: Rule/Model
- Task: RAMP Pretraining + QA

### R3-RAG
- `https://github.com/Yuan-Li-FNLP/R3-RAG` · org: Fudan NLP · date: 2025.5
- Paper(s): [Paper](https://arxiv.org/abs/2505.23794)
- Algorithm: PPO · Framework: OpenRLHF · Agent: Single · Turns: Multi · Tools: Yes (Retrieval)
- Reward phase: Both · Reward type: Rule
- Task: Multi-hop QA

### O2-Searcher
- `https://github.com/KnowledgeXLab/O2-Searcher` · org: KnowledgeXLab · date: 2025.5
- Paper(s): [Paper](https://arxiv.org/abs/2505.16582)
- Algorithm: GRPO · Framework: veRL · Agent: Single · Turns: Multi · Tools: Yes (Search)
- Reward phase: Outcome · Reward type: Rule/Model
- Task: Open-ended QA

### s3
- `https://github.com/pat-jj/s3` · org: UIUC · date: 2025.5
- Paper(s): [Paper](https://arxiv.org/abs/2505.14146)
- Algorithm: GRPO · Framework: veRL · Agent: Single · Turns: Multi · Tools: Yes (Retrieval)
- Reward phase: Outcome · Reward type: Model (Gain-Beyond-RAG)
- Task: RAG / Medical QA

### knowledge-r1
- `https://github.com/hzy312/knowledge-r1` · org: CAS / UCAS · date: 2025.5
- Paper(s): [Paper](https://arxiv.org/abs/2505.07596)
- Algorithm: GRPO · Framework: veRL · Agent: Single · Turns: Multi · Tools: Yes (Retrieval)
- Reward phase: Outcome · Reward type: Rule
- Task: Knowledge-intensive QA (KB-aware)

### WebThinker
- `https://github.com/RUC-NLPIR/WebThinker` · org: RUC · date: 2025.4
- Paper(s): [Paper](https://arxiv.org/abs/2504.21776)
- Algorithm: DPO · Framework: Custom · Agent: Single · Turns: Multi · Tools: Web Browsing
- Reward phase: Outcome · Reward type: Model/External
- Task: Reasoning/QA/Research

### DeepResearcher
- `https://github.com/GAIR-NLP/DeepResearcher` · org: SJTU · date: 2025.4
- Paper(s): [Paper](https://arxiv.org/abs/2504.03160)
- Algorithm: PPO/GRPO · Framework: veRL · Agent: Multi · Turns: Multi · Tools: Yes
- Reward phase: Outcome · Reward type: All
- Task: Research

### Search-R1
- `https://github.com/PeterGriffinJin/Search-R1` · org: UIUC/Google · date: 2025.3
- Paper(s): [paper1](https://arxiv.org/abs/2503.09516), [paper2](https://arxiv.org/abs/2505.15117)
- Algorithm: PPO/GRPO · Framework: veRL · Agent: Single · Turns: Multi · Tools: Search
- Reward phase: Outcome · Reward type: All
- Task: Search

### R1-Searcher
- `https://github.com/RUCAIBox/R1-Searcher` · org: RUC · date: 2025.3
- Paper(s): [Paper](https://arxiv.org/abs/2503.05592)
- Algorithm: PPO/DPO · Framework: OpenRLHF · Agent: Single · Turns: Multi · Tools: Yes
- Reward phase: Both · Reward type: All
- Task: Search

### C-3PO
- `https://github.com/Chen-GX/C-3PO` · org: Alibaba · date: 2025.2
- Paper(s): [Paper](https://arxiv.org/abs/2502.06205)
- Algorithm: PPO · Framework: OpenRLHF · Agent: Multi · Turns: Multi · Tools: Yes
- Reward phase: Outcome · Reward type: Model
- Task: Search

### DeepRetrieval
- `https://github.com/pat-jj/DeepRetrieval` · org: UIUC · date: 2025.3
- Paper(s): [Paper](https://arxiv.org/abs/2503.00223)
- Algorithm: GRPO · Framework: veRL · Agent: Single · Turns: Multi · Tools: Yes (Search)
- Reward phase: Outcome · Reward type: Rule
- Task: Query Generation/IR
