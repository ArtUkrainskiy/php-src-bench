#!/usr/bin/env python3
# Mutation check of difftest.php: apply one mutation to the PR sources in the binhex-mut build (a `bench build` of the PR),
# rebuild, and see whether difftest output differs from master's.
import subprocess, os

B = os.path.join(os.environ.get("BENCH_BUILDS", os.path.expanduser("~/CLionProjects/php-builds")), "binhex-mut")
HERE = os.path.dirname(os.path.abspath(__file__))
REF = open(os.path.join(HERE, "difftest-master.txt")).read()

MUT = [
    ("ext/standard/string.c", "accept 'G' (hi_bound_upper 0x48)", "_mm_set1_epi8(0x47); /* 'F' + 1 */", "_mm_set1_epi8(0x48); /* 'F' + 1 */"),
    ("ext/standard/string.c", "accept '/' (lo_bound_digit 0x2e)", "_mm_set1_epi8(0x2f); /* '0' - 1 */", "_mm_set1_epi8(0x2e); /* '0' - 1 */"),
    ("ext/standard/string.c", "validate only the first half", "if (_mm_movemask_epi8(valid) != 0xffff) {", "if (half == 0 && _mm_movemask_epi8(valid) != 0xffff) {"),
    ("ext/standard/string.c", "no restart: skip failed chunk", "\t\t\tbreak;\n\t\t}\n\t}\n#endif", "\t\t\tcontinue;\n\t\t}\n\t}\n#endif"),
    ("ext/standard/string.c", "letter offset 10 instead of 9", "_mm_set1_epi8(9);\n\tconst __m128i word_lo_mask", "_mm_set1_epi8(10);\n\tconst __m128i word_lo_mask"),
    ("Zend/zend_string.c", "bin2hex: '9' < c threshold 8", "const __m128i nine = _mm_set1_epi8(9);", "const __m128i nine = _mm_set1_epi8(8);"),
    ("Zend/zend_string.c", "bin2hex: tail skipped", "zend_bin2hex_impl(out + i * 2, in + i, in_len - i, zend_hexconvtab);\n}\n#endif", "}\n#endif"),
]

def run():
    return subprocess.run([f"{B}/sapi/cli/php", "-n", os.path.join(HERE, "difftest.php"), "200000", "7"],
                          capture_output=True, text=True, timeout=600).stdout

for path, name, a, b in MUT:
    f = os.path.join(B, path)
    orig = open(f).read()
    assert orig.count(a) == 1, name
    try:
        open(f, "w").write(orig.replace(a, b))
        subprocess.run(["make", "-j8"], cwd=B, capture_output=True, check=True, timeout=900)
        out = run()
        diff = [l.split()[0] + " " + l.split()[1] for l, r in zip(out.splitlines(), REF.splitlines()) if l != r]
        print(f"{name:38} {'CAUGHT: ' + ', '.join(diff) if diff else 'missed'}", flush=True)
    finally:
        open(f, "w").write(orig)
subprocess.run(["make", "-j8"], cwd=B, capture_output=True, check=True, timeout=900)
print("unmutated:", "same as master" if run() == REF else "DIFFERENT")
