<?php

/*
 * Build-independent correctness check for strpos / str_contains / strrpos.
 * Reference: a naive byte-by-byte search in PHP (substr_compare at a fixed offset uses
 * memcmp, not the substring-search engine, so it does not exercise zend_memnstr).
 * Fuzzes needle/haystack over small and binary alphabets, lengths that straddle the SIMD
 * block and the length-9 / 1024 thresholds, needles present at every position and absent.
 *
 * Usage: php verify.php [count] [seed]  — exits non-zero on any mismatch.
 */

function naive_strpos(string $h, string $n, int $off = 0): int|false
{
    $hl = strlen($h);
    $nl = strlen($n);
    if (0 === $nl) {
        return $off <= $hl ? $off : false; // PHP: "" matches at the offset
    }
    for ($i = $off; $i + $nl <= $hl; ++$i) {
        if (0 === substr_compare($h, $n, $i, $nl)) {
            return $i;
        }
    }

    return false;
}

function naive_strrpos(string $h, string $n): int|false
{
    $hl = strlen($h);
    $nl = strlen($n);
    if (0 === $nl) {
        return $hl;
    }
    for ($i = $hl - $nl; $i >= 0; --$i) {
        if (0 === substr_compare($h, $n, $i, $nl)) {
            return $i;
        }
    }

    return false;
}

function rand_str(int $len, array $alphabet): string
{
    $n = count($alphabet);
    $s = '';
    for ($i = 0; $i < $len; ++$i) {
        $s .= $alphabet[mt_rand(0, $n - 1)];
    }

    return $s;
}

$count = (int) ($argv[1] ?? 200000);
$seed = (int) ($argv[2] ?? 1);
mt_srand($seed);

// Alphabets: tiny (forces overlaps and many partial matches), ascii words, full binary.
$alphabets = [
    ['a', 'b'],
    ['a', 'b', 'c'],
    str_split('wordx 0123'),
    array_map('chr', [0, 1, 2, 127, 128, 200, 255, ord('a'), ord('b')]),
    array_map('chr', range(0, 255)),
];

$fail = 0;
$checked = 0;

for ($t = 0; $t < $count; ++$t) {
    $alpha = $alphabets[mt_rand(0, count($alphabets) - 1)];

    // Haystack length: mostly small, sometimes across the SIMD block and the 1024 threshold.
    $hl = match (mt_rand(0, 9)) {
        0, 1, 2, 3 => mt_rand(0, 40),
        4, 5, 6 => mt_rand(0, 300),
        7, 8 => mt_rand(1000, 1100),
        default => mt_rand(1, 4096),
    };
    $h = rand_str($hl, $alpha);

    // Needle: sometimes a real substring of the haystack (present), sometimes independent.
    if ($hl > 0 && mt_rand(0, 1)) {
        $start = mt_rand(0, $hl - 1);
        $maxlen = $hl - $start;
        $n = substr($h, $start, mt_rand(1, min($maxlen, 40)));
    } else {
        $n = rand_str(mt_rand(0, 20), $alpha);
    }

    $off = $hl > 0 ? mt_rand(0, $hl) : 0;

    $got = strpos($h, $n, $off);
    $want = naive_strpos($h, $n, $off);
    if ($got !== $want) {
        ++$fail;
        if ($fail <= 10) {
            printf(
                "strpos DIFF: h=%s n=%s off=%d got=%s want=%s\n",
                var_export($h, true),
                var_export($n, true),
                $off,
                var_export($got, true),
                var_export($want, true)
            );
        }
    }

    // str_contains and strrpos on the same inputs (no offset).
    if (str_contains($h, $n) !== (false !== naive_strpos($h, $n, 0))) {
        ++$fail;
    }
    if (strrpos($h, $n) !== naive_strrpos($h, $n)) {
        ++$fail;
    }
    ++$checked;
}

printf("checked %d cases over %d alphabets\n", $checked, count($alphabets));
echo $fail ? "\nFAILED ({$fail})\n" : "\nALL OK\n";

exit($fail ? 1 : 0);
