<?php
/* Differential fuzzer for PR #24666 (ext/json scan/escape fast paths).
 * Deterministic: same seed => identical inputs on every binary.
 * Prints one md5 per iteration over all json_encode/decode/validate results.
 * Run with base and head binaries, then cmp the two outputs. */

$seed  = (int) ($argv[1] ?? 1);
$count = (int) ($argv[2] ?? 50000);
mt_srand($seed);

/* byte-segment generators, chosen to hit every classification branch */
function seg_ascii_run(): string {        // long plain run (16B chunk logic)
    $n = mt_rand(0, 40); $s = '';
    for ($i = 0; $i < $n; $i++) $s .= chr(mt_rand(0x20, 0x7e));
    return $s;
}
function seg_special(): string {          // bytes the fast paths must stop at
    $c = ['"', '\\', '/', '<', '>', '&', "'", "\n", "\t", "\x00", "\x1f", "\x7f"];
    return $c[mt_rand(0, count($c) - 1)];
}
function seg_utf8_valid(): string {
    switch (mt_rand(0, 3)) {
        case 0: return mb_cp(mt_rand(0x80, 0x7ff));
        case 1: return mb_cp(mt_rand(0x800, 0xffff));   // may include surrogate range -> filtered
        case 2: return mb_cp(mt_rand(0x10000, 0x10ffff));
        default: return mb_cp([0x2028, 0x2029, 0x1f600, 0xe9, 0x20ac][mt_rand(0,4)]);
    }
}
function mb_cp(int $cp): string {          // encode a code point to UTF-8 bytes directly (even surrogates, for fuzzing)
    if ($cp < 0x80)   return chr($cp);
    if ($cp < 0x800)  return chr(0xc0 | ($cp >> 6)) . chr(0x80 | ($cp & 0x3f));
    if ($cp < 0x10000)return chr(0xe0 | ($cp >> 12)) . chr(0x80 | (($cp >> 6) & 0x3f)) . chr(0x80 | ($cp & 0x3f));
    return chr(0xf0 | ($cp >> 18)) . chr(0x80 | (($cp >> 12) & 0x3f)) . chr(0x80 | (($cp >> 6) & 0x3f)) . chr(0x80 | ($cp & 0x3f));
}
function seg_utf8_bad(): string {          // overlong, surrogate, truncated, >10FFFF, lone continuation
    switch (mt_rand(0, 6)) {
        case 0: return "\xc0\x80";                 // overlong 2
        case 1: return "\xe0\x80\x80";             // overlong 3
        case 2: return mb_cp(mt_rand(0xd800, 0xdfff)); // surrogate (3 bytes)
        case 3: return "\xf4\x90\x80\x80";         // U+110000 > max
        case 4: return "\xc2";                     // truncated 2
        case 5: return "\xe2\x82";                 // truncated 3
        default: return chr(mt_rand(0x80, 0xbf));  // lone continuation
    }
}
function seg_esc(): string {               // JSON escape sequences (decode side)
    $e = ['\\"', '\\\\', '\\/', '\\n', '\\t', '\\u00e9', '\\ud83d\\ude00', '\\u0000', '\\uD800'];
    return $e[mt_rand(0, count($e) - 1)];
}

function build_value(): string {           // raw string for json_encode
    $parts = mt_rand(1, 6); $s = '';
    for ($i = 0; $i < $parts; $i++) {
        switch (mt_rand(0, 4)) {
            case 0: $s .= seg_ascii_run(); break;
            case 1: $s .= seg_special(); break;
            case 2: $s .= seg_utf8_valid(); break;
            case 3: $s .= seg_utf8_bad(); break;
            default: $s .= chr(mt_rand(0, 255)); break;
        }
    }
    return $s;
}
function build_doc_body(): string {        // body placed inside "..." for json_decode/validate
    $parts = mt_rand(1, 6); $s = '';
    for ($i = 0; $i < $parts; $i++) {
        switch (mt_rand(0, 5)) {
            case 0: $s .= seg_ascii_run(); break;
            case 1: $s .= seg_esc(); break;
            case 2: $s .= seg_utf8_valid(); break;
            case 3: $s .= seg_utf8_bad(); break;
            case 4: $s .= seg_special(); break;      // may terminate string early (") etc.
            default: $s .= chr(mt_rand(0, 255)); break;
        }
    }
    return $s;
}

$enc_flags = [
    0,
    JSON_UNESCAPED_UNICODE,
    JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_LINE_TERMINATORS,
    JSON_UNESCAPED_SLASHES,
    JSON_HEX_TAG | JSON_HEX_AMP | JSON_HEX_APOS | JSON_HEX_QUOT,
    JSON_INVALID_UTF8_IGNORE,
    JSON_INVALID_UTF8_SUBSTITUTE,
    JSON_UNESCAPED_UNICODE | JSON_INVALID_UTF8_SUBSTITUTE,
    JSON_UNESCAPED_UNICODE | JSON_INVALID_UTF8_IGNORE,
    JSON_PARTIAL_OUTPUT_ON_ERROR | JSON_UNESCAPED_UNICODE,
];
$dec_flags = [0, JSON_INVALID_UTF8_IGNORE, JSON_INVALID_UTF8_SUBSTITUTE, JSON_BIGINT_AS_STRING];

for ($it = 0; $it < $count; $it++) {
    $acc = '';
    $v = build_value();
    foreach ($enc_flags as $f) {
        $r = json_encode($v, $f);
        $acc .= ($r === false ? 'F' : $r) . '|' . json_last_error() . "\x01";
    }
    $doc = '"' . build_doc_body() . '"';
    foreach ($dec_flags as $f) {
        $d = json_decode($doc, true, 512, $f);
        $acc .= serialize($d) . '|' . json_last_error() . "\x01";
    }
    $acc .= (json_validate($doc) ? '1' : '0') . '|' . json_last_error() . "\x01";
    /* also decode a guaranteed-valid document (encoder output) to exercise STR_P1 on real text */
    $doc2 = json_encode($v, JSON_UNESCAPED_UNICODE);
    if ($doc2 !== false) {
        $d2 = json_decode($doc2, true);
        $acc .= serialize($d2) . '|' . json_last_error() . "\x01";
    }
    echo $it, ':', md5($acc), "\n";
}
