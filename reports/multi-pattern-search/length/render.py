#!/usr/bin/env python3
"""Render concise time/payback and construction/memory tables from audited captures."""

import argparse
import json
import statistics as st
from pathlib import Path

REPORT = Path(__file__).resolve().parent.parent
COMPILERS = ['gcc15', 'clang21']


def read(path):
    return json.loads(Path(path).read_text())


def micro(values):
    return st.median(values) / 1000


def label(case):
    operation = case['operation']
    state = case['length_study']['match']
    return {
        'any': 'Moderation: ' + state.replace('absent', 'no match'),
        'unique': 'List matching support terms',
        'replace': 'Replace terms with help URLs',
    }[operation]


def api_label(case):
    return {
        'any': '`Matcher::matches()` (no match)',
        'unique': '`Matcher::getMatchedKeywords()`',
        'replace': '`Replacer::replace()`',
    }[case['operation']]


def size_label(size):
    return str(size) + ' B' if size < 1024 else str(size // 1024) + ' KiB'


def estimate(item):
    if item['status'] == 'slower':
        return '—'
    if item['status'] == 'close':
        return 'close'
    return '~' + str(item['estimated_calls'])


def block(text, name, value):
    start, stop = f'<!-- {name} -->', f'<!-- /{name} -->'
    left, rest = text.split(start, 1)
    _, right = rest.split(stop, 1)
    return left + start + '\n' + value + '\n' + stop + right


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    corpus = REPORT / '../../corpus/multi-pattern-length'
    cases = {
        case['id']: case
        for name in read(corpus / 'index.json')['suite_sha256']
        for case in read(corpus / name)['cases']
    }
    data = {cc: read(REPORT / f'data/length-{cc}.json') for cc in COMPILERS}
    build = {cc: read(REPORT / f'data/build-cost-{cc}.json') for cc in COMPILERS}
    payback = {cc: read(REPORT / f'data/length-payback-{cc}.json') for cc in COMPILERS}
    rows = {cc: {row['case']: row for row in data[cc]['rows']} for cc in COMPILERS}
    costs = {cc: {(row['family'], row['size'], row['class']): row for row in build[cc]['rows']} for cc in COMPILERS}
    models = {cc: {row['case']: row for row in payback[cc]['models']} for cc in COMPILERS}
    for cc in COMPILERS:
        assert all(item['status'] == 'complete' for item in [data[cc], build[cc], payback[cc]])
        assert len(rows[cc]) == len(models[cc]) == len(cases) == 24
        assert len(costs[cc]) == 23
        for result in [build[cc], payback[cc]]:
            for key in [
                'php_sha256',
                'module_sha256',
                'source_sha256',
                'source_revision',
                'corpus_index_sha256',
                'harness_sha256',
                'driver_sha256',
                'version',
            ]:
                assert result['metadata']['main_metadata'][key] == data[cc]['metadata'][key], key
        for name, row in costs[cc].items():
            snapshots = [entry['result'] for entry in row['memory']]
            assert len(snapshots) == 5 and all(v == snapshots[0] for v in snapshots)
            assert snapshots[0] == costs['gcc15'][name]['memory'][0]['result']
    main_cases = [
        name
        for name, case in cases.items()
        if case['length_study']['match'] in ['absent', 'mixed'] and case['length_study']['bytes'] != 65536
    ]
    main_cases.sort(
        key=lambda name: (
            {'any': 0, 'unique': 1, 'replace': 2}[cases[name]['operation']],
            cases[name]['length_study']['bytes'],
        )
    )

    def time_table(cc, names, with_payback=True):
        lines = [
            '| Method | Input | PHP built-ins µs | PCRE µs | Prepared µs | One-shot µs |',
            '|---|---:|---:|---:|---:|---:|',
        ]
        if with_payback:
            lines[0] += ' Strings to beat PHP | Strings to beat PCRE |'
            lines[1] += '---:|---:|'
        for name in names:
            case = cases[name]
            candidate = models[cc][name]['candidate']
            native, regex = [method for method in case['methods'] if method != candidate]
            values = rows[cc][name]['time']['ns_per_job']
            alternatives = models[cc][name]['alternatives']
            single = next(row for row in payback[cc]['batches'] if row['case'] == name and row['calls'] == 1)
            samples = single['time']['result']['ns_per_batch']

            def repay(method, alternatives=alternatives, samples=samples, candidate=candidate):
                item = alternatives[method]
                change = st.median([(b / a - 1) * 100 for a, b in zip(samples[method], samples[candidate])])
                if change <= -2:
                    return '1'
                return estimate(item)

            line = (
                f'| {api_label(case)} | {size_label(case["length_study"]["bytes"])} | '
                f'{micro(values[native]):.3f} | {micro(values[regex]):.3f} | '
                f'{micro(values[candidate]):.3f} | {micro(samples[candidate]):.3f} |'
            )
            if with_payback:
                line += f' {repay(native)} | {repay(regex)} |'
            lines.append(line)
        return '\n'.join(lines)

    def cost_table(cc, names):
        lines = [
            '| Dictionary | Keys | Matcher new, µs | Matcher added, KiB | Replacer new, µs | Replacer added, KiB |',
            '|---|---:|---:|---:|---:|---:|',
        ]
        for family, size in names:
            values = []
            for kind in ['Matcher', 'Replacer']:
                item = costs[cc].get((family, size, kind))
                if item is None:
                    values += ['n/a', 'n/a']
                else:
                    values += [
                        f'{micro(item["time"]["result"]["constructor_ns"]):.3f}',
                        f'{item["memory"][0]["result"]["retained_bytes"] / 1024:.1f}',
                    ]
            title = 'Moderation phrases' if family == 'moderation' else 'Support glossary/catalog'
            lines.append(f'| {title} | {size} | ' + ' | '.join(values) + ' |')
        return '\n'.join(lines)

    all_sizes = sorted({size for family, size, _ in costs['gcc15'] if family == 'support'})
    selected = [('moderation', 128)] + [('support', n) for n in [8, 32, 128, 512, 10000]]
    readme = (REPORT / 'README.md').read_text()
    for name in main_cases:
        case = cases[name]
        if case['length_study']['bytes'] not in [4096, 16384]:
            continue
        for cc in COMPILERS:
            candidate = models[cc][name]['candidate']
            native, regex = [method for method in case['methods'] if method != candidate]
            batch = next(row for row in payback[cc]['batches'] if row['case'] == name and row['calls'] == 1)
            samples = batch['time']['result']['ns_per_batch']
            for method in [native, regex]:
                change = st.median([(b / a - 1) * 100 for a, b in zip(samples[method], samples[candidate])])
                assert change <= -2, (cc, name, method, change)
    readme = block(readme, 'LENGTH-TABLE', time_table('gcc15', main_cases, with_payback=False))
    short_cases = [name for name in main_cases if cases[name]['length_study']['bytes'] < 1024]
    reuse = ['| Method | Input | Strings/object to beat PHP | Strings/object to beat PCRE |',
             '|---|---:|---:|---:|']
    for line in time_table('gcc15', short_cases).splitlines()[2:]:
        cells = [cell.strip() for cell in line.split('|')[1:-1]]
        reuse.append('| ' + ' | '.join(cells[:2] + cells[-2:]) + ' |')
    readme = block(readme, 'REUSE-TABLE', '\n'.join(reuse))
    readme = block(readme, 'BUILD-MEMORY-TABLE', cost_table('gcc15', selected))
    product = read(REPORT / 'data/gcc15.json')
    product_rows = {(row['case'], row['lifecycle']): row for row in product['rows']}
    negative = [
        '| One operation | Replacer lifetime | Fastest comparator | Comparator µs | Replacer µs |',
        '|---|---|---|---:|---:|',
    ]
    for name, lifecycle, title, lifetime in [
        ('order.email', 'request', 'One order email, 10 placeholders', 'Create, replace, destroy'),
        ('secrets.incident-batch', 'worker', 'One complete log: 384 records, 24 secrets', 'Prepared Replacer call'),
    ]:
        row = product_rows[name, lifecycle]
        values = row['time']['ns_per_job']
        best = min((m for m in values if m != 'replacer'), key=lambda m: st.median(values[m]))
        negative.append(
            f'| {title} | {lifetime} | `{best}()` | {micro(values[best]):.3f} | {micro(values["replacer"]):.3f} |'
        )
    readme = block(readme, 'EVERYDAY-LOSSES', '\n'.join(negative))
    length = [
        '# Input length: full results',
        '',
        '[Methods, returned results and exact comparators](README.md#operations-and-comparators).',
        '',
        (
            '128 distinct literal keys, four different saved strings of each exact length, one string per operation. '
            'PCRE caches are warm; the prepared column reuses an object, while one-shot includes its full lifetime. A sample averages complete cycles of all four '
            'strings; the displayed time is the median of 15 samples. Units are µs per operation. '
            '`Prepared` measures a call on an existing object; `One-shot` directly measures construction, '
            'one call and destruction together. They are separate measurements, not an arithmetic sum.'
        ),
        '',
        (
            'The controlled English inputs reorder authored paragraphs; long documents repeat them. This is not '
            'a production trace. Unique-result counts and replacement counts vary with length, so the cases '
            'include both scanning and natural output costs. Exact texts and counts are in the '
            '[corpus](../../corpus/multi-pattern-length/README.md).'
        ),
        '',
        (
            '`1` means a directly observed single-string batch win with at least a 2% paired-median margin, including construction and destruction. This is an observation, not statistical confidence. `~N` values are **estimates**, not directly established minima. The model includes warm construction '
            'and one destruction, divided by the difference in prepared median operation time. It chooses the first '
            'integer above that quotient. Nonpositive differences show a dash; positive differences below 2% show '
            '`close`. The 2% cutoff is a noise heuristic, not confidence. '
            '[Direct batch measurements](LENGTH-PAYBACK.md) check selected nearby sizes; they do not prove a minimum.'
        ),
        '',
    ]
    for cc in COMPILERS:
        length += [
            '## ' + cc,
            '',
            time_table(cc, main_cases),
            '',
            '### All methods and counters',
            '',
            '| Task | Input | Method | µs | CPU cycles | Instructions |',
            '|---|---:|---|---:|---:|---:|',
        ]
        for name, case in cases.items():
            row = rows[cc][name]
            for method in case['methods']:
                counter = row['counters'][method]['samples']
                length.append(
                    f'| {label(case)} | {size_label(case["length_study"]["bytes"])} | `{method}` | '
                    f'{micro(row["time"]["ns_per_job"][method]):.3f} | '
                    f'{st.median(v["cycles:u"] for v in counter):.1f} | '
                    f'{st.median(v["instructions:u"] for v in counter):.1f} |'
                )
        length += ['', '### A/A elapsed controls', '', '| Stage | Task | Time Δ |', '|---|---|---:|']
        for item in data[cc]['aa']:
            length.append(
                f'| {item["stage"]} | {label(cases[item["case"]])} | {(item["median_ratio"] - 1) * 100:+.3f}% |'
            )
        length += ['']
    length += [
        (
            '[Raw GCC samples and counters](data/length-gcc15.json) · '
            '[Raw Clang samples and counters](data/length-clang21.json) · '
            '[Capture audit](data/length-capture-audit.json) · [Reproduce](REPRODUCE.md#fixed-length-and-pure-construction-series).'
        ),
        '',
    ]
    construction = [
        '# Pure construction and retained memory',
        '',
        (
            '**Time: µs for constructing one object from an already loaded dictionary. Memory: KiB added by '
            'the retained object above that dictionary.** No search or destruction is included in the construction '
            'column. The process is warm. Intervals around `new` include the adjacent `hrtime()` cost; no '
            'empty-clock subtraction is applied. Destruction is measured separately and included only in payback.'
        ),
        '',
        (
            'Constructor times use 250 ms warmup and 15 samples of approximately one second in total. Memory '
            'uses five fresh processes; values match across all repeats and both compilers. This is Zend '
            'allocation, not process RSS or total process memory. The support glossary/catalog keys and values '
            'are the [saved memory dictionary](memory/glossary-catalog.json); moderation is the fixed-length '
            "study's 128-phrase policy. Sharing patterns differ even at the same entry count."
        ),
        '',
    ]
    for cc in COMPILERS:
        construction += [
            '## ' + cc,
            '',
            cost_table(cc, [('moderation', 128)] + [('support', n) for n in all_sizes]),
            '',
            '### Destruction cost',
            '',
            '| Dictionary | Keys | Class | Destruction, µs |',
            '|---|---:|---|---:|',
        ]
        for (family, size, kind), row in costs[cc].items():
            construction.append(f'| {family} | {size} | {kind} | {micro(row["time"]["result"]["release_ns"]):.3f} |')
        construction += ['']
    construction += [
        (
            'Construction peak is a different quantity. [Memory totals](MEMORY.md) show input alone, '
            'input plus the ready object, and their common-baseline construction peak. These columns '
            'are totals, not amounts to add together. [First constructors and build/release measurements](PREPARATION.md) '
            'have different timing scopes and are not substituted into this table.'
        ),
        '',
        '[GCC samples](data/build-cost-gcc15.json) · [Clang samples](data/build-cost-clang21.json).',
        '',
    ]
    direct = [
        '# Direct checks of reuse estimates',
        '',
        (
            'A batch builds one candidate object, processes the stated number of strings and destroys it. Native '
            'arrays, regex strings and callbacks are already prepared, with warm PCRE caches. All four saved variants '
            'are processed equally often over each timed sample. Values are µs for the **whole batch**, not per string.'
        ),
        '',
        (
            'Checks select one call and points at approximately 75% and 125% of model estimates, capped at 4096. '
            'The complete tested counts are shown below. These observations do not establish an exact minimum; '
            'large capped estimates are not bracketed. In this input-length series, near-start/middle/end and 64 KiB '
            'cases have estimates only. Direct one-operation checks at all four 4 KiB match positions are in '
            '[FIXED-4K](FIXED-4K.md). Negative API Δ means the candidate batch was faster.'
        ),
        '',
    ]
    for cc in COMPILERS:
        direct += [
            '## ' + cc,
            '',
            '| Task | Input | Calls/object | Method | µs/batch | API Δ vs method |',
            '|---|---:|---:|---|---:|---:|',
        ]
        for row in payback[cc]['batches']:
            name = row['case']
            case = cases[name]
            candidate = models[cc][name]['candidate']
            values = row['time']['result']['ns_per_batch']
            for method, samples in values.items():
                delta = (
                    '—'
                    if method == candidate
                    else f'{st.median([(b / a - 1) * 100 for a, b in zip(samples, values[candidate])]):+.2f}%'
                )
                direct.append(
                    f'| {label(case)} | {size_label(case["length_study"]["bytes"])} | {row["calls"]} | '
                    f'`{method}` | {micro(samples):.3f} | {delta} |'
                )
        direct += ['', '### Additional A/A controls', '', '| Stage | Control | Time Δ |', '|---|---|---:|']
        for item in read(REPORT / f'data/additional-aa-{cc}.json'):
            direct.append(f'| {item["stage"]} | {item["kind"]} | {(item["median_ratio"] - 1) * 100:+.3f}% |')
        direct += ['']
    direct += [
        (
            'All estimated counts, chosen direct points and raw samples: '
            '[GCC](data/length-payback-gcc15.json), [Clang](data/length-payback-clang21.json).'
        ),
        '',
    ]
    outputs = {
        'README.md': readme,
        'LENGTH.md': '\n'.join(length),
        'BUILD-MEMORY.md': '\n'.join(construction),
        'LENGTH-PAYBACK.md': '\n'.join(direct),
    }
    for name, text in outputs.items():
        text = text.rstrip() + '\n'
        path = REPORT / name
        if args.check:
            assert path.read_text() == text, 'Stale length rendering: ' + name
        else:
            path.write_text(text)
    print(
        'Length, pure-construction and estimated-payback tables PASS'
        if args.check
        else 'Rendered concise decision tables'
    )


if __name__ == '__main__':
    main()
