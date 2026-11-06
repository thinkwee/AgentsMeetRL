#!/usr/bin/env python3
"""Check diagnostic JSONL exports; see recipes/offline-inspection.md.

Standard library only. Read-only: does not modify exports or contact a service.
This validates the export contract, not native tensors or a training objective.
"""
import argparse
import json
import math
from pathlib import Path

ARRAYS = ('token_ids', 'origins', 'loss_mask', 'behavior_logprobs', 'policy_versions')
ORIGINS = {'context', 'assistant', 'tool', 'padding'}
END_REASONS = {'terminal', 'truncated', 'tool_error', 'infrastructure_error'}


def finite_number(value):
    return type(value) in (int, float) and math.isfinite(value)


def validate(row):
    errors = []
    if not isinstance(row, dict):
        return ['record must be an object']
    for key in ('sample_id', 'episode_id', 'group_id'):
        if not isinstance(row.get(key), str) or not row[key].strip():
            errors.append(f'{key}: expected nonempty string')
    if not isinstance(row.get('end_reason'), str) or row['end_reason'] not in END_REASONS:
        errors.append('end_reason: unknown or missing')
    for key in ARRAYS:
        if not isinstance(row.get(key), list):
            errors.append(f'{key}: expected array')
    if any(not isinstance(row.get(k), list) for k in ARRAYS):
        return errors
    n = len(row['token_ids'])
    if not n:
        errors.append('token_ids: empty trajectory')
    if any(len(row[k]) != n for k in ARRAYS):
        return errors + ['token arrays have different lengths']
    attention = row.get('attention_mask', [int(x != 'padding') for x in row['origins']])
    if not isinstance(attention, list) or len(attention) != n:
        return errors + ['attention_mask: wrong shape']
    for i, (token, origin, mask, lp, version, attn) in enumerate(zip(
            *(row[k] for k in ARRAYS), attention)):
        if type(token) is not int or token < 0:
            errors.append(f'token {i}: invalid token ID')
        if not isinstance(origin, str) or origin not in ORIGINS:
            errors.append(f'token {i}: unknown origin')
        if type(mask) not in (int, bool) or mask not in (0, 1):
            errors.append(f'token {i}: mask must be binary')
        if type(attn) not in (int, bool) or attn not in (0, 1):
            errors.append(f'token {i}: attention must be binary')
        if bool(attn) != (origin != 'padding'):
            errors.append(f'token {i}: attention/padding mismatch')
        if bool(mask) != (origin == 'assistant'):
            errors.append(f'token {i}: loss target/origin mismatch')
        if mask:
            if not finite_number(lp) or lp > 0:
                errors.append(f'token {i}: selected logprob must be finite and <= 0')
            if not ((type(version) is int and version >= 0) or
                    (isinstance(version, str) and version.strip())):
                errors.append(f'token {i}: selected token needs policy version')
            if i == 0:
                errors.append('token 0: selected target has no preceding context')
    if not any(row['loss_mask']):
        errors.append('no trained tokens; exclude or explain before training')
    return errors


def demo():
    row = dict(sample_id='s1', episode_id='e1', group_id='g1', end_reason='terminal',
               token_ids=[101, 201, 202, 301, 203, 204, 0],
               origins=['context', 'assistant', 'assistant', 'tool', 'assistant', 'assistant', 'padding'],
               loss_mask=[0, 1, 1, 0, 1, 1, 0],
               behavior_logprobs=[None, -.7, -.2, None, -.4, -.1, None],
               policy_versions=[None, 10, 10, None, 11, 11, None])
    assert not validate(row), validate(row)
    for key, values in [('loss_mask', [0, 1, 1, 1, 1, 1, 0]),
                        ('behavior_logprobs', [None, float('nan'), -.2, None, -.4, -.1, None]),
                        ('policy_versions', [None] * 7), ('token_ids', [101])]:
        assert validate(dict(row, **{key: values})), key
    losses = [[1., 1.], [3.] * 8]
    token_mean = sum(map(sum, losses)) / sum(map(len, losses))
    seq_mean = sum(sum(x) / len(x) for x in losses) / len(losses)
    seq_sum = sum(map(sum, losses)) / len(losses)
    assert (token_mean, seq_mean, seq_sum) == (2.6, 2.0, 13.0)
    # Behavior .2, proximal .3, current .33: update ratio != correction.
    update = math.exp(math.log(.33) - math.log(.3))
    correction = math.exp(math.log(.3) - math.log(.2))
    assert math.isclose(update, 1.1) and math.isclose(correction, 1.5)
    assert math.isclose(update * correction, .33 / .2)
    print(json.dumps({'synthetic_demo': 'passed', 'reductions': [token_mean, seq_mean, seq_sum],
                      'update_ratio': update, 'behavior_weight': correction}))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('path', nargs='?', type=Path)
    parser.add_argument('--demo', action='store_true')
    args = parser.parse_args()
    if args.demo:
        demo()
        return 0
    if args.path is None:
        parser.error('provide JSONL path or --demo')
    errors, seen, count = [], set(), 0
    try:
        with args.path.open() as f:
            for line_number, line in enumerate(f, 1):
                if not line.strip():
                    continue
                count += 1
                try:
                    row = json.loads(line)
                except (ValueError, TypeError) as exc:
                    errors.append(f'line {line_number}: invalid JSON: {exc}')
                    continue
                issues = validate(row)
                sid = row.get('sample_id') if isinstance(row, dict) else None
                if isinstance(sid, str):
                    if sid in seen:
                        issues.append('duplicate sample_id')
                    seen.add(sid)
                errors.extend(f'line {line_number}: {issue}' for issue in issues)
    except (OSError, UnicodeError) as exc:
        errors.append(str(exc))
    if not count:
        errors.append('no records')
    print(json.dumps({'records': count, 'errors': errors}, indent=2))
    return int(bool(errors))


if __name__ == '__main__':
    raise SystemExit(main())
