#!/usr/bin/env python3
# The three mutations from mutate.py that pass ext/standard/tests/array, against the two proposed tests
# (array_push_grow_boundary.phpt, array_push_holes_pointer.phpt) under ASan, in the ap-c18-mut build.
#   BENCH_BUILDS=<dir with the builds> mutate-proposed.py
import os, subprocess

B = os.path.join(os.environ["BENCH_BUILDS"], "ap-c18-mut")
HERE = os.path.dirname(os.path.abspath(__file__))
F = os.path.join(B, "ext/standard/array.c")
TESTS = [os.path.join(HERE, t) for t in ("array_push_grow_boundary.phpt", "array_push_holes_pointer.phpt")]
MUT = [
    ("unmutated", None, None),
    ("holes allowed to grow", "&& (argc <= room || HT_IS_WITHOUT_HOLES(ht))) {", "&& (argc <= room || 1)) {"),
    ("room one too large", "if (UNEXPECTED(argc > room)) {", "if (UNEXPECTED(argc > room + 1)) {"),
    ("table one slot short", "zend_hash_extend(ht, ht->nNumUsed + argc, true);", "zend_hash_extend(ht, ht->nNumUsed + argc - 1, true);"),
]

def result(test):
    env = dict(os.environ, USE_ZEND_ALLOC="0", TEST_PHP_EXECUTABLE=f"{B}/sapi/cli/php", NO_INTERACTION="1")
    r = subprocess.run([f"{B}/sapi/cli/php", "-n", "run-tests.php", "-q", "--asan", test], cwd=B, capture_output=True, text=True, timeout=600, env=env)
    return "FAIL" if "Tests failed    :     1" in r.stdout else ("PASS" if "Tests passed    :     1" in r.stdout else "?")

orig = open(F).read()
for name, a, b in MUT:
    try:
        if a:
            assert orig.count(a) == 1, name
            open(F, "w").write(orig.replace(a, b))
        subprocess.run(["make", "-j8"], cwd=B, capture_output=True, check=True, timeout=900)
        print(f"{name:25}", "  ".join(f"{os.path.basename(t)}: {result(t)}" for t in TESTS), flush=True)
    finally:
        open(F, "w").write(orig)
subprocess.run(["make", "-j8"], cwd=B, capture_output=True, check=True, timeout=900)
