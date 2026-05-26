# Problem: reward climbs then collapses (training crash mid-run)

## Symptoms

- Reward, eval metric, and entropy were all healthy for the first
  N steps.
- Around step N, reward suddenly drops sharply, never recovers.
- Sometimes preceded by a KL spike, importance-ratio spike, or NaN.
- Sometimes follows an "easy" period where the model exploits a shortcut.

## Root causes (ordered by frequency)

1. **Reward hacking found and then exhausted.** Model exploited a
   loophole; eventually hits the loophole's saturation; gradient now
   wants to undo learned shortcuts; system unstable. See
   `reward-up-eval-flat.md` to detect ahead of time.
2. **Off-policy gap exploded.** Async-rollout staleness. See
   `async-rollout-staleness.md`.
3. **Template / mode collapse.** Outputs converged; gradient now noise.
   See `entropy-collapse.md`.
4. **Single bad batch** (NaN reward, corrupted observation). One batch
   destabilized everything.
5. **Optimizer state too aggressive.** Adam's running-mean accumulated
   in a bad direction.
6. **Mid-run dataset shift.** Curriculum schedule jumped to harder
   prompts the model couldn't handle.

## Diagnosis

- Pinpoint the step where the collapse started. Look at logs from N-100
  to N+100 with high resolution.
- Save 100 rollouts from N-50, N, N+50. Compare. The change should be
  visible: shorter? more repetitive? broken parse?
- Check KL, ratio, entropy at the inflection. Which spiked first?

```
KL spiked first         → see kl-explosion.md
Ratio spiked first      → see async-rollout-staleness.md
Entropy spiked first    → see entropy-collapse.md
None of the above       → reward-spec / dataset bug — read rollouts
```

## Fixes

### Fix 1: roll back + reduce LR

The simplest. Restart from the most recent stable checkpoint with
LR halved. Often enough.

### Fix 2: stronger KL anchor

Increase β. If the policy ran away into junk, anchoring it to ref helps
recovery. See `kl-explosion.md` for veRL knobs.

### Fix 3: variance-based prompt filtering

If the cause is gradient noise on collapsed prompts, drop low-variance
groups so each step trains only on prompts whose rollouts disagree
across the group. Use reward variance per prompt as a signal-to-noise
proxy and skip groups below a threshold (`FilterGroupsConfig` in veRL).
See `zero-variance-rollouts.md`.

> **veRL** — github: `https://github.com/volcengine/verl`,
> paper: `https://arxiv.org/abs/2409.19256`, ByteDance Seed, date: 2024.9.
> `FilterGroupsConfig` exposes the threshold-based filter.

> **RAGEN** — github: `https://github.com/RAGEN-AI/RAGEN`,
> paper: `https://arxiv.org/abs/2504.20073`, RAGEN-AI, date: 2025.4.
> StarPO motivates filtering bimodal/zero-variance groups in
> multi-turn agentic RL.

### Fix 4: clip / reject NaN batches

A single NaN reward can destabilize Adam state. Add a hard skip: if any
reward in batch is NaN/inf, skip the step.

### Fix 5: gradient clipping

If `grad_norm` spikes near collapse, clip more aggressively (e.g.
0.5 instead of 1.0).

### Fix 6: discard the optimizer state on rollback

Sometimes Adam's running-mean is the offender. Restart Adam fresh from
the rollback checkpoint.

## Prevention (next run)

- **Save checkpoints frequently** (every 100–200 steps). Cheap insurance
  against unrecoverable collapse.
- **Log everything early**: KL, ratio, entropy, reward components, parse
  failure rate, response length, mean and p95.
- **Run 1 canary prompt every step** with eval-mode sampling. Save
  outputs. Watching this stream catches collapse 100s of steps earlier
  than the eval set does.

## Paper / repo references

- **RAGEN** — github: `https://github.com/RAGEN-AI/RAGEN`,
  paper: `https://arxiv.org/abs/2504.20073`, RAGEN-AI, date: 2025.4.
  StarPO framework: documents agentic-RL collapse modes and motivates
  treating low-variance / bimodal-reward prompts as the symptom to
  filter on.
- **veRL** — github: `https://github.com/volcengine/verl`,
  paper: `https://arxiv.org/abs/2409.19256`, ByteDance Seed, date: 2024.9.
  `FilterGroupsConfig` for variance-based group dropout.
