<?php
// Entity decoding on real documents: HTML pages, Markdown and JavaScript with their natural share of '&'.
//
// The documents come from corpus/real/ (run corpus/real/fetch.sh once) and are cut to exact sizes.

$docs = [
    'md' => 'real/md-release-process',   // php-src docs/release-process.md
    'md-readme' => 'real/md-bootstrap',  // bootstrap README.md
    'html' => 'real/html-phpnet',        // php.net manual page
    'html-wiki' => 'real/html-wikipedia',// en.wikipedia.org/wiki/HTML
    'js' => 'real/js-jquery',            // jquery-3.7.1.js
    'js-min' => 'real/js-jquery.min',    // jquery-3.7.1.min.js
    'js-old' => 'real/js-confutils',     // php-src win32/build/confutils.js
];
$sizes = ['4k' => 4096, '64k' => 65536, '1m' => 1 << 20];

$inputs = [];
foreach ($docs as $label => $file) {
    foreach ($sizes as $sizeLabel => $bytes) {
        $inputs["$label/$sizeLabel"] = static fn (): string => Corpus::slice($file, $bytes);
    }
}
$small = array_values(array_filter(array_keys($inputs), static fn (string $k): bool => str_ends_with($k, '/4k')));

return [
    'inputs' => $inputs,
    'cases' => [
        'html_entity_decode' => 'html_entity_decode($s)',
        'htmlspecialchars_decode' => 'htmlspecialchars_decode($s)',
        'htmlspecialchars' => ['code' => 'htmlspecialchars($s)', 'inputs' => $small],
    ],
];
