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

- The input is `$s` in the expression. It can be any value, not only a string. Every case gets
  its own copy of it, so what one case does to a string (PHP marks a string as valid UTF-8 once a
  function has checked it, and keeps that mark) does not reach the next case.
- `'setup' => 'mb_check_encoding($s, "UTF-8")'` runs on that copy before the case is measured:
  for state the expression depends on but must not create itself. The example sets the
  valid-UTF-8 mark, which changes the path some mbstring functions take; a case without it
  measures an unmarked string. Setup may change `$s`; the `bytes` column shows the result.
- `'inputs'` of a case may contain patterns with `*` and `?`: `'*-1k'` is every input whose
  name ends in `-1k`.
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

Run a suite that is not in `suites/` by path: `bench run path/to/suite.php --a base`. For one
expression no file is needed:

```sh
./bench run --code 'mb_substr($s, 0, 10)' --inputs lang:title,lang:1k,en:64k \
    --setup 'mb_check_encoding($s, "UTF-8")' --a base --b dev
```

`--inputs` takes `lang:<size>` (every language below), `<corpus file>:<size>` (`en:64k`,
`html:4k`) and `:title` for the first line; sizes are bytes or `<n>k`. The suite is written to
`results/inline-<hash>.php`, which saved results point to. `bench compare` takes the same
options.

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
| `Corpus::languages($suffix, $bytes)` | `Corpus::text()` of every language in `Corpus::LANGUAGES`, named `<language>-<suffix>`; with `$bytes = 0` the first line (a title) |
| `Corpus::line($name, $index)` | one line of `corpus/<name>.txt` |
| `Corpus::entities($share, $bytes, $pool = 'mixed')` | English words mixed with HTML entities so that about `$share` of the bytes are entities; pools are listed in `Corpus::ENTITY_POOLS` |

Generated files, committed: `en`, `es`, `ru`, `ar`, `hi`, `zh`, `ja`, `ko`, `emoji`, `html`,
`entities` in UTF-8, and `ru-cp1251`, `ja-sjis`, `zh-big5`. The languages cover the main scripts and
UTF-8 widths (bytes per character in the files: en 1.00, es 1.03, emoji mix 1.42, ar 1.76, ru 1.77,
ko 2.25, hi 2.54, ja 2.88, zh 2.89); give each the same cases rather than favouring one, which
`Corpus::languages()` makes a one-liner:

```php
$lang1k = Corpus::languages('1k', 1024);
return [
    'inputs' => $lang1k + ['html-1k' => static fn (): string => Corpus::text('html', 1024)],
    'cases' => ['json_encode' => ['code' => 'json_encode($s)', 'inputs' => array_keys($lang1k)]],
];
```

`bench table --bpc` adds the bytes per character of each input to the row labels, for results
that depend on them. `corpus/generate.py` produces them deterministically, so
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

For expressions that take a string, no generator has to be written:

```sh
./bench difftest code base dev dev-asan --code 'mb_substr($s, 257, 300)' --code 'mb_strpos($s, "a", 300)' \
    --setup 'mb_check_encoding($s, "UTF-8")' --seed 1 --count 20000
```

`difftests/code.php` makes strings of 1- to 4-byte characters and combining sequences, 10% of
them with invalid sequences (`--input ascii` or `bytes` for other inputs), up to `--max`
characters (1100), half of the lengths on or next to 16, 32, 64, 256, 512 or 1024. Each `--code`
runs on a fresh copy of the input, and with `--setup` once more on a copy that went through the
setup; warnings and exceptions are part of the output. Every build after the first is compared
with the first.

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
| `code` | any `--code` expressions on generated UTF-8, ASCII or bytes, with and without `--setup` |
| `html-decode` | `html_entity_decode()`, `htmlspecialchars_decode()`: 10 flag sets × 12 charsets, valid, truncated and malformed entities, dense and long inputs |

Rules for a generator:

- Take all randomness from `$rng`, not from `mt_rand()`: inputs must be identical on both PHP
  versions being compared.
- Aim the inputs at the code you changed: lengths around block sizes, the boundary between a fast
  and a slow path, buffer growth, truncated sequences at the very end. `$rng->length($max,
  $boundaries)` lands on or next to the boundaries half of the time, `$rng->utf8($chars,
  $classes, $invalidPercent)` draws characters by UTF-8 width (`DIFFTEST_UTF8`).

For memory errors, run the same generator on a build with sanitizers:

```sh
./bench build --profile asan dev-asan .
USE_ZEND_ALLOC=0 ASAN_OPTIONS=detect_leaks=0 ./bench difftest html-encode base dev-asan --count 2000
```

`USE_ZEND_ALLOC=0` makes PHP use `malloc()` directly; without it the Zend allocator hides buffer
overflows from the sanitizer.

## Do the checks catch a wrong change?

A differential test that passes proves little until it has failed on a wrong version of the
code. `bench mutate` puts plausible mistakes into a full build of the change, one at a time,
rebuilds it and runs the checks:

```php
<?php // mutations.php
return [
    'difftest' => ['generator' => 'code', 'against' => 'base', 'args' => ['--code', 'mb_substr($s, 257, 300)', '--count', '2000']],
    'tests' => ['ext/mbstring/tests'],
    'mutations' => [
        'chunk loop runs down to offset 0' => ['file' => 'ext/mbstring/mbstring.c',
            'from' => 'while (offset > 256 && (size_t)(end - pos) >= 256) {',
            'to' => 'while (offset > 0 && (size_t)(end - pos) >= 256) {'],
    ],
];
```

```sh
./bench build dev .                       # a full build: run-tests.php needs the tree
./bench mutate dev mutations.php
```

It first runs the checks on the unchanged build (the differential test must agree with the
reference; tests that already fail are not counted), then prints a table of which check caught
which mutation. `from` must occur exactly once in its file; the build is restored at the end,
and a run that was interrupted is undone by the next one. Good mutations are the ones a reviewer
worries about: an off-by-one in a bound, a check left out, a condition widened.
