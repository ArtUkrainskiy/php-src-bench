<?php

use Str\Matcher;
use Str\MatchResult;

/*
 * Correctness check for the Str\Matcher API against the str_contains oracle.
 * Usage: php -dextension=.../strmatch.so verify.php <N> <S> [seed]
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

$N = (int) ($argv[1] ?? 500);
$S = (int) ($argv[2] ?? 16384);
$seed = (int) ($argv[3] ?? 1);

$dict = gen_dict($N, $seed);
$text = gen_text($S, $dict, $seed);
$m = new Matcher($dict);

// Oracle: which dictionary words occur (presence set).
$oracle = [];
foreach ($dict as $w) {
    if (str_contains($text, $w)) {
        $oracle[] = $w;
    }
}
sort($oracle);

// getMatchedKeywords: set equality (sorted).
$got_raw = $m->getMatchedKeywords($text);
$got = $got_raw;
sort($got);
$ok_kw = ($oracle === $got);

// ... and the documented order on the unsorted list: by first start offset, ties by length.
$ok_order = true;
$prev = [-1, -1];
foreach ($got_raw as $kw) {
    $cur = [strpos($text, $kw), strlen($kw)];
    if ($cur < $prev) {
        $ok_order = false;

        break;
    }
    $prev = $cur;
}

// matches(): present case, and a deterministic no-match case (uppercase text can
// never match the lowercase dictionary) so the check can actually fail.
$ok_matches = ($m->matches($text) === (count($oracle) > 0));
$ok_matches_miss = (false === $m->matches(strtoupper($text)));

// Independent occurrence-count oracle: count every (overlapping) occurrence of each
// keyword with a strpos walk; must equal countMatches.
$cnt_oracle = 0;
foreach ($dict as $w) {
    $off = 0;
    while (($p = strpos($text, $w, $off)) !== false) {
        ++$cnt_oracle;
        $off = $p + 1;
    }
}

$all = $m->matchAll($text);
$cnt = $m->countMatches($text);
$ok_count = (count($all) === $cnt) && ($cnt === $cnt_oracle);

// Every MatchResult is a real occurrence: non-decreasing offset, length == strlen(keyword),
// substr(text, offset, length) === keyword.
$ok_occ = true;
$prev = -1;
foreach ($all as $r) {
    if (!$r instanceof MatchResult) {
        $ok_occ = false;

        break;
    }
    if ($r->offset < $prev) {
        $ok_occ = false;

        break;
    }
    $prev = $r->offset;
    if ($r->length !== strlen($r->keyword)) {
        $ok_occ = false;

        break;
    }
    if (substr($text, $r->offset, $r->length) !== $r->keyword) {
        $ok_occ = false;

        break;
    }
}

// Distinct keywords from matchAll must equal the getMatchedKeywords set.
$distinct = [];
foreach ($all as $r) {
    $distinct[$r->keyword] = true;
}
$distinct = array_keys($distinct);
sort($distinct);
$ok_distinct = ($distinct === $oracle);

// Independent full oracle for matchAll: strpos-walk every keyword into
// (offset, length, keyword); the sorted set must equal matchAll's. Catches a
// duplicate-plus-miss that the count check alone would pass.
$oracle_all = [];
foreach ($dict as $w) {
    $o = 0;
    while (($p = strpos($text, $w, $o)) !== false) {
        $oracle_all[] = [$p, strlen($w), $w];
        $o = $p + 1;
    }
}
usort($oracle_all, fn ($a, $b) => $a <=> $b);

$got_all = [];
foreach ($all as $r) {
    $got_all[] = [$r->offset, $r->length, $r->keyword];
}
$got_all_sorted = $got_all;
usort($got_all_sorted, fn ($a, $b) => $a <=> $b);
$ok_matchall = ($got_all_sorted === $oracle_all);

// matchAll must already be in that order (ascending offset, ties by length):
// the unsorted result must equal the sorted oracle.
$ok_matchall_order = ($got_all === $oracle_all);

// getKeywords returns the full normalized dictionary.
$kws = $m->getKeywords();
sort($kws);
$dsort = $dict;
sort($dsort);
$ok_getkw = ($kws === $dsort);

printf("N=%d S=%d oracle=%d allOcc=%d count=%d cntOracle=%d\n", $N, $S, count($oracle), count($all), $cnt, $cnt_oracle);
printf("  getMatchedKeywords == oracle : %s\n", $ok_kw ? 'OK' : 'DIFF');
printf("  getMatchedKeywords order     : %s\n", $ok_order ? 'OK' : 'DIFF');
printf("  matches() presence           : %s\n", $ok_matches ? 'OK' : 'DIFF');
printf("  matches() no-match           : %s\n", $ok_matches_miss ? 'OK' : 'DIFF');
printf("  count == independent oracle  : %s\n", $ok_count ? 'OK' : 'DIFF');
printf("  matchAll occurrences valid   : %s\n", $ok_occ ? 'OK' : 'DIFF');
printf("  matchAll == full oracle      : %s\n", $ok_matchall ? 'OK' : 'DIFF');
printf("  matchAll order (offset,len)  : %s\n", $ok_matchall_order ? 'OK' : 'DIFF');
printf("  matchAll distinct == oracle  : %s\n", $ok_distinct ? 'OK' : 'DIFF');
printf("  getKeywords == dict          : %s\n", $ok_getkw ? 'OK' : 'DIFF');

$all_ok = $ok_kw && $ok_order && $ok_matches && $ok_matches_miss && $ok_count
    && $ok_occ && $ok_matchall && $ok_matchall_order && $ok_distinct && $ok_getkw;

exit($all_ok ? 0 : 1);
