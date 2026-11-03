<?php

declare(strict_types=1);

set_error_handler(static function (int $number, string $message, string $file, int $line): bool {
    throw new ErrorException($message, 0, $number, $file, $line);
});
gc_disable();

function mp_pattern(array $keys, bool $longest): string
{
    if ($longest) {
        usort($keys, static fn (string $a, string $b): int => strlen($b) <=> strlen($a));
    }
    return '~(?:' . implode('|', array_map(static fn (string $key): string => preg_quote($key, '~'), $keys)) . ')~';
}

function mp_patterns(array $keys, bool $lookahead, bool $capture): array
{
    $patterns = [];
    foreach ($keys as $key) {
        $literal = preg_quote($key, '~');
        $patterns[] = $lookahead ? '~(?=' . ($capture ? '(' . $literal . ')' : $literal) . ')~' : '~' . $literal . '~';
    }
    return $patterns;
}

function mp_order(array $a, array $b): int
{
    return ($a['offset'] <=> $b['offset']) ?: ($a['length'] <=> $b['length']);
}

function mp_unique(string $subject, array $keys, ?array $patterns): array
{
    $first = [];
    foreach ($keys as $index => $key) {
        if ($patterns === null) {
            $position = strpos($subject, $key);
        } else {
            $found = preg_match($patterns[$index], $subject, $matches, PREG_OFFSET_CAPTURE);
            if ($found === false) {
                throw new RuntimeException(preg_last_error_msg());
            }
            $position = $found ? $matches[0][1] : false;
        }
        if ($position !== false) {
            $first[] = ['offset' => $position, 'length' => strlen($key), 'keyword' => $key];
        }
    }
    usort($first, 'mp_order');
    return array_column($first, 'keyword');
}

function mp_count(string $subject, array $keys, ?array $patterns): int
{
    $count = 0;
    foreach ($keys as $index => $key) {
        if ($patterns === null) {
            $offset = 0;
            while (($offset = strpos($subject, $key, $offset)) !== false) {
                $count++;
                $offset++;
            }
        } else {
            $found = preg_match_all($patterns[$index], $subject);
            if ($found === false) {
                throw new RuntimeException(preg_last_error_msg());
            }
            $count += $found;
        }
    }
    return $count;
}

function mp_all(string $subject, array $keys, ?array $patterns): array
{
    $hits = [];
    foreach ($keys as $index => $key) {
        if ($patterns === null) {
            $offset = 0;
            while (($offset = strpos($subject, $key, $offset)) !== false) {
                $hits[] = ['offset' => $offset, 'length' => strlen($key), 'keyword' => $key];
                $offset++;
            }
        } else {
            $found = preg_match_all($patterns[$index], $subject, $matches, PREG_SET_ORDER | PREG_OFFSET_CAPTURE);
            if ($found === false) {
                throw new RuntimeException(preg_last_error_msg());
            }
            foreach ($matches as $match) {
                $hits[] = ['offset' => $match[1][1], 'length' => strlen($key), 'keyword' => $key];
            }
        }
    }
    usort($hits, 'mp_order');
    return $hits;
}

function mp_recipes(string $method, string $operation): array
{
    switch ($method) {
        case 'contains_loop':
            return ['', '$result = false; foreach ($dictionary as $key) { if (str_contains($subject, $key)) { $result = true; break; } }'];
        case 'strtr':
            return ['', '$result = strtr($subject, $dictionary);'];
        case 'str_replace':
            return ['$keys = array_keys($dictionary); usort($keys, static fn (string $a, string $b): int => strlen($b) <=> strlen($a)); $values = array_map(static fn (string $key): string => $dictionary[$key], $keys);',
                '$result = str_replace($keys, $values, $subject);'];
        case 'preg_match':
            return ['$pattern = mp_pattern($dictionary, false);', '$found = preg_match($pattern, $subject); if ($found === false) { throw new RuntimeException(preg_last_error_msg()); } $result = $found === 1;'];
        case 'preg_replace':
            return ['$pattern = mp_pattern(array_keys($dictionary), true); $replacement = $dictionary[array_key_first($dictionary)];',
                '$result = preg_replace($pattern, $replacement, $subject); if ($result === null) { throw new RuntimeException(preg_last_error_msg()); }'];
        case 'preg_replace_callback':
            return ['$pattern = mp_pattern(array_keys($dictionary), true); $callback = static fn (array $match): string => $dictionary[$match[0]];',
                '$result = preg_replace_callback($pattern, $callback, $subject); if ($result === null) { throw new RuntimeException(preg_last_error_msg()); }'];
        case 'strpos_unique':
        case 'strpos_count':
        case 'strpos_all':
            $function = ['strpos_unique' => 'mp_unique', 'strpos_count' => 'mp_count', 'strpos_all' => 'mp_all'][$method];
            return ['', '$result = ' . $function . '($subject, $dictionary, null);'];
        case 'preg_each_unique':
        case 'preg_each_count':
        case 'preg_each_all':
            $function = ['preg_each_unique' => 'mp_unique', 'preg_each_count' => 'mp_count', 'preg_each_all' => 'mp_all'][$method];
            return ['$patterns = mp_patterns($dictionary, ' . ($method === 'preg_each_unique' ? 'false' : 'true') . ', ' . ($method === 'preg_each_all' ? 'true' : 'false') . ');',
                '$result = ' . $function . '($subject, $dictionary, $patterns);'];
        case 'matcher':
            $query = ['any' => 'matches', 'unique' => 'getMatchedKeywords', 'count' => 'countMatches', 'all' => 'matchAll'][$operation];
            return ['$prepared = new Str\\Matcher($dictionary);', '$result = $prepared->' . $query . '($subject);'];
        case 'replacer':
            return ['$prepared = new Str\\Replacer($dictionary);', '$result = $prepared->replace($subject);'];
    }
    throw new RuntimeException('Unknown method: ' . $method);
}

function mp_call(array $case, string $method, string $lifecycle, bool $checking = false, bool $mutation = false): Closure
{
    $jobs = $case['jobs'];
    $dictionary = $jobs[0]['dictionary'];
    foreach ($jobs as $index => $job) {
        if ($job['dictionary'] === $dictionary) {
            $jobs[$index]['dictionary'] = $dictionary;
        }
    }
    $jobCount = count($jobs);
    [$setup, $query] = mp_recipes($method, $case['operation']);
    $captures = '$jobs, $jobCount';
    if ($lifecycle === 'worker') {
        $dictionary = $jobs[0]['dictionary'];
        foreach ($jobs as $job) {
            if ($job['dictionary'] !== $dictionary) {
                throw new RuntimeException('Worker reuse with a changed dictionary');
            }
        }
        eval($setup);
        foreach (['prepared', 'pattern', 'patterns', 'keys', 'values', 'replacement', 'callback'] as $name) {
            if (isset($$name)) {
                $captures .= ', $' . $name;
            }
        }
        $setup = '';
    } elseif ($lifecycle !== 'request') {
        throw new RuntimeException('Invalid lifecycle');
    }
    if ($mutation) {
        $query .= ' $result = !$result;';
    }
    $consume = $checking ? '$output[] = $result;' : '$sink += is_array($result) ? count($result) : (is_string($result) ? strlen($result) : (int) $result); unset($result);';
    $finish = $checking ? 'return $output;' : 'return $sink;';
    $body = '$job = $jobs[$iteration % $jobCount]; $dictionary = $job["dictionary"]; ' . $setup
        . ' $sink = 0; $output = []; foreach ($job["documents"] as $document) { $subject = $document["text"]; '
        . $query . ' ' . $consume . ' } ' . $finish;
    return eval('return static function (int $iteration) use (' . $captures . ') { ' . $body . ' };');
}

function mp_run(Closure $call, int $iterations): int
{
    $sink = 0;
    for ($i = 0; $i < $iterations; $i++) {
        $sink += $call($i);
    }
    return $sink;
}

function mp_calibrate(Closure $call, int $multiple, int $targetNs): int
{
    $count = $multiple;
    do {
        $start = hrtime(true);
        mp_run($call, $count);
        $elapsed = hrtime(true) - $start;
        if ($elapsed >= 10_000_000) {
            break;
        }
        $count *= 2;
    } while ($count < 8_388_608);
    return max($multiple, (int) ceil($count * $targetNs / max(1, $elapsed) / $multiple) * $multiple);
}

function mp_warm(Closure $call, int $multiple, int $durationNs): void
{
    $batch = mp_calibrate($call, $multiple, 10_000_000);
    $until = hrtime(true) + $durationNs;
    do {
        mp_run($call, $batch);
    } while (hrtime(true) < $until);
}

function mp_check(array $case, array $methods, string $lifecycle, bool $mutation): int
{
    $comparisons = 0;
    foreach ($methods as $method) {
        $call = mp_call($case, $method, $lifecycle, true, $mutation && $method === 'contains_loop');
        foreach ($case['jobs'] as $index => $job) {
            $results = $call($index);
            foreach ($job['documents'] as $i => $document) {
                $result = $results[$i];
                if ($method === 'matcher' && $case['operation'] === 'all') {
                    $result = array_map(static fn ($hit): array => ['offset' => $hit->offset, 'length' => $hit->length, 'keyword' => $hit->keyword], $result);
                }
                $expected = $case['operation'] === 'replace' ? $document['expected']['text'] : $document['expected'];
                if ($result !== $expected) {
                    throw new RuntimeException('Output mismatch: ' . $case['id'] . ' / ' . $method . ' / ' . $document['id']);
                }
                $comparisons++;
            }
        }
    }
    return $comparisons;
}

