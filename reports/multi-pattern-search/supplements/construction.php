<?php
declare(strict_types=1);
require __DIR__ . '/definitions.php';
$config = json_decode(file_get_contents($argv[1]), true, 512, JSON_THROW_ON_ERROR);
$parsed = json_decode(file_get_contents($config['family'] . '.json'), true, 512, JSON_THROW_ON_ERROR);
$dictionary = array_slice($parsed['replacements'], 0, $config['size'], true);
unset($parsed);
if (count($dictionary) !== $config['size']) {
    throw new RuntimeException('Dictionary size mismatch');
}
$class = $config['class'] === 'Matcher' ? Str\Matcher::class : Str\Replacer::class;
if ($config['class'] === 'Matcher') {
    $dictionary = array_keys($dictionary);
}
if ($config['mode'] === 'check') {
    $object = new $class($dictionary);
    $actual = $config['class'] === 'Matcher' ? $object->getKeywords() : $object->getReplacements();
    if ($actual !== $dictionary) {
        throw new RuntimeException('Constructor dictionary mismatch');
    }
    echo json_encode(['status' => 'PASS', 'size' => count($dictionary)]), "\n";
    exit;
}
if ($config['mode'] === 'first') {
    $start = hrtime(true);
    $object = new $class($dictionary);
    $elapsed = hrtime(true) - $start;
    echo json_encode(['constructor_ns' => $elapsed, 'size' => count($dictionary)]), "\n";
    exit;
}
$call = static function (int $iteration) use ($dictionary, $class): int {
    $object = new $class($dictionary);
    unset($object);
    return 1;
};
$labels = $config['mode'] === 'aa' ? ['a', 'b'] : ['build_release'];
$counts = $samples = [];
foreach ($labels as $label) {
    mp_warm($call, 1, $config['warmup_ns']);
    $counts[$label] = mp_calibrate($call, 1, $config['sample_ns']);
    $samples[$label] = [];
}
$sink = 0;
for ($pass = 0; $pass < $config['passes']; $pass++) {
    $order = $pass % 2 ? array_reverse($labels) : $labels;
    foreach ($order as $label) {
        $start = hrtime(true);
        $sink += mp_run($call, $counts[$label]);
        $samples[$label][] = (hrtime(true) - $start) / $counts[$label];
    }
}
echo json_encode(['ns' => $samples, 'iterations' => $counts, 'sink' => $sink]), "\n";
