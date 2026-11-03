#!/usr/bin/env python3
"""Render allocation tables and verify every saved memory sample and fixture hash."""
import argparse
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
REPORT = ROOT.parent
from layout import layout


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
    structures = {}
    for family in index['families']:
        words = list(json.loads((ROOT / (family + '.json')).read_text())['replacements'])
        facts = json.loads((ROOT / (family + '-expected.json')).read_text())
        for fact in facts:
            for kind in ['Matcher', 'Replacer']:
                result = layout(words[:fact['size']], kind)
                assert result['states'] == fact[kind.lower() + '_states']
                measured = rows[family, fact['size'], kind]['construction']['object_extra_bytes']
                assert result['requested_array_bytes'] <= measured
                structures[family, fact['size'], kind] = result
    text = (REPORT / 'README.md').read_text()
    growth = []
    for kind in ['Matcher', 'Replacer']:
        first = rows['glossary-catalog', 1000, kind]['construction']['object_extra_bytes']
        last = rows['glossary-catalog', 10000, kind]['construction']['object_extra_bytes']
        growth.append(f'{kind}: {first / 1048576:.2f} to {last / 1048576:.2f} MiB ({last / first:.2f} times)')
    control = [rows['permuted-control', 10000, kind]['construction']['object_extra_bytes'] / 1048576
               for kind in ['Matcher', 'Replacer']]
    summary = ('From 1,000 to 10,000 strings in these saved inputs, ' + '; '.join(growth) + '. '
               f'The 10,000-string permuted-byte control takes {control[0]:.2f} MiB for Matcher and '
               f'{control[1]:.2f} MiB for Replacer. These are observed endpoints, not a fitted growth law.')
    costs = [rows['glossary-catalog', 10000, kind]['construction'] for kind in ['Matcher', 'Replacer']]
    short_costs = (f"At 10,000 saved glossary/catalog entries, the prepared object adds "
                   f"**{costs[0]['object_extra_bytes'] / 1048576:.2f} MiB for Matcher** or "
                   f"**{costs[1]['object_extra_bytes'] / 1048576:.2f} MiB for Replacer**, above the input array. "
                   f"Constructor peaks above that same input baseline are {costs[0]['construction_peak_extra_bytes'] / 1048576:.2f} and "
                   f"{costs[1]['construction_peak_extra_bytes'] / 1048576:.2f} MiB respectively. "
                   "[Memory](MEMORY.md) separates retained allocation, construction peak and query scratch space.")
    for marker, block in [('MEMORY-TABLE', table(index, rows, 'glossary-catalog')), ('MEMORY-GROWTH', summary), ('SHORT-COSTS', short_costs)]:
        start, stop = f'<!-- {marker} -->', f'<!-- /{marker} -->'
        left, rest = text.split(start, 1)
        _, right = rest.split(stop, 1)
        text = left + start + '\n' + block + '\n' + stop + right
    lines = [
        '# Memory: preparation, retained objects and queries', '',
        'All tables use **KiB (1024 bytes)** unless stated otherwise. These are Zend live-allocation counters, not process RSS.', '',
        'Five fresh processes per class, size, family and compiler: 440 processes. All recorded allocation values match across repeats and GCC 15 / Clang 21. A shared table therefore loses no observed compiler difference.', '',
        '## Reading the columns', '',
        '- **Input:** the caller\'s PHP list or map and its strings, after parsing temporaries are released.',
        '- **+Matcher / +Replacer:** additional live allocation after construction while Input remains alive. Strings are shared by reference.',
        '- **Peak +:** the constructor peak above that same input baseline, after resetting the peak counter. This includes the retained object; do not add the two columns.',
        '- **Standalone:** the object and strings it retains after the input array is released, relative to the baseline before loading the dictionary.', '',
        'Startup, input-parsing peaks, reserved allocator pages and physical peaks inside realloc are outside these counters. All native automaton buffers use Zend allocation functions and are included.', '',
        '## Growth and structure', '',
        'The automaton combines dense transition rows with packed sparse states. It keeps dense rows for shallow states, states with at least eight children, and selected states near their failure target. Other states retain actual trie edges and a failure link. A single-child transition is stored inside its sparse record; it does not need a separate edge allocation.', '',
        'For a nonempty dictionary, let N be its string count, T its total key bytes, A its distinct key-byte count, S its state count, D its dense-state count and E its separately packed sparse-edge count. On these 64-bit builds the requested runtime arrays occupy:', '',
        '- **Matcher:** `4D(A+1) + 12(S-D) + 8E + 12S + 8N` bytes.',
        '- **Replacer:** `4D(A+1) + 12(S-D) + 8E + 4S + 16N` bytes.', '',
        'These budgets exclude the fixed object and byte-map fields, allocator rounding and retained string bodies. They explain the measured object additions; the measured tables remain authoritative. The final state arrays are sized to S. Temporary build arrays can grow geometrically, but their spare capacity is not retained in the immutable runtime automaton.', '',
        '**String count alone does not determine memory.** Prefix sharing changes Matcher states; suffix sharing matters for reversed Replacer states. Alphabet size and the dense/sparse mix change the cost of each state. Dense-selection thresholds can create steps even without spare runtime capacity. Since `D ≤ S`, `E ≤ S-1`, `S ≤ 1+T` and the byte alphabet is bounded, automaton storage has a linear upper bound in total key bytes. This does not establish smooth or proportional growth in N.', '',
        'Construction also needs trie records, edges, failure-link workspace and runtime packing. Its measured peak is separate from retained storage. It should not be inferred by adding table columns.', '',
        '![Memory growth and allocation per dictionary string](memory/growth.svg)', '',
        'Lines join measured sizes only. The first 512 entries preserve the support glossary; larger dictionaries add authored combinations of product names. They are constructed inputs, not a production vocabulary or a speed experiment at 10,000 strings.', '',
        '## Saved input families', '',
        '[Glossary and catalog](memory/glossary-catalog.json) uses the existing glossary, then saved catalog labels. [Permuted control](memory/permuted-control.json) rearranges bytes within each key, preserving lengths, byte multisets, alphabet and replacement values. It is a synthetic topology control, not another product case or a proven worst case. Dictionaries are nested prefixes of the same saved list. Every replacement value is a distinct 37-byte help URL.', '',
    ]
    for family, heading in [('glossary-catalog', 'Glossary and constructed catalog'), ('permuted-control', 'Permuted-byte control')]:
        facts = json.loads((ROOT / (family + '-expected.json')).read_text())
        lines += ['## ' + heading, '', table(index, rows, family), '',
                  '| Strings | Matcher standalone | Replacer standalone | Matcher bytes/string | Replacer bytes/string |',
                  '|---|---:|---:|---:|---:|']
        for n in index['sizes']:
            m, r = [rows[family, n, kind]['construction'] for kind in ['Matcher', 'Replacer']]
            lines.append(f"| {n} | {m['standalone_bytes'] / 1024:.1f} | {r['standalone_bytes'] / 1024:.1f} | {m['object_extra_bytes'] / n:.1f} | {r['object_extra_bytes'] / n:.1f} |")
        lines += ['', 'Bytes/string uses the object addition, excluding Input.', '',
                  '| Strings | Key bytes | Mean key bytes | Alphabet bytes | Matcher states | Matcher dense | Replacer states | Replacer dense |',
                  '|---|---:|---:|---:|---:|---:|---:|---:|']
        for fact in facts:
            n = fact['size']
            m, r = [structures[family, n, kind] for kind in ['Matcher', 'Replacer']]
            lines.append(f"| {n} | {fact['keyword_bytes']} | {fact['keyword_bytes'] / n:.1f} | {fact['alphabet_bytes']} | {m['states']} | {m['dense_states']} | {r['states']} | {r['dense_states']} |")
        lines += ['', 'State/layout facts are calculated from the saved byte strings and the final implementation by [layout.py](memory/layout.py). They are explanatory counts, not public runtime API counters. The array budget below excludes fixed fields and allocator rounding.', '',
                  '| Strings | Class | Dense rows KiB | Sparse KiB | Edges KiB | Outputs KiB | Pointers KiB | Arrays KiB |',
                  '|---|---|---:|---:|---:|---:|---:|---:|']
        for n in [8, 128, 512, 2000, 10000]:
            for kind in ['Matcher', 'Replacer']:
                part = structures[family, n, kind]
                values = [part[key] / 1024 for key in ['dense_transition_bytes', 'sparse_metadata_bytes', 'packed_edge_bytes', 'output_metadata_bytes', 'dictionary_pointer_bytes', 'requested_array_bytes']]
                lines.append(f'| {n} | {kind} | ' + ' | '.join(f'{v:.1f}' for v in values) + ' |')
        lines += ['', '### Query peaks', '',
                  'Additional allocations above an already prepared object, subject and expected-result data. Each operation resets the peak; correctness checks occur after the snapshot. Result storage is included.', '',
                  '| Strings | matches() | countMatches() | getMatchedKeywords() | matchAll() | replace() |',
                  '|---|---:|---:|---:|---:|---:|']
        for n in index['sizes']:
            mq, rq = [rows[family, n, kind]['queries'] for kind in ['Matcher', 'Replacer']]
            values = [mq[m]['peak_extra_bytes'] / 1024 for m in ['matches', 'countMatches', 'getMatchedKeywords', 'matchAll']] + [rq['replace']['peak_extra_bytes'] / 1024]
            lines.append('| ' + str(n) + ' | ' + ' | '.join(f'{v:.1f}' for v in values) + ' |')
        lines += ['', '| Strings | Distinct keys matched | All overlapping hits | Replacements | Output KiB |',
                  '|---|---:|---:|---:|---:|']
        for fact in facts:
            lines.append(f"| {fact['size']} | {len(fact['getMatchedKeywords'])} | {fact['countMatches']} | {fact['replacement_count']} | {fact['output_bytes'] / 1024:.1f} |")
        lines += ['']
    lines += [
        '## Query interpretation', '',
        'Each family has a saved 65,536-byte subject made by repeating a sentence containing its first eight terms. The text stays fixed as N grows; other terms may also match. These repetitive texts measure allocations. They are not additional product-speed benchmarks.', '',
        '`matches()` and `countMatches()` allocate no additional tracked heap in these runs. `getMatchedKeywords()` needs dictionary-sized scratch storage. `matchAll()` stores a result object per hit. `replace()` has subject-sized candidate storage plus its output. Different hit density, output expansion or subject length changes these peaks.', '',
        'Constructor and query peaks occur in different operations: do not sum them. No memory comparison with PCRE/native alternatives, other allocators, machines or FPM worker sharing is claimed.', '',
        '## Data and reproduction', '',
        '[GCC samples](data/memory-gcc15.json) · [Clang samples](data/memory-clang21.json) · [fixtures](memory/index.json) · [generator](memory/generate.py) · [PHP snapshots](memory/measure.php) · [driver](memory/measure.py). The module/PHP hashes match the main time series. Every fresh process checks the measured methods against saved independent expected results.', '',
        'After the main series in [Reproduce](REPRODUCE.md), keep its BENCH_BUILDS, RUN_ROOT and BENCH_CPU variables:', '',
        '```sh',
        'python3 memory/generate.py --check',
        'for tag in gcc15 clang21; do',
        '  python3 memory/measure.py --php-build "$BENCH_BUILDS/runtime-$tag" \\',
        '    --module "$RUN_ROOT/data-product-$tag/strmatch.so" \\',
        '    --reference-data "$RUN_ROOT/data-product-$tag/results.json" \\',
        '    --compiler "$tag" --cpu "$BENCH_CPU" --output "$RUN_ROOT/memory-$tag.json"',
        'done',
        '```', '',
        'Each compiler ends with `MEMORY COMPLETE: 44 configurations, 220 fresh processes`. One compiler took under a minute here. No timing warmup is needed for allocation snapshots. Existing output files are rejected; failures abort the series.', '',
        'Copy each complete memory JSON into `data/memory-gcc15.json` or `data/memory-clang21.json` beside the corresponding imported main captures in a separate report checkout. For example, use `cp "$RUN_ROOT/memory-gcc15.json" data/memory-gcc15.json` and likewise for Clang. `python3 memory/render.py` and `python3 memory/render.py --check` update/verify only memory tables. The general renderer requires all supplemental captures to match the newly imported main binaries. `python3 memory/layout.py --check` checks state counts against saved fixtures. The optional `python3 memory/plot.py` uses Matplotlib; no plotting runs inside a measurement.', '',
    ]
    for path, value in {REPORT / 'README.md': text, REPORT / 'MEMORY.md': '\n'.join(lines)}.items():
        value = value.rstrip() + '\n'
        if args.check:
            assert path.read_text() == value, 'Stale memory rendering: ' + path.name
        else:
            path.write_text(value)
    print('Memory tables PASS' if args.check else 'Rendered hybrid memory allocation tables')


if __name__ == '__main__':
    main()
