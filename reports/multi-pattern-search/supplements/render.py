#!/usr/bin/env python3
"""Render preparation, direct payback and order controls from audited captures."""

import argparse
import importlib.util
import json
import statistics as stats
from pathlib import Path

REPORT = Path(__file__).resolve().parent.parent
COMPILERS = ['gcc15', 'clang21']
MEDIAN = stats.median


def read(name):
    return json.loads((REPORT / 'data' / name).read_text())


def changes(base, candidate):
    assert len(base) == len(candidate) == 15
    return [(b / a - 1) * 100 for a, b in zip(base, candidate)]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    spec = importlib.util.spec_from_file_location('primary_render', REPORT / 'render.py')
    primary = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(primary)
    datasets = {
        'product': primary.load('Everyday cases', 'multi-pattern-product', ''),
        'size': primary.load('Dictionary size', 'multi-pattern-scaling', 'size-'),
    }
    preparation = {cc: read(f'preparation-{cc}.json') for cc in COMPILERS}
    batches = {cc: read(f'payback-batches-{cc}.json') for cc in COMPILERS}
    models = {cc: read(f'payback-model-{cc}.json') for cc in COMPILERS}
    orders = {cc: read(f'order-{cc}.json') for cc in COMPILERS}
    for collection in [preparation, batches, models, orders]:
        for cc, data in collection.items():
            assert data['status'] == 'complete'
            assert data['metadata']['passes'] == 15
            main_meta = data['metadata']['main_metadata']
            reference = datasets['product']['data'][cc]['metadata']
            for key in ['php_sha256', 'module_sha256', 'source_revision', 'source_sha256']:
                assert main_meta[key] == reference[key], key
    cases = {(stem, key): case for stem, ds in datasets.items() for key, case in ds['cases'].items()}

    def title(stem, name):
        return primary.case_link(datasets[stem], cases[stem, name])

    def bound(cc, key, group):
        good = []
        for row in batches[cc]['rows']:
            if (row['corpus'], row['case']) != key:
                continue
            selected = [m for m in row['paired_delta_to_alternatives'] if m.startswith('preg') == (group == 'pcre')]
            if selected and all(MEDIAN(row['paired_delta_to_alternatives'][m]) <= -2 for m in selected):
                good.append(row['batch_size'])
        return f'≤{min(good)}' if good else '—'

    def payback_table(keys, detailed=False):
        heading = '| Task | Strings | GCC native | GCC PCRE | Clang native | Clang PCRE |'
        ruler = '|---|---:|---:|---:|---:|---:|'
        if detailed:
            heading += ' GCC tested jobs | Clang tested jobs |'
            ruler += '---|---|'
        lines = [heading, ruler]
        for key in keys:
            stem, name = key
            cells = [bound(cc, key, group) for cc in COMPILERS for group in ['native', 'pcre']]
            if detailed:
                for cc in COMPILERS:
                    sizes = sorted({r['batch_size'] for r in batches[cc]['rows'] if (r['corpus'], r['case']) == key})
                    cells.append(', '.join(map(str, sizes)))
            lines.append(
                f'| {title(stem, name)} | {len(cases[key]["jobs"][0]["dictionary"])} | ' + ' | '.join(cells) + ' |'
            )
        return '\n'.join(lines)

    keys = list(dict.fromkeys((r['corpus'], r['case']) for r in batches['gcc15']['rows']))
    assert set(keys) == {(r['corpus'], r['case']) for r in batches['clang21']['rows']}
    payback = [
        '# How many jobs repay preparation?',
        '',
        "**≤B means a sufficient measured batch, not an exact minimum.** At that batch size the candidate's paired median time was at least 2% lower than every measured alternative in that column's group. A dash means no such point in the tested batches. It does not mean payback is impossible for every other input or batch size.",
        '',
        'A job is the complete saved task. Most selected jobs contain one comment or article; the incident-log job contains one log document with 384 JSON records. See the corpus for each job. Dictionary strings and jobs per object are different counts.',
        '',
        'Matcher/Replacer is constructed once per batch and released at its end. Native parallel arrays and regex strings/callbacks are already prepared, and PCRE compilation caches are warm. This deliberately compares the candidate against prepared existing tools. No PHP startup or input loading is timed. In contrast, the main preparation-included tables also charge array-to-regex or parallel-array preparation.',
        '',
        'Native means every measured non-PCRE alternative for that task; PCRE means every measured regex alternative. Overlapping enumeration uses a pattern per term, rather than an ordinary alternation that would miss nested terms. All alternatives keep their natural result representation.',
        '',
    ]
    for stem, heading in [('product', 'Everyday jobs'), ('size', 'Controlled dictionary sizes')]:
        payback += ['## ' + heading, '', payback_table([key for key in keys if key[0] == stem], True), '']
    payback += [
        '## Estimated versus directly tested',
        '',
        "The model uses the main case's request-minus-worker difference as an estimate P of preparation and release. If Q is the prepared candidate time and A the prepared alternative time, it solves `P + B×Q < B×A`. The reported model value is `floor(P/(A-Q)) + 1` only when the gap is positive. It is not the fresh-process constructor measurement and includes differences between request/worker wrappers.",
        '',
        'Small differences produce unstable, sometimes very large estimates. A gap below 2% is marked small; a nonpositive estimated P is marked unstable. The model selects batch control points. The tables above use actual batches with a 2% median margin, without claiming statistical significance or an unmeasured minimum. The tested sizes need not be consecutive.',
        '',
        '[All direct batch times and paired ranges](PAYBACK-FULL.md) · [GCC model](data/payback-model-gcc15.json) · [Clang model](data/payback-model-clang21.json). The model covers all 124 case records permitting both lifecycles per compiler, including labeled controls; 36 product/size cases receive direct batch checks.',
        '',
        '## Controls and reproduction',
        '',
        'Fifteen samples, 250 ms warmup and approximately one second of measured work per method. Orders are reversed in pairs; the start rotates between pairs. A complete 2×method-count cycle balances positions; 15 samples are a partial cycle. A/A controls before/after each compiler must stay within 2%. The selected CPU and its SMT sibling are monitored; zero-jiffy activity intervals are unknown, not zero-load observations.',
        '',
        'See [Reproduce](REPRODUCE.md#additional-measurements) for the timed PHP files and portable controller. All methods are checked against saved expected output before each batch measurement. The importer also checks repeated-call result aggregates and raw stdout. These CLI jobs are not FPM throughput or a guarantee for every vocabulary.',
        '',
    ]
    full = [
        '# Direct batch times',
        '',
        'Microseconds per complete batch. The candidate is built once for B jobs; native/PCRE setup is already prepared. Delta is the median paired time change; min/max are paired changes, not confidence intervals. See [interpretation and tested counts](AMORTIZATION.md).',
        '',
    ]
    for cc in COMPILERS:
        full += [
            '## ' + cc,
            '',
            '| Task | Jobs | Existing method | Existing µs | Prepared API µs | Δ | Min Δ | Max Δ |',
            '|---|---:|---|---:|---:|---:|---:|---:|',
        ]
        for row in batches[cc]['rows']:
            sample = row['time']['ns_per_batch']
            for method, expected in row['paired_delta_to_alternatives'].items():
                values = changes(sample[method], sample[row['candidate']])
                assert values == expected
                full.append(
                    f'| {title(row["corpus"], row["case"])} | {row["batch_size"]} | '
                    f'{primary.label(method)} | {MEDIAN(sample[method]) / 1000:.3f} | '
                    f'{MEDIAN(sample[row["candidate"]]) / 1000:.3f} | {MEDIAN(values):+.1f}% | '
                    f'{min(values):+.1f}% | {max(values):+.1f}% |'
                )
        full += ['']
    prep = [
        '# Object preparation: first construction and repeated build/release',
        '',
        'All times are microseconds. **First** is the first constructor in a fresh PHP process after the dictionary is parsed. PHP startup, parsing and object release are excluded from that timer. Five fresh processes are measured. It does not imply cold CPU or filesystem caches.',
        '',
        '**Build/release** repeatedly creates and frees an object, with the same dictionary already loaded. It includes the common closure/loop cost and object release, with 250 ms warmup and 15 samples totaling about one second. It excludes searching. These are different measurements; do not substitute one for the other in payback calculations.',
        '',
        'The inputs here are the [memory dictionaries](MEMORY.md), not the moderation policies. Equal string counts do not imply equal constructor cost: lengths, alphabet and shared prefixes/suffixes differ. Use [actual product-job payback](AMORTIZATION.md) for a deployment decision.',
        '',
    ]
    prep_rows = {cc: {(r['family'], r['size'], r['class']): r for r in preparation[cc]['rows']} for cc in COMPILERS}
    for family, heading in [
        ('glossary-catalog', 'Glossary and constructed catalog'),
        ('permuted-control', 'Permuted-byte control'),
    ]:
        prep += [
            '## ' + heading,
            '',
            '| Strings | Class | GCC first | GCC build/release | Clang first | Clang build/release |',
            '|---|---|---:|---:|---:|---:|',
        ]
        for n in [8, 16, 32, 64, 128, 256, 512, 1000, 2000, 5000, 10000]:
            for kind in ['Matcher', 'Replacer']:
                values = []
                for cc in COMPILERS:
                    row = prep_rows[cc][family, n, kind]
                    first = [v['result']['constructor_ns'] for v in row['first_constructor_fresh_process']]
                    warm = row['warm_build_release']['ns']['build_release']
                    assert len(first) == 5 and len(warm) == 15
                    values += [f'{MEDIAN(first) / 1000:.3f}', f'{MEDIAN(warm) / 1000:.3f}']
                prep.append(f'| {n} | {kind} | ' + ' | '.join(values) + ' |')
        prep += ['']
    prep += [
        (
            'All first/warm samples, iteration counts, A/A controls and hashes: '
            '[GCC](data/preparation-gcc15.json), [Clang](data/preparation-clang21.json). '
            'No subtraction of an empty timing loop is used. Constructor timing is not a measurement of whole-request latency.'
        ),
        '',
    ]
    confirmation = [
        '# Order and noise controls',
        '',
        'The primary time series is preserved unchanged. Additional runs select every row with an even method count, every candidate within 5% of the fastest existing alternative, and any method whose maximum/minimum sample exceeds 1.10. Selection is an OR of these rules, defined before the final data was inspected.',
        '',
        'The original rotation/reversal sequence does not visit all positions for four methods, and its two-label A/A traversal keeps a fixed order. The additional harness reverses each pair and rotates the start between pairs. The only source change is that traversal. At 15 passes it is not an exactly complete positional cycle. Hardware-counter runs already use separate forward/reverse alternation and are not repeated here.',
        '',
        'Runs occur at different times and processes, so differences cannot be attributed solely to ordering. Both results are retained. Close medians and ranking changes are not decisive wins. Main-table bold marks only a lower median; it does not establish significance. Strong summary claims require a margin on both compilers and must survive an available repeat.',
        '',
    ]
    for cc in COMPILERS:
        confirmation += [
            '## ' + cc,
            '',
            '| Task | Mode | Main reference | Main Δ | Repeat reference | Repeat Δ | Reading |',
            '|---|---|---|---:|---|---:|---|',
        ]
        for row in orders[cc]['rows']:
            a, b = row['original_time']['ns_per_job'], row['time']['ns_per_job']
            candidate = 'replacer' if 'replacer' in a else 'matcher'
            alternatives = [m for m in a if m != candidate]
            am = min(alternatives, key=lambda m: MEDIAN(a[m]))
            bm = min(alternatives, key=lambda m: MEDIAN(b[m]))
            ad, bd = MEDIAN(changes(a[am], a[candidate])), MEDIAN(changes(b[bm], b[candidate]))
            close = abs(ad) < 2 or abs(bd) < 2 or (ad < 0) != (bd < 0)
            reading = 'Close / ranking changes' if close else 'Both lower' if ad < 0 and bd < 0 else 'Both higher'
            confirmation.append(
                f'| {title(row["corpus"], row["case"])} | {row["lifecycle"]} | '
                f'{primary.label(am)} | {ad:+.2f}% | {primary.label(bm)} | {bd:+.2f}% | {reading} |'
            )
        confirmation += ['', 'Paired-reversal A/A:', '', '| Stage | Time Δ |', '|---|---:|']
        for control in orders[cc]['aa']:
            confirmation.append(f'| {control["stage"]} | {(control["median_ratio"] - 1) * 100:+.3f}% |')
        confirmation += ['']
    confirmation += [
        (
            'Complete original/repeat samples and selection reasons: '
            '[GCC](data/order-gcc15.json), [Clang](data/order-clang21.json). '
            'Compiler, inputs, binary hashes and JIT settings match the main series. Supplemental calls explicitly set memory_limit=1G; main calls use the -n default. '
            'This A/A compares identical code in a single build, not independently linked PHP binaries.'
        ),
        '',
    ]
    summary_keys = [
        ('product', name)
        for name in [
            'moderation.en.clean',
            'help.unique',
            'help.count',
            'help.all',
            'help.link-one',
            'secrets.incident-batch',
        ]
    ]
    summary_keys += [('size', 'scale.moderation.short.absent.512'), ('size', 'scale.replace.articles1.512')]
    quick_key = ('product', 'help.unique')
    quick_bounds = [bound(cc, quick_key, group) for cc in COMPILERS for group in ['native', 'pcre']]
    if len(set(quick_bounds)) == 1 and quick_bounds[0] != '—':
        sufficient = quick_bounds[0].removeprefix('≤')
        short_payback = (
            f'For example, a 96-term Matcher listing support topics beat both prepared '
            f'native and PCRE references by at least 2% in a batch of **{sufficient} articles**, '
            'on both compilers. This is a sufficient tested size, not the minimum. '
            'Other tasks and dictionaries need different reuse.'
        )
    else:
        short_payback = (
            'The direct batch tables show sufficient tested reuse counts separately '
            'for each task, compiler and baseline. They are not exact minima.'
        )
    outputs = {
        'AMORTIZATION.md': '\n'.join(payback),
        'PAYBACK-FULL.md': '\n'.join(full),
        'PREPARATION.md': '\n'.join(prep),
        'CONFIRMATION.md': '\n'.join(confirmation),
    }
    readme = (REPORT / 'README.md').read_text()
    start, stop = '<!-- SHORT-PAYBACK -->', '<!-- /SHORT-PAYBACK -->'
    if start in readme:
        left, tail = readme.split(start, 1)
        _, right = tail.split(stop, 1)
        readme = left + start + '\n' + short_payback + '\n' + stop + right
    start, stop = '<!-- PAYBACK-TABLE -->', '<!-- /PAYBACK-TABLE -->'
    if start in readme:
        left, tail = readme.split(start, 1)
        _, right = tail.split(stop, 1)
        outputs['README.md'] = left + start + '\n' + payback_table(summary_keys) + '\n' + stop + right
    for name, text in outputs.items():
        text = text.rstrip() + '\n'
        path = REPORT / name
        if args.check:
            assert path.read_text() == text, 'Stale supplement rendering: ' + name
        else:
            path.write_text(text)
    print('Supplement tables PASS' if args.check else 'Rendered preparation, payback and order-control tables')


if __name__ == '__main__':
    main()
