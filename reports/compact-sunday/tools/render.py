#!/usr/bin/env python3
"""Regenerate report tables from exported elapsed observations and native counter series."""
import argparse
import hashlib
import json
from pathlib import Path
import re
import statistics as st

p = argparse.ArgumentParser(description=__doc__)
p.add_argument('--check', action='store_true', help='fail if generated Markdown differs')
a = p.parse_args()
root = Path(__file__).resolve().parents[1]
data = root / 'data'
outputs = {}
catalog = {}
for entry in json.loads((root / 'corpus/index.json').read_text())['suites']:
    for case in json.loads((root / 'corpus' / entry['file']).read_text())['cases']:
        catalog[case['name'] + ' @ ' + case['input']] = dict(case, suite=entry['name'])
for name, digest in json.loads((data / 'sha256.json').read_text()).items():
    assert hashlib.sha256((data / name).read_bytes()).hexdigest() == digest, name


def elapsed(record, key):
    case = record['cases'][key]
    sides = {}
    for side in ['A', 'B']:
        values = case['sides'][side]
        assert len(values['rounds']) == len(values['loop_ns']) == 5
        corrected = [[value - empty for value in samples]
                     for samples, empty in zip(values['rounds'], values['loop_ns'])]
        medians = [st.median(samples) for samples in corrected]
        assert min(medians) > 0
        sides[side] = {'ns': st.median(medians), 'rounds': medians,
                       'spread': 100 * (max(medians) / min(medians) - 1),
                       'mad': [100 * 1.4826 * st.median(abs(v - st.median(run)) for v in run) / st.median(run)
                               for run in corrected]}
    for field in ['input_hash', 'output_hash']:
        assert len(case['sides']['A'][field]) == 1
        assert case['sides']['A'][field] == case['sides']['B'][field]
    deltas = [100 * (b / a - 1) for a, b in zip(sides['A']['rounds'], sides['B']['rounds'])]
    flags = [side + ': process spread >10%' for side in sides if sides[side]['spread'] > 10]
    flags += [side + ': sample MAD >5%' for side in sides if max(sides[side]['mad']) > 5]
    return dict(a=sides['A']['ns'], b=sides['B']['ns'], delta=st.median(deltas),
                low=min(deltas), high=max(deltas), flags=flags)


counter = {}
for file in sorted((data / 'counters').glob('*.json')):
    series = json.loads(file.read_text())
    assert series['complete'] and not series['marks'] and not series['warnings']
    machine = 'AMD' if file.name.startswith('amd-') else 'Intel'
    grouped = {}
    for group, side, key, cycles, instructions, empty_cycles, empty_instructions in series['rows']:
        n = series['cases'][key]['n']
        grouped.setdefault((group, key), {}).setdefault(side, []).append(
            ((cycles - empty_cycles) / n, (instructions - empty_instructions) / n))
    for (group, key), sides in grouped.items():
        if group not in ['gcc15', 'clang21', 'gcc13', 'gcc14', 'clang18', 'clang20']:
            continue
        assert len(sides['a']) == len(sides['b']) == 5
        dc = [100 * (b[0] / x[0] - 1) for x, b in zip(sides['a'], sides['b'])]
        di = [100 * (b[1] / x[1] - 1) for x, b in zip(sides['a'], sides['b'])]
        k = machine, group, key
        assert k not in counter, k
        counter[k] = dict(cycles=st.median(dc), instructions=st.median(di), source=file.name,
                          a_cycles=st.median(v[0] for v in sides['a']),
                          b_cycles=st.median(v[0] for v in sides['b']),
                          a_instructions=st.median(v[1] for v in sides['a']),
                          b_instructions=st.median(v[1] for v in sides['b']))

rows = []
repeats = []
for label in ['amd', 'intel', 'intel-extensions']:
    machine = 'AMD' if label == 'amd' else 'Intel'
    indexed = {}
    for record in json.loads((data / ('elapsed-' + label + '.json')).read_text()):
        e = record['event']; key = e['case']; cc = e['compiler']
        r = dict(elapsed(record, key), case=key, compiler=cc, machine=machine,
                 aa=e['aa'], aa_variant=e['aa_variant'], source=e['tag'],
                 stage=e['stage'], metadata=catalog[key], date=record['date'], capture=label)
        if not r['aa']:
            r['counter'] = counter[machine, cc, key]
        rows.append(r)
        indexed[e['tag'] + '.json'] = r
    for record in json.loads((data / ('repeats-' + label + '.json')).read_text()):
        j = record['job']
        old = indexed.get(j['original'])
        repeats.append(dict(elapsed(record, j['case']), case=j['case'], compiler=j['compiler'],
                            machine=machine, original=old, source=j['tag'], date=record['date']))
ab = [r for r in rows if not r['aa']]
assert len(ab) == len(counter) == 1206 and len(repeats) == 71
lookup = {(r['machine'], r['compiler'], r['case'].split(' @ ')[0]): r for r in ab}
order = [('AMD', 'gcc15'), ('AMD', 'clang21'), ('Intel', 'gcc13'), ('Intel', 'gcc14'),
         ('Intel', 'clang18'), ('Intel', 'clang20')]
selected = []
for lang in ['en', 'ru', 'zh']:
    for state in ['absent', 'start', 'middle', 'end']:
        selected.append((f'moderation/medium/{lang}/{state}', f'Moderation {lang.upper()}, 4 KiB, {state}'))
for lang in ['en', 'ru', 'zh']:
    selected.append((f'moderation/long/{lang}/absent', f'Moderation {lang.upper()}, 64 KiB, absent'))
for state in ['absent', 'start', 'middle', 'end']:
    selected.append((f'strpos/en/{state}', f'Order ID: strpos, 4 KiB, {state}'))
selected += [('strstr/en/middle', 'Email: strstr, 4 KiB, middle'),
             ('substr_count/en/repeated', 'Placeholder: substr_count, 17 matches'),
             ('str_replace/en/repeated', 'Placeholder: str_replace, 17 matches'),
             ('documents/ireplace/receipt/equal', 'HTML receipt: str_ireplace, equal length'),
             ('strtr/en/repeated', 'Placeholder: single-key strtr, 17 matches'),
             ('documents/explode/mail_receipt/all', 'MIME receipt: explode, all parts'),
             ('documents/stream/mail_delivery/closing', 'MIME delivery: stream_get_line'),
             ('documents/search/log_long/absent', 'JSON log: strpos, 68,022 B, absent'),
             ('documents/search/support/present', 'HTML support: strpos, 2,475 B, present')]
assert len(selected) == 28
summary = '| Case | Master µs¹ | AMD GCC15 | AMD Clang21 | Intel GCC13 | Intel GCC14 | Intel Clang18 | Intel Clang20 |\n'
summary += '|---|---:|---:|---:|---:|---:|---:|---:|\n'
for key, label in selected:
    primary = lookup['AMD', 'gcc15', key]
    summary += f"| {label} | {primary['a']/1000:.4f} | "
    summary += ' | '.join(f"{lookup[m, cc, key]['delta']:+.2f}%" + ('†' if lookup[m, cc, key]['flags'] else '') for m, cc in order) + ' |\n'

confirmed = [r for r in repeats if r['original'] and not r['original']['aa']
             and r['original']['stage'] in ['product', 'extensions'] and r['original']['delta'] > 3]
assert len(confirmed) == 7 and all(r['low'] > 0 for r in confirmed)
regressions = '| Intel case | Compiler | Primary Δ time | Repeat Δ time |\n|---|---|---:|---:|\n'
for r in confirmed:
    regressions += f"| `{r['case'].split(' @ ')[0]}` | {r['compiler']} | {r['original']['delta']:+.2f}% | {r['delta']:+.2f}% |\n"


def table(group):
    text = '| Case | Master µs | Compact µs | Δ time | Δ time min | Δ time max | Δ cycles | Δ instructions |\n'
    text += '|---|---:|---:|---:|---:|---:|---:|---:|\n'
    for r in group:
        c = r['counter']
        text += f"| `{r['case'].split(' @ ')[0]}`" + (' †' if r['flags'] else '')
        text += f" | {r['a']/1000:.4f} | {r['b']/1000:.4f} | {r['delta']:+.2f}% | {r['low']:+.2f}% | {r['high']:+.2f}% | {c['cycles']:+.2f}% | {c['instructions']:+.2f}% |\n"
    return text + '\n'


for stage, filename, title in [('product', 'product.md', 'All core application cases'),
                                ('extensions', 'extensions.md', 'All extension cases'),
                                ('controls', 'controls.md', 'Inline and diagnostic controls')]:
    text = '# ' + title + '\n\n[Report and interpretation](../README.md). Primary cohort only; no substitution from repeats.\n\n'
    text += 'Negative = less elapsed time, cycles or instructions. Time is µs per whole PHP operation; min/max are paired observed extrema, not confidence limits. † flags sample MAD >5% or process spread >10%; see [replications](repeats.md).\n\n'
    text += 'Absolute counts for both sides are in [CPU counts](cpu.md). Native paired ranges are in [AMD](counters-amd.md), [Intel core](counters-intel.md) and [Intel extensions](counters-intel-extensions.md).\n\n'
    relevant = [r for r in ab if r['stage'] == stage]
    for api in dict.fromkeys(r['metadata']['api'] for r in relevant):
        text += '## ' + api + '\n\n'
        for machine, cc in order:
            group = [r for r in relevant if r['metadata']['api'] == api and (r['machine'], r['compiler']) == (machine, cc)]
            if group:text += '### ' + machine + ' ' + cc + '\n\n' + table(group)
    outputs['tables/' + filename] = text

text = '# Replication cohort\n\n[Interpretation](../README.md). These fresh five-pair measurements supplement the primary cohort; they do not replace it. Selection: process spread >10%, sample MAD >5%, A/A median outside ±2%, or application median regression >3%. Two additional 64-byte prefix controls use the two-argument strpos call. Min/max are observed paired extrema. † marks remaining noise in the replication itself. The comparison column explicitly distinguishes master/compact A/B from master/master or compact/compact A/A; A and B times refer to those named sides.\n\n'
for machine, cc in order:
    text += f'## {machine} {cc}\n\n'
    text += '| Case | A / B | Primary Δ time | Repeat A µs | Repeat B µs | Repeat Δ time | Min Δ | Max Δ |\n|---|---|---:|---:|---:|---:|---:|---:|\n'
    for r in repeats:
        if (r['machine'], r['compiler']) != (machine, cc):continue
        old = f"{r['original']['delta']:+.2f}%" if r['original'] else 'separate call shape'
        comparison = 'master / compact'
        if r['original'] and r['original']['aa']:
            variant = 'master' if r['original']['aa_variant'] == 'base' else 'compact'
            comparison = variant + ' / ' + variant
        text += f"| `{r['case'].split(' @ ')[0]}`" + (' †' if r['flags'] else '') + f" | {comparison} | {old} | {r['a']/1000:.4f} | {r['b']/1000:.4f} | {r['delta']:+.2f}% | {r['low']:+.2f}% | {r['high']:+.2f}% |\n"
    text += '\n'
outputs['tables/repeats.md'] = text
text = '# Positive primary time deltas\n\n[Interpretation](../README.md). Every positive primary median is listed, including tiny changes and noisy observations. A positive median alone does not establish a regression. Repeats, when selected by the stated rule, are in [repeats.md](repeats.md). Controls are separate from application results.\n\n'
for stage in ['product', 'extensions', 'controls']:
    text += '## ' + stage + '\n\n'
    for machine, cc in order:
        group = [r for r in ab if r['stage'] == stage and r['delta'] > 0 and (r['machine'], r['compiler']) == (machine, cc)]
        if group:text += f'### {machine} {cc}\n\n' + table(group)
outputs['tables/regressions.md'] = text
text = '# Absolute CPU counts\n\n[Interpretation](../README.md). Separate counter cohort: median cycles and retired instructions per whole PHP operation after empty-loop subtraction. Each delta is the median of paired candidate/master ratios, not necessarily the ratio of the two displayed medians. Time is measured in a different cohort. Native pass ranges and controls: [AMD](counters-amd.md), [Intel core](counters-intel.md), [Intel extensions](counters-intel-extensions.md).\n\n'
for machine, cc in order:
    text += f'## {machine} {cc}\n\n'
    for stage in ['product', 'extensions', 'controls']:
        text += '### ' + stage + '\n\n'
        text += '| Case | Master cycles | Compact cycles | Δ cycles | Master instructions | Compact instructions | Δ instructions |\n|---|---:|---:|---:|---:|---:|---:|\n'
        for r in ab:
            if (r['machine'], r['compiler'], r['stage']) != (machine, cc, stage):continue
            c = r['counter']
            text += f"| `{r['case'].split(' @ ')[0]}` | {c['a_cycles']:.3f} | {c['b_cycles']:.3f} | {c['cycles']:+.2f}% | {c['a_instructions']:.3f} | {c['b_instructions']:.3f} | {c['instructions']:+.2f}% |\n"
        text += '\n'
outputs['tables/cpu.md'] = text
text = '# A/A controls\n\n[Interpretation](../README.md). Each row compares one unchanged binary with itself. This tests run-to-run variation; it does not measure compiler-to-compiler differences or prove immunity to code layout. The table shows elapsed-time controls; native counter controls accompany every suite in the counter tables.\n\n'
text += '## Disturbed native control\n\nIn Intel mbstring counters, aa2 / mb_strstr/zh/absent / pass 1 / side b ran after a 120-second idle wait expired (CPU 2 reported 17% busy). Exclude that pair from any quiet-control claim. Original observations are retained in [the series](../data/counters/intel-extensions-mbstring.json); [quality metadata](../data/counter-quality.json) identifies row 1741 (zero-based). The A/B rows were not the rows associated with that warning. A separate five-pair [A/A validation](../data/counters/intel-extensions-aa-validation.json) repeats that one case with the same GCC14 master binary.\n\n'
validation = json.loads((data / 'counters/intel-extensions-aa-validation.json').read_text())
v = {}
for g, side, key, c, i, ec, ei in validation['rows']:
    n = validation['cases'][key]['n']; v.setdefault(side, []).append(((c-ec)/n, (i-ei)/n))
dc = st.median(100*(b[0]/x[0]-1) for x,b in zip(v['a'],v['b']))
di = st.median(100*(b[1]/x[1]-1) for x,b in zip(v['a'],v['b']))
text += f'The fresh validation median is {dc:+.3f}% cycles and {di:+.5f}% instructions. It is additional evidence, not a replacement observation in the original series.\n\n'
for machine, cc in order:
    text += f'## {machine} {cc}\n\n| Capture / control | Binary | Δ time | Min Δ | Max Δ |\n|---|---|---:|---:|---:|\n'
    for r in rows:
        if not r['aa'] or (r['machine'],r['compiler']) != (machine,cc):continue
        variant = 'master' if r['aa_variant'] == 'base' else 'compact'
        text += f"| `{r['capture']}/{r['source']}`" + (' †' if r['flags'] else '') + f" | {variant} | {r['delta']:+.2f}% | {r['low']:+.2f}% | {r['high']:+.2f}% |\n"
    text += '\n'
outputs['tables/aa.md'] = text
for label in ['amd', 'intel', 'intel-extensions']:
    text = '# Native counter tables: ' + label + '\n\n[Interpretation](../README.md). Generated by bench table from the native bench compare files. CPU cycles and retired instructions are measured separately from the elapsed-time cohort. Negative means fewer cycles/instructions. Original A/A controls are retained. The instructions column aggregates compiler deltas as defined by bench table; per-compiler exact counts are in the linked JSON rows.\n\n'
    if label == 'intel-extensions':text += '**One mbstring A/A pair was disturbed.** See [the exact pair and fresh validation](aa.md#disturbed-native-control); do not treat that original pair as a quiet control.\n\n'
    for file in sorted((data / 'counters').glob(label + '-*.json')):
        if label == 'intel' and file.name.startswith('intel-extensions-'):continue
        title = file.stem.removeprefix(label + '-')
        text += '## ' + title + '\n\n'
        text += f'<!-- bench-table ../data/counters/{file.name} --full --compact-header -->\n<!-- /bench-table -->\n\n'
    outputs['tables/counters-' + label + '.md'] = text
readme = (root / 'README.md').read_text()
for tag, content in [('summary', summary), ('regressions', regressions)]:
    pattern = r'<!-- compact-' + tag + r' -->\n.*?<!-- /compact-' + tag + r' -->'
    readme, count = re.subn(pattern, lambda _: '<!-- compact-' + tag + ' -->\n' + content + '<!-- /compact-' + tag + ' -->', readme, flags=re.S)
    assert count == 1, tag
outputs['README.md'] = readme
failed = []
for name, text in outputs.items():
    text = text.rstrip() + '\n'
    target = root / name
    if name.startswith('tables/counters-') and target.exists():
        # Native blocks are rendered and checked by bench report update/check.
        text = re.sub(r'(<!-- bench-table .+? -->\n).*?(<!-- /bench-table -->)', r'\1\2', text, flags=re.S)
        current = re.sub(r'(<!-- bench-table .+? -->\n).*?(<!-- /bench-table -->)', r'\1\2', target.read_text(), flags=re.S)
    else:current = target.read_text() if target.exists() else None
    if a.check:
        if current != text:failed.append(name)
    elif current != text:
        target.parent.mkdir(parents=True,exist_ok=True); target.write_text(text)
if failed:raise SystemExit('Generated tables differ: ' + ', '.join(failed))
print(json.dumps({'ab_rows': len(ab), 'replications': len(repeats), 'summary_rows': len(selected), 'status': 'checked' if a.check else 'rendered'}))
