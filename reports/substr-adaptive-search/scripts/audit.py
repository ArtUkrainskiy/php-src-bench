#!/usr/bin/env python3
"""Independently audit final TSV arithmetic, source hashes, Markdown and portable links."""
import ast
from collections import defaultdict
import csv
import hashlib
import json
import math
from pathlib import Path
import re
import runpy
import statistics as st
import tarfile

report = Path(__file__).resolve().parent.parent
repo = report.parents[1]
manifest = json.loads((report / 'data/report-manifest.json').read_text())
for name, expected in manifest['raw_file_sha256'].items():
    assert hashlib.sha256((repo / name).read_bytes()).hexdigest() == expected, name

cycle_rows = {}
for path in [report / 'data/amd/cycles-reference.json',
             report / 'data/intel/control-cycles.json']:
    d = json.loads(path.read_text())
    groups = defaultdict(lambda: defaultdict(list))
    for group, side, key, gross_cycles, gross_instructions, empty_cycles, empty_instructions in d['rows']:
        groups[(group, key)][side].append((gross_cycles - empty_cycles) / d['cases'][key]['n'])
    cycle_rows.update(groups)

cache = {}
metrics = list(csv.DictReader((report / 'data/metrics.tsv').open(), delimiter='\t'))
assert len(metrics) == 233 * 6
assert len({(row['compiler'], row['case']) for row in metrics}) == len(metrics)
primary_count = 0
for row in metrics:
    path = repo / row['source']
    if path not in cache:
        cache[path] = json.loads(path.read_text())
    d = cache[path]
    case = d['cases'][row['case']]
    medians = []
    instructions = []
    for side, name in [('A', 'stock'), ('B', 'ca89')]:
        raw = case['sides'][side]
        loop = st.median(raw['loop_ns'])
        net = [value - loop for samples in raw['rounds'] for value in samples]
        med = st.median(net)
        spread = 100 * 1.4826 * st.median(abs(v - med) for v in net) / med
        assert math.isclose(float(row[name + '_ns']), med, rel_tol=1e-12)
        assert math.isclose(float(row[name + '_spread_pct']), spread, rel_tol=1e-12, abs_tol=1e-12)
        assert float(row[name + '_instructions']) == raw['instructions']
        medians.append(med)
        instructions.append(raw['instructions'])
    assert math.isclose(float(row['elapsed_change_pct']), 100 * (medians[1] / medians[0] - 1), abs_tol=1e-10)
    assert math.isclose(float(row['instructions_change_pct']), 100 * (instructions[1] / instructions[0] - 1), abs_tol=1e-10)
    assert d['config']['target_ms'] == int(row['target_ms'])
    cycles = cycle_rows.get((row['compiler'], row['case']))
    if cycles:
        for side, name in [('a', 'stock'), ('b', 'ca89')]:
            assert math.isclose(float(row[name + '_cycles_separate']), st.median(cycles[side]), rel_tol=1e-12)
        paired = 100 * (st.median(b / a for a, b in zip(cycles['a'], cycles['b'])) - 1)
        assert math.isclose(float(row['cycles_change_pct']), paired, abs_tol=1e-10)
    else:
        assert not row['stock_cycles_separate'] and not row['ca89_cycles_separate'] and not row['cycles_change_pct']
    primary_count += row['primary'] == 'True'
assert primary_count == 76 * 6

# The aggregate is exactly the native case data, not a replacement of raw runs.
with tarfile.open(report / 'data/amd/native-parts.tar.gz', 'r:gz') as archive:
    members = {m.name: m for m in archive.getmembers() if m.isfile()}
    expected = set()
    for compiler in ['gcc15', 'clang21']:
        full = json.loads((report / f'data/amd/{compiler}-full233-1sec.json').read_text())
        parts = full['seconds_series']['native_parts']
        assert len(parts) == len(full['cases']) == 233
        for key, name in zip(full['cases'], parts):
            expected.add(name)
            with archive.extractfile(members[name]) as source:
                content = source.read()
            assert not re.search(rb'/(?:home|Users)/[^/\s]+/', content)
            assert not re.search(rb'/(?:tmp|var/tmp)/php[-_][^/\s]+/(?:builds|tools)/', content)
            native = json.loads(content)
            assert native['cases'] == {key: full['cases'][key]}, name
            for side, commit in [('A', manifest['base']), ('B', manifest['candidate'])]:
                assert native['sides'][side]['build']['commit'] == commit
    assert set(members) == expected and len(expected) == 466

with tarfile.open(report / 'data/run-logs.tar.gz', 'r:gz') as archive:
    logs = {m.name: archive.extractfile(m).read().decode() for m in archive.getmembers() if m.isfile()}
quality = json.loads((report / 'data/quality.json').read_text())
for name, cases in quality.items():
    log = logs.get(str(Path(name).with_suffix('.log')))
    if log is not None:
        for flags in cases.values():
            assert flags['idle_wait_timeout'] == ('measuring anyway' in log), name
for name, text in logs.items():
    assert not re.search(r'/(?:home|Users)/[^/\s]+/', text), name
    assert not re.search(r'/(?:tmp|var/tmp)/php[-_][^/\s]+/(?:builds|tools)/', text), name

root_files = {'README.md', 'REPRODUCE.md', 'LAYOUT.md', 'change.patch', 'suite.php',
              'boundary-suite.php', 'adversarial-suite.php'}
assert {p.name for p in report.iterdir() if p.is_file()} == root_files
assert {p.name for p in (report / 'scripts').iterdir()} == {'build_report.py', 'audit.py', 'reproduce.py'}

md_count = 0
for directory in [report]:
    for path in directory.rglob('*.py'):
        ast.parse(path.read_text())
        assert not re.search('[\u0400-\u04ff]', path.read_text()), path
    for path in directory.rglob('*.md'):
        text = path.read_text()
        assert not re.search(r'/(?:home|Users)/[^/\s]+/', text), path
        assert not re.search(r'/(?:tmp|var/tmp)/php[-_][^/\s]+/(?:builds|tools)/', text), path
        assert not re.search(r'\bTODO\b', text), path
        for target in re.findall(r'\]\(([^)]+)\)', text):
            if re.match(r'^[a-zA-Z]+:|^#', target):
                continue
            target = target.split('#')[0].strip('<>')
            assert (path.parent / target).exists(), (path, target)
        width = None
        fenced = False
        for line_number, line in enumerate(text.splitlines(), 1):
            if line.startswith('```'):
                fenced = not fenced
                width = None
                continue
            if fenced:
                continue
            if line.startswith('|'):
                count = len(re.split(r'(?<!\\)\|', line))
                assert width is None or count == width, (path, line_number)
                assert count - 2 <= 8, (path, line_number, 'more than eight columns')
                width = count
            else:
                width = None
        md_count += 1
print(f'Audited {len(metrics)} numeric rows, {primary_count} primary rows, '
      f'{len(manifest["raw_file_sha256"])} raw fingerprints and {md_count} Markdown files.')

runpy.run_path(str(report / 'review/check.py'), run_name='__main__')
