<?php
// Product substring search: moderation, delimiters, parsers, templates, logs and source scans.
require_once dirname(__DIR__) . '/corpus/substr-product/workloads.php';
$root = getenv('SUBSTR_PRODUCT_CORPUS') ?: dirname(__DIR__) . '/corpus/substr-product/generated';
$catalog = is_file($root . '/manifest.json') ? $root . '/manifest.json'
    : dirname(__DIR__) . '/corpus/substr-product/cases.json';
$manifest = json_decode(file_get_contents($catalog), true, 512, JSON_THROW_ON_ERROR);
$inputs = [];
$cases = [];
foreach ($manifest['cases'] as $case) {
    $input = $case['input'];
    if (!isset($inputs[$input])) {
        $inputs[$input] = static function () use ($root, $input): string {
            $path = $root . '/inputs/' . $input . '.txt';
            if (!is_file($path)) {
                throw new MissingCorpus('Run python3 corpus/substr-product/generate.py');
            }
            $value = file_get_contents($path);
            if ($value === false) {
                throw new RuntimeException('Missing product fixture: ' . $input);
            }
            return $value;
        };
    }
    $cases[$case['name']] = ['code' => $case['code'], 'inputs' => [$input]];
}
return ['inputs' => $inputs, 'cases' => $cases];
