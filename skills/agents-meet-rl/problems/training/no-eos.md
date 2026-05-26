# Problem: model never emits EOS / never stops generating

## Symptoms

- Every rollout hits `max_response_length`.
- `truncated_fraction` > 50%.
- Model emits the answer then keeps going with garbage / repetition.

## Root causes

1. **EOS token stripped or remapped** in your tokenizer / chat template.
2. **No EOS supervision** in SFT — model never learned to stop.
3. **Reward continues paying** for tokens after the answer (e.g. the
   reward function rewards substring match without checking for EOS).
4. **Generation kwargs** (`stop_token_ids`, `eos_token_id`) misconfigured.

## Diagnosis

- Check `responses` from a rollout — is the last token EOS? If not,
  why?
- Print decoded response with `skip_special_tokens=False` to see what
  the model actually emits. Often reveals weird tokens or wrong EOS.

## Fixes

### Fix 1: assert EOS in tokenizer

```python
assert tokenizer.eos_token_id is not None
assert tokenizer.eos_token_id in tokenizer(some_test_text +
    tokenizer.eos_token).input_ids
```

### Fix 2: chat template includes assistant EOS

Make sure your chat template ends with `{eos}` after assistant content.
Otherwise the model trained on truncated sequences without EOS.

### Fix 3: stop_token_ids in vLLM/SGLang

Pass explicit `stop_token_ids=[tokenizer.eos_token_id]` to your
inference engine. Many bugs come from default stop sets that don't
match the tokenizer's actual EOS.

### Fix 4: penalize post-`<answer>` tokens

If your reward function awards on substring presence, post-answer
content adds nothing but inflates length. Add a hard cap: anything
after `</answer>` is truncated for reward computation, but generates
small penalty.

### Fix 5: SFT cold-start with proper EOS

Re-run SFT making sure each example ends in `</answer>{eos}`. Then
resume RL.

### Fix 6: format reward requires close tag + EOS

Don't give format reward unless `</answer>` is followed by EOS within
N tokens.

## Common gotcha

Llama-3 has multiple EOS-like tokens (`<|eot_id|>`,
`<|end_of_text|>`). Pick the one your chat template uses and pass it
explicitly to vLLM / SGLang as a stop token. Otherwise the model emits
`<|eot_id|>` (correct stop in chat) but vLLM only stops on
`<|end_of_text|>` and continues.

## Paper / repo references

> **Search-R1** — github: `https://github.com/PeterGriffinJin/Search-R1`,
> paper: `https://arxiv.org/abs/2503.09516`, org: UIUC/Google, date: 2025.3.
> Why: ships an explicit `<answer>...</answer>{eos}` format spec and
> stop-token plumbing that handles Llama-3 / Qwen tokenizer quirks —
> a clean reference for fix 5 / fix 6.

> **Tool-Star** — github: `https://github.com/dongguanting/Tool-Star`,
> paper: `https://arxiv.org/abs/2505.16410`, org: RUC, date: 2025.5.
> Why: multi-stage SFT recipe shows how to bake in EOS supervision
> before RL takes over.

> **Agent-R1** — github: `https://github.com/0russwest0/Agent-R1`,
> paper: `https://arxiv.org/abs/2511.14460`, org: USTC, date: 2025.11.
> Why: reference vLLM-based rollout that pins explicit `stop_token_ids`
> per chat template — fix 3 done right.
