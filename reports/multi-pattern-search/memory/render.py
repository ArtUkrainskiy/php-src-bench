#!/usr/bin/env python3
"""Render allocation tables and verify every saved memory sample and fixture hash."""
import argparse
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
REPORT = ROOT.parent


def load():
    index = json.loads((ROOT / 'index.json').read_text())
    hashes = {**index['files_sha256'], 'generate.py': index['generator_sha256']}
    for name, expected in hashes.items():
        assert hashlib.sha256((ROOT / name).read_bytes()).hexdigest() == expected, name
    assert hashlib.sha256((REPORT / '../../corpus/multi-pattern-scaling/support-terms.json').read_bytes()).hexdigest() == index['glossary_sha256']
    expected_rows = {(family, size, kind) for family in index['families'] for size in index['sizes'] for kind in ['Matcher', 'Replacer']}
    datasets = []
    for compiler in ['gcc15', 'clang21']:
        data = json.loads((REPORT / 'data' / f'memory-{compiler}.json').read_text())
        assert data['status'] == 'complete'
        assert data['metadata']['repeats'] == 5 and data['metadata']['one_configuration_per_process']
        for name, key in [('index.json', 'index_sha256'), ('measure.php', 'harness_sha256'), ('measure.py', 'driver_sha256')]:
            assert hashlib.sha256((ROOT / name).read_bytes()).hexdigest() == data['metadata'][key], key
        reference = json.loads((REPORT / 'data' / f'{compiler}.json').read_text())['metadata']
        assert all(data['metadata'][key] == reference[key] for key in ['php_sha256', 'module_sha256', 'source_revision'])
        rows = {(r['family'], r['size'], r['class']): r for r in data['rows']}
        assert len(rows) == len(data['rows']) and set(rows) == expected_rows
        for row in rows.values():
            assert len(row['samples']) == 5 and all(s == row['samples'][0] for s in row['samples'])
        datasets.append(rows)
    for key in expected_rows:
        assert datasets[0][key]['samples'] == datasets[1][key]['samples'], key
    return index, {key: row['samples'][0] for key, row in datasets[0].items()}


def table(index, rows, family):
    lines = ['| Strings | Matcher input | +Matcher | Peak +Matcher | Replacer input | +Replacer | Peak +Replacer |',
             '|---|---:|---:|---:|---:|---:|---:|']
    for size in index['sizes']:
        m, r = [rows[(family, size, kind)]['construction'] for kind in ['Matcher', 'Replacer']]
        values = [c[key] / 1024 for c in [m, r] for key in ['input_bytes', 'object_extra_bytes', 'construction_peak_extra_bytes']]
        lines.append('| ' + str(size) + ' | ' + ' | '.join(f'{v:.1f}' for v in values) + ' |')
    return '\n'.join(lines)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    index, rows = load()
    readme = REPORT / 'README.md'
    text = readme.read_text()
    start, stop = '<!-- MEMORY-TABLE -->', '<!-- /MEMORY-TABLE -->'
    left, rest = text.split(start, 1)
    _, right = rest.split(stop, 1)
    text = left + start + '\n' + table(index, rows, 'glossary-catalog') + '\n' + stop + right
    growth = []
    for kind in ['Matcher', 'Replacer']:
        first = rows[('glossary-catalog', 1000, kind)]['construction']['object_extra_bytes']
        last = rows[('glossary-catalog', 10000, kind)]['construction']['object_extra_bytes']
        growth.append(f'{kind} {first/1048576:.2f} → {last/1048576:.2f} MiB ({last/first:.2f}×)')
    control = [rows[('permuted-control', 10000, kind)]['construction']['object_extra_bytes']/1048576 for kind in ['Matcher', 'Replacer']]
    summary = ('For a 10× increase from 1,000 to 10,000 strings in this corpus: ' + '; '.join(growth) + '. '
               f'The permuted-byte control at 10,000 takes {control[0]:.2f} MiB and {control[1]:.2f} MiB respectively. '
               'These endpoint ratios describe the saved inputs, not an asymptotic fit.')
    low, high = [rows[('glossary-catalog', n, 'Matcher')]['construction']['object_extra_bytes'] for n in [64, 128]]
    summary += (f' Growth is not uniformly sublinear either: 64 → 128 strings raises Matcher allocation '
                f'from {low/1024:.1f} to {high/1024:.1f} KiB ({high/low:.2f}×), '
                'as the required state capacity crosses two doubling thresholds.')
    start, stop = '<!-- MEMORY-GROWTH -->', '<!-- /MEMORY-GROWTH -->'
    left, rest = text.split(start, 1)
    _, right = rest.split(stop, 1)
    text = left + start + '\n' + summary + '\n' + stop + right
    lines = ['# Memory: preparation, retained objects and queries', '',
             'All tables use **KiB (1024 bytes)**, except where a different unit is named. These are Zend live-allocation counters, not process RSS.', '',
             'Five fresh processes per class/size/family/compiler; 440 processes in total. Every recorded byte count is identical across repeats and GCC 15 / Clang 21. Tables therefore show one shared value, without hiding a compiler difference.', '',
             '## What the columns mean', '',
             '- **Input:** live PHP array and its strings after parsing temporaries are released. Matcher receives a list of keys; Replacer receives a key-to-URL map.',
             '- **+Matcher / +Replacer:** live allocation increase after construction while that input array remains alive. Keys and replacement strings are shared by reference, so their original storage is already in Input.',
             '- **Peak +:** maximum allocation increase during that constructor, measured after resetting the peak at the input-array baseline. It includes the final object; do not add it to the +object column.',
             '- **Standalone:** object plus the strings it retains after releasing the caller’s input array, relative to the baseline before loading the dictionary.', '',
             'PHP/runtime startup, input-file parsing peaks and allocator-reserved pages are excluded. The native engine uses Zend allocation functions, so its states, transitions and temporary arrays are counted. Physical peaks inside the system allocator and RSS are not measured.', '',
             '## Growth and structure', '',
             'Let N be the number of keys, T their total bytes, A the number of distinct key bytes, S the trie state count and C its allocated capacity. The implementation stores a dense row for A+1 transition columns per state, including one fallback column. State records use 16 bytes, transition entries 4 bytes and string pointers 8 bytes in these 64-bit builds.', '',
             'The dominant requested allocation is `C × (16 + 4 × (A + 1)) + 8N` for Matcher and `C × (16 + 4 × (A + 1)) + 16N` for Replacer, plus the object and allocator rounding. C grows by doubling from 16; the arrays are not shrunk to S. Constructor peaks also include temporary structures.', '',
             '**This is not a smooth linear function of N.** Shared prefixes reduce Matcher states; shared suffixes reduce Replacer states because its trie is reversed. Capacity doublings create steps. Longer keys or a larger byte alphabet can increase bytes per key. Since `S ≤ 1 + T`, `C < 2S` above the minimum capacity and the byte alphabet is bounded by 256, the automaton’s asymptotic upper bound is linear in T, not quadratic in N. Standalone objects additionally retain their key strings and, for Replacer, replacement strings; replacement payload size is a separate cost. This bound comes from the implementation, not a fit to these eleven points.', '',
             '![Memory growth and bytes per dictionary string](memory/growth.svg)', '',
             'Lines join only measured sizes; they do not locate the intervening capacity thresholds. The 512-key boundary also changes corpus composition: larger sets add constructed catalog labels. This experiment cannot establish a universal curve for arbitrary dictionaries.', '',
             '## Saved input families', '',
             'The first 512 keys of [glossary-catalog.json](memory/glossary-catalog.json) exactly preserve the existing support glossary. To reach 10,000, the generator adds distinct combinations of authored adjectives, product nouns and usage phrases, in a fixed shuffled order. These larger sets are constructed catalog labels, not a harvested production vocabulary.', '',
             '[permuted-control.json](memory/permuted-control.json) permutes the bytes within each key, preserving its length and byte multiset, dictionary size, aggregate alphabet and corresponding replacement value. It is a synthetic topology control, not another product case or a proven worst case. At each size both families are nested prefixes of their saved 10,000-entry lists. Every replacement value is a distinct 37-byte help URL.', '',
             '## Prepared object allocation', '']
    for family, heading in [('glossary-catalog', 'Glossary and constructed catalog'), ('permuted-control', 'Permuted-byte control')]:
        facts = json.loads((ROOT / (family + '-expected.json')).read_text())
        lines += ['### ' + heading, '', table(index, rows, family), '',
                  '| Strings | Matcher standalone | Replacer standalone | Matcher bytes/string | Replacer bytes/string |',
                  '|---|---:|---:|---:|---:|']
        for n in index['sizes']:
            m, r = [rows[(family, n, kind)]['construction'] for kind in ['Matcher', 'Replacer']]
            lines.append(f"| {n} | {m['standalone_bytes']/1024:.1f} | {r['standalone_bytes']/1024:.1f} | {m['object_extra_bytes']/n:.1f} | {r['object_extra_bytes']/n:.1f} |")
        lines += ['', 'The bytes/string columns use the additional object allocation (+object), excluding the input.', '',
                  '| Strings | Key bytes | Mean key bytes | Alphabet bytes | Matcher states | Matcher capacity | Replacer states | Replacer capacity |',
                  '|---|---:|---:|---:|---:|---:|---:|---:|']
        for f in facts:
            mc = max(16, 1 << (f['matcher_states'] - 1).bit_length())
            rc = max(16, 1 << (f['replacer_states'] - 1).bit_length())
            lines.append(f"| {f['size']} | {f['keyword_bytes']} | {f['keyword_bytes']/f['size']:.1f} | {f['alphabet_bytes']} | {f['matcher_states']} | {mc} | {f['replacer_states']} | {rc} |")
        lines += ['', 'State counts and capacities are calculated from the saved strings and the implementation’s growth rule; they are explanatory facts, not extra exposed API counters.', '',
                  '### Query peaks: ' + heading, '',
                  'Additional peak allocations above an already prepared object, loaded subject and expected-result data. Each call resets the peak. Result storage is included; correctness checking occurs only after taking the snapshot.', '',
                  '| Strings | matches() | countMatches() | getMatchedKeywords() | matchAll() | replace() |',
                  '|---|---:|---:|---:|---:|---:|']
        for n in index['sizes']:
            mq, rq = [rows[(family, n, kind)]['queries'] for kind in ['Matcher', 'Replacer']]
            values = [mq[m]['peak_extra_bytes']/1024 for m in ['matches', 'countMatches', 'getMatchedKeywords', 'matchAll']] + [rq['replace']['peak_extra_bytes']/1024]
            lines.append('| ' + str(n) + ' | ' + ' | '.join(f'{v:.1f}' for v in values) + ' |')
        lines += ['', '| Strings | Distinct matched keys | All overlapping hits | Replacements | Output KiB |',
                  '|---|---:|---:|---:|---:|']
        for f in facts:
            lines.append(f"| {f['size']} | {len(f['getMatchedKeywords'])} | {f['countMatches']} | {f['replacement_count']} | {f['output_bytes']/1024:.1f} |")
        lines += ['']
    lines += ['## Query interpretation', '',
              'Each family has a saved 65,536-byte subject, made by repeating a sentence containing its first eight terms. It remains fixed across N; additional terms may also match. These repetitive texts measure allocation behavior and are not new speed benchmarks. `matches()` and `countMatches()` allocate no additional tracked heap in these runs. `getMatchedKeywords()` has dictionary-sized scratch storage; `matchAll()` retains one result object per hit; `replace()` uses subject-sized candidate storage plus its output. Different hit density, output length or subject length changes these query peaks.', '',
              'The constructor tables and query peaks answer different questions. Add a query peak to the applicable live baseline to estimate the tracked peak for that measured lifecycle; do not sum constructor and query peaks. No memory comparison with PCRE, native PHP alternatives, other machines, allocators or FPM worker sharing is claimed.', '',
              '## Data and reproduction', '',
              '[GCC samples](data/memory-gcc15.json) · [Clang samples](data/memory-clang21.json) · [fixture manifest](memory/index.json) · [generator](memory/generate.py) · [PHP snapshots](memory/measure.php) · [driver](memory/measure.py) · [renderer](memory/render.py). Runtime/extension binaries match the time-series hashes exactly; no PHP implementation changed. Each of 440 fresh processes validates every measured method against saved independently generated expected results.', '',
              'Start in the report directory after completing the four time series in [Reproduce](REPRODUCE.md). Keep that shell’s `BENCH_BUILDS`, `RUN_ROOT` and `BENCH_CPU`. The loop below selects each local PHP build, extension module and complete time-result JSON explicitly, then measures the two compilers sequentially:', '',
              '```sh',
              'python3 memory/generate.py --check',
              'for tag in gcc15 clang21; do',
              '  PHP_BUILD="$BENCH_BUILDS/runtime-$tag"',
              '  MODULE="$RUN_ROOT/data-product-$tag/strmatch.so"',
              '  REFERENCE_DATA="$RUN_ROOT/data-product-$tag/results.json"',
              '  test -f "$REFERENCE_DATA"',
              '  python3 memory/measure.py --php-build "$PHP_BUILD" --module "$MODULE" \\',
              '    --reference-data "$REFERENCE_DATA" --compiler "$tag" --cpu "$BENCH_CPU" \\',
              '    --output "$RUN_ROOT/memory-$tag.json"',
              'done',
              '```', '',
              'Each compiler command uses five fresh processes per configuration and ends with `MEMORY COMPLETE: 44 configurations, 220 fresh processes`. One compiler took under a minute here; no timing warmup is needed for these allocation snapshots. Use a fresh output file for each run. A failed or mismatching result aborts the series.', '',
              'To update this capture, copy the two completed files into `data/memory-gcc15.json` and `data/memory-clang21.json` in a separate checkout, alongside their corresponding complete time captures. Then run `python3 render.py` and `python3 render.py --check`. The allocation tables use Python’s standard library only; the optional [plot script](memory/plot.py) uses Matplotlib to regenerate the SVG. No Matplotlib code runs inside PHP or affects a measurement.', '']
    outputs = {readme: text, REPORT / 'MEMORY.md': '\n'.join(lines)}
    for path, value in outputs.items():
        value = value.rstrip() + '\n'
        if args.check:
            assert path.read_text() == value, 'Stale memory rendering: ' + path.name
        else:
            path.write_text(value)
    print('Memory tables PASS' if args.check else 'Rendered memory allocation tables')


if __name__ == '__main__':
    main()
