<?php
/*
 * The part that runs inside the PHP binary under test. It loads a suite, measures its cases and
 * prints a JSON report on stdout; the orchestrator (lib/runner.php) starts it once per side and
 * round. Modes:
 *
 *   php -n harness.php <suite.php> '{"mode":"list","filter":null}'
 *       which cases the suite has, and how long their inputs are
 *   php -n harness.php <suite.php> '{"mode":"run","samples":7,"target_ms":10,"warmup_ms":10,"filter":null,"known_n":{}}'
 *       calibrate, warm up and time every case; known_n maps case ids to iteration counts that an
 *       earlier process of the same side calibrated
 *   php -n harness.php <suite.php> '{"mode":"fixed","case":"<id>","n":100000,"empty":0}'
 *       run one case exactly n times and print nothing: for `perf stat` and profilers;
 *       "empty":1 runs the empty loop instead
 *
 * It must work on every PHP that may be measured: PHP 8.0+, built with --disable-all
 * (no ctype, mbstring, posix).
 */

require __DIR__ . '/Corpus.php';

// A warning or notice in a case means the measurement is not what the suite intended: fail loudly.
set_error_handler(static function (int $no, string $msg, string $file, int $line): bool {
    if (!(error_reporting() & $no)) {
        return false; // silenced with @
    }
    throw new ErrorException($msg, 0, $no, $file, $line);
});

try {
    $opt = json_decode($argv[2] ?? '{}', true, 16, JSON_THROW_ON_ERROR);
    $mode = $opt['mode'] ?? 'run';
    [$cases, $skipped] = bench_load_cases($argv[1] ?? '', $opt['filter'] ?? null, $mode === 'fixed' ? $opt['case'] : null);
    // No collector runs in the middle of a sample; the cases here do not create cycles.
    gc_disable();

    if ($mode === 'list') {
        $list = [];
        foreach ($cases as $case) {
            $list[] = ['id' => $case['id'], 'input_len' => bench_len($case['value'])];
        }
        echo json_encode(['php' => bench_php_info(), 'cases' => $list, 'skipped' => $skipped], JSON_THROW_ON_ERROR);
    } elseif ($mode === 'run') {
        $samples = (int) $opt['samples'];
        $targetNs = (int) ($opt['target_ms'] * 1e6);
        $warmupNs = (int) ($opt['warmup_ms'] * 1e6);
        $report = [];
        foreach ($cases as $case) {
            $knownN = $opt['known_n'][$case['id']] ?? null;
            try {
                $report[] = bench_run_case($case, $samples, $targetNs, $warmupNs, $knownN === null ? null : (int) $knownN);
            } catch (Throwable $e) {
                throw new RuntimeException("case '{$case['id']}': " . $e->getMessage(), 0, $e);
            }
        }
        echo json_encode(['php' => bench_php_info(), 'cases' => $report], JSON_THROW_ON_ERROR);
    } elseif ($mode === 'fixed') {
        if (count($cases) !== 1) {
            throw new RuntimeException("case not found: {$opt['case']}");
        }
        // The body run and the empty run must differ by the loop body only, so both evaluate the
        // expression once first: whatever its first call costs cancels out in the subtraction.
        $case = $cases[0];
        bench_evaluate($case);
        $loop = bench_compile_loop(empty($opt['empty']) ? $case['code'] : '');
        $loop($case['value'], (int) $opt['n']);
    } else {
        throw new RuntimeException("unknown mode: $mode");
    }
} catch (Throwable $e) {
    fwrite(STDERR, 'harness: ' . get_class($e) . ': ' . $e->getMessage() . ' in ' . $e->getFile() . ':' . $e->getLine() . "\n");
    exit(1);
}

/**
 * Expands the suite into cases, one per (case, input) pair, with the id "<case> @ <input>".
 * Inputs whose corpus file is missing are skipped and reported instead of failing the suite.
 *
 * @return array{list<array{id: string, code: string, value: mixed}>, list<array{input: string, reason: string}>}
 */
function bench_load_cases(string $file, ?string $filter, ?string $only): array
{
    if (!is_file($file)) {
        throw new RuntimeException("suite not found: $file");
    }
    // Loaded inside a closure, so that the suite's variables stay out of this scope.
    $suite = (static fn () => require $file)();
    if (!is_array($suite) || !isset($suite['inputs'], $suite['cases'])) {
        throw new RuntimeException("$file must return ['inputs' => [...], 'cases' => [...]]");
    }

    $cases = [];
    $values = [];
    $skipped = [];
    foreach ($suite['cases'] as $name => $case) {
        if (is_string($case)) {
            $case = ['code' => $case];
        }
        foreach ($case['inputs'] ?? array_keys($suite['inputs']) as $input) {
            if (!array_key_exists($input, $suite['inputs'])) {
                throw new RuntimeException("case '$name' uses unknown input '$input'");
            }
            $id = "$name @ $input";
            if ($only !== null && $id !== $only) {
                continue;
            }
            if ($filter !== null && $filter !== '' && !preg_match('#' . str_replace('#', '\#', $filter) . '#i', $id)) {
                continue;
            }
            if (isset($skipped[$input])) {
                continue;
            }
            if (!array_key_exists($input, $values)) {
                // Inputs are built lazily, so a filtered run only pays for what it uses.
                $value = $suite['inputs'][$input];
                try {
                    $values[$input] = $value instanceof Closure ? $value() : $value;
                } catch (MissingCorpus $e) {
                    $skipped[$input] = ['input' => (string) $input, 'reason' => $e->getMessage()];
                    continue;
                }
            }
            $cases[] = ['id' => $id, 'code' => $case['code'], 'value' => $values[$input]];
        }
    }
    return [$cases, array_values($skipped)];
}

/**
 * The measured loop as a closure: the case expression is compiled into the loop body, so there
 * is no call or timer per iteration. Returns the elapsed nanoseconds of $__n iterations.
 * An empty $code gives the empty loop whose cost is subtracted later.
 */
function bench_compile_loop(string $code): Closure
{
    $body = $code === '' ? '' : "$code;";
    return eval('return static function ($s, int $__n): int {
        $__t = hrtime(true);
        for ($__i = 0; $__i < $__n; ++$__i) { ' . $body . ' }
        return hrtime(true) - $__t;
    };');
}

/**
 * Evaluates the case expression once and returns the hash of its result, which is how the
 * outputs of A and B are compared. A case must leave its input alone: the loop keeps one $s for
 * all iterations, so an expression such as sort($s) would measure sorted input from the second
 * iteration on.
 */
function bench_evaluate(array $case): string
{
    $evaluate = eval("return static function (\$s) { \$__result = {$case['code']}; return [\$__result, \$s]; };");
    [$result, $inputAfter] = $evaluate($case['value']);
    if ($inputAfter !== $case['value']) {
        throw new RuntimeException('the expression modifies its input $s; work on a copy inside the expression');
    }
    return md5(serialize($result));
}

/** Iteration count for which one loop takes about $targetNs. */
function bench_calibrate(Closure $loop, $value, int $targetNs): int
{
    // Grow n until one loop takes at least 1/8 of the target: 32 times at a step while it is
    // still under 1/1024 of the target, then by doubling.
    $n = 1;
    $t = $loop($value, $n);
    while ($t < intdiv($targetNs, 8)) {
        $n *= $t < intdiv($targetNs, 1024) ? 32 : 2;
        $t = $loop($value, $n);
    }
    // Scale to the target, then measure at that count and scale once more: the first estimate
    // comes from a loop too short to be accurate.
    $n = max(1, intdiv($n * $targetNs, max($t, 1)));
    $t = $loop($value, $n);
    return max(1, intdiv($n * $targetNs, max($t, 1)));
}

/**
 * Times one case. $knownN is the iteration count calibrated by an earlier process of the same
 * side: reusing it skips calibration and keeps all rounds on the same count.
 */
function bench_run_case(array $case, int $samples, int $targetNs, int $warmupNs, ?int $knownN = null): array
{
    $value = $case['value'];
    $outputHash = bench_evaluate($case);
    $loop = bench_compile_loop($case['code']);
    $empty = bench_compile_loop('');

    $n = $knownN ?? bench_calibrate($loop, $value, $targetNs);
    $deadline = hrtime(true) + $warmupNs;
    do {
        $loop($value, $n);
    } while (hrtime(true) < $deadline);

    $times = [];
    for ($i = 0; $i < $samples; $i++) {
        $times[] = $loop($value, $n) / $n;
    }
    // Cost of the loop itself: median of five runs of the empty loop.
    $loopTimes = [];
    for ($i = 0; $i < 5; $i++) {
        $loopTimes[] = $empty($value, $n) / $n;
    }
    sort($loopTimes);

    return [
        'id' => $case['id'],
        'input_hash' => md5(serialize($value)),
        'output_hash' => $outputHash,
        'n' => $n,
        'samples_ns' => $times,
        'loop_ns' => $loopTimes[2],
    ];
}

/** Size of an input for the "bytes" column: string length, or serialized length of other values. */
function bench_len($value): int
{
    return is_string($value) ? strlen($value) : strlen(serialize($value));
}

function bench_php_info(): array
{
    return [
        'version' => PHP_VERSION,
        // int before PHP 8.4, bool since
        'debug' => (bool) PHP_DEBUG,
        'zts' => (bool) PHP_ZTS,
        'arch' => php_uname('m'),
        'binary' => PHP_BINARY,
    ];
}
