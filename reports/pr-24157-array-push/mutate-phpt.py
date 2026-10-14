#!/usr/bin/env python3
# Which of the mutations in mutate.py the php-src tests catch: apply each to the ap-c18-mut build,
# rebuild, run ext/standard/tests/array (with the PR's new test) under ASan and list failed tests.
#   BENCH_BUILDS=<dir with the builds> mutate-phpt.py
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


def tests(paths=("ext/standard/tests/array",)):
    # failed tests from the FAILED TEST SUMMARY section (per-test lines carry progress escapes with -j)
    env = dict(os.environ, USE_ZEND_ALLOC="0", TEST_PHP_EXECUTABLE=f"{B}/sapi/cli/php", NO_INTERACTION="1")
    r = subprocess.run([f"{B}/sapi/cli/php", "-n", "run-tests.php", "-q", "-j6", "--asan", *paths], cwd=B, capture_output=True, text=True, timeout=2400, env=env)
    lines = r.stdout.splitlines()
    if "FAILED TEST SUMMARY" not in r.stdout:
        return []
    i = next(k for k, l in enumerate(lines) if "FAILED TEST SUMMARY" in l) + 2
    out = []
    while i < len(lines) and not lines[i].startswith("====="):
        if lines[i].rstrip().endswith("]"):
            out.append(lines[i].rsplit("[", 1)[-1].rstrip().rstrip("]"))
        i += 1
    return sorted(set(out))

path = os.path.join(B, F)
orig = open(path).read()
for name, a, b in MUT:
    assert orig.count(a) == 1, name
    try:
        open(path, "w").write(orig.replace(a, b))
        subprocess.run(["make", "-j8"], cwd=B, capture_output=True, check=True, timeout=900)
        failed = tests()
        print(f"{name:40} {'CAUGHT by ' + str(len(failed)) + ': ' + ', '.join(f.rsplit('/', 1)[-1] for f in failed[:4]) if failed else 'missed'}", flush=True)
    finally:
        open(path, "w").write(orig)
subprocess.run(["make", "-j8"], cwd=B, capture_output=True, check=True, timeout=900)
print("unmutated:", tests() or "all pass")
