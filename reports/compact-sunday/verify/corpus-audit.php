<?php
// Capture actual search operands; replacement values are not search needles.
$bench = $argv[1];
$out = $argv[2];
$current = '';
$calls = [];
$payload = '';
function record_search(string $kind, string $h, string $n, int $offset = 0): void {
    global $current, $calls, $payload;
    $start = $offset < 0 ? strlen($h) + $offset : $offset;
    $available = strlen($h) - $start;
    $row = ['case' => $current, 'function' => $kind, 'needle_bytes' => strlen($n),
        'haystack_bytes' => strlen($h), 'offset' => $start,
        'outlined_eligible' => $available >= 1024 && strlen($n) >= 9,
        'adaptive_dispatch_eligible' => $available >= 8192 && strlen($n) >= 32];
    if (strlen($n) >= 32) {
        $row['needle'] = $n;
        $suffix = substr($h, $start);
        $position = strpos($suffix, $n);
        $row['audit_index'] = count(array_filter($calls, static fn($c) => isset($c['audit_index'])));
        $payload .= pack('PPq', strlen($suffix), strlen($n), $position === false ? -1 : $position) . $suffix . $n;
    }
    $calls[] = $row;
}
function probe_contains($h, $n) { record_search('str_contains', $h, $n); return str_contains($h, $n); }
function probe_pos($h, $n, $offset = 0) { record_search('strpos', $h, $n, $offset); return strpos($h, $n, $offset); }
function probe_strstr($h, $n, $before = false) { record_search('strstr', $h, $n); return strstr($h, $n, $before); }
function probe_count($h, $n) { record_search('substr_count', $h, $n); return substr_count($h, $n); }
function probe_explode($n, $h, $limit = PHP_INT_MAX) { record_search('explode', $h, $n); return explode($n, $h, $limit); }
function probe_replace($search, $replace, $subject, &$count = null) {
    foreach ((array)$search as $n) { record_search('str_replace operand', $subject, $n); }
    return str_replace($search, $replace, $subject, $count);
}
function instrument(string $code): string {
    $map = ['str_contains' => 'probe_contains', 'strpos' => 'probe_pos', 'strstr' => 'probe_strstr',
            'substr_count' => 'probe_count', 'explode' => 'probe_explode', 'str_replace' => 'probe_replace'];
    // Skip strings and comments, so a search literal is never rewritten.
    $pattern = <<<'REGEX'
~'(?:\\.|[^'\\])*'|"(?:\\.|[^"\\])*"|//[^\n]*|/\*.*?\*/|\b(?:str_contains|strpos|strstr|substr_count|explode|str_replace)(?=\s*\()~s
REGEX;
    return preg_replace_callback($pattern, static fn($m) => $map[$m[0]] ?? $m[0], $code);
}
$workloads = file_get_contents($bench . '/corpus/substr-product/workloads.php');
eval(instrument(preg_replace('/^<\?php\s*/', '', $workloads)));
$manifest = json_decode(file_get_contents($bench . '/corpus/substr-product/generated/manifest.json'), true, 512, JSON_THROW_ON_ERROR);
foreach ($manifest['cases'] as $case) {
    $current = $case['id'];
    $s = file_get_contents($bench . '/corpus/substr-product/generated/inputs/' . $case['input'] . '.txt');
    eval(instrument($case['code']) . ';');
}
file_put_contents($out . '/corpus-calls.json', json_encode($calls, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE | JSON_THROW_ON_ERROR) . "\n");
file_put_contents($out . '/corpus-long.bin', $payload);
$long = array_filter($calls, static fn($c) => $c['needle_bytes'] >= 32);
printf("cases=%d search_operands=%d long_operands=%d cases_with_long=%d adaptive_dispatch_operands=%d\n",
    count($manifest['cases']), count($calls), count($long), count(array_unique(array_column($long, 'case'))),
    count(array_filter($calls, static fn($c) => $c['adaptive_dispatch_eligible'])));
