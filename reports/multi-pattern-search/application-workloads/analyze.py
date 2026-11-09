#!/usr/bin/env python3
"""Generate exact-input tables and public evidence from completed captures."""
import argparse
import gzip
import hashlib
import json
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parent
NAMES = {'native': 'Matcher/Replacer', 'string_loop': 'stripos()/strpos() loop',
         'folded_string_loop': 'strtolower() + strpos() loop', 'preg_literal': 'literal PCRE',
         'preg_trie': 'prefix-factored PCRE', 'strtr': 'strtr()', 'str_replace': 'str_replace()',
         'preg_literal_callback': 'literal PCRE callback', 'preg_trie_callback': 'prefix-factored PCRE callback',
         'preg_tokens_callback': 'placeholder PCRE + lookup'}
OPS = {'any': 'Matcher::matches()', 'unique': 'Matcher::getMatchedKeywords()',
       'count': 'Matcher::countMatches()', 'all': 'Matcher::matchAll()', 'replace': 'Replacer::replace()'}


def method_name(method, case):
    if method == 'string_loop':
        return ('stripos()' if case['policy'] == 'ascii-insensitive' else 'strpos()') + ' loop'
    if method == 'native':
        return OPS[case['operation']]
    if method in ['preg_literal', 'preg_trie']:
        function = 'preg_match()' if case['operation'] == 'any' else 'preg_match_all()'
        return function + (' [prefix]' if method == 'preg_trie' else ' [literal]')
    if method in ['preg_literal_callback', 'preg_trie_callback', 'preg_tokens_callback']:
        return 'preg_replace_callback() [' + {'preg_literal_callback': 'literal', 'preg_trie_callback': 'prefix', 'preg_tokens_callback': 'tokens'}[method] + ']'
    return NAMES[method]


def export_capture(path):
    raw = json.loads(path.read_text())
    config = json.loads(path.with_name(path.stem + '.config.json').read_text())
    raw['run_configuration'] = {k: v for k, v in config.items() if k not in ['case', 'documents', 'dictionary']}
    raw['run_configuration'].update(case_id=config['case']['id'], dictionary_id=config['case']['dictionary'])
    raw['command'] = ['<PHP_MODULE_AND_INPUT_PATHS>' if '/home/' in token else token for token in raw['command']]
    raw['capture_file'] = path.name
    return raw


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def save(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')


def packed(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    with gzip.GzipFile(filename=str(path), mode='wb', mtime=0) as stream:
        stream.write((json.dumps(value, ensure_ascii=False, separators=(',', ':')) + '\n').encode())


def display(row, reference=None):
    reference = reference or row
    observed = f"{row['median_us']['native']:.3f}"
    ratio = row['median_us']['native'] / reference['median_us'][reference['reference']]
    delta = f"{ratio:.1f} times slower" if ratio >= 2 else f"{100 * (ratio - 1):+.2f}%"
    marker = '' if row['qualified'] and reference['qualified'] else '†'
    return observed + ' (' + delta + ')' + marker


def text_size(size):
    if size < 1024:
        return f'{size:,} B'
    return f'{size / 1024:.2f}'.rstrip('0').rstrip('.') + ' KiB'


def label(case, corpus):
    link = 'inputs/cases/' + case['id'] + '.json'
    if 'batch_size' in case:
        documents = 'document' if case['batch_size'] == 1 else 'different documents'
        keys = len(corpus['dictionaries'][case['dictionary']]['keys'])
        details = f"{case['batch_size']} {documents}; {text_size(case['total_bytes'])} total; {keys} keys"
        if case['operation'] == 'replace':
            members = {c['documents'][0]: c for c in corpus['cases']
                       if c['operation'] == 'replace' and c['dictionary'] == case['dictionary'] and 'batch_size' not in c}
            replacements = sum(members[doc]['input']['replacements'] for doc in case['documents'])
            details += f'; replacements: {replacements} total'
        return f"[{OPS[case['operation']]} · {details}]({link})"
    stats = case['input']
    subject = ('HTML template' if case['documents'][0].endswith('.html') else 'plain-text template') if case['family'] == 'email' else 'text (EN)'
    text = f"{OPS[case['operation']]} · {subject}; {text_size(stats['bytes'])}; {stats['keys']} keys"
    if case['operation'] == 'replace':
        text += f"; {stats['replacements']} replacements; output {text_size(stats['output_bytes'])}"
    elif case['operation'] == 'any':
        text += '; no matches' if not stats['occurrences'] else f"; first match at byte {stats['first_offset']}; matching key is #{stats['matched_dictionary_ranks'][0]} in dictionary order"
    else:
        text += f"; occurrences: {stats['occurrences']}; unique matched keys: {stats['unique_matched_keys']}"
    return '[' + text + '](' + link + ')'


def comparison_table(cases, rows, corpus):
    lines = ['| Input | Best existing method, µs | Prepared, µs | One-shot, µs |',
             '|---|---|---:|---:|']
    for case in cases:
        reference = rows.get((case['id'], 'oneshot')) or rows[(case['id'], 'prepared')]
        objects = {}
        for scope in ['prepared', 'oneshot']:
            row = rows.get((case['id'], scope))
            if row:
                objects[scope] = display(row, reference)
        baseline = '`' + method_name(reference['reference'], case) + '` ' + f"{reference['median_us'][reference['reference']]:.3f}" + ('' if reference['qualified'] else '†')
        lines.append('| ' + label(case, corpus) + ' | ' + baseline + ' | '
                     + objects.get('prepared', '—') + ' | ' + objects.get('oneshot', '—') + ' |')
    return '\n'.join(lines) + '\n'


def batch_table(cases, rows, corpus):
    lines = ['| Exact batch | Best existing: total µs | Object: total µs |', '|---|---|---:|']
    for case in cases:
        row = rows[(case['id'], 'batch')]
        lines.append('| ' + label(case, corpus) + ' | `' + method_name(row['reference'], case) + '` '
                     + f"{row['median_us'][row['reference']]:.3f}" + ' | ' + display(row) + ' |')
    return '\n'.join(lines) + '\n'


def overview(corpus, rows, memory, summary, build):
    by_id = {case['id']: case for case in corpus['cases']}
    panels = [
        ('Matcher: short texts and 403 keys', ['comment.69493.any', 'comment.55617.any', 'comment.69522.any']),
        ('Matcher and Replacer: complete texts and 48 keys', ['document.robotparser.unique', 'document.collections.unique',
            'document.collections.count', 'document.collections.all', 'document.robotparser.replace', 'document.collections.replace']),
        ('Replacer: email templates and 10 keys', ['email.receipt.html', 'email.receipt.txt'])]
    lines = ['# Matcher and Replacer: results on open-data texts', '',
        'Standard PHP functions, PCRE and Matcher/Replacer compared on comments, complete documents and email templates. Measured on 9 November 2026: Intel Core i7-13700H, Linux x86-64, GCC 14.2. These samples are separate from the AMD study.', '',
        '[All comparisons](TIMINGS.md) · [Every recipe](RECIPES.md) · [Hardware counters](COUNTERS.md) · [Memory](MEMORY.md) · [Quality](QUALITY.md) · [Source identity and licenses](SOURCE.md) · [Reproduce](REPRODUCE.md)', '',
        '## Tasks and inputs', '',
        '| Task | Saved inputs | Dictionary and policy |', '|---|---|---|',
        '| Comment checks: presence and unique keys | 16 individual comments; batches use 64 distinct comments from Civil Comments | All 403 English LDNOOBW entries, 2–27 bytes; ASCII-insensitive literal substrings |',
        '| Document searches: unique keys, count and all occurrences | 16 complete CPython documentation source files | 48 names, 3–18 bytes, from the existing lib2to3 mapping; case-sensitive literals |',
        '| Literal document rewriting | The same 16 complete files | The same old-name/new-name mapping; leftmost-longest replacement |',
        '| Email substitution | 12 Groundmail template families, HTML and text: 24 inputs | Existing placeholders and deterministic example values; 2–10 keys |', '',
        f"{summary['single_document_cases']} single-document tasks and {summary['batch_cases']} batch tasks produce {summary['timing_points']} comparisons: 96 single-document tasks have two object lifetimes; 24 email tasks have one. Inputs, dictionary order and batch membership were fixed before timing. Texts are unchanged; no matches were inserted. [Corpus and selection](DESIGN.md).", '',
        '## Findings: when preparation pays', '',
        '**Creating a Matcher for each of these short messages is slower.** With the 403-key dictionary, creating and destroying the object costs more than the search saves. On the 985-byte negative input, PCRE takes about 14 µs and a new Matcher about 298 µs. The prepared Matcher takes about 2 µs, but that alone does not pay for creating it.', '',
        '**Reuse can make short-message searches worthwhile, depending on the result needed.** Getting unique matched keys from 16 different comments with one Matcher is 48% faster than the best measured alternative, including construction and destruction. A presence check with `matches()` still shows no advantage at 64 comments. The tests establish these batch results, not an exact break-even count.', '',
        '**Matcher can pay for itself on a single document.** On the 40.48 KiB text with 48 keys and 10 occurrences, unique-key reporting, counting and listing occurrences are each faster even with construction and destruction included. On the 2.14 KiB text, one-shot unique-key reporting is slower. Long-running workers are therefore one useful setting, not a requirement for a benefit.', '',
        '**Replacer also has useful one-shot cases.** Replacing 10 occurrences in the 40.48 KiB text with 48 rules is 39% faster than the best measured alternative, including object creation. On the 2.14 KiB text with the same rules, one-shot Replacer is 2.9 times slower. These are different texts; they do not establish a size threshold.', '',
        '**For these small email dictionaries, use existing functions.** Every email comparison that passed quality checks favors a standard function or PCRE. In the displayed HTML template with 10 keys and 15 replacements, one-shot Replacer is 13.2 times slower. Replacement values vary between messages, so one unchanged Replacer cannot be reused for this task.', '',
        '## Selected results', '',
        'The rows show the smallest and largest single texts, one positive comment, and HTML/text versions of one template. Selection uses input properties, not timings. [More selected inputs](SUMMARY-TABLE.md) include the text with 198 occurrences. Each row links to the exact text, dictionary and expected result.', '',
        '**Prepared** excludes object construction. **One-shot** includes construction and destruction. Both include required preprocessing and result creation, consumption and release. For ASCII-insensitive checks, Matcher pays for `strtolower()` inside the timer; alternatives can use `stripos()` or PCRE `/i`. Replacer is called without the optional count argument.', '',
        'Existing functions use prebuilt arguments and warm PCRE caches. Both object columns use the one displayed reference time, selected from the one-shot series. Percentages are ratios of medians; negative means faster. Changes below 2% are treated as close. † marks a quality issue with the object or reference; the observed time and relative change are always shown. [Measured variability](QUALITY.md) and [sampling](SOURCE.md).', '',
        f"{summary['timing_qualified']} of {summary['timing_points']} timing comparisons passed quality checks; {summary['timing_flagged']} remain flagged. Hardware counters have separate checks: {summary['counter_recipe_captures_qualified']} of {summary['counter_recipe_captures']} method results passed. [Affected results](QUALITY.md).", '']
    for title, ids in panels:
        lines += ['### ' + title, '', comparison_table([by_id[i] for i in ids], rows, corpus), '']
    ids = ['batch.validation.any.b1', 'batch.validation.any.b16', 'batch.validation.any.b64',
           'batch.validation.unique.b1', 'batch.validation.unique.b4', 'batch.validation.unique.b16', 'batch.validation.unique.b64',
           'batch.rewrite.replace.b1', 'batch.rewrite.replace.b4', 'batch.rewrite.replace.b16']
    lines += ['## Reuse: one object, different texts', '',
        'Each row includes construction, processing of every listed document, release of each result and destruction. Times are batch totals. Larger batches extend the same saved document order; every member is listed in the linked input.', '',
        batch_table([by_id[i] for i in ids], rows, corpus), '',
        '## Object and result memory', '',
        'Fresh-process Zend allocator measurements, excluding loaded inputs. Constructor peak includes the retained object; method peak is additional to that object and includes preprocessing and results. The peaks occur separately and must not be added. These are not RSS measurements; existing-method memory was not measured.', '',
        '| Exact input | Object retained, B | Constructor peak above inputs, B | Method peak above object, B |', '|---|---:|---:|---:|']
    by_memory = {item['case']: item for item in memory}
    for case_id in ['comment.13.any', 'document.cookielib.all', 'document.collections.replace', 'email.receipt.html']:
        item = by_memory[case_id]
        lines.append('| ' + label(by_id[case_id], corpus) + ' | ' + str(item['object_retained_bytes']) + ' | '
            + str(item['construction_peak_above_input_bytes']) + ' | ' + str(item['method_peak_above_prepared_bytes']) + ' |')
    lines += ['', '`matchAll()` creates one `MatchResult` per occurrence. The largest single-document output has 198 occurrences; thousands or millions of results in one call were not tested. [All memory measurements](MEMORY.md).', '',
        '## Correctness and limits', '',
        'An independent Python oracle computes expected occurrences, their order and leftmost-longest replacements. Every included implementation must produce the same content. `matchAll()` object-to-array conversion is used only for checking, outside timing. `str_replace()` is included only where its sequential behavior gives the expected result.', '',
        'Correctness checks passed on four release builds: 1,096 comparisons per compiler, 4,384 total. A deliberately wrong expected output was rejected on each. Performance was measured only with GCC 14; other compilers and the initial pilot do not contribute samples.', '',
        'Measurements repeat a fixed text or fixed batch with warm caches. They cover a small set of English-focused sources, not production traffic. They do not measure complete HTTP requests or establish universal text-size or dictionary-size thresholds.', '',
        'Banword checks are literal substring searches, not word-boundary matching or toxicity classification. Document rewriting can alter substrings inside prose and identifiers; it is not semantic code migration. Email values are deterministic fixtures supplied ready for substitution; escaping and delivery are excluded. Exact source identities and runtime settings, including PCRE JIT limitations, are in [SOURCE](SOURCE.md).']
    (ROOT / 'README.md').write_text('\n'.join(lines) + '\n')

    source = ['# Builds, sources and measurement method', '',
        'Matcher and Replacer use the same strmatch module. The release PHP CLI and module were built separately with GCC 14.2; their source and binary identities are recorded below.', '',
        '| Component | Exact identity |', '|---|---|',
        '| PHP CLI source commit | `' + build['build']['commit'] + '` |',
        '| PHP CLI SHA-256 | `' + build['php_sha256'] + '` |',
        '| Extension source SHA-256 | `' + build['extension_source_sha256'] + '` |',
        '| Extension module SHA-256 | `' + build['module_sha256'] + '` |',
        '| PHP `main/php_config.h` SHA-256 | `' + build['header_config_sha256'] + '` |', '',
        '[Measured C source](../benchmark/extension/strmatch.c). [Build metadata](data/build.json) includes configure options, compiler flags and runtime versions. The module uses headers configured from the CLI\'s PHP commit. The collector verifies binary hashes before measuring.', '',
        'Intel Core i7-13700H, Linux x86-64; logical P-core 2, SMT sibling 3. Locale `C`; GC, PHP JIT and OPcache disabled in the timing harness. PCRE JIT is enabled, but individual patterns were not checked for JIT execution.', '',
        'The collector records sibling load, temperatures and CPU steal. AC was observed connected; power supply and package power were not continuously logged. Affinity pins execution but does not isolate the CPU from other system activity.', '',
        '## Input snapshots and licenses', '',
        '| Input | Snapshot and attribution | License / saved evidence |', '|---|---|---|',
        '| Civil Comments | [Google dataset](https://huggingface.co/datasets/google/civil_comments); test rows at offsets recorded in corpus.json, acquired 2026-11-09 | Dataset card declares CC0-1.0; the saved text and SHA-256 identify each acquired row |',
        '| English banword dictionary | LDNOOBW / Shutterstock, Inc.; `5faf2ba42d7b1c0977169ec3611df25a3c08eb13` | [CC BY 4.0](sources/banwords/LICENSE); [attribution](sources/banwords/ATTRIBUTION.md) |',
        '| Complete documentation and rename mapping | Python Software Foundation and contributors; `8d21aa21f2cbc6d50aab3f420bb23be1d081dac4` | [Complete CPython license](sources/python/LICENSE), including its historical terms |',
        '| HTML/text email templates | Groundmail; `5240b4a4de917b4d69bf2725b5441e50cb94a682` | [MIT license](sources/emails/LICENSE) |', '',
        '[corpus.json](corpus.json) records source URLs, Git revisions, byte sizes and SHA-256 hashes. Civil Comments responses did not identify an immutable dataset revision: use the saved row texts and hashes to reproduce these inputs. Later downloads may differ.', '',
        '[DESIGN](DESIGN.md) specifies selection, dictionary transformations and expected-output checks. Every measured case has a self-contained JSON with its texts, ordered dictionary and expected output.', '',
        '## Timing and quality checks', '',
        'Each recipe receives 100 ms warmup and 15 samples targeting 40 ms each. Recipe order rotates and reverses between rounds. A second native object runs the same code as an A/A control. The collector keeps the first attempt passing quality checks, with at most two attempts; if neither passes, it keeps and flags the first. [Thresholds and affected cases](QUALITY.md).', '',
        'Summary percentages compare the native median with the single reference median shown in the row. Raw captures also retain paired sample ratios. The 2% rule for calling a difference close is a reporting convention, not a confidence interval.', '',
        '## PCRE recipes', '',
        '- `literal`: alternatives made from escaped literal keys.',
        '- `prefix`: equivalent alternatives with shared prefixes factored out.',
        '- `tokens`: recognize `{{name}}`, look it up in the replacement map and preserve unknown tokens.', '',
        'Unique/count/all searches use lookahead and group keys by byte length to retain overlapping and nested matches. Unique/all include deduplication or sorting as required. Replacement alternatives select longest matches first and use callbacks to insert literal values without rescanning them. Pattern construction and compilation are outside timing for every PCRE recipe.', '',
        '## Hardware counters', '',
        'Each recipe has five alternating 0/N pairs, with N targeting 30 ms. Subtract the zero-iteration count from the N-iteration count and divide by N to obtain user-mode cycles and instructions per job. Both the collector and PHP are pinned to the P-core. Counter captures and quality checks are separate from elapsed timing.', '',
        '## Raw evidence', '',
        '- [Elapsed points and every attempt](data/elapsed.json.gz)',
        '- [Counter pairs](data/counters.json.gz) and [raw perf observations](data/counter-captures.json.gz)',
        '- [Fresh-process native allocation observations](data/memory.json)',
        '- [Correctness summary](data/checks.json) and [display-selection rule](data/summary-selection.json)', '',
        'Public captures retain samples, diagnostics and collection settings. Local command paths are replaced by placeholders; exact texts are supplied in case JSONs. Timings and counters are unchanged.']
    (ROOT / 'SOURCE.md').write_text('\n'.join(source) + '\n')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--results', type=Path, required=True)
    parser.add_argument('--environment', type=Path, required=True)
    parser.add_argument('--timing-only', action='store_true')
    args = parser.parse_args()
    done = json.loads((args.results / 'time-done.json').read_text())
    identity = json.loads((args.results / 'measurement-identity.json').read_text())
    corpus = json.loads((ROOT / 'corpus.json').read_text())
    environment = json.loads(args.environment.read_text())
    assert sha(ROOT / 'corpus.json') == identity['corpus_sha256']
    assert sha(ROOT / 'harness.php') == identity['harness_sha256']
    assert sha(ROOT / 'run.py') == identity['runner_sha256']
    assert done['points'] == 236
    cases = corpus['cases']
    rows = {}
    for case in cases:
        for scope in case['modes']:
            path = args.results / 'timings' / ('gcc14-' + case['id'] + '-' + scope + '.json')
            row = json.loads(path.read_text())
            assert row['fingerprint'] == identity['fingerprint']
            assert row['reference'] in case['methods']
            rows[(case['id'], scope)] = row
        save(ROOT / 'inputs' / 'cases' / (case['id'] + '.json'), {
            **case, 'dictionary_contents': corpus['dictionaries'][case['dictionary']],
            'document_files': [corpus['documents'][i] for i in case['documents']],
            'document_contents': {i: (ROOT / corpus['documents'][i]['path']).read_text() for i in case['documents']}})
    assert len(rows) == 236
    elapsed_raw = []
    for path in sorted((args.results / 'captures').glob('time-gcc14-*.json')):
        if path.name.endswith('.config.json'):
            continue
        elapsed_raw.append(export_capture(path))
    packed(ROOT / 'data/elapsed.json.gz', {'identity': identity, 'points': list(rows.values()), 'captures': elapsed_raw})
    singles = [case for case in cases if 'batch_size' not in case]
    batches = [case for case in cases if 'batch_size' in case]
    full = ['# Timings: every input and object lifetime', '', '[Summary](README.md) · [Corpus](DESIGN.md) · [Quality](QUALITY.md)', '',
            'Both object columns compare against the one reference median shown in the row, taken from the one-shot series. Each batch has its own reference. † marks a quality issue with the object or reference. [Every implementation and control](RECIPES.md) is retained.', '']
    for family, title in [('validation', 'Matcher: ASCII-insensitive searches in comments'), ('references', 'Matcher: case-sensitive searches in complete texts'),
                          ('rewrite', 'Replacer: literal substitution in complete texts'), ('email', 'Replacer: email templates with changing values')]:
        full += ['## ' + title, '', comparison_table([c for c in singles if c['family'] == family], rows, corpus), '']
    full += ['## Reuse across different texts', '', 'Batch totals include construction once, all B documents and destruction. Each linked input lists every member.', '', batch_table(batches, rows, corpus)]
    (ROOT / 'TIMINGS.md').write_text('\n'.join(full))
    recipes = ['# Timings: every implementation and A/A control', '',
               'Native A/A runs the same code with a separate object. Deviation is the largest absolute sample deviation from the implementation\'s median. The quality column applies to the complete input/mode comparison; [flags](QUALITY.md).', '',
               '| Input | Mode | Recipe | Median, µs/job | Maximum deviation | Comparison qualified |',
               '|---|---|---|---:|---:|---|']
    by_id = {case['id']: case for case in cases}
    for (case_id, scope), row in rows.items():
        for method, median in row['median_us'].items():
            name = 'Native A/A control' if method == 'native_aa' else method_name(method, by_id[case_id])
            recipes.append(f"| [{case_id}](inputs/cases/{case_id}.json) | {scope} | {name} | {median:.3f} | {100 * row['relative_spread'][method]:.2f}% | {'yes' if row['qualified'] else 'no'} |")
    (ROOT / 'RECIPES.md').write_text('\n'.join(recipes) + '\n')
    flagged = [row for row in rows.values() if not row['qualified']]
    quality = ['# Quality checks and flagged results', '', f"{len(rows) - len(flagged)} of {len(rows)} GCC 14 timing comparisons passed; {len(flagged)} remain flagged.", '',
               'Limits: A/A difference 2%; maximum sample deviation from its median 5%; SMT sibling busy time 2%; no CPU steal. With at most two attempts, the collector keeps the first passing attempt or flags the first if neither passes. All attempts are retained.', '',
               'In summary tables, † marks a quality issue in the object or its shared reference. Observed times and relative changes are always retained. Spread is the largest absolute sample deviation from its median.', '',
               '| Exact input | Mode | Flags | A/A change | Sample spread by implementation |', '|---|---|---|---:|---|']
    for row in flagged:
        spreads = ', '.join(m + ': ' + f'{100*v:.2f}%' for m,v in row['relative_spread'].items())
        capture = json.loads((args.results / 'captures' / row['raw']).read_text())
        spreads += f'; SMT busy {capture["sibling_busy_percent"]:.2f}%; CPU steal {capture["cpu_steal_ticks"]} ticks'
        quality.append('| ' + row['case'] + ' | ' + row['scope'] + ' | ' + ', '.join(row['flags']) + ' | ' + f"{row['aa_percent']:+.2f}%" + ' | ' + spreads + ' |')
    (ROOT / 'QUALITY.md').write_text('\n'.join(quality) + '\n')

    # Reporting selection depends only on input metadata, never on elapsed times.
    chosen = []
    def select(options):
        for case in options:
            if case['id'] not in [x['id'] for x in chosen]:
                chosen.append(case)
    comments = [c for c in singles if c['family'] == 'validation' and c['operation'] == 'any']
    select([min(comments, key=lambda c: c['input']['bytes']), max(comments, key=lambda c: c['input']['bytes'])])
    positives = [c for c in comments if c['input']['occurrences']]
    if positives:
        select([min(positives, key=lambda c: c['id'])])
    for operation in ['unique', 'count', 'all', 'replace']:
        options = [c for c in singles if c['family'] in ['references', 'rewrite'] and c['operation'] == operation]
        select([min(options, key=lambda c: c['input']['bytes']), max(options, key=lambda c: c['input']['bytes'])])
        if operation != 'replace':
            select([max(options, key=lambda c: c['input']['occurrences'])])
    select([c for c in singles if c['family'] == 'email' and corpus['documents'][c['documents'][0]]['template_family'] in ['receipt', 'password-reset']])
    save(ROOT / 'data/summary-selection.json', {'rule': 'input-size extremes and largest occurrence count for document searches, one positive comment by ID, both forms of receipt/password-reset; no timing fields used', 'cases': [c['id'] for c in chosen]})
    (ROOT / 'SUMMARY-TABLE.md').write_text('# Selected inputs: size extremes and larger match counts\n\n'
        'Includes a positive comment, the document with 198 occurrences, and both formats of two email templates. '
        'Input selection uses no timings. Modes and the reference rule follow the [main report](README.md).\n\n'
        + comparison_table(chosen, rows, corpus))

    build = environment['compilers']['gcc14']
    public_build = {k: v for k, v in build.items() if k not in ['php', 'module', 'build_command']}
    public_build['build_command'] = ['<LOCAL_PATH>' if '/home/' in x else x for x in build['build_command']]
    cpu_model = next(line.split(':', 1)[1].strip() for line in Path('/proc/cpuinfo').read_text().splitlines() if line.startswith('model name'))
    public_build.update(cpu=cpu_model, system=environment['platform'], logical_cpu=identity['cpu'],
                        smt_sibling=identity['smt_sibling'], gc='disabled in harness', pcre_jit=True, php_jit=False, opcache=False)
    save(ROOT / 'data/build.json', public_build)
    save(ROOT / 'data/checks.json', json.loads((args.results / 'checks.json').read_text()))
    summary = {'timing_points': len(rows), 'timing_qualified': len(rows) - len(flagged),
               'timing_flagged': len(flagged), 'compiler': 'gcc14',
               'single_document_cases': len(singles), 'batch_cases': len(batches),
               'timing_complete': True, 'counters_complete': False, 'memory_complete': False}
    if not args.timing_only:
        counter_done = json.loads((args.results / 'counters-done.json').read_text())
        assert counter_done['points'] == 236
        counters = [json.loads(path.read_text()) for path in sorted((args.results / 'counters').glob('*.json'))]
        assert len(counters) == 236
        assert all(c['fingerprint'] == identity['fingerprint'] for c in counters)
        packed(ROOT / 'data/counters.json.gz', {'points': counters, 'identity': identity})
        counter_raw = []
        for path in sorted((args.results / 'captures').glob('perf-gcc14-*.json')):
            if path.name.endswith('.config.json'):
                continue
            counter_raw.append(export_capture(path))
        packed(ROOT / 'data/counter-captures.json.gz', counter_raw)
        lines = ['# Cycles and instructions per job', '', 'Each median uses five alternating 0/N pairs after subtraction. Captures are separate from elapsed timing. † means at least one pair failed quality checks; [raw pairs](data/counters.json.gz) and [criteria](QUALITY.md) remain available.', '',
                 '| Input | Mode | Recipe | Cycles/job | Instructions/job |', '|---|---|---|---:|---:|']
        by_id = {case['id']: case for case in cases}
        for point in counters:
            for method, data in point['methods'].items():
                marker = '' if data['qualified'] else '†'
                lines.append('| ' + point['case'] + ' | ' + point['scope'] + ' | ' + method_name(method, by_id[point['case']]) + ' | '
                    + f"{data['median']['cpu_core/cycles/u']:.1f}" + marker + ' | '
                    + f"{data['median']['cpu_core/instructions/u']:.1f}" + marker + ' |')
        (ROOT / 'COUNTERS.md').write_text('\n'.join(lines) + '\n')
        memory = []
        memory_dir = args.results / 'memory'
        memory_dir.mkdir(exist_ok=True)
        for case in cases:
            path = memory_dir / (case['id'] + '.json')
            if not path.exists():
                config = args.results / 'captures' / ('check-gcc14-' + case['id'] + '.config.json')
                result = subprocess.run(['taskset', '-c', str(identity['cpu']), build['php'], '-n', '-d', 'extension=' + build['module'],
                    str(ROOT / 'memory.php'), str(config)], capture_output=True, text=True, check=True, timeout=30)
                save(path, json.loads(result.stdout))
            memory.append(json.loads(path.read_text()))
        save(ROOT / 'data/memory.json', memory)
        lines = ['# Memory: retained objects and operation peaks', '', 'Fresh-process Zend allocator bytes, excluding loaded inputs. Constructor peak includes the retained object; method peak is additional to that object, including preprocessing and results. Batch results are released between documents. The peaks must not be added. These are not RSS measurements.', '',
                 '| Input | Object retained, B | Constructor peak above inputs, B | Method peak above prepared object, B |', '|---|---:|---:|---:|']
        for item in memory:
            lines.append('| ' + item['case'] + ' | ' + str(item['object_retained_bytes']) + ' | '
                + str(item['construction_peak_above_input_bytes']) + ' | ' + str(item['method_peak_above_prepared_bytes']) + ' |')
        (ROOT / 'MEMORY.md').write_text('\n'.join(lines) + '\n')
        summary.update(counters_complete=True, memory_complete=True,
                       counter_recipe_captures=sum(len(c['methods']) for c in counters),
                       counter_recipe_captures_qualified=sum(d['qualified'] for c in counters for d in c['methods'].values()))
        invalid_methods = [d for c in counters for d in c['methods'].values() if not d['qualified']]
        sibling_invalid = sum(any(any(v['sibling_busy_percent'] > 2 for v in pair['raw'].values()) for pair in d['pairs']) for d in invalid_methods)
        quality += ['', '## Counter checks: separate from timing checks', '',
                    f"{summary['counter_recipe_captures_qualified']} of {summary['counter_recipe_captures']} method results passed all five 0/N pairs. {len(invalid_methods)} have a failed pair; {sibling_invalid} include SMT sibling load above 2%. One result means one implementation on one input in one mode.", '',
                    'Every pair requires positive corrected cycles and instructions, available events running at least 99% of the interval, and SMT sibling busy time at most 2%. All five pairs must pass. Flagged medians are shown with † without supporting comparative claims. No counter retries were made.', '',
                    '## Where elapsed time and instruction counts disagree', '',
                    'These rows passed timing and counter checks, but time differs by at least 2% in one direction and cycles or instructions by at least 2% in the other. The captures are independent; the table records the disagreement without attributing a cause. Ratios below 1 favor the native implementation.', '',
                    '| Input | Mode | Elapsed native/reference | Cycles native/reference | Instructions native/reference |',
                    '|---|---|---:|---:|---:|']
        disagreements = 0
        for point in counters:
            row = rows[(point['case'], point['scope'])]
            native, reference = point['methods']['native'], point['methods'][row['reference']]
            if not (row['qualified'] and native['qualified'] and reference['qualified']):
                continue
            ratios = [native['median'][event] / reference['median'][event] for event in ['cpu_core/cycles/u', 'cpu_core/instructions/u']]
            ratio = row['paired_ratio']
            if any((ratio < .98 and r > 1.02) or (ratio > 1.02 and r < .98) for r in ratios):
                disagreements += 1
                quality.append(f"| {point['case']} | {point['scope']} | {ratio:.3f} | {ratios[0]:.3f} | {ratios[1]:.3f} |")
        if not disagreements:
            quality += ['', 'No such opposite-direction comparison was observed among results passing both sets of checks.']
        (ROOT / 'QUALITY.md').write_text('\n'.join(quality) + '\n')
    save(ROOT / 'data/summary.json', summary)
    if not args.timing_only:
        overview(corpus, rows, memory, summary, public_build)
    print(json.dumps(summary, indent=2), flush=True)


if __name__ == '__main__':
    main()
