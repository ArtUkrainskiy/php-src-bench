<?php
/*
 * Unit checks for the parts of the tool that decide what a table says. Run through
 * tests/run.sh, or directly:
 *
 *   php -n tests/unit.php
 */
declare(strict_types=1);

define('BENCH_ROOT', dirname(__DIR__));
require BENCH_ROOT . '/lib/console.php';
require BENCH_ROOT . '/lib/environment.php';
require BENCH_ROOT . '/lib/process.php';
require BENCH_ROOT . '/lib/stats.php';
require BENCH_ROOT . '/lib/render.php';
require BENCH_ROOT . '/lib/compare.php';
require BENCH_ROOT . '/lib/Corpus.php';

$failed = 0;
$checks = 0;
function same($expected, $actual, string $what): void
{
    global $failed, $checks;
    $checks++;
    if ($expected !== $actual) {
        $failed++;
        fwrite(STDERR, "FAIL $what\n  expected: " . var_export($expected, true) . "\n  actual:   " . var_export($actual, true) . "\n");
    }
}
function throws(string $class, callable $fn, string $what): void
{
    try {
        $fn();
        same($class, 'no exception', $what);
    } catch (Throwable $e) {
        same($class, get_class($e), $what);
    }
}

/* ---- statistics */

same(2.0, median([3, 1, 2]), 'median, odd count');
same(2.5, median([4, 1, 2, 3]), 'median, even count');
same('+', verdict([10, 11, 12], [7, 8, 9]), 'every B round faster');
same('-', verdict([7, 8, 9], [10, 11, 12]), 'every B round slower');
same('~', verdict([8, 9, 10], [7, 9.5, 11]), 'overlapping rounds');
$stats = side_stats(['loop_ns' => [1.0, 1.0], 'rounds' => [[11.0, 12.0, 13.0], [11.0, 11.0, 14.0]]]);
same(10.5, $stats['median'], 'empty loop is subtracted from the median');
same([11.0, 10.0], $stats['round_medians'], 'round medians');
same(null, $stats['instructions'], 'no instruction count without --perf');

/* ---- what a row says: result_rows() on a made-up result with one case */

/** A result with one case; every side gets the same samples in each of its rounds. */
function result_with(array $roundsA, array $roundsB, array $extra = []): array
{
    $side = static fn (array $rounds, string $hash): array => [
        'rounds' => array_map(static fn (float $ns): array => [$ns, $ns, $ns], $rounds),
        'loop_ns' => array_fill(0, count($rounds), 0.0),
        'n' => array_fill(0, count($rounds), 1000),
        'input_hash' => ['in'],
        'output_hash' => [$hash],
    ];
    $a = $extra['A'] ?? [];
    $b = $extra['B'] ?? [];
    return [
        'config' => ['rounds' => count($roundsA), 'perf' => isset($a['instructions'])],
        'cases' => ['case' => ['input_len' => 8, 'sides' => ['A' => $a + $side($roundsA, 'out'), 'B' => $b + $side($roundsB, 'out')]]],
    ];
}
function row(array $result): array
{
    return result_rows($result, ['A', 'B'], true, (bool) $result['config']['perf'])[0];
}

$row = row(result_with([100.0, 101.0, 102.0, 103.0], [50.0, 51.0, 52.0, 53.0]));
same('+', $row['verdict'], 'B clearly faster');
same(true, abs($row['ratio'] - 101.5 / 51.5) < 1e-9, 'ratio is A time / B time');
same('-', row(result_with([50.0, 51.0, 52.0, 53.0], [100.0, 101.0, 102.0, 103.0]))['verdict'], 'B clearly slower');
same('~', row(result_with([100.0, 100.1, 100.2, 100.3], [99.5, 99.6, 99.7, 99.8]))['verdict'], 'separated rounds, but less than 1% apart: no mark');
same('~', row(result_with([99.5, 99.6, 99.7, 99.8], [100.0, 100.1, 100.2, 100.3]))['verdict'], 'the 1% rule is the same in both directions');
same('?', row(result_with([100.0, 101.0], [50.0, 51.0]))['verdict'], 'no verdict with fewer than 4 rounds');
$row = row(result_with([0.02, 0.02, 0.02, 0.02], [0.06, 0.06, 0.06, 0.06]));
same([null, '~'], [$row['ratio'], $row['verdict']], 'times near zero are not compared');
$row = row(result_with([100.0, 101.0, 102.0, 103.0], [50.0, 51.0, 52.0, 53.0], ['A' => ['instructions' => 1000.0], 'B' => ['instructions' => 1001.0]]));
same(true, $row['same_instructions'] ?? false, 'time changed, instructions did not: flagged');
$row = row(result_with([100.0, 101.0, 102.0, 103.0], [50.0, 51.0, 52.0, 53.0], ['A' => ['instructions' => 1000.0], 'B' => ['instructions' => 500.0]]));
same([false, 2.0], [isset($row['same_instructions']), $row['instr_ratio']], 'time and instructions both changed: not flagged');
$row = row(result_with([100.0, 101.0, 102.0, 103.0], [50.0, 51.0, 52.0, 53.0], ['A' => ['instructions' => 1000.0], 'B' => ['instructions' => 0.0]]));
same(null, $row['instr_ratio'], 'no instruction ratio against zero');
same(true, row(result_with([100.0, 101.0, 102.0, 103.0], [50.0, 51.0, 52.0, 80.0]))['disturbed'] ?? false, 'a round far from the others is reported');
same(true, row(result_with([1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], ['B' => ['output_hash' => ['other']]]))['out_diff'] ?? false, 'different outputs');
same(true, row(result_with([1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], ['B' => ['input_hash' => ['other']]]))['in_diff'] ?? false, 'different inputs');
$row = row(result_with([1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0], ['A' => ['output_hash' => ['x', 'y']]]));
same([true, false], [$row['unstable'] ?? false, isset($row['out_diff'])], 'a result that changes between processes is not an A/B difference');

/* ---- the two sides must be comparable */

$build = ['configure' => '--disable-all', 'cflags' => '-O2', 'cc' => 'gcc 13'];
$side = static fn (bool $debug, ?array $build): array => ['name' => 'x', 'info' => ['debug' => $debug], 'build' => $build];
same([], check_sides(['A' => $side(false, $build), 'B' => $side(false, $build)]), 'equal builds: nothing to report');
same(1, count(check_sides(['A' => $side(false, $build), 'B' => $side(true, $build)])), 'a debug build is reported');
same(1, count(check_sides(['A' => $side(false, $build), 'B' => $side(false, ['cc' => 'clang 18'] + $build)])), 'another compiler is reported');
same(1, count(check_sides(['A' => $side(false, $build), 'B' => $side(false, null)])), 'a binary of unknown origin is reported');

/* ---- formatting */

same('2.45× faster', format_ratio(2.45, 'faster', 'slower'), 'ratio above 1');
same('2.00× slower', format_ratio(0.5, 'faster', 'slower'), 'ratio below 1 is inverted');
same('10.9× fewer', format_ratio(10.9, 'fewer', 'more'), 'one decimal from 10×');
same('1.00×', format_ratio(1.0, 'faster', 'slower'), 'no direction for equal values');
same('1.00×', format_ratio(0.997, 'faster', 'slower'), 'no direction when it rounds to 1.00');
same('1.01× slower', format_ratio(1 / 1.006, 'faster', 'slower'), 'smallest difference with a direction');
same('52.8', format_ns(52.84), 'nanoseconds below 1000');
same('15294', format_ns(15294.4), 'nanoseconds from 1000');
same(12, text_width('1.62× faster'), 'width counts characters, not bytes');
$source = ['snapshot' => false, 'commit' => str_repeat('a', 40), 'subject' => 'Fix it'];
same('aaaaaaaaaaa Fix it', build_source($source), 'a build of a commit');
same('working tree on top of bbbbbbbbbbb Base', build_source(['snapshot' => true, 'base_commit' => str_repeat('b', 40), 'base_subject' => 'Base'] + $source), 'a build of a working tree');

/* ---- perf output */

same(123456789.0, perf_parse_instructions("123456789,,cpu_core/instructions/u,2000000,100.00,,\n", 'case'), 'perf stat CSV line');
same(42.0, perf_parse_instructions("some warning\n42,,instructions:u,1000,100.00,,\n", 'case'), 'other lines are skipped');
throws('BenchError', static fn () => perf_parse_instructions("<not counted>,,cpu_core/instructions/u,0,0.00,,\n", 'case'), 'a counter that did not count');

/* ---- command line */

same([['html'], ['a' => 'base', 'b' => 'dev', 'perf' => true, 'rounds' => '6']],
    parse_args(['html', '--a', 'base', '--b=dev', '--perf', '--rounds', '6']), 'options and positional arguments');
throws('BenchError', static fn () => parse_args(['--nope']), 'unknown option');
throws('BenchError', static fn () => parse_args(['--a']), 'option without a value');
same(6, int_option(['rounds' => '6'], 'rounds', 4), 'integer option');
same(4, int_option([], 'rounds', 4), 'integer option default');
throws('BenchError', static fn () => int_option(['rounds' => 'six'], 'rounds', 4), 'integer option with junk');
same(2.5, float_option(['target-ms' => '2.5'], 'target-ms', 10.0), 'float option');

/* ---- environment */

same([0, 1, 2, 3, 8], parse_cpu_list('0-3,8'), 'cpu list with a range');
same([], parse_cpu_list(null), 'missing cpu list');

/* ---- bench compare and bench table */

same('−25', percent_change(0.75), 'percent_change: fewer cycles');
same('+4', percent_change(1.04), 'percent_change: more cycles');
same('0', percent_change(0.996), 'percent_change: rounds to 0, never "−0"');
same('−12', percent_change(0.875), 'percent_change: half rounds up, towards +');
same('+1', percent_change(1.005), 'percent_change: 1.005 is +0.5%, rounds up');
same('0', percent_change(0.995), 'percent_change: 0.995 is −0.5%, rounds up to 0');
same('+3', percent_change(1.025), 'percent_change: +2.5% rounds up');
same('−2', percent_change(0.975), 'percent_change: −2.5% rounds up');
same('GCC 14.2', compiler_name(['cc' => 'gcc (GCC) 14.2.1 20240912 (Red Hat 14.2.1-3)']), 'compiler_name: Fedora gcc');
$tiny = ['groups' => [['name' => 'g', 'a' => 'x', 'b' => 'y']], 'builds' => [], 'cases' => ['c1' => ['n' => 10], 'c2' => ['n' => 10]],
    'marks' => ['g' => ['c2' => '≠out']],
    'rows' => [['g', 'a', 'c1', 150, 300, 0, 0], ['g', 'b', 'c1', 120, 300, 0, 0], ['g', 'a', 'c2', 5000, 9000, 1000, 2000], ['g', 'b', 'c2', 2500, 9000, 1000, 2000]]];
$table = series_table($tiny, [], false, 'master');
same(true, str_contains($table, '| c1 | 15 | n/a |'), 'series_table: under 20 cycles per call is n/a');
same(true, str_contains($table, '| c2 | 400 | −62% ≠out |'), 'series_table: format 2 totals minus the empty loop, with the ≠out mark');
same(true, str_contains($table, 'n/a: under 20 cycles'), 'series_table: n/a is explained');
$tiny['cases']['c2'] += ['input_len' => 1030, 'input_chars' => 579];
same(true, str_contains(series_table($tiny, [], false, 'master', true), '| c2 (1.78 B/char) | 400 |'), 'series_table: --bpc adds bytes per character');
same('−1', percent_change(0.9949), 'percent_change: below half rounds down');
same('GCC 13.3', compiler_name(['cc' => 'gcc (Ubuntu 13.3.0-6ubuntu2~24.04.1) 13.3.0']), 'compiler_name: gcc');
same('GCC 14.2', compiler_name(['cc' => 'gcc-14 (Ubuntu 14.2.0-4ubuntu2~24.04) 14.2.0']), 'compiler_name: gcc-14');
same('GCC 13.3', compiler_name(['cc' => 'cc (Ubuntu 13.3.0-6ubuntu2~24.04.1) 13.3.0']), 'compiler_name: cc');
same('clang 20.1', compiler_name(['cc' => 'Ubuntu clang version 20.1.2 (0ubuntu1~24.04.3)']), 'compiler_name: clang');
same(null, compiler_name(null), 'compiler_name: foreign binary');
same([52345678.0, 123456789.0], perf_parse_cycles("52345678,,cpu_core/cycles/,51234567,100.00,,\n123456789,,cpu_core/instructions/,51234567,100.00,,\n", 'x'), 'perf_parse_cycles: hybrid CPU');
same([5.0, 7.0], perf_parse_cycles("1,,cpu_atom/cycles/,0,0.00,,\n5,,cycles,9,100.00,,\n7,,instructions,9,100.00,,\n", 'x'), 'perf_parse_cycles: skips E-core counters');
throws('BenchError', static fn () => perf_parse_cycles("<not counted>,,cpu_core/cycles/,0,0.00,,\n", 'x'), 'perf_parse_cycles: no count');

/* ---- languages */

same(['en-1k', 'es-1k', 'ru-1k', 'ar-1k', 'hi-1k', 'zh-1k', 'ja-1k', 'ko-1k', 'emoji-1k'], array_keys(Corpus::languages('1k', 1024)), 'Corpus::languages names');
same(Corpus::text('ru', 1024), (Corpus::languages('1k', 1024)['ru-1k'])(), 'Corpus::languages is Corpus::text');
same(31, strlen((Corpus::languages('title', 0)['en-title'])()), 'a title is the first line (31 bytes in English)');

/* ---- corpus: generated inputs are the same on every machine and PHP version */

same('4a642ea9db7259853dbbfe507132ec1c', md5(Corpus::text('en', 4096)), 'Corpus::text(en) changed: published results use these bytes');
same('cdc1a06a1fdb53a3dc4984c1ea8318a7', md5(Corpus::entities(0.25, 4096)), 'Corpus::entities changed: published results use these bytes');
same(true, strlen(Corpus::text('en', 1000)) >= 1000, 'Corpus::text returns at least the requested bytes');
same("\n", substr(Corpus::text('ru', 100), -1), 'Corpus::text keeps whole lines');
same(false, str_contains(Corpus::entities(0.0, 512), '&'), 'no entities at share 0');
same(1, preg_match('/^(&[#A-Za-z0-9]*;?)+$/', Corpus::entities(1.0, 512, 'named')), 'only entities at share 1');
same(4096, strlen(Corpus::slice('en', 4096)), 'Corpus::slice is exact');
throws('MissingCorpus', static fn () => Corpus::text('no-such-corpus', 10), 'missing corpus file');
throws('InvalidArgumentException', static fn () => Corpus::entities(0.5, 64, 'nope'), 'unknown entity pool');

echo $failed ? "$failed of $checks checks failed\n" : "$checks checks passed\n";
exit($failed ? 1 : 0);
