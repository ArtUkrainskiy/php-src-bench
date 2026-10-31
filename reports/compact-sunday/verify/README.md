# Correctness checks

The frozen [standalone adapter](standalone.c) contains the stock matcher from
cf1b5771a76 and compact matcher from 8d7babbc364, plus the unchanged inline
dispatch. The private stock symbols are renamed to coexist in one translation
unit. This is a correctness adapter, not a performance benchmark. Its unused
x86 header is inherited from the earlier adapter; it is not a production dependency.

[validate.c](validate.c) compares both matchers with libc `memmem`. It includes
20,000 deterministic random inputs with seed 20261030 and 135,460 guarded
length configurations. Some configurations make multiple comparisons. Small
inputs deliberately retain the existing inline path. These are not 135,460
tests exclusively of the new compact helper.

On Linux x86-64, with GCC or Clang and libc `memmem`:

```sh
COMPACT_CHECK=$(mktemp -d)
cc -std=gnu11 -O1 -g -fsanitize=address,undefined \
  -fno-omit-frame-pointer reports/compact-sunday/verify/validate.c \
  -o "$COMPACT_CHECK/check"
"$COMPACT_CHECK/check" 20000
```

Expected output is `random=20000 guarded=135460: candidate/base/libc checks passed`.
The original GCC 13 and Clang 18 runs are recorded in
[c-validation.json](../data/c-validation.json). Each compiler also detected both
deliberate mutations: changing the compact default shift from `needle_len + 1`
to `needle_len + 2`, or changing its last-position loop from `p <= end` to
`p < end`. Both exit with mismatch code 3 at the explicit last-position fixture.
The [original C validation archive](../data/c-verification.tar.gz) contains the
captured generation/build driver, six source snapshots and their build/run logs.
It records the sanitizer compiler options used for these exact runs.

Full PHP string PHPT logs for six candidate release compilers, two AMD stock
builds and one candidate ASan/UBSan build are preserved in
[php-validation.tar.gz](../data/php-validation.tar.gz), with
[parsed counts](../data/php-validation-summary.json). To reproduce with a full
build, run from its php-src build directory:

```sh
sapi/cli/php -n run-tests.php -q -j8 -p "$PWD/sapi/cli/php" \
  --offline ext/standard/tests/strings
```

For a full debug ASan/UBSan build, add `--asan` and set `USE_ZEND_ALLOC=0`.
The archive includes the original driver setting that environment variable and
the Clang 21 sanitizer build metadata.
The added PHPT in the source patch checks 300 inputs. No ARM, Windows or 32-bit
build is represented by these results.

[corpus-audit.php](corpus-audit.php) records search operands from the owned
233-case corpus. Invoke it with a php-src-bench root and an existing output
directory. It distinguishes searched strings from replacement strings.
The [route summary](../data/corpus-route-summary.json) also records an earlier
instrumented adaptive-matcher run at 8c6759. Those route counts describe that
version, not the compact-only candidate. This capture script alone does not
reproduce internal adaptive-route instrumentation.

[check.py](../check.py) verifies report arithmetic, raw hashes and PHPT counts
without running benchmarks. It does not rerun correctness tests or turn the
quick timing series into statistically independent rounds.
