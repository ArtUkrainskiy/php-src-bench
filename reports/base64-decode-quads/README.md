# base64_decode(): four characters at a time in the character loop

Status: open for a PR, not in any release.

php-src change: one commit on branch `base64-decode-quads` ("ext/standard: Decode base64 four
characters at a time in the character loop") on top of master
[`100e8f353ea`](https://github.com/php/php-src/commit/100e8f353ea). The commit is
`ext/standard/base64.c` plus an UPGRADING line and one new phpt; it ships here as `change.patch`
(the branch is not pushed yet, so there is no public commit link).

The vector decoders (SSSE3, AVX2, AVX-512, NEON) stop at the first 32-byte block that holds
anything but alphabet characters, and everything after that — as well as every input shorter
than 45 bytes — goes through the character loop in `php_base64_decode_impl()`: one character per
iteration, a `switch` on its position in the group. The change decodes whole groups of four
alphabet characters at once while the input is clean and keeps the one-character step for
whitespace, padding, invalid bytes and the last partial group. Output is unchanged.

## Summary

`base64_decode()` of short strings (tokens, keys, JWT parts) runs about 40–50% cheaper, and of
line-wrapped base64 (email, PEM) up to ~70% cheaper; large clean base64 is unchanged. Nothing
changes in user code — the function just gets faster once this ships.

Instructions per call are the headline: `perf stat`, deterministic, and the range spans six
compilers — GCC 13/14 and clang 18/20 on an Intel i7-13700H, GCC 15 and clang 21 on an AMD
Ryzen 9 5950X. The AMD cycles column (GCC 15 / clang 21, median of three paired passes on a
quiet host) is supporting; for the short inputs it is indicative, not exact — one decode is
cheap and the fixed input keeps the branch predictor warm. Negative = faster.

| `base64_decode()` input | instructions/call | AMD cycles |
|---|---:|---:|
| 24 B (a token) | −41…−46% | −38…−58% |
| 44 B (a 32-byte key) | −45…−50% | −45…−64% |
| 136 B | −47…−51% | −46…−63% |
| 1 KB, clean | −29…−31% | −22…−42% |
| 64 KB, clean | −1% (flat) | flat |
| 1 KB in 76-column lines (MIME) | −67…−70% | −63…−80% |
| 64 KB in 76-column lines (MIME) | −69…−71% | −64…−81% |
| 64 KB in 64-column lines (PEM) | −68…−71% | −64…−81% |
| 64 KB MIME, strict | −73…−76% | −68…−79% |

Clean input (no line breaks) is unchanged; the line-wrapped rows are a win only when a whole
wrapped blob is decoded in one `base64_decode()` call.

`base64_encode()` is not touched. Clean 64 KB barely moves (−1% instructions): the vector loop
does the bulk and only the ≤44-byte scalar tail reaches the changed character loop. The win is
on short input and on line-wrapped input.

Short input — a token, an id, a key — is under ~45 bytes and is decoded entirely by the
character loop, so it gets the win with no line breaks involved. The line-wrapped rows apply
when a whole wrapped blob is passed to `base64_decode()` in one call: it skips the line breaks
(even in strict mode) and runs the rest through this loop. Email base64 is wrapped at 76 columns (RFC 2045), PEM at 64. A parser
that strips the line breaks first keeps the input on the vector path and is unaffected. clang
gains the most, its old character loop was the slowest.

Raw data: `intel-instructions.txt` (per compiler, all cases), `amd-cycles.txt` (AMD cycles and
instructions); inputs built by `base64_cases.php`.

## Verification

- `./bench difftest base64 <base> <head>` seed 1, 30,000 inputs each, on all six compilers
  (GCC 13/14, clang 18/20, GCC 15, clang 21): clean base64, MIME and PEM lines, random line
  lengths, whitespace and invalid bytes anywhere, padding in every position, lengths around the
  group and vector block boundaries, both modes, plus `base64_encode()` of input and decoded
  bytes. Output identical to master. The snapshot tags `false` apart from `""`, so a strict-mode
  regression between the two would show.
- The check has teeth: against a deliberately broken build (the eligibility guard removed) the
  same differential reports a mismatch.
- With the decoder forced onto the SSSE3 and the generic path, 20,000 inputs: identical (run with
  a build that forces the scalar path; not scripted here).
- ASan + UBSan build of the change: 80,000 decodes (clean, MIME, malformed, both modes,
  `b64_asan.php`) run clean, no sanitizer report.
- `ext/standard/tests/url`, `.../strings/base64*`, `.../http`: pass; the new
  `base64_decode_whitespace.phpt` (a line break at every position of inputs up to 100 bytes, both
  modes) passes on master too.

## Reproduce

Run from a `php-src-bench` checkout (this report's repo): `./bench` is its A/B build wrapper and
ships the differential generator (`difftests/base64.php`) and `lib/`. `base` is master
`100e8f353ea`; `head` is that plus `change.patch` (one commit: `ext/standard/base64.c` + an
UPGRADING line + a new phpt). `$B` is the build directory (`~/php-builds` by default). Case names
map to the table by size: token24 = 24 B, key44 = 44 B, b136 = 136 B, clean1k/mime1k = 1 KB,
clean64k/mime64k/pem64k = 64 KB. Perf needs `kernel.perf_event_paranoid <= 1`; pin to an isolated
core (CPU 2 below — adjust to your topology) and use the performance governor.

Other compilers: `CC=clang ./bench build …`. Without `bench`, build each tree by hand with
`./configure --disable-all --disable-cgi --disable-phpdbg --enable-cli --enable-werror`,
`CFLAGS='-fstack-protector-strong -fpic -fpie -O2 -g -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64'`,
`LDFLAGS='-Wl,-O1 -pie'` (official Docker-image release flags) into `$B/b64-base` and
`$B/b64-head`; the differential still runs via this repo's `./bench difftest`, and the ASan check
is a build with `--enable-address-sanitizer --enable-undefined-sanitizer` running `b64_asan.php`.

```
B=~/php-builds

# 1. Build base (master) and head (master + change.patch).
./bench build b64-base 100e8f353ea
git -C <php-src> worktree add ../wt-b64 100e8f353ea && git -C ../wt-b64 apply "$(pwd)/change.patch"
PHP_SRC=<php-src>/../wt-b64 ./bench build b64-head .

# 2. Correctness: identical output, 30,000 inputs (difftests/base64.php ships in this repo).
./bench difftest base64 b64-base b64-head --seed 1 --count 30000

# 3. Instructions per call = perf over N decodes minus N=0, divided by N, for base and head.
#    (grep handles hybrid Intel: drop the "<not counted>" cpu_core/cpu_atom line.)
ins(){ taskset -c 2 perf stat -e instructions:u "$B/$1/sapi/cli/php" -n base64_cases.php "$2" "$3" "$4" 2>&1 \
         | grep -E 'instructions' | grep -vE '<not' | head -1 | tr -d , | awk '{print $1}'; }
for c in token24 key44 b136 clean1k clean64k mime1k mime64k pem64k; do
  for s in 0 1; do n=20000
    for v in base head; do
      echo "$c strict=$s $v $(( ($(ins b64-$v $c $n $s) - $(ins b64-$v $c 0 $s)) / n ))"
    done
  done
done

# 4. Cycles: the same subtraction with -e cycles:u, pinned, several paired passes, take the median
#    (amd-cycles.txt is GCC 15 / clang 21, three passes).

# 5. Memory safety: ASan + UBSan build, 80k decodes (clean / MIME / malformed, both modes).
PHP_SRC=<php-src>/../wt-b64 ./bench build --profile asan b64-head-asan .
USE_ZEND_ALLOC=0 "$B/b64-head-asan/sapi/cli/php" -n b64_asan.php   # prints "done <n>", no sanitizer output
```

`intel-instructions.txt` and `amd-cycles.txt` are the full runs behind the table (all cases,
each compiler).

## Why the vector loops were left alone

Resuming the vector loop after a line break instead of finishing in the character loop gives
another ~3× on MIME and PEM input; that is a separate change to every vector variant and comes
as a follow-up. Stripping whitespace first and decoding the rest as clean input was measured and
rejected: slower than resuming in place on MIME, and it needs a temporary buffer.
