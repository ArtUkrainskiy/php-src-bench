<?php
// json_encode() and json_decode() of strings: ASCII and non-ASCII text, escaped and unescaped Unicode.

$text = static fn (string $name, int $bytes): Closure => static fn (): string => Corpus::text($name, $bytes);
$json = static fn (string $name, int $bytes, int $flags = 0): Closure
    => static fn (): string => json_encode(Corpus::text($name, $bytes), $flags | JSON_THROW_ON_ERROR);

return [
    'inputs' => [
        'en-1k' => $text('en', 1024),
        'en-64k' => $text('en', 65536),
        'html-1k' => $text('html', 1024),
        'ru-1k' => $text('ru', 1024),
        'ru-64k' => $text('ru', 65536),
        'zh-1k' => $text('zh', 1024),
        'zh-64k' => $text('zh', 65536),
        'emoji-1k' => $text('emoji', 1024),
        // JSON documents for json_decode(): one string, with \uXXXX escapes or raw UTF-8. They are made
        // by the json_encode() of the binary under test: if a change alters json_encode(), A and B
        // get different documents and the rows are marked ≠in.
        'json-en-64k' => $json('en', 65536),
        'json-ru-64k' => $json('ru', 65536),
        'json-ru-raw-64k' => $json('ru', 65536, JSON_UNESCAPED_UNICODE),
    ],
    'cases' => [
        'json_encode' => [
            'code' => 'json_encode($s)',
            'inputs' => ['en-1k', 'en-64k', 'html-1k', 'ru-1k', 'ru-64k', 'zh-1k', 'zh-64k', 'emoji-1k'],
        ],
        'json_encode UNESCAPED_UNICODE' => [
            'code' => 'json_encode($s, JSON_UNESCAPED_UNICODE)',
            'inputs' => ['ru-1k', 'ru-64k', 'zh-1k', 'zh-64k', 'emoji-1k'],
        ],
        'json_decode' => [
            'code' => 'json_decode($s)',
            'inputs' => ['json-en-64k', 'json-ru-64k', 'json-ru-raw-64k'],
        ],
    ],
];
