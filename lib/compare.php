<?php
/*
 * `bench compare` and `bench table`: a series of CPU cycles and instructions per call for pairs
 * of builds (A = the reference, B = the change), one pair per group, usually one group per
 * compiler, and the table of the change in cycles relative to A that goes into PR comments.
 *
 * Each count is `perf stat` of user-space cycles and instructions over a harness process that
 * runs one case a fixed number of times, minus the same process running the empty loop as many
 * times: what is left is the cost of the expression alone, with start-up and loop overhead
 * cancelled. All
 * processes run one after another on one CPU, in passes that alternate the order of A and B.
 * Unless --no-control is given, the series starts and ends with A of the first group against
 * itself (groups "aa" and "aa2"): the spread of that control is the noise floor of the series.
 *
 * Before measuring, every build evaluates every case once: a case whose result or input differs
 * between A and B of a group is marked (≠out, ≠in), and builds made with different compilers'
 * options, flags or profiles within a group are reported, as `bench run` does.
 *
 * A series (format 2), saved after every case so that an interrupted one still has its data:
 *   format, kind ("compare"), date, suite, elapsed_s, complete
 *   config    passes, cpu, target_ms, filter, control, events
 *   env       the machine, see system_info()
 *   groups    list of {name, a, b}, in the order measured
 *   builds    by name: {php, build (.bench-build.json or null), info}
 *   cases     by case id: {input_len, n (iterations per count)}
 *   warnings  list of strings: unfair groups, differing results
 *   marks     by group, by case id: "≠out" or "≠in"
 *   rows      list of [group, "a"|"b", case id, cycles, instructions, empty-loop cycles,
 *             empty-loop instructions], totals of the n-iteration processes
 * Format 1 had [group, side, case id, cycles per call, instructions per call] rows.
 */
declare(strict_types=1);

const SERIES_FORMAT = 2;

/** Below this many cycles per call of A, the change is not shown in percent: compare instructions. */
const MIN_TABLE_CYCLES = 20;

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

    Needs perf with access to hardware counters (`bench check`); on a hybrid CPU, a P-core.
    The A/A control uses one binary: it shows run-to-run noise, not code placement.
    Then: bench table <series.json> [--full] [--labels FILE] [--base-name NAME] [--header]

    USAGE;
}

function usage_table(): void
{
    echo <<<'USAGE'
    Usage: bench table <series.json> [--full] [--labels FILE] [--base-name NAME] [--header]

      Markdown table of the change in CPU cycles per call relative to A, one column per group;
      the control groups follow in a table of their own. Say "negative = fewer cycles (faster)"
      above the table where you publish it.
      --full         add the range over the passes to each cell and a column with the change
                     in instructions (for reports)
      --labels FILE  rows to show and their labels, one "<case id>=<label>" per line, in order
                     (default: every case, labelled by its id)
      --base-name N  what A is called in the second column (default: master)
      --header       first print how the series was measured (machine, builds, passes)

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
    $config['events'] = $events;

    // Every build evaluates every case once: which cases it has, and what they return.
    $lengths = null;
    $hashes = [];
    foreach ($builds as $name => $side) {
        progress("checking $name");
        $list = harness($side['php'], $suite, ['mode' => 'list', 'filter' => $config['filter']], $config['cpu']);
        $builds[$name]['info'] = $list['php'];
        $ids = array_column($list['cases'], 'input_len', 'id');
        if ($lengths !== null && ($only = array_diff_key($ids, $lengths) + array_diff_key($lengths, $ids))) {
            warn('cases not in every build, skipped: ' . implode(', ', array_keys($only)));
        }
        $lengths = $lengths === null ? $ids : array_intersect_key($lengths, $ids);
        $run = harness($side['php'], $suite, ['mode' => 'run', 'samples' => 3, 'target_ms' => 5, 'warmup_ms' => 2, 'filter' => $config['filter'], 'known_n' => []], $config['cpu']);
        foreach ($run['cases'] as $c) {
            $hashes[$name][$c['id']] = $c;
        }
    }
    if (!$lengths) {
        throw new BenchError('no cases match');
    }
    $warnings = [];
    $marks = [];
    foreach ($order as $g) {
        $sides = ['A' => $builds[$g['a']] + ['name' => $g['a']], 'B' => $builds[$g['b']] + ['name' => $g['b']]];
        foreach (check_sides($sides) as $problem) {
            $warnings[] = "group {$g['name']}: $problem";
        }
        foreach (array_keys($lengths) as $id) {
            $a = $hashes[$g['a']][$id];
            $b = $hashes[$g['b']][$id];
            if ($a['input_hash'] !== $b['input_hash']) {
                $marks[$g['name']][$id] = '≠in';
            } elseif ($a['output_hash'] !== $b['output_hash']) {
                $marks[$g['name']][$id] = '≠out';
            }
        }
        if (isset($marks[$g['name']])) {
            $warnings[] = "group {$g['name']}: A and B give different results or inputs in " . count($marks[$g['name']]) . ' case(s): '
                . implode(', ', array_map(static fn ($id, $m) => "$id ($m)", array_keys($marks[$g['name']]), $marks[$g['name']]));
        }
    }
    foreach (array_merge(check_machine($env), $warnings) as $warning) {
        warn($warning);
    }

    // Iterations per case: enough for the reference to run about target_ms, the same for every build.
    $cases = [];
    foreach ($hashes[$first['a']] as $id => $c) {
        if (isset($lengths[$id])) {
            $ns = max(1.0, median($c['samples_ns']) - $c['loop_ns']);
            $cases[$id] = ['input_len' => $lengths[$id], 'n' => max(20, (int) ($config['target_ms'] * 1e6 / $ns))];
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
        'warnings' => $warnings,
        'marks' => $marks,
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
                    $series['rows'][] = [$g['name'], $side, $id, $body[0], $body[1], $empty[0], $empty[1]];
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
        $lines = @file((string) $options['labels'], FILE_IGNORE_NEW_LINES | FILE_SKIP_EMPTY_LINES);
        if ($lines === false || !$lines) {
            throw new BenchError("cannot read {$options['labels']}, or it has no rows");
        }
        foreach ($lines as $line) {
            [$id, $label] = array_pad(explode('=', $line, 2), 2, null);
            $labels[$id] = $label ?? $id;
        }
    }
    if (empty($series['complete'])) {
        warn('the series is incomplete (interrupted?): the table has the cases measured so far');
    }
    foreach ($series['warnings'] ?? [] as $warning) {
        warn($warning);
    }
    if (isset($options['header'])) {
        echo series_header($series), "\n";
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
    // One lock per physical core (SMT siblings share it), in /tmp whatever TMPDIR says, so that
    // every shell and every user finds the same file.
    $core = min(cpu_siblings($cpu));
    $file = "/tmp/php-src-bench-core$core.lock";
    $lock = @fopen($file, 'c+') ?: throw new BenchError("cannot open $file");
    @chmod($file, 0666);
    if (!flock($lock, LOCK_EX | LOCK_NB)) {
        $holder = trim((string) stream_get_contents($lock));
        throw new BenchError("CPU $cpu (or its SMT sibling) is in use by another bench process" . ($holder !== '' ? " ($holder)" : '') . '; wait for it or pick another CPU with --cpu');
    }
    ftruncate($lock, 0);
    fwrite($lock, 'pid ' . getmypid() . ', since ' . date('H:i'));
    fflush($lock);
    return $lock;
}

/**
 * The perf binary and the events that count user-space cycles and instructions of the pinned
 * process, checked by counting them once. On a hybrid CPU the counters are those of the P-cores.
 *
 * @return array{string, string}
 */
function perf_cycles_probe(int $cpu): array
{
    $pcores = parse_cpu_list(read_sys('/sys/devices/cpu_core/cpus'));
    if ($pcores && !in_array($cpu, $pcores, true)) {
        throw new BenchError("CPU $cpu is not a performance core; pick one of " . read_sys('/sys/devices/cpu_core/cpus') . ' with --cpu');
    }
    $perf = perf_probe($cpu);
    $events = $pcores ? 'cpu_core/cycles/u,cpu_core/instructions/u' : 'cycles:u,instructions:u';
    $proc = proc_open(array_merge(taskset_prefix($cpu), [$perf, 'stat', '-x', ',', '-e', $events, '--', 'true']),
        [1 => ['file', '/dev/null', 'w'], 2 => ['pipe', 'w']], $pipes, null, ['LC_ALL' => 'C'] + getenv());
    $report = is_resource($proc) ? (string) stream_get_contents($pipes[2]) : '';
    if (is_resource($proc)) {
        proc_close($proc);
    }
    perf_parse_cycles($report, 'a probe of the counters');
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
    // Rounded to 9 decimals first, so that 1.005 is +0.5% and rounds up, as on paper.
    $v = (int) floor(round(($ratio - 1) * 100, 9) + 0.5);
    return $v > 0 ? "+$v" : ($v < 0 ? '−' . -$v : '0');
}

/** "GCC 13.3" or "clang 20.1" from the compiler a build was made with, or null. */
function compiler_name(?array $build): ?string
{
    $cc = $build['cc'] ?? '';
    if (preg_match('/clang version (\d+\.\d+)/', $cc, $m)) {
        return "clang $m[1]";
    }
    // "gcc-14 (Ubuntu 14.2.0-4ubuntu2~24.04) 14.2.0", "gcc (GCC) 14.2.1 20240912 (Red Hat 14.2.1-3)"
    if (preg_match('/^(?:\S*-)?g?cc\b.*?\)\s+(\d+\.\d+)\.\d+/', $cc, $m)) {
        return "GCC $m[1]";
    }
    return null;
}

/** What the series is about: machine, builds of every group, passes; the lines above a published table. */
function series_header(array $series): string
{
    $env = $series['env'] ?? [];
    $lines = [];
    if (!empty($env['cpu_model'])) {
        $lines[] = sprintf('Machine: %s, CPU %s, kernel %s.', $env['cpu_model'], $env['cpu'] ?? '?', $env['kernel'] ?? '?');
    }
    foreach ($series['groups'] as $g) {
        if (in_array($g['name'], ['aa', 'aa2'], true)) {
            continue;
        }
        $describe = static function (string $name) use ($series): string {
            $b = $series['builds'][$name]['build'] ?? null;
            if ($b === null) {
                return $name;
            }
            return sprintf('%s (%s %s%s)', $name, substr($b['commit'] ?? '', 0, 11), compiler_name($b) ?? '?',
                isset($b['profile']) ? ", profile {$b['profile']}" : '');
        };
        $lines[] = "Group {$g['name']}: A = {$describe($g['a'])}, B = {$describe($g['b'])}.";
    }
    $c = $series['config'] ?? [];
    if ($c) {
        $lines[] = sprintf('%d alternating passes per case, user-space cycles per call (perf stat, minus the empty loop)%s.',
            $c['passes'] ?? 0, !empty($c['control']) ? ', A against A at the start and the end' : '');
    }
    $lines[] = 'negative = fewer cycles (faster)';
    return implode("\n", $lines) . "\n";
}

/**
 * Per call cycles and instructions of each row: format 2 rows hold the totals of the n-iteration
 * processes, format 1 rows the per-call values.
 *
 * @return array{array, array} cycles and instructions by case id, group, side: lists over passes
 */
function series_per_call(array $series): array
{
    $cyc = [];
    $ins = [];
    foreach ($series['rows'] as $row) {
        [$g, $side, $id] = $row;
        if (count($row) === 5) {
            [$c, $i] = [(float) $row[3], (float) $row[4]];
        } else {
            $n = $series['cases'][$id]['n'];
            [$c, $i] = [($row[3] - $row[5]) / $n, ($row[4] - $row[6]) / $n];
        }
        $cyc[$id][$g][$side][] = $c;
        $ins[$id][$g][$side][] = $i;
    }
    return [$cyc, $ins];
}

/**
 * The Markdown table of a series: per row, A's median cycles in the first group, then per group
 * the median over passes of (B cycles / median A cycles − 1). Control groups get a table of
 * their own after the main one. A cell gets "≠out" or "≠in" when A and B of its group gave
 * different results or inputs; below MIN_TABLE_CYCLES of A it shows "n/a".
 *
 * @param array<string, string> $labels case id => label, in display order; empty: every case
 */
function series_table(array $series, array $labels, bool $full, string $baseName): string
{
    [$cyc, $ins] = series_per_call($series);
    if (!$labels) {
        foreach (array_keys($series['cases']) as $id) {
            $labels[$id] = $id;
        }
    }
    $main = [];
    $control = [];
    $controlCompiler = null;
    foreach ($series['groups'] as $g) {
        if (in_array($g['name'], ['aa', 'aa2'], true)) {
            $control[$g['name']] = $g['name'] === 'aa' ? 'A/A start' : 'A/A end';
            $controlCompiler ??= compiler_name($series['builds'][$g['a']]['build'] ?? null);
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
    $tooSmall = false;
    foreach ([[$main, true], [$control, false]] as [$groups, $isMain]) {
        if (!$groups) {
            continue;
        }
        $first = array_key_first($groups);
        $withIns = $full && $isMain;
        $scale = $isMain ? $groups[$first] : ($controlCompiler ?? $groups[$first]);
        if (!$isMain) {
            $out .= "\nControl: $baseName against itself.\n\n";
        }
        $out .= "| call | $baseName, CPU cycles per call ($scale) | " . implode(' | ', $groups) . ' |' . ($withIns ? ' instructions |' : '') . "\n";
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
                $mark = isset($series['marks'][$g][$id]) ? ' ' . $series['marks'][$g][$id] : '';
                if ($a < MIN_TABLE_CYCLES) {
                    $cells[] = 'n/a' . $mark;
                    $tooSmall = true;
                    continue;
                }
                $ratios = array_map(static fn ($b): float => $b / $a, $cyc[$id][$g]['b']);
                sort($ratios);
                $cell = percent_change(median($ratios)) . '%';
                if ($full) {
                    $cell .= ' (' . percent_change($ratios[0]) . ' … ' . percent_change(end($ratios)) . ')';
                }
                $cells[] = $cell . $mark;
                $insA = median($ins[$id][$g]['a']);
                if ($insA > 0) {
                    $insRatios[] = median($ins[$id][$g]['b']) / $insA;
                }
            }
            $line = "| $label | " . number_format(median($cyc[$id][$first]['a'])) . ' | ' . implode(' | ', $cells) . ' |';
            if ($withIns) {
                if ($insRatios) {
                    $lo = percent_change(min($insRatios));
                    $hi = percent_change(max($insRatios));
                    $line .= " $lo%" . ($lo === $hi ? '' : " … $hi%") . ' |';
                } else {
                    $line .= ' |';
                }
            }
            $out .= $line . "\n";
        }
    }
    if ($tooSmall) {
        $out .= "\nn/a: under " . MIN_TABLE_CYCLES . " cycles per call, the subtraction of the empty loop dominates; compare instructions.\n";
    }
    return $out;
}
