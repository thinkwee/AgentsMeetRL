# Problem: applying agentic-RL to a vertical domain (medical, finance, OS, biology…)

You're not training a general-purpose reasoner — you have a specific
domain (medicine, biology, finance, systems, etc.) and want to apply
agentic-RL. The decisions are different from a generic RL run because
the corpus is sparse, the verifier is custom, and the reward shape is
domain-specific.

## When this applies

- You can name a vertical: medicine, finance, biology, OS tuning,
  scientific simulation, etc.
- A general benchmark (HotpotQA, SWE-bench, etc.) is not a good proxy
  for the success metric you actually care about.
- You have access to a domain-specific verifier (lab assay, market
  back-test, kernel benchmark, segmentation IoU, …).

If none of these apply, this file is the wrong place — go back to
`../_INDEX.md`.

## Decision flow

1. **Choose the success metric first, before reward.** If the metric
   is non-differentiable (e.g. portfolio Sharpe, IoU, Linux kernel
   latency), it usually maps directly to RL reward — not to SFT.
2. **Choose the agent boundary.** Tools the agent can call (database
   query, simulator, search, lab API) define the action space. Lock
   this *before* training; changing it mid-run invalidates rollouts.
3. **Decide rule vs model reward.** If the metric is computable
   (segmentation IoU, financial back-test, kernel benchmark), use
   rule. If it requires expert judgement (clinical fidelity, code
   quality), use a learned reward model (and budget for label
   collection).
4. **Pick base framework.** Most domain projects use veRL or its
   forks because they support custom reward callbacks and tool APIs
   without subclassing. See `../../references/base-frameworks.md`.
5. **Start with a tiny eval set, hand-graded.** A 20-item domain
   eval that you grade yourself catches more issues than a 500-item
   auto-graded one.
6. **Plan for distribution shift.** Domain data drifts (markets shift,
   kernel APIs change, clinical guidelines update). Either freeze
   your eval set with a snapshot, or budget for periodic re-grading.

## Common pitfalls

- **Reusing a generic prompt template.** Domain users want
  domain-specific output structure (SOAP note, prospectus, kernel
  config patch). Bake the structure into the format reward.
- **Treating the LLM-judge as ground truth in domains it wasn't
  trained on.** A code-judge LLM grading clinical reasoning will
  miss obvious errors. Always cross-validate with a domain expert
  on a sample.
- **Skipping the SFT warmup on domain corpus.** Most domain projects
  do a small SFT pass on domain text before RL — the base model
  rarely speaks the domain vocabulary well enough for RL to bootstrap
  from scratch. See `../training/sft-to-rl-transition.md`.

## Paper / repo references

- `MedSAM-Agent` — GRPO via veRL for medical image segmentation; reward is clinical-fidelity model-based score.
  github: `https://github.com/CUHK-AIM-Group/MedSAM-Agent`, paper: `https://arxiv.org/abs/2602.03320`, CUHK/Tencent, date: 2026.2
- `OS-R1` — GRPO via veRL for Linux kernel parameter tuning; rule-based reward.
  github: `https://github.com/LHY-24/OS-R1`, paper: `https://arxiv.org/abs/2508.12551`, ISCAS, date: 2025.8
- `Biomni` — biomedical agent (scRNAseq/CRISPR/ADMET/knowledge workflows); single-turn baseline pre-RL.
  github: `https://github.com/snap-stanford/Biomni`, paper: `https://www.biorxiv.org/content/10.1101/2025.05.30.656746v1`, Stanford University (SNAP), date: 2025.3
- `MMedAgent-RL` — medical agent with RL fine-tuning (code pending).
  paper: `https://arxiv.org/abs/2506.00555`, date: 2025.6
- `Alpha-R1` — GRPO for finance alpha-factor screening; portfolio-returns + LLM judge as combined reward.
  github: `https://github.com/FinStep-AI/Alpha-R1`, paper: `https://arxiv.org/abs/2512.23515`, SJTU / FinStep.AI / StepFun, date: 2025.12


## See also

- `../training/sft-to-rl-transition.md` — domain SFT warmup before RL.
- `../training/reward-mixing.md` — combining domain rule + LLM judge.
- `../research-workflow/data-curation.md` — building domain eval sets.
- `../../references/domain-specific.md` — full corpus.
