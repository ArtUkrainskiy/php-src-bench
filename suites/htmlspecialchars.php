<?php
// htmlspecialchars() and htmlentities(): short strings, text, markup, non-Latin scripts, legacy charsets.
//
// Short strings are what templates pass; 64 KB inputs are too long for the branch predictor to
// memorize, unlike the 1 KB ones; the flag combinations take other paths through the code.
// The number in an input name is its size in bytes; inputs made of whole lines of a corpus file
// (en-, ru-, html- ...) are at least that long, the "bytes" column of the result is exact.

// Inputs are closures: built only when a selected case uses them, skipped when a corpus file is missing.
$text = static fn (string $name, int $bytes): Closure => static fn (): string => Corpus::text($name, $bytes);
$real = static fn (string $name, int $bytes): Closure => static fn (): string => Corpus::slice("real/$name", $bytes);

// Every language of the corpus gets the same calls: its first line as a title, 1 KB and 64 KB.
$titles = Corpus::languages('title', 0);
$lang1k = Corpus::languages('1k', 1024);
$lang64k = Corpus::languages('64k', 65536);

return [
    'inputs' => $titles + $lang1k + $lang64k + [
        'empty' => '',
        'word-8' => 'abcdefgh',
        'name-16' => 'Niklaus E. Wirth',
        'title-40' => 'What is new in PHP 8.5? A pipe operator.',
        'title-amp-40' => 'Tom & Jerry: "The Movie" <1992>, part 2 ',
        'ru-title-30' => 'Что нового в PHP 8.5',
        'en-64' => $text('en', 64),
        'en-256' => $text('en', 256),
        'html-1k' => $text('html', 1024),
        'html-page-4k' => $real('html-phpnet', 4096),
        'html-wiki-64k' => $real('html-wikipedia', 65536),
        'md-4k' => $real('md-release-process', 4096),
        'js-4k' => $real('js-jquery', 4096),
        'js-min-4k' => $real('js-jquery.min', 4096),
        'entities-1k' => $text('entities', 1024),
        'amp-1k' => str_repeat('&', 1024),
        'quot-1k' => str_repeat('"', 1024),
        'cp1251-64k' => $text('ru-cp1251', 65536),
        'cp1251-1k' => $text('ru-cp1251', 1024),
        'sjis-1k' => $text('ja-sjis', 1024),
        'big5-1k' => $text('zh-big5', 1024),
    ],
    'cases' => [
        'htmlspecialchars' => [
            'code' => 'htmlspecialchars($s)',
            'inputs' => array_merge(
                ['empty', 'word-8', 'name-16', 'title-40', 'title-amp-40', 'ru-title-30'],
                array_keys($titles),
                ['en-64', 'en-256'],
                array_keys($lang1k),
                array_keys($lang64k),
                ['html-1k', 'html-page-4k', 'html-wiki-64k', 'md-4k', 'js-4k', 'js-min-4k', 'amp-1k', 'quot-1k'],
            ),
        ],
        'htmlspecialchars !double_encode' => [
            'code' => 'htmlspecialchars($s, ENT_QUOTES | ENT_SUBSTITUTE, null, false)',
            'inputs' => ['html-1k', 'entities-1k', 'amp-1k'],
        ],
        'htmlspecialchars ENT_DISALLOWED' => [
            'code' => 'htmlspecialchars($s, ENT_QUOTES | ENT_SUBSTITUTE | ENT_DISALLOWED)',
            'inputs' => ['en-1k', 'html-1k'],
        ],
        'htmlspecialchars cp1251' => [
            'code' => "htmlspecialchars(\$s, ENT_QUOTES | ENT_SUBSTITUTE, 'cp1251')",
            'inputs' => ['en-1k', 'cp1251-1k', 'cp1251-64k'],
        ],
        'htmlspecialchars Shift_JIS' => [
            'code' => "htmlspecialchars(\$s, ENT_QUOTES | ENT_SUBSTITUTE, 'Shift_JIS')",
            'inputs' => ['sjis-1k'],
        ],
        'htmlspecialchars BIG5' => [
            'code' => "htmlspecialchars(\$s, ENT_QUOTES | ENT_SUBSTITUTE, 'BIG5')",
            'inputs' => ['big5-1k'],
        ],
        'htmlentities' => [
            'code' => 'htmlentities($s)',
            'inputs' => array_merge(['title-40'], array_keys($lang1k), ['html-1k']),
        ],
    ],
];
