#!/usr/bin/env python3
"""Render the compact-Sunday report from archived measurements."""
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
    languages = dict(en='English', ru='Russian', es='Spanish', ar='Arabic', hi='Hindi',
                     zh='Chinese', ja='Japanese', ko='Korean', emoji='Mixed emoji')
    if key.startswith('banlist12/'):
        _, language, size, state = key.split('/')
        assert state == 'clean'
        return languages[language] + ' moderation ' + size
    return {
        'explode/pipe2/4k': 'Split fields on two pipes',
        'explode/colon2/4k': 'Split fields on `::`',
        'parse-http/body64k': 'Parse HTTP headers',
        'render-template/4k': 'Replace template placeholders',
        'count-template/4k': 'Count `{{order.id}}` slots',
        'boundary/9/absent': '9-byte search (no match)',
        'boundary/31/early': '32-byte early match (text)',
        'boundary/32/early': '32-byte early match (repeated a)',
        'boundary/31/early-corrected': '31-byte early match',
    }[key]
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
    flags = ['--header','--full','--compact-header','--base-name','master','--labels',str(a.out/labels_name)]
    text = subprocess.check_output([str(a.bench_root/'bench'),'table',str(a.out/name),*flags],
        env={**os.environ,'BENCH_PHP':a.php},text=True)
    marker = name+' --header --full --compact-header --base-name master --labels '+labels_name
    matrices += '## '+name[:-5]+'\n\n<!-- bench-table '+marker+' -->\n'+text+'<!-- /bench-table -->\n\n'
(a.out/'cycles.md').write_text('# CPU cycles and instructions\n\nAll changes are relative to master. A call is one complete listed operation; moderation includes all 12 searches. Each matrix includes master-against-master controls for the same cases. Counters were collected separately from elapsed time. Intel counters are diagnostic only because its elapsed A/A failed.\n\n'+matrices)
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
absolute='# Absolute cycles and instructions\n\nCounters come from the separate five-pass series.\n\n'
for cc,rows in groups.items():
    title = 'GCC 15.2' if cc == 'gcc15' else 'Clang 21.1'
    absolute+=f'## {title}\n\n| Case | master cycles | compact cycles | master instr. | compact instr. |\n|---|--:|--:|--:|--:|\n'
    for r in rows:
        c=r['cycles']
        absolute+=f"| {r['label']} | {c['a']:.2f} | {c['b']:.2f} | {c['ai']:.2f} | {c['bi']:.2f} |\n"
    absolute+='\n'
(a.out/'counters.md').write_text(absolute.rstrip()+'\n')
(a.out/'metrics.json').write_text(json.dumps(metrics,indent=2)+'\n')
(a.out/'manifest.json').write_text(json.dumps(dict(base='cf1b5771a76a81b455a8677446daf9c46e1781be',head='8d7babbc364ffcf28dac9777ce807edc9adbb534',elapsed_pairs=len(metrics),raw_sha256={str(p.relative_to(a.data)):hashlib.sha256(p.read_bytes()).hexdigest() for p in raw_paths}),indent=2)+'\n')

def readme_table(cc):
    rows = groups[cc]
    order = [r for r in rows if '/post/clean' in r['case']]
    order += [r for r in rows if '/thread/clean' in r['case']]
    order += [r for r in rows if not r['case'].startswith(('banlist12/', 'boundary/'))]
    for prefix in ['boundary/9/absent', 'boundary/31/early-corrected', 'boundary/31/early @', 'boundary/32/early @']:
        order += [r for r in rows if r['case'].startswith(prefix)]
    assert len(order) == len(rows) == 20 and len({r['case'] for r in order}) == 20
    lines = ['| Case | Bytes | master µs | compact µs | Time Δ | Cycles Δ | Instr. Δ |',
             '|---|--:|--:|--:|--:|--:|--:|']
    for r in order:
        c = r['cycles']
        lines.append(f"| {r['label']} | {r['bytes']} | {r['a_ns']/1000:.4f} | {r['b_ns']/1000:.4f} | {pct(r['delta_time'])} | {pct(c['delta'])} | {pct(100*(c['bi']/c['ai']-1))} |")
    return '\n'.join(lines)

aa_table = ['| Compiler | Before: time Δ | After: time Δ | Noise threshold |',
            '|---|--:|--:|--:|']
for cc, title in [('gcc15', 'GCC 15.2'), ('clang21', 'Clang 21.1')]:
    values = {('before' if 'aa-before-' in r['source'] else 'after'): r['delta_time']
              for r in controls if r['compiler'] == cc}
    floor = max(2.0, *(abs(v) for v in values.values()))
    aa_table.append(f"| {title} | {pct(values['before'])} | {pct(values['after'])} | {floor:.2f}% |")

post_changes = [r['delta_time'] for r in metrics if not r['aa'] and '/post/clean' in r['case']]
template_changes = [r['delta_time'] for r in metrics if not r['aa'] and r['case'].startswith(('render-template/', 'count-template/'))]
losses = [r['delta_time'] for r in groups['gcc15'] if r['label'].startswith('32-byte early')]
intro = (f"On AMD Ryzen 9 5950X with GCC 15 and Clang 21, a 12-term banlist check with no matches takes "
         f"{abs(max(post_changes)):.2f}–{abs(min(post_changes)):.2f}% less time than master; template replacement and counting take "
         f"{abs(max(template_changes)):.2f}–{abs(min(template_changes)):.2f}% less. "
         f"The two 32-byte early-match controls take {min(losses):.2f}–{max(losses):.2f}% more time than master on GCC. "
         "These are costs of individual PHP operations, not whole-request speedups.")

readme = '''# Compact Sunday shift tables

Proposed change to the substring search used by `strpos()`, `str_replace()` and related functions.

Compare [`strpos-compact-sunday-pr`](https://github.com/ArtUkrainskiy/php-src/tree/strpos-compact-sunday-pr)
with [PHP master](https://github.com/php/php-src/tree/master), both PHP 8.7.0-dev.
[Patch](change.patch) · [Measured build metadata](manifest.json).

The patch reduces the Sunday shift table from 1024 to 256 bytes for 9–31-byte
needles (searched substrings) when at least 1024 input bytes remain from the
current search position. On the Sunday path, needles of 32 bytes or more retain
the wide table. The search algorithm and the inline path for needles below
9 bytes or remaining inputs below 1024 bytes are unchanged. The measured changes include
the cost of the new dispatch and differences in code placement.

__SUMMARY__

## Cases

Inputs are generated application fixtures, not production traffic samples.
All moderation inputs are lower-case UTF-8; searches are case-sensitive literal
substrings, without word-boundary matching or normalization inside timing.
There is one post case for each of English, Russian, Spanish, Arabic, Hindi,
Chinese, Japanese, Korean and mixed emoji. Thread timing cases cover English
and Chinese only.

| Case | Input and measured work | Searched substrings |
|---|---|---|
| Moderation post | About 1 KiB of ordinary comments/messages; check all 12 banlist entries, no match | Local phrases such as `spam`, `casino bonus`, plus advertising-domain fragments; 4–55 UTF-8 bytes across languages |
| Moderation thread | About 64 KiB of messages; the same 12-entry absent search | Same phrases as the corresponding post |
| Split fields | About 4 KiB, 170 varied product fields; `explode()` returns every field | Two consecutive pipe characters or `::`, two bytes |
| Parse HTTP headers | Seven headers and a 64 KiB body; find the terminator after 261 header bytes, then parse the headers; body is not parsed | `\\r\\n\\r\\n`, `\\r\\n` and `: ` |
| Replace template placeholders | 4250-byte order-card/email template; replace 68 slots with four values using `str_replace()` | `{{order.id}}`, `{{user.name}}`, `{{tracking.url}}`, `{{support.email}}`; 12–17 bytes |
| Count template slots | Same template; `substr_count()` finds 17 occurrences | `{{order.id}}`, 12 bytes |
| Search controls | Ordinary ASCII filler; an absent 9-byte substring or a 31/32-byte match at byte offset 7 | Text tokens, plus a 32-byte token made of 31 `a` bytes and `b` |

The split operations are `explode('||', $s)` and `explode('::', $s)`.
Exact input sizes are in the tables. [Measured suite](suite.php) · [31-byte control](early31-suite.php) · [Data-label notes](data-notes.md).

## Results

All deltas are relative to master; negative means lower cost. Elapsed time is
the primary comparison. Time columns show medians in microseconds per complete
operation after empty-loop subtraction.
Cycles and instructions come from a separate series: cycle deltas are the median
of five paired ratios; instruction deltas compare the median absolute counts.

For each case, each build runs at least **3 seconds of warmup**, followed by
**10 approximately one-second samples** in one PHP process. There is one paired round. Counters use
five separate 50 ms-target passes. These are preliminary measurements;
ten samples in one process are not ten independent rounds.

A/A compares the identical master binary before and after the timing series.
We use a minimum 2% threshold, increased to the observed A/A variation if larger:

__AA_TABLE__

Changes at or below this threshold are inconclusive in this run.
The threshold is a reporting rule, not a statistical confidence interval.

Intel elapsed results are excluded: identical-binary A/A reached approximately
−50% and +93%. The GCC 13/14 and Clang 18/20 counter tables are diagnostic only.
There is no valid Intel elapsed-performance conclusion.

Delimiter and HTTP rows check unchanged short-search paths; their timing changes
are not attributed to a new search algorithm. The 32-byte early-match controls
exercise the new dispatcher with the wide table.

[Absolute counters](counters.md) · [Compiler counter tables](cycles.md) · [Raw measurements](data/native.tar.gz) · [Reproduce](reproduce.md).

### GCC 15.2

__GCC_TABLE__

### Clang 21.1

__CLANG_TABLE__

Long-thread cycle gains accompany less than 0.5% change in instructions. The
[profiles](profiles.md) do not isolate a single cause; code generation and placement also matter.

## Measurement and limits

Measured 31 October 2026 on Ryzen 9 5950X, CPU 15, SMT sibling 31, performance
governor, turbo enabled. The core was not reserved for the benchmark. Matched release
builds use the `docker` profile; [flags and commands](reproduce.md).

Native ARM, Windows and 32-bit builds have not been tested.

## Correctness and reproduction

All eight tested release binaries pass 699 PHPT string tests each, with 62 skipped.
The full PHP ASan/UBSan build passes 680 tests, with 81 skipped. No run has failures
or warnings. The added PHPT checks 300 input combinations. GCC and Clang sanitizer
runs each compare the extracted matchers with libc on 20,000 seeded random inputs
and 135,460 input-length combinations with guard pages. The verifier detects both
injected faults with each compiler.

[Verification commands and logs](verify/README.md) · [Build and reproduce](reproduce.md) · [Raw native measurements](data/native.tar.gz) · [Unrounded values](metrics.json) · [Hashes](manifest.json).

Tables are generated by [build-report.py](build-report.py).
[check.py](check.py) verifies the archived measurements and displayed values;
`bench report check reports/compact-sunday` checks the report's links and native tables.
'''
readme = readme.replace('__SUMMARY__', intro).replace('__GCC_TABLE__', readme_table('gcc15'))
readme = readme.replace('__CLANG_TABLE__', readme_table('clang21')).replace('__AA_TABLE__', '\n'.join(aa_table))
control_path = a.out / 'search-metrics.json'
if control_path.exists():
    controls_data = json.loads(control_path.read_text())
    stress = next(r for r in controls_data if r['phase'] == 'amd-wide-check' and not r['aa'])
    intro_cost = (f"Searching 4096 `a` bytes for 63 `a` bytes followed by `b` takes {stress['delta_time']:.2f}% more time on GCC 15. "
        "This 64-byte needle uses the existing wide table. A separate profile records more branch misses with nearly unchanged instructions; "
        "the precise cause of the changed branch behavior remains unresolved. [Case and profile](search-controls.md#synthetic-repeated-prefix-regression).\n\n"
        "Elapsed results are AMD-only. Intel elapsed measurements failed A/A controls; native ARM, Windows and 32-bit builds were not tested. "
        "There is one paired elapsed round per comparison. [Reproduce](reproduce.md) · [Raw measurements](data/native.tar.gz).\n\n")
    readme = readme.replace('## Cases', intro_cost + '## Cases', 1)
    extra = ('## Search-shape controls\n\n'
        'The [4096-byte search matrix](search-controls.md) measures absent, early, late and repeated-prefix inputs, '
        'plus repeated `substr_count()`/`str_replace()` and long-needle controls. '
        'There are 21 elapsed cases per compiler, plus a separate GCC 15 repeated-prefix check at 64 bytes. '
        f"That check takes {stress['master_ns']/1000:.4f} → {stress['compact_ns']/1000:.4f} µs, {stress['delta_time']:+.2f}% relative to master. "
        'The full 58-case counter sweep includes needle lengths 8–256.\n\n')
    readme = readme.replace('## Measurement and limits', extra + '## Measurement and limits')
(a.out/'README.md').write_text(readme)
print('Rendered',len(metrics),'elapsed pairs and three counter matrices')
