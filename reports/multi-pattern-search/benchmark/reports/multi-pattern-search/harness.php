<?php

declare(strict_types=1);

require __DIR__ . '/../../corpus/multi-pattern-matrix/workloads.php';
set_error_handler(static function (int $number, string $message, string $file, int $line): bool {
    throw new ErrorException($message, 0, $number, $file, $line);
});
gc_disable();


function probe_pattern(array $keys): string
{
    $root = [];
    foreach ($keys as $key) {
        $node = &$root;
        for ($i = 0; $i < strlen($key); $i++) {
            $byte = $key[$i];
            if (!isset($node[$byte])) { $node[$byte] = []; }
            $node = &$node[$byte];
        }
        $node[''] = true;
        unset($node);
    }
    $emit = static function (array $node) use (&$emit): string {
        $terminal = isset($node['']);
        unset($node['']);
        $parts = [];
        foreach ($node as $byte => $child) {
            $parts[] = preg_quote((string) $byte, '~') . $emit($child);
        }
        $body = count($parts) > 1 ? '(?:' . implode('|', $parts) . ')' : ($parts[0] ?? '');
        return $terminal && $body !== '' ? '(?:' . $body . ')?' : $body;
    };
    return '~' . $emit($root) . '~';
}

function matrix_call(array $case, string $method, string $scope, int $batch, bool $checking = false): Closure
{
    if (!in_array($scope, ['prepared', 'oneshot'], true) || $batch < 1) {
        throw new RuntimeException('Invalid measurement scope/batch');
    }
    if ($method === 'replacer_new') { $method = 'replacer'; $scope = 'oneshot'; }
    $job = $case['jobs'][0];
    $dictionary = $job['dictionary'];
    $subject = $job['documents'][0]['text'];
    $operation = $case['operation'];
    $object = $patterns = $pattern = $keys = $values = $callback = $replacement = null;
    $create = $destroy = '';
    if ($method === 'matcher' || $method === 'replacer') {
        $class = $method === 'matcher' ? 'Str\\Matcher' : 'Str\\Replacer';
        if ($scope === 'prepared') {
            $object = new $class($dictionary);
        } else {
            $create = '$object = new ' . $class . '($dictionary);';
            $destroy = 'unset($object);';
        }
        $query = $method === 'replacer' ? 'replace' : ['any' => 'matches', 'unique' => 'getMatchedKeywords', 'count' => 'countMatches', 'all' => 'matchAll'][$operation];
        $body = '$result = $object->' . $query . '($subject);';
    } elseif ($method === 'contains_loop') {
        $body = '$result = false; foreach ($dictionary as $key) { if (str_contains($subject, $key)) { $result = true; break; } }';
    } elseif (in_array($method, ['preg_trie_callback', 'preg_trie_constant', 'preg_chunked_callback', 'preg_chunked_constant'], true)) {
        $callback = static fn (array $match): string => $dictionary[$match[0]];
        $replacement = $dictionary[array_key_first($dictionary)];
        if (str_starts_with($method, 'preg_chunked_')) {
            $patterns = array_map('probe_pattern', array_chunk(array_keys($dictionary), 512));
            $arg = '$patterns';
        } else {
            $pattern = probe_pattern(array_keys($dictionary));
            $arg = '$pattern';
        }
        $body = str_ends_with($method, '_constant')
            ? '$result = preg_replace(' . $arg . ', $replacement, $subject);'
            : '$result = preg_replace_callback(' . $arg . ', $callback, $subject);';
        $body .= ' if ($result === null) { throw new RuntimeException(preg_last_error_msg()); }';
    } elseif ($method === 'preg_delimited_callback') {
        foreach ($dictionary as $key => $value) {
            if (!str_starts_with($key, '{{') || !str_ends_with($key, '}}')
                    || strpbrk(substr($key, 2, -2), '{}') !== false) {
                throw new RuntimeException('Delimited recipe requires non-nested {{...}} keys');
            }
        }
        $pattern = '~\\{\\{[^{}]*\\}\\}~';
        $callback = static fn (array $match): string => $dictionary[$match[0]] ?? $match[0];
        $body = '$result = preg_replace_callback($pattern, $callback, $subject); if ($result === null) { throw new RuntimeException(preg_last_error_msg()); }';
    } elseif ($method === 'strtr') {
        $body = '$result = strtr($subject, $dictionary);';
    } elseif ($method === 'str_replace') {
        $keys = product_sorted_keywords(array_keys($dictionary));
        $values = array_map(static fn (string $key): string => $dictionary[$key], $keys);
        $body = '$result = str_replace($keys, $values, $subject);';
    } elseif ($method === 'preg_match') {
        $pattern = product_pattern($dictionary);
        $body = '$found = preg_match($pattern, $subject); if ($found === false) { throw new RuntimeException(preg_last_error_msg()); } $result = $found === 1;';
    } elseif ($method === 'preg_replace' || $method === 'preg_replace_callback') {
        $pattern = product_pattern(array_keys($dictionary));
        $callback = static fn (array $match): string => $dictionary[$match[0]];
        $replacement = $dictionary[array_key_first($dictionary)];
        $body = $method === 'preg_replace' ? '$result = preg_replace($pattern, $replacement, $subject);'
            : '$result = preg_replace_callback($pattern, $callback, $subject);';
        $body .= ' if ($result === null) { throw new RuntimeException(preg_last_error_msg()); }';
    } elseif (str_starts_with($method, 'strpos_')) {
        $body = ($operation === 'count' ? '$total = 0;' : '$hits = [];') . ' foreach ($dictionary as $key) { $offset = 0;';
        if ($operation === 'unique') {
            $body .= ' $position = strpos($subject, $key); if ($position !== false) { $hits[] = ["offset"=>$position,"length"=>strlen($key),"keyword"=>$key]; }';
        } else {
            $body .= ' while (($position = strpos($subject, $key, $offset)) !== false) {';
            if ($operation === 'count') {
                $body .= ' $total++;';
            }
            if ($operation === 'all') {
                $body .= ' $hits[] = ["offset"=>$position,"length"=>strlen($key),"keyword"=>$key];';
            }
            $body .= ' $offset = $position + 1; }';
        }
        $body .= ' }';
        if ($operation === 'count') {
            $body .= ' $result = $total;';
        } else {
            $body .= ' usort($hits, "product_hit_order"); $result = ' . ($operation === 'unique' ? 'array_column($hits, "keyword")' : '$hits') . ';';
        }
        $body .= ' unset($hits);';
    } elseif ($method === 'preg_match_chunks' || str_starts_with($method, 'preg_grouped_')) {
        $groups = [];
        if ($operation === 'any') {
            $groups[] = $dictionary;
        } else {
            foreach ($dictionary as $key) {
                $groups[strlen($key)][] = $key;
            }
        }
        $patterns = [];
        foreach ($groups as $group) {
            foreach (array_chunk($group, $GLOBALS['matrix_chunk_keys']) as $chunk) {
                $alternation = implode('|', array_map(static fn (string $key): string => preg_quote($key, '~'), $chunk));
                $patterns[] = $operation === 'any' ? '~(?:' . $alternation . ')~'
                    : ($operation === 'count' ? '~(?=(?:' . $alternation . '))~' : '~(?=(' . $alternation . '))~');
            }
        }
        $body = ($operation === 'any' ? '$result = false;' : ($operation === 'count' ? '$total = 0;' : '$hits = $first = [];')) . ' foreach ($patterns as $pattern) {';
        if ($operation === 'any') {
            $body .= ' $found = preg_match($pattern, $subject); if ($found === false) { throw new RuntimeException(preg_last_error_msg()); } if ($found === 1) { $result = true; break; }';
        } elseif ($operation === 'count') {
            $body .= ' $found = preg_match_all($pattern, $subject); if ($found === false) { throw new RuntimeException(preg_last_error_msg()); } $total += $found;';
        } else {
            $body .= ' $found = preg_match_all($pattern, $subject, $matches, PREG_SET_ORDER | PREG_OFFSET_CAPTURE); if ($found === false) { throw new RuntimeException(preg_last_error_msg()); } foreach ($matches as $match) { [$key, $offset] = $match[1]; $hit = ["offset"=>$offset,"length"=>strlen($key),"keyword"=>$key];';
            $body .= $operation === 'all' ? ' $hits[] = $hit;' : ' if (!isset($first[$key]) || $offset < $first[$key]["offset"]) { $first[$key] = $hit; }';
            $body .= ' } unset($matches, $match, $hit);';
        }
        $body .= ' }';
        if ($operation === 'count') {
            $body .= ' $result = $total;';
        } elseif ($operation !== 'any') {
            if ($operation === 'unique') {
                $body .= ' $hits = array_values($first);';
            }
            $body .= ' usort($hits, "product_hit_order"); $result = ' . ($operation === 'unique' ? 'array_column($hits, "keyword")' : '$hits') . ';';
        }
        $body .= ' unset($hits, $first);';
    } else {
        throw new RuntimeException('Unknown timing recipe: ' . $method);
    }
    $consume = $checking ? '$output[] = $result; unset($result);'
        : '$sink += is_array($result) ? count($result) : (is_string($result) ? strlen($result) : (int) $result); unset($result);';
    $body = '$sink = 0; $output = []; ' . $create . ' for ($job = 0; $job < $batch; $job++) { ' . $body . ' ' . $consume . ' } ' . $destroy
        . ($checking ? ' return $output;' : ' return $sink;');
    return eval('return static function () use ($dictionary, $subject, $object, $patterns, $pattern, $keys, $values, $callback, $replacement, $batch) { ' . $body . ' };');
}

function matrix_loop(Closure $call, int $count): int
{
    $sink = 0;
    for ($i = 0; $i < $count; $i++) {
        $sink += $call();
    }
    return $sink;
}

function matrix_calibrate(Closure $call, int $target): int
{
    $count = 1;
    do {
        $start = hrtime(true);
        matrix_loop($call, $count);
        $elapsed = hrtime(true) - $start;
        if ($elapsed >= 5000000 || $count >= 8388608) {
            break;
        }
        $count *= 2;
    } while (true);
    return max(1, (int) ceil($count * $target / max(1, $elapsed)));
}

function matrix_check(array $case, string $method, string $scope, int $batch, bool $mutation): void
{
    $call = matrix_call($case, $method, $scope, $batch, true);
    $outputs = $call();
    $expected = $case['jobs'][0]['documents'][0]['expected'];
    if ($case['operation'] === 'replace') {
        $expected = $expected['text'];
    }
    if ($mutation) {
        $expected = !$expected;
    }
    foreach ($outputs as $output) {
        if ($method === 'matcher' && $case['operation'] === 'all') {
            $output = array_map(static fn ($hit): array => ['offset' => $hit->offset, 'length' => $hit->length, 'keyword' => $hit->keyword], $output);
        }
        if ($output !== $expected) {
            throw new RuntimeException('Output mismatch: ' . $case['id'] . ' / ' . $method . ' / ' . $scope);
        }
    }
}

try {
    if (PHP_DEBUG || !class_exists('Str\\Matcher') || !class_exists('Str\\Replacer')) {
        throw new RuntimeException('Release PHP and both prototype classes required');
    }
    $config = json_decode(file_get_contents($argv[1]), true, 512, JSON_THROW_ON_ERROR);
    $raw = file_get_contents($config['case_path']);
    if (hash('sha256', $raw) !== $config['case_sha256']) {
        throw new RuntimeException('Case hash mismatch');
    }
    $case = json_decode($raw, true, 512, JSON_THROW_ON_ERROR)['cases'][0];
    if ($case['operation'] === 'replace') {
        $case['methods'] = array_merge($case['methods'], ['preg_trie_callback', 'preg_trie_constant', 'preg_chunked_callback', 'preg_chunked_constant', 'replacer_new', 'preg_delimited_callback']);
    }
    $GLOBALS['matrix_chunk_keys'] = $config['chunk_keys'] ?? MATRIX_PCRE_CHUNK_KEYS;
    if ($GLOBALS['matrix_chunk_keys'] < 1) {
        throw new RuntimeException('Invalid chunk size');
    }
    $scope = $config['scope'];
    $batch = $config['batch'] ?? 1;
    $calls = [];
    foreach ($config['methods'] as $label => $method) {
        if (!in_array($method, $case['methods'], true)) {
            throw new RuntimeException('Undeclared method');
        }
        matrix_check($case, $method, $scope, $batch, $config['mutation'] ?? false);
        $calls[$label] = matrix_call($case, $method, $scope, $batch);
    }
    if ($config['mode'] === 'check') {
        echo json_encode(['status' => 'PASS', 'comparisons' => count($calls) * $batch, 'case' => $case['id'], 'scope' => $scope, 'batch' => $batch]), "\n";
        exit;
    }
    if ($config['mode'] === 'perf') {
        $call = $calls[array_key_first($calls)];
        matrix_loop($call, 8);
        echo json_encode(['sink' => matrix_loop($call, $config['iterations'])]), "\n";
        exit;
    }
    if ($config['mode'] !== 'time') {
        throw new RuntimeException('Unknown mode');
    }
    $counts = $samples = $orders = [];
    foreach ($calls as $label => $call) {
        $warmCount = matrix_calibrate($call, 10000000);
        $until = hrtime(true) + $config['warmup_ns'];
        do {
            matrix_loop($call, $warmCount);
        } while (hrtime(true) < $until);
        $counts[$label] = matrix_calibrate($call, $config['sample_ns']);
        $samples[$label] = [];
    }
    $sink = 0;
    for ($round = 0; $round < $config['passes']; $round++) {
        $labels = array_keys($calls);
        $shift = intdiv($round, 2) % count($labels);
        $order = array_merge(array_slice($labels, $shift), array_slice($labels, 0, $shift));
        if ($round % 2) {
            $order = array_reverse($order);
        }
        $orders[] = $order;
        foreach ($order as $label) {
            $start = hrtime(true);
            $sink += matrix_loop($calls[$label], $counts[$label]);
            $elapsed = hrtime(true) - $start;
            $samples[$label][] = $elapsed / $counts[$label];
        }
    }
    echo json_encode(['ns_per_job' => $samples, 'iterations' => $counts, 'orders' => $orders, 'round_ids' => range(0, $config['passes'] - 1), 'sink' => $sink,
        'case' => $case['id'], 'scope' => $scope, 'batch' => $batch, 'chunk_keys' => $GLOBALS['matrix_chunk_keys'], 'native_results' => true]), "\n";
} catch (Throwable $error) {
    fwrite(STDERR, get_class($error) . ': ' . $error->getMessage() . "\n");
    exit(1);
}
