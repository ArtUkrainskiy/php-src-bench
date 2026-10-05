# Contributing

Suites for more functions, generators for differential tests, fixes and support for other
platforms are all welcome.

## Before you send a change

```sh
tests/run.sh
```

It checks syntax, the code that decides what a table says, the rendering of saved results against
`tests/expected/`, that every suite loads, that the committed corpus is what
`corpus/generate.py` produces, that bad suites and options are refused with a useful message,
the mismatch and crash paths of `bench difftest`, and does one tiny real run. It needs a PHP 8.0 or newer:
`BENCH_PHP=/path/to/php`, one of your builds, or `php` in `PATH`.

If you changed the table on purpose, run `tests/run.sh --update` and include the changed files
from `tests/expected/` in the commit.

## Conventions

- Code in `lib/`, suites and generators must run on PHP 8.0 built with `--disable-all`: no
  extensions beyond the always-enabled ones, no syntax newer than 8.0, no Composer.
- PHP: 4 spaces, plain functions, thresholds as named constants. Bash: tabs, `set -euo pipefail`.
- A suite starts with a one-line comment that says what it is for; `bench suites` prints it.
- Inputs must be deterministic. Generated text comes from `corpus/generate.py`, random inputs from
  a seeded generator of your own, not from `mt_rand()`.
- Do not commit `results/` or downloaded documents from `corpus/real/`. A result that others
  should be able to see goes to `reports/`, see [reports/README.md](reports/README.md).
- Changing how time is measured, or what the generated inputs are, changes every published
  number. Say so in the commit message.

## Adding a suite or a generator

See [docs/suites.md](docs/suites.md). If the function you measure needs an extension, say in
the suite's first comment which `BENCH_CONFIGURE_EXTRA` the builds need.
