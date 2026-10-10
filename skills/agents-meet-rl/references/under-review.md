# Under Review (Open-source pending)

Notable papers whose code is not yet open-source. Track these for future reference.

_Total: 33 entries._

| # | Title | Idea | Link |
|---|---|---|---|
| 1 | SAPO: Single-Rollout Autoregressive Policy Optimization | PPO-style agentic RL on ALFWorld/WebShop built on verl-agent; repo dy-liang/SAPO is README-only so far (code "will be released in the next few days"). | https://arxiv.org/abs/2608.19842 |
| 2 | Test-Time Self-Evolving GUI Visual Grounding | Reflection-guided on-policy self-distillation for GUI grounding; no public code repository located. | https://arxiv.org/abs/2608.11191 |
| 3 | ChemWorld | Chemistry agent environment; no public code repository located. | https://arxiv.org/abs/2608.10792 |
| 4 | EviBack | No public code repository located. | https://arxiv.org/abs/2607.23955 |
| 5 | MAVEN: Evidence-State Rewards | Evidence-state process rewards for search agents; no public code repository located. | https://arxiv.org/abs/2607.02073 |
| 6 | GRASP | No public code repository located. | https://arxiv.org/abs/2607.10463 |
| 7 | SINKFLEX-RL | No public code repository located. | https://arxiv.org/abs/2608.10357 |
| 8 | Agon | No public code repository located. | https://arxiv.org/abs/2607.07690 |
| 9 | GroundCUA | ServiceNow computer-use grounding release whose training/ directory is marked Coming Soon. | https://github.com/ServiceNow/GroundCUA |
| 10 | RoMeRL | Robust memory RL; README states training code is being organized, only eval checkpoints released. | https://arxiv.org/abs/2608.02508 |
| 11 | SearchMaster | Search-agent RL whose training code is explicitly marked planned for release. | https://arxiv.org/abs/2608.01822 |
| 12 | UI-Mate | Tencent GUI agent whose RL methodology is described in prose but whose repo ships inference/eval code only. | https://arxiv.org/abs/2608.15930 |
| 13 | Qwen-CUA | Computer-use agent from xlang-ai; repo carries the technical report and a reference demo only, weights hosted separately. | https://arxiv.org/abs/2608.02352 |
| 14 | Qwen-UI-Agent: Towards Next-Generation Real-World Centric Foundation GUI Agent | Tongyi-MAI's GUI foundation agent claiming ~10K parallel envs and online RL; repo is public but ships no training code. | https://arxiv.org/abs/2607.28227 |
| 15 | CoEvolve: Training LLM Agents via Agent-Data Mutual Evolution | CoEvolve: agent-data mutual evolution that mines forgetting/uncertainty signals from rollouts to synthesize new tasks and update the RL training distribution. | https://arxiv.org/abs/2604.15840 |
| 16 | JoyAgents-R1: Joint Evolution Dynamics for Versatile Multi-LLM Agents with Reinforcement Learning | HiMA-Ecom/HiMA-R1: variance-reduction GRPO that selects informative agent groups by reward variance for joint training of hierarchical e-commerce multi-agents. | https://arxiv.org/abs/2506.19846 |
| 17 | Shop-R1: Rewarding LLMs to Simulate Human Behavior in Online Shopping via Reinforcement Learning | Shop-R1: two-stage RL simulating shopper behavior via logit-guided rationale rewards plus difficulty-aware hierarchical action rewards to curb reward hacking. | https://arxiv.org/abs/2507.17842 |
| 18 | Training Long-Context, Multi-Turn Software Engineering Agents with Reinforcement Learning | Trains long-context multi-turn SWE agents via rejection fine-tuning then synchronous DAPO RL, lifting Qwen2.5-72B from 11% to 39% on SWE-bench Verified. | https://arxiv.org/abs/2508.03501 |
| 19 | Acting Less is Reasoning More! Teaching Model to Act Efficiently | OTC-PO: rewards correct answers with minimal tool calls (tool productivity) to fight cognitive offloading, cutting calls up to 68% while keeping accuracy. | https://arxiv.org/abs/2504.14870 |
| 20 | Agentic Reasoning and Tool Integration for LLMs via Reinforcement Learning | ARTIST: outcome-based RL teaching LLMs to autonomously decide when/which tools to invoke within multi-turn reasoning without step-level supervision. | https://arxiv.org/abs/2505.01441 |
| 21 | ComputerRL: Scaling End-to-End Online Reinforcement Learning for Computer Use Agents | ComputerRL: scales online RL over thousands of parallel desktops with an API-GUI action paradigm and Entropulse (RL/SFT alternation) to avoid entropy collapse. | https://arxiv.org/abs/2508.14040 |
| 22 | Understanding Tool-Integrated Reasoning | Understanding TIR: formal proof tools strictly expand LLM support, plus ASPO (Advantage Shaping Policy Optimization) that reshapes advantage to guide tool use. | https://zhongwenxu.notion.site/Understanding-Tool-Integrated-Reasoning-2551c4e140e3805489fadcc802a1ea83 |
| 23 | Memory-R1: Enhancing Large Language Model Agents to Manage and Utilize Memories via Reinforcement Learning | Memory-R1: outcome-driven RL (PPO/GRPO) trains a Memory Manager (ADD/UPDATE/DELETE/NOOP) and Answer agent for learned external memory using only 152 QA pairs. | https://arxiv.org/abs/2508.19828 |
| 24 | Encouraging Good Processes Without the Need for Good Answers: Reinforcement Learning for LLM Agent Planning | RLTR: decouples agent planning from answering, rewarding tool-use completeness of invocation sequences so planning improves without verifiable final answers. | https://arxiv.org/abs/2508.19598 |
| 25 | SFR-DeepResearch: Towards Effective Reinforcement Learning for Autonomously Reasoning Single Agents | SFR-DeepResearch: simple RL recipe on entirely synthetic data that continually trains reasoning-optimized single agents while preserving reasoning ability. | https://arxiv.org/abs/2509.06283 |
| 26 | WebExplorer: Explore and Evolve for Training Long-Horizon Web Agents | WebExplorer: model-based exploration with long-to-short query evolution generates hard data for SFT+RL, training an 8B web agent over ~16 search turns. | https://arxiv.org/abs/2509.06501 |
| 27 | EnvX: Agentize Everything with Agentic AI | EnvX: agentizes GitHub repos via TODO-guided environment init and an Agent-to-Agent protocol for multi-repo collaboration; RL not detailed in abstract. | https://arxiv.org/abs/2509.08088 |
| 28 | UI-TARS-2 Technical Report: Advancing GUI Agent with Multi-Turn Reinforcement Learning | UI-TARS-2: stabilized multi-turn RL for GUI agents with a data flywheel, hybrid file/terminal+GUI environments, and a unified sandbox for large-scale rollouts. | https://arxiv.org/abs/2509.02544 |
| 29 | UI-Venus Technical Report: Building High-performance UI Agents with RFT | UI-Venus: reinforcement fine-tuning of Qwen2.5-VL UI agents with grounding/navigation reward design plus self-evolving trajectory alignment and sparse-action enhancement. | https://arxiv.org/abs/2508.10833 |
| 30 | Agent2 : An Agent-Generates-Agent Framework for Reinforcement Learning Automation | Agent2: an LLM Generator Agent auto-designs/optimizes RL Target Agents by splitting development into MDP modeling and algorithmic optimization stages. | https://arxiv.org/abs/2509.13368 |
| 31 | Adversarial Reinforcement Learning for Large Language Model Agent Safety | ARLAS: trains LLM agent safety as a two-player zero-sum game with population-based learning defending against all prior attacker checkpoints to avoid cyclic dynamics. | https://arxiv.org/abs/2510.05442 |
| 32 | Learning to Refine: An Agentic RL Approach for Iterative SPARQL Query Construction | A 3B model learns iterative SPARQL query construction via outcome-only GRPO (no SFT), using real-time execution feedback to recover from errors and self-refine. | https://www.arxiv.org/abs/2511.11770 |
| 33 | InfoFlow: Reinforcing Search Agent Via Reward Density Optimization | InfoFlow combats sparse search rewards via reward-density optimization: subproblem intermediate rewards, corrective guidance on stalls, and a history-compressing refiner agent. | https://arxiv.org/abs/2510.26575 |
