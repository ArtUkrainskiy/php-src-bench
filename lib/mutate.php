<?php
/*
 * `bench mutate`: do the checks of a change catch it when it is wrong? Each mutation replaces one
 * piece of the changed C code with a plausible mistake, the build is rebuilt incrementally, and
 * the checks run: a differential test against a reference build and php-src tests. A mutation
 * that no check catches is a gap in the checks.
 *
 * The mutations file returns
 *
 *   [
 *       'difftest' => ['generator' => 'code', 'against' => 'base', 'args' => ['--code', '...', '--count', '2000']],
 *       'tests' => ['ext/mbstring/tests'],                      // run-tests.php in the build
 *       'mutations' => [
 *           'chunk loop runs down to 0' => ['file' => 'ext/mbstring/mbstring.c', 'from' => 'offset > 256', 'to' => 'offset > 0'],
 *       ],
 *   ]
 *
 * `from` must occur exactly once in the file. The original file is kept as <file>.bench-orig
 * while a mutation is in place, so that an interrupted run is undone by the next one.
 */
declare(strict_types=1);

function usage_mutate(): void
{
    echo <<<'USAGE'
    Usage: bench mutate <build> <mutations.php> [--only RE]

      <build>          a full build (not --slim) of the change: its sources are mutated in place,
                       rebuilt with make, and restored at the end
      <mutations.php>  the checks and the mutations, see the top of lib/mutate.php
      --only RE        only mutations whose name matches RE

    Prints a Markdown table: for every mutation, whether the differential test and the tests
    caught it. Before the mutations the same checks run on the unchanged build: the differential
    test must agree with the reference, and tests that fail already are not counted later.

    USAGE;
}

function cmd_mutate(array $positional, array $options): int
{
    if (isset($options['help']) || count($positional) !== 2) {
        usage_mutate();
        return isset($options['help']) ? 0 : 2;
    }
    [$buildName, $file] = $positional;
    $dir = str_contains($buildName, '/') ? rtrim($buildName, '/') : BENCH_BUILDS . "/$buildName";
    if (!is_file("$dir/Makefile") || !is_file("$dir/run-tests.php")) {
        throw new BenchError("$dir is not a full build (bench build without --slim)");
    }
    $spec = (static fn () => require $file)();
    if (!is_array($spec) || empty($spec['mutations'])) {
        throw new BenchError("$file must return ['mutations' => [...], 'difftest' => [...], 'tests' => [...]]");
    }
    if (empty($spec['difftest']) && empty($spec['tests'])) {
        throw new BenchError("$file has no checks: give it 'difftest', 'tests' or both");
    }
    mutate_restore_all($dir);

    $mutations = $spec['mutations'];
    if (isset($options['only'])) {
        $mutations = array_filter($mutations, static fn (string $name): bool => (bool) preg_match('#' . str_replace('#', '\#', (string) $options['only']) . '#i', $name), ARRAY_FILTER_USE_KEY);
    }
    foreach ($mutations as $name => $m) {
        $count = substr_count((string) @file_get_contents("$dir/{$m['file']}"), $m['from']);
        if ($count !== 1) {
            throw new BenchError("mutation '$name': 'from' occurs $count times in {$m['file']}, it must occur once");
        }
    }

    progress('the unchanged build: make');
    mutate_make($dir) || throw new BenchError("$dir does not build before any mutation");
    progress('the unchanged build: checks');
    $baseline = mutate_checks($dir, $spec);
    if (($baseline['difftest'] ?? 'same') !== 'same') {
        throw new BenchError("the differential test already differs on the unchanged build: {$baseline['difftest']}");
    }
    $knownFailures = $baseline['failed'] ?? [];
    if ($knownFailures) {
        warn(count($knownFailures) . ' test(s) fail on the unchanged build and are not counted: ' . implode(', ', array_slice($knownFailures, 0, 5)));
    }

    $rows = [];
    $i = 0;
    try {
        foreach ($mutations as $name => $m) {
            progress(sprintf('mutation %d/%d: %s', ++$i, count($mutations), $name));
            $path = "$dir/{$m['file']}";
            $original = (string) file_get_contents($path);
            file_put_contents("$path.bench-orig", $original);
            file_put_contents($path, str_replace($m['from'], $m['to'], $original));
            try {
                if (!mutate_make($dir)) {
                    $rows[$name] = ['build' => 'does not build'];
                    continue;
                }
                $result = mutate_checks($dir, $spec);
                $newFailures = array_values(array_diff($result['failed'] ?? [], $knownFailures));
                $rows[$name] = [
                    'difftest' => isset($result['difftest']) ? ($result['difftest'] === 'same' ? 'missed' : "caught ({$result['difftest']})") : null,
                    'tests' => isset($result['failed']) ? ($newFailures ? 'caught (' . count($newFailures) . ' failed)' : 'missed') : null,
                    'failed' => $newFailures,
                ];
            } finally {
                rename("$path.bench-orig", $path);
            }
        }
    } finally {
        progress('restoring the build: make');
        mutate_make($dir);
        progress('');
    }

    $out = sprintf("%s\n\n| mutation | difftest | tests |\n|---|---|---|\n", "Mutations of $buildName ($file)");
    $caught = 0;
    foreach ($rows as $name => $r) {
        if (isset($r['build'])) {
            $out .= "| $name | {$r['build']} | |\n";
            continue;
        }
        $caught += (str_starts_with((string) $r['difftest'], 'caught') || str_starts_with((string) $r['tests'], 'caught')) ? 1 : 0;
        $out .= sprintf("| %s | %s | %s |\n", $name, $r['difftest'] ?? 'not run', $r['tests'] ?? 'not run');
    }
    $out .= sprintf("\nCaught by at least one check: %d of %d mutations that build.\n", $caught, count(array_filter($rows, static fn (array $r): bool => !isset($r['build']))));
    echo $out;
    $saved = sprintf('%s/results/%s-mutate-%s.json', BENCH_ROOT, date('Ymd-His'), basename($dir));
    @mkdir(dirname($saved), 0777, true);
    @file_put_contents($saved, json_encode(['date' => date('c'), 'build' => $buildName, 'spec' => $spec, 'rows' => $rows],
        JSON_PRETTY_PRINT | JSON_UNESCAPED_SLASHES | JSON_UNESCAPED_UNICODE) . "\n");
    fwrite(STDERR, "saved $saved\n");
    return 0;
}

/** Puts back every source file that an interrupted run left mutated. */
function mutate_restore_all(string $dir): void
{
    $found = (string) shell_exec('find ' . escapeshellarg($dir) . ' -name "*.bench-orig" -not -path "*/.git/*" 2>/dev/null');
    foreach (array_filter(explode("\n", $found)) as $orig) {
        rename($orig, substr($orig, 0, -strlen('.bench-orig')));
        warn('restored ' . substr($orig, strlen($dir) + 1, -strlen('.bench-orig')) . ' from an interrupted run');
    }
}

function mutate_make(string $dir): bool
{
    $jobs = max(1, (int) trim((string) shell_exec('nproc 2>/dev/null')));
    exec('make -C ' . escapeshellarg($dir) . " -j$jobs >" . escapeshellarg("$dir/.bench-mutate-make.log") . ' 2>&1', $_, $status);
    return $status === 0;
}

/**
 * Runs the checks of the spec on the build.
 *
 * @return array{difftest?: string, failed?: list<string>} difftest: "same", "N of M inputs differ" or "crash";
 *         failed: the tests that failed
 */
function mutate_checks(string $dir, array $spec): array
{
    $result = [];
    $php = "$dir/sapi/cli/php";
    if (!empty($spec['difftest'])) {
        $d = $spec['difftest'];
        $cmd = array_merge([BENCH_ROOT . '/bench', 'difftest', (string) $d['generator'], (string) $d['against'], $php], array_map('strval', $d['args'] ?? []));
        $proc = proc_open($cmd, [1 => ['pipe', 'w'], 2 => ['pipe', 'w']], $pipes);
        $stdout = (string) stream_get_contents($pipes[1]);
        $stderr = (string) stream_get_contents($pipes[2]);
        $status = proc_close($proc);
        if ($status === 0) {
            $result['difftest'] = 'same';
        } elseif (preg_match('/MISMATCH: (\d+) of (\d+) inputs differ/', $stderr, $m)) {
            $result['difftest'] = "$m[1] of $m[2] inputs differ";
        } elseif (str_contains($stderr, 'FAILED')) {
            $result['difftest'] = 'crash';
        } else {
            throw new BenchError("bench difftest failed:\n$stdout$stderr");
        }
    }
    if (!empty($spec['tests'])) {
        $jobs = max(1, (int) trim((string) shell_exec('nproc 2>/dev/null')));
        $cmd = array_merge([$php, '-n', 'run-tests.php', '-q', "-j$jobs", '--no-color', '-p', $php], array_map('strval', $spec['tests']));
        $proc = proc_open($cmd, [1 => ['pipe', 'w'], 2 => ['pipe', 'w']], $pipes, $dir, ['TEST_PHP_EXECUTABLE' => $php, 'NO_INTERACTION' => '1'] + getenv());
        $out = (string) stream_get_contents($pipes[1]);
        stream_get_contents($pipes[2]);
        proc_close($proc);
        $failed = [];
        if (($pos = strpos($out, 'FAILED TEST SUMMARY')) !== false) {
            preg_match_all('/\[([^\]\s]+\.phpt)\]\s*$/m', substr($out, $pos), $m);
            $failed = $m[1];
        }
        $result['failed'] = array_values(array_unique($failed));
    }
    return $result;
}
