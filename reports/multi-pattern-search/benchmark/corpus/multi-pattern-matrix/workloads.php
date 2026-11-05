<?php

declare(strict_types=1);

require_once __DIR__ . '/../multi-pattern-product/workloads.php';

const MATRIX_PCRE_CHUNK_KEYS = 512;

/* Correctness adapter; timing must call Matcher::matchAll() without normalization. */
function matrix_prepare(string $method, string $operation, array $dictionary, int $chunkKeys = MATRIX_PCRE_CHUNK_KEYS): Closure
{
    if ($chunkKeys < 1) {
        throw new InvalidArgumentException('PCRE chunk size must be positive');
    }
    if ($method === 'preg_replace_callback') {
        $pattern = product_pattern(array_keys($dictionary));
        $callback = static fn (array $match): string => $dictionary[$match[0]];
        return static function (string $subject) use ($pattern, $callback): string {
            $result = preg_replace_callback($pattern, $callback, $subject);
            if ($result === null) {
                throw new RuntimeException(preg_last_error_msg());
            }
            return $result;
        };
    }
    if (str_starts_with($method, 'preg_each_')) {
        throw new RuntimeException('Use a prepared grouped PCRE recipe');
    }
    if ($method !== 'preg_match_chunks' && !str_starts_with($method, 'preg_grouped_')) {
        return product_prepare($method, $operation, $dictionary);
    }
    if (count(array_unique($dictionary)) !== count($dictionary)) {
        throw new RuntimeException('Expected distinct dictionary keys');
    }
    $groups = [];
    if ($operation === 'any') {
        $groups[] = $dictionary;
    } else {
        foreach ($dictionary as $key) {
            $groups[strlen($key)][] = $key;
        }
    }
    // Equal-length distinct keys cannot both match at one position. Separate
    // lengths retain nested keys; lookaheads also retain overlapping positions.
    $patterns = [];
    foreach ($groups as $group) {
        foreach (array_chunk($group, $chunkKeys) as $chunk) {
            $body = implode('|', array_map(static fn (string $key): string => preg_quote($key, '~'), $chunk));
            $patterns[] = $operation === 'any' ? '~(?:' . $body . ')~'
                : ($operation === 'count' ? '~(?=(?:' . $body . '))~' : '~(?=(' . $body . '))~');
        }
    }
    return static function (string $subject) use ($patterns, $operation) {
        $total = 0;
        $hits = $first = [];
        foreach ($patterns as $pattern) {
            if ($operation === 'any') {
                $found = preg_match($pattern, $subject);
                if ($found === false) {
                    throw new RuntimeException(preg_last_error_msg());
                }
                if ($found === 1) {
                    return true;
                }
                continue;
            }
            if ($operation === 'count') {
                $found = preg_match_all($pattern, $subject);
                if ($found === false) {
                    throw new RuntimeException(preg_last_error_msg());
                }
                $total += $found;
                continue;
            }
            $found = preg_match_all($pattern, $subject, $matches, PREG_SET_ORDER | PREG_OFFSET_CAPTURE);
            if ($found === false) {
                throw new RuntimeException(preg_last_error_msg());
            }
            $total += $found;
            foreach ($matches as $match) {
                [$key, $offset] = $match[1];
                $hit = ['offset' => $offset, 'length' => strlen($key), 'keyword' => $key];
                if ($operation === 'all') {
                    $hits[] = $hit;
                } elseif (!isset($first[$key]) || $offset < $first[$key]['offset']) {
                    $first[$key] = $hit;
                }
            }
        }
        if ($operation === 'any') {
            return false;
        }
        if ($operation === 'count') {
            return $total;
        }
        if ($operation === 'unique') {
            $hits = array_values($first);
        }
        usort($hits, 'product_hit_order');
        return $operation === 'unique' ? array_column($hits, 'keyword') : $hits;
    };
}
