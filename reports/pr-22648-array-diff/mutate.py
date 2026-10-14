#!/usr/bin/env python3
# Mutation check of difftest.php: apply one mutation to the PR's array.c in the ad-mut build
# (a `bench build` of master + PR #22648), rebuild, compare difftest with master's output.
import os, subprocess

B = os.path.join(os.environ["BENCH_BUILDS"], "ad-mut")
HERE = os.path.dirname(os.path.abspath(__file__))
REF = open(os.path.join(HERE, "difftest-master.txt")).read()
F = "ext/standard/array.c"
MUT = [
    ("no out-of-range check", "\t\tif (offset >= range || !zend_bitset_in(exclude, (uint32_t) offset)) {", "\t\tif (!zend_bitset_in(exclude, (uint32_t) offset)) {"),
    ("minimum never updated", "\t\t\tif (Z_LVAL_P(value) < min) {\n\t\t\t\tmin = Z_LVAL_P(value);", "\t\t\tif (0) {\n\t\t\t\tmin = Z_LVAL_P(value);"),
    ("no addref on copied values", "\t\t\tzval_add_ref(value);\n\t\t}\n\t} ZEND_HASH_FOREACH_END();\n\n\tefree(exclude);", "\t\t\t(void) 0;\n\t\t}\n\t} ZEND_HASH_FOREACH_END();\n\n\tefree(exclude);"),
    ("string keys dropped", "\t\tif (offset >= range || !zend_bitset_in(exclude, (uint32_t) offset)) {\n\t\t\tif (key) {", "\t\tif (offset >= range || !zend_bitset_in(exclude, (uint32_t) offset)) {\n\t\t\tif (0) {"),
    ("first array type not checked", "\tif (!php_array_values_are_all_long(Z_ARRVAL(args[0]))) {", "\tif (0) {"),
    ("references not dereferenced in the copy loop", "\t\tentry = value;\n\t\tZVAL_DEREF(entry);", "\t\tentry = value;"),
]

def run():
    r = subprocess.run([f"{B}/sapi/cli/php", "-n", os.path.join(HERE, "difftest.php"), "200000", "7"], capture_output=True, text=True, timeout=1200)
    return r.stdout if r.returncode == 0 else f"exit {r.returncode}\n" + r.stdout

path = os.path.join(B, F)
orig = open(path).read()
for name, a, b in MUT:
    assert orig.count(a) == 1, name
    try:
        open(path, "w").write(orig.replace(a, b))
        subprocess.run(["make", "-j8"], cwd=B, capture_output=True, check=True, timeout=900)
        out = run()
        if out.startswith("exit"):
            print(f"{name:32} CAUGHT: {out.splitlines()[0]}", flush=True)
            continue
        diff = [l.split("  ")[0].strip() for l, r in zip(out.splitlines(), REF.splitlines()) if l != r]
        print(f"{name:32} {'CAUGHT: ' + ', '.join(diff) if diff else 'missed'}", flush=True)
    finally:
        open(path, "w").write(orig)
subprocess.run(["make", "-j8"], cwd=B, capture_output=True, check=True, timeout=900)
print("unmutated:", "same as master" if run() == REF else "DIFFERENT")
