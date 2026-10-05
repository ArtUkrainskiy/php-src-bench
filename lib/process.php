<?php
/*
 * Starting the processes that do the measuring: the harness inside a PHP binary under test,
 * pinned to one CPU, and `perf stat` around it for instruction counts.
 */
declare(strict_types=1);

/** Absolute path of a program from $PATH, or null. */
function find_executable(string $name): ?string
{
    foreach (array_merge(explode(':', (string) getenv('PATH')), ['/usr/bin', '/bin']) as $dir) {
        if ($dir !== '' && is_executable("$dir/$name") && !is_dir("$dir/$name")) {
            return "$dir/$name";
        }
    }
    return null;
}

/** `taskset -c <cpu>` as a command prefix, or nothing where taskset is missing (the runner warns). */
function taskset_prefix(int $cpu): array
{
    static $taskset = null;
    $taskset ??= find_executable('taskset') ?? '';
    return $taskset === '' ? [] : [$taskset, '-c', (string) $cpu];
}

/** The harness command line; -n keeps php.ini and extensions of the host out of the measurement. */
function php_command(string $php, string $suite, array $options): array
{
    return [$php, '-n', '-d', 'memory_limit=-1', HARNESS, $suite, json_encode($options)];
}

/** Runs the harness in $php pinned to $cpu and returns its JSON report. */
function harness(string $php, string $suite, array $options, int $cpu): array
{
    $command = array_merge(taskset_prefix($cpu), php_command($php, $suite, $options));
    $proc = proc_open($command, [1 => ['pipe', 'w'], 2 => STDERR], $pipes);
    if (!is_resource($proc)) {
        throw new BenchError("cannot start $php");
    }
    $out = (string) stream_get_contents($pipes[1]);
    fclose($pipes[1]);
    if (proc_close($proc) !== 0) {
        throw new BenchError("harness failed on $php");
    }
    $report = json_decode($out, true);
    if (!is_array($report)) {
        throw new BenchError("unexpected output from the harness on $php (does a case of the suite print something?):\n" . substr($out, 0, 300));
    }
    return $report;
}

/* ---------------------------------------------------------------- perf stat */

/** The event that counts user-space instructions; on hybrid CPUs only the P-core PMU has the pinned process. */
function perf_event(): string
{
    return is_dir('/sys/devices/cpu_core') ? 'cpu_core/instructions/u' : 'instructions:u';
}

/** `perf stat` around a command, pinned as a whole, printing CSV on stderr. */
function perf_command(string $perf, int $cpu, array $command): array
{
    return array_merge(taskset_prefix($cpu), [$perf, 'stat', '-x', ',', '-e', perf_event(), '--'], $command);
}

/**
 * Fails early, with a reason the user can act on, when instruction counts cannot be measured
 * here: perf missing, counters not permitted, or no hardware counters at all (most VMs).
 */
function perf_probe(int $cpu): string
{
    $perf = find_executable('perf')
        ?? throw new BenchError('--perf needs the perf tool (Debian/Ubuntu: linux-tools-common and linux-tools-$(uname -r))');
    $proc = proc_open(perf_command($perf, $cpu, ['true']), [1 => ['file', '/dev/null', 'w'], 2 => ['pipe', 'w']], $pipes, null, ['LC_ALL' => 'C'] + getenv());
    $report = is_resource($proc) ? (string) stream_get_contents($pipes[2]) : '';
    $status = is_resource($proc) ? proc_close($proc) : -1;
    if ($status === 0 && preg_match('/^\d+,/m', $report)) {
        return $perf;
    }
    if (str_contains($report, 'perf_event_paranoid')) {
        $virtual = preg_match('/^flags\s*:.*\bhypervisor\b/m', (string) @file_get_contents('/proc/cpuinfo')) === 1;
        throw new BenchError("--perf: the kernel does not let this user count instructions (kernel.perf_event_paranoid is "
            . trim((string) @file_get_contents('/proc/sys/kernel/perf_event_paranoid')) . "); allow it with: sudo sysctl kernel.perf_event_paranoid=1"
            . ($virtual ? '. This is a virtual machine: it may have no hardware counters at all, in which case --perf cannot work here' : ''));
    }
    if (str_contains($report, 'not supported') || str_contains($report, 'not counted')) {
        throw new BenchError("--perf: no instruction counter on CPU $cpu. Virtual machines usually have no hardware counters, "
            . 'and on a hybrid CPU only performance cores are counted; measure without --perf here');
    }
    throw new BenchError("--perf: perf stat does not work here:\n" . trim($report));
}

/**
 * Runs `perf stat` for every job on a small pool of CPUs and returns the instruction totals as
 * $counts[case id][side label]['body'|'empty']. A job is a fixed number of iterations of one
 * case, or of the empty loop. Instruction counts do not depend on load, so the jobs share the
 * machine.
 *
 * perf itself is pinned, not only its child: otherwise the child starts on any core, and on
 * hybrid CPUs the P-core counter runs less than 100% of the time and gets scaled, which adds
 * several percent of noise.
 *
 * @param list<array{php: string, id: string, label: string, iterations: int, empty: bool}> $jobs
 * @return array<string, array<string, array{body?: float, empty?: float}>>
 */
function perf_instructions(array $jobs, string $suite, int $cpu): array
{
    $perf = perf_probe($cpu);
    $cpus = perf_cpus($cpu);
    $running = [];
    $counts = [];
    $started = 0;
    $total = count($jobs);
    while ($jobs || $running) {
        while ($jobs && count($running) < count($cpus)) {
            $job = array_shift($jobs);
            $freeCpu = current(array_diff($cpus, array_column($running, 'cpu')));
            $running[] = perf_start($perf, $job, $suite, $freeCpu);
            progress(sprintf('perf %d/%d: %s', ++$started, $total, $job['id']));
        }
        foreach ($running as $i => $slot) {
            $running[$i]['report'] .= (string) stream_get_contents($slot['stderr']);
            $status = proc_get_status($slot['proc']);
            if (!$status['running']) {
                $job = $slot['job'];
                $counts[$job['id']][$job['label']][$job['empty'] ? 'empty' : 'body'] = perf_finish($running[$i], $status['exitcode']);
                unset($running[$i]);
            }
        }
        if ($running) {
            usleep(5000);
        }
    }
    return $counts;
}

/** Starts one job; the returned slot is what perf_finish() needs to collect it. */
function perf_start(string $perf, array $job, string $suite, int $cpu): array
{
    // "empty" is 0 or 1 so that both command lines of a case have the same length: the cost of
    // process start-up depends on it, and it must cancel out when the two counts are subtracted.
    $harness = php_command($job['php'], $suite, ['mode' => 'fixed', 'case' => $job['id'], 'n' => $job['iterations'], 'empty' => (int) $job['empty']]);
    $proc = proc_open(perf_command($perf, $cpu, $harness), [1 => ['file', '/dev/null', 'w'], 2 => ['pipe', 'w']], $pipes, null, ['LC_ALL' => 'C'] + getenv());
    if (!is_resource($proc)) {
        throw new BenchError('cannot start perf');
    }
    stream_set_blocking($pipes[2], false);
    return ['proc' => $proc, 'stderr' => $pipes[2], 'report' => '', 'cpu' => $cpu, 'job' => $job];
}

/** Collects a finished job and returns its instruction count. */
function perf_finish(array $slot, int $exitCode): float
{
    $report = $slot['report'] . stream_get_contents($slot['stderr']);
    fclose($slot['stderr']);
    // The exit code comes from proc_get_status(): before PHP 8.3 proc_close() returns -1 once
    // the status has been polled.
    proc_close($slot['proc']);
    $job = $slot['job'];
    if ($exitCode !== 0) {
        throw new BenchError("perf stat failed for '{$job['id']}' on {$job['php']}:\n$report");
    }
    return perf_parse_instructions($report, $job['id']);
}

/**
 * Extracts the instruction count from the CSV that `perf stat -x,` prints, for example
 *
 *     123456789,,cpu_core/instructions/u,2000000,100.00,,
 *
 * i.e. value, unit, event, time the counter ran, share of the run time it was counting.
 */
function perf_parse_instructions(string $report, string $id): float
{
    foreach (explode("\n", $report) as $line) {
        $fields = explode(',', $line);
        if (isset($fields[2]) && str_contains($fields[2], 'instructions') && preg_match('/^\d+$/', $fields[0])) {
            if (isset($fields[4]) && is_numeric($fields[4]) && (float) $fields[4] < 100) {
                warn("perf counter for '$id' ran {$fields[4]}% of the time, the count is scaled and noisy");
            }
            return (float) $fields[0];
        }
    }
    throw new BenchError("no instruction count from perf for '$id':\n$report");
}
