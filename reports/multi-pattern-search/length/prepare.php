<?php

declare(strict_types=1);
require __DIR__ . '/../supplements/definitions.php';
$config = json_decode(file_get_contents($argv[1]), true, 512, JSON_THROW_ON_ERROR);
$dictionary = $config['dictionary'];
$class = $config['class'] === 'Matcher' ? Str\Matcher::class : Str\Replacer::class;
if ($config['mode'] === 'memory') {
    $before = memory_get_usage(false);
    memory_reset_peak_usage();
    $object = new $class($dictionary);
    $retained = memory_get_usage(false) - $before;
    $peak = memory_get_peak_usage(false) - $before;
    $actual = $class === Str\Matcher::class ? $object->getKeywords() : $object->getReplacements();
    if ($actual !== $dictionary) {
        throw new RuntimeException('Constructor dictionary mismatch');
    }
    echo json_encode(['retained_bytes' => $retained, 'peak_extra_bytes' => $peak]), "\n";
    exit;
}
$constructNs = $releaseNs = 0;
$call = static function (int $iteration) use ($dictionary, $class, &$constructNs, &$releaseNs): int {
    $start = hrtime(true);
    $object = new $class($dictionary);
    $constructed = hrtime(true);
    unset($object);
    $released = hrtime(true);
    $constructNs += $constructed - $start;
    $releaseNs += $released - $constructed;
    return 1;
};
mp_warm($call, 1, $config['warmup_ns']);
$count = mp_calibrate($call, 1, $config['sample_ns']);
$labels = $config['mode'] === 'aa' ? ['a', 'b'] : ['value'];
$create = $release = array_fill_keys($labels, []);
$sink = 0;
for ($pass = 0; $pass < $config['passes']; $pass++) {
    $order = $pass % 2 ? array_reverse($labels) : $labels;
    foreach ($order as $label) {
        $constructNs = $releaseNs = 0;
        $sink += mp_run($call, $count);
        $create[$label][] = $constructNs / $count;
        $release[$label][] = $releaseNs / $count;
    }
}
echo json_encode(['constructor_ns' => $config['mode'] === 'aa' ? $create : $create['value'],
    'release_ns' => $config['mode'] === 'aa' ? $release : $release['value'], 'iterations' => $count,
    'sink' => $sink, 'passes' => $config['passes'], 'dictionary_size' => count($dictionary)]), "\n";
