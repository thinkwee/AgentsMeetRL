# Domain-Specific Agents

Specialized verticals: medical, legal, finance, OS tuning. Reward usually mixes domain rules + LLM-judge.

_Total: 9 entries._

### MedSAM-Agent
- `https://github.com/CUHK-AIM-Group/MedSAM-Agent` · org: CUHK/Tencent · date: 2026.2
- Paper(s): [Paper](https://arxiv.org/abs/2602.03320)
- Algorithm: GRPO (via veRL) · Framework: Custom · Agent: Single · Turns: Multi · Tools: Yes (SAM/MedSAM2)
- Reward phase: Both · Reward type: Model (clinical fidelity)
- Task: Medical Image Segmentation
- Domain: Medical

### Doctor-R1
- `https://github.com/thu-unicorn/Doctor-R1` · org: Tsinghua (thu-unicorn) · date: 2025.10
- Paper(s): [Paper](https://arxiv.org/abs/2510.04284)
- Algorithm: Experiential Agentic RL · Framework: veRL · Agent: Multi · Turns: Multi · Tools: No
- Reward phase: Both · Reward type: Model + Rule + safety veto
- Task: Clinical inquiry & diagnosis
- Domain: Medical

### Alpha-R1
- `https://github.com/FinStep-AI/Alpha-R1` · org: SJTU / FinStep.AI / StepFun · date: 2025.12
- Paper(s): [Paper](https://arxiv.org/abs/2512.23515)
- Algorithm: GRPO · Framework: Custom · Agent: Single · Turns: Multi · Tools: Yes
- Reward phase: Outcome · Reward type: External (portfolio returns) + Model
- Task: Alpha factor screening (with real-time news)
- Domain: Financial

### OS-R1
- `https://github.com/LHY-24/OS-R1` · org: ISCAS · date: 2025.8
- Paper(s): [Paper](https://arxiv.org/abs/2508.12551)
- Algorithm: GRPO (via veRL) · Framework: Custom · Agent: Single · Turns: Multi · Tools: Yes (LightRAG, kernel config)
- Reward phase: Outcome · Reward type: Rule
- Task: Linux Kernel Tuning
- Domain: OS/Systems

### MMedAgent-RL
- code: pending · org: Unknown · date: 2025.6
- Paper(s): [paper](https://arxiv.org/abs/2506.00555)
- Algorithm: Unknown · Framework: Unknown · Agent: Multi · Turns: Unknown · Tools: Unknown
- Reward phase: Unknown · Reward type: Unknown
- Task: Unknown
- Domain: Medical

### MedResearcher-R1
- `https://github.com/AQ-MedAI/MedResearcher-R1` · org: Ant Group (AQ-MedAI) · date: 2025.8
- Paper(s): [Paper](https://arxiv.org/abs/2508.14880)
- Algorithm: GRPO-based (SFT + Online RL) · Framework: Custom · Agent: Single · Turns: Multi · Tools: Yes (Search/KG)
- Reward phase: Outcome · Reward type: Rule + Model
- Task: Medical Deep Research (MedBrowseComp)
- Domain: Medical

### LegalDelta
- `https://github.com/NEUIR/LegalDelta` · org: Northeastern University (NEUIR) · date: 2025.8
- Paper(s): [Paper](https://arxiv.org/abs/2508.12281)
- Algorithm: GRPO (CoT-guided info-gain) · Framework: Custom · Agent: Single · Turns: Multi · Tools: No
- Reward phase: Process · Reward type: Model + Rule
- Task: Legal Reasoning
- Domain: Legal

### DoctorAgent-RL
- `https://github.com/JarvisUSTC/DoctorAgent-RL` · org: UCAS/CAS/USTC · date: 2025.5
- Paper(s): [Paper](https://arxiv.org/abs/2505.19630)
- Algorithm: GRPO · Framework: RAGEN · Agent: Multi · Turns: Multi · Tools: No
- Reward phase: Both · Reward type: Model/Rule
- Task: Consultation/Diagnosis
- Domain: Medical

### Biomni
- `https://github.com/snap-stanford/Biomni` · org: Stanford University (SNAP) · date: 2025.3
- Paper(s): [Paper](https://www.biorxiv.org/content/10.1101/2025.05.30.656746v1)
- Algorithm: TBD · Framework: Custom · Agent: Single · Turns: Single · Tools: Yes
- Reward phase: TBD · Reward type: TBD
- Task: scRNAseq/CRISPR/ADMET/Knowledge
- Domain: Biomedical
