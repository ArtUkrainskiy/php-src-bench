<?php
/*
 * What the machine looks like and how quiet it is: CPU topology, frequency settings, background
 * load. Everything is read from /proc and /sys, so this part is Linux only.
 */
declare(strict_types=1);

// --wait-idle considers the machine quiet below these limits. They are looser than the limits
// for warnings further down, because a condition to wait for has to be reachable on a desktop.
const QUIET_LOAD = 4.0;            // 1-minute load average
const QUIET_PINNED_BUSY_PCT = 15;  // the pinned CPU and its SMT sibling
const QUIET_ALL_BUSY_PCT = 30;     // average over all CPUs
const QUIET_SAMPLES = 3;           // consecutive quiet samples needed
// check_machine() warns above these.
const WARN_LOAD = 1.5;
const WARN_BUSY_PCT = 10;

function read_sys(string $path): ?string
{
    $v = @file_get_contents($path);
    return $v === false ? null : trim($v);
}

/**
 * Parses a kernel CPU list such as "0-11,14".
 *
 * @return list<int>
 */
function parse_cpu_list(?string $list): array
{
    $cpus = [];
    foreach (explode(',', (string) $list) as $part) {
        if (preg_match('/^(\d+)(?:-(\d+))?$/', trim($part), $m)) {
            $cpus = array_merge($cpus, range((int) $m[1], (int) ($m[2] ?? $m[1])));
        }
    }
    return $cpus;
}

/**
 * Hardware threads that share a physical core with $cpu, itself included.
 *
 * @return list<int>
 */
function cpu_siblings(int $cpu): array
{
    return parse_cpu_list(read_sys("/sys/devices/system/cpu/cpu$cpu/topology/thread_siblings_list")) ?: [$cpu];
}

/**
 * Performance cores of a hybrid CPU, every online CPU otherwise.
 *
 * @return list<int>
 */
function candidate_cpus(): array
{
    return parse_cpu_list(read_sys('/sys/devices/cpu_core/cpus'))
        ?: parse_cpu_list(read_sys('/sys/devices/system/cpu/online'));
}

/** First CPU (preferring P-cores) whose physical core is not the one of CPU 0, which gets most interrupts. */
function default_cpu(): int
{
    foreach (candidate_cpus() as $cpu) {
        if (!in_array(0, cpu_siblings($cpu), true)) {
            return $cpu;
        }
    }
    return 0;
}

/**
 * Up to four CPUs on different physical cores (CPU 0's core excluded) to spread perf runs over;
 * the pinned CPU comes first.
 *
 * @return list<int>
 */
function perf_cpus(int $pinned): array
{
    $cpus = [$pinned];
    $seen = cpu_siblings($pinned);
    foreach (candidate_cpus() as $cpu) {
        $group = cpu_siblings($cpu);
        if (in_array(0, $group, true) || array_intersect($group, $seen)) {
            continue;
        }
        $cpus[] = $cpu;
        $seen = array_merge($seen, $group);
        if (count($cpus) === 4) {
            break;
        }
    }
    return $cpus;
}

/**
 * Share of time each CPU was busy over a short window, from /proc/stat.
 *
 * @return array<int, float> percent by CPU number
 */
function cpu_busy(float $seconds = 0.3): array
{
    $snapshot = static function (): array {
        $cpus = [];
        foreach (@file('/proc/stat') ?: [] as $line) {
            if (preg_match('/^cpu(\d+)\s+(.+)$/', $line, $m)) {
                $v = array_map('intval', preg_split('/\s+/', trim($m[2])));
                // [total jiffies, idle + iowait]
                $cpus[(int) $m[1]] = [array_sum($v), $v[3] + ($v[4] ?? 0)];
            }
        }
        return $cpus;
    };
    $before = $snapshot();
    usleep((int) ($seconds * 1e6));
    $busy = [];
    foreach ($snapshot() as $cpu => [$total, $idle]) {
        $dt = $total - ($before[$cpu][0] ?? 0);
        $busy[$cpu] = $dt > 0 ? round(100 * (1 - ($idle - ($before[$cpu][1] ?? 0)) / $dt), 1) : 0.0;
    }
    return $busy;
}

/** True when a compiler, linker or build driver is running somewhere on the machine. */
function compiler_running(): bool
{
    foreach (glob('/proc/[0-9]*/comm') ?: [] as $file) {
        $comm = trim((string) @file_get_contents($file));
        if (in_array($comm, ['cc1', 'cc1plus', 'clang', 'clang++', 'ld', 'ld.lld', 'ld.gold', 'make', 'ninja', 'rustc'], true)) {
            return true;
        }
    }
    return false;
}

/** Busiest hardware thread of the physical core of $cpu, in percent. */
function core_busy(array $busy, int $cpu): float
{
    return max(array_map(static fn (int $c): float => $busy[$c] ?? 0.0, cpu_siblings($cpu)));
}

/**
 * Reasons why the machine is not quiet enough to measure right now; empty when it is.
 *
 * @return list<string>
 */
function quiet_blockers(int $cpu): array
{
    $blockers = [];
    if (compiler_running()) {
        $blockers[] = 'a compiler is running';
    }
    $load = sys_getloadavg();
    if ($load !== false && $load[0] >= QUIET_LOAD) {
        $blockers[] = sprintf('load %.1f', $load[0]);
    }
    $busy = cpu_busy(0.3);
    if (core_busy($busy, $cpu) >= QUIET_PINNED_BUSY_PCT) {
        $blockers[] = sprintf('CPU %d %.0f%% busy', $cpu, core_busy($busy, $cpu));
    }
    $average = array_sum($busy) / max(1, count($busy));
    if ($average >= QUIET_ALL_BUSY_PCT) {
        $blockers[] = sprintf('all CPUs %.0f%% busy on average', $average);
    }
    return $blockers;
}

/**
 * With --wait-idle, blocks until the machine is quiet (see quiet_blockers()) for a few samples
 * in a row. The configured number of seconds is the waiting budget of the whole run: once it
 * is spent, measuring goes on without waiting.
 */
function wait_idle(array $config, string $what): void
{
    // Run-wide state, shared by all calls of one `bench run`.
    static $budget = null;
    static $lastQuiet = 0.0;
    $budget ??= (float) $config['wait_idle'];
    if ($budget <= 0) {
        return;
    }
    // A machine found quiet less than a minute ago needs one sample, otherwise several.
    $needed = microtime(true) - $lastQuiet < 60 ? 1 : QUIET_SAMPLES;
    $quietSamples = 0;
    while ($quietSamples < $needed) {
        $started = microtime(true);
        $blockers = quiet_blockers($config['cpu']);
        if (!$blockers) {
            $quietSamples++;
            continue;
        }
        $quietSamples = 0;
        $needed = QUIET_SAMPLES;
        progress("waiting for an idle machine before $what (" . implode(', ', $blockers) . ')');
        sleep(2);
        $budget -= microtime(true) - $started;
        if ($budget <= 0) {
            progress('');
            warn("wait-idle: machine still busy after {$config['wait_idle']}s (" . implode(', ', $blockers) . '), measuring anyway');
            return;
        }
    }
    $lastQuiet = microtime(true);
    progress('');
}

/** Facts about the machine and the pinned CPU that are stored with every result. */
function system_info(int $cpu): array
{
    $model = null;
    if (preg_match('/^model name\s*:\s*(.+)$/m', (string) @file_get_contents('/proc/cpuinfo'), $m)) {
        $model = $m[1];
    }
    $onAc = null; // null: no mains supply found (desktop, VM)
    foreach (glob('/sys/class/power_supply/*/type') ?: [] as $typeFile) {
        if (read_sys($typeFile) === 'Mains') {
            $onAc = ($onAc ?? false) || read_sys(dirname($typeFile) . '/online') === '1';
        }
    }
    $noTurbo = read_sys('/sys/devices/system/cpu/intel_pstate/no_turbo');
    $boost = read_sys('/sys/devices/system/cpu/cpufreq/boost');
    $pcores = parse_cpu_list(read_sys('/sys/devices/cpu_core/cpus'));
    $load = sys_getloadavg();

    // Busy share of the pinned CPU and its SMT siblings, plus an idle alternative core.
    $busy = cpu_busy();
    $busyPinned = [];
    foreach (cpu_siblings($cpu) as $c) {
        $busyPinned[$c] = $busy[$c] ?? 0.0;
    }
    $idleCpu = null; // a CPU to suggest when the pinned one is busy
    foreach ($pcores ?: array_keys($busy) as $candidate) {
        if (!in_array(0, cpu_siblings($candidate), true) && core_busy($busy, $candidate) < WARN_BUSY_PCT) {
            $idleCpu = $candidate;
            break;
        }
    }
    return [
        'cpu_model' => $model,
        'kernel' => php_uname('r'),
        'cpu' => $cpu,
        'cpu_siblings' => read_sys("/sys/devices/system/cpu/cpu$cpu/topology/thread_siblings_list"),
        'hybrid_pcores' => $pcores ? read_sys('/sys/devices/cpu_core/cpus') : null,
        'cpu_is_pcore' => $pcores ? in_array($cpu, $pcores, true) : null,
        'governor' => read_sys("/sys/devices/system/cpu/cpu$cpu/cpufreq/scaling_governor"),
        'epp' => read_sys("/sys/devices/system/cpu/cpu$cpu/cpufreq/energy_performance_preference"),
        'turbo' => $noTurbo !== null ? $noTurbo === '0' : ($boost !== null ? $boost === '1' : null),
        'on_ac' => $onAc,
        'load' => $load === false ? null : $load[0],
        'busy_pct' => $busyPinned,
        'idle_cpu' => $idleCpu,
    ];
}

/**
 * Sources of timing noise on this machine. Governor and turbo are advice; load and a busy
 * pinned CPU make wall times unusable.
 *
 * @return list<string>
 */
function check_machine(array $env): array
{
    $warnings = [];
    $tune = 'sudo ' . BENCH_ROOT . '/bench tune on';
    if ($env['governor'] !== null && $env['governor'] !== 'performance') {
        $warnings[] = "CPU governor is '{$env['governor']}': frequency scaling adds noise ($tune)";
    }
    if ($env['turbo'] === true) {
        $warnings[] = "turbo boost is on: thermal and frequency drift between rounds ($tune)";
    }
    if ($env['on_ac'] === false) {
        $warnings[] = 'running on battery';
    }
    if ($env['load'] !== null && $env['load'] > WARN_LOAD) {
        $warnings[] = sprintf('load average is %.1f: other programs are competing for the CPU', $env['load']);
    }
    foreach ($env['busy_pct'] as $cpu => $pct) {
        if ($pct >= WARN_BUSY_PCT) {
            $who = (int) $cpu === $env['cpu'] ? "CPU $cpu" : "CPU $cpu (SMT sibling of CPU {$env['cpu']})";
            $advice = $env['idle_cpu'] !== null && $env['idle_cpu'] !== $env['cpu'] ? "try --cpu {$env['idle_cpu']}" : 'wait for it to finish';
            $warnings[] = sprintf('%s is %.0f%% busy with other processes: timings will be noisy (%s)', $who, $pct, $advice);
        }
    }
    if ($env['cpu_is_pcore'] === false) {
        $warnings[] = "CPU {$env['cpu']} is an efficiency core; P-cores: {$env['hybrid_pcores']}";
    }
    if (!taskset_prefix($env['cpu'])) {
        $warnings[] = 'taskset not found (package util-linux): processes are not pinned to a CPU';
    }
    return $warnings;
}

function environment_line(array $env): string
{
    $parts = [sprintf('CPU %d%s', $env['cpu'], $env['cpu_model'] ? " ({$env['cpu_model']})" : '')];
    if ($env['governor'] !== null) {
        $parts[] = "governor {$env['governor']}";
    }
    if ($env['turbo'] !== null) {
        $parts[] = 'turbo ' . ($env['turbo'] ? 'on' : 'off');
    }
    $parts[] = "kernel {$env['kernel']}";
    return implode(', ', $parts);
}
