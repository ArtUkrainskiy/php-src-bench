<?php

/*
 * One literal needle: strpos / str_contains / preg_match on a subject. Cycles/instructions
 * come from perf outside (per-call = K minus K=0). The subject is random "wordN " tokens
 * (alphabet w,o,r,d,space,0-9), so a needle byte is "common" if it is one of those and
 * "rare" otherwise. The needle is passed in, so the caller controls first/last byte class.
 *
 * Usage: needle_bench.php <mode> <S> <K> <pos> <needle> [seed]
 *   mode: strpos | contains | preg
 *   pos:  start | end | absent   (start = early exit; end/absent = full scan)
 */

$mode = $argv[1] ?? 'strpos';
$S = (int) ($argv[2] ?? 16384);
$K = (int) ($argv[3] ?? 0);
$pos = $argv[4] ?? 'absent';
$needle = $argv[5] ?? 'zqxjkvy';
$seed = (int) ($argv[6] ?? 1);

mt_srand($seed);
$out = '';
while (strlen($out) < $S) {
    $out .= 'word'.mt_rand(0, 9).' ';
}
$subject = substr($out, 0, $S);

$nl = strlen($needle);
if ('start' === $pos) {
    $subject = $needle.substr($subject, $nl);
} elseif ('end' === $pos) {
    $subject = substr($subject, 0, $S - $nl).$needle;
}
// 'absent': the needle (rare bytes) never occurs in the random text.

$pat = '/'.preg_quote($needle, '/').'/';
$sink = 0;

switch ($mode) {
    case 'strpos':
        for ($i = 0; $i < $K; ++$i) {
            $sink += false === strpos($subject, $needle) ? 0 : 1;
        }

        break;

    case 'contains':
        for ($i = 0; $i < $K; ++$i) {
            $sink += str_contains($subject, $needle) ? 1 : 0;
        }

        break;

    case 'preg':
        for ($i = 0; $i < $K; ++$i) {
            $sink += preg_match($pat, $subject);
        }

        break;

    default:
        fwrite(STDERR, "bad mode\n");

        exit(2);
}

echo $sink, "\n";
