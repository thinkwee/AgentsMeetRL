# Skill behavior regression cases

These are manual acceptance prompts and answer rubrics, not claims of automated
model evaluation. A reviewer can ask the prompts without showing the rubric.

| Prompt | Required distinction |
|---|---|
| Tool outputs have loss mask zero. Can they affect gradients? | No direct action loss; context representations can affect later losses |
| Split one ten-turn attempt into ten samples; is loss unchanged? | Only with matching conditioning, target ownership, weights and denominators |
| Can I replace rollout logprobs with freshly computed old logprobs? | Preserve behavior provenance; specify proximal policy and correction |
| Partial rollout resumes after a weight refresh; what version do I store? | Per-span/token provenance or explicitly pin the episode |
| Token-mean guarantees no length bias, correct? | Equal token weights differ from equal episode weights; no stability guarantee |
| All-zero groups are removed; does the dataset stay the same? | Accepted distribution changes; log all attempted groups and rejection slices |
| Teacher sees reference answer. Where can it be stored? | Teacher-only conditioning, no student-token leakage; response alignment audit |
| Is a tool timeout a failed task? | Distinguish task-visible tool failure from infrastructure and budget failure |
| Ratio max is 6; must training be invalid? | No universal threshold; inspect convention, lag, quantiles, ESS and clipping |
| The source has a function, so is the feature validated? | Source existence, configuration reachability, execution and quality differ |
| Two methods differ by 1 point with CI crossing zero; replicated? | Point estimate alone does not establish improvement |
| Can the installed skill inspect logs? | With available authorized tools yes; never claim inspection without actual access |

For each evaluation, record model/skill revision, prompt, response, rubric failures,
and changed files. Do not treat string matching or link lint as behavioral proof.
