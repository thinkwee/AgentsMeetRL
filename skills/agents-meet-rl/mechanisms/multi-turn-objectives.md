# Multi-turn objectives and credit

## Specify the statistical unit first

For terminal reward `R_i`, a common outcome-GRPO estimator assigns
`A_i = (R_i - mean_group(R)) / (std_group(R) + epsilon)` to each trained token of
attempt i. Some variants omit standard-deviation normalization. This is shared
outcome credit, not evidence that every action contributed equally to success.
Grouping turns with different states together is not ordinary outcome GRPO.

With process rewards, choose whether discounting advances per token, model turn,
or environment step. GAE and bootstrapping must use the same transition unit and
terminal semantics. Inserting a long tool observation should not silently add
hundreds of discount steps if the intended unit is an agent action.

## Three reductions are not interchangeable

Let `m_it` select trained tokens, `n_i = sum_t m_it`, and `l_it` be a token loss.
For N nonempty trajectories:

- **Token mean:** `sum_i,t m_it*l_it / sum_i n_i`. Each valid token has equal
  weight; long trajectories contribute more total terms.
- **Sequence mean of token means:** `sum_i (sum_t m_it*l_it / n_i) / N`.
  Each trajectory has equal aggregate weight; each token in a short trajectory
  gets more weight than a token in a long one.
- **Sequence mean of token sums:** `sum_i,t m_it*l_it / N`.
  Average magnitude changes with generated length. A fixed length normalizer
  changes scale without introducing each trajectory's inverse length.

Example: one trajectory has 2 tokens with loss 1 each, another has 8 tokens with
loss 3 each. The three reductions give **2.6, 2.0, 13.0**, respectively. Neither
of the first two guarantees stable output length. Choose the intended objective,
then monitor reward, entropy, length, and gradient statistics.

Ratio granularity (token ratio versus a sequence statistic, e.g. GSPO), advantage
construction, and reduction are three separate choices. Disabling GRPO's std
normalization alone does not reproduce every component of a Dr.GRPO recipe.

## Splitting, filtering, and distribution

When splitting a trajectory, retain original episode-level denominators if the
objective is to remain unchanged. Averages of per-turn averages usually change
weights. Repeated history must be context-only in later samples.

Distributed token mean requires a global valid-token denominator, with scaling
consistent with the backend's gradient averaging and accumulation. The mean of
unequal microbatch means is generally not the global mean. Check a fixed batch
under different partitions, including fully masked rows and uneven lengths.

Rejecting tokens can either preserve the original denominator or renormalize on
survivors; these are different objectives. State the choice. Zero-variance GRPO
groups have no outcome-advantage signal but may still have KL/entropy gradients.

## Evidence and verification

[veRL's pinned agg_loss](../implementations/verl.md) implements distinct reduction
modes; [slime's card](../implementations/slime.md) identifies its reducer path.
The numeric example is a derivation, not a measured training result. Check it
with [the offline recipe](../recipes/offline-inspection.md).
