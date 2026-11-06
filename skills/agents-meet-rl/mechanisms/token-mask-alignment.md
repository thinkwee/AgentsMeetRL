# Token, mask, and logprob alignment

## Worked trajectory

The IDs below are illustrative, not a real tokenizer vocabulary. Masks are
**target-token aligned** here; a backend may store next-token prediction slots.

| Position | Token ID | Origin | Attention valid | Loss | Behavior logprob |
|---|---:|---|---:|---:|---|
| 0 | 101 | user/prompt | 1 | 0 | absent |
| 1 | 201 | assistant tool call | 1 | 1 | -0.7 |
| 2 | 202 | assistant tool call end | 1 | 1 | -0.2 |
| 3 | 301 | tool observation | 1 | 0 | absent |
| 4 | 203 | assistant final answer | 1 | 1 | -0.4 |
| 5 | 204 | assistant EOS | 1 | 1 | -0.1 |
| 6 | 0 | padding | 0 | 0 | absent |

Tool observations have no policy-gradient target, but later predictions attend
to them. Consequently their representations can receive gradients through later
assistant losses. Loss masking does not detach context or hide observations.
Sampled assistant delimiters/EOS may be targets; externally inserted template
markers are not sampled actions merely because they have an assistant role tag.

## Alignment procedure

1. Preserve generated IDs from the engine, including stop-token handling; retain
   the actual input IDs for every call. Do not rebuild training targets from text.
2. Map every logprob to the token it scores. For causal LM logits, slot `j-1`
   predicts target token `j`. Shift masks and probability arrays consistently,
   exactly once; the first token of a standalone sequence has no preceding slot.
3. Verify IDs, target spans, and logprob lengths before padding or packing.
   Masked probability placeholders must never enter ratios, KL, or statistics.
4. Build causal attention and per-sequence boundaries separately from loss masks.
   Packed examples must not attend across episodes. Check position IDs and any
   multimodal payload alignment; matching token IDs alone is insufficient for VLMs.
5. Compare the same weights/context on rollout and trainer paths. Report masked
   absolute logprob differences and quantiles; do not assume bitwise equivalence
   across precision, kernels, or MoE routing implementations.

## Retokenization diagnosis

`encode(decode(ids)) != ids` reveals a round-trip difference, not proof that the
training path uses those reconstructed IDs. The decisive check is rollout input
and target IDs versus the actual learner tensors. Any mismatch on trained tokens
requires explanation; there is no universal acceptable 1% drift threshold.
Appending separately tokenized tool text is only correct when the rollout used
that same prefix construction. Reapplying a chat template may break prefix identity.

See [veRL response masks](../implementations/verl.md) and
[AReaL tensor alignment](../implementations/areal.md). Use the
[offline inspection recipe](../recipes/offline-inspection.md) before changing loss.
