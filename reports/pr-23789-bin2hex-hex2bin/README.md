# bin2hex() and hex2bin() with SSE2/NEON (php-src PR #23789)

Review material for [php/php-src#23789](https://github.com/php/php-src/pull/23789) by adapik, "ext/standard: Add SSE2/NEON fast path for bin2hex()/hex2bin()". PR head [`c4c2ad73ee4`](https://github.com/php/php-src/pull/23789/commits/c4c2ad73ee495ef60483c168204d254ddb5899db), merged without conflicts onto master [`c65321c70f7`](https://github.com/php/php-src/commit/c65321c70f7); nothing had to be changed to build it. Measured and checked on 13–14 October 2026.

The PR adds `zend_bin2hex_simd()`, 16 input bytes per iteration, used by `bin2hex()` and every other caller of `zend_bin2hex()` (`md5()`, `sha1()`, `hash()`, openssl, opcache), and `php_hex2bin_simd_chunk()`, 32 hex characters per call, with the existing scalar loop restarting at the first chunk that holds anything but a hex digit.

## Summary

- **Big-endian AArch64: `hex2bin()` returns wrong bytes.** `zend_simd.h` enables the NEON path on every `__aarch64__` target. Built for `aarch64_be` with clang 18.1 and 20.1 and run under QEMU, `php_hex2bin_simd_chunk()` accepts every valid chunk and writes zeros instead of the decoded bytes. `#if defined(XSSE2) && !defined(WORDS_BIGENDIAN)` avoids it. [Details](#big-endian-aarch64).
- **Long inputs:** from 256 bytes (512 hex characters) up both functions take 76–89% fewer cycles than master on all four compilers, 4.1–8.8× faster.
- **Short `hex2bin()` inputs pay for the SIMD call.** Below 32 hex characters the SIMD path never runs, yet `hex2bin()` executes 3–5% more instructions and takes 1–4% more cycles. Moving the SIMD loop and the scalar tail after it into one non-inlined function, as `zend_bin2hex()` does, removes it. [Details](#short-hex2bin-inputs).
- **Digests** reach the new `bin2hex()` path through `zend_bin2hex()`: `md5()` of 32 bytes takes 9–11% fewer cycles, `hash('sha256')` 12–17% fewer.
- **Output** is byte for byte the same as master on x86-64 with all four compilers and under ASan/UBSan.
- **Not measured:** AMD and ARM hardware (the PR description has numbers for a Ryzen 5 7500F and an Apple M2), GCC for big-endian AArch64, a full php-src build for big-endian AArch64.

## Results

Change in CPU cycles per call with the PR, relative to master (negative = fewer cycles, faster). Intel i7-13700H, one column per compiler, median of five alternating runs; the second column is master's cost for scale:

| call | master, CPU cycles per call (GCC 13.3) | GCC 13.3 | GCC 14.2 | clang 18.1 | clang 20.1 |
|---|--:|--:|--:|--:|--:|
| `bin2hex()`, 8 bytes | 82 | +4% | +1% | 0% | +3% |
| `bin2hex()`, 16 bytes | 97 | −25% | −27% | −22% | −31% |
| `bin2hex()`, 32 bytes | 129 | −41% | −36% | −37% | −44% |
| `bin2hex()`, 256 bytes | 618 | −79% | −78% | −76% | −76% |
| `bin2hex()`, 64 KB | 133,748 | −86% | −85% | −85% | −85% |
| `hex2bin()`, 16 hex characters | 124 | +2% | +2% | +3% | +2% |
| `hex2bin()`, 32 hex characters | 182 | −52% | −53% | −48% | −55% |
| `hex2bin()`, 64 hex characters | 307 | −65% | −67% | −64% | −67% |
| `hex2bin()`, 512 hex characters | 1,985 | −80% | −77% | −83% | −83% |
| `hex2bin()`, 128 KB of hex | 473,088 | −84% | −79% | −89% | −87% |
| `md5()` of 32 bytes | 443 | −9% | −10% | −11% | −11% |
| `hash('sha256')` of 32 bytes | 440 | −14% | −12% | −17% | −12% |

All 37 cases, with the spread of the runs and the change in instructions: [full table](#full-table).

## Short `hex2bin()` inputs

Below 32 hex characters `hex2bin()` never reaches the SIMD loop, but it still executes 3–5% more instructions and takes 1–4% more cycles than master. The non-inlined call to `php_hex2bin_simd_chunk()` inside `zif_hex2bin()` makes every compiler save two more callee-saved registers (6 pushes instead of 4) and keep three values on the stack for the whole call, short inputs included. With `-falign-functions=64 -falign-loops=32` the same code costs 13–20% more cycles with clang 20.1 (+26 instructions and +20 cycles for 8 hex characters), so how much it shows depends on code placement.

`bin2hex()` has no such cost: `zend_bin2hex()` calls `zend_bin2hex_simd()` last, and that function finishes the tail itself. [`tail-variant.diff`](tail-variant.diff) gives `hex2bin()` the same shape — one non-inlined function runs the SIMD loop and the scalar tail, `php_hex2bin()` calls it only for 32 characters and more. Output identical to master; change in cycles relative to master:

| call | master, CPU cycles per call (GCC 13.3) | GCC 13.3 | GCC 14.2 | clang 18.1 | clang 20.1 | instructions |
|---|--:|--:|--:|--:|--:|--:|
| `hex2bin()`, 8 hex characters | 94 | +2% (+1 … +5) | +2% (+1 … +3) | +1% (−1 … +7) | 0% (−1 … +2) | +1% … +2% |
| `hex2bin()`, 16 hex characters | 122 | +1% (0 … +8) | +2% (+2 … +2) | −1% (−1 … 0) | −2% (−2 … +2) | +1% … +2% |
| `hex2bin()`, 30 hex characters | 172 | +3% (−1 … +6) | 0% (−1 … +4) | −1% (−1 … +71) | 0% (0 … +1) | +1% |
| `hex2bin()`, 32 hex characters | 178 | −51% (−51 … −50) | −52% (−53 … −49) | −48% (−48 … −46) | −53% (−53 … −53) | −55% … −49% |
| `hex2bin()`, 40 hex characters | 207 | −44% (−44 … −43) | −44% (−45 … −44) | −40% (−41 … −40) | −43% (−44 … −43) | −47% … −42% |
| `hex2bin()`, 62 hex characters | 297 | −34% (−34 … −27) | −39% (−39 … −37) | −30% (−30 … −29) | −34% (−34 … −25) | −34% … −29% |
| `hex2bin()`, 64 hex characters | 310 | −65% (−65 … −64) | −66% (−66 … −66) | −63% (−64 … −61) | −67% (−67 … −66) | −68% … −61% |
| `hex2bin()`, 66 hex characters | 320 | −65% (−65 … −61) | −65% (−65 … −65) | −61% (−61 … −60) | −64% (−64 … −64) | −66% … −60% |
| `hex2bin()`, 96 hex characters | 435 | −70% (−70 … −69) | −71% (−71 … −71) | −70% (−71 … −70) | −72% (−72 … −72) | −74% … −66% |
| `hex2bin()`, 128 hex characters | 550 | −73% (−74 … −72) | −73% (−73 … −73) | −73% (−73 … −73) | −75% (−75 … −75) | −77% … −69% |
| `hex2bin()`, 200 hex characters | 806 | −74% (−74 … −73) | −72% (−72 … −72) | −74% (−75 … −74) | −75% (−76 … −75) | −77% … −69% |
| `hex2bin()`, 512 hex characters | 1,946 | −80% (−82 … −80) | −76% (−77 … −76) | −82% (−83 … −82) | −83% (−83 … −82) | −85% … −76% |
| `hex2bin()`, 2,048 hex characters | 7,423 | −83% (−87 … −83) | −80% (−80 … −79) | −86% (−86 … −85) | −86% (−87 … −85) | −87% … −78% |
| `hex2bin()`, 128 KB of hex | 469,634 | −84% (−84 … −83) | −79% (−79 … −78) | −88% (−88 … −87) | −87% (−87 … −86) | −88% … −79% |
| `hex2bin()`, 64 hex characters, upper case | 311 | −65% (−65 … −57) | −67% (−67 … −66) | −62% (−63 … −62) | −67% (−67 … −66) | −68% … −61% |
| `hex2bin()`, 64 hex characters, mixed case | 313 | −65% (−65 … −65) | −66% (−67 … −66) | −63% (−63 … −63) | −67% (−67 … −56) | −68% … −61% |
| `hex2bin()`, 2,048 hex characters, mixed case | 7,422 | −83% (−83 … −82) | −80% (−80 … −79) | −86% (−101 … −83) | −86% (−86 … −82) | −87% … −78% |
| `hex2bin()`, 64 characters, one invalid | 1,168 | +1% (0 … +5) | +1% (0 … +2) | −1% (−2 … +1) | −1% (−2 … 0) | −4% … −3% |
| `hex2bin()`, 2,048 characters, one invalid | 4,841 | −63% (−64 … −63) | −61% (−62 … −61) | −64% (−64 … −62) | −62% (−62 … −61) | −72% … −66% |

The short inputs are within 2% of master's instructions and 3% of its cycles, the long ones keep the gains of the PR.

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

## Method

- Machine: Intel i7-13700H, P-core CPU 2, governor `powersave`, turbo on, kernel 7.0.0-34. Compilers GCC 13.3.0, GCC 14.2.0, clang 18.1.3, clang 20.1.2.
- Builds: `bench build` with the flags of the official Docker image plus `-g`: `BENCH_CFLAGS='-fstack-protector-strong -fpic -fpie -O2 -g -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64'`, `LDFLAGS='-Wl,-O1 -pie'`, `--enable-werror`.
- Metric: CPU cycles and instructions per call from `perf stat`, N calls minus the same process with 0 calls, divided by N ([`pairs-run.sh`](pairs-run.sh), cases in [`cases.php`](cases.php)). Five runs per case, master and the PR alternating (A B, B A, …); the value is the median over runs of the PR's cycles divided by master's, written as a change in percent.
- Inputs: short ones come from a pool of 256 random strings of the same length (fixed seed), so that the branch predictor does not see one string repeated.
- Control: master against master in the same series, −2 … +2% over all 37 cases. One sample is negative (`c18t change hex2bin-mixed-1024`, −104 cycles: the 0-call process took longer than the N-call one); it is one run of five and does not move the median.
- Raw data: [`intel-docker-20261014.txt`](intel-docker-20261014.txt). Tables: [`speedup-table.py`](speedup-table.py) with the row labels in [`rows-review.txt`](rows-review.txt) and [`rows-full.txt`](rows-full.txt).

## Full table

Change in CPU cycles per call relative to master (negative = fewer cycles, faster), median of five runs, in brackets the lowest and the highest run; last column: change in instructions, lowest and highest over the four compilers.

| call | master, CPU cycles per call (GCC 13.3) | GCC 13.3 | GCC 14.2 | clang 18.1 | clang 20.1 | instructions |
|---|--:|--:|--:|--:|--:|--:|
| `bin2hex()`, 4 bytes | 73 | +5% (+4 … +7) | +1% (+1 … +3) | +1% (−1 … +6) | +1% (0 … +1) | 0% … +3% |
| `bin2hex()`, 8 bytes | 82 | +4% (+2 … +6) | +1% (0 … +1) | 0% (0 … +2) | +3% (+2 … +4) | 0% … +2% |
| `bin2hex()`, 15 bytes | 95 | +6% (+4 … +11) | −1% (−2 … +49) | +13% (0 … +25) | +2% (+1 … +3) | 0% … +2% |
| `bin2hex()`, 16 bytes | 97 | −25% (−26 … −21) | −27% (−27 … −21) | −22% (−22 … −22) | −31% (−31 … −30) | −27% … −23% |
| `bin2hex()`, 20 bytes | 105 | −20% (−23 … −17) | −22% (−22 … −20) | −21% (−22 … −20) | −27% (−27 … −26) | −23% … −21% |
| `bin2hex()`, 31 bytes | 127 | −17% (−17 … −8) | −16% (−19 … −11) | −17% (−19 … −16) | −18% (−18 … −18) | −19% … −16% |
| `bin2hex()`, 32 bytes | 129 | −41% (−42 … −40) | −36% (−41 … −31) | −37% (−39 … −35) | −44% (−45 … −44) | −43% … −37% |
| `bin2hex()`, 33 bytes | 129 | −39% (−40 … −39) | −38% (−40 … −38) | −31% (−35 … −17) | −46% (−47 … −46) | −41% … −36% |
| `bin2hex()`, 48 bytes | 158 | −49% (−49 … −49) | −49% (−51 … −47) | −41% (−42 … −40) | −51% (−51 … −50) | −52% … −46% |
| `bin2hex()`, 64 bytes | 189 | −55% (−56 … −54) | −62% (−63 … −61) | −49% (−50 … −48) | −56% (−56 … −55) | −58% … −52% |
| `bin2hex()`, 100 bytes | 269 | −62% (−64 … −61) | −66% (−67 … −66) | −57% (−57 … −56) | −61% (−61 … −61) | −63% … −59% |
| `bin2hex()`, 256 bytes | 618 | −79% (−79 … −78) | −78% (−79 … −72) | −76% (−77 … −72) | −76% (−76 … −74) | −78% … −74% |
| `bin2hex()`, 1 KB | 2,204 | −84% (−84 … −83) | −84% (−84 … −83) | −83% (−83 … −81) | −84% (−84 … −83) | −85% … −83% |
| `bin2hex()`, 64 KB | 133,748 | −86% (−92 … −81) | −85% (−87 … −83) | −85% (−86 … −81) | −85% (−86 … −85) | −88% … −86% |
| `hex2bin()`, 8 hex characters | 94 | +4% (+3 … +7) | +2% (0 … +3) | +2% (+1 … +3) | +2% (+1 … +3) | +5% |
| `hex2bin()`, 16 hex characters | 124 | +2% (+1 … +2) | +2% (+2 … +4) | +3% (+1 … +4) | +2% (+2 … +4) | +4% … +5% |
| `hex2bin()`, 30 hex characters | 171 | +4% (+2 … +4) | +2% (−1 … +19) | +1% (0 … +3) | +2% (+1 … +2) | +3% … +5% |
| `hex2bin()`, 32 hex characters | 182 | −52% (−53 … −48) | −53% (−53 … −52) | −48% (−49 … −45) | −55% (−55 … −54) | −57% … −51% |
| `hex2bin()`, 40 hex characters | 210 | −45% (−46 … −44) | −47% (−48 … −46) | −42% (−44 … −42) | −45% (−45 … −44) | −48% … −43% |
| `hex2bin()`, 62 hex characters | 313 | −36% (−42 … −25) | −38% (−39 … −36) | −33% (−36 … −25) | −34% (−35 … −34) | −34% … −30% |
| `hex2bin()`, 64 hex characters | 307 | −65% (−65 … −62) | −67% (−67 … −66) | −64% (−65 … −58) | −67% (−68 … −67) | −69% … −63% |
| `hex2bin()`, 66 hex characters | 320 | −64% (−65 … −60) | −66% (−66 … −64) | −62% (−62 … −61) | −65% (−65 … −64) | −67% … −61% |
| `hex2bin()`, 96 hex characters | 430 | −71% (−72 … −70) | −72% (−72 … −71) | −71% (−72 … −71) | −72% (−73 … −72) | −75% … −67% |
| `hex2bin()`, 128 hex characters | 550 | −73% (−74 … −73) | −74% (−74 … −73) | −74% (−74 … −73) | −75% (−76 … −75) | −78% … −70% |
| `hex2bin()`, 200 hex characters | 834 | −74% (−75 … −73) | −73% (−75 … −71) | −75% (−75 … −74) | −75% (−76 … −75) | −78% … −70% |
| `hex2bin()`, 512 hex characters | 1,985 | −80% (−80 … −78) | −77% (−78 … −77) | −83% (−87 … −81) | −83% (−83 … −82) | −85% … −77% |
| `hex2bin()`, 2,048 hex characters | 7,527 | −83% (−83 … −77) | −79% (−80 … −78) | −87% (−87 … −87) | −86% (−86 … −86) | −87% … −79% |
| `hex2bin()`, 128 KB of hex | 473,088 | −84% (−85 … −82) | −79% (−80 … −77) | −89% (−89 … −88) | −87% (−88 … −87) | −88% … −79% |
| `hex2bin()`, 64 hex characters, upper case | 313 | −65% (−66 … −63) | −67% (−69 … −66) | −64% (−64 … −63) | −67% (−67 … −65) | −69% … −63% |
| `hex2bin()`, 64 hex characters, mixed case | 312 | −66% (−66 … −65) | −67% (−68 … −67) | −64% (−64 … −64) | −67% (−68 … −67) | −69% … −63% |
| `hex2bin()`, 2,048 hex characters, mixed case | 7,419 | −83% (−84 … −82) | −80% (−81 … −78) | −87% (−87 … −87) | −87% (−87 … −85) | −87% … −79% |
| `hex2bin()`, 64 characters, one invalid | 1,171 | −4% (−5 … −4) | +2% (0 … +2) | +3% (0 … +3) | 0% (0 … +28) | −5% … −3% |
| `hex2bin()`, 2,048 characters, one invalid | 4,812 | −63% (−64 … −62) | −60% (−60 … −58) | −62% (−63 … −62) | −61% (−72 … −52) | −72% … −66% |
| `md5()` of 32 bytes | 443 | −9% (−10 … −2) | −10% (−10 … −7) | −11% (−11 … −9) | −11% (−12 … −8) | −11% … −10% |
| `sha1()` of 32 bytes | 484 | −2% (−3 … +11) | −2% (−4 … +2) | −5% (−5 … −4) | −5% (−6 … −5) | −6% … −5% |
| `hash('xxh128')` of 32 bytes | 292 | −8% (−8 … −8) | −8% (−9 … −7) | −14% (−14 … −13) | −12% (−12 … −11) | −12% … −11% |
| `hash('sha256')` of 32 bytes | 440 | −14% (−14 … −11) | −12% (−12 … −11) | −17% (−17 … −17) | −12% (−13 … −7) | −18% … −17% |

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
mapfile -t ROWS < rows-full.txt
./speedup-table.py --full out.txt 'g13:GCC 13.3,g14:GCC 14.2,c18:clang 18.1,c20:clang 20.1' "${ROWS[@]}"
```
