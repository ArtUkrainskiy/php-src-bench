"""Build the final English benchmark reports from the published raw series.

No measurements or private results paths are needed. --check verifies every generated file.
"""
import argparse
from collections import defaultdict
import csv
import hashlib
import io
import json
import os
from pathlib import Path
import shutil
import statistics as st
import subprocess
p = argparse.ArgumentParser(description=__doc__)
p.add_argument('--php', default=os.environ.get('BENCH_PHP') or shutil.which('php'))
p.add_argument('--check', action='store_true')
a = p.parse_args()
assert a.php, 'Set BENCH_PHP or pass --php to select the report renderer'
report = Path(__file__).resolve().parent.parent
repo = report.parents[1]
seconds = report / 'data/amd'
intel = report / 'data/intel'
base = 'ef99f4248f1450c39fb86fd7fd6f24c49b8d11eb'
head = 'ca89fb5fb96399ed730cacb12d948025f83c4e6e'
names = {'gcc15': 'GCC 15.2', 'clang21': 'Clang 21.1', 'gcc13': 'GCC 13.3', 'gcc14': 'GCC 14.2', 'clang18': 'Clang 18.1', 'clang20': 'Clang 20.1'}
primary = json.loads((report / 'data/primary-cases.json').read_text())
assert len(primary) == 76
outputs = {}
provenance = {}
raw = {}

def read(path):
    d = json.loads(path.read_text())
    provenance[str(path.relative_to(repo))] = hashlib.sha256(path.read_bytes()).hexdigest()
    return d
case_quality = read(report / 'data/quality.json')
read(report / 'data/primary-cases.json')
read(report / 'data/corpus-manifest.json')
for archive in [report / 'data/amd/native-parts.tar.gz', report / 'data/run-logs.tar.gz']:
    provenance[str(archive.relative_to(repo))] = hashlib.sha256(archive.read_bytes()).hexdigest()
paths = [seconds / (cc + '-full233-1sec.json') for cc in list(names)[:2]]
paths += list(seconds.glob('*-aa-*.json'))
paths += list((seconds / 'final-confirmation').glob('*-ab-repeat.json'))
paths += list((seconds / 'final-confirmation').glob('*-aa-*.json'))
for cc in list(names)[2:]:
    paths += [intel / (cc + '-' + kind + '.json') for kind in ['full233', 'focus', 'quality-recheck', 'aa-before', 'aa-after', 'early']]
for path in sorted(set(paths)):
    d = read(path)
    x, y = (d['sides'][s] for s in ['A', 'B'])
    aa_pair = '-aa-' in path.name
    aa_head = '-aa-after' in path.name or '-aa-control' in path.name
    assert x['build']['commit'] == (head if aa_head else base), path
    assert y['build']['commit'] == ((head if aa_head else base) if aa_pair else head), path
    if aa_pair:
        assert x['php'] == y['php'], path
    for side in [x, y]:
        assert side['build']['commit'] in [base, head]
        assert not side['info']['debug'] and (not side['build']['snapshot'])
        assert not side['info']['zts']
        assert side['build']['profile'] == 'docker'
    for key in ['cc', 'configure', 'cflags_user', 'ldflags', 'profile']:
        assert x['build'][key] == y['build'][key], (path, key)
    for case in d['cases'].values():
        aa, bb = (case['sides'][s] for s in ['A', 'B'])
        assert aa['input_hash'] == bb['input_hash'] and aa['output_hash'] == bb['output_hash']
        assert len(aa['input_hash']) == len(aa['output_hash']) == 1
    raw[path] = d
code = "require $argv[1].'/lib/stats.php';require $argv[1].'/lib/render.php';$out=[];foreach(array_slice($argv,2) as $path){$d=json_decode(file_get_contents($path),true);$out[]=result_rows($d,['A','B'],true,$d['config']['perf']);}echo json_encode($out);"
rendered = json.loads(subprocess.check_output([a.php, '-n', '-r', code, str(repo)] + [str(path) for path in raw], text=True))
rows = {path: {r['id']: r for r in rr} for path, rr in zip(raw, rendered)}
full = {}
chosen = {}
sources = {}
for cc in names:
    path = seconds / (cc + '-full233-1sec.json') if cc in ['gcc15', 'clang21'] else intel / (cc + '-full233.json')
    full[cc] = rows[path]
    assert len(full[cc]) == 233 and set(primary) <= set(full[cc])
    chosen[cc] = dict(full[cc])
    sources[cc] = {key: path for key in full[cc]}
    if cc in ['gcc15', 'clang21']:
        assert raw[path]['seconds_series']['complete']
    else:
        for kind in ['focus', 'quality-recheck']:
            path = intel / (cc + '-' + kind + '.json')
            for key, row in rows[path].items():
                chosen[cc][key] = row
                sources[cc][key] = path
expected_hashes = {}
for path, d in raw.items():
    for key, case in d['cases'].items():
        hashes = (case['sides']['A']['input_hash'], case['sides']['A']['output_hash'])
        assert key not in expected_hashes or hashes == expected_hashes[key], (path, key)
        expected_hashes[key] = hashes
cycles = {}
cycle_paths = {'amd': seconds / 'cycles-reference.json', 'intel': intel / 'control-cycles.json'}
for machine, path in cycle_paths.items():
    d = read(path)
    assert d['complete'] and (not d['warnings']) and (not d['marks'])
    for group in d['groups']:
        aa, bb = (d['builds'][group[s]]['build'] for s in ['a', 'b'])
        assert aa['commit'] == base and bb['commit'] == (head if group['name'] in names else base)
        for field in ['cc', 'configure', 'cflags_user', 'ldflags', 'profile']:
            assert aa[field] == bb[field], (machine, group, field)
        assert not aa['debug'] and (not bb['debug']) and (aa['profile'] == 'docker')
    values = defaultdict(lambda: defaultdict(list))
    for group, side, key, bc, bi, ec, ei in d['rows']:
        values[group, key][side].append((bc - ec) / d['cases'][key]['n'])
    for (cc, key), v in values.items():
        if cc in names:
            cycles[cc, key] = (st.median(v['a']), st.median(v['b']), 100 * (st.median((b / aa for aa, b in zip(v['a'], v['b']))) - 1))
    fingerprints = read((seconds if machine == 'amd' else intel) / 'build-fingerprints.json')
    for name, record in fingerprints.items():
        assert record.get('binary_sha1', record.get('sha1')) == d['builds'][name]['sha1'], name
policy = read(seconds / 'final-confirmation/policy.json')
status = read(seconds / 'final-confirmation/status.json')
selection = read(seconds / 'final-confirmation/selection.json')
assert status['state'] == 'complete' and status['completed_runs'] == status['planned_runs'] == 47
assert len(selection) == 23 and (not policy['new_variants_or_inputs'])

def pct(v):
    return f'{v:+.2f}%'.replace('-', '−')

def delta(r):
    return 100 * (r['stats']['B']['median'] / r['stats']['A']['median'] - 1)

def label(key):
    return key.split(' @ ')[0].replace('/TODO/', '/comment-marker/').replace('|', '\\|')

def state(r, path, key):
    noisy = r.get('disturbed') or max((s['spread_pct'] for s in r['stats'].values())) > 5
    noisy = noisy or case_quality[str(path.relative_to(report))][key]['idle_wait_timeout']
    key = 'noise' if noisy else r['verdict']
    return {'noise': 'Noise', '+': 'Faster', '-': 'Slower', '~': 'Unclear', '?': 'Unclear'}[key]

def table(cc, keys, absolute=False, original=False):
    rr = full[cc] if original else chosen[cc]
    titles = ['Case', 'Stock, µs', 'Change, µs', 'Δ time', 'Δ cycles¹', 'Δ instr.', 'Result']
    if absolute:
        titles = ['Case', 'Stock, µs', 'Change, µs', 'Δ time', 'Stock spread', 'Change spread', 'Result', 'Source']
    text = '| ' + ' | '.join(titles) + ' |\n|' + '|'.join('---' if i in [0, len(titles)-1] else '--:' for i in range(len(titles))) + '|\n'
    counters = '| Case | Stock cycles¹ | Change cycles¹ | Δ cycles¹ | Stock instr. | Change instr. | Δ instr. |\n|---|--:|--:|--:|--:|--:|--:|\n'
    for key in keys:
        r = rr[key]
        path = sources[cc][key]
        if original:
            path = seconds / (cc + '-full233-1sec.json') if cc in ['gcc15', 'clang21'] else intel / (cc + '-full233.json')
        x, y = (r['stats'][s] for s in ['A', 'B'])
        cyc = cycles.get((cc, key))
        values = [label(key), f"{x['median'] / 1000:.4f}", f"{y['median'] / 1000:.4f}", pct(delta(r))]
        if absolute:
            values += [f"{x['spread_pct']:.2f}%", f"{y['spread_pct']:.2f}%"]
        else:
            values += [pct(cyc[2]) if cyc else '—', pct(100 * (y['instructions'] / x['instructions'] - 1))]
        values += [state(r, path, key)]
        if absolute:
            target = os.path.relpath(path, report / 'tables')
            values += [f'[{path.stem}]({target})']
            counters += '| ' + ' | '.join([label(key), f'{cyc[0]:.2f}' if cyc else '—', f'{cyc[1]:.2f}' if cyc else '—', pct(cyc[2]) if cyc else '—', f"{x['instructions']:.2f}", f"{y['instructions']:.2f}", pct(100 * (y['instructions']/x['instructions'] - 1))]) + ' |\n'
        text += '| ' + ' | '.join(values) + ' |\n'
    return text + '\n' + ('### Separate counters\n\n' + counters + '\n' if absolute else '')

def cycle_block(machine, summary):
    path = cycle_paths[machine]
    target = os.path.relpath(path, report if summary else report / 'tables')
    args = [str(repo / 'bench'), 'table', str(path), '--full', '--compact-header', '--base-name', 'Stock']
    marker = target + ' --full --compact-header --base-name Stock'
    if summary:
        args += ['--labels', str(report / 'data/cycle-labels.txt')]
        marker += ' --labels data/cycle-labels.txt'
    value = subprocess.check_output(args, env={**os.environ, 'BENCH_PHP': a.php}, text=True)
    return '<!-- bench-table ' + marker + ' -->\n' + value + '<!-- /bench-table -->\n\n'
sample_names = ['banlist12/' + lang + '/post/clean' for lang in ['en', 'ru', 'es', 'ar', 'hi', 'zh', 'ja', 'ko', 'emoji']]
sample_names += ['banlist12/en/comment/clean', 'banlist12/en/post/early', 'banlist12/hi/post/early', 'banlist12/en/thread/clean', 'banlist12/ru/thread/clean', 'banlist12/zh/thread/clean', 'explode/pipe2/4k', 'explode/colon2/4k', 'explode/comma/4k', 'explode/crlf/4k', 'parse-records/4k', 'parse-query/4k', 'parse-http/small', 'parse-http/body64k', 'scan-template/4k', 'render-template/4k', 'log-contains/event/thread/clean', 'log-filter/thread/clean']
sample = [next((k for k in primary if k.split(' @ ')[0] == name)) for name in sample_names]
cycle_keys = sample[:9] + [next((k for k in primary if k.startswith(name + ' @ '))) for name in ['explode/pipe2/4k', 'explode/colon2/4k', 'parse-records/4k', 'parse-query/4k', 'parse-http/small', 'parse-http/body64k', 'render-template/4k', 'log-contains/event/thread/clean']]
labels_text = ''.join((key + '=' + label(key) + '\n' for key in cycle_keys))
labels_path = report / 'data/cycle-labels.txt'
if a.check:
    assert labels_path.read_text() == labels_text, 'data/cycle-labels.txt is stale'
else:
    labels_path.write_text(labels_text)
outputs[labels_path] = labels_text
text = '# Forward substring search: product benchmarks\n\nThis report measures a change to `zend_memnstr_ex()`, the forward matcher used by PHP string functions. The change reduces Sunday setup costs for medium needles and limits expensive verification on long scans. The corpus covers everyday moderation, separators, parsers, templates and logs.\n\n'
patch = 'change.patch'
text += f'Compared: change [`{head[:11]}`](https://github.com/ArtUkrainskiy/php-src/commit/{head}) ([branch](https://github.com/ArtUkrainskiy/php-src/tree/strpos-adaptive-pr), [patch]({patch})) versus stock PHP [`{base[:11]}`](https://github.com/php/php-src/commit/{base}). Measured on 30 October 2026 with the same two commits and corpus on all six compiler/CPU combinations.\n\n'
text += '**Elapsed time of the complete PHP operation is the primary criterion.** Negative deltas mean lower cost; every delta is relative to stock. Cycles and instructions are diagnostic evidence, not substitutes for elapsed time. There is no application-wide average or assumed traffic distribution.\n\n'
text += '## Summary\n\n'
text += '| CPU / compiler | Clean posts, Δ time | 4 KiB template, Δ time |\n|---|---:|---:|\n'
for cc in names:
    posts = [r for k, r in chosen[cc].items() if k.startswith('banlist12/') and '/post/clean @ ' in k]
    template = next((r for k, r in chosen[cc].items() if k.startswith('render-template/4k @ ')))
    text += '| ' + ('AMD' if cc in ['gcc15', 'clang21'] else 'Intel') + ' / ' + names[cc] + ' | ' + pct(min(map(delta, posts))) + ' … ' + pct(max(map(delta, posts))) + ' | ' + pct(delta(template)) + ' |\n'
text += '\n' + 'The post ranges cover medians across all nine languages, not uncertainty bounds; row quality and controls remain below and in the full tables. Moderation checks twelve literals in already normalized text. Short comments and one-/two-byte separators mostly retain their existing work. They have no general speedup guarantee. The template case performs four replacements with allocations, not a complete page request.\n\n'
text += 'There are real losses: the independent AMD repeat retained GCC slowdowns around 1.66–2.48% in three parser cases. The original Clang `explode("||")` 4 KiB result was +3.24%, versus +0.20% in its single independent repeat; neither result is deleted. Quiet Intel retains roughly +4.4% and +5.4% on long English and Chinese text with Clang 20. A universal 3% regression bound and greater cross-compiler stability are not supported.\n\n'
text += '## Everyday elapsed times\n\n'
text += 'The main tables use the complete final AMD one-second series, without replacing rows by favourable repeats. They include all nine clean-post languages plus short/early controls, long texts, separators, parsers, templates and logs.\n\n'
for cc in ['gcc15', 'clang21']:
    text += '### AMD / ' + names[cc] + '\n\n' + table(cc, sample)
text += '¹ Cycles were measured separately: five paired passes × 50 ms on AMD, three × 50 ms in the fresh quiet Intel series. Binary hashes match the elapsed-time builds. Instruction deltas here are from the elapsed-time series. These columns do not yield exact simultaneous IPC. A dash means no matching completed cycle row.\n\n'
text += 'Faster/Slower requires separated round medians and at least a 1% difference. Unclear means overlap or a small difference, not proof of equality. Noise includes sample spread over 5%, round drift over 10%, or an idle-wait timeout. Spread is `1.4826 × MAD / median`, not a confidence interval.\n\n'
text += '## Regressions and independent controls\n\n'
text += 'A finite confirmation stage selected every noisy row and every usable slower row from the full AMD series: 23 cases, 47 runs including same-binary A/A and profiles. Selection did not depend on obtaining a favourable result. Each selected case has one new A/B run; there are no recursive retries. Three remain noisy. The original slower rows and all their controls are shown here.\n\n'
text += '| Case | Compiler | Original Δ time | Repeat Δ time | Stock A/A | Change A/A | Result |\n|---|---|---:|---:|---:|---:|---|\n'
for item in selection:
    if not item['original_slower']:
        continue
    cc, key = (item['compiler'], item['case'])
    prefix = f"{cc}-case{item['index']:03d}"
    cells = [label(key), names[cc], pct(item['original_time_change_pct'])]
    for suffix in ['ab-repeat', 'aa-base', 'aa-control']:
        path = seconds / 'final-confirmation' / (prefix + '-' + suffix + '.json')
        r = rows[path][key]
        quality = state(r, path, key)
        cells.append(pct(delta(r)) + (' ⚠' if quality == 'Noise' else ''))
        if suffix == 'ab-repeat':
            verdict = quality
    text += '| ' + ' | '.join(cells + [verdict]) + ' |\n'
text += '\n' + '⚠ marks a noisy A/A control. Small positive parser deltas present in both runs are retained even if the repeat is Unclear. A/A is specific to the measured case/build; it is not a universal error bar for every compiler or CPU.\n\n'
text += '## Compiler cycle matrix and A/A\n\n'
text += 'Generated by `bench compare` / `bench table --full --compact-header`, with every available compiler and same-row A/A below each table. Absolute stock cycles use the compiler named above the table. Each percentage compares the change with that column\'s own stock build. The cycle A/A uses GCC 15 on AMD and GCC 13 on Intel. [All 76 rows and pass ranges](tables/cycles.md) are retained.\n\n'
for machine in cycle_paths:
    text += '### ' + machine.upper() + '\n\n' + cycle_block(machine, True)
text += '## Machine and method\n\n'
text += 'AMD Ryzen 9 5950X, GCC 15.2 / Clang 21.1: pinned physical core, `performance` governor, turbo enabled. Intel i7-13700H, GCC 13.3 / GCC 14.2 / Clang 18.1 / Clang 20.1: pinned P-core, AC power, `powersave` governor, turbo enabled. No frequency-setting changes are made to reproduce the report. The compiler matrix compares matched pairs within a machine; it is not an absolute AMD-versus-Intel ranking.\n\n'
text += 'All timing pairs are non-debug, non-ZTS CLI release builds using the `docker` profile, `--disable-all --disable-cgi --disable-phpdbg --enable-cli --enable-werror`, CFLAGS `-fstack-protector-strong -fpic -fpie -O2 -g -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64`, LDFLAGS `-Wl,-O1 -pie`. Compiler, configure options and flags match within each pair. Full generated flags, binary fingerprints, environment and warnings remain in the raw series. Extra-alignment builds are historical diagnostics only.\n\n'
text += 'AMD: 233 cases per compiler, four paired rounds × one approximately 1000 ms sample, warmup at least 1000 ms, perf instructions. Each case runs in its own PHP processes; compilers alternate after each case. Calibration chooses the iteration count; timing the batch avoids a timer call per operation. The median empty-loop cost is subtracted. Case preparation and result checking are outside the timed loop.\n\n'
text += 'Quiet Intel: the initial 233-case sweep uses four rounds × seven samples × 10 ms. A preselected 22-case focus and quality rechecks use 50 ms. The selection policy is quality recheck, then preselected focus, then original full run; the original 233 rows are always retained. The source and sample window of each chosen row are recorded. Earlier busy-laptop elapsed times are historical and unusable for speed claims.\n\n'
text += 'Cycle cost is `(counted process − empty-loop process) / iterations`, measured sequentially with alternating A/B order. The delta is the median of paired B/A pass ratios; absolute costs are separate side medians, so their ratio can differ slightly from the published paired delta. Elapsed deltas are directly `(median ca89 / median stock − 1) × 100%`. Instructions in elapsed runs are separate perf counts.\n\n'
timing_link = 'tables/confirmations.md'
text += f'The [A/A window-duration pilot and all final confirmations]({timing_link}) preserve both short and one-second controls. Longer windows did not universally reduce A/A drift. The final method also changes grouping from a whole filtered suite to one case per PHP process, so differences between old and new series cannot be assigned to warmup or duration alone.\n\n'
text += '## Code\n\n'
text += 'The header memchr/verify path for remaining haystacks below 1024 bytes or needles below 9 bytes is unchanged. Needles of 9–31 bytes use a 256-byte uint8 Sunday table instead of the original 1 KiB unsigned-int table. Needles of at least 32 bytes retain wide-table Sunday below 8192 input bytes. On larger buffers, sixteen deep failed verifications trigger a work-versus-progress check; with at least 4096 bytes remaining, expensive scans may switch to an SSE2 pair filter, sampled four-byte filter and portable Two-Way. Full-verification budgets cover the remaining scan. The patch changes one C file and adds five PHPT files. No public API is added.\n\n'
diag = 'tables/profiles.md'

text += f'Unchanged instruction counts do not erase elapsed regressions. Profiles of the two confirmed GCC HTTP cases show L1 instruction-cache misses increasing from about 0.02 to 2.41 and 1.90 per call; the affected PHP entry-point addresses and sizes are unchanged. This is consistent with placement/cache effects, not proof of a unique cause. Long Russian/Hindi Clang scans can improve while executing more instructions. [Earlier profiles and disassembly]({diag}) and [new profiles](data/amd/final-confirmation/gcc15-case066-why.log) are retained. A general explanation for every layout-sensitive row has not been established.\n\n'
text += '''## Algorithm references

- **Sunday / Quick Search.** Daniel M. Sunday, [A very fast substring search algorithm](https://doi.org/10.1145/79173.79184), 1990. PHP already uses this shift rule. The short-needle path keeps the same search and stores its shifts in bytes.
- **Two-Way.** Maxime Crochemore and Dominique Perrin, [Two-way string-matching](https://doi.org/10.1145/116825.116845), 1991. `zend_memnstr_twoway()` uses critical factorization and remembers periodic matches across shifts.
- **SIMD pair filtering.** The [packed-pair implementation in Rust memchr 2.7.6](https://github.com/BurntSushi/memchr/blob/2.7.6/src/arch/all/packedpair/mod.rs) is a related implementation reference for choosing two needle positions using background byte frequencies. Here SSE2 checks both positions at sixteen candidate starts, then verifies each hit completely.
- **Four-byte filtering, related work.** Simone Faro and M. Oğuzhan Külekci, [Fast Packed String Matching for Short Patterns](https://arxiv.org/abs/1209.6449), 2012 preprint, section 3.2 (EPSM_a). The related primitive intersects shifted byte-equality masks. `zend_memnstr_gram4()` applies it to a selected internal four-byte anchor, with overlapping windows, selectivity sampling and a verification budget.

The dispatch thresholds, byte-frequency weights, sampling rules and verification budgets are implementation choices evaluated by these PHP measurements. The references describe the search mechanisms; the measured gains, losses and applicability come from this corpus. The work-count checks are fixture audits rather than a formal proof of the complete hybrid.

'''
text += '## Corpus and scope\n\n'
corpus_link = 'data/corpus-manifest.json'
manifest_link = 'data/corpus-manifest.json'
text += f'The [owned product corpus]({corpus_link}) has 141 frozen inputs and 233 operations, including a preselected 76-case primary set. The [manifest]({manifest_link}) records exact byte sizes, SHA-256 and recipes. Nine language variants cover comments, posts and approximately 64 KiB threads with absent/early/late matches. Normalization, word boundaries and case folding are outside timing. Fields, queries, HTTP, separators, templates and payment logs include PHP loops and allocations. A 64 KiB HTTP body does not imply a full-body scan: parsing stops at the header terminator.\n\n'
text += 'The messages are constructed deterministic fixtures, not captured production traffic. No popularity weights are inferred. Public document snapshots are supplementary and retain source hashes; fetching current pages cannot reproduce the exact old snapshots. Their content is not committed. Source-text fixtures are pinned separately from the runtime base commit. One MiB exports, 64 KiB queries, the 112-case boundary grid and six repeated-prefix cases are size/stress guards, not typical request frequencies.\n\n'
text += '## Tests\n\n'
validation = read(report / 'data/validation.json')
vlink = 'data/validation.json'
verify = 'verify/README.md'
text += f'- All 233 product and 112 boundary outputs agree across six compiler builds; Python ground truth independently generates exact expected search/split/replacement values. Raw runner hashes use MD5 of PHP serialized values; manifest SHA-256 covers input bytes. These are different checks.\n- Core/string PHPT: release 6237 passed, 243 skipped, one expected failure; debug/ZTS 6236 passed, 244 skipped, one expected failure. No unexpected failures or warnings. String-only tests on each of the six compiler builds: 703 passed, 62 skipped.\n- Exact extracted matching functions under ASan/UBSan: 100000 randomized inputs and 135460 guarded configurations for SSE2 and forced scalar, both passed. Four functional mutations are rejected. Work-count fixtures reject the tested disabled budgets/window reset; they are not a formal all-input complexity proof.\n- [Validation records]({vlink}), [sources and commands]({verify}). Benchmark framework self-tests were rerun after measurement and [passed](verify/framework-tests.txt). Native ARM and 32-bit runs remain untested; scalar on x86 does not replace them.\n\n'
text += '## Full evidence\n\n'
text += '- [All 76 primary cases on six compilers: absolute elapsed time, cycles, instructions and deltas](tables/primary.md).\n- [All 233 original rows on six compilers](tables/all-product.md), [every observed elapsed increase over 1%](tables/increases.md), [TSV](data/metrics.tsv).\n- [All cycle passes and A/A](tables/cycles.md), [elapsed A/A controls](tables/controls.md).\n- [Boundary grid](tables/boundaries.md) and [repeated-prefix stress cases](tables/stress.md), separate from everyday cases.\n- [All finite AMD confirmations](tables/confirmations.md), [quiet Intel early-match confirmations](tables/early.md), [data and file roles](LAYOUT.md).\n\n'
text += '## Not measured\n\nCold requests, complete FPM requests, framework throughput and production traffic weights; native ARM/32-bit performance; Go/Rust or cold-versus-cached PCRE. No universal cross-compiler stability or maximum-regression claim is made. All timing rows, including noisy and unresolved layout-sensitive rows, are published; such rows are not proof of an algorithmic gain.\n\n'
repro = 'REPRODUCE.md'
text += f'## Reproduce\n\n[Commands for rebuilding, rerunning and regenerating the report]({repro}). The report regenerates from published raw data without private `results/` paths. `scripts/build_report.py --check` checks generated text/metrics and data invariants; `bench report check reports/substr-adaptive-search` checks native cycle blocks, links, placeholders and portable paths.\n'
outputs[report / 'README.md'] = text
for filename, title, mode in [('tables/primary.md', 'Primary product cases', 'primary'), ('tables/all-product.md', 'All original product rows', 'full'), ('tables/increases.md', 'All observed elapsed increases over 1%', 'increases')]:
    doc = '# ' + title + '\n\n' + 'Elapsed time is primary. Cycles¹ come from a separate series; no simultaneous IPC is implied. Instructions are from the indicated elapsed run. Full tables retain original rows; primary tables use the documented Intel focus/quality policy. Increases include noisy and unclear rows, not only confirmed regressions.\n\n'
    for cc in names:
        keys = primary if mode == 'primary' else list(full[cc])
        if mode == 'increases':
            keys = [key for key in keys if delta(full[cc][key]) > 1 or delta(chosen[cc][key]) > 1]
        doc += '## ' + ('AMD' if cc in ['gcc15', 'clang21'] else 'Intel') + ' / ' + names[cc] + '\n\n'
        doc += table(cc, keys, True, original=mode in ['full', 'increases'])
        if mode == 'increases' and cc not in ['gcc15', 'clang21']:
            doc += '### Documented focus/quality selection\n\n' + table(cc, keys, True)
    outputs[report / filename] = doc
controls = '# ' + 'Elapsed-time A/A controls' + '\n\n'
controls += 'Each A/A pair runs the same binary on both sides. These selected controls do not cover all 233 cases. AMD includes six pilot cases at both durations; Intel has ten stock controls before and ten candidate controls after its series. Additional A/A for all originally usable AMD slower cases is in the main report and raw confirmation data.\n\n'
for path in raw:
    if '-aa-' not in path.name or path.parent.name == 'final-confirmation':
        continue
    controls += '## ' + path.stem + '\n\n'
    controls += '| Case | A₁, µs | A₂, µs | Δ A/A | A₁ / A₂ spread | Result |\n|---|---:|---:|---:|---:|---|\n'
    for key, r in rows[path].items():
        x, y = (r['stats'][s] for s in ['A', 'B'])
        controls += '| ' + ' | '.join([label(key), f"{x['median'] / 1000:.4f}", f"{y['median'] / 1000:.4f}", pct(delta(r)), f"{x['spread_pct']:.2f}% / {y['spread_pct']:.2f}%", state(r, path, key)]) + ' |\n'
    controls += '\n[' + path.name + '](' + os.path.relpath(path, report / 'tables') + ').\n\n'
outputs[report / 'tables/controls.md'] = controls
outputs[report / 'tables/cycles.md'] = '# Complete primary cycle matrices\n\nAll 76 preselected product cases, every available compiler, original pass ranges and same-row A/A controls. AMD uses five passes; quiet Intel uses three. A/A is the first compiler of each machine, not each compiler. These cycles were measured separately from elapsed time.\n\n## AMD\n\n' + cycle_block('amd', False) + '## Quiet Intel\n\n' + cycle_block('intel', False)

confirmations = '# Complete finite AMD confirmation stage\n\n'
confirmations += 'Every selected case is retained, including favourable, unfavourable and noisy originals. One A/B repeat per selected case. All originally usable slower cases also have stock and candidate A/A controls. The fixed [policy](../data/amd/final-confirmation/policy.json) and [selection](../data/amd/final-confirmation/selection.json) are unchanged.\n\n'
confirmations += '| Case | Compiler | Original Δ time | Repeat Δ time | Original result | Repeat result | Source |\n|---|---|--:|--:|---|---|---|\n'
for item in selection:
    cc, key = item['compiler'], item['case']
    path = seconds / 'final-confirmation' / f"{cc}-case{item['index']:03d}-ab-repeat.json"
    original_path = seconds / (cc + '-full233-1sec.json')
    confirmations += '| ' + ' | '.join([label(key), names[cc], pct(delta(full[cc][key])), pct(delta(rows[path][key])), state(full[cc][key], original_path, key), state(rows[path][key], path, key), f'[{path.stem}]({os.path.relpath(path, report / "tables")})']) + ' |\n'
outputs[report / 'tables/confirmations.md'] = confirmations + '\n'

early = '# Quiet Intel early-match confirmations\n\n'
early += 'Same ca89 candidate and reference. These supplementary boundary calls are not a production frequency distribution. All original elapsed results and noisy rows are retained.\n\n'
for cc in list(names)[2:]:
    path = intel / (cc + '-early.json')
    early += '## ' + names[cc] + '\n\n| Case | Stock, µs | Change, µs | Δ time | Δ instr. | Result |\n|---|--:|--:|--:|--:|---|\n'
    for key, r in rows[path].items():
        x, y = (r['stats'][s] for s in ['A', 'B'])
        early += '| ' + ' | '.join([label(key), f"{x['median']/1000:.4f}", f"{y['median']/1000:.4f}", pct(delta(r)), pct(100*(y['instructions']/x['instructions']-1)), state(r, path, key)]) + ' |\n'
    early += '\n[Native series](' + os.path.relpath(path, report / 'tables') + ').\n\n'
outputs[report / 'tables/early.md'] = early

for title, output, files in [
    ('Synthetic routing boundary grid', 'boundaries.md', ['amd-boundaries.json', 'intel-boundaries.json']),
    ('Repeated-prefix stress cases', 'stress.md', ['amd-adversarial.json', 'amd-long-prefix.json', 'intel-adversarial.json', 'intel-long-prefix.json'])]:
    doc = '# ' + title + '\n\nSupplementary guards, not a frequency distribution of everyday requests. These compare the same final candidate and base. Every original pass, A/A control and warning remains visible.\n\n'
    for name in files:
        path = report / 'data/stress' / name
        d = read(path)
        assert d['complete']
        for group in d['groups']:
            aa, bb = (d['builds'][group[s]]['build'] for s in ['a', 'b'])
            assert aa['commit'] == base and bb['commit'] == (head if group['name'] in names else base)
            assert aa['profile'] == bb['profile'] == 'docker'
        args = [str(repo / 'bench'), 'table', str(path), '--header', '--full', '--compact-header', '--base-name', 'Stock']
        value = subprocess.check_output(args, env={**os.environ, 'BENCH_PHP': a.php}, text=True)
        marker = os.path.relpath(path, report / 'tables') + ' --header --full --compact-header --base-name Stock'
        doc += '## ' + name[:-5] + '\n\n<!-- bench-table ' + marker + ' -->\n' + value + '<!-- /bench-table -->\n\n'
    outputs[report / 'tables' / output] = doc
stream = io.StringIO()
w = csv.writer(stream, delimiter='\t', lineterminator='\n')
w.writerow(['compiler', 'case', 'primary', 'stock_ns', 'ca89_ns', 'elapsed_change_pct', 'stock_cycles_separate', 'ca89_cycles_separate', 'cycles_change_pct', 'stock_instructions', 'ca89_instructions', 'instructions_change_pct', 'stock_spread_pct', 'ca89_spread_pct', 'elapsed_result', 'source', 'target_ms'])
for cc, rr in chosen.items():
    for key, r in rr.items():
        x, y = (r['stats'][s] for s in ['A', 'B'])
        cyc = cycles.get((cc, key), ('', '', ''))
        path = sources[cc][key]
        w.writerow([cc, key, key in primary, x['median'], y['median'], delta(r), *cyc, x['instructions'], y['instructions'], 100 * (y['instructions'] / x['instructions'] - 1), x['spread_pct'], y['spread_pct'], state(r, path, key), str(path.relative_to(repo)), raw[path]['config']['target_ms']])
outputs[report / 'data/metrics.tsv'] = stream.getvalue()
outputs[report / 'data/report-manifest.json'] = json.dumps({'base': base, 'candidate': head, 'primary_cases': len(primary), 'product_cases_per_compiler': 233, 'compilers': list(names), 'raw_file_sha256': provenance, 'confirmation_runs': 47, 'source_changes_during_final_series': False}, indent=2) + '\n'
for path, value in outputs.items():
    if path.suffix == '.md':
        value = value.rstrip() + '\n'
    if a.check:
        assert path.exists() and path.read_text() == value, 'Generated file differs: ' + str(path.relative_to(repo))
    else:
        path.write_text(value)
print('Verified' if a.check else 'Generated', len(outputs), 'files from', len(raw), 'raw elapsed series; six compilers, 233 cases each.')
