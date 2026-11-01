<?php
require_once __DIR__ . '/functions.php';

function compact_corpus_suite(string $name): array
{
    $root = getenv('COMPACT_CORPUS') ?: __DIR__ . '/../corpus';
    $path = $root . '/' . $name . '.json';
    $index = json_decode(file_get_contents($root . '/index.json'), true, 512, JSON_THROW_ON_ERROR);
    $expectedHash = null;
    foreach ($index['suites'] as $suite) {
        if ($suite['name'] === $name && $suite['file'] === $name . '.json') {
            $expectedHash = $suite['sha256'];
            break;
        }
    }
    if ($expectedHash === null || hash_file('sha256', $path) !== $expectedHash) {
        throw new RuntimeException('Frozen suite hash mismatch: ' . $name);
    }
    $manifest = json_decode(file_get_contents($path), true, 512, JSON_THROW_ON_ERROR);
    $inputs = [];
    $cases = [];
    foreach ($manifest['cases'] as $case) {
        if (!$case['benchmark']) {
            continue;
        }
        if (!function_exists($case['api'])) {
            throw new RuntimeException('Required function unavailable: ' . $case['api']);
        }
        $key = $case['input'];
        foreach ($case['needles'] as $needle) {
            $diagnostic = $case['panel'] === 'control' && strncmp($manifest['suite'], 'controls-', 9) === 0;
            if (strlen($needle) < 1 || strlen($needle) > 256 ||
                (!$diagnostic && (strlen($needle) < 9 || strlen($needle) > 31))) {
                throw new RuntimeException('Needle outside compact range: ' . $case['name']);
            }
        }
        $input = $manifest['inputs'][$key];
        if (strlen($input['text']) !== $input['bytes'] ||
            hash('sha256', $input['text']) !== $input['sha256']) {
            throw new RuntimeException('Frozen input mismatch: ' . $key);
        }
        $inputs[$key] = $input['text'];
        $cases[$case['name']] = ['code' => $case['code'], 'inputs' => [$key]];
        if (isset($case['setup'])) {
            $cases[$case['name']]['setup'] = $case['setup'];
        }
    }
    return ['inputs' => $inputs, 'cases' => $cases];
}
