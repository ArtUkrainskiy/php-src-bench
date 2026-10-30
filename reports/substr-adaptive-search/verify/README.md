# Reproducing the matching checks

`standalone.c` extracts the candidate matching functions and the unchanged inline dispatch from the stated PHP commit. The recorded hashes and exact-source assertions are in [validation.json](../data/validation.json). This harness checks the extracted matching code; the full PHP release and debug/ZTS tests are recorded separately.

`validate.c` compares the inline candidate and each new stage with libc `memmem`. It covers empty and binary strings, matches at the end, random inputs and inaccessible guard pages. With an argument of 100000 it also executes the recorded 135460 guarded configurations. Run from this directory on an x86-64 Linux system with GCC or Clang:

```sh
cc -O1 -g -fsanitize=address,undefined -fno-omit-frame-pointer validate.c -o /tmp/substr-check
/tmp/substr-check 100000
cc -O1 -g -U__SSE2__ -fsanitize=address,undefined -fno-omit-frame-pointer validate.c -o /tmp/substr-check-scalar
/tmp/substr-check-scalar 100000
python3 mutate.py
python3 complexity.py
```

The `-U__SSE2__` run forces the portable matching fallback on this x86 host; it does not validate native Arm or 32-bit code generation. The standalone adapter uses x86 headers. The expected successful sanitizer output is recorded in [SSE2](validation-asan.txt) and [scalar](validation-scalar.txt).

[Functional mutations](mutations.json) must fail with a mismatched result. The [work-count audit](complexity.txt) counts compared bytes, including full candidate verification, on a sparse prefix followed by a dense suffix. It rejects disabled filter/Sunday budgets and a missing window reset. Its bound is an audit of these fixtures, not a formal complexity proof for all possible inputs or a latency benchmark.
