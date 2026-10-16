<?php
/*
 * `bench why`: when the cycles of a case change and its instructions do not, the work is the
 * same and something else moved: code placement, branch prediction, the front end. This counts
 * what perf can count for one case on two builds, per call, and shows where the functions you
 * name sit in each binary.
 */
declare(strict_types=1);

/**
 * Events tried, in the order shown; the ones this CPU cannot count are left out. The first six
 * count user space only, as `bench compare` does; the top-down slots cannot be restricted so.
 */
const WHY_EVENTS = [
    'cycles', 'instructions', 'branches', 'branch-misses',
    'L1-icache-load-misses', 'iTLB-load-misses',
    'slots', 'topdown-retiring', 'topdown-fe-bound', 'topdown-bad-spec', 'topdown-be-bound',
];

function usage_why(): void
{
    echo <<<'USAGE'
    Usage: bench why <suite> <A> <B> --filter RE [--functions f1,f2] [--passes N] [--cpu N]
           bench why --code EXPR [--inputs SPEC] [--setup CODE] <A> <B> [...]

      Counts cycles, instructions, branches and their misses, instruction cache and TLB misses
      and the top-down slots (where the CPU supports them) per call of each case that matches
      --filter, on A and B, in alternating passes (default 3), and prints the change.
      --functions  also print address, size and alignment of these functions in both binaries
                   (from nm): a function that moved is the first suspect when only cycles changed

    USAGE;
}

function cmd_why(array $positional, array $options): int
{
    if (isset($options['help']) || count($positional) < (isset($options['code']) ? 2 : 3)) {
        usage_why();
        return isset($options['help']) ? 0 : 2;
    }
    $suite = isset($options['code']) ? inline_suite($options) : resolve_suite(array_shift($positional));
    [$a, $b] = [resolve_side($positional[0]), resolve_side($positional[1])];
    $cpu = cpu_option($options);
    $passes = int_option($options, 'passes', 3);
    $filter = isset($options['filter']) ? (string) $options['filter'] : null;
    $lock = lock_cpu($cpu);
    [$perf] = perf_cycles_probe($cpu);
    $events = why_events($perf, $cpu);

    $run = harness($a['php'], $suite, ['mode' => 'run', 'samples' => 3, 'target_ms' => 5, 'warmup_ms' => 2, 'filter' => $filter, 'known_n' => []], $cpu);
    if (count($run['cases']) > 10) {
        throw new BenchError(count($run['cases']) . ' cases match: narrow them down with --filter');
    }
    $out = '';
    foreach ($run['cases'] as $c) {
        $n = max(20, (int) (50e6 / max(1.0, median($c['samples_ns']) - $c['loop_ns'])));
        $counts = ['a' => [], 'b' => []];
        for ($p = 1; $p <= $passes; $p++) {
            foreach ($p % 2 ? ['a' => $a, 'b' => $b] : ['b' => $b, 'a' => $a] as $side => $build) {
                progress("{$c['id']}: pass $p/$passes, " . strtoupper($side));
                $body = why_count($perf, $events, $build['php'], $suite, $c['id'], $n, false, $cpu);
                $empty = why_count($perf, $events, $build['php'], $suite, $c['id'], $n, true, $cpu);
                foreach ($body as $e => $v) {
                    $counts[$side][$e][] = ($v - ($empty[$e] ?? 0)) / $n;
                }
            }
        }
        progress('');
        $out .= "\n{$c['id']} (per call, median of $passes passes)\n\n| event | A | B | B vs A |\n|---|--:|--:|--:|\n";
        foreach ($events as $e) {
            if (!isset($counts['a'][$e], $counts['b'][$e])) {
                continue;
            }
            [$va, $vb] = [median($counts['a'][$e]), median($counts['b'][$e])];
            $out .= sprintf("| %s | %s | %s | %s |\n", $e, why_number($va), why_number($vb), $va >= 20 && $vb >= 20 ? percent_change($vb / $va) . '%' : '');
        }
    }
    flock($lock, LOCK_UN);
    echo "A: {$a['name']}\nB: {$b['name']}\n$out";
    if (isset($options['functions'])) {
        echo "\n", why_functions(explode(',', (string) $options['functions']), $a, $b);
    }
    return 0;
}

/** The events of WHY_EVENTS that perf can count on this CPU, probed one by one. */
/** The perf name of an event: on the P-core PMU of a hybrid CPU, user space only where possible. */
function why_event_name(string $e): string
{
    $user = !str_starts_with($e, 'topdown-') && $e !== 'slots';
    return is_dir('/sys/devices/cpu_core') ? "cpu_core/$e/" . ($user ? 'u' : '') : $e . ($user ? ':u' : '');
}

function why_events(string $perf, int $cpu): array
{
    $ok = [];
    foreach (WHY_EVENTS as $e) {
        $event = why_event_name($e);
        $proc = proc_open(array_merge(taskset_prefix($cpu), [$perf, 'stat', '-x', ',', '-e', $event, '--', 'true']),
            [1 => ['file', '/dev/null', 'w'], 2 => ['pipe', 'w']], $pipes, null, ['LC_ALL' => 'C'] + getenv());
        $report = (string) stream_get_contents($pipes[2]);
        proc_close($proc);
        if (preg_match('/^\d+,/m', $report)) {
            $ok[] = $e;
        }
    }
    return $ok;
}

/** @return array<string, float> event => count for one harness process */
function why_count(string $perf, array $events, string $php, string $suite, string $id, int $n, bool $empty, int $cpu): array
{
    $list = implode(',', array_map('why_event_name', $events));
    $command = array_merge(taskset_prefix($cpu), [$perf, 'stat', '-x', ',', '-e', $list, '--'],
        php_command($php, $suite, ['mode' => 'fixed', 'case' => $id, 'n' => $n, 'empty' => (int) $empty]));
    $proc = proc_open($command, [1 => ['file', '/dev/null', 'w'], 2 => ['pipe', 'w']], $pipes, null, ['LC_ALL' => 'C'] + getenv());
    $report = (string) stream_get_contents($pipes[2]);
    if (proc_close($proc) !== 0) {
        throw new BenchError("perf stat failed for '$id' on $php:\n$report");
    }
    $counts = [];
    foreach (explode("\n", $report) as $line) {
        $f = explode(',', $line);
        if (isset($f[2]) && preg_match('/^\d+$/', $f[0]) && !str_contains($f[2], 'cpu_atom')) {
            $name = preg_replace('#^cpu_core/|/u?$|:u$#', '', $f[2]);
            $counts[$name] = (float) $f[0];
            // More events than counters: perf time-shares them and scales the counts up.
            if (isset($f[4]) && is_numeric($f[4]) && (float) $f[4] < 100) {
                static $warned = [];
                if (!isset($warned[$name])) {
                    warn("perf counted $name only {$f[4]}% of the time (more events than counters): its row is an estimate");
                    $warned[$name] = true;
                }
            }
        }
    }
    return $counts;
}

function why_number(float $v): string
{
    return abs($v) >= 100 ? number_format($v) : sprintf('%.2f', $v);
}

/** Address, size and alignment of the named functions in both binaries, from `nm -S`. */
function why_functions(array $names, array $a, array $b): string
{
    $nm = find_executable('nm') ?? throw new BenchError('--functions needs nm (binutils)');
    $symbols = static function (string $php) use ($nm): array {
        $table = [];
        exec(escapeshellarg($nm) . ' -S --defined-only ' . escapeshellarg($php) . ' 2>/dev/null', $lines);
        foreach ($lines as $line) {
            if (preg_match('/^([0-9a-f]+) ([0-9a-f]+) [tTwW] (\S+)$/', $line, $m)) {
                $table[$m[3]] = [hexdec($m[1]), hexdec($m[2])];
            }
        }
        return $table;
    };
    [$sa, $sb] = [$symbols($a['php']), $symbols($b['php'])];
    $out = "| function | A address | A size | B address | B size | moved by | alignment A / B |\n|---|--:|--:|--:|--:|--:|--:|\n";
    foreach ($names as $name) {
        $name = trim($name);
        if (!isset($sa[$name], $sb[$name])) {
            $out .= "| $name | not found in " . (isset($sa[$name]) ? 'B' : 'A') . " (inlined or static with another name?) | | | | | |\n";
            continue;
        }
        [$addrA, $sizeA] = $sa[$name];
        [$addrB, $sizeB] = $sb[$name];
        $out .= sprintf("| %s | 0x%x | %d | 0x%x | %d | %+d | %d / %d |\n", $name, $addrA, $sizeA, $addrB, $sizeB, $addrB - $addrA, $addrA % 64, $addrB % 64);
    }
    return $out . "\nAlignment is the address modulo 64 (a cache line). Run `objdump -d` on both binaries for the hot loop itself.\n";
}
