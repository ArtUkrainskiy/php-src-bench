<?php
// Independent expected outputs come from Python, not from another Zend search.
declare(strict_types=1);
require_once __DIR__ . '/workloads.php';
$root = $argv[1] ?? __DIR__ . '/generated';
$manifest = json_decode(file_get_contents($root . '/manifest.json'), true, 512, JSON_THROW_ON_ERROR);
$expectedFile = $root . '/expected.json';
if (hash_file('sha256', $expectedFile) !== $manifest['expected_sha256']) {
    throw new RuntimeException('Expected outputs changed');
}
$expectedResults = json_decode(file_get_contents($expectedFile), true, 512, JSON_THROW_ON_ERROR);
$checked = 0;
$failures = [];
foreach ($manifest['inputs'] as $name => $input) {
    $path = $root . '/inputs/' . $name . '.txt';
    if (filesize($path) !== $input['bytes'] || hash_file('sha256', $path) !== $input['sha256']) {
        throw new RuntimeException('Fixture changed: ' . $name);
    }
}
foreach ($manifest['cases'] as $case) {
    $s = file_get_contents($root . '/inputs/' . $case['input'] . '.txt');
    $function = eval('return static function (string $s) { return ' . $case['code'] . '; };');
    $actual = $function($s);
    $expected = $expectedResults[$case['id']];
    // JSON represents an empty header dictionary as {}, PHP decodes that as [].
    if ($actual !== $expected) {
        $failures[] = $case['id'];
    }
    $checked++;
}
echo json_encode(['php' => PHP_VERSION, 'checked' => $checked, 'failures' => $failures],
    JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES | JSON_THROW_ON_ERROR), "\n";
exit($failures ? 1 : 0);
