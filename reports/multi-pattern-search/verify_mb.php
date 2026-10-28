<?php

use Str\Matcher;
use Str\Replacer;

/*
 * Multibyte / multilingual / binary correctness for Str\Matcher and Str\Replacer.
 * Byte-based Aho-Corasick on valid UTF-8 is character-correct by construction; this
 * proves it against the str_contains / strtr oracles, byte for byte, balanced across
 * languages. Also: binary bytes, embedded NUL, NFC vs NFD (must NOT match), byte offsets.
 */

$fail = 0;

function chk(string $label, bool $ok): void
{
    global $fail;
    if (!$ok) {
        ++$fail;
    }
    printf("  %-44s %s\n", $label, $ok ? 'OK' : 'FAIL');
}

// Matcher vs oracle for a given dictionary + subject.
function check_matcher(string $label, array $dict, string $text): void
{
    $m = new Matcher($dict);

    // Presence oracle.
    $oracle = [];
    foreach (array_unique($dict) as $w) {
        if ('' !== $w && str_contains($text, $w)) {
            $oracle[] = $w;
        }
    }
    sort($oracle);
    $got = $m->getMatchedKeywords($text);
    sort($got);
    chk("{$label}: getMatchedKeywords == oracle", $oracle === $got);

    // Independent overlapping occurrence count.
    $cnt = 0;
    foreach (array_unique($dict) as $w) {
        if ('' === $w) {
            continue;
        }
        $o = 0;
        while (($p = strpos($text, $w, $o)) !== false) {
            ++$cnt;
            $o = $p + 1;
        }
    }
    chk("{$label}: countMatches == strpos oracle", $m->countMatches($text) === $cnt);

    // Every MatchResult is a real byte-offset occurrence.
    $all = $m->matchAll($text);
    $occ_ok = (count($all) === $cnt);
    $prev = -1;
    foreach ($all as $r) {
        if ($r->length !== strlen($r->keyword)) {
            $occ_ok = false;

            break;
        }
        if (substr($text, $r->offset, $r->length) !== $r->keyword) {
            $occ_ok = false;

            break;
        }
        if ($r->offset < $prev) {
            $occ_ok = false;

            break;
        }
        $prev = $r->offset;
    }
    chk("{$label}: matchAll byte-offsets valid", $occ_ok);
}

// Replacer vs strtr.
function check_replacer(string $label, array $map, string $text): void
{
    $r = new Replacer($map);
    chk("{$label}: replace == strtr", $r->replace($text) === strtr($text, $map));
}

// Balanced language keyword sets (UTF-8).
$langs = [
    'en' => ['hello', 'world'],
    'es' => ['cañón', 'niño'],          // Latin + diacritics
    'ru' => ['привет', 'мир'],          // Cyrillic
    'zh' => ['世界', '你好'],             // Han
    'ja' => ['日本', 'こんにちは'],        // Kana + Kanji
    'ko' => ['안녕', '세계'],             // Hangul
    'emoji' => ['😀', '👍🏽'],            // emoji incl. skin-tone modifier
];

$dict = [];
foreach ($langs as $ws) {
    foreach ($ws as $w) {
        $dict[] = $w;
    }
}

// Subject: each keyword embedded twice, surrounded by multilingual noise.
$noise = 'quick коричневая 狐 が тест test ∑≠ 가나 ❤ ';
$text = '';
foreach ($dict as $w) {
    $text .= $noise.$w.' middle '.$w.' ';
}
$text .= $noise;

echo "multilingual (balanced: en/es/ru/zh/ja/ko/emoji):\n";
check_matcher('ml all', $dict, $text);
$map = [];
foreach ($dict as $i => $w) {
    $map[$w] = '['.$i.']';
}
check_replacer('ml all', $map, $text);

// Per-language isolation (each language alone).
foreach ($langs as $lang => $ws) {
    $t = '';
    foreach ($ws as $w) {
        $t .= "xx {$w} yy {$w} zz ";
    }
    check_matcher("only {$lang}", $ws, $t);
}

echo "binary / embedded NUL:\n";
$bin = ["\xff\x00\xfe", "\x80\x81", "\xC3\x28"]; // high bytes, NUL, invalid-UTF8 bytes
$bt = "head\xff\x00\xfemid\x80\x81tail\xC3\x28end\xff\x00\xfe";
check_matcher('binary', $bin, $bt);
check_replacer('binary', ["\xff\x00\xfe" => 'R1', "\x80\x81" => 'R2'], $bt);

echo "NFC vs NFD (must NOT match — different bytes):\n";
$nfc = "\u{00E9}";   // é as one code point (C3 A9)
$nfd = "e\u{0301}";  // e + combining acute (65 CC 81)
$mm = new Matcher([$nfc]);
chk('NFC keyword vs NFD text: no match', false === $mm->matches($nfd));
chk('NFC keyword vs NFC text: match', true === $mm->matches('caf'.$nfc));
chk('byte lengths differ (2 vs 3)', 2 === strlen($nfc) && 3 === strlen($nfd));

echo "char-boundary safety (a substring of a multibyte char must not false-match):\n";
// 世 = E4 B8 96, 界 = E7 95 8C. A real character keyword must hit only whole characters.
$cb = new Matcher(['世界']);
$subject = 'a世界b世c世界';
$all = $cb->matchAll($subject);
$cb_ok = true;
foreach ($all as $r) {
    if ('世界' !== substr($subject, $r->offset, $r->length)) {
        $cb_ok = false;
    }
}
chk('世界 matches only whole sequence', $cb_ok && 2 === count($all));

echo $fail ? "\nFAILED ({$fail})\n" : "\nALL OK\n";

exit($fail ? 1 : 0);
