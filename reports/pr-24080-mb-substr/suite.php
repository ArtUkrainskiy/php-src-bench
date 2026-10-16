<?php
// mb_substr() and mb_strpos() on strings marked as valid UTF-8 (php-src PR 24080), every language.
//
// The input is [string, half its length in characters, 6 characters near the end]: lengths are
// worked out once here, on a copy, because mb_strlen() would mark the measured string.

$input = static function (string $text): Closure {
    return static function () use ($text): array {
        $copy = strrev(strrev($text));
        return [$text, intdiv(mb_strlen($copy, 'UTF-8'), 2), mb_substr($copy, -12, 6, 'UTF-8')];
    };
};
$inputs = [];
foreach (Corpus::LANGUAGES as $language) {
    $inputs["$language-title"] = $input(Corpus::line($language, 0));
    $inputs["$language-1k"] = $input(Corpus::text($language, 1024));
    $inputs["$language-64k"] = $input(Corpus::text($language, 65536));
}
$flag = 'mb_check_encoding($s[0], "UTF-8")';

return [
    'inputs' => $inputs,
    'cases' => [
        'head10' => ['code' => 'mb_substr($s[0], 0, 10)', 'inputs' => ['*-title'], 'setup' => $flag],
        'mid20' => ['code' => 'mb_substr($s[0], $s[1], 20)', 'inputs' => ['*-1k', '*-64k'], 'setup' => $flag],
        'tail20' => ['code' => 'mb_substr($s[0], -20)', 'inputs' => ['en-1k', 'en-64k'], 'setup' => $flag],
        'firsthalf' => ['code' => 'mb_substr($s[0], 0, $s[1])', 'inputs' => ['en-1k'], 'setup' => $flag],
        'strpos-mid' => ['code' => 'mb_strpos($s[0], $s[2], $s[1])', 'inputs' => ['en-1k', 'en-64k'], 'setup' => $flag],
        'head10 unflagged' => ['code' => 'mb_substr($s[0], 0, 10)', 'inputs' => ['en-title']],
        'mid20 unflagged' => ['code' => 'mb_substr($s[0], $s[1], 20)', 'inputs' => ['en-1k', 'zh-1k']],
    ],
];
