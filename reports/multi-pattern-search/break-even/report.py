#!/usr/bin/env python3
"""Render boundary pairs and all supporting observations from saved captures."""
import argparse
import gzip
import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('study', ROOT / 'study.py')
study = importlib.util.module_from_spec(spec)
spec.loader.exec_module(study)


def size(value):
    return str(value) + ' B' if value < 1024 else f'{value / 1024:g} KiB'


def pack(path, data):
    with gzip.GzipFile(filename=str(path), mode='wb', mtime=0) as stream:
        stream.write(json.dumps(data, ensure_ascii=False, separators=(',', ':')).encode())


def native(row, mode):
    median = row['median_us'][mode]
    ratio = median / row['median_us'][row['reference']]
    change = f'{ratio:.1f} times slower' if ratio >= 2 else f'{100 * (ratio - 1):+.2f}%'
    marker = '' if row['scopes'][mode]['qualified'] else '†'
    return f'{median:.3f} ({change}){marker}'


def quality_detail(row, mode, capture=None):
    stat = row['scopes'][mode]
    values = row['spread']
    detail = ('spread: call ' + f'{100 * values[mode]:.2f}%' + ', A/A call '
        + f'{100 * values[mode + "_aa"]:.2f}%' + ', reference '
        + f'{100 * values[row["reference"]]:.2f}%' + '; A/A change '
        + f'{stat["aa_percent"]:+.2f}%')
    if capture is not None:
        detail += f'; SMT busy {capture["sibling_busy_percent"]:.2f}%; CPU steal {capture["cpu_steal_ticks"]} ticks'
    return detail


def reference(row):
    extra_names = {'single_substr_count': 'substr_count()', 'substring_count_loop': 'substr_count()/strpos() loop'}
    name = extra_names.get(row['reference']) or study.method_name(row['reference'], row['case']['operation'])
    return '`' + name + '` ' + f"{row['median_us'][row['reference']]:.3f}"


def input_link(row):
    c = row['case']
    condition = 'no matches' if c['condition'] == 'absent' else f"one match at byte {c['first_offset']}"
    if c['operation'] == 'replace':
        assert c['occurrences'] == c['unique_matched_keys'] == 1
        condition = f"replacements: 1; start byte {c['first_offset']}; output " + size(len(c['expected']['subject'].encode()))
    keys = str(c['keys']) + (' key' if c['keys'] == 1 else ' keys')
    return f"[{size(c['bytes'])}; {keys}; {condition}](inputs/cases/{c['id']}.json)"


def boundary(rows, op, axis, mode, fixed_bytes=4096):
    field = 'keys' if axis == 'keys' else 'bytes'
    candidates = [r for r in rows if r['case']['background'] == 'technical' and r['case']['operation'] == op
        and r['case']['condition'] == ('absent' if op == 'any' else 'single')
        and r['case']['bytes' if axis == 'keys' else 'keys'] == (fixed_bytes if axis == 'keys' else 48)]
    winners = [r for r in candidates if r['scopes'][mode]['state'] == 'win']
    win = min(winners, key=lambda r: r['case'][field]) if winners else None
    losses = [r for r in candidates if r['scopes'][mode]['state'] == 'loss' and (win is None or r['case'][field] < win['case'][field])]
    loss = max(losses, key=lambda r: r['case'][field]) if losses else None
    reversal = bool(win and any(r['scopes'][mode]['state'] == 'loss' and r['case'][field] > win['case'][field] for r in candidates))
    validation = next((r for r in rows if win and r['case']['background'] == 'comments'
        and all(r['case'][k] == win['case'][k] for k in ['operation', 'keys', 'bytes', 'condition'])), None)
    return loss, win, validation, reversal


def endpoint(row, axis, mode, link_prefix=''):
    if row is None:
        return 'Not established'
    value = str(row['case']['keys']) + (' key' if row['case']['keys'] == 1 else ' keys') if axis == 'keys' else size(row['case']['bytes'])
    label = 'Prepared' if mode == 'prepared' else 'One-shot'
    return f"[{value}]({link_prefix}inputs/cases/{row['case']['id']}.json)<br>{reference(row)}<br>{label}: {native(row, mode)}"


def boundary_table(rows, axis, mode, fixed_bytes=4096, link_prefix='', include_oneshot=False):
    win_title = 'Smallest tested prepared win, µs' if include_oneshot else 'Smallest tested win, µs'
    lines = ['| Operation | Nearest smaller loss, µs | ' + win_title + ' | Same mode on the second text, µs |',
             '|---|---|---|---|']
    for op in study.OPS:
        loss, win, check, reversal = boundary(rows, op, axis, mode, fixed_bytes)
        condition = 'no matches' if op == 'any' else 'replacements: 1' if op == 'replace' else 'one occurrence'
        mode_label = 'Prepared' if mode == 'prepared' else 'One-shot'
        repeated = 'No winning point to check' if not win else 'Not checked' if not check else '[Input](' + link_prefix + 'inputs/cases/' + check['case']['id'] + '.json)<br>' + reference(check) + '<br>' + mode_label + ': ' + native(check, mode) + '<br>' + check['scopes'][mode]['state'].replace('close', 'inconclusive')
        result = endpoint(win, axis, mode, link_prefix)
        if include_oneshot and win:
            result += '<br>One-shot: ' + native(win, 'oneshot')
        field = 'keys' if axis == 'keys' else 'bytes'
        uncertain = [r for r in rows if win and r['case']['background'] == 'technical'
            and r['case']['operation'] == op and r['case']['condition'] == ('absent' if op == 'any' else 'single')
            and r['case']['bytes' if axis == 'keys' else 'keys'] == (fixed_bytes if axis == 'keys' else 48)
            and (not loss or r['case'][field] > loss['case'][field]) and r['case'][field] < win['case'][field]
            and r['scopes'][mode]['state'] in ['flagged', 'close']]
        if uncertain:
            result += '<br>Intermediate observations:<br>' + '<br>'.join(endpoint(r, axis, mode, link_prefix)
                for r in sorted(uncertain, key=lambda r:r['case'][field]))
        if reversal:
            result += '<br>A larger tested input loses again'
        lines.append('| `' + study.OPS[op] + '`; ' + condition + ' | ' + endpoint(loss, axis, mode, link_prefix) + ' | ' + result + ' | ' + repeated + ' |')
    return '\n'.join(lines)


def prepared_matrix(rows, link_prefix=''):
    lines = ['| Operation | 128 B | 256 B | 1 KiB | 4 KiB |', '|---|---|---|---|---|']
    for op in study.OPS:
        cells = []
        for byte_size in [128, 256, 1024, 4096]:
            group = sorted((r for r in rows if r['case']['background'] == 'technical'
                and r['case']['operation'] == op and r['case']['bytes'] == byte_size), key=lambda r:r['case']['keys'])
            assert [r['case']['keys'] for r in group] == [8, 16, 32, 48]
            cells.append('<br>'.join('[' + str(r['case']['keys']) + ': ' + native(r, 'prepared')
                + '](' + link_prefix + f'TIMINGS.md#{op}-b{byte_size})' for r in group))
        condition = 'no matches' if op == 'any' else 'replacements: 1' if op == 'replace' else 'one occurrence'
        lines.append('| `' + study.OPS[op] + '`; ' + condition + ' | ' + ' | '.join(cells) + ' |')
    return '\n'.join(lines)


def prepared_starting_table(rows, link_prefix=''):
    lines = ['| Operation | Best measured existing, µs | Prepared, µs | Decision |', '|---|---|---:|---|']
    for op in study.OPS:
        row = next(r for r in rows if r['case']['background'] == 'technical' and r['case']['operation'] == op
                   and r['case']['bytes'] == 128 and r['case']['keys'] == 8)
        label = '`' + study.OPS[op] + '`' + ('; replacements: 1' if op == 'replace' else '')
        lines.append('| [' + label + '](' + link_prefix + 'inputs/cases/' + row['case']['id'] + '.json) | '
            + reference(row) + ' | ' + native(row, 'prepared') + ' | ' + row['scopes']['prepared']['state'].replace('close', 'inconclusive') + ' |')
    return '\n'.join(lines)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--results', type=Path, required=True)
    parser.add_argument('--environment', type=Path, required=True)
    args = parser.parse_args()
    assert (args.results / 'time-done.json').exists()
    assert (args.results / 'counters-done.json').exists()
    identity = study.read(args.results / 'identity.json')
    for name, digest in identity['files'].items():
        assert study.sha(ROOT / name) == digest, name
    primary_rows = [study.read(p) for p in sorted((args.results / 'timings').glob('*.json'))]
    confirmations = [study.read(p) for p in sorted((args.results / 'confirmations').glob('*.json'))]
    chosen = {r['case']['id']: r for r in primary_rows}
    for row in confirmations:
        if all(s['qualified'] for s in row['scopes'].values()):
            chosen[row['case']['id']] = row
    rows = list(chosen.values())
    short_path = ROOT / 'short-256/data/timings.json.gz'
    short_rows, short_summary = [], None
    if short_path.exists():
        with gzip.open(short_path, 'rt') as stream:
            short_data = json.load(stream)
        short_rows = [r for r in short_data['points'] if r['case']['bytes'] == 256]
        short_summary = study.read(ROOT / 'short-256/data/summary.json')
    grid_path = ROOT / 'prepared-grid/data/timings.json.gz'
    grid_rows, grid_summary = [], None
    if grid_path.exists():
        with gzip.open(grid_path, 'rt') as stream:
            grid_rows = json.load(stream)['points']
        grid_summary = study.read(ROOT / 'prepared-grid/data/summary.json')
    counters = [study.read(p) for p in sorted((args.results / 'counters').glob('*.json'))]
    assert len(rows) == len(counters) <= study.read(ROOT / 'plan.json')['max_measured_inputs']
    assert all(r['fingerprint'] == identity['fingerprint'] for r in rows + counters)
    data = ROOT / 'data'
    data.mkdir(exist_ok=True)
    for row in rows:
        study.save(ROOT / 'inputs/cases' / (row['case']['id'] + '.json'), row['case'])
    pack(data / 'timings.json.gz', {'identity': identity, 'points': rows, 'primary_points': primary_rows, 'confirmations': confirmations})
    pack(data / 'counters.json.gz', {'identity': identity, 'points': counters})
    captures = [{**study.read(p), 'capture_file': p.name} for p in sorted((args.results / 'captures').glob('*.json')) if not p.name.endswith('.config.json')]
    pack(data / 'captures.json.gz', captures)
    study.save(data / 'selection.json', study.read(args.results / 'selection.json'))
    if (args.results / 'followup-policy.json').exists():
        policy = study.read(args.results / 'followup-policy.json')
        assert study.sha(ROOT / 'followup.py') == policy['followup_sha256']
        study.save(data / 'followup-policy.json', policy)
    if (args.results / 'last-gap-probe.json').exists():
        probe = study.read(args.results / 'last-gap-probe.json')
        assert study.sha(ROOT / 'probe.py') == probe['script_sha256']
        study.save(data / 'last-gap-probe.json', probe)
    qualified = sum(r['scopes'][m]['qualified'] for r in rows for m in ['prepared', 'oneshot'])
    counter_qualified = sum(m['qualified'] for c in counters for m in c['methods'].values())
    counter_total = sum(len(c['methods']) for c in counters)
    summary = {'inputs': len(rows), 'native_comparisons': 2 * len(rows), 'qualified_native_comparisons': qualified,
               'counter_results': counter_total, 'qualified_counter_results': counter_qualified,
               'correctness_comparisons': sum(r['correctness_comparisons'] for r in rows),
               'mutation_detected': study.read(args.results / 'mutation.json')['detected'], 'compiler': 'gcc14',
               'quality_confirmations': len(confirmations)}
    study.save(data / 'summary.json', summary)
    environment = study.read(args.environment)
    build = environment['compilers']['gcc14']
    public_build = {k: v for k, v in build.items() if k not in ['php', 'module', 'build_command']}
    public_build.update(cpu='Intel Core i7-13700H', logical_cpu=identity['cpu'], smt_sibling=identity['sibling'])
    study.save(data / 'build.json', public_build)
    lines = ['# Timings: every selected input', '',
             '[Boundary summary](README.md) · [Method](METHOD.md) · [Quality](QUALITY.md)', '',
             'Both native lifetimes share one existing-method capture. Percentages use the displayed medians. † marks a failed quality check.', '',
             '| Operation and exact input | Best existing, µs | Prepared, µs | One-shot, µs | Paired decision: prepared / one-shot |',
             '|---|---|---:|---:|---|']
    for row in rows:
        lines.append('| `' + study.OPS[row['case']['operation']] + '`; ' + row['case']['background'] + '; ' + input_link(row) + ' | ' + reference(row)
            + ' | ' + native(row, 'prepared') + ' | ' + native(row, 'oneshot') + ' | '
            + row['scopes']['prepared']['state'] + ' / ' + row['scopes']['oneshot']['state'] + ' |')
    (ROOT / 'TIMINGS.md').write_text('\n'.join(lines) + '\n')
    quality = ['# Quality checks and uncertain points', '',
               f"{qualified} of {2 * len(rows)} native timing comparisons passed. Both modes have separate A/A controls and share the reference samples.", '',
               'A win requires a paired median below 0.98 and every paired ratio below 1. A loss requires a median above 1.02 and every ratio above 1. Other qualified results are close. Flagged observations retain their time and measured relative change; the flag describes measurement quality.', '',
               f"The primary collector allows two attempts. {len(confirmations)} uncertain boundary inputs received one additional quality confirmation under the saved follow-up policy. A confirmation replaces the summary capture only when both modes pass; all original attempts remain in the raw data. No fastest-attempt selection is used.", '',
               '| Input | Mode | State | Flags | Measured variability | Paired native/reference min–max |', '|---|---|---|---|---|---:|']
    for row in rows:
        for mode, stat in row['scopes'].items():
            detail = quality_detail(row, mode, study.read(args.results / 'captures' / row['capture']))
            quality.append(f"| {row['case']['id']} | {mode} | {stat['state']} | {', '.join(stat['flags']) or 'none'} | {detail} | {stat['paired_min']:.4f}–{stat['paired_max']:.4f} |")
    quality += ['', '## Hardware counters', '',
                f'{counter_qualified} of {counter_total} method results passed all five 0/N pairs. A failed pair flags its median independently of timing quality. Events must run for at least 99% of the interval; corrected counts must be positive and sibling load at most 2%. Raw pairs identify the failed checks.']
    quality += ['', '## Faster time with more cycles or instructions', '',
                'Only comparisons passing both timing and relevant counter checks are listed. Ratios below 1 favor the native operation. A lower elapsed time does not imply fewer instructions; these measurements do not identify the cause of different instruction throughput.', '',
                '| Input | Mode | Paired elapsed native/reference | Cycles native/reference | Instructions native/reference |',
                '|---|---|---:|---:|---:|']
    counter_by_id = {p['case']: p for p in counters}
    for row in rows:
        methods = counter_by_id[row['case']['id']]['methods']
        ref = methods[row['reference']]
        for mode in ['prepared', 'oneshot']:
            own = methods[mode]
            if not (row['scopes'][mode]['qualified'] and own['qualified'] and ref['qualified']):
                continue
            ratios = [own['median'][e] / ref['median'][e] for e in ['cpu_core/cycles/u', 'cpu_core/instructions/u']]
            elapsed = row['scopes'][mode]['paired_ratio']
            if any((elapsed < .98 and ratio > 1.02) or (elapsed > 1.02 and ratio < .98) for ratio in ratios):
                quality.append(f"| {row['case']['id']} | {mode} | {elapsed:.3f} | {ratios[0]:.3f} | {ratios[1]:.3f} |")
    (ROOT / 'QUALITY.md').write_text('\n'.join(quality) + '\n')
    lines = ['# Cycles and instructions: every implementation', '',
             'Five alternating 0/N pairs per implementation; median after subtraction and division by N. † means at least one pair failed quality checks. Captures are separate from elapsed timing.', '',
             '| Input | Implementation | Cycles/job | Instructions/job |', '|---|---|---:|---:|']
    by_id = {r['case']['id']: r for r in rows}
    for point in counters:
        for method, result in point['methods'].items():
            marker = '' if result['qualified'] else '†'
            lines.append('| ' + point['case'] + ' | ' + study.method_name(method, by_id[point['case']]['case']['operation']) + ' | '
                + f"{result['median']['cpu_core/cycles/u']:.1f}" + marker + ' | ' + f"{result['median']['cpu_core/instructions/u']:.1f}" + marker + ' |')
    (ROOT / 'COUNTERS.md').write_text('\n'.join(lines) + '\n')
    lines = ['# Matcher and Replacer: measured break-even points', '',
             '9 November 2026. GCC 14.2, Intel Core i7-13700H. The saved dictionary has 48 case-sensitive literal keys of 3–18 B; smaller dictionaries preserve its order. Controlled derived texts test when one-shot and prepared calls beat existing PHP/PCRE implementations. These are measured configurations, not universal thresholds.', '',
             '[Prepared grid](prepared-grid/README.md) · [One-shot length study](TIMINGS.md) · [256-byte one-shot checks](short-256/README.md) · [Cycles and instructions](COUNTERS.md) · [Quality](QUALITY.md) · [Method and source inputs](METHOD.md) · [Build identity](data/build.json)', '',
             f"The length and 4 KiB search measured {len(rows)} inputs: {qualified} of {2 * len(rows)} native comparisons passed timing quality checks. All selected inputs passed independent expected-output checks, and a deliberately wrong expected output was rejected.", '',
             '## One-shot: text length with 48 keys', '',
             'Includes object construction, operation, result release and destruction. Existing arguments and compiled PCRE caches are already prepared. Counterexamples and close results remain in the full tables.', '',
             '**Reading the one-shot table:** each row compares the nearest smaller confirmed loss with the smallest tested win for the same operation and 48 keys. Values between tested lengths remain unknown. The last column checks the winning configuration on a second text. Percentages use the displayed medians; win/loss decisions use paired samples.', '',
             boundary_table(rows, 'length', 'oneshot'), '',
             '## Prepared: dictionary size on short and longer texts', '',
             'Prepared times exclude construction and destruction. Each winning cell also shows one-shot time against the same reference, including both costs. Smaller dictionaries are ordered prefixes of the same set. These points establish when a call wins; they do not establish how many calls repay construction.', '',
             '### 4 KiB', '',
             boundary_table(rows, 'keys', 'prepared', include_oneshot=True), '',
             '## Presence checks: the same dictionary, different match positions', '',
             'All three controls use a 64 KiB text and the same 48-key dictionary. The matching key is #25. Both native and existing algorithms can stop early; their stopping conditions differ.', '',
             '| Match starts at byte | Text | Best existing, µs | Prepared, µs | One-shot, µs |', '|---:|---|---|---:|---:|']
    for row in sorted((r for r in rows if r['case']['background'] == 'technical' and r['case']['condition'] in ['early', 'middle', 'late']), key=lambda r:r['case']['first_offset']):
        lines.append(f"| {row['case']['first_offset']} | {input_link(row)} | {reference(row)} | {native(row, 'prepared')} | {native(row, 'oneshot')} |")
    lines += ['', '## Limits and reproduction', '',
              'Zero or one occurrence is held fixed; this series does not measure dense results. Technical prose and comment text have different byte distributions. A failed second-text check or a later reversal limits the recommendation to the confirmed input. Close or flagged points cannot establish a losing endpoint.', '',
              '[Reproduction commands](REPRODUCE.md), the [plan](plan.json), [collector](study.py), [harness](harness.php), exact input JSONs and [raw captures](data/captures.json.gz) are saved. No AMD or earlier application timings are merged.']
    # Put input-specific conclusions before the technical tables.
    findings = []
    if short_rows and not grid_rows:
        description = []
        for op, label in [('any', 'no-match presence checks'), ('unique', 'unique-key reporting'), ('count', 'counting'), ('replace', 'replacement')]:
            _, win, _, _ = boundary(short_rows, op, 'keys', 'prepared', fixed_bytes=256)
            if win:
                description.append((win['case']['keys'], label))
        groups = {}
        for n, label in description:
            groups.setdefault(n, []).append(label)
        wins_text = '; '.join(str(n) + ' keys for ' + ', '.join(labels) for n, labels in sorted(groups.items()))
        if not any(r['scopes']['oneshot']['state'] == 'win' for r in short_rows):
            findings += ['On 256-byte texts, no tested input produced a confirmed one-shot win. The first confirmed prepared wins on the primary text were ' + wins_text + '.']
        _, short_all_win, short_all_check, _ = boundary(short_rows, 'all', 'keys', 'prepared', fixed_bytes=256)
        if short_all_win and short_all_check and short_all_check['scopes']['prepared']['state'] == 'loss':
            findings += [f"The {short_all_win['case']['keys']}-key prepared `matchAll()` win on 256 bytes did not repeat on the second text."]
    reporting = [boundary(rows, op, 'length', 'oneshot') for op in ['unique', 'count', 'all']]
    if all(win and win['case']['bytes'] == 4096 and low and low['case']['bytes'] == 2048
           and check and check['scopes']['oneshot']['state'] == 'win' for low, win, check, rev in reporting):
        findings += ['With 48 keys and one occurrence, one-shot unique-key reporting, counting and listing all win at 4 KiB and lose at 2 KiB. The 4 KiB wins also passed on the second text, although the smallest gains are only a few percent.']
    low, win, check, rev = boundary(rows, 'any', 'length', 'oneshot')
    if low and win:
        findings += [f"A one-shot presence check first wins at {size(win['case']['bytes'])} with no matches. That result does not extend to early matches: on the 64 KiB control with a hit at byte 8, PCRE remains much faster than creating a Matcher."]
    low, win, check, rev = boundary(rows, 'replace', 'length', 'oneshot')
    if low and win:
        findings += [f"For one replacement with 48 rules, one-shot Replacer loses at {size(low['case']['bytes'])} and wins at {size(win['case']['bytes'])}."]
    small = [r for r in rows if r['case']['background'] == 'technical' and r['case']['keys'] == 48 and r['case']['bytes'] == 128]
    if not grid_rows and len(small) == 5 and all(r['scopes']['prepared']['state'] == 'win' for r in small):
        findings += ['All five prepared operations already win on the primary 128-byte inputs with 48 keys. Smaller texts were not measured.']
    _, _, check, _ = boundary(rows, 'unique', 'keys', 'prepared')
    if not grid_rows and check and check['scopes']['prepared']['state'] == 'loss':
        findings += [f"The prepared unique-key result changes winner between texts at {check['case']['keys']} keys: it wins on the primary text and loses on the second. Key count and text length alone do not determine which method is faster."]
    insertion = lines.index('## One-shot: text length with 48 keys')
    lines[insertion:insertion] = ['## What these results tell you', ''] + [item for finding in findings for item in [finding, '']]
    if short_rows:
        introduction = next(i for i, line in enumerate(lines) if line.startswith('**Reading the one-shot table:**'))
        lines[introduction:introduction] = [f"The 256-byte slice measured {short_summary['short_inputs']} short inputs and one separate 4 KiB count-baseline control; {short_summary['qualified_native_comparisons']} of {short_summary['native_comparisons']} timing comparisons passed. [Its quality register](short-256/QUALITY.md) and samples remain separate.", '']
        at = lines.index('### 4 KiB')
        short_control = next((r for r in short_data['points'] if r['case']['bytes'] == 4096 and r['case']['operation'] == 'count'), None)
        control_text = ' Its separate 4 KiB check leaves the one-shot count result unchanged.' if short_control and short_control['scopes']['oneshot']['state'] == 'win' else ''
        lines[at:at] = ['### 256 B', '',
            'This slice also measures an overlap-safe `substr_count()`/`strpos()` counting recipe.' + control_text + ' [Full short-text tables and counting control](short-256/README.md).', '',
            boundary_table(short_rows, 'keys', 'prepared', fixed_bytes=256, link_prefix='short-256/', include_oneshot=True), '']
    if grid_rows:
        # Replace isolated prepared boundary pairs with the complete N-by-length study.
        begin = lines.index('## Prepared: dictionary size on short and longer texts')
        end = lines.index('## Presence checks: the same dictionary, different match positions')
        lines[begin:end] = ['## Prepared objects: which dictionary wins at each text length?', '',
            'Objects are constructed before timing. Each call includes result creation, consumption and release. Every length tests 8, 16, 32 and 48 keys with the same dictionary order. Replacer performs exactly one replacement in every row, regardless of dictionary size.', '',
            '**Each entry is key count: prepared time in µs (observed change against the best measured existing method).** Negative means faster; positive means slower. † marks a quality issue and never removes the measured change. Click an entry for the reference name and time; [quality details](prepared-grid/QUALITY.md) give the actual sample spread and A/A deviation.', '',
            prepared_matrix(grid_rows, 'prepared-grid/'), '',
            '### Starting point: 128 B and 8 keys', '',
            'The presence check has no matches. Each other operation has one occurrence; Replacer makes one replacement and returns 122 bytes. Construction and destruction are excluded.', '',
            prepared_starting_table(grid_rows, 'prepared-grid/'), '',
            '[Full prepared grid, second-text checks and raw captures](prepared-grid/README.md). This is a prepared-call study; it does not measure how many calls repay construction.', '']
        start_rows = [r for r in grid_rows if r['case']['background'] == 'technical'
            and r['case']['bytes'] == 128 and r['case']['keys'] == 8]
        start_rows.sort(key=lambda r: list(study.OPS).index(r['case']['operation']))
        labels = {'any': 'presence checking', 'unique': 'unique-key reporting', 'count': 'counting',
                  'all': 'listing occurrences', 'replace': 'replacement'}
        parts = []
        for state, ending in [('win', 'won'), ('close', 'was inconclusive'), ('loss', 'lost'), ('flagged', 'failed timing quality checks')]:
            names = [labels[r['case']['operation']] for r in start_rows if r['scopes']['prepared']['state'] == state]
            if names:
                parts.append(', '.join(names) + ' ' + ending)
        early = ['For prepared objects, the explicit starting point is 128 B / 8 keys: ' + '; '.join(parts) + '. The grid below shows all tested dictionary sizes at 128 B, 256 B, 1 KiB and 4 KiB.', '']
        checks = [r for r in grid_rows if r['case']['background'] == 'comments']
        checks.sort(key=lambda r: list(study.OPS).index(r['case']['operation']))
        if len(checks) == 5 and all(r['scopes']['prepared']['state'] == 'win' for r in checks):
            tested = '; '.join(str(n) + ' keys for ' + ', '.join(labels[r['case']['operation']] for r in checks if r['case']['keys'] == n)
                for n in sorted({r['case']['keys'] for r in checks}))
            early += ['At 128 B, the smallest confirmed winning dictionaries also won on the second text: ' + tested + '.', '']
        flagged_grid = grid_summary['timing_comparisons'] - grid_summary['qualified_timing_comparisons']
        if flagged_grid:
            early += [f'{flagged_grid} of {grid_summary["timing_comparisons"]} prepared comparisons have quality flags. Their observed times and relative changes remain in every table; sample spread and A/A deviation are reported separately.', '']
        if short_rows and not any(r['scopes']['oneshot']['state'] == 'win' for r in short_rows):
            early += ['No tested 256-byte input produced a confirmed one-shot win. A fast prepared call alone does not pay the cost of creating a new object for each text.', '']
        at = lines.index('## What these results tell you') + 2
        lines[at:at] = early
        # Keep sample-quality counts with the source cohorts, away from the conclusions.
        length_line = next(line for line in lines if line.startswith('The length and 4 KiB search measured '))
        short_line = next((line for line in lines if line.startswith('The 256-byte slice measured ')), '')
        for line in [length_line, short_line]:
            if line:
                lines.remove(line)
        footer = lines.index('## Limits and reproduction')
        lines[footer:footer] = ['## Measurement sets and quality', '',
            f"Prepared grid: {grid_summary['primary_inputs']} primary comparisons and {grid_summary['validation_inputs']} second-text checks; {grid_summary['qualified_timing_comparisons']} of {grid_summary['timing_comparisons']} passed. [Quality register](prepared-grid/QUALITY.md).", '',
            length_line, '', short_line, '',
            'The extension build is shared; captures and their quality checks remain separate. Timings from different cohorts are not averaged together.', '']
    content = '\n'.join(lines) + '\n'
    while '\n\n\n' in content:
        content = content.replace('\n\n\n', '\n\n')
    (ROOT / 'README.md').write_text(content)
    print(json.dumps(summary, indent=2))


if __name__ == '__main__':
    main()
