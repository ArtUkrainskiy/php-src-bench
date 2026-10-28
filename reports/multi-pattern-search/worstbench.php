<?php

use Str\Matcher;
use Str\Replacer;

/*
 * Adversarial-dictionary worst case: dict {a, aa, ..., a^k} over subject a^n. Keyword
 * a^j occurs (n - j + 1) times, so the total number of occurrences H is about O(n * k).
 *
 *   matches()             immune: stops at the first hit (here, position 0).
 *   countMatches()        O(subject): sums a precomputed per-state output count.
 *   getMatchedKeywords()  }
 *   matchAll()            } enumerate every occurrence via the out_link chain, so they
 *   replace()             } are output-dependent, O(subject + H); matchAll also sorts.
 *                         replace() is NOT immune: best[] keeps one keyword per start,
 *                         but the fill loop still visits every occurrence.
 *
 * Usage: php -dextension=strmatch.so worstbench.php <mode> <depth> <len> <rep>
 *   mode: count | matchall | replace | matches
 */

$mode = $argv[1] ?? 'count';
$depth = (int) ($argv[2] ?? 10);   // dictionary depth: a, aa, ..., a^depth
$len = (int) ($argv[3] ?? 1000);   // subject length
$rep = (int) ($argv[4] ?? 0);

$dict = [];
for ($j = 1; $j <= $depth; ++$j) {
    $dict[] = str_repeat('a', $j);
}
$text = str_repeat('a', $len);

$sink = 0;

if ('replace' === $mode) {
    $map = [];
    foreach ($dict as $w) {
        $map[$w] = 'X';
    }
    $r = new Replacer($map);
    for ($i = 0; $i < $rep; ++$i) {
        $sink += strlen($r->replace($text));
    }
    echo $sink, "\n";

    return;
}

$m = new Matcher($dict);

switch ($mode) {
    case 'count':
        for ($i = 0; $i < $rep; ++$i) {
            $sink += $m->countMatches($text);
        }

        break;

    case 'matchall':
        for ($i = 0; $i < $rep; ++$i) {
            $sink += count($m->matchAll($text));
        }

        break;

    case 'matches':
        for ($i = 0; $i < $rep; ++$i) {
            $sink += $m->matches($text) ? 1 : 0;
        }

        break;

    default:
        fwrite(STDERR, "unknown mode\n");

        exit(2);
}

echo $sink, "\n";
