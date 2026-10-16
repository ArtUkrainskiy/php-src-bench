# php-src-bench

[![tests](https://github.com/ArtUkrainskiy/php-src-bench/actions/workflows/ci.yml/badge.svg)](https://github.com/ArtUkrainskiy/php-src-bench/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

A/B micro-benchmarks for [php-src](https://github.com/php/php-src).

You changed a C function in PHP and want to know three things before opening a pull request:
is it faster than master, by how much, and is the output still the same. php-src-bench builds both
versions, runs the same PHP expressions on both and prints a table you can paste into the PR.

```
$ ./bench run htmlspecialchars --a base --b ascii-fast-path --perf
A: base — PHP 8.6.0-dev, 100e8f353ea ext/uri: Preserve empty query and fragment in URL builders
B: ascii-fast-path — PHP 8.6.0-dev, 0e4d8e73a21 ext/standard: Add a fast path for ASCII in htmlspecialchars()
CPU 2 (13th Gen Intel(R) Core(TM) i7-13700H), governor powersave, turbo on, kernel 7.0.0-34-generic
4 rounds × 7 samples × 10 ms, cc (Ubuntu 13.3.0-6ubuntu2~24.04.1) 13.3.0, configure --disable-all --disable-cgi --disable-phpdbg --enable-cli, CFLAGS -O2 -g -falign-functions=64 -falign-loops=32, 2026-10-05T21:18+00:00

case                                           bytes  A ns/op     ±  B ns/op     ±          B vs A  A instr/op  B instr/op  instr B vs A
htmlspecialchars @ empty                           0      6.6  4.6%      6.4  3.0%  1.03× faster ~         120         120         1.00×
htmlspecialchars @ word-8                          8     53.0  1.5%     32.8  0.8%  1.62× faster ✓         937         564   1.66× fewer
htmlspecialchars @ en-1k                        1042     4317  0.7%     1754  0.2%  2.46× faster ✓       63146       10027   6.30× fewer
htmlspecialchars @ en-64k                      65583   321682  0.4%   186046  0.5%  1.73× faster ✓     3946273      611834   6.45× fewer
htmlspecialchars @ html-page-4k                 4096    15277  1.4%     8210  0.3%  1.86× faster ✓      254920       69106   3.69× fewer
htmlspecialchars @ amp-1k                       1024     2402  0.3%     1722  0.5%  1.39× faster ✓       49264       35105   1.40× fewer
htmlspecialchars @ zh-64k                      65577   120665  0.4%   102448  0.4%  1.18× faster ✓     2420120     2047976   1.18× fewer
htmlspecialchars cp1251 @ cp1251-1k             1056     3391  1.7%     3437  1.6%  1.01× slower ~       62075       46134   1.35× fewer
htmlentities @ ru-1k                            1030     4550  1.0%     3539  0.6%  1.29× faster ✓       65113       55339   1.18× fewer
…
```

(An excerpt of a run made on 5 October 2026 with the alignment flags that are now
`--profile align`; numbers for a PR come from `bench compare`, below. The whole table and how it
was made are in
[reports/htmlspecialchars-ascii-fast-path](reports/htmlspecialchars-ascii-fast-path/).)

What it takes care of, so that you do not have to:

- **Two real builds.** A and B are separate release builds of two commits, with the same
  configure options and compiler flags. Nothing is patched into the binary under test.
- **Noise.** Each build is started four times, pinned to one core, in the order A B B A A B B A, so
  that drift hits both equally; one such process per build is a *round*. A row gets a ✓ or ✗ only
  when every round of B beat (or lost to) every round of A; everything else is `~`. Background
  load, frequency scaling, debug builds and builds made with different options are reported.
- **Instruction counts** (`--perf`), the metric php-src's own CI benchmark uses. They do not
  depend on how busy the machine is, and they expose wall-time differences that are only code
  placement.
- **Numbers for a pull request.** `bench compare` measures CPU cycles per call of the same change
  built with several compilers, with a master-against-master control, and `bench table` turns
  that into the Markdown table of "−25%" cells that goes into a PR comment.
- **Correctness.** For every case the value the expression returns is compared between A and B.
  `bench difftest` goes further and compares the builds on thousands of generated inputs, and
  `bench mutate` checks that those checks catch a wrong version of the change.
- **The cause of a difference.** `bench why` counts branch misses, cache misses and front-end
  stalls of both builds and shows where the functions sit, for a change in time without a change
  in work.
- **Someone else's pull request.** `bench pr <N>` fetches it, merges it onto master and builds
  both sides; `bench report` turns a series into a report directory a review can link to.
- **A record.** Each run is saved as JSON and can be rendered again as a terminal or Markdown table.

## Requirements

- Linux. Developed and used on x86-64 (Ubuntu 24.04, an Intel hybrid CPU); other systems are untested.
- A php-src checkout and what php-src needs to build: a C compiler, `make`, `autoconf`, `bison`,
  `re2c`, `pkg-config`.
- Some PHP 8.0+ in `PATH` (or `BENCH_PHP`) for the tool itself until the first build exists:
  `bench build` does not need it, `bench doctor`, `run` and the others do.
- git 2.38 or newer for `bench pr` (`git merge-tree --write-tree`).
- `git`, `taskset` (util-linux) for CPU pinning, `curl` for the real-document corpus.
- For `--perf`: the `perf` tool, hardware performance counters (most virtual machines have none)
  and permission to use them. Ubuntu forbids that by default; `sudo sysctl kernel.perf_event_paranoid=1`
  allows it until the next reboot. `./bench check` tells you whether instruction counts are available.

Ubuntu: `sudo apt install git curl build-essential autoconf bison re2c pkg-config linux-tools-common linux-tools-$(uname -r)`
(on Debian the perf package is `linux-perf`).

## Quick start

Clone this repository next to php-src:

```sh
git clone https://github.com/ArtUkrainskiy/php-src-bench.git
```

```
projects/
├── php-src/         your checkout, with your change on a branch or in the working tree
├── php-src-bench/   this repository
└── php-builds/      created by `bench build`: a git worktree per build, or only the binary (--slim)
```

Elsewhere, point `PHP_SRC` at the php-src checkout and `BENCH_BUILDS` at the directory for builds.

```sh
cd php-src-bench
./bench doctor                      # what this machine has and lacks (before the first build: PHP 8.0+ in PATH)
./bench build base "$(git -C ../php-src merge-base master HEAD)"   # the commit your branch starts from
./bench build dev .                 # your php-src working tree, as it is right now
corpus/real/fetch.sh                # once: real HTML, Markdown and JS used as inputs
./bench check                       # what on this machine will add noise?
./bench run html --a base --b dev --perf
```

Where `bench check` says that instruction counts are not available (most virtual machines, the
efficiency cores of a hybrid CPU), drop `--perf`; `bench compare` and `bench why` need those
counters and do not work there.

What to expect:

- **Time.** The first build of a name takes 1–6 minutes depending on the machine, later builds of
  the same name are incremental (seconds; a changed header rebuilds everything). A suite of 40 cases with `--perf` runs for about half a
  minute, a filtered `--quick` run for a second or two.
- **Your php-src checkout.** `bench build` does not touch its files, index or branches. It adds a
  git worktree per build (`git worktree list` shows them) and, for `.`, a commit object holding
  the snapshot, uncommitted and untracked files included. A build takes about 400 MB;
  `bench build --slim` keeps only the binary and its metadata (about 50 MB, no incremental
  rebuild). `./bench rm <name>` deletes a build, `./bench gc` lists them with size and age and
  removes the ones matching a pattern or `--older-than DAYS` with `--yes`. `bench build` refuses
  to start with less than 10 GB free (`BENCH_MIN_FREE_GB`).
- **Warnings.** On a laptop every run starts with warnings about the CPU governor and turbo
  boost. Those are advice: `sudo ./bench tune on` removes them until `tune off` or a reboot. The
  ones that make wall times unusable are a busy pinned CPU, a high load and, after the run, a
  spread above 5% or a disturbed round. Then wait, use `--wait-idle`, or rely on `--perf`, which
  load does not affect.

## Reading the result

| Column | Meaning |
|---|---|
| `case` | `<case> @ <input>`: the names of an expression and of an input in the suite file, e.g. `htmlspecialchars($s)` on 1 KB of English text |
| `bytes` | length of the input |
| `ns/op` | median time of one evaluation of the expression, loop overhead subtracted |
| `±` | how much the samples scatter around that median, in percent (a robust stand-in for the standard deviation: 1.4826·MAD/median) |
| `B vs A` | how many times B is faster or slower than A |
| `instr/op`, `instr B vs A` | instructions per evaluation, with `--perf` |

Marks in `B vs A`:

| Mark | Meaning |
|---|---|
| `✓` / `✗` | every round of B was faster / slower than every round of A, and the difference is at least 1% |
| `~` | the rounds of A and B overlap: no clear difference |
| `?` | fewer than 4 rounds (`--quick`): no verdict |
| `≈0` | both times are too close to zero to compare |
| `layout?` | the time changed but the instruction count did not: the amount of work is the same, so the cause is something else (code placement, cache or branch behaviour) and has to be found before the row is reported |
| `≠out` | A and B returned different results for this case |
| `≠in` | A and B got different inputs: the suite built them with a function that the change affects |

Markdown output (`--md`) uses ✅ and ❌ for the first two. The lines above the table say what A and
B are, which CPU the processes were pinned to, and how the run was done: `4 rounds × 7 samples ×
10 ms` is four processes per build, each taking seven timed samples of about 10 ms for every
case. A line starting with `!` means the comparison is not fair (a debug build, different
compiler or options).

When a row's spread is above a few percent, its wall time is noise: look at the instruction
counts. When both columns are clean and still disagree, neither is wrong: report both, and read
"Traps" in [docs/methodology.md](docs/methodology.md) before quoting the nicer one.

## From a change to a pull request

```sh
./bench build dev .                                         # after every edit, incremental
./bench run htmlspecialchars --a base --b dev --filter 'en-|html-' --quick   # iterate on a few cases
./bench run htmlspecialchars --a base --b dev --perf        # the full table, 4 rounds
./bench difftest html-encode base dev --count 20000         # same output on random inputs?
./bench show results/<file>.json --md                       # Markdown, while iterating
```

Every run prints `saved results/<date>-<time>-<suite>.json`; that is the file `bench show` takes.
`bench run` is for iterating; the numbers that go into a PR come from `bench compare` and
`bench table` (cycles per call, in percent, on several compilers), described below.
`--filter` matches case ids, which are the names in `suites/<suite>.php`. The tool does not
replace php-src's own tests: run them with the built binary before you send the change
(`cd ../php-builds/dev && sapi/cli/php run-tests.php -q -p "$PWD/sapi/cli/php" ext/standard/tests/strings`).

Results worth keeping, together with the commands that produced them, live in
[reports/](reports/), so that a PR can link to them.

## Reviewing someone else's pull request

```sh
./bench doctor                                   # once: what this machine has and lacks
export BENCH_CONFIGURE_EXTRA="--enable-mbstring --disable-mbregex"   # the PR changes mbstring
./bench pr 24080 --slim --cc gcc,clang-20        # fetch, merge onto master, build both sides
./bench difftest code pr24080-base-gcc13 pr24080-head-gcc13 --code 'mb_substr($s, 257, 300)' \
    --setup 'mb_check_encoding($s, "UTF-8")'
./bench compare --code 'mb_substr($s, 0, 10)' --inputs lang:title,lang:1k --setup 'mb_check_encoding($s, "UTF-8")' \
    gcc13=pr24080-base-gcc13:pr24080-head-gcc13 clang20=pr24080-base-clang20:pr24080-head-clang20
```

`bench pr` fetches the PR head and master from the remote of your php-src checkout that points at
php/php-src into `refs/bench/pr/<N>/`, merges them the way GitHub would (without touching your
working tree or branches; `git for-each-ref refs/bench` lists what it keeps) and builds
`pr<N>-base` and `pr<N>-head`; `--base REF` merges onto another commit, `--no-merge` builds the
head as it is, and a later run reuses the master it fetched unless `--update`. The builds have
only the extensions `BENCH_CONFIGURE_EXTRA` adds: the difference test stops when a function is
missing. That PR changes only strings marked as valid UTF-8, so `--setup` marks the input first;
without it the table would show the unchanged path. A series that was interrupted continues
with `bench compare --resume <series.json>`.

## Numbers for a pull request: several compilers

A change in a hot loop can measure differently with GCC and clang, because each compiler places
code differently. For the numbers you publish, build both sides with every compiler you have and
compare CPU cycles per call. With one compiler first:

```sh
./bench build --slim --cc gcc base "$(git -C ../php-src merge-base master HEAD)"   # -> base-gcc13
./bench build --slim --cc gcc dev .                                                # -> dev-gcc13
./bench compare htmlspecialchars gcc13=base-gcc13:dev-gcc13
```

For a single expression no suite file is needed: `--code 'mb_substr($s, 0, 10)' --inputs
lang:title,lang:1k` measures it on every language of the corpus, and `--setup` prepares each
input first (see [docs/suites.md](docs/suites.md)).

`bench build --cc` names a build `<name>-<compiler><major version>` (`bench builds` lists them);
a build that already exists at the same commit with the same configuration is kept, so a shared
`base` is built once. Suites that need an extension need it on both sides:
`BENCH_CONFIGURE_EXTRA="--enable-mbstring --disable-mbregex" ./bench build ...` (mbregex needs
oniguruma). With four compilers:

```sh
CCS=(--cc gcc,gcc-14,clang,clang-20)       # whatever compilers are installed
./bench build --slim "${CCS[@]}" base "$(git -C ../php-src merge-base master HEAD)"
./bench build --slim "${CCS[@]}" dev .
./bench compare htmlspecialchars gcc13=base-gcc13:dev-gcc13 gcc14=base-gcc14:dev-gcc14 \
    clang18=base-clang18:dev-clang18 clang20=base-clang20:dev-clang20
./bench table results/<date>-compare-htmlspecialchars.json --header --full
```

`bench compare` needs `perf` with access to hardware counters (`bench check` says whether it
works here) and, on a hybrid CPU, a performance core. Before measuring, every build runs every
case once: a case whose result differs between A and B of a group is marked `≠out`, and a group
whose builds differ in compiler, flags or configure options is reported. Then every case runs in
five passes that alternate A and B, on one CPU, with A of the first group against itself at the
start and the end of the series. Each pass of each side is two processes, the case for about
`--target-ms` (50 ms) and the empty loop, so a series takes roughly
(groups + 2) × cases × passes × 2 × 90 ms of measuring, plus one run of every build to check
results and calibrate; the 35 cases on four compilers below took 193 s of measuring. It needs
hardware counters: not in most virtual machines, and on a hybrid CPU only on a performance core.

`bench table` prints the change in cycles relative to A (`--labels FILE` sets the rows and their
names, `--base-name` what A is called, `--header` the machine, builds and method). For
[reports/pr-24080-mb-substr](reports/pr-24080-mb-substr/), `bench table compare-head.json
--labels labels-compare.txt` prints, among its 35 rows:

```
| call | master, CPU cycles per call (GCC 13.3) | GCC 13.3 | GCC 14.2 | clang 18.1 | clang 20.1 |
|---|--:|--:|--:|--:|--:|
| `mb_substr($s, 0, 10)`, English (1.00 B/char), 31-byte title | 188 | −33% | −21% | −48% | −49% |
| `mb_substr($s, $half, 20)`, English (1.00 B/char), 64 KB | 62,919 | −92% | −90% | −96% | −95% |
| `mb_substr($s, $half, 20)`, Hindi (2.54 B/char), 1 KB | 2,320 | −21% | −10% | −40% | −43% |
| `mb_substr($s, 0, 10)`, English (1.00 B/char), 31-byte title, without the flag | 189 | +4% | +4% | +1% | +1% |
```

Negative means fewer cycles, faster; say so above the table where you publish it. Under 20
cycles per call a cell shows `n/a` with the change in instructions; a cell whose change is not
larger than the A/A control of its row gets `~`, and `layout?` marks a change in cycles without
a change in instructions (see `bench why`). How it is measured:
[docs/methodology.md](docs/methodology.md).

## A report a pull request can link to

```sh
./bench report new reports/my-change --series results/<date>-compare-<suite>.json --labels labels.txt
# fill in the TODOs of reports/my-change/README.md
./bench report check reports/my-change     # before every commit
./bench report update reports/my-change    # after a new series: regenerate the tables
```

`new` writes a README with the sections a review needs (Summary, Results, Code, Tests,
Reproduce), the tables of the series and a Reproduce section made from what the series recorded
about its builds, and copies the series, its suite and the labels without the paths of your
machine. Tables live between `<!-- bench-table <series> [options] -->` and
`<!-- /bench-table -->` and are never typed by hand. `check` fails on paths of your machine
(including `~/...` spellings of the tool's directory), Cyrillic in Markdown, broken relative links
and anchors, tables that differ from their series, TODOs, and warns about builds of working-tree
snapshots that nobody else can check out. `update` also removes such paths from JSON files.

## Commands

| Command | |
|---|---|
| `bench build [--slim] [--profile P] [--cc LIST] [--no-werror] <name> [<ref>\|.]` | build a php-src ref (or `.`, the working tree) as `<name>`; `--slim`: binary only; `--profile docker` (default), `align`, `plain`, `asan`; `--cc gcc,clang-20`: one build per compiler |
| `bench pr <N> [--cc LIST] [--profile P] [--slim] [--no-werror] [--base REF] [--update] [--no-merge]` | fetch php-src PR N, merge it onto master, build both sides |
| `bench doctor` | what the machine has and lacks: tools, compilers, php-src, perf counters, disk, corpus, noise |
| `bench builds` | list builds |
| `bench rm <name>...` | delete builds |
| `bench gc [--older-than DAYS] [--yes] [<pattern>...]` | list builds with size and age; remove the matching ones with `--yes` |
| `bench suites` | list suites |
| `bench run <suite> --a <build> [--b <build>] [options]` | measure; `--code EXPR --inputs SPEC` instead of a suite; `bench run --help` lists the options |
| `bench compare <suite> <group>=<A>:<B>... [options]` | cycles and instructions per call for pairs of builds, one group per compiler; `--code` instead of a suite, `--resume` an interrupted series; `bench compare --help` |
| `bench table <series.json> [--full] [--labels FILE] [--header] [--bpc] [--base-name NAME]` | the change in cycles relative to A as a Markdown table |
| `bench report new\|update\|check <dir>` | a report directory from a series, its generated tables, the checks before committing it |
| `bench show <result.json> [--md]` | render a saved result again |
| `bench difftest <generator> <A> <B> [<C>...] [--seed N] [--count N]` | compare outputs of builds on generated inputs; `code --code EXPR` for any expression |
| `bench mutate <build> <mutations.php> [--only RE]` | put mistakes into the change one at a time and see whether the differential test and the tests catch them |
| `bench why <suite> <A> <B> --filter RE [--functions f,g]` (or `--code`) | branch misses, front-end stalls and function addresses of two builds, for a case whose cycles changed and instructions did not |
| `bench check [--cpu N]` | report noise sources on this machine and whether `--perf` can work |
| `bench tune on\|off\|status` | `on`: performance governor, no turbo boost; `off`: back to what it was (both need sudo) |
| `bench php` | print the php binary that runs the tool itself |

`--a` and `--b` take a build name or a path to any `php` binary. Options you will use most:
`--filter RE` (cases matching a regular expression), `--quick` (fast and rough), `--perf`
(instruction counts), `--wait-idle S` (wait for a quiet machine before each process, up to S
seconds in total; after that it measures anyway and says so), `--md`.

Builds are configured with `--disable-all --disable-cgi --disable-phpdbg --enable-cli` and, by
default, the compiler and linker flags of the official Docker image plus `-g` and
`--enable-werror` (`--profile docker`). `--profile align` adds fixed function and loop alignment
for finding out whether a difference is code placement, `plain` is `-O2 -g`, `asan` a debug build
with sanitizers; see the methodology notes. Add extensions with
`BENCH_CONFIGURE_EXTRA="--enable-mbstring --disable-mbregex" ./bench build ...`, change flags with `BENCH_CFLAGS`
and `BENCH_LDFLAGS` (an `LDFLAGS` from your shell is ignored, with a warning).

## Suites

A suite is a PHP file in `suites/` that returns inputs and expressions:

| Suite | |
|---|---|
| `html` | the four functions of `ext/standard/html.c` on small inputs and 1 KB of every language, a quick overview |
| `htmlspecialchars` | `htmlspecialchars()` and `htmlentities()`: short strings, titles, 1 KB and 64 KB of every language, markup, legacy charsets |
| `entities` | entity decoding with a growing share of entities, from none to entities only |
| `entity-period` | `html_entity_decode()` with one entity every N bytes |
| `realdata` | entity decoding on real HTML pages, Markdown and JavaScript |
| `json` | `json_encode()` and `json_decode()` of strings: 1 KB and 64 KB of every language, escaped and raw Unicode |

"Every language" is the nine of the corpus (`Corpus::LANGUAGES`: English, Spanish, Russian,
Arabic, Hindi, Chinese, Japanese, Korean, emoji in English), from 1.00 to 2.89 bytes per
character. Writing your own takes a few lines, see [docs/suites.md](docs/suites.md); for one
expression, `--code` and `--inputs` need no file.

## More

- [docs/methodology.md](docs/methodology.md): how it measures, why you can trust a ✓, and the
  traps that produce convincing but wrong numbers.
- [docs/suites.md](docs/suites.md): suites, inputs, the corpus, differential test generators.
- [reports/](reports/): published results.
- [AGENTS.md](AGENTS.md): instructions for AI coding agents that use or change this tool.
- [CONTRIBUTING.md](CONTRIBUTING.md): conventions and the self-tests (`tests/run.sh`).

## Limitations

- It measures one function call in a hot loop. That says nothing about cold caches or about what
  the change is worth for an application; for that, php-src has `benchmark/benchmark.php`
  (Symfony Demo, WordPress under callgrind).
- Everything runs under `php -n`: no opcache, no JIT. It is for C code behind PHP functions, not
  for changes to the VM, opcache or the JIT.
- Times of a few nanoseconds are mostly the remainder of subtracting the loop overhead: below
  about 10 ns per call, compare instruction counts.
- One machine and one set of flags give one code placement. Check a result on several compilers
  (`bench compare`) and, when a single compiler disagrees, with `--profile align`.
- Linux only: CPU pinning, noise detection and `perf` rely on `/proc`, `/sys` and `taskset`.
  Developed with GCC on x86-64; the PHP being measured must be 8.0 or newer.
- Suites so far cover string functions of `ext/standard` and `ext/json`. Others are easy to add.

## License

[MIT](LICENSE)
