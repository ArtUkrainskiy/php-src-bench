<?php

use Str\Replacer;

/*
 * Correctness of Str\Replacer::replace against strtr (same semantics: longest key first,
 * left to right, non-overlapping, no rescan of the inserted text).
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

$fail = 0;

function check(string $label, array $map, string $text): void
{
    global $fail;

    $r = new Replacer($map);
    $count = 0;
    $got = $r->replace($text, $count);
    $want = strtr($text, $map);
    $ok = ($got === $want);
    if (!$ok) {
        ++$fail;
    }
    printf("  %-28s %s  (count=%d, len %d->%d)\n", $label, $ok ? 'OK' : 'DIFF', $count, strlen($text), strlen($got));

    if (!$ok) {
        // Show the first byte where the two outputs diverge.
        $n = min(strlen($got), strlen($want));
        for ($i = 0; $i < $n; ++$i) {
            if ($got[$i] !== $want[$i]) {
                break;
            }
        }
        printf(
            "     diverge at %d: got=%s want=%s\n",
            $i,
            var_export(substr($got, $i, 20), true),
            var_export(substr($want, $i, 20), true)
        );
    }
}

echo "hand-crafted edge cases:\n";
check('overlap he/she/hers', ['he' => '[HE]', 'she' => '[SHE]', 'hers' => '[HERS]'], 'ushers shelter here, hers');
check('prefix ab/abc/abcd', ['ab' => 'X', 'abc' => 'YY', 'abcd' => 'ZZZ'], 'abcde ab abc abcd abx');
check('empty replacement', ['foo' => '', 'bar' => '!'], 'foobar foo bar barfoo');
check('replacement contains key', ['cat' => 'cats', 's' => 'S'], 'cat cats scat'); // no rescan: cat -> cats, the new s stays
check('longer replacement', ['a' => 'AAAA'], 'banana');
check('adjacent keys', ['ab' => '1', 'cd' => '2'], 'abcdabcd');
check('no match', ['xyz' => 'Q'], 'hello world');
check('whole string is key', ['hello' => 'bye'], 'hello');

echo "\nrandom dicts vs strtr:\n";
foreach ([[50, 4096, 1], [500, 16384, 1], [2000, 32768, 7], [500, 16384, 42]] as [$N, $S, $seed]) {
    $dict = gen_dict($N, $seed);
    $map = [];
    foreach ($dict as $i => $w) {
        $map[$w] = '<'.($i % 7).'>'; // varied-length replacements
    }
    $text = gen_text($S, $dict, $seed);
    check("N={$N} S={$S} seed={$seed}", $map, $text);
}

echo $fail ? "\nFAILED ({$fail})\n" : "\nALL OK\n";

exit($fail ? 1 : 0);
