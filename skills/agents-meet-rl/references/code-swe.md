# Code & SWE Agents

Software-engineering agents that locate, repair, and test. Most use SWE-bench-style verifiable rewards.

_Total: 24 entries._

## Contents

FastContext, SWE-Edit, CodeScout, CUDA-Agent, SWE-World, CUDA-L2, PPP-Agent, DeepAnalyze, RepoDeepSearch, CUDA-L1, digitalhuman, SWE-Swiss, MedAgentGym, CURE, Time-R1, ML-Agent, R1-Code-Interpreter, Skywork-OR1, sweet_rl, swe-rl, CTRL, AceCoder, rllm, open-r1.

### FastContext
- **Idea:** Trains a small parallel-tool-calling repository-explorer subagent so a coding agent gets focused file/line context cheaply via task-grounded RL.
- `https://github.com/microsoft/fastcontext` · org: Microsoft · date: 2026.6
- Paper(s): [Paper](https://arxiv.org/abs/2606.14066)
- Algorithm: Task-grounded RL · Framework: Custom · Agent: Single · Turns: Multi · Tools: Yes (Read/Glob/Grep, parallel)
- Reward phase: Outcome · Reward type: Rule-Based
- Task: Repo-explorer subagent (context gathering + citations)

### SWE-Edit
- **Idea:** Decomposes code editing into Viewer and Editor subagents and trains the editor to adaptively pick edit mode rather than always using find-and-replace.
- `https://github.com/microsoft/SWE-Edit` · org: Microsoft Research · date: 2026.4
- Paper(s): [Paper](https://arxiv.org/abs/2604.26102)
- Algorithm: GRPO (adaptive mode selection) · Framework: Custom · Agent: Multi (Viewer + Editor subagents) · Turns: Multi · Tools: Yes (bash, file ops, viewer subagent)
- Reward phase: Outcome · Reward type: Rule/External (test-based)
- Task: SWE-bench Verified (find-replace vs whole-file rewrite)

### CodeScout
- **Idea:** RL recipe for code-search agents using a multi-level (file/module/function) F1 reward over a plain Unix terminal toolset.
- `https://github.com/OpenHands/codescout` · org: OpenHands · date: 2026.3
- Paper(s): [Paper](https://arxiv.org/abs/2603.17829)
- Algorithm: GSPO · Framework: SkyRL · Agent: Single · Turns: Multi · Tools: Yes (terminal: rg/sed/cat)
- Reward phase: Outcome · Reward type: Rule-Based (F1)
- Task: Repo-level code search/localization (terminal)

### CUDA-Agent
- **Idea:** Large-scale agentic RL for CUDA kernels combining data synthesis, a skill-augmented dev environment with automated verification/profiling rewards, and stable-training techniques.
- `https://github.com/BytedTsinghua-SIA/CUDA-Agent` · org: ByteDance/Tsinghua · date: 2026.2
- Paper(s): [Paper](https://arxiv.org/abs/2602.24286)
- Algorithm: Agentic RL (staged) · Framework: Custom · Agent: Single · Turns: Multi · Tools: Yes (compile/verify/profile)
- Reward phase: Outcome · Reward type: Rule (correctness + performance)
- Task: CUDA Kernel Generation

### SWE-World
- **Idea:** Docker-free SWE RL: a learned world model predicts execution outcomes and test feedback, enabling cheap rollouts and test-time trajectory selection.
- `https://github.com/RUCAIBox/SWE-World` · org: RUC (RUCAIBox) · date: 2026.2
- Paper(s): [Paper](https://arxiv.org/abs/2602.03419)
- Algorithm: RL with learned world model (SWT + SWR) · Framework: OpenRLHF + veRL · Agent: Single · Turns: Multi · Tools: Yes
- Reward phase: Both · Reward type: Model (surrogate) + Rule
- Task: Docker-free SWE (SWE-Bench Verified)

### CUDA-L2
- **Idea:** Contrastive RL with CUDA execution speed as reward optimizes HGEMM matmul kernels, beating cuBLAS by 19.2% via large-scale config exploration.
- `https://github.com/deepreinforce-ai/CUDA-L2` · org: DeepReinforce AI · date: 2025.12
- Paper(s): [Paper](https://arxiv.org/abs/2512.02551)
- Algorithm: Contrastive RL · Framework: Custom · Agent: Single · Turns: Single · Tools: Yes (compile/benchmark)
- Reward phase: Outcome · Reward type: Rule (TFLOPs)
- Task: HGEMM / CUDA Matmul

### PPP-Agent
- **Idea:** Multi-objective RL (PPP) jointly optimizing productivity, proactivity, and personalization, evaluated in the UserVille simulator with configurable LLM user simulators.
- `https://github.com/sunnweiwei/PPP-Agent` · org: CMU/OpenHands · date: 2025.11
- Paper(s): [Paper](https://arxiv.org/abs/2511.02208)
- Algorithm: PPP-RL · Framework: veRL · Agent: Single · Turns: Multi · Tools: Search, Ask, Browse
- Reward phase: Both · Reward type: Rule+Model
- Task: SWE/Research

### DeepAnalyze
- **Idea:** Curriculum-based agentic RL plus data-grounded trajectory synthesis trains an 8B model for end-to-end autonomous data science without fixed workflows.
- `https://github.com/ruc-datalab/DeepAnalyze` · org: RUC/Tsinghua · date: 2025.10
- Paper(s): [Paper](https://arxiv.org/abs/2510.16872)
- Algorithm: Curriculum RL · Framework: Custom · Agent: Single · Turns: Multi · Tools: Yes (Code exec)
- Reward phase: Outcome · Reward type: Rule/External
- Task: Data Science

### RepoDeepSearch
- **Idea:** ToolTrain: rejection-sampled SFT plus tool-integrated RL teaches LLMs to navigate repository retrieval tools across multi-step reasoning for bug localization.
- `https://github.com/Mizersy/RepoDeepSearch` · org: PKU, Bytedance, BIT · date: 2025.8
- Paper(s): [Paper](https://arxiv.org/abs/2508.03012)
- Algorithm: GRPO · Framework: veRL · Agent: Single · Turns: Multi · Tools: Yes
- Reward phase: Both · Reward type: Rule/External
- Task: Search/Repair

### CUDA-L1
- **Idea:** Contrastive RL using execution speedup as the only reward turns a weak LLM into a CUDA optimizer that combines and rejects optimizations.
- `https://github.com/deepreinforce-ai/CUDA-L1` · org: DeepReinforce AI · date: 2025.7
- Paper(s): [Paper](https://arxiv.org/abs/2507.14111)
- Algorithm: Contrastive RL · Framework: Custom · Agent: Single · Turns: Single · Tools: No
- Reward phase: Outcome · Reward type: Rule (performance)
- Task: CUDA Optimization

### digitalhuman
- **Idea:** RLVER: PPO with deterministic emotion scores from self-consistent simulated users as verifiable rewards to train empathetic dialogue agents.
- `https://github.com/Tencent/digitalhuman` · org: Tencent · date: 2025.7
- Paper(s): [Paper](https://arxiv.org/abs/2507.03112)
- Algorithm: PPO/GRPO/ReMax/RLOO · Framework: veRL · Agent: Multi · Turns: Multi · Tools: Yes
- Reward phase: Outcome · Reward type: Rule/Model/External
- Task: Empathy/Math/Code/MultimodalQA

### SWE-Swiss
- **Idea:** Decomposes issue resolution into localization/repair/unit-test skills, trained via multi-task SFT then two-stage RL on repair, plus similarity-based selection.
- `https://github.com/zhenyuhe00/SWE-Swiss` · org: Tsinghua / ByteDance · date: 2025.7
- Paper(s): —
- Algorithm: Two-stage RL curriculum · Framework: veRL · Agent: Single · Turns: Multi · Tools: Yes
- Reward phase: Outcome · Reward type: Rule (test-based)
- Task: SWE (Localization/Repair/Unit-Test)

### MedAgentGym
- **Idea:** Scalable sandboxed environment of 72K biomedical coding tasks with verifiable feedback for multi-turn trajectory sampling and offline/online RL.
- `https://github.com/wshi83/MedAgentGym` · org: Emory/Georgia Tech · date: 2025.6
- Paper(s): [Paper](https://arxiv.org/abs/2506.04405)
- Algorithm: SFT/DPO/PPO/GRPO · Framework: Hugginface · Agent: Single · Turns: Multi · Tools: Yes
- Reward phase: Outcome · Reward type: External
- Task: Medical/Code

### CURE
- **Idea:** Co-evolves a code generator and a unit-test generator via RL with no ground-truth code; the tester learns from the coder's mistakes.
- `https://github.com/Gen-Verse/CURE` · org: University of Chicago  /  Princeton/ByteDance · date: 2025.6
- Paper(s): [Paper](https://arxiv.org/abs/2506.03136)
- Algorithm: PPO · Framework: Huggingface · Agent: Single · Turns: Single · Tools: No
- Reward phase: Outcome · Reward type: External
- Task: Code

### Time-R1
- **Idea:** Three-stage RL curriculum with a dynamic rule-based reward builds temporal understanding then future prediction, letting a 3B model beat far larger ones.
- `https://github.com/ulab-uiuc/Time-R1` · org: UIUC · date: 2025.5
- Paper(s): [Paper](https://arxiv.org/abs/2505.13508)
- Algorithm: PPO/GRPO/DPO · Framework: veRL · Agent: Multi · Turns: Multi · Tools: Code
- Reward phase: Outcome · Reward type: All
- Task: Temporal

### ML-Agent
- **Idea:** Online RL for ML-engineering agents using exploration-enriched SFT, step-wise (per-action) RL, and a unified reward unifying heterogeneous ML signals.
- `https://github.com/MASWorks/ML-Agent` · org: MASWorks · date: 2025.5
- Paper(s): [Paper](https://arxiv.org/abs/2505.23723)
- Algorithm: Custom · Framework: Custom · Agent: Single · Turns: Multi · Tools: Yes
- Reward phase: Process · Reward type: All
- Task: Code

### R1-Code-Interpreter
- **Idea:** Multi-stage RL curriculum partitioning samples by improvement potential teaches LLMs to autonomously emit code queries during reasoning.
- `https://github.com/yongchao98/R1-Code-Interpreter` · org: MIT · date: 2025.5
- Paper(s): [Paper](https://arxiv.org/abs/2505.21668)
- Algorithm: GRPO · Framework: Custom · Agent: Single · Turns: Multi · Tools: Yes (Code exec)
- Reward phase: Outcome · Reward type: Rule/External
- Task: Code Interpretation

### Skywork-OR1
- **Idea:** Scalable long-CoT RL on R1-Distill models whose key lesson is mitigating premature entropy collapse to sustain exploration and test accuracy.
- `https://github.com/SkyworkAI/Skywork-OR1` · org: Skywork AI · date: 2025.5
- Paper(s): [Paper](https://arxiv.org/abs/2505.22312)
- Algorithm: Large-scale rule-based RL (GRPO variant) · Framework: Custom (veRL fork) · Agent: Single · Turns: Single · Tools: No
- Reward phase: Outcome · Reward type: Rule (verifiable)
- Task: Math + Code (AIME/LiveCodeBench)

### sweet_rl
- **Idea:** SWEET-RL solves multi-turn credit assignment by training a critic with privileged training-time info to give step-level rewards for the policy.
- `https://github.com/facebookresearch/sweet_rl` · org: Meta/UCB · date: 2025.3
- Paper(s): [Paper](https://arxiv.org/abs/2503.15478)
- Algorithm: DPO · Framework: OpenRLHF · Agent: Multi · Turns: Multi · Tools: Web Browsing
- Reward phase: Process · Reward type: Model
- Task: Design/Code

### swe-rl
- **Idea:** RL on open-source software-evolution data with a lightweight rule-based similarity reward to ground-truth PRs; skills generalize beyond SWE.
- `https://github.com/facebookresearch/swe-rl` · org: Meta/UIUC/CMU · date: 2025.2
- Paper(s): [Paper](https://arxiv.org/abs/2502.18449)
- Algorithm: RL-based · Framework: Custom · Agent: Single · Turns: Single · Tools: No
- Reward phase: Outcome · Reward type: Rule (similarity)
- Task: SWE (SWE-bench)

### CTRL
- **Idea:** Trains a critic via RL to generate feedback maximizing a fixed generator's code-correction performance, with no human-labeled critiques.
- `https://github.com/HKUNLP/critic-rl` · org: HKU/ByteDance · date: 2025.2
- Paper(s): [Paper](https://arxiv.org/abs/2502.03492)
- Algorithm: RL (critique-revision) · Framework: Custom · Agent: Single · Turns: Multi · Tools: Yes (Code exec)
- Reward phase: Process · Reward type: Model
- Task: Code Refinement

### AceCoder
- **Idea:** Auto-synthesized (question, test-case) pairs supply verifiable pass-rate rewards for code RL, removing the need for hand-labeled reward data.
- `https://github.com/TIGER-AI-Lab/AceCoder` · org: Waterloo (TIGER-Lab) · date: 2025.2
- Paper(s): [Paper](https://arxiv.org/abs/2502.01718)
- Algorithm: GRPO · Framework: Custom · Agent: Single · Turns: Single · Tools: Yes
- Reward phase: Outcome · Reward type: External (test cases)
- Task: Code Generation

### rllm
- **Idea:** Framework (verl fork) for post-training custom language agents and environments with RL; recipes for DeepSWE, DeepCoder, DeepScaleR.
- `https://github.com/agentica-project/rllm` · org: Berkeley Sky Computing Lab  /  BAIR / Together AI · date: 2025.1
- Paper(s): [Notion Blog](https://pretty-radio-b75.notion.site/rLLM-A-Framework-for-Post-Training-Language-Agents-21b81902c146819db63cd98a54ba5f31)
- Algorithm: PPO/GRPO · Framework: veRL · Agent: Single · Turns: Multi · Tools: Yes
- Reward phase: Outcome · Reward type: External
- Task: Code Edit

### open-r1
- **Idea:** Fully open reproduction of DeepSeek-R1: GRPO plus distillation/R1-Zero pipeline with code-execution sandboxes as verifiable reward signals.
- `https://github.com/huggingface/open-r1` · org: HuggingFace · date: 2025.1
- Paper(s): —
- Algorithm: GRPO · Framework: TRL · Agent: Single · Turns: Single · Tools: Yes
- Reward phase: Outcome · Reward type: All
- Task: Math/Code
