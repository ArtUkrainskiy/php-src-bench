# bin2hex() and hex2bin() with SSE2/NEON (php-src PR #23789)

Review material for [php/php-src#23789](https://github.com/php/php-src/pull/23789) by adapik, "ext/standard: Add SSE2/NEON fast path for bin2hex()/hex2bin()". PR head [`c4c2ad73ee4`](https://github.com/php/php-src/pull/23789/commits/c4c2ad73ee495ef60483c168204d254ddb5899db), merged without conflicts onto master [`c65321c70f7`](https://github.com/php/php-src/commit/c65321c70f7); nothing had to be changed to build it. All measurements and checks on 13–14 October 2026.

The PR adds `zend_bin2hex_simd()` (16 input bytes per iteration, used by `bin2hex()` and every other caller of `zend_bin2hex()`: `md5()`, `sha1()`, `hash()`, openssl, opcache) and `php_hex2bin_simd_chunk()` (32 hex characters per call, with the existing scalar loop restarting at the first chunk that holds anything but a hex digit).

## Summary

Intel i7-13700H, cycles per call relative to master, four compilers (GCC 13.3, GCC 14.2, clang 18.1, clang 20.1), official Docker image flags:

| input | `bin2hex()` | `hex2bin()` (size of the binary side) |
|---|--:|--:|
| 4–15 bytes (no SIMD) | 0.99–1.13, instructions 1.00–1.03 | 1.01–1.04, instructions 1.03–1.05 |
| 16 bytes | 0.69–0.78 | 0.45–0.52 |
| 32 bytes | 0.56–0.64 | 0.33–0.36 |
| 64 bytes | 0.38–0.51 | 0.25–0.27 |
| 256 bytes | 0.21–0.24 | 0.17–0.23 |
| 1 KB | 0.16–0.17 | 0.13–0.21 |
| 64 KB | 0.14–0.15 | 0.11–0.21 |

| digest of a 32-byte input (hex output through `zend_bin2hex()`) | cycles |
|---|--:|
| `md5()` | 0.89–0.91 |
| `sha1()` | 0.95–0.98 |
| `hash('sha256')` | 0.83–0.88 |
| `hash('xxh128')` | 0.86–0.92 |

- **Big-endian AArch64: `hex2bin()` returns wrong bytes.** `zend_simd.h` enables the NEON path on every `__aarch64__` target. Built for `aarch64_be` with clang 18.1 and 20.1 and run under QEMU, `php_hex2bin_simd_chunk()` from the PR accepts every valid chunk and writes zeros instead of the decoded bytes (50,000 of 50,000 random valid chunks). Invalid chunks are still rejected, and `zend_bin2hex_simd()` is correct there. The same program built for little-endian AArch64 is correct. Details below.
- **Short `hex2bin()` inputs pay for the SIMD call.** Below 32 hex characters the SIMD loop never runs, yet `hex2bin()` executes 3–5% more instructions (1.01–1.04 of the cycles). The non-inlined call to `php_hex2bin_simd_chunk()` inside `zif_hex2bin()` makes the compiler save two more callee-saved registers and keep three values on the stack for every call. With `-falign-functions=64 -falign-loops=32` builds, the same change costs 1.13–1.20 of the cycles with clang 20.1 (+26 instructions, +20 cycles for 4 bytes). Moving the SIMD loop and the scalar tail after it into one non-inlined function, the way `zend_bin2hex()` already does it, removes this: 1.01–1.02 of the instructions and 0.98–1.03 of the cycles for 4–15 bytes, with the same gains on long inputs ([`tail-variant.diff`](tail-variant.diff)).
- **Invalid input** costs one wasted chunk at most: `hex2bin()` of 1 KB with one bad character at a random position takes 0.37–0.40 of master's cycles, since the SIMD path reaches the bad chunk sooner than the scalar loop.
- Output is byte for byte the same as master on x86-64 with all four compilers and under ASan/UBSan.

Not measured: AMD and ARM hardware (the PR description has numbers for a Ryzen 5 7500F and an Apple M2), GCC for big-endian AArch64, a full php-src build for big-endian AArch64.

## Full table

i7-13700H, P-core CPU 2, governor `powersave`, turbo on, kernel 7.0.0-34; cycles and instructions from `perf stat` over N calls minus the same process with 0 calls, divided by N. Five passes per case, master and the PR alternating (A B, B A, …); the value is the median ratio, in brackets the range over the passes. The second column is master's cycles per call with GCC 13.3, for scale. Short inputs come from a pool of 256 random strings of the same length (fixed seed), so that the branch predictor does not see one string repeated.

Builds: `bench build` with `BENCH_CFLAGS='-fstack-protector-strong -fpic -fpie -O2 -g -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64'`, `LDFLAGS='-Wl,-O1 -pie'` (the flags of the official Docker image, plus `-g`) and `--enable-werror`. Compilers: GCC 13.3.0, GCC 14.2.0, clang 18.1.3, clang 20.1.2. Raw data: [`intel-docker-20261014.txt`](intel-docker-20261014.txt).

### master → PR

| case | master, cycles (GCC 13) | GCC 13.3 | GCC 14.2 | clang 18.1 | clang 20.1 | instructions |
|---|--:|--:|--:|--:|--:|--:|
| bin2hex-4 | 73 | 1.05 [1.04–1.07] | 1.01 [1.01–1.03] | 1.01 [0.99–1.06] | 1.01 [1.00–1.01] | 1.00–1.03 |
| bin2hex-8 | 82 | 1.04 [1.02–1.06] | 1.01 [1.00–1.01] | 1.00 [1.00–1.02] | 1.03 [1.02–1.04] | 1.00–1.02 |
| bin2hex-15 | 95 | 1.06 [1.04–1.11] | 0.99 [0.98–1.49] | 1.13 [1.00–1.25] | 1.02 [1.01–1.03] | 1.00–1.02 |
| bin2hex-16 | 97 | 0.75 [0.74–0.79] | 0.73 [0.73–0.79] | 0.78 [0.78–0.78] | 0.69 [0.69–0.70] | 0.73–0.77 |
| bin2hex-20 | 105 | 0.80 [0.77–0.83] | 0.78 [0.78–0.80] | 0.79 [0.78–0.80] | 0.73 [0.73–0.74] | 0.77–0.79 |
| bin2hex-31 | 127 | 0.83 [0.83–0.92] | 0.84 [0.81–0.89] | 0.83 [0.81–0.84] | 0.82 [0.82–0.82] | 0.81–0.84 |
| bin2hex-32 | 129 | 0.59 [0.58–0.60] | 0.64 [0.59–0.69] | 0.63 [0.61–0.65] | 0.56 [0.55–0.56] | 0.57–0.63 |
| bin2hex-33 | 129 | 0.61 [0.60–0.61] | 0.62 [0.60–0.62] | 0.69 [0.65–0.83] | 0.54 [0.53–0.54] | 0.59–0.64 |
| bin2hex-48 | 158 | 0.51 [0.51–0.51] | 0.51 [0.49–0.53] | 0.59 [0.58–0.60] | 0.49 [0.49–0.50] | 0.48–0.54 |
| bin2hex-64 | 189 | 0.45 [0.44–0.46] | 0.38 [0.37–0.39] | 0.51 [0.50–0.52] | 0.44 [0.44–0.45] | 0.42–0.48 |
| bin2hex-100 | 269 | 0.38 [0.36–0.39] | 0.34 [0.33–0.34] | 0.43 [0.43–0.44] | 0.39 [0.39–0.39] | 0.37–0.41 |
| bin2hex-256 | 618 | 0.21 [0.21–0.22] | 0.22 [0.21–0.28] | 0.24 [0.23–0.28] | 0.24 [0.24–0.26] | 0.22–0.26 |
| bin2hex-1024 | 2,204 | 0.16 [0.16–0.17] | 0.16 [0.16–0.17] | 0.17 [0.17–0.19] | 0.16 [0.16–0.17] | 0.15–0.17 |
| bin2hex-64k | 133,748 | 0.14 [0.08–0.19] | 0.15 [0.13–0.17] | 0.15 [0.14–0.19] | 0.15 [0.14–0.15] | 0.12–0.14 |
| hex2bin-4 | 94 | 1.04 [1.03–1.07] | 1.02 [1.00–1.03] | 1.02 [1.01–1.03] | 1.02 [1.01–1.03] | 1.05–1.05 |
| hex2bin-8 | 124 | 1.02 [1.01–1.02] | 1.02 [1.02–1.04] | 1.03 [1.01–1.04] | 1.02 [1.02–1.04] | 1.04–1.05 |
| hex2bin-15 | 171 | 1.04 [1.02–1.04] | 1.02 [0.99–1.19] | 1.01 [1.00–1.03] | 1.02 [1.01–1.02] | 1.03–1.05 |
| hex2bin-16 | 182 | 0.48 [0.47–0.52] | 0.47 [0.47–0.48] | 0.52 [0.51–0.55] | 0.45 [0.45–0.46] | 0.43–0.49 |
| hex2bin-20 | 210 | 0.55 [0.54–0.56] | 0.53 [0.52–0.54] | 0.58 [0.56–0.58] | 0.55 [0.55–0.56] | 0.52–0.57 |
| hex2bin-31 | 313 | 0.64 [0.58–0.75] | 0.62 [0.61–0.64] | 0.67 [0.64–0.75] | 0.66 [0.65–0.66] | 0.66–0.70 |
| hex2bin-32 | 307 | 0.35 [0.35–0.38] | 0.33 [0.33–0.34] | 0.36 [0.35–0.42] | 0.33 [0.32–0.33] | 0.31–0.37 |
| hex2bin-33 | 320 | 0.36 [0.35–0.40] | 0.34 [0.34–0.36] | 0.38 [0.38–0.39] | 0.35 [0.35–0.36] | 0.33–0.39 |
| hex2bin-48 | 430 | 0.29 [0.28–0.30] | 0.28 [0.28–0.29] | 0.29 [0.28–0.29] | 0.28 [0.27–0.28] | 0.25–0.33 |
| hex2bin-64 | 550 | 0.27 [0.26–0.27] | 0.26 [0.26–0.27] | 0.26 [0.26–0.27] | 0.25 [0.24–0.25] | 0.22–0.30 |
| hex2bin-100 | 834 | 0.26 [0.25–0.27] | 0.27 [0.25–0.29] | 0.25 [0.25–0.26] | 0.25 [0.24–0.25] | 0.22–0.30 |
| hex2bin-256 | 1,985 | 0.20 [0.20–0.22] | 0.23 [0.22–0.23] | 0.17 [0.13–0.19] | 0.17 [0.17–0.18] | 0.15–0.23 |
| hex2bin-1024 | 7,527 | 0.17 [0.17–0.23] | 0.21 [0.20–0.22] | 0.13 [0.13–0.13] | 0.14 [0.14–0.14] | 0.13–0.21 |
| hex2bin-64k | 473,088 | 0.16 [0.15–0.18] | 0.21 [0.20–0.23] | 0.11 [0.11–0.12] | 0.13 [0.12–0.13] | 0.12–0.21 |
| hex2bin-upper-32 | 313 | 0.35 [0.34–0.37] | 0.33 [0.31–0.34] | 0.36 [0.36–0.37] | 0.33 [0.33–0.35] | 0.31–0.37 |
| hex2bin-mixed-32 | 312 | 0.34 [0.34–0.35] | 0.33 [0.32–0.33] | 0.36 [0.36–0.36] | 0.33 [0.32–0.33] | 0.31–0.37 |
| hex2bin-mixed-1024 | 7,419 | 0.17 [0.16–0.18] | 0.20 [0.19–0.22] | 0.13 [0.13–0.13] | 0.13 [0.13–0.15] | 0.13–0.21 |
| hex2bin-invalid-32 | 1,171 | 0.96 [0.95–0.96] | 1.02 [1.00–1.02] | 1.03 [1.00–1.03] | 1.00 [1.00–1.28] | 0.95–0.97 |
| hex2bin-invalid-1024 | 4,812 | 0.37 [0.36–0.38] | 0.40 [0.40–0.42] | 0.38 [0.37–0.38] | 0.39 [0.28–0.48] | 0.28–0.34 |
| md5-32 | 443 | 0.91 [0.90–0.98] | 0.90 [0.90–0.93] | 0.89 [0.89–0.91] | 0.89 [0.88–0.92] | 0.89–0.90 |
| sha1-32 | 484 | 0.98 [0.97–1.11] | 0.98 [0.96–1.02] | 0.95 [0.95–0.96] | 0.95 [0.94–0.95] | 0.94–0.95 |
| hash-xxh128-32 | 292 | 0.92 [0.92–0.92] | 0.92 [0.91–0.93] | 0.86 [0.86–0.87] | 0.88 [0.88–0.89] | 0.88–0.89 |
| hash-sha256-32 | 440 | 0.86 [0.86–0.89] | 0.88 [0.88–0.89] | 0.83 [0.83–0.83] | 0.88 [0.87–0.93] | 0.82–0.83 |

### master → PR with the SIMD loop and its scalar tail in one function ([`tail-variant.diff`](tail-variant.diff)), `hex2bin()` rows

| case | master, cycles (GCC 13) | GCC 13.3 | GCC 14.2 | clang 18.1 | clang 20.1 | instructions |
|---|--:|--:|--:|--:|--:|--:|
| hex2bin-4 | 94 | 1.02 [1.01–1.05] | 1.02 [1.01–1.03] | 1.01 [0.99–1.07] | 1.00 [0.99–1.02] | 1.01–1.02 |
| hex2bin-8 | 122 | 1.01 [1.00–1.08] | 1.02 [1.02–1.02] | 0.99 [0.99–1.00] | 0.98 [0.98–1.02] | 1.01–1.02 |
| hex2bin-15 | 172 | 1.03 [0.99–1.06] | 1.00 [0.99–1.04] | 0.99 [0.99–1.71] | 1.00 [1.00–1.01] | 1.01–1.01 |
| hex2bin-16 | 178 | 0.49 [0.49–0.50] | 0.48 [0.47–0.51] | 0.52 [0.52–0.54] | 0.47 [0.47–0.47] | 0.45–0.51 |
| hex2bin-32 | 310 | 0.35 [0.35–0.36] | 0.34 [0.34–0.34] | 0.37 [0.36–0.39] | 0.33 [0.33–0.34] | 0.32–0.39 |
| hex2bin-1024 | 7,423 | 0.17 [0.13–0.17] | 0.20 [0.20–0.21] | 0.14 [0.14–0.15] | 0.14 [0.13–0.15] | 0.13–0.22 |
| hex2bin-64k | 469,634 | 0.16 [0.16–0.17] | 0.21 [0.21–0.22] | 0.12 [0.12–0.13] | 0.13 [0.13–0.14] | 0.12–0.21 |

The rows of `bin2hex()` and the other `hex2bin()` rows are in the raw data (groups `g13t` … `c20t`); `bin2hex()` is not touched by the variant. One sample in the raw data is negative (`c18t change hex2bin-mixed-1024`, −104 cycles: the 0-call process took longer than the N-call one); it is one of five passes and does not move the median.

### Control

Master against master (GCC 13.3) in the same series: median ratios 0.98–1.02 over all 37 cases. One pass of one case was disturbed (spread up to 0.97 of the median); medians are used everywhere.

## Big-endian AArch64

`Zend/zend_simd.h` defines `XSSE2` and maps the SSE2 intrinsics to NEON for `__aarch64__` without looking at the byte order; php-src's configure recognises `aarch64_be` and defines `WORDS_BIGENDIAN` there.

[`be/gen.py`](be/gen.py) cuts `php_hex2bin_simd_chunk()`, `zend_bin2hex_simd()` and `zend_bin2hex_impl()` out of the PR sources and wraps them in a freestanding test program (no libc, inputs read through a `volatile` buffer so that nothing is constant-folded). It checks 50,000 random valid 32-character chunks (mixed case) and 50,000 chunks with one non-hex byte against a scalar reference, and `zend_bin2hex_simd()` on 2,000 inputs: the first one 256 bytes long holding every byte value, the rest 16–255 bytes. Output of all five builds: [`be/results.txt`](be/results.txt).

```sh
python3 be/gen.py <php-src with the PR> > harness.c
clang --target=aarch64_be-none-linux-gnu -O2 -ffreestanding -nostdlib -static -fno-builtin \
      -fuse-ld=lld -I<php-src>/Zend harness.c -o h-be      # any LLD; here -fuse-ld=/usr/bin/ld.lld-15
qemu-aarch64_be ./h-be                                     # qemu-user
```

| target, compiler | valid chunks decoded right | invalid chunks rejected | `bin2hex` inputs right |
|---|--:|--:|--:|
| x86-64, clang 18.1, `-O2` | 50,000 / 50,000 | 50,000 / 50,000 | 2,000 / 2,000 |
| aarch64 (little-endian), clang 18.1, `-O2`, `qemu-aarch64` 8.2.2 | 50,000 / 50,000 | 50,000 / 50,000 | 2,000 / 2,000 |
| aarch64_be, clang 18.1, `-O2`, `qemu-aarch64_be` 8.2.2 | **0** / 50,000 | 50,000 / 50,000 | 2,000 / 2,000 |
| aarch64_be, clang 18.1, `-O0` | **0** / 50,000 | 50,000 / 50,000 | 2,000 / 2,000 |
| aarch64_be, clang 20.1, `-O2` | **0** / 50,000 | 50,000 / 50,000 | 2,000 / 2,000 |

Every wrong chunk came back as 16 zero bytes (the harness counts them: 50,000 of 50,000 on each big-endian build), for example:

```
in   b25Db6b0507f311F7C5acBeBbD66FDe3
got  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
ref  b2 5d b6 b0 50 7f 31 1f 7c 5a cb eb bd 66 fd e3
```

The helper returns `true` for these chunks, so `hex2bin()` would return a string of the right length with wrong content. Excluding big-endian targets (`#if defined(XSSE2) && !defined(WORDS_BIGENDIAN)` around the `hex2bin()` part, as `Zend/zend_string.h` already does for its aarch64 code) avoids it; the `bin2hex()` part gave correct results on big-endian.

## Correctness on x86-64

- [`difftest.php`](difftest.php) prints one SHA-256 per section over every result (`var_export()`, so `false` for invalid hex is recorded):
  every length 0–300 for `bin2hex()` (20 random strings each); every byte value at every position of 16, 17, 32, 33 and 48-byte strings; every length 0–600 for `hex2bin()`, odd lengths included (10 mixed-case strings each); every byte value at every position of valid hex strings of 2, 30, 32, 34, 62, 64, 66, 96, 98 and 128 characters; all 65,536 pairs of characters at positions 0, 30, 31 and 62 of a 64-character string; 200,000 random strings of up to 2,000 characters, 30% of them with 1–3 random bytes replaced (seed 7).
- Identical output ([`difftest-master.txt`](difftest-master.txt)) on master, the PR and the variant with all four compilers, with both the Docker flags and the alignment flags, and on the PR built with `--enable-debug --enable-address-sanitizer --enable-undefined-sanitizer` (clang 18.1, `USE_ZEND_ALLOC=0`, nothing on stderr): [`difftest-builds.txt`](difftest-builds.txt).
- The check catches errors: [`mutate.py`](mutate.py) applies seven mutations to the PR one at a time (accept `G`, accept `/`, validate only the first half of a chunk, skip a failed chunk instead of restarting the scalar loop, a wrong letter offset, a wrong digit threshold in `bin2hex`, a missing `bin2hex` tail) and every one changes the output: [`mutate-output.txt`](mutate-output.txt).
- `ext/standard/tests/strings` and `ext/hash/tests`: 758 passed, 0 failed with GCC 13.3 and clang 20.1.

### The PR's tests

- `hex2bin_simd_boundary.phpt` lists a length of 2000, but the source string is `str_repeat('0123456789abcdefABCDEF', 10)`, 220 characters, so that case tests 220.
- Invalid characters are placed at offsets 0–63 of a 64-character string and at offsets 5 and 20 of the third chunk of a 160-character string, all inside SIMD chunks; the other two test files have no invalid input. No case puts one in the scalar tail after a completed SIMD loop, such as offsets 32 and 33 of a 34-character string or 64 and 65 of a 66-character one.

## Reproduce

From the root of php-src-bench, with `PHP_SRC` pointing at a php-src clone:

```sh
git -C $PHP_SRC fetch origin master pull/23789/head:pr23789
W=$PWD/../php-src-pr23789
git -C $PHP_SRC worktree add "$W" origin/master && git -C "$W" merge pr23789
F='-fstack-protector-strong -fpic -fpie -O2 -g -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64'
for cc in "cc g13" "gcc-14 g14" "clang c18" "clang-20 c20"; do set -- $cc
  CC=$1 BENCH_CFLAGS="$F" LDFLAGS='-Wl,-O1 -pie' BENCH_CONFIGURE_EXTRA=--enable-werror ./bench build binhex-$2-base origin/master
  CC=$1 BENCH_CFLAGS="$F" LDFLAGS='-Wl,-O1 -pie' BENCH_CONFIGURE_EXTRA=--enable-werror PHP_SRC="$W" ./bench build binhex-$2-pr .
done
cd reports/pr-23789-bin2hex-hex2bin
B=${BENCH_BUILDS:-../../../php-builds}
for b in g13-base g13-pr; do $B/binhex-$b/sapi/cli/php -n difftest.php 200000 7 | diff - difftest-master.txt && echo "$b ok"; done
CPU=2 PASSES=5 ./pairs-run.sh out.txt g13:g13-base:g13-pr g14:g14-base:g14-pr c18:c18-base:c18-pr c20:c20-base:c20-pr aa:g13-base:g13-base
./table.py out.txt g13,g14,c18,c20
```
