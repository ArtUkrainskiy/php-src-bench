# Suites, inputs and differential tests

## A suite

`suites/<name>.php` returns the inputs and the cases. Every case runs on every input unless it
lists its own; the id of a measurement is `<case> @ <input>`, which is what `--filter` matches.

```php
<?php
// One line saying what this suite is for: `bench suites` prints it.

return [
    'inputs' => [
        'word-8' => 'abcdefgh',
        'en-1k' => static fn (): string => Corpus::text('en', 1024),
        'en-64k' => static fn (): string => Corpus::text('en', 65536),
        'amp-1k' => str_repeat('&', 1024),
    ],
    'cases' => [
        'html_entity_decode' => 'html_entity_decode($s)',
        'htmlspecialchars !double_encode' => [
            'code' => 'htmlspecialchars($s, ENT_QUOTES, null, false)',
            'inputs' => ['en-1k', 'amp-1k'],
        ],
    ],
];
```

- The input is `$s` in the expression. It can be any value, not only a string.
- An input given as a closure is built only when a selected case needs it.
- The expression is compiled into the measured loop as is, so keep it to the call you want to
  measure. Its result is hashed once to compare A with B; it is not stored during the loop.
- The expression must not modify `$s` (the loop reuses it) and must return the same value every
  time; the harness refuses the first and the result reports the second.
- Do not build an input with the function you are measuring: if the change affects it, A and B
  get different inputs and the row is marked `≠in`.
- A warning or notice raised by the expression fails the run, with the case named.
- The number in an input name is its nominal size. Inputs made with `Corpus::text()` consist of
  whole lines and are a little longer; the `bytes` column of the result is exact.
- Suites run on both binaries under `php -n`, including builds made with `--disable-all`: use
  only what such a build has, or build with `BENCH_CONFIGURE_EXTRA`.

Run a suite that is not in `suites/` by path: `bench run path/to/suite.php --a base`.

## Choosing inputs

- **Sizes the function really sees.** For `htmlspecialchars()` that is 8–40 bytes from templates
  far more often than a whole page. Per-call overhead dominates there.
- **64 KB next to 1 KB.** The branch predictor memorizes a short input that is repeated in a loop;
  see the traps in [methodology.md](methodology.md).
- **The worst case of the new code**, not only the best: if a fast path handles runs of plain
  bytes, measure inputs made of the bytes it cannot handle.
- **Paths you did not mean to touch**: other flags, other charsets, the sibling function that
  shares the loop. A table without a single `~` row has probably not looked for regressions.
- **Real documents.** Generated text has no realistic mix of markup and punctuation.

## The corpus

`Corpus` (`lib/Corpus.php`) builds inputs from the text files in `corpus/`:

| Call | Result |
|---|---|
| `Corpus::text($name, $bytes)` | whole lines of `corpus/<name>.txt`, repeated until at least `$bytes` long; never cuts a multibyte sequence |
| `Corpus::slice($name, $bytes)` | exactly `$bytes` bytes of the file; for files without useful lines, such as minified code |
| `Corpus::entities($share, $bytes, $pool = 'mixed')` | English words mixed with HTML entities so that about `$share` of the bytes are entities; pools are listed in `Corpus::ENTITY_POOLS` |

Generated files, committed: `en`, `html`, `entities`, `ru`, `zh`, `ja`, `emoji` in UTF-8, and
`ru-cp1251`, `ja-sjis`, `zh-big5`. `corpus/generate.py` produces them deterministically, so
everybody measures the same bytes; `tests/run.sh` checks that.

Real documents (`real/<name>`) are downloaded by `corpus/real/fetch.sh` and not committed, see
[corpus/real/README.md](../corpus/real/README.md). A suite skips inputs whose file is missing and
tells you to run the script.

## Differential tests

A benchmark compares outputs on a few dozen inputs. Before claiming "the output does not change",
compare the two builds on thousands of generated ones:

```sh
./bench difftest html-encode base dev --seed 1 --count 20000
```

A generator is a PHP script in `difftests/` with two functions and one call:

```php
<?php
require dirname(__DIR__) . '/lib/difftest.php';

function generate(DifftestRng $rng): string        // one input, built from $rng only
{
    return str_repeat($rng->pick(['&', 'a', '<']), $rng->next(100));
}

function outputs(string $input): Generator          // everything the functions under test make of it
{
    foreach ([ENT_QUOTES, ENT_NOQUOTES] as $flags) {
        yield "htmlspecialchars $flags" => htmlspecialchars($input, $flags);
    }
}

difftest_run($argv, 'generate', 'outputs');
```

`difftest_run()` prints one line per generated input, `<index>\t<hash of all outputs>`, and
handles `--seed N`, `--count N` and `--dump INDEX` (print that input and every output in hex).
`bench difftest` runs the script with both binaries and compares the lines. On a mismatch it
prints how many inputs differ, the first of them and which of its outputs differ; a binary that
crashes or aborts under a sanitizer is reported with its exit status.

| Generator | Covers |
|---|---|
| `html-encode` | `htmlspecialchars()`, `htmlentities()`: 13 flag sets × 14 charsets × `double_encode` on/off, inputs mixing plain runs, special characters, valid and broken multibyte sequences, entities |
| `html-decode` | `html_entity_decode()`, `htmlspecialchars_decode()`: 10 flag sets × 12 charsets, valid, truncated and malformed entities, dense and long inputs |

Rules for a generator:

- Take all randomness from `$rng`, not from `mt_rand()`: inputs must be identical on both PHP
  versions being compared.
- Aim the inputs at the code you changed: lengths around block sizes, the boundary between a fast
  and a slow path, buffer growth, truncated sequences at the very end.

For memory errors, run the same generator on a build with sanitizers:

```sh
BENCH_CONFIGURE_EXTRA="--enable-debug --enable-address-sanitizer --enable-undefined-sanitizer" \
BENCH_CFLAGS="-O1 -g -fno-omit-frame-pointer" ./bench build dev-asan .
USE_ZEND_ALLOC=0 ASAN_OPTIONS=detect_leaks=0 ./bench difftest html-encode base dev-asan --count 2000
```

`USE_ZEND_ALLOC=0` makes PHP use `malloc()` directly; without it the Zend allocator hides buffer
overflows from the sanitizer.
