# How php-src-bench measures, and where numbers lie

## The measurement

**Two binaries, one suite.** A and B are separate release builds made by `bench build` with
the same compiler, configure options and CFLAGS. `bench build` records them, and a result whose
two sides differ in any of them, or contain a debug build, says so in a line starting with `!`
above the table. For a binary that `bench build` did not make there is nothing to compare, which
is reported as well. The alternative of keeping an `_old()` copy of the function inside one
binary is not used: it changes the binary under test.

**No timer per call.** A case is a PHP expression such as `htmlspecialchars($s)`. The harness
(`lib/harness.php`, running inside the binary under test) compiles it into the body of a `for`
loop, calibrates the iteration count so that one sample takes `--target-ms` (10 ms), and times
whole loops with `hrtime()`. The same number of iterations of an empty loop is timed too and
subtracted, so `ns/op` is the cost of the expression alone.

**Interleaved rounds.** One process measures all cases of one side; a pair of processes, one per
side, is a round. There are four rounds by default (`--rounds`), in the order A B, B A, A B, B A,
so drift in temperature and frequency hits both sides equally. The iteration count calibrated by
the first process of a side is reused by its later rounds. The very first process of a run is
A's, and a first process tends to be a little slower (up to a few percent in its round); the
verdict rule below needs all rounds to agree, so this cannot produce a mark on its own.

**Pinning.** Every process is pinned with `taskset` to one CPU: a performance core on hybrid CPUs,
and not a sibling of CPU 0, which serves most interrupts. `--cpu N` overrides the choice.

**Statistics.** The reported time is the median of all samples of a side. `±` is
`1.4826·MAD/median`, a robust estimate of the relative standard deviation. A spread above 5% makes
the runner warn that wall times are unreliable.

**The verdict.** B gets `✓` (or `✗`) only if the median of *every* round of B is below (above) the
median of *every* round of A, and the difference is at least 1%. With 4 rounds per side, two
builds that do not differ separate this cleanly in at most 2 of 70 orderings, about 3% of cases;
measured on 251 cases of one build against itself it was 1 case. So an occasional false mark in a
large suite is expected, always with a tiny difference; a real effect shows up in a group of
related cases. With fewer than 4 rounds (`--quick`) no verdict is given, because clean separation
by chance is then too common.

`~` means that the rounds overlap, not that the builds are equal. One process disturbed by other
work on the machine is enough to turn a `✓` into `~`, and the spread `±` does not show it,
because it describes samples within the processes. The runner therefore reports cases where one
round of a build is more than 10% slower than another round of the same build; run those again.

**Instruction counts.** With `--perf` every case is also run a fixed number of times under
`perf stat`, counting user-space instructions, and the count of an empty loop of the same length
is subtracted. This is the metric of php-src's CI benchmark (which uses callgrind), and it does
not depend on load, so these runs are done in parallel on spare cores. `perf` itself is pinned
too: on hybrid CPUs a process that starts on an efficiency core leaves the P-core counter running
only part of the time, and a count scaled up from that is several percent off.

How exact they are: repeated runs of one binary agree to a few instructions per call, under
0.001%, and the values match callgrind (937 against 937.03, 63,144 against 63,145.6 instructions
per call for two cases of the htmlspecialchars suite). Two things other than the code under test
can still move a count by a fraction of a percent: where the allocator places blocks, which
depends on the length of paths and arguments (seen as 0.5–0.7% in cases that reallocate a lot),
and where the linker places constant data (up to 0.3% between two builds of the same commit in
different directories). Differences below about 0.5% in instruction counts are therefore not
evidence of anything.

**Output comparison.** In every process each case is evaluated once before it is timed, and the
value it returns is hashed, as is the input. If the hashes of A and B differ, the row is marked
`≠out`: the change altered behavior, and its timing is beside the point until that is explained.
This covers the return value of one call, not side effects. Two things would make it meaningless
and are caught: an expression that modifies its input is refused by the harness (the loop would
measure the modified input from the second iteration on), and a result that changes from process
to process is reported as not deterministic instead of as a difference between A and B.

**What the empty loop does not model.** Subtracting the empty loop removes the loop counter and
the branch exactly, in instructions. In time it removes slightly too much, because the empty loop
runs faster without a body than the same loop instructions do around one. The error is a
fraction of a nanosecond: times under about 10 ns per call read up to 10% low, above 50 ns the
effect on a ratio is under 1%. Rows where both times are under half a nanosecond are not compared
at all (`≈0`).

## Keeping the machine quiet

`bench check` reports what will add noise: a governor other than `performance`, turbo boost,
battery power, load average, other processes on the pinned core or its SMT sibling.
`sudo ./bench tune on` sets the performance governor and turns turbo off; `tune off` restores what
was there.

On a machine where builds or indexing start on their own, use `--wait-idle S`: before every
measured process the runner waits until no compiler is running, the load average is below 4 and
the pinned core is idle. S is the waiting budget of the whole run; when it is spent, the runner
says so and measures anyway. Instruction counts are not affected by load either way, which is the
main reason to always pass `--perf` for numbers you intend to publish.

## Why builds use `-falign-functions=64 -falign-loops=32`

With plain `-O2`, changing one function shifts the address of everything linked after it, and the
speed of untouched code changes with its alignment. In a calibration run for php-src commit
`e0c3f46496c`, which only touched `traverse_for_entities()`, `htmlspecialchars()` with
`double_encode: false` came out 3–15% slower in every round, with identical disassembly and
identical instruction counts: the function had moved by 240 bytes. With 64-byte function and
32-byte loop alignment the phantom regression disappeared (within ±1.2%), while the real changes
in `html_entity_decode()` measured the same. Binaries are about 5% larger.

These are not the flags distributions build PHP with. Absolute times differ slightly from a
stock build; what the flags protect is the comparison. To check a result under plain flags, build
both sides with `BENCH_CFLAGS="-O2 -g"`.

Alignment does not remove placement effects *inside* the function you changed. The `layout?` mark
points at rows where that may have happened: the time changed, the instruction count did not. The
mark does not prove that code placement is the cause. A change in memory access or branch
behaviour looks the same, so compare `objdump -d` of the function in both builds and
`perf stat -e branch-misses,cache-misses` before deciding what the row means.

## Traps

**The branch predictor memorizes short inputs.** A benchmark repeats the same input millions of
times. For a 1 KB string the predictor learns the outcome of data-dependent branches (is this
byte a space? does it need escaping?), which never happens in production, where every string is
new. Measured on `htmlspecialchars()` over English text: 0.2 branch misses per byte at 64 KB
in every build, 0.05 to 0.15 at 1 KB depending on the build. The effect can even invert a result: inlining a decoder cut instructions by
1.35× and made a 1 KB cp1251 input 1.2× *slower*, while 64 KB of the same text got 1.1× faster —
the old code layout happened to be easier to memorize. For byte loops, always include inputs of
64 KB or more next to the short ones, and look at `branch-misses` before believing a wall time:

```sh
# N: the CPU that `bench check` prints; <build>: the name you gave to `bench build`
taskset -c N perf stat -e cycles,instructions,branches,branch-misses \
    ../php-builds/<build>/sapi/cli/php -n lib/harness.php suites/htmlspecialchars.php \
    '{"mode":"fixed","case":"htmlspecialchars @ en-64k","n":3000,"empty":0}'
```

This runs the expression of one case exactly 3000 times and prints nothing; the header of
`lib/harness.php` describes the modes.

**Fewer instructions is not less time.** The byte loop of `htmlspecialchars()` went from 60 to 45
instructions per byte with no change in wall time, because it was limited by taken branches and
mispredictions, not by the number of instructions. Report both columns; when they disagree, say so.

**The same logic compiles differently.** In a large function, rewriting a condition in an
equivalent form, or adding one more live variable, can change register allocation of the whole
loop and move unrelated paths by several percent. Re-measure after every edit, including
"cosmetic" ones, and compare `objdump -d` when a rename seems to change performance.

**Wall time on a busy machine.** A compiler running on other cores still moves wall times by tens
of percent through shared caches, memory bandwidth and frequency limits. Pinning does not help.
Wait (`--wait-idle`) or rely on instruction counts.

**Debug builds.** A php-src tree configured with `--enable-debug` is several times slower and
has different hot spots. A result with such a side has `DEBUG` next to it and a `!` line above
the table; treat the whole run as void.

**Micro is not macro.** A function that is 3× faster matters only as much as the application
spends in it. `htmlspecialchars()` is 1.2% of a Symfony Demo request and 0.01% of a WordPress
request; the change in the example at the top of the README made Symfony Demo 0.87% cheaper in
instructions and left WordPress untouched. To learn where an application spends its time, use
`benchmark/benchmark.php` from php-src, which runs these applications under callgrind.

## What a result file contains

`results/<date>-<time>-<suite>.json` (not committed; date and time are UTC) keeps everything
needed to render the table again with `bench show`: the configuration of the run, the machine (CPU model, governor, turbo, load),
both builds (commit, configure options, CFLAGS, compiler) and, for every case and side, the raw
samples of every round, the empty-loop cost, iteration counts, input and output hashes and
instruction counts.
