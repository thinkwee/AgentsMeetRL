# Problem: logits don't match sampled tokens — retokenization drift

## Symptoms

- KL divergence to old policy explodes within a few steps even with
  small clip ε.
- NaNs or extremely large importance ratios after a fresh refresh.
- `old_log_probs` stored from rollout differs from a recompute of
  log-probs over the same text.
- Common in custom rollout code that:
  - stores rollouts as decoded text,
  - re-tokenizes for training,
  - mixes tokenizers across rollout (vLLM/SGLang) and training (HF).

## Root causes

The corpus's diagnosis (Agent-R1 calls this out by name):

> "Retokenization drift in text-based pipelines: if rollout data is
> collected as text and later tokenized again for training, the
> `Token → Text → Token` conversion is not reversible."
> — `https://github.com/0russwest0/Agent-R1`, paper:
> `https://arxiv.org/abs/2511.14460`, org: USTC, date: 2025.3.

Specifically:

1. **BPE merges differ across encode/decode** — leading whitespace,
   special tokens, byte-level encoding edge cases.
2. **vLLM / SGLang vs HuggingFace tokenization** — even nominally the
   same tokenizer can produce different token IDs (eg. `<think>` may be
   one token in one and three in the other).
3. **Tool-output insertion** — when the env appends tool output, the
   join boundary `<tool_response>...</tool_response>` may merge
   differently after re-tokenize.
4. **Multi-turn template drift** — applying a chat template at training
   time may insert different control tokens than at rollout time.

## Diagnosis

### Quick assertion

For a sampled rollout, store both `token_ids` and the decoded `text`.
Then re-tokenize `text` and assert equality:

```python
recomputed_ids = tokenizer(text, add_special_tokens=False).input_ids
assert recomputed_ids == sampled_token_ids, "drift detected"
```

If this fails on >1% of rollouts, you have drift.

### Inspect first divergent token

Compute `recomputed_ids` and `sampled_token_ids` and find the first
index where they differ. Decode each side near that index. Common
offenders:

- ` ` vs `Ġ` byte-level encoding boundaries.
- `\n\n<assistant>` vs `\n<assistant>` template injection.
- Tool-output `<tool_response>{json}</tool_response>` joining.

### Compare KL across implementation paths

Start a run with text-based rollout collection, log KL. Switch to
token-ID rollout collection, log KL. If KL drops dramatically (e.g.
from 5.0 to 0.2), drift was the culprit.

## Fixes

### Fix 1: store token IDs, not strings, between rollout and update

The straightforward fix. Frameworks that already do this include:

> **veRL** — github: `https://github.com/volcengine/verl`,
> paper: `https://arxiv.org/abs/2409.19256`, ByteDance Seed, date: 2024.9.
> Rollouts carry `responses` as token IDs end-to-end through the data
> flow; no decode/re-tokenize step is required.

> **verl-agent** — github: `https://github.com/langfengQ/verl-agent`,
> paper: `https://arxiv.org/abs/2505.10978`, NTU, date: 2025.5.
> Per-step rollout stores tokenized prompt+response, never re-tokenizes
> for training — explicit design choice.

> **Agent-R1** — github: `https://github.com/0russwest0/Agent-R1`,
> paper: `https://arxiv.org/abs/2511.14460`, org: USTC, date: 2025.11.
> Step-level MDP makes this explicit: each step's prompt and response
> are stored as token IDs.

> **SkyRL-Agent** — github: `https://github.com/NovaSky-AI/SkyRL`,
> paper: `https://arxiv.org/abs/2511.16108`, date: 2025.11.
> Long-horizon agent training that preserves token-level info.

### Fix 2: pin tokenizer version + chat template

If you can't avoid re-tokenization (legacy code), at least:

- Pin tokenizer version exactly between rollout and training.
- Use the *same* chat template + skipping rules
  (`add_generation_prompt`, `add_special_tokens`, etc.).
- Test: re-tokenize a sample of rollouts and assert ID equality.

### Fix 3: same inference engine + tokenizer

Mixing engines is risky. If your trainer uses HF and rollout uses vLLM:

- Use vLLM ≥ 0.6.x with `prompt_token_ids=...` so vLLM doesn't
  re-tokenize on its side.
- Or keep one engine end-to-end (slime / NeMo-RL favor this).

### Fix 4: avoid concatenating tool output at the string level

If you concatenate raw tool output into the prompt as a string, the
chat template at training time may slice differently. Instead:

- Tokenize tool output once, append IDs.
- Or use the framework's `multi_turn` rollout interface (verl's
  `examples/sglang_multiturn/`).

## Paper / repo references

- `Agent-R1` — github: `https://github.com/0russwest0/Agent-R1`,
  paper: `https://arxiv.org/abs/2511.14460`, org: USTC, date: 2025.11.
  Calls out retokenization drift as a motivating bug.
- `verl-agent` — github: `https://github.com/langfengQ/verl-agent`,
  paper: `https://arxiv.org/abs/2505.10978`, NTU/Skywork, date: 2025.5
  (NeurIPS 2025).
- `SkyRL` — github: `https://github.com/NovaSky-AI/SkyRL`,
  paper: `https://arxiv.org/abs/2511.16108`, UC Berkeley, date: 2025.11.
