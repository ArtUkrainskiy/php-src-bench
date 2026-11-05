<?php

declare(strict_types=1);

set_error_handler(static function (int $number, string $message, string $file, int $line): bool {
    throw new ErrorException($message, 0, $number, $file, $line);
});
gc_disable();

function construction_memory(string $path, string $class): array
{
    $baseline = memory_get_usage(false);
    $dictionary = json_decode(file_get_contents($path), true, 512, JSON_THROW_ON_ERROR);
    $before = memory_get_usage(false);
    memory_reset_peak_usage();
    $object = new $class($dictionary);
    $ready = memory_get_usage(false);
    $peak = memory_get_peak_usage(false);
    return ['input_bytes' => $before - $baseline, 'object_extra_bytes' => $ready - $before,
        'input_and_object_bytes' => $ready - $baseline, 'construction_peak_including_input_bytes' => $peak - $baseline];
}

function query_memory(array $config, string $class): array
{
    $dictionary = json_decode(file_get_contents($config['dictionary_path']), true, 512, JSON_THROW_ON_ERROR);
    $subject = file_get_contents($config['subject_path']);
    $object = new $class($dictionary);
    $method = $config['query'];
    $before = memory_get_usage(false);
    memory_reset_peak_usage();
    $result = $object->$method($subject);
    $ready = memory_get_usage(false);
    $peak = memory_get_peak_usage(false);
    $afterResult = ['baseline_bytes' => $before, 'result_retained_bytes' => $ready - $before,
                    'query_peak_extra_bytes' => $peak - $before];
    if ($method === 'matchAll') {
        $result = array_map(static fn ($hit): array => ['offset' => $hit->offset, 'length' => $hit->length, 'keyword' => $hit->keyword], $result);
    }
    if (hash('sha256', json_encode($result, JSON_UNESCAPED_SLASHES | JSON_UNESCAPED_UNICODE)) !== $config['expected_sha256']) {
        throw new RuntimeException('Output mismatch in query-memory observation');
    }
    return $afterResult;
}

function constructor_time(array $config, string $class): array
{
    $dictionary = json_decode(file_get_contents($config['dictionary_path']), true, 512, JSON_THROW_ON_ERROR);
    $call = eval('return static function (array $dictionary, int $count): int { $sum = 0; for ($i = 0; $i < $count; $i++) { $start = hrtime(true); $object = new ' . $class . '($dictionary); $sum += hrtime(true) - $start; unset($object); } return $sum; };');
    $count = 1;
    do {
        $sum = $call($dictionary, $count);
        if ($sum >= 5000000 || $count >= 8388608) {
            break;
        }
        $count *= 2;
    } while (true);
    $warm = hrtime(true) + 250000000;
    do {
        $call($dictionary, $count);
    } while (hrtime(true) < $warm);
    $count = max(1, (int) ceil($count * 66666667 / max(1, $call($dictionary, $count))));
    $samples = $empty = [];
    for ($round = 0; $round < 15; $round++) {
        $samples[] = $call($dictionary, $count) / $count;
        $sum = 0;
        for ($i = 0; $i < $count; $i++) {
            $start = hrtime(true);
            $sum += hrtime(true) - $start;
        }
        $empty[] = $sum / $count;
    }
    return ['ns_per_constructor' => $samples, 'empty_timer_ns' => $empty, 'iterations' => $count,
            'destruction' => 'Outside timer; no object retained between iterations',
            'timer_floor' => 'Raw bracket overhead retained, not subtracted'];
}

try {
    if (PHP_DEBUG || !class_exists('Str\\Matcher') || !function_exists('memory_reset_peak_usage')) {
        throw new RuntimeException('Release prototype runtime with resettable heap peak required');
    }
    $config = json_decode(file_get_contents($argv[1]), true, 512, JSON_THROW_ON_ERROR);
    if (!in_array($config['class'], ['Str\\Matcher', 'Str\\Replacer'], true)) {
        throw new RuntimeException('Unexpected class');
    }
    if (hash_file('sha256', $config['dictionary_path']) !== $config['dictionary_file_sha256']) {
        throw new RuntimeException('Dictionary file hash mismatch');
    }
    if ($config['mode'] === 'construction_memory') {
        $result = construction_memory($config['dictionary_path'], $config['class']);
    } elseif ($config['mode'] === 'query_memory') {
        if (hash_file('sha256', $config['subject_path']) !== $config['subject_sha256']) {
            throw new RuntimeException('Subject file hash mismatch');
        }
        $result = query_memory($config, $config['class']);
    } elseif ($config['mode'] === 'constructor_time') {
        $result = constructor_time($config, $config['class']);
    } else {
        throw new RuntimeException('Unknown supplemental mode');
    }
    echo json_encode(['status' => 'PASS', 'mode' => $config['mode'], 'result' => $result,
                     'php' => PHP_VERSION, 'debug' => (bool) PHP_DEBUG, 'zend_allocator' => getenv('USE_ZEND_ALLOC') !== '0']), "\n";
} catch (Throwable $error) {
    fwrite(STDERR, get_class($error) . ': ' . $error->getMessage() . "\n");
    exit(1);
}
