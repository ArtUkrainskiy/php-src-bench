#!/usr/bin/env python3
"""Render match-position and fixed-input dictionary-size comparisons from audited data."""

import argparse
import json
import statistics as st
from pathlib import Path

REPORT = Path(__file__).resolve().parent.parent
COMPILERS = {'gcc15': 'GCC 15.2', 'clang21': 'Clang 21.1'}
SIZES = [8, 16, 32, 64, 128, 256, 512]
POSITIONS = {
    'absent': 'No match',
    'start': 'Near start (byte 18)',
    'middle': 'Middle (about 2 KiB)',
    'end': 'Near end (last 9 bytes)',
}


def read(path):
    return json.loads(path.read_text())


def micro(samples):
    return st.median(samples) / 1000


def block(text, name, value):
    start, stop = f'<!-- {name} -->', f'<!-- /{name} -->'
    before, rest = text.split(start, 1)
    _, after = rest.split(stop, 1)
    return before + start + '\n' + value + '\n' + stop + after


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    corpus = REPORT / '../../corpus/multi-pattern-4k'
    cases = {
        case['id']: case
        for filename in read(corpus / 'index.json')['suite_sha256']
        for case in read(corpus / filename)['cases']
    }
    data = {cc: read(REPORT / f'data/grid-{cc}.json') for cc in COMPILERS}
    batches = {cc: read(REPORT / f'data/grid-oneshot-{cc}.json') for cc in COMPILERS}
    rows = {cc: {row['case']: row for row in data[cc]['rows']} for cc in COMPILERS}
    shots = {
        cc: {row['case']: row['time']['result']['ns_per_batch'] for row in batches[cc]['rows']} for cc in COMPILERS
    }
    assert len(cases) == 18
    for cc in COMPILERS:
        assert data[cc]['status'] == batches[cc]['status'] == 'complete'
        assert set(rows[cc]) == set(shots[cc]) == set(cases)
        for key in [
            'compiler',
            'php_sha256',
            'module_sha256',
            'source_sha256',
            'source_revision',
            'corpus_index_sha256',
            'harness_sha256',
            'driver_sha256',
            'protocol',
            'version',
        ]:
            assert batches[cc]['metadata']['main_metadata'][key] == data[cc]['metadata'][key], key

    def table(cc, identifiers, position=False):
        lines = [
            f'| {"First match: Matcher::matches()" if position else "Dictionary keys"} | PHP µs | PCRE µs | Prepared µs | One-shot µs |',
            '|---|---:|---:|---:|---:|',
        ]
        for name in identifiers:
            case = cases[name]
            candidate = 'replacer' if case['operation'] == 'replace' else 'matcher'
            native, regex = [m for m in case['methods'] if m != candidate]
            first = POSITIONS[case['grid']['match']] if position else str(case['grid']['keys'])
            values = shots[cc][name]
            prepared = rows[cc][name]['time']['ns_per_job'][candidate]
            lines.append(
                f'| {first} | {micro(values[native]):.3f} | {micro(values[regex]):.3f} | '
                f'{micro(prepared):.3f} | {micro(values[candidate]):.3f} |'
            )
        return '\n'.join(lines)

    def winning(cc, operation, scope):
        candidate = 'matcher' if operation == 'any' else 'replacer'
        state = 'absent' if operation == 'any' else 'mixed'
        sizes = []
        for size in SIZES:
            name = f'grid.{operation}.{state}.{size}'
            values = shots[cc][name] if scope == 'one-shot' else rows[cc][name]['time']['ns_per_job']
            comparisons = [m for m in cases[name]['methods'] if m != candidate]
            if all(st.median([b / a - 1 for a, b in zip(values[m], values[candidate])]) <= -0.02 for m in comparisons):
                sizes.append(size)
        return sizes

    def describe(sizes):
        return ', '.join(map(str, sizes)) if sizes else 'none of the tested sizes'

    summary = []
    winners = {
        (cc, operation): winning(cc, operation, 'one-shot') for cc in COMPILERS for operation in ['any', 'replace']
    }
    if len({tuple(sizes) for sizes in winners.values()}) == 1:
        summary.append(
            '**On both compilers**, one-shot `Matcher::matches()` (no match) and `Replacer::replace()` '
            f'beat both comparators at **{describe(winners["gcc15", "any"])} keys** on these inputs.'
        )
    else:
        for cc, title in COMPILERS.items():
            summary.extend(
                [
                    (
                        f'**{title}:** a one-shot `Matcher::matches()` wins against both comparators at '
                        f'**{describe(winners[cc, "any"])} keys**; a one-shot `Replacer::replace()` at '
                        f'**{describe(winners[cc, "replace"])} keys**.'
                    ),
                    '',
                ]
            )
    small = shots['gcc15']['grid.replace.mixed.8']
    prepared = rows['gcc15']['grid.replace.mixed.8']['time']['ns_per_job']['replacer']
    summary.extend(
        [
            '',
            (
                '**Eight-key replacement favors PCRE:** with GCC, '
                f'`preg_replace_callback()` takes **{micro(small["preg_replace_callback"]):.3f} µs**, '
                f'against **{micro(prepared):.3f} µs** for a prepared Replacer and '
                f'**{micro(small["replacer"]):.3f} µs** including construction and destruction.'
            ),
        ]
    )
    position_names = [f'grid.any.{state}.position' for state in POSITIONS]
    text = (REPORT / 'README.md').read_text()
    text = block(text, 'POSITION-TABLE', table('gcc15', position_names, position=True))
    text = block(text, 'DICTIONARY-4K-SUMMARY', '\n'.join(summary))
    full = [
        '# Fixed 4 KiB inputs: match position and dictionary size',
        '',
        (
            'One operation processes one of four different saved English strings, exactly **4096 bytes** each. '
            'All variants cycle equally often. These are controlled authored examples, not production traces. '
            '[Saved inputs and expected results](../../corpus/multi-pattern-4k/README.md).'
        ),
        '',
        (
            '**Time in µs, lower is better.** `Prepared` is one call using an existing candidate object. '
            '`One-shot` directly times constructing one candidate object, processing one string and destroying '
            'the object together. PHP and PCRE times in these tables come from the same one-operation batch series; '
            'their dictionaries, regex strings and callbacks are already prepared and PCRE caches are warm. '
            'Input loading is excluded for every method. Prepared timings come from a separate series.'
        ),
        '',
        (
            'The protocol uses 250 ms warmup per method, 15 time samples (about one second total per method), '
            'rotating/reversed order, CPU affinity and an idle SMT sibling. Five N-minus-zero counter passes '
            'measure prepared operations. Only the Ryzen 9 5950X was measured. '
            'The one-shot timing excludes initial cold-process loading.'
        ),
        '',
        (
            'PHP comparators: a `str_contains()` loop for `matches()` and `strtr()` for replacement. '
            'PCRE comparators: `preg_match()` with one alternation and `preg_replace_callback()` with longest-first '
            'literal alternatives, respectively.'
        ),
        '',
        '## Practical reading',
        '',
        *summary,
        '',
        (
            'These lists require at least a 2% paired-median advantage against each comparator. This is a '
            'noise heuristic, not statistical confidence or a universal crossover threshold. Smaller gaps '
            'remain visible in the tables. A win with a prepared object does not imply a one-shot win.'
        ),
        '',
    ]
    for cc, title in COMPILERS.items():
        full += [
            f'## {title}',
            '',
            '### First-match position: Matcher::matches()',
            '',
            (
                '128 keys. The four positive variants match dictionary entries **1, 37, 91 and 128** '
                '(1-based), in the same order for start/middle/end. Byte offsets are 18 near the start, '
                '2062–2067 in the middle and 4087–4090 near the end; see the saved per-variant facts. '
                'The PHP loop follows dictionary order and stops at its first matching key.'
            ),
            '',
            table(cc, position_names, position=True),
            '',
            '### Dictionary size: Matcher::matches(), no match',
            '',
            (
                'The same four clean strings are used at every dictionary size. All 512 moderation keys '
                'are absent. Dictionaries grow by appending entries from the saved policy lexicon.'
            ),
            '',
            table(cc, [f'grid.any.absent.{n}' for n in SIZES]),
            '',
            (
                f'Prepared Matcher wins against both comparators at {describe(winning(cc, "any", "prepared"))} keys '
                '(same 2% heuristic).'
            ),
            '',
            '### Dictionary size: Replacer::replace(), matching terms',
            '',
            (
                'The same four support articles are used at every dictionary size. Keys are the first entries of the '
                'support lexicon; values are help URLs. More keys also cause more replacements and larger output. '
                'This measures that application workload, not dictionary-size overhead in isolation. '
                '[Per-variant replacement counts](../../corpus/multi-pattern-4k/CASES.md).'
            ),
            '',
            table(cc, [f'grid.replace.mixed.{n}' for n in SIZES]),
            '',
            (
                f'Prepared Replacer wins against both comparators at {describe(winning(cc, "replace", "prepared"))} keys '
                '(same 2% heuristic).'
            ),
            '',
            '### Prepared operations: time and counters',
            '',
            '| Case | Method | µs | CPU cycles | Instructions |',
            '|---|---|---:|---:|---:|',
        ]
        for name, row in rows[cc].items():
            for method in cases[name]['methods']:
                counters = row['counters'][method]['samples']
                full.append(
                    f'| `{name}` | `{method}` | {micro(row["time"]["ns_per_job"][method]):.3f} | '
                    f'{st.median(v["cycles:u"] for v in counters):.1f} | '
                    f'{st.median(v["instructions:u"] for v in counters):.1f} |'
                )
        full += ['', '### A/A controls', '', '| Stage | Scope | Case | Time Δ |', '|---|---|---|---:|']
        for scope, controls in [('Prepared', data[cc]['aa']), ('One-shot', batches[cc]['aa'])]:
            for control in controls:
                full.append(
                    f'| {control["stage"]} | {scope} | `{control["case"]}` | '
                    f'{(control["median_ratio"] - 1) * 100:+.3f}% |'
                )
        full += [
            '',
            f'[Prepared samples and counters](data/grid-{cc}.json) · [One-shot samples](data/grid-oneshot-{cc}.json).',
            '',
        ]
    full += ['[Import audit](data/grid-capture-audit.json) · [Reproduce](REPRODUCE.md#fixed-4-kib-matrix).', '']
    for name, content in {'README.md': text, 'FIXED-4K.md': '\n'.join(full)}.items():
        content = content.rstrip() + '\n'
        path = REPORT / name
        if args.check:
            assert path.read_text() == content, 'Stale fixed-4-KiB rendering: ' + name
        else:
            path.write_text(content)
    print('Fixed-4-KiB tables PASS' if args.check else 'Rendered fixed-4-KiB tables')


if __name__ == '__main__':
    main()
