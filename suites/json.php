<?php
// json_encode() and json_decode() of strings: ASCII and non-ASCII text, escaped and unescaped Unicode.

$text = static fn (string $name, int $bytes): Closure => static fn (): string => Corpus::text($name, $bytes);
$json = static fn (string $name, int $bytes, int $flags = 0): Closure
    => static fn (): string => json_encode(Corpus::text($name, $bytes), $flags | JSON_THROW_ON_ERROR);

// Every language of the corpus gets the same calls at 1 KB and 64 KB.
$lang1k = Corpus::languages('1k', 1024);
$lang64k = Corpus::languages('64k', 65536);
$nonAscii = array_values(array_filter(array_merge(array_keys($lang1k), array_keys($lang64k)), static fn (string $id): bool => !str_starts_with($id, 'en-')));
// JSON documents for json_decode(): one string, with \uXXXX escapes or raw UTF-8. They are made
// by the json_encode() of the binary under test: if a change alters json_encode(), A and B get
// different documents and the rows are marked ≠in.
$documents = [];
foreach (Corpus::LANGUAGES as $language) {
    $documents["json-$language-64k"] = $json($language, 65536);
    if ($language !== 'en') {
        $documents["json-$language-raw-64k"] = $json($language, 65536, JSON_UNESCAPED_UNICODE);
    }
}

return [
    'inputs' => $lang1k + $lang64k + ['html-1k' => $text('html', 1024)] + $documents,
    'cases' => [
        'json_encode' => [
            'code' => 'json_encode($s)',
            'inputs' => array_merge(array_keys($lang1k), array_keys($lang64k), ['html-1k']),
        ],
        'json_encode UNESCAPED_UNICODE' => [
            'code' => 'json_encode($s, JSON_UNESCAPED_UNICODE)',
            'inputs' => $nonAscii,
        ],
        'json_decode' => [
            'code' => 'json_decode($s)',
            'inputs' => array_keys($documents),
        ],
    ],
];
