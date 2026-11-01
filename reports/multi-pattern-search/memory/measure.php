<?php

declare(strict_types=1);

// One process measures one class/dictionary size. All snapshots use Zend's live
// allocation counter; parser temporaries are released before construction.
set_error_handler(static function (int $number, string $message, string $file, int $line): bool {
    throw new ErrorException($message, 0, $number, $file, $line);
});
gc_disable();
if (PHP_DEBUG || !extension_loaded('strmatch') || !function_exists('memory_reset_peak_usage')) {
    throw new RuntimeException('A release PHP with strmatch and memory_reset_peak_usage is required');
}
[$script, $family, $size, $kind] = $argv;
$size = (int) $size;
if (!in_array($kind, ['Matcher', 'Replacer'], true)) {
    throw new InvalidArgumentException('Unknown class');
}
$baseline = memory_get_usage(false);
$parsed = json_decode(file_get_contents($family . '.json'), true, 512, JSON_THROW_ON_ERROR);
$dictionary = array_slice($parsed['replacements'], 0, $size, true);
unset($parsed);
if (count($dictionary) !== $size) {
    throw new RuntimeException('Dictionary size mismatch');
}
if ($kind === 'Matcher') {
    $dictionary = array_keys($dictionary);
}
$before = memory_get_usage(false);
$inputBytes = $before - $baseline;
memory_reset_peak_usage();
if ($kind === 'Matcher') {
    $object = new Str\Matcher($dictionary);
} else {
    $object = new Str\Replacer($dictionary);
}
$extraBytes = memory_get_usage(false) - $before;
$peakBytes = memory_get_peak_usage(false) - $before;
unset($dictionary);
$standaloneBytes = memory_get_usage(false) - $baseline;
$construction = [
    'input_bytes' => $inputBytes,
    'object_extra_bytes' => $extraBytes,
    'construction_peak_extra_bytes' => $peakBytes,
    'standalone_bytes' => $standaloneBytes,
];
$subject = file_get_contents($family . '.txt');
$expectedRows = json_decode(file_get_contents($family . '-expected.json'), true, 512, JSON_THROW_ON_ERROR);
$expected = null;
foreach ($expectedRows as $row) {
    if ($row['size'] === $size) {
        $expected = $row;
        break;
    }
}
unset($expectedRows, $row);
if ($expected === null || strlen($subject) !== $expected['subject_bytes']) {
    throw new RuntimeException('Missing expected results');
}
$methods = $kind === 'Matcher' ? ['matches', 'countMatches', 'getMatchedKeywords', 'matchAll'] : ['replace'];
$queries = [];
foreach ($methods as $method) {
    $count = 0;
    $before = memory_get_usage(false);
    memory_reset_peak_usage();
    $result = $method === 'replace' ? $object->replace($subject, $count) : $object->$method($subject);
    $liveBytes = memory_get_usage(false) - $before;
    $queryPeakBytes = memory_get_peak_usage(false) - $before;
    if ($method === 'matchAll') {
        $signature = '';
        foreach ($result as $hit) {
            $signature .= $hit->offset . ':' . $hit->length . ':' . $hit->keyword . "\n";
        }
        $correct = hash('sha256', $signature) === $expected['matchAll_sha256'] && count($result) === $expected['countMatches'];
        unset($hit, $signature);
    } elseif ($method === 'replace') {
        $correct = hash('sha256', $result) === $expected['replace_sha256'] && $count === $expected['replacement_count'];
    } else {
        $correct = $result === $expected[$method];
    }
    unset($result);
    if (!$correct) {
        throw new RuntimeException('Output mismatch: ' . $method);
    }
    $queries[$method] = ['live_result_bytes' => $liveBytes, 'peak_extra_bytes' => $queryPeakBytes];
}
echo json_encode(['size' => $size, 'class' => $kind, 'construction' => $construction, 'queries' => $queries,
    'runtime' => ['php' => PHP_VERSION, 'extension' => phpversion('strmatch'), 'debug' => (bool) PHP_DEBUG,
        'zend_allocator' => getenv('USE_ZEND_ALLOC') !== '0'],
], JSON_THROW_ON_ERROR), "\n";
