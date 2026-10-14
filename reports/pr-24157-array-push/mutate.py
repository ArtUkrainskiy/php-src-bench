#!/usr/bin/env python3
# Mutation check of difftest.php: apply one mutation to the PR's array.c in the ap-c18-mut build
# (master + PR #24157, clang, --enable-debug with ASan/UBSan), rebuild, run difftest and
# compare with the unmutated PR's output.
# Runs difftest twice: with USE_ZEND_ALLOC=0 (ASan sees every allocation) and with ZendMM
# (memory_get_usage() then shows the table size).
#   BENCH_BUILDS=<dir with the builds> mutate.py
import os, subprocess

B = os.path.join(os.environ["BENCH_BUILDS"], "ap-c18-mut")
HERE = os.path.dirname(os.path.abspath(__file__))
F = "ext/standard/array.c"
MUT = [
    ("internal pointer not restored", "\t\t\tht->nInternalPointer = pos;\n", ""),
    ("holes allowed to grow", "&& (argc <= room || HT_IS_WITHOUT_HOLES(ht))) {", "&& (argc <= room || 1)) {"),
    ("next index not checked", "if (appends_after_last\n", "if ((appends_after_last || 1)\n"),
    ("room one too large", "if (UNEXPECTED(argc > room)) {", "if (UNEXPECTED(argc > room + 1)) {"),
    ("table one slot short", "zend_hash_extend(ht, ht->nNumUsed + argc, true);", "zend_hash_extend(ht, ht->nNumUsed + argc - 1, true);"),
    ("value refcount not added", "\t\t\t\t\tZ_TRY_ADDREF(args[i]);\n\t\t\t\t\tZEND_HASH_FILL_ADD", "\t\t\t\t\tZEND_HASH_FILL_ADD"),
    ("uninitialized array not initialized", "\t\t\t} else if (HT_FLAGS(ht) & HASH_FLAG_UNINITIALIZED) {\n\t\t\t\tzend_hash_real_init_packed(ht);\n\t\t\t}", "\t\t\t}"),
]

def run():
    # without ZendMM for ASan, then with ZendMM so that memory_get_usage() shows the table size
    outs, rcs, errs = [], [], []
    for zm in ("0", "1"):
        env = dict(os.environ, USE_ZEND_ALLOC=zm)
        r = subprocess.run([f"{B}/sapi/cli/php", "-n", os.path.join(HERE, "difftest.php"), "3000", "7"], capture_output=True, text=True, timeout=1800, env=env)
        outs.append(r.stdout); rcs.append(r.returncode); errs.append(r.stderr)
    return "".join(outs), next((c for c in rcs if c != 0), 0), "".join(errs)

path = os.path.join(B, F)
orig = open(path).read()
subprocess.run(["make", "-j8"], cwd=B, capture_output=True, check=True, timeout=900)
ref, rc, err = run()
assert rc == 0 and not err.strip(), (rc, err[:500])
for name, a, b in MUT:
    assert orig.count(a) == 1, name
    try:
        open(path, "w").write(orig.replace(a, b))
        subprocess.run(["make", "-j8"], cwd=B, capture_output=True, check=True, timeout=900)
        out, rc, err = run()
        asan = next((l for l in err.splitlines() if "ERROR: AddressSanitizer" in l or "runtime error" in l or "Assertion" in l), None)
        diff = [" ".join(l.split(" ")[:2]) for l, r in zip(out.splitlines(), ref.splitlines()) if l != r]
        if asan:
            print(f"{name:40} CAUGHT by ASan/UBSan/assert: {asan.strip()[:120]}", flush=True)
        elif rc != 0:
            print(f"{name:40} CAUGHT: exit {rc}: {err.strip()[:120]}", flush=True)
        elif diff or len(out.splitlines()) != len(ref.splitlines()):
            print(f"{name:40} CAUGHT: {len(diff)} lines differ, first: {', '.join(diff[:3])}", flush=True)
        else:
            print(f"{name:40} missed", flush=True)
    finally:
        open(path, "w").write(orig)
subprocess.run(["make", "-j8"], cwd=B, capture_output=True, check=True, timeout=900)
print("unmutated:", "same as before" if run()[0] == ref else "DIFFERENT")
