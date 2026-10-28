<?php
/* Adversarial-dictionary worst case for Aho-Corasick output: dict {a, aa, ..., a^k}
 * over subject a^n. Keyword a^j occurs (n-j+1) times, so total occurrences ~ O(n*k).
 * This is where "O(subject)" stops holding: count/matchAll walk the out_link chain on
 * every position. replace is immune (best[] keeps one keyword per start position).
 *
 * Usage: php -dextension=strmatch.so worstbench.php <mode> <K_depth> <N_len> <REP>
 *   mode: count | matchall | replace | matches
 */

$mode = $argv[1] ?? 'count';
$kd   = (int)($argv[2] ?? 10);   // dictionary depth: a, aa, ..., a^kd
$n    = (int)($argv[3] ?? 1000); // subject length
$rep  = (int)($argv[4] ?? 0);

$dict = [];
for ($j = 1; $j <= $kd; $j++) $dict[] = str_repeat('a', $j);
$text = str_repeat('a', $n);

$sink = 0;
if ($mode === 'replace') {
    $map = [];
    foreach ($dict as $w) $map[$w] = 'X'; // all map to one char
    $r = new Str\Replacer($map);
    for ($i = 0; $i < $rep; $i++) $sink += strlen($r->replace($text));
} else {
    $m = new Str\Matcher($dict);
    switch ($mode) {
        case 'count':    for ($i = 0; $i < $rep; $i++) $sink += $m->countMatches($text); break;
        case 'matchall': for ($i = 0; $i < $rep; $i++) $sink += count($m->matchAll($text)); break;
        case 'matches':  for ($i = 0; $i < $rep; $i++) $sink += $m->matches($text) ? 1 : 0; break;
        default: fwrite(STDERR, "unknown mode\n"); exit(2);
    }
}
echo $sink, "\n";
