from pathlib import Path
import subprocess
import tempfile

root = Path(__file__).resolve().parent
source = (root/'standalone.c').read_text()
prefix = r'''
#define _GNU_SOURCE
#include <stddef.h>
#include <stdint.h>
#include <stdio.h>
static uint64_t comparisons, twoway_calls;
static int audit_equal(unsigned char a, unsigned char b) { comparisons++; return a == b; }
static int audit_memcmp(const void *a, const void *b, size_t n) {
    const unsigned char *x = a, *y = b;
    for (size_t i = 0; i < n; i++) {
        if (!audit_equal(x[i], y[i])) return x[i] < y[i] ? -1 : 1;
    }
    return 0;
}
'''
source = source.replace('memcmp(', 'audit_memcmp(')
source = source.replace('needle[i] == haystack[pos + i]', 'audit_equal(needle[i], haystack[pos + i])')
source = source.replace('needle[i - 1] == haystack[pos + i - 1]', 'audit_equal(needle[i - 1], haystack[pos + i - 1])')
source = source.replace('if (needle[i] != p[i]) {', 'if (!audit_equal(needle[i], p[i])) {')
source = source.replace('size_t length = (size_t)(end - haystack);\n\tif (needle_len > length)',
    'twoway_calls++;\n\tsize_t length = (size_t)(end - haystack);\n\tif (needle_len > length)', 1)
source = source.replace('int main(int argc, char **argv)', 'int unused_manifest_main(int argc, char **argv)')
main = r'''
int main(void) {
    size_t prefix = 14000, dense = 131072, hl = prefix + dense;
    unsigned char *h = malloc(hl), n[1536];
    for (size_t i = 0; i < prefix; i++) h[i] = i % 200 ? 'x' : 'a';
    for (size_t i = 0; i < dense; i++) h[prefix + i] = "ab"[i % 2];
    int failed = 0;
    size_t lengths[] = {31, 32, 96, 384, 1536};
    for (size_t k = 0; k < 5; k++) {
        size_t nl = lengths[k];
        if (nl < 2 || nl > sizeof n) return 2;
        for (size_t i = 0; i < nl; i++) n[i] = "ab"[i % 2];
        n[nl - 2] = n[nl - 1] = 'b';
        comparisons = twoway_calls = 0;
        const unsigned char *got = zend_candidate_find(h, hl, n, nl);
        uint64_t bound = 32 * hl + 256 * nl;
        printf("needle=%zu hay=%zu compared_bytes=%llu bound=%llu twoway=%llu found=%d\n",
                nl, hl, (unsigned long long)comparisons, (unsigned long long)bound,
                (unsigned long long)twoway_calls, got != NULL);
        if (got || comparisons > bound) failed = 1;
    }
    free(h);
    return failed ? 3 : 0;
}
'''
with tempfile.TemporaryDirectory(prefix='substring-work-check-') as temporary:
    work = Path(temporary)
    for name, text in [('normal', source), ('budget-disabled', source.replace('if (--checks_left == 0)', 'if (0)')), ('sunday-budget-disabled', source.replace('if (deep_work > (size_t)(p - window)', 'if (0')), ('window-reset-disabled', source.replace('window = p + 1;', 'window = haystack;'))]:
        path = work / f'complexity-{name}.c'
        path.write_text(prefix + text + main)
        binary = work / f'complexity-{name}'
        subprocess.run(['gcc', '-O2', str(path), '-o', str(binary)], check=True)
        result = subprocess.run([str(binary)], capture_output=True, text=True)
        (root / f'complexity-{name}.log').write_text(result.stdout + result.stderr)
        print(name, 'exit=', result.returncode)
        print(result.stdout, end='')
        if (name == 'normal' and result.returncode != 0) or (name != 'normal' and result.returncode == 0):
            raise SystemExit('Complexity check did not distinguish the budget mutation')
