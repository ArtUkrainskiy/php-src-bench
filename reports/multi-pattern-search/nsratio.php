<?php

use Str\Matcher;
use Str\Replacer;

/*
 * Paired ns/op ratio in ONE process, robust to between-process frequency drift.
 * For R reps, time A then B (K calls each) back to back and record B/A per rep; report
 * the median ratio and the median absolute ns. Alternate the order each rep to cancel ramp.
 *
 * Usage: php -dextension=strmatch.so nsratio.php <pair> <N> <S> <K> <R> [seed]
 *   pair: replace-vs-strtr | matchall-vs-strpos
 */

function gen_dict(int $n, int $seed): array
{
    mt_srand($seed);
    $words = [];
    $seen = [];
    while (count($words) < $n) {
        $len = mt_rand(4, 12);
        $w = '';
        for ($i = 0; $i < $len; ++$i) {
            $w .= chr(mt_rand(97, 122));
        }
        if (isset($seen[$w])) {
            continue;
        }
        $seen[$w] = true;
        $words[] = $w;
    }

    return $words;
}

function gen_text(int $bytes, array $dict, int $seed): string
{
    mt_srand($seed ^ 0x5A5A);
    $n = count($dict);
    $out = '';
    while (strlen($out) < $bytes) {
        if (mt_rand(0, 99) < 8) {
            $out .= $dict[mt_rand(0, $n - 1)].' ';
        } else {
            $len = mt_rand(2, 10);
            for ($i = 0; $i < $len; ++$i) {
                $out .= chr(mt_rand(97, 122));
            }
            $out .= ' ';
        }
    }

    return substr($out, 0, $bytes);
}

// Mean ns per call of $op over $K calls.
function time_op(callable $op, int $K): float
{
    $t0 = hrtime(true);
    $sink = 0;
    for ($i = 0; $i < $K; ++$i) {
        $sink += $op();
    }
    $t1 = hrtime(true);

    return ($t1 - $t0) / $K;
}

$pair = $argv[1] ?? 'replace-vs-strtr';
$N = (int) ($argv[2] ?? 500);
$S = (int) ($argv[3] ?? 16384);
$K = (int) ($argv[4] ?? 500);
$R = (int) ($argv[5] ?? 15);
$seed = (int) ($argv[6] ?? 1);

$dict = gen_dict($N, $seed);
$map = [];
foreach ($dict as $i => $w) {
    $map[$w] = '<'.($i % 7).'>';
}
$text = gen_text($S, $dict, $seed);

if ('replace-vs-strtr' === $pair) {
    $replacer = new Replacer($map);
    $a_name = 'replace';
    $a_op = fn () => strlen($replacer->replace($text));
    $b_name = 'strtr';
    $b_op = fn () => strlen(strtr($text, $map));
} elseif ('matchall-vs-strpos' === $pair) {
    $matcher = new Matcher($dict);
    $a_name = 'matchAll';
    $a_op = fn () => count($matcher->matchAll($text));
    $b_name = 'strpos-loop';
    $b_op = function () use ($dict, $text) {
        $c = 0;
        foreach ($dict as $w) {
            if (str_contains($text, $w)) {
                ++$c;
            }
        }

        return $c;
    };
} else {
    fwrite(STDERR, "unknown pair\n");

    exit(2);
}

// Warm up (lazy caches, branch predictor) before timing.
for ($i = 0; $i < max(1, intdiv($K, 5)); ++$i) {
    $a_op();
    $b_op();
}

$a_times = [];
$b_times = [];
$ratios = [];
for ($rep = 0; $rep < $R; ++$rep) {
    if ($rep & 1) {
        $b = time_op($b_op, $K);
        $a = time_op($a_op, $K);
    } else {
        $a = time_op($a_op, $K);
        $b = time_op($b_op, $K);
    }
    $a_times[] = $a;
    $b_times[] = $b;
    $ratios[] = $b / $a;
}
sort($a_times);
sort($b_times);
sort($ratios);

$median = fn (array $x) => $x[intdiv(count($x), 2)];
printf(
    "%s N=%d S=%d K=%d R=%d: %s %.1f ns, %s %.1f ns, %s/%s ratio median %.2fx (min %.2f max %.2f)\n",
    $pair,
    $N,
    $S,
    $K,
    $R,
    $a_name,
    $median($a_times),
    $b_name,
    $median($b_times),
    $b_name,
    $a_name,
    $median($ratios),
    $ratios[0],
    $ratios[count($ratios) - 1]
);
