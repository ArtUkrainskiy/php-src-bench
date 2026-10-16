<?php
/*
 * `bench compare` and `bench table`: a series of CPU cycles and instructions per call for pairs
 * of builds (A = the reference, B = the change), one pair per group, usually one group per
 * compiler, and the table of the change in cycles relative to A that goes into PR comments.
 *
 * Each count is `perf stat -e cycles,instructions` over a harness process that runs one case a
 * fixed number of times, minus the same process running the empty loop as many times: what is
 * left is the cost of the expression alone, with start-up and loop overhead cancelled. All
 * processes run one after another on one CPU, in passes that alternate the order of A and B.
 * Unless --no-control is given, the series starts and ends with A of the first group against
 * itself (groups "aa" and "aa2"): the spread of that control is the noise floor of the series.
 *
 * A series (format 1), saved after every case so that an interrupted one still has its data:
 *   format, kind ("compare"), date, suite, elapsed_s, complete
 *   config   passes, cpu, target_ms, filter, control
 *   env      the machine, see system_info()
 *   groups   list of {name, a, b}, in the order measured
 *   builds   by name: {php, build (.bench-build.json or null), info}
 *   cases    by case id: {input_len, n (iterations per count)}
 *   rows     list of [group, "a"|"b", case id, cycles per call, instructions per call]
 */
declare(strict_types=1);

const SERIES_FORMAT = 1;

function usage_compare(): void
{
    echo <<<'USAGE'
    Usage: bench compare <suite> <group>=<A>:<B> [<group>=<A>:<B> ...] [options]

      <group>=<A>:<B>  a pair of builds (names in $BENCH_BUILDS or paths to php binaries);
                       usually one group per compiler, e.g. gcc13=base-gcc13:pr-gcc13
      --passes N       alternating passes per case and group (default 5)
      --target-ms MS   duration of one counted process of the reference (default 50)
      --filter RE      only cases whose id ("name @ input") matches RE
      --cpu N          pin every process to this CPU (default: a P-core that is not CPU 0's sibling)
      --wait-idle S    wait for a quiet machine before each process, as in `bench run`
      --no-control     no A-against-A control at the start and the end
      --out FILE       where to save the series (default: results/<date>-compare-<suite>.json)

    Then: bench table <series.json> [--full] [--labels FILE] [--base-name NAME]

    USAGE;
}

function usage_table(): void
{
    echo <<<'USAGE'
    Usage: bench table <series.json> [--full] [--labels FILE] [--base-name NAME]

      Markdown table of the change in CPU cycles per call relative to A, one column per group;
      the control groups follow in a table of their own. Say "negative = fewer cycles (faster)"
      above the table where you publish it.
      --full         add the range over the passes to each cell and a column with the change
                     in instructions (for reports)
      --labels FILE  rows to show and their labels, one "<case id>=<label>" per line, in order
                     (default: every case, labelled by its id)
      --base-name N  what A is called in the second column (default: master)

    USAGE;
}

function cmd_compare(array $positional, array $options): int
{
    if (isset($options['help']) || count($positional) < 2) {
        usage_compare();
        return isset($options['help']) ? 0 : 2;
    }
    $suite = resolve_suite(array_shift($positional));
    $groups = [];
    $builds = [];
    foreach ($positional as $spec) {
        if (!preg_match('/^([A-Za-z0-9._-]+)=([^:]+):([^:]+)$/', $spec, $m)) {
            throw new BenchError("a group is <name>=<A>:<B>, got: $spec");
        }
        if (in_array($m[1], ['aa', 'aa2'], true) || isset($groups[$m[1]])) {
            throw new BenchError("group name '$m[1]' is reserved or used twice");
        }
        $groups[$m[1]] = ['name' => $m[1], 'a' => $m[2], 'b' => $m[3]];
        foreach ([$m[2], $m[3]] as $b) {
            $builds[$b] ??= resolve_side($b);
        }
    }
    $config = [
        'passes' => int_option($options, 'passes', 5),
        'cpu' => cpu_option($options),
        'target_ms' => float_option($options, 'target-ms', 50.0),
        'filter' => isset($options['filter']) ? (string) $options['filter'] : null,
        'control' => !isset($options['no-control']),
        'wait_idle' => int_option($options, 'wait-idle', 0),
    ];
    if ($config['passes'] < 1 || $config['target_ms'] <= 0) {
        throw new BenchError('--passes must be at least 1 and --target-ms positive');
    }
    $first = reset($groups);
    $order = array_values($groups);
    if ($config['control']) {
        array_unshift($order, ['name' => 'aa', 'a' => $first['a'], 'b' => $first['a']]);
        $order[] = ['name' => 'aa2', 'a' => $first['a'], 'b' => $first['a']];
    }

    $lock = lock_cpu($config['cpu']);
    $env = system_info($config['cpu']);
    [$perf, $events] = perf_cycles_probe($config['cpu']);

    // Which cases every build can run, and their input lengths.
    $lengths = null;
    foreach ($builds as $name => $side) {
        $list = harness($side['php'], $suite, ['mode' => 'list', 'filter' => $config['filter']], $config['cpu']);
        $builds[$name]['info'] = $list['php'];
        $ids = array_column($list['cases'], 'input_len', 'id');
        $lengths = $lengths === null ? $ids : array_intersect_key($lengths, $ids);
    }
    if (!$lengths) {
        throw new BenchError('no cases match');
    }
    foreach (check_machine($env) as $warning) {
        warn($warning);
    }

    // Iterations per case: enough for the reference to run about target_ms, the same for every build.
    progress('calibrating on ' . $first['a']);
    $timing = harness($builds[$first['a']]['php'], $suite, ['mode' => 'run', 'samples' => 3, 'target_ms' => 5, 'warmup_ms' => 2, 'filter' => $config['filter'], 'known_n' => []], $config['cpu']);
    $cases = [];
    foreach ($timing['cases'] as $c) {
        if (isset($lengths[$c['id']])) {
            $ns = max(1.0, median($c['samples_ns']) - $c['loop_ns']);
            $cases[$c['id']] = ['input_len' => $lengths[$c['id']], 'n' => max(20, (int) ($config['target_ms'] * 1e6 / $ns))];
        }
    }

    $file = $options['out'] ?? sprintf('%s/results/%s-compare-%s.json', BENCH_ROOT, date('Ymd-His'), basename($suite, '.php'));
    $series = [
        'format' => SERIES_FORMAT,
        'kind' => 'compare',
        'date' => date('c'),
        'suite' => $suite,
        'elapsed_s' => 0,
        'complete' => false,
        'config' => $config,
        'env' => $env,
        'groups' => $order,
        'builds' => array_map(static fn (array $s): array => ['php' => $s['php'], 'build' => $s['build'], 'info' => $s['info']], $builds),
        'cases' => $cases,
        'rows' => [],
    ];

    $started = microtime(true);
    $total = count($order) * count($cases) * $config['passes'] * 2;
    $done = 0;
    foreach ($order as $g) {
        foreach ($cases as $id => $case) {
            for ($pass = 1; $pass <= $config['passes']; $pass++) {
                foreach ($pass % 2 ? ['a', 'b'] : ['b', 'a'] as $side) {
                    $eta = $done ? (microtime(true) - $started) / $done * ($total - $done) : 0;
                    progress(sprintf('%s %s, pass %d/%d, %s  [%d/%d%s]', $g['name'], $id, $pass, $config['passes'], $side, $done + 1, $total,
                        $done ? sprintf(', ~%d min left', (int) ceil($eta / 60)) : ''));
                    wait_idle($config, $id);
                    $php = $builds[$g[$side]]['php'];
                    $body = perf_cycles($perf, $events, $php, $suite, $id, $case['n'], false, $config['cpu']);
                    $empty = perf_cycles($perf, $events, $php, $suite, $id, $case['n'], true, $config['cpu']);
                    $series['rows'][] = [$g['name'], $side, $id,
                        (int) round(($body[0] - $empty[0]) / $case['n']), (int) round(($body[1] - $empty[1]) / $case['n'])];
                    $done++;
                }
            }
            $series['elapsed_s'] = round(microtime(true) - $started, 1);
            save_series($file, $series);
        }
    }
    progress('');
    $series['complete'] = true;
    save_series($file, $series);
    fwrite(STDERR, "saved $file\n");
    flock($lock, LOCK_UN);
    echo series_table($series, [], false, 'master');
    return 0;
}

function cmd_table(array $positional, array $options): int
{
    if (isset($options['help']) || count($positional) !== 1) {
        usage_table();
        return isset($options['help']) ? 0 : 2;
    }
    $series = json_decode((string) @file_get_contents($positional[0]), true);
    if (!is_array($series) || ($series['kind'] ?? '') !== 'compare') {
        throw new BenchError("not a series from `bench compare`: {$positional[0]}");
    }
    $labels = [];
    if (isset($options['labels'])) {
        $lines = @file((string) $options['labels'], FILE_IGNORE_NEW_LINES | FILE_SKIP_EMPTY_LINES)
            ?: throw new BenchError("cannot read {$options['labels']}");
        foreach ($lines as $line) {
            [$id, $label] = array_pad(explode('=', $line, 2), 2, null);
            $labels[$id] = $label ?? $id;
        }
    }
    if (empty($series['complete'])) {
        warn('the series is incomplete (interrupted?): the table has the cases measured so far');
    }
    echo series_table($series, $labels, isset($options['full']), (string) ($options['base-name'] ?? 'master'));
    return 0;
}

/* ---------------------------------------------------------------- measuring */

/**
 * Takes an exclusive lock on the CPU for the whole series: a second `bench compare` or
 * `bench run` on the same CPU would disturb both. The lock goes away with the process.
 *
 * @return resource
 */
function lock_cpu(int $cpu)
{
    $file = sys_get_temp_dir() . "/php-src-bench-cpu$cpu.lock";
    $lock = fopen($file, 'c+') ?: throw new BenchError("cannot open $file");
    if (!flock($lock, LOCK_EX | LOCK_NB)) {
        $holder = trim((string) stream_get_contents($lock));
        throw new BenchError("CPU $cpu is in use by another bench process" . ($holder !== '' ? " ($holder)" : '') . '; wait for it or pick another CPU with --cpu');
    }
    ftruncate($lock, 0);
    fwrite($lock, 'pid ' . getmypid() . ', since ' . date('H:i'));
    fflush($lock);
    return $lock;
}

/**
 * The perf binary and the events that count cycles and instructions of the pinned process
 * (all privilege levels: start-up in the kernel cancels out with the empty run).
 *
 * @return array{string, string}
 */
function perf_cycles_probe(int $cpu): array
{
    $perf = perf_probe($cpu);
    $events = is_dir('/sys/devices/cpu_core') ? 'cpu_core/cycles/,cpu_core/instructions/' : 'cycles,instructions';
    return [$perf, $events];
}

/**
 * Cycles and instructions of one harness process that runs case $id $n times (or the empty
 * loop $n times).
 *
 * @return array{float, float}
 */
function perf_cycles(string $perf, string $events, string $php, string $suite, string $id, int $n, bool $empty, int $cpu): array
{
    // "empty" is 0 or 1 so that both command lines have the same length, as in perf_start().
    $command = array_merge(taskset_prefix($cpu), [$perf, 'stat', '-x', ',', '-e', $events, '--'],
        php_command($php, $suite, ['mode' => 'fixed', 'case' => $id, 'n' => $n, 'empty' => (int) $empty]));
    $proc = proc_open($command, [1 => ['file', '/dev/null', 'w'], 2 => ['pipe', 'w']], $pipes, null, ['LC_ALL' => 'C'] + getenv());
    if (!is_resource($proc)) {
        throw new BenchError('cannot start perf');
    }
    $report = (string) stream_get_contents($pipes[2]);
    fclose($pipes[2]);
    if (proc_close($proc) !== 0) {
        throw new BenchError("perf stat failed for '$id' on $php:\n$report");
    }
    return perf_parse_cycles($report, $id);
}

/**
 * Cycles and instructions from `perf stat -x,` output, e.g.
 *
 *     52345678,,cpu_core/cycles/,51234567,100.00,,
 *     123456789,,cpu_core/instructions/,51234567,100.00,,
 *
 * @return array{float, float}
 */
function perf_parse_cycles(string $report, string $id): array
{
    $found = [];
    foreach (explode("\n", $report) as $line) {
        $f = explode(',', $line);
        if (!isset($f[2]) || !preg_match('/^\d+$/', $f[0]) || str_contains($f[2], 'cpu_atom')) {
            continue;
        }
        $event = str_contains($f[2], 'instructions') ? 'instructions' : (str_contains($f[2], 'cycles') ? 'cycles' : null);
        if ($event !== null) {
            if (isset($f[4]) && is_numeric($f[4]) && (float) $f[4] < 100) {
                warn("perf counter for '$id' ran {$f[4]}% of the time, the count is scaled and noisy");
            }
            $found[$event] = (float) $f[0];
        }
    }
    if (!isset($found['cycles'], $found['instructions'])) {
        throw new BenchError("no cycle or instruction count from perf for '$id':\n$report");
    }
    return [$found['cycles'], $found['instructions']];
}

function save_series(string $file, array $series): void
{
    @mkdir(dirname($file), 0777, true);
    $json = json_encode($series, JSON_PRETTY_PRINT | JSON_UNESCAPED_SLASHES | JSON_UNESCAPED_UNICODE | JSON_THROW_ON_ERROR);
    if (@file_put_contents($file, $json . "\n") === false) {
        throw new BenchError("cannot write $file");
    }
}

/* ---------------------------------------------------------------- the table */

/** A change as a signed whole percent, rounded half up: "−25", "+4", "0" (ratio 0.75 → "−25"). */
function percent_change(float $ratio): string
{
    $v = (int) floor(($ratio - 1) * 100 + 0.5);
    return $v > 0 ? "+$v" : ($v < 0 ? '−' . -$v : '0');
}

/** "GCC 13.3" or "clang 20.1" from the compiler a build was made with, or null. */
function compiler_name(?array $build): ?string
{
    $cc = $build['cc'] ?? '';
    if (preg_match('/clang version (\d+\.\d+)/', $cc, $m)) {
        return "clang $m[1]";
    }
    // "gcc-14 (Ubuntu 14.2.0-4ubuntu2~24.04) 14.2.0": the version is the last word.
    if (preg_match('/^(?:\S*-)?g?cc\b.*\s(\d+\.\d+)\.\d+$/', $cc, $m)) {
        return "GCC $m[1]";
    }
    return null;
}

/**
 * The Markdown table of a series: per row, A's median cycles in the first group, then per group
 * the median over passes of (B cycles / median A cycles − 1). Control groups get a table of
 * their own after the main one.
 *
 * @param array<string, string> $labels case id => label, in display order; empty: every case
 */
function series_table(array $series, array $labels, bool $full, string $baseName): string
{
    $cyc = [];
    $ins = [];
    foreach ($series['rows'] as [$g, $side, $id, $c, $i]) {
        $cyc[$id][$g][$side][] = $c;
        $ins[$id][$g][$side][] = $i;
    }
    if (!$labels) {
        foreach (array_keys($series['cases']) as $id) {
            $labels[$id] = $id;
        }
    }
    $main = [];
    $control = [];
    foreach ($series['groups'] as $g) {
        if (in_array($g['name'], ['aa', 'aa2'], true)) {
            $control[$g['name']] = $g['name'] === 'aa' ? 'A/A start' : 'A/A end';
        } else {
            $main[$g['name']] = compiler_name($series['builds'][$g['b']]['build'] ?? null) ?? $g['name'];
        }
    }
    // Two groups with the same compiler (e.g. two changes) are told apart by their names.
    if (count(array_unique($main)) < count($main)) {
        foreach ($main as $name => $title) {
            $main[$name] = "$title ($name)";
        }
    }
    $out = '';
    foreach ([[$main, true], [$control, false]] as [$groups, $isMain]) {
        if (!$groups) {
            continue;
        }
        $first = array_key_first($groups);
        $withIns = $full && $isMain;
        if (!$isMain) {
            $out .= "\nControl: $baseName against itself.\n\n";
        }
        $out .= "| call | $baseName, CPU cycles per call ({$groups[$first]}) | " . implode(' | ', $groups) . ' |' . ($withIns ? ' instructions |' : '') . "\n";
        $out .= '|---|--:|' . str_repeat('--:|', count($groups)) . ($withIns ? '--:|' : '') . "\n";
        foreach ($labels as $id => $label) {
            if (!isset($cyc[$id][$first]['a'])) {
                if (!isset($series['cases'][$id])) {
                    throw new BenchError("no case '$id' in the series");
                }
                continue; // not measured yet
            }
            $cells = [];
            $insRatios = [];
            foreach ($groups as $g => $title) {
                if (!isset($cyc[$id][$g]['a'], $cyc[$id][$g]['b'])) {
                    $cells[] = '';
                    continue;
                }
                $a = median($cyc[$id][$g]['a']);
                $ratios = array_map(static fn (int $b): float => $b / $a, $cyc[$id][$g]['b']);
                sort($ratios);
                $cell = percent_change(median($ratios)) . '%';
                if ($full) {
                    $cell .= ' (' . percent_change($ratios[0]) . ' … ' . percent_change(end($ratios)) . ')';
                }
                $cells[] = $cell;
                $insRatios[] = median($ins[$id][$g]['b']) / median($ins[$id][$g]['a']);
            }
            $line = "| $label | " . number_format(median($cyc[$id][$first]['a'])) . ' | ' . implode(' | ', $cells) . ' |';
            if ($withIns && $insRatios) {
                $lo = percent_change(min($insRatios));
                $hi = percent_change(max($insRatios));
                $line .= " $lo%" . ($lo === $hi ? '' : " … $hi%") . ' |';
            }
            $out .= $line . "\n";
        }
    }
    return $out;
}
