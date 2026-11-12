<?php
// Construction time and memory of Str\Matcher and Str\Replacer for the report's dictionaries.
//
//   php construct.php            # list the dictionary names
//   php construct.php <name>     # measure one dictionary; run each in a fresh process
//
// Per dictionary and class: median construction time over repeated constructions (destruction outside the
// timer), memory the object retains (memory_get_usage() after minus before), and the construction peak
// above the starting usage. Zend allocator accounting, not RSS. Prints one JSON object per line.
declare(strict_types=1);

gc_disable();
const TARGET_NS = 200_000_000;

$root = dirname(__DIR__);
$load = static fn(string $name): array => json_decode(file_get_contents("$root/dictionaries/$name.json"), true);
$controlled = static function (int $n): array {
    // Same family as the controlled grid: random keys of 4-16 letters a-p, no key inside another.
    $cell = json_decode(file_get_contents(dirname(__DIR__) . '/cells/controlled/unique.n1024.b4096.one.json'), true);
    return array_slice($cell['keys'], 0, $n);
};
// Name => function that makes the keys; only the measured dictionary is ever loaded.
$dictionaries = [];
foreach ([8, 16, 32, 128, 1024] as $n) {
    $dictionaries["random a-p, $n keys"] = static fn(): array => $controlled($n);
}
foreach ([8, 32, 128, 512, 2048, 8019] as $n) {
    $dictionaries["PHP identifiers, $n keys"] = static fn(): array => array_slice($load('php-identifiers'), 0, $n);
}
$dictionaries['LDNOOBW, 403 keys'] = static fn(): array => $load('ldnoobw-en');
$dictionaries['crawler patterns, 1469 keys'] = static fn(): array => $load('crawler-patterns');
$dictionaries['PHP functions, 3345 keys'] = static fn(): array => $load('php-functions');
foreach (['en', 'es', 'ru', 'zh', 'ja', 'ko'] as $lang) {
    $dictionaries["words ($lang), 128 keys"] = static fn(): array => $load("words-$lang");
}
$dictionaries['nested a..a, 512 keys'] = static fn(): array => array_map(static fn(int $i): string => str_repeat('a', $i), range(1, 512));
$dictionaries['64-byte common prefix, 10000 keys'] = static fn(): array => array_map(
    static fn(int $i): string => str_repeat('p', 64) . sprintf('%05d', $i), range(0, 9999));
$dictionaries['random bytes, 10000 keys'] = static function (): array {
    mt_srand(7);
    $random = [];
    while (count($random) < 10000) {
        $random[implode(array_map(static fn(): string => chr(mt_rand(0, 255)), range(1, 12)))] = true;
    }
    return array_map('strval', array_keys($random));
};

if (!isset($argv[1])) {
    echo implode("\n", array_keys($dictionaries)), "\n";
    exit;
}
foreach ([$argv[1] => ($dictionaries[$argv[1]] ?? throw new RuntimeException('Unknown dictionary'))()] as $name => $keys) {
    $mapping = array_combine($keys, array_map('strtoupper', $keys));
    foreach (['matcher' => static fn() => new Str\Matcher($keys), 'replacer' => static fn() => new Str\Replacer($mapping)] as $class => $build) {
        $before = memory_get_usage();
        memory_reset_peak_usage();
        $object = $build();
        $peak = memory_get_peak_usage() - $before;
        $retained = memory_get_usage() - $before;
        unset($object);
        $times = [];
        $spent = 0;
        while ($spent < TARGET_NS || count($times) < 5) {
            $start = hrtime(true);
            $object = $build();
            $elapsed = hrtime(true) - $start;
            unset($object);
            $times[] = $elapsed;
            $spent += $elapsed;
        }
        sort($times);
        echo json_encode(['dictionary' => $name, 'class' => $class, 'keys' => count($keys),
            'key_bytes' => array_sum(array_map('strlen', $keys)), 'construct_us' => $times[intdiv(count($times), 2)] / 1000,
            'constructions' => count($times), 'retained_bytes' => $retained, 'peak_bytes' => $peak], JSON_UNESCAPED_UNICODE), "\n";
    }
}
