# Problem: token-level vs sequence-level loss aggregation

## Decision

Choose the statistical unit before selecting a reduction. Token mean weights valid
tokens equally; sequence mean of token means weights sequences equally; sequence
mean of token sums scales with sequence length. None universally prevents length
blow-up. Ratio granularity and advantage normalization are separate choices.

See [multi-turn objectives](../../mechanisms/multi-turn-objectives.md) for formulas,
a worked unequal-length example, splitting semantics, and distributed denominators.

## Concrete implementation

The [veRL implementation card](../../implementations/verl.md) pins `agg_loss` and
its `token-mean`, `seq-mean-token-mean`, and `seq-mean-token-sum` paths. Check the
actual version and global-batch normalization before copying configuration.
Disabling `norm_adv_by_std_in_grpo` alone does not reproduce the complete Dr.GRPO
recipe. Likewise a sequence-level importance ratio does not determine the reducer.

## Diagnosis and verification

For the same generated trajectories, compute each reduction offline. Check that
sample splitting preserves intended episode weighting and that unequal microbatch
partitions reproduce the global objective. Track length against task reward and
entropy; investigate reward/termination/context effects before changing reduction.

## Paper / repo references

- [veRL](https://github.com/volcengine/verl), [paper](https://arxiv.org/abs/2409.19256).
- [Dr.GRPO](https://arxiv.org/abs/2503.20783).
- [slime implementation card](../../implementations/slime.md).
