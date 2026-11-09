<?php
declare(strict_types=1);

try {
    if (PHP_DEBUG || !class_exists(Str\Matcher::class)) {
        throw new RuntimeException('Release PHP and extension required');
    }
    $config = json_decode(file_get_contents($argv[1]), true, 512, JSON_THROW_ON_ERROR);
    $case = $config['case'];
    $operation = $case['operation'];
    $dictionary = $operation === 'replace' ? $config['dictionary']['replacements'] : $config['dictionary']['keys'];
    $class = $operation === 'replace' ? Str\Replacer::class : Str\Matcher::class;
    $query = ['any' => 'matches', 'unique' => 'getMatchedKeywords', 'count' => 'countMatches',
              'all' => 'matchAll', 'replace' => 'replace'][$operation];
    $inputBaseline = memory_get_usage(false);
    memory_reset_peak_usage();
    $object = new $class($dictionary);
    $retained = memory_get_usage(false) - $inputBaseline;
    $constructionPeak = memory_get_peak_usage(false) - $inputBaseline;
    $methodBaseline = memory_get_usage(false);
    memory_reset_peak_usage();
    $sink = 0;
    foreach ($case['documents'] as $id) {
        $subject = $config['documents'][$id];
        if ($case['policy'] === 'ascii-insensitive') { $subject = strtolower($subject); }
        $result = $object->$query($subject);
        $sink += is_array($result) ? count($result) : (is_string($result) ? strlen($result) : (int) $result);
        unset($result, $subject);
    }
    $methodPeak = memory_get_peak_usage(false) - $methodBaseline;
    unset($object);
    echo json_encode(['case' => $case['id'], 'allocator' => 'Zend memory_get_usage(false)',
        'input_baseline_bytes' => $inputBaseline, 'object_retained_bytes' => $retained,
        'construction_peak_above_input_bytes' => $constructionPeak,
        'method_peak_above_prepared_bytes' => $methodPeak, 'sink' => $sink]), "\n";
} catch (Throwable $error) {
    fwrite(STDERR, get_class($error) . ': ' . $error->getMessage() . "\n");
    exit(1);
}
