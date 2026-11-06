# Source-inspected implementation snapshots

These cards describe specific commits, not the latest release or benchmark rankings.
Source was read from Git objects (excluding local working-tree edits); each commit's
existence in the public GitHub repository was checked on 2026-11-06. No training
run, dependency installation, or end-to-end configuration validation was performed.
Dependency compatibility must be checked in the pinned repository before running.

| Framework | Concrete interface inspected | Limitation |
|---|---|---|
| [slime](slime.md) | Sample, custom generation, Megatron policy loss and TIS | Custom Agent loop and configuration still need validation |
| [veRL](verl.md) | AgentLoopOutput, ToolAgentLoop, aggregation and rollout correction | Loop/engine combinations are not a universal compatibility guarantee |
| [AReaL](areal.md) | Workflow, interaction tensor conversion, proximal policy and staleness manager | Admission control alone is not an audit of consumed lag |

Use [sources.json](../evidence/sources.json) for claim-to-code provenance. Evidence
levels are distinct: paper-described, source-inspected, configuration-validated,
runtime-validated. Quality improvements additionally require controlled evaluation.
Do not promote a source-inspected feature to runtime-validated merely because an
API exists. Entries missing from these cards remain catalogue-only.
