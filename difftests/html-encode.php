<?php
/*
 * Differential test for htmlspecialchars() and htmlentities().
 *
 *   bench difftest html-encode base dev --seed 1 --count 20000
 *
 * Every input goes through both functions with 13 flag sets, 14 charsets and double_encode on
 * and off. To see one input in full:
 *
 *   php -n difftests/html-encode.php --seed 1 --count 20000 --dump 1234
 */
require dirname(__DIR__) . '/lib/difftest.php';

const SPECIAL = ['&', '"', "'", '<', '>'];
const PLAIN = ['a', 'z', 'A', 'Z', '0', '9', ' ', ' ', "\n", "\t", '!', '#', '%', '(', '=', ';', '?', '@', '[', '\\', '`', '{', '~', '/'];
// Neighbours of the escaped bytes, control characters and bytes around 0x80.
const EDGE = ["\0", "\x01", "\x08", "\x0B", "\x0C", "\r", "\x1F", "\x21", "\x23", "\x25", "\x28", "\x3B", "\x3D", "\x3F", "\x7E", "\x7F", "\x80", "\x81"];
const MULTIBYTE = [
    "\xC3\xA9", "\xD0\x96", "\xE2\x82\xAC", "\xE4\xB8\xAD", "\xF0\x9F\x98\x80", "\xC2\xA0", "\xEF\xBF\xBD", "\xEF\xBB\xBF",
    // invalid or truncated UTF-8
    "\xC3", "\xE2\x82", "\xF0\x9F\x98", "\xC0\xAF", "\xED\xA0\x80", "\xF4\x90\x80\x80", "\xFF", "\xFE", "\x80", "\xBF", "\xC3\x28", "\xE2\x28\xA1",
    // lead and trail bytes of Shift_JIS, Big5, EUC-JP, GB2312, including trail bytes in the ASCII range
    "\x83\x41", "\x83\x5C", "\x81\x26", "\x81\x3C", "\x95\x22", "\xA4\x40", "\xA4\x27", "\xB1\x3E", "\x8E\xB1", "\x8F\xB0\xA1", "\xA1\xA1", "\xB0\xA1",
    "\x81", "\x8E", "\x8F\xB0", "\xA0", "\xE0", "\xFC\xFC",
];
const TOKENS = [
    '&amp;', '&lt;', '&gt;', '&quot;', '&apos;', '&#039;', '&#39;', '&#x27;', '&nbsp;', '&euro;', '&hellip;', '&Aacute;', '&fjlig;',
    '&#65;', '&#x41;', '&#0;', '&#1;', '&#x9;', '&#128;', '&#xD800;', '&#x10FFFF;', '&#x110000;', '&#99999999999;',
    '&;', '&#;', '&#x;', '&amp', '&#65', '&foo;', '&a b;', '&abcdefghijklmnopqrstuvwxyzabcdefgh;', '&&', '&<', 'fj', '<=', '>=', '</a>',
    '<a href="x?a=1&b=2">', "<p class='c'>", '&#x00000000000000000000000041;',
];
const FLAG_SETS = [
    'default' => ENT_QUOTES | ENT_SUBSTITUTE | ENT_HTML401,
    'compat|401' => ENT_COMPAT | ENT_HTML401,
    'noquotes|401' => ENT_NOQUOTES | ENT_HTML401,
    'quotes|401|ignore' => ENT_QUOTES | ENT_IGNORE | ENT_HTML401,
    'quotes|401|strict' => ENT_QUOTES | ENT_HTML401,
    'quotes|html5' => ENT_QUOTES | ENT_SUBSTITUTE | ENT_HTML5,
    'noquotes|html5' => ENT_NOQUOTES | ENT_HTML5,
    'quotes|xhtml' => ENT_QUOTES | ENT_SUBSTITUTE | ENT_XHTML,
    'quotes|xml1' => ENT_QUOTES | ENT_SUBSTITUTE | ENT_XML1,
    'compat|xml1|strict' => ENT_COMPAT | ENT_XML1,
    'quotes|401|disallowed' => ENT_QUOTES | ENT_SUBSTITUTE | ENT_HTML401 | ENT_DISALLOWED,
    'quotes|html5|disallowed' => ENT_QUOTES | ENT_HTML5 | ENT_DISALLOWED,
    'quotes|xml1|disallowed' => ENT_QUOTES | ENT_SUBSTITUTE | ENT_XML1 | ENT_DISALLOWED,
];
const CHARSETS = ['UTF-8', 'ISO-8859-1', 'ISO-8859-5', 'ISO-8859-15', 'cp1251', 'cp1252', 'cp866', 'KOI8-R', 'MacRoman', 'Shift_JIS', 'BIG5', 'BIG5-HKSCS', 'EUC-JP', 'GB2312'];

function generate(DifftestRng $rng): string
{
    $roll = $rng->next(100);
    if ($roll < 6) {
        // Output much longer than the input, then a long plain run: exercises buffer growth.
        return str_repeat($rng->pick(SPECIAL), $rng->next(400))
            . str_repeat($rng->pick(PLAIN), $rng->next(3000))
            . str_repeat($rng->pick(SPECIAL), $rng->next(40))
            . str_repeat($rng->pick(PLAIN), $rng->next(300));
    }
    if ($roll < 10) {
        // Short strings: below 64 bytes of input the output buffer starts at 128 bytes.
        return str_repeat($rng->pick(SPECIAL), $rng->next(30)) . str_repeat($rng->pick(PLAIN), $rng->next(64)) . ($rng->chance(50) ? $rng->pick(MULTIBYTE) : '');
    }
    if ($roll < 13) {
        return str_repeat($rng->pick(PLAIN), $rng->next(5000)) . ($rng->chance(50) ? $rng->pick(SPECIAL) : '');
    }
    if ($roll < 16) {
        return str_repeat($rng->pick(MULTIBYTE), $rng->next(600));
    }
    // Plain runs of every length around 8, 16, 32 and 64 bytes, separated by everything else.
    $length = $roll < 30 ? 300 + $rng->next(3000) : $rng->next(260);
    $longestRun = $rng->pick([1, 3, 8, 17, 33, 70, 200]);
    $input = '';
    while (strlen($input) < $length) {
        $kind = $rng->next(100);
        if ($kind < 45) {
            $runLength = $rng->next($longestRun) + 1;
            $byte = $rng->pick(PLAIN);
            for ($i = 0; $i < $runLength; $i++) {
                $input .= $rng->chance(85) ? $byte : $rng->pick(PLAIN);
            }
        } elseif ($kind < 65) {
            $input .= $rng->pick(SPECIAL);
        } elseif ($kind < 80) {
            $input .= $rng->pick(MULTIBYTE);
        } elseif ($kind < 90) {
            $input .= $rng->pick(TOKENS);
        } else {
            $input .= $rng->pick(EDGE);
        }
    }
    return $input;
}

function outputs(string $input): Generator
{
    foreach (FLAG_SETS as $flagName => $flags) {
        foreach (CHARSETS as $charset) {
            foreach ([true, false] as $doubleEncode) {
                foreach (['htmlspecialchars', 'htmlentities'] as $function) {
                    // @: htmlentities() raises a notice for charsets it supports only partially
                    yield "$function $flagName $charset " . ($doubleEncode ? 'double' : 'single')
                        => @$function($input, $flags, $charset, $doubleEncode);
                }
            }
        }
    }
}

difftest_run($argv, 'generate', 'outputs');
