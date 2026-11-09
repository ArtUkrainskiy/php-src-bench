#!/usr/bin/env python3
"""Render the complete prepared-call grid and reusable summary tables."""
import argparse
import importlib.util
import json
from pathlib import Path

import study

ROOT = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('boundary_render', ROOT.parent / 'report.py')
base = importlib.util.module_from_spec(spec)
spec.loader.exec_module(base)
base.study = study


def matrix(rows, prefix=''):
    return base.prepared_matrix(rows, prefix)


def starting_table(rows, prefix=''):
    return base.prepared_starting_table(rows, prefix)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--results', type=Path, required=True)
    parser.add_argument('--environment', type=Path, required=True)
    args = parser.parse_args()
    assert (args.results / 'time-done.json').exists() and (args.results / 'counters-done.json').exists()
    identity = study.read(args.results / 'identity.json')
    plan = study.read(ROOT / 'plan.json')
    for name, digest in identity['files'].items():
        assert study.sha(ROOT / name) == digest
    assert study.sha(ROOT / 'run_grid.py') == plan['schedule_sha256']
    rows = [study.read(p) for p in sorted((args.results / 'timings').glob('*.json'))]
    counters = [study.read(p) for p in sorted((args.results / 'counters').glob('*.json'))]
    assert len(rows) == len(counters) <= 85
    primary = [r for r in rows if r['case']['background'] == 'technical']
    assert len(primary) == 80
    assert all(r['fingerprint'] == identity['fingerprint'] for r in rows + counters)
    data = ROOT / 'data'
    data.mkdir(exist_ok=True)
    for row in rows:
        study.save(ROOT / 'inputs/cases' / (row['case']['id'] + '.json'), row['case'])
    base.pack(data / 'timings.json.gz', {'identity': identity, 'points': rows})
    base.pack(data / 'counters.json.gz', {'identity': identity, 'points': counters})
    captures = [{**study.read(p), 'capture_file': p.name} for p in sorted((args.results / 'captures').glob('*.json')) if not p.name.endswith('.config.json')]
    base.pack(data / 'captures.json.gz', captures)
    study.save(data / 'selection.json', study.read(args.results / 'selection.json'))
    summary = {'primary_inputs': len(primary), 'validation_inputs': len(rows) - len(primary),
               'mode': 'prepared', 'timing_comparisons': len(rows),
               'qualified_timing_comparisons': sum(r['scopes']['prepared']['qualified'] for r in rows),
               'correctness_comparisons': sum(r['correctness_comparisons'] for r in rows),
               'counter_results': sum(len(c['methods']) for c in counters),
               'qualified_counter_results': sum(m['qualified'] for c in counters for m in c['methods'].values()),
               'compiler': 'gcc14', 'starting_bytes': 128, 'starting_keys': 8}
    study.save(data / 'summary.json', summary)
    build = study.read(args.environment)['compilers']['gcc14']
    study.save(data / 'build.json', {**{k:v for k,v in build.items() if k not in ['php','module','build_command']},
                                   'cpu':'Intel Core i7-13700H', 'logical_cpu':identity['cpu'], 'smt_sibling':identity['sibling']})
    lines = ['# Prepared calls: every length/dictionary combination', '',
             '[Summary](README.md) · [Method](METHOD.md) · [Quality](QUALITY.md)', '',
             'One row is one exact input and one prepared call. Construction and destruction are outside timing. Percentages use the shown medians. † marks failed quality checks.', '']
    for op in study.OPS:
        lines += ['## ' + study.OPS[op], '']
        for size in plan['subject_sizes']:
            lines += [f'<a id="{op}-b{size}"></a>', '### ' + base.size(size), '',
                      '| Keys and exact input | Best measured existing, µs | Prepared, µs | Decision |', '|---|---|---:|---|']
            group = sorted((r for r in primary if r['case']['operation']==op and r['case']['bytes']==size), key=lambda r:r['case']['keys'])
            for row in group:
                label = str(row['case']['keys'])
                if op == 'replace':
                    label += ' keys; replacements: 1; output ' + base.size(len(row['case']['expected']['subject'].encode()))
                lines.append('| [' + label + '](inputs/cases/' + row['case']['id'] + '.json) | '
                    + base.reference(row) + ' | ' + base.native(row,'prepared') + ' | ' + row['scopes']['prepared']['state'].replace('close','inconclusive') + ' |')
            lines += ['']
    lines += ['## Checks on the second text', '', '| Operation and exact input | Best measured existing, µs | Prepared, µs | Decision |', '|---|---|---:|---|']
    for row in rows:
        if row['case']['background']=='technical':
            continue
        lines.append('| `' + study.OPS[row['case']['operation']] + '`; ' + base.input_link(row) + ' | '
            + base.reference(row) + ' | ' + base.native(row,'prepared') + ' | ' + row['scopes']['prepared']['state'].replace('close','inconclusive') + ' |')
    (ROOT/'TIMINGS.md').write_text('\n'.join(lines)+'\n')
    lines = ['# Every implementation and A/A control', '',
             '| Input | Implementation | Median, µs | Maximum deviation |', '|---|---|---:|---:|']
    for row in rows:
        for method, value in row['median_us'].items():
            lines.append(f"| {row['case']['id']} | {study.method_name(method,row['case']['operation'])} | {value:.3f} | {100*row['spread'][method]:.2f}% |")
    (ROOT/'RECIPES.md').write_text('\n'.join(lines)+'\n')
    quality = ['# Quality checks', '',
               f"{summary['qualified_timing_comparisons']} of {summary['timing_comparisons']} prepared comparisons passed. Two attempts at most; keep the first passing capture, otherwise flag the first. All attempts are retained.", '',
               '| Input | Decision | Flags | Measured variability | Paired ratio min–max |', '|---|---|---|---|---:|']
    for row in rows:
        stat=row['scopes']['prepared']
        detail = base.quality_detail(row, 'prepared', study.read(args.results / 'captures' / row['capture']))
        quality.append(f"| {row['case']['id']} | {stat['state']} | {', '.join(stat['flags']) or 'none'} | {detail} | {stat['paired_min']:.4f}–{stat['paired_max']:.4f} |")
    quality += ['', '## Counter quality', '',
                f"{summary['qualified_counter_results']} of {summary['counter_results']} implementation results passed all five 0/N pair checks. These checks are separate from timing quality. Flagged counters are marked †."]
    counter_by_id={c['case']:c for c in counters}
    quality += ['', '## Opposite directions between time and counters', '',
                'Only comparisons passing both sets of checks are listed. Lower time need not mean fewer instructions; no cause is inferred.', '',
                '| Input | Paired elapsed ratio | Cycles ratio | Instructions ratio |', '|---|---:|---:|---:|']
    for row in rows:
        methods=counter_by_id[row['case']['id']]['methods'];own=methods['prepared'];ref=methods[row['reference']]
        if not(row['scopes']['prepared']['qualified'] and own['qualified'] and ref['qualified']):
            continue
        elapsed=row['scopes']['prepared']['paired_ratio']
        ratios=[own['median'][e]/ref['median'][e] for e in ['cpu_core/cycles/u','cpu_core/instructions/u']]
        if any((elapsed<.98 and r>1.02) or (elapsed>1.02 and r<.98) for r in ratios):
            quality.append(f"| {row['case']['id']} | {elapsed:.3f} | {ratios[0]:.3f} | {ratios[1]:.3f} |")
    (ROOT/'QUALITY.md').write_text('\n'.join(quality)+'\n')
    lines=['# Cycles and instructions', '', 'Five alternating 0/N pairs per implementation. † means at least one pair failed quality checks.', '',
           '| Input | Implementation | Cycles/job | Instructions/job |', '|---|---|---:|---:|']
    by_id={r['case']['id']:r for r in rows}
    for point in counters:
        for method,result in point['methods'].items():
            marker='' if result['qualified'] else '†'
            lines.append('| '+point['case']+' | '+study.method_name(method,by_id[point['case']]['case']['operation'])+' | '
                +f"{result['median']['cpu_core/cycles/u']:.1f}"+marker+' | '+f"{result['median']['cpu_core/instructions/u']:.1f}"+marker+' |')
    (ROOT/'COUNTERS.md').write_text('\n'.join(lines)+'\n')
    lines=['# Prepared objects: dictionary size by text length', '',
           'GCC 14.2, Intel Core i7-13700H. All native objects are created before timing. Each result includes the call, result creation, consumption and release.', '',
           '[General break-even report](../README.md) · [Every comparison](TIMINGS.md) · [Every implementation](RECIPES.md) · [Counters](COUNTERS.md) · [Quality](QUALITY.md) · [Method](METHOD.md)', '',
           f"80 primary comparisons and {summary['validation_inputs']} second-text checks; {summary['qualified_timing_comparisons']} passed timing quality checks. All inputs passed {summary['correctness_comparisons']} exact-output comparisons before timing; wrong expected output was rejected.", '',
           '## Prepared time and observed advantage at every dictionary size', '',
           'Each entry is key count: prepared time in µs (observed change against the best measured existing method). Every cell tests N=8, 16, 32, 48. Negative means faster; positive means slower. † marks a quality issue; its measured change is still shown. Click an entry for all reference times. [Quality details](QUALITY.md) quantify sample spread and A/A deviation.', '',
           matrix(rows), '', '## Starting point: 128 B and 8 keys', '',
           'Presence has no matches. Other operations have one occurrence; replacement returns 122 bytes.', '',
           starting_table(rows), '', '## Limits and reproduction', '',
           'The grid uses one real dictionary family and controlled prefixes of one primary background. The smallest confirmed winning N at 128 bytes is checked on a second background; all five checks won. Those checks are listed in the full timing table. This is a prepared-call comparison, not the number of calls needed to amortize construction.', '',
           '[Reproduce](REPRODUCE.md) · [Frozen plan](plan.json) · [Exact points](data/timings.json.gz) · [Raw captures](data/captures.json.gz).']
    (ROOT/'README.md').write_text('\n'.join(lines)+'\n')
    print(json.dumps(summary,indent=2))


if __name__=='__main__':
    main()
