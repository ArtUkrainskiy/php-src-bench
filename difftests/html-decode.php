<?php
/*
 * Differential test for html_entity_decode() and htmlspecialchars_decode().
 *
 *   bench difftest html-decode base dev --seed 1 --count 20000
 *
 * Every input goes through htmlspecialchars_decode() with 10 flag sets and through
 * html_entity_decode() with the same flag sets and 12 charsets. To see one input in full:
 *
 *   php -n difftests/html-decode.php --seed 1 --count 20000 --dump 1234
 */
require dirname(__DIR__) . '/lib/difftest.php';

const SINGLE_BYTES = [
    '&', '&', '&', '&', ';', ';', ';', '#', '#', 'x', 'X', '0', '1', '9', 'a', 'f', 'F', 'g', 'A', 'Z', 'q',
    ' ', ' ', '<', '>', '"', "'", "\n", '=', '@', '[', '`', '{', '/', '.', "\0",
    "\x80", "\xC3", "\xA9", "\xE2", "\x81", "\xFF", "\xA0",
];
// Valid entities of every kind, then everything that only looks like one.
const TOKENS = [
    '&amp;', '&AMP;', '&Amp;', '&lt;', '&gt;', '&quot;', '&apos;', '&#39;', '&#039;', '&#x27;', '&#X27;',
    '&#34;', '&#38;', '&#60;', '&#62;', '&nGt;', '&nLt;', '&hellip;', '&nbsp;', '&euro;', '&Aacute;', '&aacute;',
    '&Tab;', '&fjlig;', '&CounterClockwiseContourIntegral;', '&NotNestedGreaterGreater;', '&#x10FFFF;',
    '&#1114111;', '&#1114112;', '&#x110000;', '&#0;', '&#13;', '&#x0D;', '&#xD800;', '&#xFFFE;', '&#x1;',
    '&#x9;', '&#128;', '&#x80;', '&#160;', '&#x41;', '&#65;', '&#x00000000000000000000000041;',
    '&#0000000000000000000000000000065;', '&#x0x41;', '&#xx41;', '&#x;', '&#;', '&;', '&', '&&', '&&amp;',
    '&amp', '&am;', '&a;', '&abcdefghijklmnopqrstuvwxyzabcde;', '&abcdefghijklmnopqrstuvwxyzabcdef;',
    '&#65', '&#x41', '&lt', '&#-1;', '&#+1;', '&# 1;', '&#1 ;', '&#99999999999999999999;', '&#x7FFFFFFFFFFFFFFF;',
    '&#9223372036854775808;', '&a#b;', '&#a;', '&x41;', '&#xg;', '&#x4G;',
];
const FLAG_SETS = [
    'quotes|401' => ENT_QUOTES | ENT_SUBSTITUTE | ENT_HTML401,
    'compat|401' => ENT_COMPAT | ENT_HTML401,
    'noquotes|401' => ENT_NOQUOTES | ENT_HTML401,
    'quotes|html5' => ENT_QUOTES | ENT_HTML5,
    'compat|html5' => ENT_COMPAT | ENT_HTML5,
    'quotes|xhtml' => ENT_QUOTES | ENT_XHTML,
    'noquotes|xhtml' => ENT_NOQUOTES | ENT_XHTML,
    'quotes|xml1' => ENT_QUOTES | ENT_XML1,
    'quotes|401|disallowed' => ENT_QUOTES | ENT_HTML401 | ENT_DISALLOWED,
    'quotes|html5|ignore' => ENT_QUOTES | ENT_HTML5 | ENT_IGNORE,
];
const CHARSETS = ['UTF-8', 'ISO-8859-1', 'ISO-8859-15', 'cp1251', 'cp1252', 'KOI8-R', 'Shift_JIS', 'BIG5', 'EUC-JP', 'GB2312', 'MacRoman', 'cp866'];

function generate(DifftestRng $rng): string
{
    $roll = $rng->next(100);
    if ($roll < 3) {
        // one short piece repeated: dense input
        return str_repeat($rng->pick(['&', '&amp;', '&#39;', '&;', '&a', 'a;', '&#', '&lt;&gt;']), 1 + $rng->next(1500));
    }
    if ($roll < 5) {
        // an entity start followed by a very long name or number
        $run = str_repeat($rng->pick(['a', '0', 'Z', '#']), $rng->next(3000));
        return $rng->pick(['&', '&#', '&#x']) . $run . $rng->pick(['', ';', '5;']);
    }
    // Mostly short; some lengths around multiples of 64 for block boundaries; a few long ones.
    if ($roll < 13) {
        $length = max(0, 64 * $rng->next(5) + $rng->next(7) - 3);
    } elseif ($roll < 15) {
        $length = 1000 + $rng->next(4000);
    } else {
        $length = $rng->next(200);
    }
    $input = '';
    while (strlen($input) < $length) {
        $input .= $rng->chance(30) ? $rng->pick(TOKENS) : $rng->pick(SINGLE_BYTES);
    }
    return $input;
}

function outputs(string $input): Generator
{
    foreach (FLAG_SETS as $flagName => $flags) {
        yield "htmlspecialchars_decode $flagName" => htmlspecialchars_decode($input, $flags);
        foreach (CHARSETS as $charset) {
            yield "html_entity_decode $flagName $charset" => html_entity_decode($input, $flags, $charset);
        }
    }
}

difftest_run($argv, 'generate', 'outputs');
