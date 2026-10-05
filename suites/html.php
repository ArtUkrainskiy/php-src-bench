<?php
// The four functions of ext/standard/html.c on small inputs: a quick overview of encode and decode.
//
// For details use the suites htmlspecialchars (encode), entities and realdata (decode).

$text = static fn (string $name, int $bytes): Closure => static fn (): string => Corpus::text($name, $bytes);

return [
    'inputs' => [
        'empty' => '',
        'word-8' => 'abcdefgh',
        'en-64' => $text('en', 64),
        'en-1k' => $text('en', 1024),
        'en-64k' => $text('en', 65536),
        'html-1k' => $text('html', 1024),
        'entities-1k' => $text('entities', 1024),
        'amp-1k' => str_repeat('&', 1024),
        'quot-1k' => str_repeat('"', 1024),
        'ru-1k' => $text('ru', 1024),
        'zh-1k' => $text('zh', 1024),
        'emoji-1k' => $text('emoji', 1024),
        'cp1251-1k' => $text('ru-cp1251', 1024),
        'sjis-1k' => $text('ja-sjis', 1024),
        'big5-1k' => $text('zh-big5', 1024),
    ],
    'cases' => [
        'htmlspecialchars' => [
            'code' => 'htmlspecialchars($s)',
            'inputs' => ['empty', 'word-8', 'en-64', 'en-1k', 'en-64k', 'html-1k', 'quot-1k', 'ru-1k', 'zh-1k', 'emoji-1k'],
        ],
        'htmlspecialchars !double_encode' => [
            'code' => 'htmlspecialchars($s, ENT_QUOTES | ENT_SUBSTITUTE, null, false)',
            'inputs' => ['html-1k', 'entities-1k', 'amp-1k'],
        ],
        'htmlspecialchars cp1251' => [
            'code' => "htmlspecialchars(\$s, ENT_QUOTES | ENT_SUBSTITUTE, 'cp1251')",
            'inputs' => ['cp1251-1k'],
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
            'inputs' => ['en-1k', 'html-1k', 'ru-1k'],
        ],
        'html_entity_decode' => [
            'code' => 'html_entity_decode($s)',
            'inputs' => ['en-1k', 'html-1k', 'entities-1k', 'amp-1k'],
        ],
        'htmlspecialchars_decode' => [
            'code' => 'htmlspecialchars_decode($s)',
            'inputs' => ['en-1k', 'entities-1k'],
        ],
    ],
];
