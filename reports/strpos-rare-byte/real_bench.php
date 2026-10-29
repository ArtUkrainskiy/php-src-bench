<?php

/*
 * Load a corpus file as the haystack and run K searches for a needle (base64-encoded on
 * the command line so odd bytes survive the shell). Cycles/call come from perf (K minus 0).
 *
 * Usage: real_bench.php <mode> <corpus> <needle_b64> <K>
 *   mode: strpos | contains | preg
 */

$mode = $argv[1] ?? 'strpos';
$corpus = $argv[2] ?? '';
$needle = base64_decode($argv[3] ?? '');
$K = (int) ($argv[4] ?? 0);

$h = file_get_contents($corpus);
$pat = '/'.preg_quote($needle, '/').'/';
$sink = 0;

switch ($mode) {
    case 'strpos':
        for ($i = 0; $i < $K; ++$i) {
            $sink += false === strpos($h, $needle) ? 0 : 1;
        }

        break;

    case 'contains':
        for ($i = 0; $i < $K; ++$i) {
            $sink += str_contains($h, $needle) ? 1 : 0;
        }

        break;

    case 'preg':
        for ($i = 0; $i < $K; ++$i) {
            $sink += preg_match($pat, $h);
        }

        break;

    default:
        fwrite(STDERR, "bad mode\n");

        exit(2);
}

echo $sink, "\n";
