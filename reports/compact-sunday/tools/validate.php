<?php
require_once __DIR__ . '/functions.php';
$path = $argv[1] ?? __DIR__ . '/../corpus';
$family = $argv[2] ?? 'core';
$files = [];
if (is_dir($path)) {
    $index = json_decode(file_get_contents($path . '/index.json'), true, 512, JSON_THROW_ON_ERROR);
    foreach ($index['suites'] as $suite) {
        $file = $path . '/' . $suite['file'];
        if (hash_file('sha256', $file) !== $suite['sha256']) {
            throw new RuntimeException('Frozen suite hash mismatch: ' . $suite['name']);
        }
        $files[] = $file;
    }
} else {
    $files[] = $path;
}
$count = 0;
foreach ($files as $file) {
    $manifest = json_decode(file_get_contents($file), true, 512, JSON_THROW_ON_ERROR);
    foreach ($manifest['cases'] as $case) {
        if ($family !== 'all' && $case['family'] !== $family) {
            continue;
        }
        if (!function_exists($case['api'])) {
            throw new RuntimeException('Required function unavailable: ' . $case['api']);
        }
        $input = $manifest['inputs'][$case['input']];
        $s = $input['text'];
        if (strlen($s) !== $case['bytes'] || hash('sha256', $s) !== $case['sha256']) {
            throw new RuntimeException('Input mismatch: ' . $case['name']);
        }
        $remaining = strlen($s) - ($case['search_offset_bytes'] ?? 0);
        $lengths = array_map('strlen', $case['needles']);
        $entryPath = $remaining < 1024 || max($lengths) < 9 ? 'existing inline control' :
            (min($lengths) >= 32 ? 'wide Sunday control' : 'compact Sunday');
        if ($remaining !== $case['entry_remaining_bytes']) {
            throw new RuntimeException('Remaining length mismatch: ' . $case['name']);
        }
        if ($entryPath !== $case['entry_path']) {
            throw new RuntimeException('Wrong entry path: ' . $case['name']);
        }
        foreach ($case['needles'] as $i => $needle) {
            $diagnostic = $case['panel'] === 'control' && strncmp($manifest['suite'], 'controls-', 9) === 0;
            if (strlen($needle) < 1 || strlen($needle) > 256 ||
                (!$diagnostic && (strlen($needle) < 9 || strlen($needle) > 31)) ||
                strlen($needle) !== $case['needle_bytes'][$i]) {
                throw new RuntimeException('Needle length mismatch: ' . $case['name']);
            }
        }
        $searchable = $case['ascii_folded_fixture'] ? strtolower($s) : $s;
        foreach ($case['needles'] as $i => $needle) {
            $position = strpos($searchable, $case['ascii_folded_fixture'] ? strtolower($needle) : $needle);
            if (($position === false ? -1 : $position) !== $case['positions'][$i]) {
                throw new RuntimeException('Match position mismatch: ' . $case['name']);
            }
        }
        if (isset($case['setup'])) {
            eval($case['setup'] . ';');
        }
        $got = eval('return ' . $case['code'] . ';');
        if ($got !== $case['expected']) {
            throw new RuntimeException('Output mismatch: ' . $case['name']);
        }
        if ($case['api'] === 'stream_get_line' && eval('return ' . $case['code'] . ';') !== $case['expected']) {
            throw new RuntimeException('Repeated stream read mismatch: ' . $case['name']);
        }
        $count++;
    }
}
echo "checked $count $family cases; all outputs match independent expectations\n";
