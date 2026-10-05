<?php
/*
 * Turns a result (the array described at the top of runner.php) into a table for the terminal
 * or for Markdown, with everything a reader needs in order to judge it.
 */
declare(strict_types=1);

// A verdict needs this many rounds: with fewer, two equal builds separate cleanly by chance too often.
const MIN_ROUNDS_FOR_VERDICT = 4;
// Smaller differences between two builds are within code placement effects: no mark.
const MIN_RATIO_FOR_VERDICT = 1.01;
// Instruction counts closer than this count as unchanged.
const SAME_INSTRUCTIONS_RATIO = 1.005;
// Samples spread wider than this (percent) mean the wall time of the row is noise.
const NOISY_SPREAD_PCT = 5.0;
// A round this far from the fastest round of the same side was disturbed by something.
// Times under DISTURBED_MIN_NS jitter that much on their own and are not checked.
const DISTURBED_ROUND_RATIO = 1.10;
const DISTURBED_MIN_NS = 20.0;
// Below this many nanoseconds per op a time is the remainder of subtracting the empty loop: no ratio.
const MEASURABLE_NS = 0.5;

function render(array $result, bool $markdown): void
{
    $labels = array_keys($result['sides']);
    $ab = count($labels) === 2;
    $hasPerf = (bool) $result['config']['perf'];

    $rows = result_rows($result, $labels, $ab, $hasPerf);
    $header = result_header($result);
    $columns = table_columns($labels, $ab, $hasPerf);
    $table = table_cells($rows, $labels, $ab, $hasPerf, $markdown);
    $legend = legend($rows, $ab, $hasPerf, $markdown);

    if ($markdown) {
        print_markdown($header, $columns, $table, $legend);
    } else {
        print_plain($header, $columns, $table, $legend);
    }
    foreach (result_warnings($rows, $hasPerf) as $warning) {
        warn($warning);
    }
}

/**
 * One row per case: statistics of every side and, for A/B results, the comparison.
 *
 * Row keys: id, bytes, stats[label], disturbed (a round of some side is far from the others);
 * with two sides also ratio (A time / B time, null when there is nothing to compare), verdict
 * ('+', '-', '~', '?'), instr_ratio and the flags out_diff, in_diff, unstable, same_instructions.
 */
function result_rows(array $result, array $labels, bool $ab, bool $hasPerf): array
{
    $rows = [];
    foreach ($result['cases'] as $id => $case) {
        $stats = [];
        foreach ($labels as $label) {
            $stats[$label] = side_stats($case['sides'][$label]);
        }
        $row = ['id' => $id, 'bytes' => $case['input_len'], 'stats' => $stats];
        foreach ($stats as $st) {
            if (min($st['round_medians']) >= DISTURBED_MIN_NS && max($st['round_medians']) / min($st['round_medians']) > DISTURBED_ROUND_RATIO) {
                $row['disturbed'] = true;
            }
        }
        if ($ab) {
            [$a, $b] = [$stats['A'], $stats['B']];
            $measurable = $a['median'] >= MEASURABLE_NS && $b['median'] >= MEASURABLE_NS;
            $row['ratio'] = $measurable ? $a['median'] / $b['median'] : null;
            $row['verdict'] = $result['config']['rounds'] >= MIN_ROUNDS_FOR_VERDICT ? verdict($a['round_medians'], $b['round_medians']) : '?';
            if ($row['verdict'] !== '?' && ($row['ratio'] === null || max($row['ratio'], 1 / $row['ratio']) < MIN_RATIO_FOR_VERDICT)) {
                $row['verdict'] = '~';
            }
            $sideA = $case['sides']['A'];
            $sideB = $case['sides']['B'];
            if (count($sideA['output_hash']) > 1 || count($sideB['output_hash']) > 1) {
                $row['unstable'] = true;
            } elseif ($sideA['output_hash'] !== $sideB['output_hash']) {
                $row['out_diff'] = true;
            }
            if ($sideA['input_hash'] !== $sideB['input_hash']) {
                $row['in_diff'] = true;
            }
            if ($hasPerf) {
                $row['instr_ratio'] = $a['instructions'] > 0 && $b['instructions'] > 0 ? $a['instructions'] / $b['instructions'] : null;
                if (in_array($row['verdict'], ['+', '-'], true) && $row['instr_ratio'] !== null
                    && max($row['instr_ratio'], 1 / $row['instr_ratio']) < SAME_INSTRUCTIONS_RATIO) {
                    $row['same_instructions'] = true;
                }
            }
        }
        $rows[] = $row;
    }
    return $rows;
}

/** Where a build comes from: a commit, or a working tree on top of one. */
function build_source(array $build): string
{
    if ($build['snapshot'] && isset($build['base_commit'])) {
        return sprintf('working tree on top of %s %s', substr($build['base_commit'], 0, 11), $build['base_subject']);
    }
    return substr($build['commit'], 0, 11) . ' ' . $build['subject'] . ($build['snapshot'] ? ' (+ working tree)' : '');
}

/** Compiler and options of a build on one line. */
function build_options(array $build): string
{
    $parts = [$build['cc'], "configure {$build['configure']}"];
    if (isset($build['cflags_user'])) { // absent in metadata written by early versions
        $parts[] = "CFLAGS {$build['cflags_user']}";
    }
    return implode(', ', $parts);
}

/**
 * What makes a comparison of the two sides unfair. Used before a run and again when a result
 * is rendered, so that a published table carries it too.
 *
 * @return list<string>
 */
function check_sides(array $sides): array
{
    $problems = [];
    foreach ($sides as $label => $side) {
        if ($side['info']['debug']) {
            $problems[] = "$label ({$side['name']}) is a DEBUG build: its timings mean nothing";
        }
    }
    if (count($sides) < 2) {
        return $problems;
    }
    if (!isset($sides['A']['build'], $sides['B']['build'])) {
        $problems[] = 'A or B was not built by `bench build`: nothing checks that both have the same configure options and CFLAGS';
        return $problems;
    }
    // cflags are the effective ones from the Makefile, cflags_user what was asked for
    foreach (['configure', 'cflags', 'cc'] as $key) {
        if ($sides['A']['build'][$key] !== $sides['B']['build'][$key]) {
            $problems[] = "A and B differ in $key: '{$sides['A']['build'][$key]}' vs '{$sides['B']['build'][$key]}'";
        }
    }
    return $problems;
}

/** Lines above the table: what A and B are, the machine, the run parameters, what is wrong with the comparison. */
function result_header(array $result): array
{
    $header = [];
    foreach ($result['sides'] as $label => $side) {
        $source = $side['build'] ? build_source($side['build']) : $side['php'];
        $header[] = sprintf('%s: %s — PHP %s, %s%s', $label, $side['name'], $side['info']['version'], $source, $side['info']['debug'] ? ', DEBUG' : '');
    }
    $header[] = environment_line($result['env']);

    $config = $result['config'];
    $run = [sprintf('%d rounds × %d samples × %g ms', $config['rounds'], $config['samples'], $config['target_ms'])];
    if ($result['sides']['A']['build']) {
        $run[] = build_options($result['sides']['A']['build']);
    }
    $run[] = substr($result['date'], 0, 16) . substr($result['date'], 19); // minutes are enough; keep the UTC offset
    $header[] = implode(', ', $run);

    foreach (check_sides($result['sides']) as $problem) {
        $header[] = "! $problem";
    }
    return $header;
}

/** @return list<string> */
function table_columns(array $labels, bool $ab, bool $hasPerf): array
{
    $columns = ['case', 'bytes'];
    foreach ($labels as $label) {
        array_push($columns, $ab ? "$label ns/op" : 'ns/op', '±');
    }
    if ($ab) {
        $columns[] = 'B vs A';
    }
    if ($hasPerf) {
        foreach ($labels as $label) {
            $columns[] = $ab ? "$label instr/op" : 'instr/op';
        }
        if ($ab) {
            $columns[] = 'instr B vs A';
        }
    }
    return $columns;
}

/**
 * The cells of every row, in the order of table_columns().
 *
 * @return list<array{cells: list<string>, verdict: string}>
 */
function table_cells(array $rows, array $labels, bool $ab, bool $hasPerf, bool $markdown): array
{
    $marks = ['+' => $markdown ? '✅' : '✓', '-' => $markdown ? '❌' : '✗', '~' => '~', '?' => '?'];
    $table = [];
    foreach ($rows as $row) {
        $cells = [$row['id'], (string) $row['bytes']];
        foreach ($labels as $label) {
            $cells[] = format_ns($row['stats'][$label]['median']);
            $cells[] = sprintf('%.1f%%', $row['stats'][$label]['spread_pct']);
        }
        if ($ab) {
            $cells[] = ($row['ratio'] === null ? '≈0' : format_ratio($row['ratio'], 'faster', 'slower')) . " {$marks[$row['verdict']]}"
                . (isset($row['same_instructions']) ? ' layout?' : '')
                . (isset($row['out_diff']) ? ' ≠out' : '') . (isset($row['in_diff']) ? ' ≠in' : '');
        }
        if ($hasPerf) {
            foreach ($labels as $label) {
                $cells[] = sprintf('%.0f', $row['stats'][$label]['instructions']);
            }
            if ($ab) {
                $cells[] = $row['instr_ratio'] === null ? 'n/a' : format_ratio($row['instr_ratio'], 'fewer', 'more');
            }
        }
        $table[] = ['cells' => $cells, 'verdict' => $row['verdict'] ?? '~'];
    }
    return $table;
}

/** Explains the columns and only those marks that occur in this table. */
function legend(array $rows, bool $ab, bool $hasPerf, bool $markdown): string
{
    $has = static fn (string $key, $value = true): bool => in_array($value, array_column($rows, $key), true);
    $parts = ['ns/op: median time of one evaluation, loop overhead subtracted', '±: spread of the samples (1.4826·MAD/median)'];
    if ($ab) {
        $parts[] = 'B vs A: A time / B time';
        $parts[] = ($markdown ? '✅/❌' : '✓/✗') . ': every round of B was faster/slower than every round of A, by at least 1%';
        $parts[] = '~: rounds overlap, no clear difference';
        if ($has('verdict', '?')) {
            $parts[] = '?: no verdict with fewer than ' . MIN_ROUNDS_FOR_VERDICT . ' rounds';
        }
        if ($has('ratio', null)) {
            $parts[] = '≈0: too fast to compare';
        }
    }
    if ($hasPerf) {
        $parts[] = 'instr/op: instructions per evaluation';
    }
    if ($has('same_instructions')) {
        $parts[] = 'layout?: the time changed, the instruction count did not; the amount of work does not explain it (code placement? cache or branch behaviour?)';
    }
    if ($has('out_diff')) {
        $parts[] = '≠out: A and B returned different results';
    }
    if ($has('in_diff')) {
        $parts[] = '≠in: A and B got different inputs';
    }
    return implode('; ', $parts);
}

function print_markdown(array $header, array $columns, array $table, string $legend): void
{
    foreach ($header as $line) {
        echo "$line  \n";
    }
    // the first column is left-aligned, numbers are right-aligned
    $alignment = array_map(static fn (int $i): string => $i === 0 ? '---' : '--:', array_keys($columns));
    echo "\n| ", implode(' | ', $columns), " |\n";
    echo '|', implode('|', $alignment), "|\n";
    foreach ($table as $row) {
        echo '| ', implode(' | ', array_map(static fn (string $c): string => str_replace('|', '\|', $c), $row['cells'])), " |\n";
    }
    echo "\n<sub>$legend</sub>\n";
}

function print_plain(array $header, array $columns, array $table, string $legend): void
{
    $color = stream_isatty(STDOUT) && getenv('NO_COLOR') === false;
    foreach ($header as $line) {
        echo $color ? "\033[2m$line\033[0m\n" : "$line\n";
    }
    $widths = [];
    foreach (array_merge([$columns], array_column($table, 'cells')) as $cells) {
        foreach ($cells as $i => $cell) {
            $widths[$i] = max($widths[$i] ?? 0, text_width($cell));
        }
    }
    // The first column is left-aligned, numbers are right-aligned.
    $line = static function (array $cells) use ($widths): string {
        $out = [];
        foreach ($cells as $i => $cell) {
            $pad = str_repeat(' ', $widths[$i] - text_width($cell));
            $out[] = $i === 0 ? $cell . $pad : $pad . $cell;
        }
        return implode('  ', $out);
    };
    $colors = ['+' => "\033[32m", '-' => "\033[31m"]; // green: B faster, red: B slower
    echo "\n", $line($columns), "\n";
    foreach ($table as $row) {
        $text = $line($row['cells']);
        if ($color && isset($colors[$row['verdict']])) {
            $text = $colors[$row['verdict']] . $text . "\033[0m";
        }
        echo $text, "\n";
    }
    echo "\n", wordwrap($legend, 110, "\n"), "\n";
}

/**
 * Things the reader of the table must know before trusting it.
 *
 * @return list<string>
 */
function result_warnings(array $rows, bool $hasPerf): array
{
    $with = static fn (string $flag): array => array_column(array_filter($rows, static fn (array $row): bool => isset($row[$flag])), 'id');
    $plural = static fn (int $n, string $one, string $many): string => "$n " . ($n === 1 ? $one : $many);
    $warnings = [];
    if ($ids = $with('out_diff')) {
        $warnings[] = 'outputs differ between A and B for: ' . implode(', ', $ids);
    }
    if ($ids = $with('unstable')) {
        $warnings[] = 'the result changes from call to call, so outputs cannot be compared: ' . implode(', ', $ids);
    }
    if ($ids = $with('in_diff')) {
        $warnings[] = 'A and B measured different inputs (the suite builds them with a function that behaves differently), timings are not comparable: ' . implode(', ', $ids);
    }
    if ($n = count($with('same_instructions'))) {
        $warnings[] = $plural($n, 'case', 'cases') . ' changed wall time with unchanged instruction counts (layout?): the amount of work is the same, '
            . 'so look for the cause before reporting it: compare `objdump -d` of the function in both builds and `perf stat -e branch-misses,cache-misses`';
    }
    if ($ids = $with('disturbed')) {
        $warnings[] = $plural(count($ids), 'case has', 'cases have') . ' a round more than 10% slower than another round of the same build '
            . '(something disturbed a process), so the ratio and mark are shaky; run again: '
            . implode(', ', array_slice($ids, 0, 5)) . (count($ids) > 5 ? ', …' : '');
    }
    $noisy = count(array_filter($rows, static fn (array $row): bool => max(array_column($row['stats'], 'spread_pct')) > NOISY_SPREAD_PCT));
    if ($noisy) {
        $warnings[] = sprintf('%d of %d cases have a spread above %g%%: wall times are unreliable (background load?), %s',
            $noisy, count($rows), NOISY_SPREAD_PCT, $hasPerf ? 'instruction counts are unaffected' : 'rerun on an idle machine or add --perf');
    }
    return $warnings;
}

/** "10.9× faster" / "1.23× slower" for a ratio above / below 1; no direction when it rounds to 1.00×. */
function format_ratio(float $ratio, string $better, string $worse): string
{
    $times = $ratio >= 1 ? $ratio : 1 / $ratio;
    if ($times < 1.005) {
        return '1.00×';
    }
    return sprintf($times >= 10 ? '%.1f× %s' : '%.2f× %s', $times, $ratio >= 1 ? $better : $worse);
}

function format_ns(float $ns): string
{
    return $ns >= 1000 ? number_format($ns, 0, '.', '') : sprintf('%.1f', $ns);
}

/** Display width without mbstring: bytes minus UTF-8 continuation bytes. */
function text_width(string $s): int
{
    return strlen($s) - preg_match_all('/[\x80-\xBF]/', $s);
}
