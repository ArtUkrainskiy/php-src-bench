#!/usr/bin/env python3
"""Render the independent compact-Sunday screen from native records."""
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
p.add_argument('--data', type=Path, required=True)
p.add_argument('--out', type=Path, required=True)
p.add_argument('--bench-root', type=Path, required=True)
p.add_argument('--php', required=True)
a = p.parse_args(); a.bench_root = a.bench_root.resolve(); a.out.mkdir(parents=True, exist_ok=True)
raw_paths = []
for folder in ['amd', 'early31']:
    for path in sorted((a.data / folder).glob('*.json')):
        d = json.loads(path.read_text())
        if 'sides' in d and 'cases' in d: raw_paths.append(path)
assert len(raw_paths) == 44, len(raw_paths)
code = "require $argv[1].'/lib/stats.php';require $argv[1].'/lib/render.php';$r=[];foreach(array_slice($argv,2) as $p){$d=json_decode(file_get_contents($p),true);$r[]=result_rows($d,['A','B'],true,false);}echo json_encode($r);"
native = json.loads(subprocess.check_output([a.php, '-n', '-r', code, str(a.bench_root), *map(str, raw_paths)], text=True))
counter = {}
matrices = ''
labels = {}
def label(key):
    key = key.split(' @ ')[0]
    if key == 'boundary/31/early': return 'boundary/32/early-text (original label: 31)'
    return key.replace('-corrected', '')
cycle_sources = [('amd/cycles.json', 'amd-cycles.json'), ('intel-counters/cycles.json', 'intel-cycles.json'), ('early31/cycles.json', 'early31-cycles.json')]
for relative, name in cycle_sources:
    data = json.loads((a.data / relative).read_text())
    assert data['complete'] and not data['warnings'] and not data['marks'], relative
    for key in data['cases']: labels[key] = label(key)
    values = defaultdict(lambda: defaultdict(list))
    for group, side, key, bc, bi, ec, ei in data['rows']:
        values[group, key][side].append(((bc - ec) / data['cases'][key]['n'], (bi - ei) / data['cases'][key]['n']))
    for (group, key), sides in values.items():
        x, y = sides['a'], sides['b']; assert len(x) == len(y) == 5
        counter[name, group, key] = dict(a=st.median(c for c,i in x), b=st.median(c for c,i in y),
            ai=st.median(i for c,i in x), bi=st.median(i for c,i in y),
            delta=100*(st.median(b[0]/aa[0] for aa,b in zip(x,y))-1))
    data = json.loads(re.sub(r'/(?:tmp|home)/[^\s\"\\)]+', lambda m: '<recorded-path>/' + Path(m[0]).name, json.dumps(data)))
    (a.out / name).write_text(json.dumps(data, indent=2) + '\n')
for relative, name in cycle_sources:
    data = json.loads((a.out/name).read_text())
    labels_name = name[:-5] + '-labels.txt'
    (a.out/labels_name).write_text(''.join(k+'='+labels[k]+'\n' for k in data['cases']))
    flags = ['--header','--full','--compact-header','--base-name','Stock','--labels',str(a.out/labels_name)]
    text = subprocess.check_output([str(a.bench_root/'bench'),'table',str(a.out/name),*flags],
        env={**os.environ,'BENCH_PHP':a.php},text=True)
    marker = name+' --header --full --compact-header --base-name Stock --labels '+labels_name
    matrices += '## '+name[:-5]+'\n\n<!-- bench-table '+marker+' -->\n'+text+'<!-- /bench-table -->\n\n'
(a.out/'cycles.md').write_text('# Separate hardware-counter series\n\nIntel is diagnostic only: its elapsed A/A failed. Every matrix includes same-row cycle A/A. These are separate measurements from the elapsed series; they do not establish exact simultaneous IPC.\n\n'+matrices)
metrics = []
groups = defaultdict(list); controls = []
for path, rr in zip(raw_paths,native):
    d=json.loads(path.read_text()); assert len(rr)==1
    cfg=d['config']; assert (cfg['rounds'],cfg['samples'],cfg['target_ms'],cfg['warmup_ms'])==(1,10,1000,3000)
    key=next(iter(d['cases'])); case=d['cases'][key]; x,y=(case['sides'][z] for z in ['A','B'])
    assert x['input_hash']==y['input_hash'] and x['output_hash']==y['output_hash']
    cc='clang21' if 'clang21' in d['sides']['A']['name'] else 'gcc15'
    aa=d['sides']['A']['name']==d['sides']['B']['name']
    assert d['sides']['A']['build']['commit']=='cf1b5771a76a81b455a8677446daf9c46e1781be'
    assert d['sides']['B']['build']['commit']==('cf1b5771a76a81b455a8677446daf9c46e1781be' if aa else '8d7babbc364ffcf28dac9777ce807edc9adbb534')
    am,bm=(rr[0]['stats'][z]['median'] for z in ['A','B'])
    assert abs(am-(st.median(x['rounds'][0])-st.median(x['loop_ns'])))<1e-8
    assert abs(bm-(st.median(y['rounds'][0])-st.median(y['loop_ns'])))<1e-8
    samples={z:[t-st.median(case['sides'][z]['loop_ns']) for t in case['sides'][z]['rounds'][0]] for z in ['A','B']}
    log_path=path.with_suffix('.log')
    if not log_path.exists(): log_path=path.parent/(cc+'.log')
    idle='measuring anyway' in log_path.read_text()
    noisy=idle or any(max(v)/min(v)>1.1 for v in samples.values())
    noisy=noisy or max(rr[0]['stats'][z]['spread_pct'] for z in ['A','B'])>5
    source='early31-cycles.json' if path.parent.name=='early31' else 'amd-cycles.json'
    c=None if aa else counter.get((source,cc,key))
    record=dict(source=str(path.relative_to(a.data)),log=str(log_path.relative_to(a.data)),compiler=cc,case=key,label=label(key),bytes=case['input_len'],
        aa=aa,a_ns=am,b_ns=bm,delta_time=100*(bm/am-1),cycles=c,noisy=noisy,idle_wait_timeout=idle,
        a_min=min(samples['A']),a_max=max(samples['A']),b_min=min(samples['B']),b_max=max(samples['B']))
    metrics.append(record)
    (controls if aa else groups[cc]).append(record)
def pct(n): return f'{n:+.2f}%'
tables='# Elapsed time: stock → compact Sunday\n\nOne paired round, ten approximately one-second samples per version after at least three seconds warmup. Samples share one PHP process per version. Deltas are descriptive; this is not four independent paired rounds. Negative means lower cost.\n\n'
absolute='# Absolute cycles and instructions\n\nCounters come from the separate five-pass series.\n\n'
for cc,rows in groups.items():
    observed_aa=max(abs(r['delta_time']) for r in controls if r['compiler']==cc)
    floor=max(2.0,observed_aa)
    tables+=f'## {cc}\n\nObserved A/A envelope: {observed_aa:.2f}%. Interpretation floor: {floor:.2f}%.\n\n| Case | Bytes | Stock µs | Compact µs | Δ time | Δ cycles | Δ instr. | Quality |\n|---|--:|--:|--:|--:|--:|--:|---|\n'
    absolute+=f'## {cc}\n\n| Case | Stock cycles | Compact cycles | Stock instr. | Compact instr. |\n|---|--:|--:|--:|--:|\n'
    for r in rows:
        c=r['cycles']; qual='Noise' if r['noisy'] else ('Near A/A' if abs(r['delta_time'])<=floor else 'Observed')
        di=100*(c['bi']/c['ai']-1)
        tables+=f"| {r['label']} | {r['bytes']} | {r['a_ns']/1000:.4f} | {r['b_ns']/1000:.4f} | {pct(r['delta_time'])} | {pct(c['delta'])} | {pct(di)} | {qual} |\n"
        absolute+=f"| {r['label']} | {c['a']:.2f} | {c['b']:.2f} | {c['ai']:.2f} | {c['bi']:.2f} |\n"
    tables+='\n'; absolute+='\n'
tables+='## Elapsed A/A\n\n| Source | Compiler | A ns | B ns | Δ time | Quality |\n|---|---|--:|--:|--:|---|\n'
for r in controls: tables+=f"| {r['source']} | {r['compiler']} | {r['a_ns']:.3f} | {r['b_ns']:.3f} | {pct(r['delta_time'])} | {'Noise' if r['noisy'] else 'Observed'} |\n"
(a.out/'time.md').write_text(tables); (a.out/'counters.md').write_text(absolute)
(a.out/'metrics.json').write_text(json.dumps(metrics,indent=2)+'\n')
(a.out/'manifest.json').write_text(json.dumps(dict(base='cf1b5771a76a81b455a8677446daf9c46e1781be',head='8d7babbc364ffcf28dac9777ce807edc9adbb534',elapsed_pairs=len(metrics),raw_sha256={str(p.relative_to(a.data)):hashlib.sha256(p.read_bytes()).hexdigest() for p in raw_paths}),indent=2)+'\n')
print('Rendered',len(metrics),'elapsed pairs and three counter matrices')
