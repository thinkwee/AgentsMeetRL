# Environments / Benchmarks / Gyms

Sandbox environments and benchmarks. Pick one matching your task before designing rewards.

_Total: 47 entries._

## Contents

AEnvironment, OpenSandbox, OpenEnv, open-trajectory-gym, NeMo-Gym, LoCoBench-Agent, Simia-Agent-Training, PaperArena, enterprise-deep-research, meta-agents-research-environments, BrowseComp-Plus, MCP-Bench, MCPVerse, CompassVerifier, tau2-bench, Mind2Web-2, MCP-Universe, gem, MLE-Dojo, R2E-Gym, SWE-smith, atropos, InternBootcamp, loong, DataSciBench, reasoning-gym, llmgym, SWE-Gym, debug-gym, gym-llm, AgentGym, tau-bench, appworld, android_world, TheAgentCompany, LlamaGym, visualwebarena, LMRL-Gym, OSWorld, webarena, AgentBench, WebShop, ScienceWorld, factorio-learning-environment, alfworld, jericho, TextWorld.

### AEnvironment
- **Idea:** 'Everything as Environment' abstraction extending MCP into one Environment API so tools, benchmarks, and multi-agent systems plug into RL training uniformly.
- `https://github.com/inclusionAI/AEnvironment` · org: Ant Group (inclusionAI) · date: 2026.5
- Paper(s): —
- Task: Agentic RL Env Platform (MCP, AReaL-integrated, TAU2/SWE/Terminal-Bench)

### OpenSandbox
- **Idea:** Multi-language sandbox platform with standardized lifecycle APIs over Docker/K8s for secure agent code execution in RL training and evaluation.
- `https://github.com/alibaba/OpenSandbox` · org: Alibaba · date: 2026.3
- Paper(s): —
- Task: Code/GUI/Agent Eval

### OpenEnv
- **Idea:** Gymnasium-style step()/reset()/state() standard for containerized agentic execution environments, removing per-env custom integration for RL.
- `https://github.com/meta-pytorch/OpenEnv` · org: Meta (PyTorch) · date: 2026.3
- Paper(s): —
- Task: Chess/Arcade/Finance

### open-trajectory-gym
- **Idea:** SFT->online RL->GEPA post-training pipeline on multi-turn tool-use trajectories for locally-deployable CTF/security agents, bring-your-own components.
- `https://github.com/westonbrown/open-trajectory-gym` · org: Individual · date: 2026.3
- Paper(s): —
- Task: CTF/Security

### NeMo-Gym
- **Idea:** Manages the full stateful agent system (data, harness, verifier, exec context) so evaluation, optimization, and RL share one reproducible pipeline at scale.
- `https://github.com/NVIDIA-NeMo/Gym` · org: NVIDIA · date: 2026.1
- Paper(s): —
- Task: Multi-step/Multi-turn

### LoCoBench-Agent
- **Idea:** Turns 8K static code scenarios into interactive multi-turn envs to test long-context (10K-1M tokens) SWE-agent behavior across languages.
- `https://github.com/SalesforceAIResearch/LoCoBench-Agent` · org: Salesforce AI Research · date: 2025.11
- Paper(s): —
- Task: SWE

### Simia-Agent-Training
- **Idea:** Uses reasoning models to simulate realistic environments, then trains tool-use agents via SFT and RL on those synthetic trajectories instead of real systems.
- `https://github.com/microsoft/Simia-Agent-Training` · org: Microsoft · date: 2025.10
- Paper(s): —
- Task: ToolUse/API

### PaperArena
- **Idea:** Benchmark for research questions needing cross-paper synthesis via orchestrated external tools (PDF parsing, retrieval, computation).
- `https://github.com/Melmaphother/PaperArena` · org: University of Science and Technology of China · date: 2025.9
- Paper(s): —
- Task: ScientificLiteratureQA

### enterprise-deep-research
- **Idea:** Multi-agent deep-research system combining adaptive query decomposition, specialized search agents, reflection, and human-in-the-loop steering.
- `https://github.com/SalesforceAIResearch/enterprise-deep-research` · org: Salesforce AI Research · date: 2025.9
- Paper(s): —
- Task: DeepResearch

### meta-agents-research-environments
- **Idea:** Gaia2 evaluation in evolving environments where new info and shifting conditions force agents to adapt strategies, adding temporal complexity to static benchmarks.
- `https://github.com/facebookresearch/meta-agents-research-environments` · org: Meta (FAIR) · date: 2025.9
- Paper(s): —
- Task: Gaia2 / Multi-universe

### BrowseComp-Plus
- **Idea:** Evaluates deep-research agents against a fixed ~100K human-verified corpus to control retrieval and isolate retriever-vs-LLM effects fairly.
- `https://github.com/texttron/BrowseComp-Plus` · org: University of Waterloo · date: 2025.8
- Paper(s): —
- Task: Deep Research Eval

### MCP-Bench
- **Idea:** Connects LLMs to 28 live MCP servers (250 tools) to test cross-domain orchestration, schema understanding, and fuzzy-instruction tool planning.
- `https://github.com/Accenture/mcp-bench` · org: Accenture · date: 2025.8
- Paper(s): [Paper](https://arxiv.org/abs/2508.20453)
- Task: MCP Tool-use (28 servers)

### MCPVerse
- **Idea:** Benchmark of 550+ executable real-world tools used simultaneously, an OS-like environment for testing agents in large tool spaces.
- `https://github.com/hailsham/mcpverse` · org: Individual · date: 2025.8
- Paper(s): —
- Task: MCP Tools (550+)

### CompassVerifier
- **Idea:** Verifier model classifying outputs as correct/incorrect/quality-problematic robustly across prompt formats, for consistent RL reward signals.
- `https://github.com/open-compass/CompassVerifier` · org: Shanghai AI Lab · date: 2025.7
- Paper(s): —
- Task: Reasoning

### tau2-bench
- **Idea:** Dual-control simulation where agent and simulated user both act, testing policy adherence and tool use in customer-service dialogues.
- `https://github.com/sierra-research/tau2-bench` · org: Sierra Research · date: 2025.6
- Paper(s): —
- Task: Tool-Agent-User

### Mind2Web-2
- **Idea:** Evaluates long-horizon agentic search with an Agent-as-a-Judge rubric scoring citation-backed synthesis of real-time information.
- `https://github.com/OSU-NLP-Group/Mind2Web-2` · org: Ohio State University · date: 2025.6
- Paper(s): —
- Task: Web

### MCP-Universe
- **Idea:** Benchmarks agents against real live MCP servers and unfamiliar tool spaces over multi-step tasks rather than simplified synthetic tool calls.
- `https://github.com/SalesforceAIResearch/MCP-Universe` · org: Salesforce AI Research · date: 2025.5
- Paper(s): —
- Task: MCP Tool-use

### gem
- **Idea:** Gym-style composable env API for LLM agents with async vectorization, tool integration (Python/search/MCP), and adapters to 6 RL frameworks.
- `https://github.com/axon-rl/gem` · org: Sea AI Lab · date: 2025.5
- Paper(s): —
- Task: Math/Code/Game/QA

### MLE-Dojo
- **Idea:** Gym-style sandbox over 200+ Kaggle ML-engineering tasks giving both final-outcome and intermediate-step rewards via a FeedbackManager for SFT/RL.
- `https://github.com/MLE-Dojo/MLE-Dojo` · org: GIT, Stanford · date: 2025.5
- Paper(s): —
- Task: MLE

### R2E-Gym
- **Idea:** SWE-GEN builds executable training envs from commits (not human PRs) plus hybrid exec/exec-free verifiers for scalable real-world SWE-agent RL.
- `https://github.com/R2E-Gym/R2E-Gym` · org: UC Berkeley/ANU · date: 2025.4
- Paper(s): —
- Task: SWE

### SWE-smith
- **Idea:** Toolkit that turns any GitHub repo into a SWE-gym, generating unlimited synthetic training tasks for SWE agents.
- `https://github.com/SWE-bench/SWE-smith` · org: Princeton/Stanford/SWE-bench · date: 2025.4
- Paper(s): —
- Task: SWE

### atropos
- **Idea:** Microservice framework for async LLM RL: envs run as decoupled services that tokenize/score rollouts into a shared trajectory API queue independent of trainers.
- `https://github.com/NousResearch/atropos` · org: Nous Research · date: 2025.4
- Paper(s): —
- Task: Game/Code/Tool

### InternBootcamp
- **Idea:** Evolutionarily auto-generated 1000+ verifiable reasoning tasks (case_generator/prompt_func/verify_func) showing task-count scaling boosts RL reasoning via cross-task transfer.
- `https://github.com/InternLM/InternBootcamp` · org: InternBootcamp · date: 2025.4
- Paper(s): —
- Task: Coding/QA/Game

### loong
- **Idea:** Self-bootstrapping RLVR loop (Generator/Verifier/Agent) over 8729 seed questions in 12 computable domains using executable rationales for deterministic reward.
- `https://github.com/camel-ai/loong` · org: CAMEL-AI.org · date: 2025.3
- Paper(s): —
- Task: RLVR

### DataSciBench
- **Idea:** Benchmark evaluating LLM agents on multi-step interdependent data-science workflows (plan, code, sequential execution) via completion-rate, cost, and error metrics.
- `https://github.com/THUDM/DataSciBench` · org: Tsinghua · date: 2025.2
- Paper(s): —
- Task: data analysis

### reasoning-gym
- **Idea:** 100+ procedural dataset generators with built-in score_answer functions giving infinite difficulty-adjustable, algorithmically verifiable rewards for RL reasoning training.
- `https://github.com/open-thought/reasoning-gym` · org: open-thought · date: 2025.1
- Paper(s): —
- Task: Math/Game

### llmgym
- **Idea:** Gymnasium-style unified reset/step interface bundling diverse LLM-app environments (QA, customer service, terminal) with built-in feedback for RL/SFT benchmarking.
- `https://github.com/tensorzero/llmgym` · org: tensorzero · date: 2025.1
- Paper(s): —
- Task: TextGame/Tool

### SWE-Gym
- **Idea:** First training environment of 2,438 executable real-world Python tasks for SWE agents via SFT plus inference-time verifier scaling.
- `https://github.com/SWE-Gym/SWE-Gym` · org: UC Berkeley/UIUC/CMU/Apple · date: 2024.12
- Paper(s): [Paper](https://arxiv.org/abs/2412.21139)
- Task: SWE

### debug-gym
- **Idea:** Interactive debugging env wrapping pdb plus bash/view/grep/edit/eval tools so agents debug via real breakpoints/state inspection, not just code synthesis.
- `https://github.com/microsoft/debug-gym` · org: Microsoft Research · date: 2024.11
- Paper(s): —
- Task: Debugging/Game/Code

### gym-llm
- **Idea:** LLMEnv adapter exposing gymnasium control/game envs to LLM agents via observation/action/goal schemas plus history-reflection, targeting planning over real-time control.
- `https://github.com/rsanchezmo/gym-llm` · org: Rodrigo Sánchez Molina · date: 2024.8
- Paper(s): —
- Task: Control/Game

### AgentGym
- **Idea:** 14 ReAct-format envs as HTTP services plus AgentEvol, a self-evolution method letting agents improve beyond seen data across tasks/environments.
- `https://github.com/WooooDyy/AgentGym` · org: Fudan · date: 2024.6
- Paper(s): —
- Task: Web/Game

### tau-bench
- **Idea:** Benchmark for tool-agent-user interaction: LLM-simulated users hold dynamic multi-turn conversations testing API tool use under policy constraints (pass^k consistency).
- `https://github.com/sierra-research/tau-bench` · org: Sierra · date: 2024.6
- Paper(s): —
- Task: Tool

### appworld
- **Idea:** High-fidelity sandbox of 9 apps/457 APIs over ~100 simulated people where agents write interactive Python; success judged by database-state changes.
- `https://github.com/StonyBrookNLP/appworld` · org: Stony Brook University · date: 2024.6
- Paper(s): —
- Task: Phone Use

### android_world
- **Idea:** Live-emulator benchmark of 116 tasks across 20 apps with parameter-randomized dynamic task instantiation and durable reward signals to prevent solution memorization.
- `https://github.com/google-research/android_world` · org: Google Research · date: 2024.5
- Paper(s): —
- Task: Phone Use

### TheAgentCompany
- **Idea:** Simulated software company (GitLab, PM, chat) benchmarking agents on consequential cross-role work tasks with checkpoint-based deterministic and LLM evaluators.
- `https://github.com/TheAgentCompany/TheAgentCompany` · org: CMU, Duke · date: 2024.3
- Paper(s): —
- Task: Coding

### LlamaGym
- **Idea:** Single Agent base class abstracting context, episode batching, reward assignment, and PPO loops so LLMs can be online-RL fine-tuned in Gym with three methods.
- `https://github.com/KhoomeiK/LlamaGym` · org: Rohan Pandey · date: 2024.3
- Paper(s): —
- Task: Game

### visualwebarena
- **Idea:** Multimodal extension of WebArena with visually-grounded web tasks evaluated via screenshots and Set-of-Marks element marking for vision-language agents.
- `https://github.com/web-arena-x/visualwebarena` · org: CMU · date: 2024.1
- Paper(s): —
- Task: Web

### LMRL-Gym
- **Idea:** Eight multi-turn RL benchmarks (mazes, chess, Wordle, 20-questions) stressing credit assignment, trajectory stitching, and info-gathering with BC+ILQL/PPO baselines.
- `https://github.com/abdulhaim/LMRL-Gym` · org: UC Berkeley · date: 2023.12
- Paper(s): —
- Task: Game

### OSWorld
- **Idea:** Computer-use benchmark running real OSes (Ubuntu/Windows via VM/Docker/AWS) where screenshot-driven agents do open-ended GUI/file/web tasks with parallel evaluation.
- `https://github.com/xlang-ai/OSWorld` · org: HKU, CMU, Salesforce, Waterloo · date: 2023.10
- Paper(s): —
- Task: Computer Use

### webarena
- **Idea:** Self-hostable replicas of real sites (shop, GitLab, Reddit, maps) for reproducible web-agent eval scored by functional task outcomes, not surface metrics.
- `https://github.com/web-arena-x/webarena` · org: CMU · date: 2023.7
- Paper(s): —
- Task: Web

### AgentBench
- **Idea:** First benchmark evaluating LLM-as-agent across 8 multi-turn interactive environments (OS, DB, knowledge graph, card game, ALFWorld, web shop/browse).
- `https://github.com/THUDM/AgentBench` · org: Tsinghua University · date: 2023.7
- Paper(s): —
- Task: Game/Web/QA/Tool

### WebShop
- **Idea:** Simulated e-commerce env (1.18M products, 12k instructions) for instruction-following shopping supporting IL/RL/IL+RL with sim-to-real transfer to live sites.
- `https://github.com/princeton-nlp/WebShop` · org: Princeton-NLP · date: 2022.7
- Paper(s): —
- Task: Web

### ScienceWorld
- **Idea:** Text-based environment of 10 elementary-science task families (up to 1,386 variations) with tunable simplifications, benchmarking agent scientific reasoning.
- `https://github.com/allenai/ScienceWorld` · org: AllenAI · date: 2022.3
- Paper(s): —
- Task: TextGame/ScienceQA

### factorio-learning-environment
- **Idea:** Open-ended Factorio benchmark where agents act via a Python-code REPL (observe output, generate program, get state feedback) for non-saturating evals.
- `https://github.com/JackHopkins/factorio-learning-environment` · org: JackHopkins · date: 2021.6
- Paper(s): —
- Task: Game

### alfworld
- **Idea:** Aligns parallel TextWorld and embodied ALFRED/THOR tasks so agents learn abstract high-level policies in text before transferring to 3D actuation.
- `https://github.com/alfworld/alfworld` · org: Microsoft, CMU, UW · date: 2020.10
- Paper(s): —
- Task: Embodied

### jericho
- **Idea:** Python interface to real interactive-fiction games exposing object trees, vocab, and template action generators to tame combinatorial text action spaces.
- `https://github.com/microsoft/jericho` · org: Microsoft, GIT · date: 2018.10
- Paper(s): —
- Task: TextGame

### TextWorld
- **Idea:** Procedurally generates text adventure games (tw-make) behind a Gym-like API to supply diverse, difficulty-controllable RL training scenarios.
- `https://github.com/microsoft/TextWorld` · org: Microsoft Research · date: 2018.6
- Paper(s): —
- Task: TextGame
