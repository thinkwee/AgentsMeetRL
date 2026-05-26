# Code & SWE Agents

Software-engineering agents that locate, repair, and test. Most use SWE-bench-style verifiable rewards.

_Total: 22 entries._

## Contents

SWE-Edit, CUDA-Agent, SWE-World, CUDA-L2, PPP-Agent, DeepAnalyze, RepoDeepSearch, CUDA-L1, SWE-Swiss, MedAgentGym, CURE, Time-R1, ML-Agent, R1-Code-Interpreter, digitalhuman, Skywork-OR1, sweet_rl, swe-rl, CTRL, AceCoder, rllm, open-r1.

### SWE-Edit
- `https://github.com/microsoft/SWE-Edit` · org: Microsoft Research · date: 2026.4
- Paper(s): [Paper](https://arxiv.org/abs/2604.26102)
- Algorithm: GRPO (adaptive mode selection) · Framework: Custom · Agent: Multi (Viewer + Editor subagents) · Turns: Multi · Tools: Yes (bash, file ops, viewer subagent)
- Reward phase: Outcome · Reward type: Rule/External (test-based)
- Task: SWE-bench Verified (find-replace vs whole-file rewrite)

### CUDA-Agent
- `https://github.com/BytedTsinghua-SIA/CUDA-Agent` · org: ByteDance/Tsinghua · date: 2026.2
- Paper(s): [Paper](https://arxiv.org/abs/2602.24286)
- Algorithm: Agentic RL (staged) · Framework: Custom · Agent: Single · Turns: Multi · Tools: Yes (compile/verify/profile)
- Reward phase: Outcome · Reward type: Rule (correctness + performance)
- Task: CUDA Kernel Generation

### SWE-World
- `https://github.com/RUCAIBox/SWE-World` · org: RUC (RUCAIBox) · date: 2026.2
- Paper(s): [Paper](https://arxiv.org/abs/2602.03419)
- Algorithm: RL with learned world model (SWT + SWR) · Framework: OpenRLHF + veRL · Agent: Single · Turns: Multi · Tools: Yes
- Reward phase: Both · Reward type: Model (surrogate) + Rule
- Task: Docker-free SWE (SWE-Bench Verified)

### CUDA-L2
- `https://github.com/deepreinforce-ai/CUDA-L2` · org: DeepReinforce AI · date: 2025.12
- Paper(s): [Paper](https://arxiv.org/abs/2512.02551)
- Algorithm: Contrastive RL · Framework: Custom · Agent: Single · Turns: Single · Tools: Yes (compile/benchmark)
- Reward phase: Outcome · Reward type: Rule (TFLOPs)
- Task: HGEMM / CUDA Matmul

### PPP-Agent
- `https://github.com/sunnweiwei/PPP-Agent` · org: CMU/OpenHands · date: 2025.11
- Paper(s): [Paper](https://arxiv.org/abs/2511.02208)
- Algorithm: PPP-RL · Framework: veRL · Agent: Single · Turns: Multi · Tools: Search, Ask, Browse
- Reward phase: Both · Reward type: Rule+Model
- Task: SWE/Research

### DeepAnalyze
- `https://github.com/ruc-datalab/DeepAnalyze` · org: RUC/Tsinghua · date: 2025.10
- Paper(s): [Paper](https://arxiv.org/abs/2510.16872)
- Algorithm: Curriculum RL · Framework: Custom · Agent: Single · Turns: Multi · Tools: Yes (Code exec)
- Reward phase: Outcome · Reward type: Rule/External
- Task: Data Science

### RepoDeepSearch
- `https://github.com/Mizersy/RepoDeepSearch` · org: PKU, Bytedance, BIT · date: 2025.8
- Paper(s): [Paper](https://arxiv.org/abs/2508.03012)
- Algorithm: GRPO · Framework: veRL · Agent: Single · Turns: Multi · Tools: Yes
- Reward phase: Both · Reward type: Rule/External
- Task: Search/Repair

### CUDA-L1
- `https://github.com/deepreinforce-ai/CUDA-L1` · org: DeepReinforce AI · date: 2025.7
- Paper(s): [Paper](https://arxiv.org/abs/2507.14111)
- Algorithm: Contrastive RL · Framework: Custom · Agent: Single · Turns: Single · Tools: No
- Reward phase: Outcome · Reward type: Rule (performance)
- Task: CUDA Optimization

### SWE-Swiss
- `https://github.com/zhenyuhe00/SWE-Swiss` · org: Tsinghua / ByteDance · date: 2025.7
- Paper(s): —
- Algorithm: Two-stage RL curriculum · Framework: veRL · Agent: Single · Turns: Multi · Tools: Yes
- Reward phase: Outcome · Reward type: Rule (test-based)
- Task: SWE (Localization/Repair/Unit-Test)

### MedAgentGym
- `https://github.com/wshi83/MedAgentGym` · org: Emory/Georgia Tech · date: 2025.6
- Paper(s): [Paper](https://arxiv.org/abs/2506.04405)
- Algorithm: SFT/DPO/PPO/GRPO · Framework: Hugginface · Agent: Single · Turns: Multi · Tools: Yes
- Reward phase: Outcome · Reward type: External
- Task: Medical/Code

### CURE
- `https://github.com/Gen-Verse/CURE` · org: University of Chicago  /  Princeton/ByteDance · date: 2025.6
- Paper(s): [Paper](https://arxiv.org/abs/2506.03136)
- Algorithm: PPO · Framework: Huggingface · Agent: Single · Turns: Single · Tools: No
- Reward phase: Outcome · Reward type: External
- Task: Code

### Time-R1
- `https://github.com/ulab-uiuc/Time-R1` · org: UIUC · date: 2025.5
- Paper(s): [Paper](https://arxiv.org/abs/2505.13508)
- Algorithm: PPO/GRPO/DPO · Framework: veRL · Agent: Multi · Turns: Multi · Tools: Code
- Reward phase: Outcome · Reward type: All
- Task: Temporal

### ML-Agent
- `https://github.com/MASWorks/ML-Agent` · org: MASWorks · date: 2025.5
- Paper(s): [Paper](https://arxiv.org/abs/2505.23723)
- Algorithm: Custom · Framework: Custom · Agent: Single · Turns: Multi · Tools: Yes
- Reward phase: Process · Reward type: All
- Task: Code

### R1-Code-Interpreter
- `https://github.com/yongchao98/R1-Code-Interpreter` · org: MIT · date: 2025.5
- Paper(s): [Paper](https://arxiv.org/abs/2505.21668)
- Algorithm: GRPO · Framework: Custom · Agent: Single · Turns: Multi · Tools: Yes (Code exec)
- Reward phase: Outcome · Reward type: Rule/External
- Task: Code Interpretation

### digitalhuman
- `https://github.com/Tencent/digitalhuman` · org: Tencent · date: 2025.7
- Paper(s): [Paper](https://arxiv.org/abs/2507.03112)
- Algorithm: PPO/GRPO/ReMax/RLOO · Framework: veRL · Agent: Multi · Turns: Multi · Tools: Yes
- Reward phase: Outcome · Reward type: Rule/Model/External
- Task: Empathy/Math/Code/MultimodalQA

### Skywork-OR1
- `https://github.com/SkyworkAI/Skywork-OR1` · org: Skywork AI · date: 2025.5
- Paper(s): [Paper](https://arxiv.org/abs/2505.22312)
- Algorithm: Large-scale rule-based RL (GRPO variant) · Framework: Custom (veRL fork) · Agent: Single · Turns: Single · Tools: No
- Reward phase: Outcome · Reward type: Rule (verifiable)
- Task: Math + Code (AIME/LiveCodeBench)

### sweet_rl
- `https://github.com/facebookresearch/sweet_rl` · org: Meta/UCB · date: 2025.3
- Paper(s): [Paper](https://arxiv.org/abs/2503.15478)
- Algorithm: DPO · Framework: OpenRLHF · Agent: Multi · Turns: Multi · Tools: Web Browsing
- Reward phase: Process · Reward type: Model
- Task: Design/Code

### swe-rl
- `https://github.com/facebookresearch/swe-rl` · org: Meta/UIUC/CMU · date: 2025.2
- Paper(s): [Paper](https://arxiv.org/abs/2502.18449)
- Algorithm: RL-based · Framework: Custom · Agent: Single · Turns: Single · Tools: No
- Reward phase: Outcome · Reward type: Rule (similarity)
- Task: SWE (SWE-bench)

### CTRL
- `https://github.com/HKUNLP/critic-rl` · org: HKU/ByteDance · date: 2025.2
- Paper(s): [Paper](https://arxiv.org/abs/2502.03492)
- Algorithm: RL (critique-revision) · Framework: Custom · Agent: Single · Turns: Multi · Tools: Yes (Code exec)
- Reward phase: Process · Reward type: Model
- Task: Code Refinement

### AceCoder
- `https://github.com/TIGER-AI-Lab/AceCoder` · org: Waterloo (TIGER-Lab) · date: 2025.2
- Paper(s): [Paper](https://arxiv.org/abs/2502.01718)
- Algorithm: GRPO · Framework: Custom · Agent: Single · Turns: Single · Tools: Yes
- Reward phase: Outcome · Reward type: External (test cases)
- Task: Code Generation

### rllm
- `https://github.com/agentica-project/rllm` · org: Berkeley Sky Computing Lab  /  BAIR / Together AI · date: 2025.1
- Paper(s): [Notion Blog](https://pretty-radio-b75.notion.site/rLLM-A-Framework-for-Post-Training-Language-Agents-21b81902c146819db63cd98a54ba5f31)
- Algorithm: PPO/GRPO · Framework: veRL · Agent: Single · Turns: Multi · Tools: Yes
- Reward phase: Outcome · Reward type: External
- Task: Code Edit

### open-r1
- `https://github.com/huggingface/open-r1` · org: HuggingFace · date: 2025.1
- Paper(s): —
- Algorithm: GRPO · Framework: TRL · Agent: Single · Turns: Single · Tools: Yes
- Reward phase: Outcome · Reward type: All
- Task: Math/Code
