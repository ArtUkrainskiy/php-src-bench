# php-src-bench

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

(An excerpt; the whole table and how it was made are in
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
- **Correctness.** For every case the value the expression returns is compared between A and B.
  `bench difftest` goes further and compares the two builds on thousands of generated inputs.
- **A record.** Each run is saved as JSON and can be rendered again as a terminal or Markdown table.

## Requirements

- Linux. Developed and used on x86-64 (Ubuntu 24.04, an Intel hybrid CPU); other systems are untested.
- A php-src checkout and what php-src needs to build: a C compiler, `make`, `autoconf`, `bison`,
  `re2c`, `pkg-config`.
- `git`, `taskset` (util-linux) for CPU pinning, `curl` for the real-document corpus.
- For `--perf`: the `perf` tool, hardware performance counters (most virtual machines have none)
  and permission to use them. Ubuntu forbids that by default; `sudo sysctl kernel.perf_event_paranoid=1`
  allows it until the next reboot. `./bench check` tells you whether instruction counts are available.

Ubuntu: `sudo apt install git curl build-essential autoconf bison re2c pkg-config linux-tools-common linux-tools-$(uname -r)`
(on Debian the perf package is `linux-perf`).

## Quick start

Clone this repository next to php-src (or point `PHP_SRC` at your checkout):

```
projects/
├── php-src/       your checkout, with your change on a branch or in the working tree
├── php-src-bench/     this repository
└── php-builds/    created by `bench build`, one git worktree per build
```

```sh
cd php-src-bench
./bench build base "$(git -C ../php-src merge-base master HEAD)"   # the commit your branch starts from
./bench build dev .                 # your php-src working tree, as it is right now
corpus/real/fetch.sh                # once: real HTML, Markdown and JS used as inputs
./bench check                       # what on this machine will add noise?
./bench run html --a base --b dev --perf
```

What to expect:

- **Time.** The first build of a name takes 1–6 minutes depending on the machine, later builds of
  the same name are incremental (seconds). A suite of 40 cases with `--perf` runs for about half a
  minute, a filtered `--quick` run for a second or two.
- **Your php-src checkout.** `bench build` does not touch its files, index or branches. It adds a
  git worktree per build (`git worktree list` shows them) and, for `.`, a commit object holding
  the snapshot, uncommitted and untracked files included. A build takes about 370 MB;
  `./bench rm <name>` deletes one.
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
./bench show results/<file>.json --md                       # Markdown for the PR description
```

Every run prints `saved results/<date>-<time>-<suite>.json`; that is the file `bench show` takes.
`--filter` matches case ids, which are the names in `suites/<suite>.php`. The tool does not
replace php-src's own tests: run them with the built binary before you send the change
(`cd ../php-builds/dev && sapi/cli/php run-tests.php -q -p "$PWD/sapi/cli/php" ext/standard/tests/strings`).

Results worth keeping, together with the commands that produced them, live in
[reports/](reports/), so that a PR can link to them.

## Commands

| Command | |
|---|---|
| `bench build <name> [<ref>\|.]` | build a php-src ref (or `.`, the working tree) as `<name>` |
| `bench builds` | list builds |
| `bench rm <name>` | delete a build |
| `bench suites` | list suites |
| `bench run <suite> --a <build> [--b <build>] [options]` | measure; `bench run --help` lists the options |
| `bench show <result.json> [--md]` | render a saved result again |
| `bench difftest <generator> <A> <B> [--seed N] [--count N]` | compare outputs of two builds on generated inputs |
| `bench check [--cpu N]` | report noise sources on this machine and whether `--perf` can work |
| `bench tune on\|off\|status` | `on`: performance governor, no turbo boost; `off`: back to what it was (both need sudo) |

`--a` and `--b` take a build name or a path to any `php` binary. Options you will use most:
`--filter RE` (cases matching a regular expression), `--quick` (fast and rough), `--perf`
(instruction counts), `--wait-idle S` (wait for a quiet machine before each process, up to S
seconds in total; after that it measures anyway and says so), `--md`.

Builds are configured with `--disable-all --disable-cgi --disable-phpdbg --enable-cli` and
`CFLAGS="-O2 -g -falign-functions=64 -falign-loops=32"`. Add extensions with
`BENCH_CONFIGURE_EXTRA="--enable-mbstring" ./bench build ...`, change flags with `BENCH_CFLAGS`.
Why the alignment flags are there is explained in the methodology notes.

## Suites

A suite is a PHP file in `suites/` that returns inputs and expressions:

| Suite | |
|---|---|
| `html` | the four functions of `ext/standard/html.c` on small inputs, a quick overview |
| `htmlspecialchars` | `htmlspecialchars()` and `htmlentities()`: short strings, text, markup, non-Latin scripts, legacy charsets |
| `entities` | entity decoding with a growing share of entities, from none to entities only |
| `entity-period` | `html_entity_decode()` with one entity every N bytes |
| `realdata` | entity decoding on real HTML pages, Markdown and JavaScript |
| `json` | `json_encode()` and `json_decode()` of strings |

Writing your own takes a few lines, see [docs/suites.md](docs/suites.md).

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
- The builds use alignment flags that distributions do not use (see the methodology notes); to
  check a result under plain flags, build both sides with `BENCH_CFLAGS="-O2 -g"`.
- Linux only: CPU pinning, noise detection and `perf` rely on `/proc`, `/sys` and `taskset`.
  Developed with GCC on x86-64; the PHP being measured must be 8.0 or newer.
- Suites so far cover string functions of `ext/standard` and `ext/json`. Others are easy to add.

## License

[MIT](LICENSE)
