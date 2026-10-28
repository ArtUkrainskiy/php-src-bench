<?php
/* Correctness check for the rich Str\Matcher API against the strpos oracle.
 * Usage: php -dextension=.../strmatch.so verify.php <N> <S> [seed] */

function gen_dict(int $n, int $seed): array {
    mt_srand($seed);
    $words = []; $seen = [];
    while (count($words) < $n) {
        $len = mt_rand(4, 12); $w = '';
        for ($i = 0; $i < $len; $i++) $w .= chr(mt_rand(97, 122));
        if (isset($seen[$w])) continue;
        $seen[$w] = true; $words[] = $w;
    }
    return $words;
}
function gen_text(int $bytes, array $dict, int $seed): string {
    mt_srand($seed ^ 0x5a5a);
    $n = count($dict); $out = '';
    while (strlen($out) < $bytes) {
        if (mt_rand(0, 99) < 8) { $out .= $dict[mt_rand(0, $n - 1)] . ' '; }
        else { $len = mt_rand(2, 10); for ($i = 0; $i < $len; $i++) $out .= chr(mt_rand(97, 122)); $out .= ' '; }
    }
    return substr($out, 0, $bytes);
}

$N = (int)($argv[1] ?? 500);
$S = (int)($argv[2] ?? 16384);
$seed = (int)($argv[3] ?? 1);

$dict = gen_dict($N, $seed);
$text = gen_text($S, $dict, $seed);

$m = new Str\Matcher($dict);

/* oracle: which dict words occur */
$oracle = [];
foreach ($dict as $w) if (str_contains($text, $w)) $oracle[] = $w;
sort($oracle);

/* getMatchedKeywords: set equality (sorted) ... */
$got_raw = $m->getMatchedKeywords($text);
$got = $got_raw; sort($got);
$ok_kw = ($oracle === $got);

/* ... and the claimed first-occurrence order, on the UNSORTED list. AC emits at the
   end of a keyword, so first-occurrence end positions must be non-decreasing. */
$ok_order = true; $prevEnd = -1;
foreach ($got_raw as $kw) {
    $end = strpos($text, $kw) + strlen($kw) - 1;
    if ($end < $prevEnd) { $ok_order = false; break; }
    $prevEnd = $end;
}

/* matches(): present case, and a deterministic no-match case (uppercase text can
   never match the lowercase dict) — this one must be able to fail. */
$ok_matches = ($m->matches($text) === (count($oracle) > 0));
$ok_matches_miss = ($m->matches(strtoupper($text)) === false);

/* independent occurrence-count oracle: count every (overlapping) occurrence of each
   keyword with a strpos walk; must equal countMatches (not matchAll against itself). */
$cnt_oracle = 0;
foreach ($dict as $w) { $off = 0; while (($p = strpos($text, $w, $off)) !== false) { $cnt_oracle++; $off = $p + 1; } }

/* matchAll: every MatchResult must be a real occurrence, count == countMatches == oracle,
   offsets ascending, substr matches keyword, length == strlen(keyword) */
$all = $m->matchAll($text);
$cnt = $m->countMatches($text);
$ok_count = (count($all) === $cnt) && ($cnt === $cnt_oracle);
$ok_occ = true; $prev = -1;
foreach ($all as $r) {
    if (!($r instanceof Str\MatchResult)) { $ok_occ = false; break; }
    if ($r->offset < $prev) { $ok_occ = false; break; }   // non-decreasing offset
    $prev = $r->offset;
    if ($r->length !== strlen($r->keyword)) { $ok_occ = false; break; }
    if (substr($text, $r->offset, $r->length) !== $r->keyword) { $ok_occ = false; break; }
}

/* distinct keywords from matchAll must equal getMatchedKeywords set */
$distinct = [];
foreach ($all as $r) $distinct[$r->keyword] = true;
$distinct = array_keys($distinct); sort($distinct);
$ok_distinct = ($distinct === $oracle);

/* getKeywords returns the full normalized dict */
$kws = $m->getKeywords(); sort($kws);
$dsort = $dict; sort($dsort);
$ok_getkw = ($kws === $dsort);

printf("N=%d S=%d oracle=%d allOcc=%d count=%d cntOracle=%d\n", $N, $S, count($oracle), count($all), $cnt, $cnt_oracle);
printf("  getMatchedKeywords == oracle : %s\n", $ok_kw ? 'OK' : 'DIFF');
printf("  getMatchedKeywords order     : %s\n", $ok_order ? 'OK' : 'DIFF');
printf("  matches() presence           : %s\n", $ok_matches ? 'OK' : 'DIFF');
printf("  matches() no-match           : %s\n", $ok_matches_miss ? 'OK' : 'DIFF');
printf("  count == independent oracle  : %s\n", $ok_count ? 'OK' : 'DIFF');
printf("  matchAll occurrences valid   : %s\n", $ok_occ ? 'OK' : 'DIFF');
printf("  matchAll distinct == oracle  : %s\n", $ok_distinct ? 'OK' : 'DIFF');
printf("  getKeywords == dict          : %s\n", $ok_getkw ? 'OK' : 'DIFF');

exit(($ok_kw && $ok_order && $ok_matches && $ok_matches_miss && $ok_count && $ok_occ && $ok_distinct && $ok_getkw) ? 0 : 1);
