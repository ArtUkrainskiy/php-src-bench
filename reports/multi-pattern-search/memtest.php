<?php

use Str\Matcher;
use Str\Replacer;

/*
 * Memory of the prepared automaton and the transient per-call scratch.
 *   automaton: VmRSS delta (resident, page-granular) plus the Zend-heap delta (precise;
 *     the buffers are emalloc'd). Run one N per process for a clean before/after delta.
 *   per-call scratch (emalloc'd best[] / hits): memory_get_peak_usage around the call
 *     after memory_reset_peak_usage (PHP 8.2+). VmHWM is the process lifetime maximum,
 *     so it would not show a call peak below an earlier one, and is not used here.
 *
 * Usage: php -dextension=strmatch.so memtest.php <N> <S> [seed]
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

// One field from /proc/self/status, in KB.
function status_kb(string $field): int
{
    foreach (file('/proc/self/status') as $line) {
        if (0 === strncmp($line, $field.':', strlen($field) + 1)) {
            return (int) preg_replace('/\D/', '', $line);
        }
    }

    return 0;
}

$N = (int) ($argv[1] ?? 5000);
$S = (int) ($argv[2] ?? 65536);
$seed = (int) ($argv[3] ?? 1);

$dict = gen_dict($N, $seed);
$text = gen_text($S, $dict, $seed);

$total_bytes = 0;
foreach ($dict as $w) {
    $total_bytes += strlen($w);
}

$rss0 = status_kb('VmRSS');
$heap0 = memory_get_usage();
$m = new Matcher($dict);
$rss1 = status_kb('VmRSS');
$heap1 = memory_get_usage();
printf(
    "automaton: RSS +%d KB, Zend heap +%d KB  (N=%d, %d keyword bytes => %.0f B/keyword-byte RSS)\n",
    $rss1 - $rss0,
    intdiv($heap1 - $heap0, 1024),
    $N,
    $total_bytes,
    ($rss1 - $rss0) * 1024.0 / max(1, $total_bytes)
);

memory_reset_peak_usage();
$base = memory_get_usage();
$res = $m->matchAll($text);
printf(
    "matchAll transient Zend-heap peak: ~%d KB (text %d KB, %d matches)\n",
    intdiv(memory_get_peak_usage() - $base, 1024),
    intdiv($S, 1024),
    count($res)
);
unset($res);

$map = [];
foreach ($dict as $w) {
    $map[$w] = 'X';
}
$replacer = new Replacer($map);
memory_reset_peak_usage();
$base = memory_get_usage();
$out = $replacer->replace($text);
printf(
    "replace transient Zend-heap peak: ~%d KB (best[] ~ 4 bytes/subject byte = %d KB)\n",
    intdiv(memory_get_peak_usage() - $base, 1024),
    intdiv($S * 4, 1024)
);
