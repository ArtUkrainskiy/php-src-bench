"""Supplementary measurements after four complete main series.

Configuration is supplied through RUN_ROOT, STRMATCH_SOURCE, PHP_BUILD_GCC15,
PHP_BUILD_CLANG21, BENCH_CPU and BENCH_SIBLING. Run prepare.py first.
The timed PHP files are byte-identical to the captured run. This controller
adapts machine paths and removes the original asynchronous queue wait.
Outputs are append-only raw calls plus complete JSON records in RUN_ROOT.
"""

import datetime
import fcntl
import hashlib
import json
import math
import os
import statistics as st
import subprocess
import sys
from pathlib import Path

REPORT = Path(__file__).resolve().parent.parent
R = Path(os.environ['RUN_ROOT']).resolve()
SOURCE = Path(os.environ['STRMATCH_SOURCE']).resolve()
CPU = int(os.environ['BENCH_CPU'])
SIBLING = int(os.environ['BENCH_SIBLING'])
REV = '287aaab7fb729d3a8e91c6fd35224c4359c343e3'
BUILDS = {cc: Path(os.environ['PHP_BUILD_' + cc.upper()]).resolve() for cc in ['gcc15', 'clang21']}
PASSES = 15
WARM = 250_000_000
SAMPLE = round(1e9 / 15)
sequence = 0
PINNED_CODE = None


def digest(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def read(p):
    return json.loads(Path(p).read_text())


def save(p, d):
    p = Path(p)
    p.parent.mkdir(parents=True, exist_ok=True)
    t = p.with_suffix(p.suffix + '.tmp')
    t.write_text(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
    t.replace(p)


def state(phase, **data):
    save(
        R / 'post-status.json',
        {'phase': phase, 'updated': datetime.datetime.now(datetime.UTC).isoformat(), 'pid': os.getpid(), **data},
    )


def ticks(cpu=SIBLING):
    a = next(x for x in Path('/proc/stat').read_text().splitlines() if x.startswith(f'cpu{cpu} ')).split()[1:9]
    a = list(map(int, a))
    return sum(a), a[3] + a[4]


def interval_activity(before, after):
    total = after[0] - before[0]
    idle = after[1] - before[1]
    return None if total <= 0 else 100 * (1 - idle / total)


def activity(before):
    return interval_activity(before, ticks())


def command(cc):
    return [
        'taskset',
        '-c',
        str(CPU),
        str(BUILDS[cc] / 'sapi/cli/php'),
        '-n',
        '-d',
        'memory_limit=1G',
        '-d',
        'pcre.jit=1',
        '-d',
        'opcache.enable_cli=0',
        '-d',
        'opcache.jit=0',
        '-d',
        'extension=' + str(R / ('data-product-' + cc) / 'strmatch.so'),
    ]


def call(cc, harness, cfg):
    global sequence
    sequence += 1
    path = R / 'supplement-raw' / f'{sequence:05}-{cc}-{harness}.json'
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('x') as f:
        f.write(json.dumps(cfg, ensure_ascii=False, indent=2) + '\n')
    before = ticks()
    try:
        p = subprocess.run(
            [*command(cc), str(R / (harness + '.php')), str(path)],
            text=True,
            capture_output=True,
            timeout=120,
            check=False,
        )
    except subprocess.TimeoutExpired as error:
        for stream in ['stdout', 'stderr']:
            value = getattr(error, stream) or b''
            if isinstance(value, bytes):
                value = value.decode('utf-8', errors='replace')
            path.with_name(path.stem + '-' + stream + '.txt').write_text(value)
        raise
    busy = activity(before)
    path.with_name(path.stem + '-stdout.txt').write_text(p.stdout)
    path.with_name(path.stem + '-stderr.txt').write_text(p.stderr)
    if p.returncode or p.stderr:
        raise RuntimeError(f'{harness} {cfg.get("case", {}).get("id", "")}: {p.stdout}\n{p.stderr}')
    data = json.loads(p.stdout)
    save(path.with_name(path.stem + '-output.json'), data)
    if busy is not None and busy > 5:
        raise RuntimeError(f'SMT sibling busy {busy:.2f}%, preserve and remeasure this supplemental call')
    return data, {'raw_config': str(path.relative_to(R)), 'sibling_busy_percent': busy}


def metadata(cc):
    assert PINNED_CODE is not None
    for name, expected in PINNED_CODE.items():
        assert digest(Path(__file__) if name == 'measure.py' else R / name) == expected, (
            'Changed frozen script: ' + name
        )
    d = read(R / ('data-product-' + cc) / 'results.json')['metadata']
    s = read(R / ('data-size-' + cc) / 'results.json')['metadata']
    assert d['source_revision'] == s['source_revision'] == REV
    assert d['source_sha256'] == s['source_sha256']
    assert d['php_sha256'] == s['php_sha256'] and d['module_sha256'] == s['module_sha256']
    assert digest(BUILDS[cc] / 'sapi/cli/php') == d['php_sha256']
    assert digest(R / ('data-product-' + cc) / 'strmatch.so') == d['module_sha256']
    for stem, corpus in [('product', 'multi-pattern-product'), ('size', 'multi-pattern-scaling')]:
        main = read(R / ('data-' + stem + '-' + cc) / 'results.json')
        assert main['status'] == 'complete'
        assert main['metadata']['corpus_index_sha256'] == digest(REPORT / '../../corpus' / corpus / 'index.json')
    for name, expected in d['source_sha256'].items():
        assert digest(SOURCE / name) == expected
    return {
        'main_metadata': d,
        'pinned_scripts': PINNED_CODE,
        'definitions_sha256': digest(R / 'definitions.php'),
        'order_harness_sha256': digest(R / 'order-harness.php'),
        'constructor_protocol': {
            'first': 'first constructor in a fresh PHP process after parsing; release/startup excluded; CPU and file caches are not cold',
            'warm': 'construction and release plus common closure/loop cost',
            'model': 'request minus worker is an estimate including wrapper differences, not the first constructor',
        },
        'order_protocol': 'paired reverse order; starting position rotates every pair',
        'batch_harness_sha256': digest(R / 'batch.php'),
        'construction_harness_sha256': digest(R / 'construction.php'),
        'driver_sha256': digest(__file__),
        'passes': PASSES,
        'warmup_ns': WARM,
        'sample_ns': SAMPLE,
    }


def aa_check(data, metric):
    v = data[metric]
    ratios = [b / a for a, b in zip(v['a'], v['b'])]
    median = st.median(ratios)
    if abs(median - 1) > 0.02:
        raise RuntimeError(f'Supplement A/A outside2%: {(median - 1) * 100:.2f}%')
    return {'paired_ratios': ratios, 'median_ratio': median}


def load_cases():
    cases = {}
    for stem, corpus in [('product', 'multi-pattern-product'), ('size', 'multi-pattern-scaling')]:
        root = REPORT / '../../corpus' / corpus
        index = read(root / 'index.json')
        for file, sha in index['suite_sha256'].items():
            assert digest(root / file) == sha
            for case in read(root / file)['cases']:
                key = (stem, case['id'])
                assert key not in cases
                cases[key] = case
    return cases


def memory(cc):
    state('memory', compiler=cc)
    cmd = [
        'python3',
        str(REPORT / 'memory/measure.py'),
        '--php-build',
        str(BUILDS[cc]),
        '--module',
        str(R / ('data-product-' + cc) / 'strmatch.so'),
        '--compiler',
        cc,
        '--reference-data',
        str(R / ('data-product-' + cc) / 'results.json'),
        '--cpu',
        str(CPU),
        '--output',
        str(R / ('memory-' + cc + '.json')),
    ]
    with (R / ('memory-' + cc + '.log')).open('w') as f:
        p = subprocess.run(cmd, stdout=f, stderr=subprocess.STDOUT, timeout=600, check=False)
    if p.returncode:
        raise RuntimeError('Memory driver failed ' + cc)
    d = read(R / ('memory-' + cc + '.json'))
    assert d['status'] == 'complete' and len(d['rows']) == 44
    print('MEMORY COMPLETE', cc, flush=True)


def constructors(cc):
    root = REPORT / 'memory'
    index = read(root / 'index.json')
    rows = []
    controls = []
    meta = metadata(cc)
    for stage in ['before', 'after']:
        cfg = {
            'family': str(root / 'glossary-catalog'),
            'size': 128,
            'class': 'Matcher',
            'mode': 'aa',
            'passes': PASSES,
            'warmup_ns': WARM,
            'sample_ns': SAMPLE,
        }
        d, raw = call(cc, 'construction', cfg)
        controls.append({'stage': stage, 'result': d, **raw, **aa_check(d, 'ns')})
        if stage == 'after':
            break
        for family in index['families']:
            for size in index['sizes']:
                for cls in ['Matcher', 'Replacer']:
                    state('constructors', compiler=cc, family=family, size=size, kind=cls, complete=len(rows), total=44)
                    cfg = {
                        'family': str(root / family),
                        'size': size,
                        'class': cls,
                        'mode': 'check',
                        'passes': PASSES,
                        'warmup_ns': WARM,
                        'sample_ns': SAMPLE,
                    }
                    check, check_raw = call(cc, 'construction', cfg)
                    first = []
                    for repeat in range(5):
                        cfg['mode'] = 'first'
                        d, raw = call(cc, 'construction', cfg)
                        first.append({'result': d, **raw})
                    cfg['mode'] = 'time'
                    d, raw = call(cc, 'construction', cfg)
                    assert d['sink'] == PASSES * sum(d['iterations'].values())
                    rows.append(
                        {
                            'family': family,
                            'size': size,
                            'class': cls,
                            'check': check,
                            'check_raw': check_raw,
                            'first_constructor_fresh_process': first,
                            'warm_build_release': d,
                            'warm_raw': raw,
                        }
                    )
                    save(
                        R / ('constructors-' + cc + '.json'),
                        {'status': 'running', 'metadata': meta, 'rows': rows, 'aa': controls},
                    )
                    print('CONSTRUCTOR', cc, family, size, cls, flush=True)
    save(R / ('constructors-' + cc + '.json'), {'status': 'complete', 'metadata': meta, 'rows': rows, 'aa': controls})


def models(cc, cases):
    rows = []
    for stem in ['product', 'size']:
        data = read(R / ('data-' + stem + '-' + cc) / 'results.json')
        by = {(v['case'], v['lifecycle']): v for v in data['rows']}
        for name in sorted({v['case'] for v in data['rows']}):
            if (name, 'worker') not in by or (name, 'request') not in by:
                continue
            case = cases[stem, name]
            candidate = 'replacer' if case['operation'] == 'replace' else 'matcher'
            w = by[name, 'worker']['time']['ns_per_job']
            q = by[name, 'request']['time']['ns_per_job']
            p = st.median(q[candidate]) - st.median(w[candidate])
            alts = {}
            for method in case['methods']:
                if method == candidate:
                    continue
                gap = st.median(w[method]) - st.median(w[candidate])
                saving = st.median([(1 - b / a) * 100 for a, b in zip(w[method], w[candidate])])
                estimate = math.floor(p / gap) + 1 if p >= 0 and gap > 0 else None
                alts[method] = {
                    'prepared_median_ns': st.median(w[method]),
                    'candidate_saving_percent': saving,
                    'gap_ns': gap,
                    'estimated_jobs': estimate,
                    'status': 'not_faster_prepared'
                    if gap <= 0
                    else 'unstable_preparation'
                    if p < 0
                    else 'small_gap'
                    if saving < 2
                    else 'model',
                }
            rows.append(
                {
                    'corpus': stem,
                    'case': name,
                    'title': case['title'],
                    'kind': case['kind'],
                    'operation': case['operation'],
                    'dictionary_size': len(case['jobs'][0]['dictionary']),
                    'documents_per_job': [len(v['documents']) for v in case['jobs']],
                    'candidate': candidate,
                    'request_median_ns': st.median(q[candidate]),
                    'worker_median_ns': st.median(w[candidate]),
                    'estimated_build_release_ns': p,
                    'alternatives': alts,
                    'model_note': 'request-minus-worker is an estimate, not cold constructor timing; native/PCRE alternatives are already prepared; threshold is not a directly verified minimum',
                }
            )
    save(R / ('amortization-model-' + cc + '.json'), {'status': 'complete', 'metadata': metadata(cc), 'rows': rows})
    return {(v['corpus'], v['case']): v for v in rows}


def expected_sink(case, iterations, batch):
    one = 0
    for job in case['jobs']:
        for doc in job['documents']:
            value = doc['expected']
            one += (
                len(value['text'].encode())
                if case['operation'] == 'replace'
                else len(value)
                if isinstance(value, list)
                else int(value)
            )
    assert iterations * batch % len(case['jobs']) == 0
    return one * (iterations * batch // len(case['jobs']))


def batches(cc, cases, model):
    chosen = [
        'moderation.en.clean',
        'moderation.ru.clean',
        'moderation.zh.clean',
        'moderation.en.start',
        'moderation.en.body',
        'moderation.en.end',
        'moderation.en.post-clean',
        'help.count',
        'help.unique',
        'help.all',
        'help.link-one',
        'punctuation.mixed',
        'chat.emoticons',
        'secrets.clean',
        'secrets.incident-batch',
    ]
    chosen = [('product', name) for name in chosen]
    chosen += [
        ('size', prefix + str(n))
        for prefix in ['scale.moderation.short.absent.', 'scale.search.unique.', 'scale.replace.articles1.']
        for n in [8, 16, 32, 64, 128, 256, 512]
    ]
    assert len(set(chosen)) == 36 and all(name in cases and name in model for name in chosen)
    rows = []
    controls = []
    meta = metadata(cc)

    def take(stem, name, n):
        case = cases[stem, name]
        cfg = {
            'case': case,
            'batch_size': n,
            'methods': case['methods'],
            'mode': 'check',
            'passes': PASSES,
            'warmup_ns': WARM,
            'sample_ns': SAMPLE,
        }
        state('amortization', compiler=cc, case=name, batch_size=n, rows=len(rows))
        check, check_raw = call(cc, 'batch', cfg)
        cfg['mode'] = 'time'
        d, raw = call(cc, 'batch', cfg)
        assert d['sink'] == PASSES * sum(expected_sink(case, count, n) for count in d['iterations'].values())
        candidate = model[stem, name]['candidate']
        changes = {
            method: [(b / a - 1) * 100 for a, b in zip(samples, d['ns_per_batch'][candidate])]
            for method, samples in d['ns_per_batch'].items()
            if method != candidate
        }
        record = {
            'corpus': stem,
            'case': name,
            'batch_size': n,
            'candidate': candidate,
            'time': d,
            'check': check,
            'check_raw': check_raw,
            'raw': raw,
            'paired_delta_to_alternatives': changes,
            'wins_every_alternative_with_2percent_margin': all(st.median(v) <= -2 for v in changes.values()),
        }
        rows.append(record)
        save(
            R / ('amortization-batches-' + cc + '.json'),
            {'status': 'running', 'metadata': meta, 'rows': rows, 'aa': controls},
        )
        print('BATCH', cc, name, n, flush=True)
        return record

    for stage in ['before', 'after']:
        case = cases['product', 'moderation.en.clean']
        cfg = {
            'case': case,
            'batch_size': 8,
            'methods': {'a': 'matcher', 'b': 'matcher'},
            'mode': 'time',
            'passes': PASSES,
            'warmup_ns': WARM,
            'sample_ns': SAMPLE,
        }
        d, raw = call(cc, 'batch', cfg)
        controls.append({'stage': stage, 'result': d, **raw, **aa_check(d, 'ns_per_batch')})
        if stage == 'after':
            break
        for stem, name in chosen:
            m = model[stem, name]
            best = min(m['alternatives'], key=lambda k: m['alternatives'][k]['prepared_median_ns'])
            a = m['alternatives'][best]
            n = a['estimated_jobs']
            stable = a['status'] == 'model' and n is not None and n <= 1024
            sizes = sorted({1, max(2, n - 1), min(1024, max(2, math.ceil(n * 1.2) + 1))}) if stable else [1, 8]
            last = None
            for size in sizes:
                last = take(stem, name, size)
            for attempt in range(2):
                if not stable or last['wins_every_alternative_with_2percent_margin'] or last['batch_size'] >= 1024:
                    break
                last = take(stem, name, min(1024, last['batch_size'] * 2))
    save(
        R / ('amortization-batches-' + cc + '.json'),
        {'status': 'complete', 'metadata': meta, 'rows': rows, 'aa': controls},
    )


def order_controls(cc, cases):
    meta = metadata(cc)
    selected = []
    rows = []
    controls = []
    for stem in ['product', 'size']:
        for row in read(R / ('data-' + stem + '-' + cc) / 'results.json')['rows']:
            candidate = 'replacer' if cases[stem, row['case']]['operation'] == 'replace' else 'matcher'
            samples = row['time']['ns_per_job']
            others = [m for m in row['methods'] if m != candidate]
            best = min(others, key=lambda m: st.median(samples[m]))
            delta = st.median([b / a - 1 for a, b in zip(samples[best], samples[candidate])])
            reasons = []
            if len(row['methods']) % 2 == 0:
                reasons.append('even method count: incomplete positional balance in main rotation')
            if abs(delta) <= 0.05:
                reasons.append('candidate within5% of fastest alternative')
            if any(max(v) / min(v) > 1.1 for v in samples.values()):
                reasons.append('main sample max/min exceeds1.10')
            if reasons:
                selected.append((stem, row, reasons))
    save(
        R / ('order-confirmation-' + cc + '.json'),
        {
            'status': 'running',
            'metadata': meta,
            'selection_rule': 'all even method counts, candidate within5% of best alternative, or any time sample max/min>1.10; original data retained',
            'planned_rows': len(selected),
            'rows': rows,
            'aa': controls,
        },
    )
    for stage in ['before', 'after']:
        case = cases['product', 'moderation.en.clean']
        cfg = {
            'case': case,
            'lifecycle': 'worker',
            'methods': {'a': 'matcher', 'b': 'matcher'},
            'mode': 'time',
            'passes': PASSES,
            'warmup_ns': WARM,
            'sample_ns': SAMPLE,
        }
        d, raw = call(cc, 'order-harness', cfg)
        controls.append({'stage': stage, 'result': d, **raw, **aa_check(d, 'ns_per_job')})
        if stage == 'after':
            break
        for stem, original, reasons in selected:
            state('order-confirmation', compiler=cc, case=original['case'], complete=len(rows), total=len(selected))
            case = cases[stem, original['case']]
            cfg = {
                'case': case,
                'lifecycle': original['lifecycle'],
                'methods': case['methods'],
                'mode': 'check',
                'passes': PASSES,
                'warmup_ns': WARM,
                'sample_ns': SAMPLE,
            }
            check, check_raw = call(cc, 'order-harness', cfg)
            cfg['mode'] = 'time'
            cfg['methods'] = {m: m for m in case['methods']}
            d, raw = call(cc, 'order-harness', cfg)
            assert d['sink'] == PASSES * sum(expected_sink(case, count, 1) for count in d['iterations'].values())
            rows.append(
                {
                    'corpus': stem,
                    'case': original['case'],
                    'lifecycle': original['lifecycle'],
                    'reasons': reasons,
                    'original_time': original['time'],
                    'time': d,
                    'check': check,
                    'check_raw': check_raw,
                    'raw': raw,
                }
            )
            save(
                R / ('order-confirmation-' + cc + '.json'),
                {'status': 'running', 'metadata': meta, 'planned_rows': len(selected), 'rows': rows, 'aa': controls},
            )
            print('ORDER CONFIRMATION', cc, original['case'], original['lifecycle'], flush=True)
    save(
        R / ('order-confirmation-' + cc + '.json'),
        {
            'status': 'complete',
            'metadata': meta,
            'selection_rule': 'all even method counts, candidate within5% of best alternative, or any time sample max/min>1.10; original data retained',
            'planned_rows': len(selected),
            'rows': rows,
            'aa': controls,
        },
    )


if '--validate' in sys.argv:
    PINNED_CODE = read(R / 'supplement-smoke-manifest.json')
    for cc in BUILDS:
        metadata(cc)
    cases = load_cases()
    assert len(cases) == 126
    sibling_path = Path(f'/sys/devices/system/cpu/cpu{CPU}/topology/thread_siblings_list')
    siblings = set()
    for value in sibling_path.read_text().strip().split(','):
        bounds = list(map(int, value.split('-')))
        siblings.update(range(bounds[0], bounds[-1] + 1))
    assert SIBLING != CPU and SIBLING in siblings, 'Invalid SMT sibling'
    print('SUPPLEMENT PREFLIGHT PASS: binaries, helpers, source, corpora, topology')
    sys.exit(0)

entry_lock = (R / 'post-run.lock').open('a')
fcntl.flock(entry_lock, fcntl.LOCK_EX | fcntl.LOCK_NB)


def fresh_outputs():
    raw = R / 'supplement-raw'
    assert not raw.exists() or not any(raw.iterdir()), 'Use a fresh supplement output directory'
    for pattern in [
        'constructors-*.json',
        'amortization-*.json',
        'order-confirmation-*.json',
        'memory-*.json',
        'SUPPLEMENTS_COMPLETE',
    ]:
        assert not list(R.glob(pattern)), 'Existing completed/incremental supplement data: ' + pattern


try:
    fresh_outputs()
    assert (R / 'SUPPLEMENTS_SMOKE_COMPLETE').read_text().strip() == 'PASS'
    PINNED_CODE = read(R / 'supplement-smoke-manifest.json')
    assert set(PINNED_CODE) == {'batch.php', 'construction.php', 'definitions.php', 'order-harness.php'}
    PINNED_CODE['measure.py'] = digest(__file__)
    for name, expected in PINNED_CODE.items():
        assert digest(Path(__file__) if name == 'measure.py' else R / name) == expected
    save(R / ('run-manifest-' + str(os.getpid()) + '.json'), PINNED_CODE)
    assert not (R / 'failure.json').exists(), 'Main matrix failure flag'
    assert (R / 'MATRIX_COMPLETE').read_text().strip() == 'PASS'
    for cc in BUILDS:
        for stem, total in [('product', 92), ('size', 158)]:
            d = read(R / ('data-' + stem + '-' + cc) / 'results.json')
            assert d['status'] == 'complete' and len(d['rows']) == total and d['metadata']['source_revision'] == REV
    assert (R / 'SUPPLEMENTS_SMOKE_COMPLETE').read_text().strip() == 'PASS'
    smoke = read(R / 'supplement-smoke-manifest.json')
    for name, sha in smoke.items():
        assert digest(R / name) == sha, 'Stale supplement smoke: ' + name
    lock = Path(f'/tmp/php-bench-multi-pattern-cpu-{CPU}.lock').open('w')  # noqa: SIM115 -- held until process exit
    fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
    fresh_outputs()
    cases = load_cases()
    for cc in BUILDS:
        order_controls(cc, cases)
        memory(cc)
        constructors(cc)
        model = models(cc, cases)
        batches(cc, cases, model)
        metadata(cc)
    (R / 'SUPPLEMENTS_COMPLETE').write_text('PASS\n')
    state('complete')
    print('SUPPLEMENTS COMPLETE', flush=True)
except BaseException as e:
    save(
        R / 'failure-post.json',
        {'error': repr(e), 'time': datetime.datetime.now(datetime.UTC).isoformat(), 'pid': os.getpid()},
    )
    raise
