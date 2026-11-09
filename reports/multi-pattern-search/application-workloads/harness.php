<?php
declare(strict_types=1);

setlocale(LC_CTYPE, 'C');
set_error_handler(static function ($number, $message, $file, $line): bool {
    throw new ErrorException($message, 0, $number, $file, $line);
});
gc_disable();

function app_order(array $a, array $b): int
{
    return ($a['offset'] <=> $b['offset']) ?: ($a['length'] <=> $b['length']);
}

function app_trie(array $keys): string
{
    $root = [];
    foreach ($keys as $key) {
        $node = &$root;
        for ($i = 0; $i < strlen($key); ++$i) {
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
        foreach ($node as $byte => $children) {
            $parts[] = preg_quote((string) $byte, '~') . $emit($children);
        }
        $body = count($parts) > 1 ? '(?:' . implode('|', $parts) . ')' : ($parts[0] ?? '');
        return $terminal && $body !== '' ? '(?:' . $body . ')?' : $body;
    };
    return $keys ? $emit($root) : '(?!)';
}

function app_call(array $config, string $method, string $scope, bool $checking = false): Closure
{
    $case = $config['case'];
    $keys = $config['dictionary']['keys'];
    $mapping = $config['dictionary']['replacements'] ?? [];
    $dictionary = $case['operation'] === 'replace' ? $mapping : $keys;
    $operation = $case['operation'];
    $ascii = $case['policy'] === 'ascii-insensitive';
    $subjects = [];
    foreach ($case['documents'] as $id) { $subjects[$id] = $config['documents'][$id]; }
    $class = $operation === 'replace' ? Str\Replacer::class : Str\Matcher::class;
    $query = ['any' => 'matches', 'unique' => 'getMatchedKeywords', 'count' => 'countMatches', 'all' => 'matchAll', 'replace' => 'replace'][$operation];
    $object = $method === 'native' && $scope === 'prepared' ? new $class($dictionary) : null;
    $patterns = [];
    $sorted = $keys;
    usort($sorted, static fn($a, $b): int => strlen($b) <=> strlen($a));
    $values = array_map(static fn($key): string => $mapping[$key] ?? '', $sorted);
    $callback = static fn(array $match): string => $mapping[$match[0]];
    $tokenCallback = static fn(array $match): string => $mapping[$match[0]] ?? $match[0];
    if (str_starts_with($method, 'preg_')) {
        if ($operation === 'replace') {
            $body = $method === 'preg_trie_callback' ? app_trie($sorted)
                : implode('|', array_map(static fn($k): string => preg_quote($k, '~'), $sorted));
            $patterns[] = $method === 'preg_tokens_callback' ? '~\{\{[a-zA-Z0-9_]+\}\}~' : '~(?:' . ($body ?: '(?!)') . ')~';
        } elseif ($operation === 'any') {
            $body = $method === 'preg_trie' ? app_trie($keys)
                : implode('|', array_map(static fn($k): string => preg_quote($k, '~'), $keys));
            $patterns[] = '~(?:' . ($body ?: '(?!)') . ')~' . ($ascii ? 'i' : '');
        } else {
            $groups = [];
            foreach ($keys as $key) { $groups[strlen($key)][] = $key; }
            foreach ($groups as $group) {
                $body = $method === 'preg_trie' ? app_trie($group)
                    : implode('|', array_map(static fn($k): string => preg_quote($k, '~'), $group));
                $patterns[] = '~(?=(' . $body . '))~' . ($ascii ? 'i' : '');
            }
        }
        // Compile before any timed call, including the counter zero-iteration run.
        foreach ($patterns as $pattern) {
            if (preg_match($pattern, '') === false) { throw new RuntimeException(preg_last_error_msg()); }
        }
    }
    return static function () use ($subjects, $keys, $mapping, $dictionary, $operation, $ascii, $class, $query,
        $object, $method, $scope, $checking, $patterns, $sorted, $values, $callback, $tokenCallback) {
        $prepared = $object;
        if ($method === 'native' && $scope !== 'prepared') { $prepared = new $class($dictionary); }
        $outputs = [];
        $sink = 0;
        foreach ($subjects as $id => $original) {
            $subject = $original;
            if ($method === 'native') {
                if ($ascii) { $subject = strtolower($subject); }
                $result = $prepared->$query($subject);
            } elseif ($method === 'strtr') {
                $result = strtr($subject, $mapping);
            } elseif ($method === 'str_replace') {
                $result = str_replace($sorted, $values, $subject);
            } elseif ($operation === 'replace') {
                $result = preg_replace_callback($patterns[0], $method === 'preg_tokens_callback' ? $tokenCallback : $callback, $subject);
                if ($result === null) { throw new RuntimeException(preg_last_error_msg()); }
            } elseif ($method === 'string_loop' || $method === 'folded_string_loop') {
                $folded = $method === 'folded_string_loop';
                if ($folded && $ascii) { $subject = strtolower($subject); }
                $insensitive = $ascii && !$folded;
                $hits = [];
                $result = $operation === 'any' ? false : 0;
                foreach ($keys as $key) {
                    $offset = 0;
                    do {
                        $position = $insensitive ? stripos($subject, $key, $offset) : strpos($subject, $key, $offset);
                        if ($position === false) { break; }
                        if ($operation === 'any') { $result = true; break 2; }
                        if ($operation === 'count') { ++$result; }
                        else { $hits[] = ['offset' => $position, 'length' => strlen($key), 'keyword' => $key]; }
                        if ($operation === 'unique') { break; }
                        $offset = $position + 1;
                    } while (true);
                }
                if ($operation === 'unique' || $operation === 'all') {
                    usort($hits, 'app_order');
                    $result = $operation === 'unique' ? array_column($hits, 'keyword') : $hits;
                }
                unset($hits);
            } else {
                $hits = $first = [];
                $result = $operation === 'any' ? false : 0;
                foreach ($patterns as $pattern) {
                    if ($operation === 'any') {
                        $found = preg_match($pattern, $subject);
                        if ($found === false) { throw new RuntimeException(preg_last_error_msg()); }
                        if ($found) { $result = true; break; }
                    } elseif ($operation === 'count') {
                        $found = preg_match_all($pattern, $subject);
                        if ($found === false) { throw new RuntimeException(preg_last_error_msg()); }
                        $result += $found;
                    } else {
                        if (preg_match_all($pattern, $subject, $matches, PREG_OFFSET_CAPTURE) === false) { throw new RuntimeException(preg_last_error_msg()); }
                        foreach ($matches[1] as [$key, $offset]) {
                            if ($ascii) { $key = strtolower($key); }
                            $hit = ['offset' => $offset, 'length' => strlen($key), 'keyword' => $key];
                            if ($operation === 'all') { $hits[] = $hit; }
                            elseif (!isset($first['k' . $key]) || $offset < $first['k' . $key]['offset']) { $first['k' . $key] = $hit; }
                        }
                        unset($matches, $hit, $key);
                    }
                }
                if ($operation === 'unique' || $operation === 'all') {
                    if ($operation === 'unique') { $hits = array_values($first); }
                    usort($hits, 'app_order');
                    $result = $operation === 'unique' ? array_column($hits, 'keyword') : $hits;
                }
                unset($hits, $first);
            }
            if ($checking) {
                if ($method === 'native' && $operation === 'all') {
                    $result = array_map(static fn($h): array => ['offset' => $h->offset, 'length' => $h->length, 'keyword' => $h->keyword], $result);
                }
                $outputs[$id] = $result;
            } else {
                $sink += is_array($result) ? count($result) : (is_string($result) ? strlen($result) : (int) $result);
            }
            unset($result, $subject);
        }
        unset($prepared);
        return $checking ? $outputs : $sink;
    };
}

function app_loop(Closure $call, int $count): int
{
    $sink = 0;
    for ($i = 0; $i < $count; ++$i) { $sink += $call(); }
    return $sink;
}

function app_calibrate(Closure $call, int $target): int
{
    $count = 1;
    do {
        $start = hrtime(true);
        app_loop($call, $count);
        $elapsed = hrtime(true) - $start;
        if ($elapsed >= 3000000 || $count >= 1048576) { break; }
        $count *= 2;
    } while (true);
    return max(1, (int) ceil($count * $target / max(1, $elapsed)));
}

try {
    if (PHP_DEBUG || !class_exists(Str\Matcher::class)) { throw new RuntimeException('Release PHP and extension required'); }
    $config = json_decode(file_get_contents($argv[1]), true, 512, JSON_THROW_ON_ERROR);
    $mode = $config['mode'];
    if ($mode === 'check') {
        $checks = 0;
        foreach ($config['case']['modes'] as $scope) {
            foreach ($config['case']['methods'] as $method) {
                $call = app_call($config, $method, $scope, true);
                $expected = $config['case']['expected'];
                if ($config['mutation'] ?? false) { $expected = ['deliberately-wrong']; }
                if ($call() !== $expected) { throw new RuntimeException('Output mismatch: ' . $config['case']['id'] . '/' . $scope . '/' . $method); }
                ++$checks;
            }
        }
        echo json_encode(['status' => 'PASS', 'checks' => $checks]), "\n";
        exit;
    }
    $calls = [];
    foreach ($config['methods'] as $label => $method) { $calls[$label] = app_call($config, $method, $config['scope']); }
    if ($mode === 'perf') {
        $call = reset($calls);
        app_loop($call, 4);
        echo json_encode(['sink' => app_loop($call, $config['iterations'])]), "\n";
        exit;
    }
    $counts = $samples = $orders = [];
    foreach ($calls as $label => $call) {
        $warm = app_calibrate($call, 3000000);
        $until = hrtime(true) + $config['warmup_ns'];
        do { app_loop($call, $warm); } while (hrtime(true) < $until);
        $counts[$label] = app_calibrate($call, $config['sample_ns']);
        $samples[$label] = [];
    }
    $sink = 0;
    for ($round = 0; $round < $config['passes']; ++$round) {
        $labels = array_keys($calls);
        $shift = intdiv($round, 2) % count($labels);
        $order = array_merge(array_slice($labels, $shift), array_slice($labels, 0, $shift));
        if ($round % 2) { $order = array_reverse($order); }
        $orders[] = $order;
        foreach ($order as $label) {
            $start = hrtime(true);
            $sink += app_loop($calls[$label], $counts[$label]);
            $samples[$label][] = (hrtime(true) - $start) / $counts[$label];
        }
    }
    echo json_encode(['ns_per_job' => $samples, 'iterations' => $counts, 'orders' => $orders, 'sink' => $sink]), "\n";
} catch (Throwable $error) {
    fwrite(STDERR, get_class($error) . ': ' . $error->getMessage() . "\n");
    exit(1);
}
