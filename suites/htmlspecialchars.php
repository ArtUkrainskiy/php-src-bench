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

return [
    'inputs' => [
        'empty' => '',
        'word-8' => 'abcdefgh',
        'name-16' => 'Niklaus E. Wirth',
        'title-40' => 'What is new in PHP 8.5? A pipe operator.',
        'title-amp-40' => 'Tom & Jerry: "The Movie" <1992>, part 2 ',
        'ru-title-30' => 'Что нового в PHP 8.5',
        'en-64' => $text('en', 64),
        'en-256' => $text('en', 256),
        'en-1k' => $text('en', 1024),
        'en-64k' => $text('en', 65536),
        'html-1k' => $text('html', 1024),
        'html-page-4k' => $real('html-phpnet', 4096),
        'html-wiki-64k' => $real('html-wikipedia', 65536),
        'md-4k' => $real('md-release-process', 4096),
        'js-4k' => $real('js-jquery', 4096),
        'js-min-4k' => $real('js-jquery.min', 4096),
        'entities-1k' => $text('entities', 1024),
        'amp-1k' => str_repeat('&', 1024),
        'quot-1k' => str_repeat('"', 1024),
        'ru-1k' => $text('ru', 1024),
        'zh-1k' => $text('zh', 1024),
        'emoji-1k' => $text('emoji', 1024),
        'ru-64k' => $text('ru', 65536),
        'zh-64k' => $text('zh', 65536),
        'cp1251-64k' => $text('ru-cp1251', 65536),
        'cp1251-1k' => $text('ru-cp1251', 1024),
        'sjis-1k' => $text('ja-sjis', 1024),
        'big5-1k' => $text('zh-big5', 1024),
    ],
    'cases' => [
        'htmlspecialchars' => [
            'code' => 'htmlspecialchars($s)',
            'inputs' => [
                'empty', 'word-8', 'name-16', 'title-40', 'title-amp-40', 'ru-title-30', 'en-64', 'en-256', 'en-1k', 'en-64k',
                'html-1k', 'html-page-4k', 'html-wiki-64k', 'md-4k', 'js-4k', 'js-min-4k', 'amp-1k', 'quot-1k', 'ru-1k', 'ru-64k', 'zh-1k', 'zh-64k', 'emoji-1k',
            ],
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
            'inputs' => ['title-40', 'en-1k', 'html-1k', 'ru-1k'],
        ],
    ],
];
