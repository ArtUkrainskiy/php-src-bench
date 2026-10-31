#!/usr/bin/env python3
"""Extract the actual matcher, audit route reachability, and test audit mutations."""
from pathlib import Path
import argparse
import hashlib
import json
import struct
import subprocess

p = argparse.ArgumentParser(description=__doc__)
p.add_argument('--source', type=Path, required=True)
p.add_argument('--cc', default='gcc')
p.add_argument('--sanitize', action='store_true')
p.add_argument('--adapter', type=Path, help='frozen standalone.c compatibility adapter')
p.add_argument('--out', type=Path, help='directory for generated sources and logs')
a = p.parse_args()
script_root = Path(__file__).resolve().parent
root = a.out.resolve() if a.out else script_root
root.mkdir(parents=True, exist_ok=True)
adapter_path = a.adapter or script_root.parents[2] / 'reports/substr-adaptive-search/verify/standalone.c'
adapter = adapter_path.read_text()
source = (a.source / 'Zend/zend_operators.c').read_text()
start = '#define ZEND_MEMNSTR_GRAM_SAMPLE_SIZE'
core = source[source.index(start):source.index('ZEND_API const char* ZEND_FASTCALL zend_memnrstr_ex(')]
prefix = adapter[:adapter.index(start)]
inline_start = adapter.rfind('static', 0, adapter.index('\nzend_memnstr('))
suffix = adapter[inline_start:adapter.index('typedef const unsigned char *(*finder)')]
instrumented = core
for name in ['sunday_short', 'sunday_adaptive', 'adaptive', 'gram4', 'twoway']:
    pos = instrumented.index('zend_memnstr_' + name + '(')
    brace = instrumented.index('{', pos)
    instrumented = instrumented[:brace + 1] + '\n audit_enter("' + name + '", haystack);' + instrumented[brace + 1:]
instrumented = instrumented.replace('while (span - pos >= 16) {', 'while (span - pos >= 16) { audit_pair_blocks++;')
instrumented = instrumented.replace('while (span - pos >= ZEND_MEMNSTR_GRAM_STEP) {', 'while (span - pos >= ZEND_MEMNSTR_GRAM_STEP) { audit_gram_blocks++;')
pair = instrumented.index('static const char *zend_memnstr_adaptive(')
instrumented = instrumented[:pair] + instrumented[pair:].replace('for (; pos < span; pos++) {', 'for (; pos < span; pos++) { audit_pair_tail++;', 1)
instrumented = instrumented.replace('size_t i = MAX(cut, memory);', 'size_t i = MAX(cut, memory); if (memory) audit_memory++;')
audit = '''
static const char *audit_base;
static unsigned audit_pair_blocks, audit_pair_tail, audit_gram_blocks, audit_memory;
static void audit_enter(const char *name, const char *h) {
    printf(" %s:%zu", name, (size_t)(h - audit_base));
}
'''
main = '''
int main(void) {
    uint64_t hl, nl; int64_t expected; size_t index = 0;
    while (fread(&hl, 8, 1, stdin) == 1) {
        if (fread(&nl, 8, 1, stdin) != 1 || fread(&expected, 8, 1, stdin) != 1) return 2;
        char *h = malloc(hl), *n = malloc(nl);
        if (!h || !n || fread(h, hl, 1, stdin) != 1 || fread(n, nl, 1, stdin) != 1) return 2;
        audit_base = h;
        audit_pair_blocks = audit_pair_tail = audit_gram_blocks = audit_memory = 0;
        printf("%zu", index++);
        const char *match = zend_memnstr(h, n, nl, h + hl);
        int64_t got = match ? match - h : -1;
        printf(" result:%lld pair_blocks:%u pair_tail:%u gram_blocks:%u memory:%u\\n",
            (long long)got, audit_pair_blocks, audit_pair_tail, audit_gram_blocks, audit_memory);
        free(h); free(n);
        if (got != expected) return 1;
    }
    return 0;
}
'''
cases = []
def add(name, h, n, routes, tail=False, gram=False, memory=False):
    cases.append(dict(name=name, h=h, n=n, routes=routes, tail=tail, gram=gram, memory=memory))
for m in [32, 33, 63, 64, 65, 255, 256, 257]:
    n = b'a' * (m - 1) + b'b'
    size = 8192 + ((m + 13) % 16)
    positions = [46, 47, 48] + [size - m - i for i in range(15)]
    add(f'pair/{m}/absent', b'a' * size, n, ['sunday_adaptive:0', 'adaptive:31'], True)
    for i, t in enumerate(positions):
        h = bytearray(b'a' * size); h[t + m - 1] = ord('b')
        add(f'pair/{m}/start-{t}', bytes(h), n, ['sunday_adaptive:0', 'adaptive:31'], i >= 3)
n = b'a' * 31 + b'b'
prefix_h = b'a' * 64 + b'c'
for label, h, routes, gram in [
    ('selective', (prefix_h + b'ab' * 8192)[:16384], ['adaptive:31', 'gram4:1056'], True),
    ('dense', (prefix_h + b'aaab' * 4096)[:16384], ['adaptive:31', 'gram4:2078', 'twoway:2078'], False),
    ('changing', (prefix_h + b'ab' * 4096)[:8192] + b'aaab' * 14336,
     ['adaptive:31', 'gram4:4128', 'twoway:15837'], True),
]:
    add('gram/' + label + '/absent', h, n, routes, gram=gram)
    add('gram/' + label + '/present', h[:-32] + n, n, routes, gram=gram)
n = b'ab' * 16
h = (b'bb' + b'ab' * 15) * 2048
add('twoway/periodic-memory', h, n, ['adaptive:41', 'gram4:4405', 'twoway:4405'], memory=True)
add('twoway/periodic-memory-present', h[:-33] + b'c' + n, n,
    ['adaptive:41', 'gram4:4405', 'twoway:4405'], memory=True)
add('extra/gram-periodic-ascii', ((b'bb' + b'ab' * 15) * 3 + b'c' + b'abac' * 16384)[:65536],
    b'ab' * 16, ['adaptive:41', 'gram4:8174'], gram=True)
add('extra/gram-periodic-dna', ((b'TCGT' + b'ACGT' * 7) * 4 + b'x' + b'ACGA' * 16384)[:65536],
    b'ACGT' * 8, ['adaptive:81', 'gram4:8262'], gram=True)
payload = b''.join(struct.pack('<QQq', len(c['h']), len(c['n']), c['h'].find(c['n'])) + c['h'] + c['n'] for c in cases)
flags = ['-std=gnu11', '-O1', '-g', '-Wall', '-Wextra']
if a.sanitize:
    flags += ['-fsanitize=address,undefined', '-fno-omit-frame-pointer']
reports = {}
for mutation in ['none', 'drop-pair-bit15', 'skip-pair-tail']:
    text = prefix + audit + instrumented + suffix + main
    if mutation == 'drop-pair-bit15':
        i = text.index('static const char *zend_memnstr_adaptive(')
        text = text[:i] + text[i:].replace('while (mask) {', 'mask &= 0x7fff; while (mask) {', 1)
    if mutation == 'skip-pair-tail':
        text = text.replace('pos < span; pos++) { audit_pair_tail++;', 'pos < 0; pos++) { audit_pair_tail++;', 1)
    path = root / ('audit-' + a.cc.replace('/', '_') + '-' + mutation + ( '-asan' if a.sanitize else '') + '.c')
    path.write_text(text)
    executable = path.with_suffix('')
    subprocess.run([a.cc, *flags, str(path), '-o', str(executable)], check=True)
    result = subprocess.run([str(executable)], input=payload, capture_output=True)
    path.with_suffix('.log').write_bytes(result.stdout + result.stderr)
    if mutation == 'none':
        assert result.returncode == 0 and not result.stderr, result.stderr.decode(errors='replace')
        lines = result.stdout.decode().splitlines()
        assert len(lines) == len(cases)
        for case, line in zip(cases, lines):
            fields = line.split()[1:]
            for route in case['routes']:
                assert route in fields, (case['name'], route, line)
            counts = {k: int(v) for k, v in (s.split(':') for s in fields)}
            if case['tail']: assert counts['pair_tail'] > 0, case['name']
            if case['gram']: assert counts['gram_blocks'] > 0, case['name']
            if case['memory']: assert counts['memory'] > 0, case['name']
    else:
        assert result.returncode == 1, (mutation, result.returncode, result.stderr)
    reports[mutation] = dict(returncode=result.returncode, completed_lines=len(result.stdout.splitlines()))
manifest = dict(source=str(a.source), matcher_sha256=hashlib.sha256(core.encode()).hexdigest(),
                compiler=a.cc, compiler_version=subprocess.check_output([a.cc, '--version'], text=True).splitlines()[0],
                sanitize=a.sanitize, runs=reports,
                cases=[{k: v for k, v in c.items() if k not in ['h', 'n']} |
                       dict(haystack_bytes=len(c['h']), needle_bytes=len(c['n']),
                            haystack_sha256=hashlib.sha256(c['h']).hexdigest(),
                            needle_sha256=hashlib.sha256(c['n']).hexdigest(), expected=c['h'].find(c['n'])) for c in cases])
(root / ('audit-' + a.cc.replace('/', '_') + ('-asan' if a.sanitize else '') + '.json')).write_text(json.dumps(manifest, indent=2) + '\n')
print(len(cases), 'route fixtures passed; both boundary mutations rejected')
