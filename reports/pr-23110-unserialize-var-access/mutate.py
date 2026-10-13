#!/usr/bin/env python3
# Mutation check of difftest.php: apply one mutation to the PR's var_unserializer.re in the unser-mut build
# (a `bench build` of master + PR), rebuild (re2c regenerates the scanner), compare difftest with master's output.
import os, subprocess

B = os.path.join(os.environ.get("BENCH_BUILDS", os.path.expanduser("~/CLionProjects/php-builds")), "unser-mut")
HERE = os.path.dirname(os.path.abspath(__file__))
REF = open(os.path.join(HERE, "difftest-master.txt")).read()
F = "ext/standard/var_unserializer.re"
MUT = [
    ("last slot of a chunk accepted", "if (slot >= var_hash->used_slots) return NULL;", "if (slot > var_hash->used_slots) return NULL;"),
    ("chunk index off by one", "zend_long chunk_index = rem / VAR_ENTRIES_MAX;", "zend_long chunk_index = (rem + 1) / VAR_ENTRIES_MAX;"),
    ("slot off by one", "zend_long slot = rem % VAR_ENTRIES_MAX;", "zend_long slot = (rem + 1) % VAR_ENTRIES_MAX;"),
    ("last base slot sent to overflow path", "if (id < VAR_ENTRIES_MAX) {", "if (id < VAR_ENTRIES_MAX - 1) {"),
    ("overflow chunk not recorded", "(*var_hashx)->chunk_list[(*var_hashx)->num_chunks++] = var_hash;", "(*var_hashx)->chunk_list[(*var_hashx)->num_chunks] = var_hash; if (0) (*var_hashx)->num_chunks++;"),
    ("unused base slot accepted", "if (id >= d->entries.used_slots) return NULL;", "if (id > d->entries.used_slots) return NULL;"),
]

def run():
    r = subprocess.run([f"{B}/sapi/cli/php", "-n", os.path.join(HERE, "difftest.php"), "3000", "7"], capture_output=True, text=True, timeout=1200)
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
