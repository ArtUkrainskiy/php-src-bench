#!/usr/bin/env python3
# Mutation check of difftest.php: apply one mutation to the PR's array.c in the as-mut build
# (a `bench build` of master + PR #23517), rebuild, compare difftest with master's output.
import os, subprocess

B = os.path.join(os.environ["BENCH_BUILDS"], "as-mut")
HERE = os.path.dirname(os.path.abspath(__file__))
REF = open(os.path.join(HERE, "difftest-master.txt")).read()
F = "ext/standard/array.c"
MUT = [
    ("fast path also for arrays with holes", "\t\t\tif (without_holes) {", "\t\t\tif (1) {"),
    ("one slot too many", "\t\t\t\t\tk = ht->nNumUsed - 1;", "\t\t\t\t\tk = ht->nNumUsed;"),
    ("two-element case copies slot 2", "ZVAL_COPY_VALUE(ht->arPacked, ht->arPacked + 1);", "ZVAL_COPY_VALUE(ht->arPacked, ht->arPacked + 2);"),
    ("vacated last slot not cleared", "\t\t\t\t\tZVAL_UNDEF(ht->arPacked + k);\n", "\t\t\t\t\t(void) 0;\n"),
    ("next free index one too high", "\t\tZ_ARRVAL_P(stack)->nNumUsed = k;\n\t\tZ_ARRVAL_P(stack)->nNextFreeElement = k;", "\t\tZ_ARRVAL_P(stack)->nNumUsed = k;\n\t\tZ_ARRVAL_P(stack)->nNextFreeElement = k + 1;"),
]

def run():
    r = subprocess.run([f"{B}/sapi/cli/php", "-n", os.path.join(HERE, "difftest.php"), "500000", "7"], capture_output=True, text=True, timeout=1200)
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
