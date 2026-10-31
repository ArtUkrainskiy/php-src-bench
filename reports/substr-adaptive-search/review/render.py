#!/usr/bin/env python3
"""Render supplemental native time/counter series without modifying the frozen report."""
import argparse
from collections import defaultdict
import hashlib
import json
import os
from pathlib import Path
import re
import statistics as st
import subprocess

p = argparse.ArgumentParser(description=__doc__)
p.add_argument('--bench-root', type=Path, required=True)
p.add_argument('--php', required=True)
p.add_argument('--data', type=Path, required=True)
p.add_argument('--out', type=Path, required=True)
p.add_argument('--partial', action='store_true')
a = p.parse_args()
a.out.mkdir(parents=True, exist_ok=True)
if not a.partial:
    assert (a.data / 'measurements-complete').exists()
    assert (a.data / 'extra-complete').exists()
    assert (a.data / 'confirm-complete').exists()
events = json.loads((a.data / 'events.json').read_text())
paths = [a.data / (v['name'] + '.json') for v in events]
assert len(paths) == len(set(paths))
php_code = "require $argv[1].'/lib/stats.php';require $argv[1].'/lib/render.php';$out=[];foreach(array_slice($argv,2) as $path){$d=json_decode(file_get_contents($path),true);$out[]=result_rows($d,['A','B'],true,$d['config']['perf']);}echo json_encode($out);"
native = json.loads(subprocess.check_output([a.php, '-n', '-r', php_code, str(a.bench_root), *map(str, paths)], text=True))
cycles = {}
for path in [a.data / 'cycles.json', a.data / 'extra-cycles.json']:
    if not path.exists(): continue
    data = json.loads(path.read_text())
    if a.partial and not data['complete']: continue
    assert data['complete'] and not data['warnings'] and not data['marks'], path
    rows = defaultdict(lambda: defaultdict(list))
    for group, side, key, bc, bi, ec, ei in data['rows']:
        rows[group, key][side].append(((bc - ec) / data['cases'][key]['n'], (bi - ei) / data['cases'][key]['n']))
    for (group, key), values in rows.items():
        assert len(values['a']) == len(values['b']) == 3
        cycles[group, key] = dict(a=st.median(c for c, i in values['a']), b=st.median(c for c, i in values['b']),
            delta=100 * (st.median(b[0] / aa[0] for aa, b in zip(values['a'], values['b'])) - 1),
            ai=st.median(i for c, i in values['a']), bi=st.median(i for c, i in values['b']))
metrics = []
groups = defaultdict(list)
aa = []
for event, path, rr in zip(events, paths, native):
    data = json.loads(path.read_text())
    assert data['config']['target_ms'] == data['config']['warmup_ms'] == 1000
    assert data['config']['rounds'] == 4 and data['config']['samples'] == 1
    key = event['case']
    assert list(data['cases']) == [key] and len(rr) == 1
    x, y = (data['cases'][key]['sides'][side] for side in ['A', 'B'])
    assert x['input_hash'] == y['input_hash'] and x['output_hash'] == y['output_hash']
    row = rr[0]
    log_path = path.with_suffix('.log')
    idle_timeout = log_path.exists() and 'measuring anyway' in log_path.read_text()
    am, bm = [row['stats'][s]['median'] for s in ['A', 'B']]
    assert abs(am - (st.median(v[0] for v in x['rounds']) - st.median(x['loop_ns']))) < 1e-8
    assert abs(bm - (st.median(v[0] for v in y['rounds']) - st.median(y['loop_ns']))) < 1e-8
    cc = 'clang21' if 'clang21' in event['name'] else 'gcc15'
    if event['a'] == event['b']:
        kind = 'aa'
    elif event['b'].startswith('review-no-gram4'):
        kind = 'nogram'
    elif event['b'].startswith('review-scalar'):
        kind = 'scalar'
    else:
        kind = 'stock'
    cycle = cycles.get((kind + '-' + cc, key))
    record = dict(source=path.name, case=key, compiler=cc, comparison=kind,
                  a=event['a'], b=event['b'], a_ns=am, b_ns=bm, delta_time=100 * (bm / am - 1),
                  a_instructions=x['instructions'], b_instructions=y['instructions'],
                  delta_instructions=100 * (y['instructions'] / x['instructions'] - 1),
                  a_spread=row['stats']['A']['spread_pct'], b_spread=row['stats']['B']['spread_pct'],
                  native_verdict=row['verdict'], disturbed=row.get('disturbed', False) or idle_timeout,
                  idle_wait_timeout=idle_timeout, cycles=cycle)
    metrics.append(record)
    if kind == 'aa': aa.append(record)
    elif not event['name'].startswith('smoke-'): groups[kind, cc].append(record)

def pct(value):
    return '—' if value is None else f'{value:+.2f}%'

captions = {'stock': ('Stock', 'ca89'), 'nogram': ('ca89', 'No gram4'), 'scalar': ('ca89', 'Scalar')}
table = '# Supplemental route measurements\n\nNegative deltas mean that B costs less than A. Elapsed time is primary; counters are diagnostic.\n\n'
detail = '# Absolute diagnostic counters\n\nCycles come from a separate three-pass native `bench compare`; instructions below come from the one-second elapsed series.\n\n'
for (kind, cc), records in groups.items():
    left, right = captions[kind]
    title = f'{cc}: {left} → {right}'
    table += f'## {title}\n\n| Case | A, µs | B, µs | Δ time | Δ cycles | Δ instr. | Spread A/B | Result |\n|---|--:|--:|--:|--:|--:|--:|---|\n'
    detail += f'## {title}\n\n| Case | A cycles | B cycles | A instr. | B instr. |\n|---|--:|--:|--:|--:|\n'
    for r in records:
        label = r['case'].split(' @ ')[0].replace('|', '\\|')
        if r['source'].startswith('confirm-'): label += ' (repeat)'
        c = r['cycles']
        verdict = {'+': 'Faster', '-': 'Slower', '~': 'Unclear', '?': 'Unclear'}.get(r['native_verdict'], str(r['native_verdict']))
        if r['disturbed'] or max(r['a_spread'], r['b_spread']) > 5: verdict = 'Noise'
        table += f"| {label} | {r['a_ns']/1000:.4f} | {r['b_ns']/1000:.4f} | {pct(r['delta_time'])} | {pct(c['delta'] if c else None)} | {pct(r['delta_instructions'])} | {r['a_spread']:.1f}% / {r['b_spread']:.1f}% | {verdict} |\n"
        detail += '| ' + ' | '.join([label, f"{c['a']:.2f}" if c else '—', f"{c['b']:.2f}" if c else '—', f"{r['a_instructions']:.2f}", f"{r['b_instructions']:.2f}"]) + ' |\n'
    table += '\n'
    detail += '\n'
table += '## Elapsed A/A controls\n\n| Series | Case | A, µs | B, µs | Δ time | Spread A/B |\n|---|---|--:|--:|--:|--:|\n'
for r in aa:
    table += f"| {r['source'][:-5]} | {r['case'].split(' @ ')[0]} | {r['a_ns']/1000:.4f} | {r['b_ns']/1000:.4f} | {pct(r['delta_time'])} | {r['a_spread']:.1f}% / {r['b_spread']:.1f}% |\n"
(a.out / 'time.md').write_text(table)
(a.out / 'counters.md').write_text(detail)
(a.out / 'metrics.json').write_text(json.dumps(metrics, indent=2) + '\n')
(a.out / 'manifest.json').write_text(json.dumps(dict(native_series=len(paths), metrics=len(metrics),
    files={p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}, partial=a.partial), indent=2) + '\n')
if not a.partial:
    views = a.out / 'cycle-views'
    views.mkdir(exist_ok=True)
    doc = '# Separate cycle and instruction diagnostics\n\n'
    doc += 'These are presentation views of the two original series, not separate experiments. All groups use the original iteration counts calibrated from ca89 with GCC 15 (50 ms target, three passes). Cycle A/A always uses ca89 with GCC 15. Negative deltas mean less cost for B. These counters are separate from elapsed timing.\n\n'
    for source in ['cycles.json', 'extra-cycles.json']:
        data = json.loads((a.data / source).read_text())
        data['machine_warnings'] = [re.sub(r'/tmp/php[-_][^/\s]+/tools/bench', 'bench', v) for v in data['machine_warnings']]
        (a.out / source).write_text(json.dumps(data, indent=2) + '\n')
        for kind in ['nogram', 'scalar', 'stock']:
            view = dict(data)
            names = {g['name'] for g in data['groups'] if g['name'] in ['aa', 'aa2'] or g['name'].startswith(kind + '-')}
            view['groups'] = [g for g in data['groups'] if g['name'] in names]
            view['rows'] = [r for r in data['rows'] if r[0] in names]
            view['presentation_view'] = dict(source=source, selected_groups=sorted(names))
            name = ('main' if source == 'cycles.json' else 'periodic') + '-' + kind + '.json'
            path = views / name
            path.write_text(json.dumps(view, indent=2) + '\n')
            base_label = 'Stock' if kind == 'stock' else 'ca89'
            flags = ['--full', '--compact-header', '--base-name', base_label]
            value = subprocess.check_output([str(a.bench_root / 'bench'), 'table', str(path), *flags],
                env={**os.environ, 'BENCH_PHP': a.php}, text=True)
            relative = 'cycle-views/' + name
            left, right = captions[kind]
            doc += f'## {name[:-5]}: {left} → {right}\n\n<!-- bench-table {relative} ' + ' '.join(flags) + ' -->\n'
            doc += value + '<!-- /bench-table -->\n\n'
    (a.out / 'cycles.md').write_text(doc.rstrip() + '\n')
print(len(metrics), 'native elapsed rows rendered')
