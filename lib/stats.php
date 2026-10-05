<?php
/*
 * Statistics over the raw samples of one case: medians, spread and the A/B verdict.
 */
declare(strict_types=1);

function median(array $values): float
{
    sort($values);
    $count = count($values);
    $mid = intdiv($count, 2);
    return $count % 2 ? (float) $values[$mid] : ($values[$mid - 1] + $values[$mid]) / 2;
}

/**
 * Robust statistics of the per-op times of one side, with the cost of the empty loop removed.
 *
 * @param array{loop_ns: list<float>, rounds: list<list<float>>, instructions?: float} $side
 * @return array{median: float, spread_pct: float, round_medians: list<float>, instructions: ?float}
 */
function side_stats(array $side): array
{
    $loop = median($side['loop_ns']);
    $all = [];
    $roundMedians = [];
    foreach ($side['rounds'] as $samples) {
        $net = array_map(static fn ($t): float => $t - $loop, $samples);
        $roundMedians[] = median($net);
        array_push($all, ...$net);
    }
    $med = median($all);
    $mad = median(array_map(static fn (float $t): float => abs($t - $med), $all));
    return [
        'median' => $med,
        // 1.4826·MAD estimates the standard deviation for normally distributed samples
        'spread_pct' => $med > 0 ? 1.4826 * $mad / $med * 100 : 0.0,
        'round_medians' => $roundMedians,
        'instructions' => $side['instructions'] ?? null,
    ];
}

/**
 * Compares the round medians of both sides: '+' if every B round beat every A round,
 * '-' if every B round lost to every A round, '~' otherwise.
 */
function verdict(array $a, array $b): string
{
    if (max($b) < min($a)) {
        return '+';
    }
    if (min($b) > max($a)) {
        return '-';
    }
    return '~';
}
