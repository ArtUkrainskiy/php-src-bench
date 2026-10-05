<?php
/*
 * Orchestrator behind `bench run|show|check|builds|suites`. For a run it starts one harness
 * process per side and round (lib/harness.php, inside the PHP binary under test), collects their
 * reports, optionally counts instructions with perf, saves the result and renders it.
 *
 * It is executed by whatever PHP is at hand, usually one of the benchmark builds, so it must
 * work on PHP 8.0+ built with --disable-all (no ctype, mbstring, posix).
 *
 * Data is passed around as arrays. The two that matter:
 *
 * A side, A or B:
 *   name       what the user passed to --a/--b
 *   php        absolute path of the binary
 *   build      metadata saved by `bench build` (.bench-build.json), or null for a foreign binary
 *   info       what the binary says about itself: version, debug, zts, arch (set by list_cases())
 *
 * A result, as saved in results/*.json (format 1; old files must keep rendering):
 *   format, date, suite, elapsed_s
 *   config     rounds, samples, target_ms, warmup_ms, filter, cpu, perf, wait_idle
 *   env        the machine, see system_info()
 *   sides      A and B as above
 *   cases      by case id:
 *     input_len              bytes of the input
 *     sides[A|B]:
 *       rounds        list of rounds, each a list of samples in ns per op (loop cost included)
 *       loop_ns       cost of the empty loop in ns per iteration, one value per round
 *       n             iterations per sample, one value per round
 *       input_hash    hashes of the input seen in the rounds; more than one: the case is not deterministic
 *       output_hash   the same for the result of the expression
 *       instructions  instructions per op, with --perf
 */
declare(strict_types=1);

define('BENCH_ROOT', getenv('BENCH_ROOT') ?: dirname(__DIR__));
define('BENCH_BUILDS', getenv('BENCH_BUILDS') ?: dirname(BENCH_ROOT) . '/php-builds');
define('HARNESS', BENCH_ROOT . '/lib/harness.php');

const RESULT_FORMAT = 1;

require __DIR__ . '/console.php';
require __DIR__ . '/environment.php';
require __DIR__ . '/process.php';
require __DIR__ . '/stats.php';
require __DIR__ . '/render.php';

exit(main($argv));

function main(array $argv): int
{
    try {
        [$positional, $options] = parse_args(array_slice($argv, 2));
        return match ($argv[1] ?? '') {
            'run' => cmd_run($positional, $options),
            'show' => cmd_show($positional, $options),
            'check' => cmd_check($options),
            'builds' => cmd_builds(),
            'suites' => cmd_suites(),
            default => throw new BenchError('unknown command, see `bench help`'),
        };
    } catch (BenchError $e) {
        fwrite(STDERR, "bench: {$e->getMessage()}\n");
        return 1;
    }
}

function usage_run(): void
{
    echo <<<'TXT'
    Usage: bench run <suite> --a <build|php> [--b <build|php>] [options]

      <suite>          suites/<suite>.php or a path to a suite file (`bench suites` lists them)
      --a, --b         build name in $BENCH_BUILDS or path to a php binary;
                       with --b, results read as "B is N× faster/slower than A"
      --filter RE      only cases whose id ("name @ input") matches RE (case-insensitive)
      --rounds N       A/B process pairs, alternating order ABBA (default 4)
      --samples N      timed samples per case per process (default 7)
      --target-ms MS   duration of one sample (default 10)
      --warmup-ms MS   warm-up per case per process (default 10)
      --cpu N          pin to this CPU (default: a P-core that is not CPU 0's sibling)
      --wait-idle S    before every measured process, wait until no compiler runs, load average
                       < 4 and the pinned CPU and its sibling are idle; after S seconds of
                       waiting in total, measure anyway and warn
      --quick          2 rounds, 5 samples, 5 ms: fast iteration, no verdicts
      --perf           also count instructions per op with perf stat (very low noise)
      --md             print a Markdown table (for PR descriptions)
      --no-save        do not save the result JSON to results/

    TXT;
}

/* ---------------------------------------------------------------- bench run */

function cmd_run(array $positional, array $options): int
{
    if (isset($options['help']) || !$positional) {
        usage_run();
        return isset($options['help']) ? 0 : 2;
    }
    $suite = resolve_suite($positional[0]);
    if (!isset($options['a'])) {
        throw new BenchError('--a <build|php> is required');
    }
    $sides = ['A' => resolve_side((string) $options['a'])];
    if (isset($options['b'])) {
        $sides['B'] = resolve_side((string) $options['b']);
    }
    $config = run_config($options);
    $env = system_info($config['cpu']);
    if ($config['perf']) {
        perf_probe($config['cpu']); // fail now rather than after the timed rounds
    }

    $ids = list_cases($sides, $suite, $config); // also fills $sides[..]['info'], which the checks below read
    foreach (array_merge(check_machine($env), check_sides($sides)) as $warning) {
        warn($warning);
    }

    $started = microtime(true);
    $cases = measure_rounds($sides, $suite, $config, $ids);
    if ($config['perf']) {
        $cases = measure_instructions($cases, $sides, $suite, $config);
    }
    progress('');

    $result = [
        'format' => RESULT_FORMAT,
        'date' => date('c'),
        'suite' => $suite,
        'elapsed_s' => round(microtime(true) - $started, 1),
        'config' => $config,
        'env' => $env,
        'sides' => array_map(static fn (array $s): array => [
            'name' => $s['name'],
            'php' => $s['php'],
            'info' => $s['info'],
            'build' => $s['build'],
        ], $sides),
        'cases' => $cases,
    ];
    if (!isset($options['no-save'])) {
        $file = save_result($result);
        $file === null ? warn('cannot write the result to ' . BENCH_ROOT . '/results') : fwrite(STDERR, "saved $file\n");
    }
    render($result, isset($options['md']));
    return 0;
}

/** @return list<string> names of the suites in suites/ */
function suite_names(): array
{
    return array_map(static fn (string $file): string => basename($file, '.php'), glob(BENCH_ROOT . '/suites/*.php') ?: []);
}

/** Resolves a suite name or path to the absolute path of the suite file. */
function resolve_suite(string $spec): string
{
    foreach ([$spec, BENCH_ROOT . "/suites/$spec.php", BENCH_ROOT . "/suites/$spec"] as $candidate) {
        if (is_file($candidate)) {
            return (string) realpath($candidate);
        }
    }
    throw new BenchError("suite not found: $spec (available: " . (implode(', ', suite_names()) ?: 'none') . ')');
}

/** Resolves --a/--b, a build name in $BENCH_BUILDS or a path to a php binary, to a side (without info). */
function resolve_side(string $spec): array
{
    if (str_contains($spec, '/') || is_file($spec)) {
        $php = realpath($spec);
        if ($php === false || !is_executable($php)) {
            throw new BenchError("not an executable: $spec");
        }
    } else {
        $php = BENCH_BUILDS . "/$spec/sapi/cli/php";
        if (!is_executable($php)) {
            $names = array_map('basename', glob(BENCH_BUILDS . '/*', GLOB_ONLYDIR) ?: []);
            throw new BenchError("unknown build '$spec' (available: " . (implode(', ', $names) ?: 'none') . ')');
        }
    }
    $meta = dirname($php, 3) . '/.bench-build.json'; // <build>/sapi/cli/php -> <build>
    $build = is_file($meta) ? json_decode((string) file_get_contents($meta), true) : null;
    return ['name' => $spec, 'php' => $php, 'build' => is_array($build) ? $build : null];
}

function cpu_option(array $options): int
{
    return isset($options['cpu']) ? int_option($options, 'cpu', 0) : default_cpu();
}

/** Measurement parameters from the command line; --quick only changes the defaults. */
function run_config(array $options): array
{
    $quick = isset($options['quick']);
    $config = [
        'rounds' => int_option($options, 'rounds', $quick ? 2 : 4),
        'samples' => int_option($options, 'samples', $quick ? 5 : 7),
        'target_ms' => float_option($options, 'target-ms', $quick ? 5.0 : 10.0),
        'warmup_ms' => float_option($options, 'warmup-ms', $quick ? 5.0 : 10.0),
        'filter' => isset($options['filter']) ? (string) $options['filter'] : null,
        'cpu' => cpu_option($options),
        'perf' => isset($options['perf']),
        'wait_idle' => int_option($options, 'wait-idle', 0),
    ];
    if ($config['rounds'] < 1 || $config['samples'] < 1) {
        throw new BenchError('--rounds and --samples must be at least 1');
    }
    if ($config['target_ms'] <= 0 || $config['target_ms'] > 1000 || $config['warmup_ms'] < 0) {
        throw new BenchError('--target-ms must be between 0 and 1000, --warmup-ms not negative');
    }
    return $config;
}

/**
 * Asks every side which cases of the suite it can run; stores PHP info in $sides and returns
 * the input length by case id for the cases both sides have.
 *
 * @return array<string, int>
 */
function list_cases(array &$sides, string $suite, array $config): array
{
    $lists = [];
    foreach ($sides as $label => $side) {
        $list = harness($side['php'], $suite, ['mode' => 'list', 'filter' => $config['filter']], $config['cpu']);
        $sides[$label]['info'] = $list['php'];
        $lists[$label] = array_column($list['cases'], 'input_len', 'id');
        if ($label === 'A' && $list['skipped']) {
            warn(skipped_inputs_message($list['skipped']));
        }
    }
    $common = isset($lists['B']) ? array_intersect_key($lists['A'], $lists['B']) : $lists['A'];
    foreach ($lists as $label => $list) {
        if ($missing = array_diff_key($list, $common)) {
            warn("cases only on $label, skipped: " . implode(', ', array_keys($missing)));
        }
    }
    if (!$common) {
        throw new BenchError('no cases match');
    }
    return $common;
}

/** @param list<array{input: string, reason: string}> $skipped */
function skipped_inputs_message(array $skipped): string
{
    $names = array_column($skipped, 'input');
    $shown = implode(', ', array_slice($names, 0, 4)) . (count($names) > 4 ? ', …' : '');
    return sprintf('%d input%s skipped (%s): %s', count($names), count($names) === 1 ? '' : 's', $shown, $skipped[0]['reason']);
}

/**
 * Runs the timed rounds. Sides alternate in ABBA order so that drift (temperature, frequency)
 * hits both equally.
 *
 * @param array<string, int> $inputLengths by case id, from list_cases()
 * @return array<string, array{input_len: int, sides: array<string, array>}> the "cases" of a result
 */
function measure_rounds(array $sides, string $suite, array $config, array $inputLengths): array
{
    $cases = [];
    foreach ($inputLengths as $id => $length) {
        $cases[$id] = ['input_len' => $length, 'sides' => []];
    }
    $labels = array_keys($sides);
    $knownN = []; // iteration counts calibrated by the first process of each side
    for ($round = 0; $round < $config['rounds']; $round++) {
        foreach ($round % 2 ? array_reverse($labels) : $labels as $label) {
            wait_idle($config, sprintf('round %d/%d: %s', $round + 1, $config['rounds'], $label));
            progress(sprintf('round %d/%d: %s (%s), %d cases', $round + 1, $config['rounds'], $label, $sides[$label]['name'], count($cases)));
            $report = harness($sides[$label]['php'], $suite, [
                'mode' => 'run',
                'filter' => $config['filter'],
                'samples' => $config['samples'],
                'target_ms' => $config['target_ms'],
                'warmup_ms' => $config['warmup_ms'],
                'known_n' => $knownN[$label] ?? [],
            ], $config['cpu']);
            foreach ($report['cases'] as $c) {
                if (!isset($cases[$c['id']])) {
                    continue; // a case the other side does not have
                }
                $knownN[$label][$c['id']] = $c['n'];
                $s = &$cases[$c['id']]['sides'][$label];
                $s['n'][] = $c['n'];
                $s['loop_ns'][] = $c['loop_ns'];
                $s['rounds'][] = $c['samples_ns'];
                $s['input_hash'][$c['input_hash']] = true;
                $s['output_hash'][$c['output_hash']] = true;
                unset($s);
            }
        }
    }
    // The hashes were collected as sets; store them as lists.
    foreach ($cases as &$case) {
        foreach ($case['sides'] as &$s) {
            $s['input_hash'] = array_keys($s['input_hash']);
            $s['output_hash'] = array_keys($s['output_hash']);
        }
        unset($s);
    }
    unset($case);
    return $cases;
}

/**
 * Adds instructions per op to every side of every case: perf stat over a fixed number of
 * iterations, minus the same number of iterations of the empty loop.
 */
function measure_instructions(array $cases, array $sides, string $suite, array $config): array
{
    // The same count for A and B: about as many iterations as one timed process ran.
    $iterations = static fn (array $case): int
        => max(array_map(static fn (array $side): int => max($side['n']), $case['sides'])) * $config['samples'];
    $jobs = [];
    foreach ($cases as $id => $case) {
        foreach ($sides as $label => $side) {
            foreach ([false, true] as $empty) {
                $jobs[] = ['php' => $side['php'], 'id' => $id, 'label' => $label, 'iterations' => $iterations($case), 'empty' => $empty];
            }
        }
    }
    $counts = perf_instructions($jobs, $suite, $config['cpu']);
    foreach ($cases as $id => &$case) {
        foreach ($sides as $label => $side) {
            $case['sides'][$label]['instructions'] = ($counts[$id][$label]['body'] - $counts[$id][$label]['empty']) / $iterations($case);
        }
    }
    unset($case);
    return $cases;
}

/** Writes the result to results/<date>-<time>-<suite>.json and returns the file name, or null on failure. */
function save_result(array $result): ?string
{
    $dir = BENCH_ROOT . '/results';
    @mkdir($dir, 0777, true);
    $file = sprintf('%s/%s-%s.json', $dir, date('Ymd-His'), basename($result['suite'], '.php'));
    $json = json_encode($result, JSON_PRETTY_PRINT | JSON_UNESCAPED_SLASHES | JSON_UNESCAPED_UNICODE | JSON_THROW_ON_ERROR);
    return @file_put_contents($file, $json . "\n") === false ? null : $file;
}

/* ---------------------------------------------------------------- other commands */

function cmd_show(array $positional, array $options): int
{
    $file = $positional[0] ?? throw new BenchError('usage: bench show <result.json> [--md]');
    $data = @file_get_contents($file);
    if ($data === false) {
        throw new BenchError("cannot read $file");
    }
    $result = json_decode($data, true);
    if (!is_array($result) || ($result['format'] ?? null) !== RESULT_FORMAT) {
        throw new BenchError("$file is not a result saved by bench run");
    }
    render($result, isset($options['md']));
    return 0;
}

function cmd_check(array $options): int
{
    $cpu = cpu_option($options);
    $env = system_info($cpu);
    echo environment_line($env), "\n";
    $warnings = check_machine($env);
    foreach ($warnings as $warning) {
        warn($warning);
    }
    try {
        perf_probe($cpu);
        echo "instruction counts (--perf): available\n";
    } catch (BenchError $e) {
        echo 'instruction counts (--perf): not available. ', preg_replace('/^--perf:? ?/', '', $e->getMessage()), "\n";
    }
    echo $warnings
        ? "wall times will be noisier than they could be; governor and turbo are advice, a busy CPU or a high load is a reason to wait\n"
        : "no noise sources detected\n";
    return 0;
}

function cmd_builds(): int
{
    $found = false;
    foreach (glob(BENCH_BUILDS . '/*/.bench-build.json') ?: [] as $file) {
        $build = json_decode((string) file_get_contents($file), true);
        if (!is_array($build)) {
            continue; // a build that was interrupted
        }
        printf("%-20s %-12s %s%s\n", $build['name'], $build['version'], build_source($build), $build['debug'] ? '  [debug build]' : '');
        $found = true;
    }
    if (!$found) {
        echo 'no builds in ' . BENCH_BUILDS . ", create one with: bench build <name> [<git-ref>|.]\n";
    }
    return 0;
}

/** Lists suites with the first line of the comment at the top of each file. */
function cmd_suites(): int
{
    foreach (suite_names() as $name) {
        $about = '';
        foreach (file(BENCH_ROOT . "/suites/$name.php") ?: [] as $line) {
            if (preg_match('~^//\s*(\S.*)$~', trim($line), $m)) {
                $about = $m[1];
                break;
            }
        }
        printf("%-20s %s\n", $name, $about);
    }
    return 0;
}
