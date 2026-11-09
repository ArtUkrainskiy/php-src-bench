#!/usr/bin/env python3
"""Render the short-text slice separately from the original boundary series."""
import argparse
import gzip
import hashlib
import importlib.util
import json
from pathlib import Path

import study

ROOT = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('boundary_render', ROOT.parent / 'report.py')
base = importlib.util.module_from_spec(spec)
spec.loader.exec_module(base)
base.study = study


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--results', type=Path, required=True)
    parser.add_argument('--environment', type=Path, required=True)
    args = parser.parse_args()
    identity = study.read(args.results / 'identity.json')
    plan = study.read(ROOT / 'plan.json')
    for name, digest in identity['files'].items():
        assert study.sha(ROOT / name) == digest, name
    assert study.sha(ROOT / 'run256.py') == plan['schedule_sha256']
    assert (args.results / 'time-done.json').exists() and (args.results / 'counters-done.json').exists()
    rows = [study.read(p) for p in sorted((args.results / 'timings').glob('*.json'))]
    counters = [study.read(p) for p in sorted((args.results / 'counters').glob('*.json'))]
    assert len(rows) == len(counters) <= plan['max_measured_inputs']
    assert all(r['fingerprint'] == identity['fingerprint'] for r in rows + counters)
    short = [r for r in rows if r['case']['bytes'] == 256]
    controls = [r for r in rows if r['case']['bytes'] != 256]
    assert len(short) <= 33 and len(controls) == 1
    captures = [{**study.read(p), 'capture_file': p.name} for p in sorted((args.results / 'captures').glob('*.json')) if not p.name.endswith('.config.json')]
    data = ROOT / 'data'
    data.mkdir(exist_ok=True)
    for row in rows:
        study.save(ROOT / 'inputs/cases' / (row['case']['id'] + '.json'), row['case'])
    base.pack(data / 'timings.json.gz', {'identity': identity, 'points': rows})
    base.pack(data / 'counters.json.gz', {'identity': identity, 'points': counters})
    base.pack(data / 'captures.json.gz', captures)
    study.save(data / 'selection.json', study.read(args.results / 'selection.json'))
    summary = {'short_inputs': len(short), 'baseline_controls': len(controls), 'native_comparisons': 2 * len(rows),
               'qualified_native_comparisons': sum(s['qualified'] for r in rows for s in r['scopes'].values()),
               'correctness_comparisons': sum(r['correctness_comparisons'] for r in rows),
               'counter_results': sum(len(c['methods']) for c in counters),
               'qualified_counter_results': sum(m['qualified'] for c in counters for m in c['methods'].values()),
               'compiler': 'gcc14', 'date': '2026-11-09'}
    study.save(data / 'summary.json', summary)
    build = study.read(args.environment)['compilers']['gcc14']
    study.save(data / 'build.json', {**{k: v for k, v in build.items() if k not in ['php', 'module', 'build_command']},
                                   'cpu': 'Intel Core i7-13700H', 'logical_cpu': identity['cpu'], 'smt_sibling': identity['sibling']})
    lines = ['# Every 256-byte input and the count-baseline control', '',
             '[Summary](README.md) · [Method](METHOD.md) · [Quality](QUALITY.md)', '',
             'One reference median is shared by both object modes. Relative changes use the displayed medians. † marks a quality issue.', '',
             '| Operation and exact input | Best measured existing, µs | Prepared, µs | One-shot, µs | Paired decisions |',
             '|---|---|---:|---:|---|']
    for row in rows:
        lines.append('| `' + study.OPS[row['case']['operation']] + '`; ' + row['case']['background'] + '; ' + base.input_link(row) + ' | '
            + base.reference(row) + ' | ' + base.native(row, 'prepared') + ' | ' + base.native(row, 'oneshot') + ' | '
            + row['scopes']['prepared']['state'] + ' / ' + row['scopes']['oneshot']['state'] + ' |')
    (ROOT / 'TIMINGS.md').write_text('\n'.join(lines) + '\n')
    lines = ['# Timings: every implementation and A/A control', '',
             '| Input | Implementation | Median, µs | Maximum deviation |', '|---|---|---:|---:|']
    for row in rows:
        for method, value in row['median_us'].items():
            lines.append(f"| {row['case']['id']} | {study.method_name(method, row['case']['operation'])} | {value:.3f} | {100 * row['spread'][method]:.2f}% |")
    (ROOT / 'RECIPES.md').write_text('\n'.join(lines) + '\n')
    quality = ['# Quality checks', '',
        f"{summary['qualified_native_comparisons']} of {summary['native_comparisons']} native timing comparisons passed. The primary two-attempt policy, A/A, spread and sibling-load limits match the parent study.", '',
        'A win requires a paired median below 0.98 and every paired ratio below 1. A loss requires a median above 1.02 and every ratio above 1. Other qualified results are inconclusive.', '',
        '| Input | Mode | Decision | Flags | Measured variability | Paired ratio min–max |', '|---|---|---|---|---|---:|']
    for row in rows:
        for mode, stat in row['scopes'].items():
            detail = base.quality_detail(row, mode, study.read(args.results / 'captures' / row['capture']))
            quality.append(f"| {row['case']['id']} | {mode} | {stat['state']} | {', '.join(stat['flags']) or 'none'} | {detail} | {stat['paired_min']:.4f}–{stat['paired_max']:.4f} |")
    quality += ['', '## Counter checks', '',
                f"{summary['qualified_counter_results']} of {summary['counter_results']} method results passed every 0/N pair. These checks are independent of timing checks; flagged medians remain in COUNTERS with †."]
    quality += ['', '## Opposite directions in time and counters', '',
                'Only comparisons passing timing and both counter checks are listed. Lower time can coexist with more instructions. This table records that observation without attributing a cause.', '',
                '| Input | Mode | Paired elapsed ratio | Cycles ratio | Instructions ratio |', '|---|---|---:|---:|---:|']
    counter_by_id = {c['case']: c for c in counters}
    for row in rows:
        methods = counter_by_id[row['case']['id']]['methods']
        reference = methods[row['reference']]
        for mode in ['prepared', 'oneshot']:
            own = methods[mode]
            if not (row['scopes'][mode]['qualified'] and own['qualified'] and reference['qualified']):
                continue
            elapsed = row['scopes'][mode]['paired_ratio']
            ratios = [own['median'][event] / reference['median'][event] for event in ['cpu_core/cycles/u', 'cpu_core/instructions/u']]
            if any((elapsed < .98 and ratio > 1.02) or (elapsed > 1.02 and ratio < .98) for ratio in ratios):
                quality.append(f"| {row['case']['id']} | {mode} | {elapsed:.3f} | {ratios[0]:.3f} | {ratios[1]:.3f} |")
    (ROOT / 'QUALITY.md').write_text('\n'.join(quality) + '\n')
    lines = ['# Cycles and instructions', '', 'Five alternating 0/N pairs per implementation. † means at least one pair failed quality checks.', '',
             '| Input | Implementation | Cycles/job | Instructions/job |', '|---|---|---:|---:|']
    by_id = {r['case']['id']: r for r in rows}
    for point in counters:
        for method, value in point['methods'].items():
            marker = '' if value['qualified'] else '†'
            lines.append('| ' + point['case'] + ' | ' + study.method_name(method, by_id[point['case']]['case']['operation']) + ' | '
                + f"{value['median']['cpu_core/cycles/u']:.1f}" + marker + ' | ' + f"{value['median']['cpu_core/instructions/u']:.1f}" + marker + ' |')
    (ROOT / 'COUNTERS.md').write_text('\n'.join(lines) + '\n')
    lines = ['# Matcher and Replacer on 256-byte texts', '',
        '9 November 2026. GCC 14.2, Intel Core i7-13700H. Short-text inputs are exactly 256 bytes; a separate 4 KiB control checks the count baseline. Dictionary order and match count stay fixed while N changes.', '',
        '[All inputs](TIMINGS.md) · [Every implementation](RECIPES.md) · [Counters](COUNTERS.md) · [Quality](QUALITY.md) · [Method](METHOD.md) · [Build identity](data/build.json)', '',
        f"{len(short)} short inputs and one 4 KiB count-baseline check. {summary['qualified_native_comparisons']} of {summary['native_comparisons']} native comparisons passed timing quality checks. All selected inputs passed exact-output checks; [overlap-specific baseline checks](data/count-baseline-checks.json) also rejected a deliberately incorrect counting recipe.", '',
        '## What pays on a short text', '']
    one_shot_wins = [r for r in short if r['scopes']['oneshot']['state'] == 'win']
    if not one_shot_wins:
        lines += ['No tested 256-byte input produced a confirmed one-shot win. Faster prepared calls therefore require object reuse to pay for construction on this slice.', '']
    else:
        lines += ['Some one-shot inputs won; their exact configurations remain in the full table.', '']
    winners = []
    changed_winners = []
    for op in study.OPS:
        low, win, check, rev = base.boundary(short, op, 'keys', 'prepared', fixed_bytes=256)
        if win:
            winners.append(win['case']['keys'])
            if check and check['scopes']['prepared']['state'] == 'loss':
                changed_winners.append('`' + study.OPS[op] + '` with ' + str(win['case']['keys']) + ' keys')
    if winners:
        counts = sorted(set(winners))
        description = ' or '.join(map(str, counts))
        lines += ['The smallest tested confirmed prepared wins on the primary text use ' + description + ' keys, depending on the operation. The next table shows the smaller losses and the second-text checks.', '']
    if changed_winners:
        lines += ['The winner changes between texts for ' + '; '.join(changed_winners) + '.', '']
    lines += ['## Prepared: smallest tested winning dictionary', '',
        'The loss and win cells each show the input size, best measured existing time and prepared-object time. These are tested points, not universal key-count thresholds. Intermediate close or flagged observations retain their measured times and relative changes.', '',
        base.boundary_table(short, 'keys', 'prepared', fixed_bytes=256), '',
        '## All five operations with the same 48-key dictionary', '',
        'Prepared excludes construction and destruction; one-shot includes both. Percentages use the single reference median in the row.', '',
        '| Operation | Result | Best measured existing, µs | Prepared, µs | One-shot, µs |', '|---|---|---|---:|---:|']
    for op in study.OPS:
        row = next(r for r in short if r['case']['operation'] == op and r['case']['keys'] == 48 and r['case']['background'] == 'technical'
                   and r['case']['condition'] == ('absent' if op == 'any' else 'single'))
        result = {'any':'false', 'unique':'1 unique key', 'count':'int 1', 'all':'list of 1 MatchResult', 'replace':'1 replacement; output 250 B'}[op]
        lines.append('| [`' + study.OPS[op] + '`](inputs/cases/' + row['case']['id'] + '.json) | ' + result + ' | '
            + base.reference(row) + ' | ' + base.native(row, 'prepared') + ' | ' + base.native(row, 'oneshot') + ' |')
    lines += ['', '## Presence: early, middle and late matches', '',
        'The matching key is #25 of the same 48-key dictionary.', '',
        '| Match starts at byte | Best measured existing, µs | Prepared, µs | One-shot, µs |', '|---:|---|---:|---:|']
    for row in sorted((r for r in short if r['case']['background'] == 'technical' and r['case']['condition'] in ['early','middle','late']),key=lambda r:r['case']['first_offset']):
        lines.append('| [' + str(row['case']['first_offset']) + '](inputs/cases/' + row['case']['id'] + '.json) | '
            + base.reference(row) + ' | ' + base.native(row, 'prepared') + ' | ' + base.native(row, 'oneshot') + ' |')
    control = controls[0]
    lines += ['', '## Counting: 4 KiB baseline crosscheck', '',
        'The additional recipe uses `substr_count()` for keys without self-overlap and a one-byte-advancing `strpos()` loop for the other keys. Preparation of this eligibility map is outside timing. The 4 KiB control has 48 keys and one occurrence.', '',
        '| Best measured existing, µs | Prepared, µs | One-shot, µs |', '|---|---:|---:|',
        '| ' + base.reference(control) + ' | ' + base.native(control, 'prepared') + ' | ' + base.native(control, 'oneshot') + ' |', '',
        'This is a separate baseline check, not a 256-byte observation. Its complete input and every recipe are in [TIMINGS](TIMINGS.md) and [RECIPES](RECIPES.md).', '',
        '## Limits and reproduction', '',
        'The slice tests one dictionary family, two controlled English backgrounds and zero or one occurrence. Values between sampled N are unknown. Short repeated texts favor a warm working set; these are not full-request or production-throughput measurements. † marks a quality issue while retaining the observed time and relative change.', '',
        '[Reproduction](REPRODUCE.md) · [Frozen plan](plan.json) · [Exact observations](data/timings.json.gz) · [All capture attempts](data/captures.json.gz).']
    if control['reference'] == 'string_loop' and control['scopes']['oneshot']['state'] == 'win':
        position = lines.index('## Counting: 4 KiB baseline crosscheck') + 2
        close = abs(control['median_us']['substring_count_loop'] / control['median_us']['string_loop'] - 1) < .02
        lines[position:position] = [('The two PHP count loops are within 2%; one-shot Matcher still wins against both.' if close else 'The extra recipe does not change the 4 KiB conclusion: one-shot Matcher still wins against the measured alternatives.'), '']
    (ROOT / 'README.md').write_text('\n'.join(lines) + '\n')
    print(json.dumps(summary, indent=2))


if __name__ == '__main__':
    main()
