<?php
// Recipes compared with Str\Matcher / Str\Replacer. recipe($method, $input) returns a prepare closure;
// calling it builds what an application builds per call (objects, pattern strings, callbacks, arrays) and
// returns a query closure: string => result. Prepared timing calls only the query closure; one-shot timing
// calls prepare and query. Analysis that depends only on the dictionary (prefix layers, self-overlapping
// keys, key order) runs once, before either.
//
// Existing-method recipes return the same information as the native call, in any order and in the
// cheapest shape: occurrences as [offset, key] or [key, offset] pairs. The native calls pay for their
// ordering and for MatchResult objects.
// $input = ['keys' => list, 'mapping' => array, 'op' => any|unique|count|all|replace, 'ascii' => bool];
// with 'ascii', keys are lowercase and matching ignores ASCII case.
declare(strict_types=1);

function recipe_prefix(array $keys): string
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
    $result = $keys ? $emit($root) : '(?!)';
    $emit = null;
    return $result;
}

function recipe_self_overlap(string $key): bool
{
    $n = strlen($key);
    for ($length = 1; $length < $n; ++$length) {
        if ($key[$length - 1] === $key[$n - 1] && substr_compare($key, $key, $n - $length, $length) === 0) {
            return true;
        }
    }
    return false;
}

/**
 * Prefix layers: a key's layer is one more than the highest layer among its proper prefixes in the
 * dictionary (0 without one). No key of a layer is a prefix of another, so at most one key of a layer
 * matches at any position, and one lookahead alternation per layer reports every occurrence.
 */
function recipe_layers(array $keys): array
{
    $set = array_fill_keys($keys, true);
    $sorted = $keys;
    usort($sorted, static fn($a, $b): int => strlen($a) <=> strlen($b));
    $layer = [];
    foreach ($sorted as $key) {
        $level = 0;
        for ($n = 1; $n < strlen($key); ++$n) {
            $prefix = substr($key, 0, $n);
            if (isset($set[$prefix])) { $level = max($level, $layer[$prefix] + 1); }
        }
        $layer[$key] = $level;
    }
    $layers = [];
    foreach ($keys as $key) { $layers[$layer[$key]][] = $key; }
    ksort($layers);
    return array_values($layers);
}

/** Pattern strings for each key group; $chunk splits a group into alternations of at most that many keys. */
function recipe_pattern_strings(array $groups, bool $prefix, int $chunk, string $op, bool $fold): array
{
    $patterns = [];
    foreach ($groups as $group) {
        foreach ($chunk ? array_chunk($group, $chunk) : [$group] as $part) {
            $body = $prefix ? recipe_prefix($part) : implode('|', array_map(static fn($k): string => preg_quote($k, '~'), $part));
            $pattern = match ($op) {
                'replace', 'any' => '~(?:' . $body . ')~',
                'count' => '~(?=(?:' . $body . '))~',
                default => '~(?=(' . $body . '))~',
            };
            $patterns[] = $pattern . ($fold ? 'i' : '');
        }
    }
    return $patterns;
}

function recipe_native(array $input): Closure
{
    $op = $input['op'];
    if ($op === 'replace') {
        $mapping = $input['mapping'];
        return static function () use ($mapping): Closure {
            $replacer = new Str\Replacer($mapping);
            return static fn(string $s): string => $replacer->replace($s);
        };
    }
    $keys = $input['keys'];
    $fold = $input['ascii'];
    return static function () use ($keys, $op, $fold): Closure {
        $m = new Str\Matcher($keys);
        return match (true) {
            $op === 'any' && $fold => static fn(string $s): bool => $m->matches(strtolower($s)),
            $op === 'any' => static fn(string $s): bool => $m->matches($s),
            $op === 'unique' && $fold => static fn(string $s): array => $m->getMatchedKeywords(strtolower($s)),
            $op === 'unique' => static fn(string $s): array => $m->getMatchedKeywords($s),
            $op === 'count' && $fold => static fn(string $s): int => $m->countMatches(strtolower($s)),
            $op === 'count' => static fn(string $s): int => $m->countMatches($s),
            $fold => static fn(string $s): array => $m->matchAll(strtolower($s)),
            default => static fn(string $s): array => $m->matchAll($s),
        };
    };
}

/** Loops over the dictionary: str_contains(), strpos(), stripos() and substr_count(), called directly. */
function recipe_loop(string $method, array $input): Closure
{
    $op = $input['op'];
    $keys = $input['keys'];
    $caseless = $input['ascii'] && $method === 'strpos_loop';       // stripos() per key
    $folded = $input['ascii'] && $method === 'folded_strpos_loop';  // strtolower() once, then strpos()
    if ($method === 'single_contains') {
        $key = $keys[0];
        return static fn(): Closure => static fn(string $s): bool => str_contains($s, $key);
    }
    if ($method === 'single_unique') {
        $key = $keys[0];
        return static fn(): Closure => static fn(string $s): array => str_contains($s, $key) ? [$key] : [];
    }
    if ($method === 'contains_loop') {
        return static fn(): Closure => static function (string $s) use ($keys): bool {
            foreach ($keys as $key) {
                if (str_contains($s, $key)) { return true; }
            }
            return false;
        };
    }
    if ($method === 'substring_count_loop') {
        $plain = $overlapping = [];
        foreach ($keys as $key) {
            if (recipe_self_overlap($key)) { $overlapping[] = $key; } else { $plain[] = $key; }
        }
        return static fn(): Closure => static function (string $s) use ($plain, $overlapping): int {
            $count = 0;
            foreach ($plain as $key) { $count += substr_count($s, $key); }
            foreach ($overlapping as $key) {
                for ($at = strpos($s, $key); $at !== false; $at = strpos($s, $key, $at + 1)) { ++$count; }
            }
            return $count;
        };
    }
    if ($caseless) {
        return match ($op) {
            'any' => static fn(): Closure => static function (string $s) use ($keys): bool {
                foreach ($keys as $key) {
                    if (stripos($s, $key) !== false) { return true; }
                }
                return false;
            },
            'unique' => static fn(): Closure => static function (string $s) use ($keys): array {
                $found = [];
                foreach ($keys as $key) {
                    if (stripos($s, $key) !== false) { $found[] = $key; }
                }
                return $found;
            },
            'count' => static fn(): Closure => static function (string $s) use ($keys): int {
                $count = 0;
                foreach ($keys as $key) {
                    for ($at = stripos($s, $key); $at !== false; $at = stripos($s, $key, $at + 1)) { ++$count; }
                }
                return $count;
            },
            'all' => static fn(): Closure => static function (string $s) use ($keys): array {
                $hits = [];
                foreach ($keys as $key) {
                    for ($at = stripos($s, $key); $at !== false; $at = stripos($s, $key, $at + 1)) { $hits[] = [$at, $key]; }
                }
                return $hits;
            },
        };
    }
    return match ($op) {
        'any' => static fn(): Closure => static function (string $s) use ($keys, $folded): bool {
            if ($folded) { $s = strtolower($s); }
            foreach ($keys as $key) {
                if (str_contains($s, $key)) { return true; }
            }
            return false;
        },
        'unique' => static fn(): Closure => static function (string $s) use ($keys, $folded): array {
            if ($folded) { $s = strtolower($s); }
            $found = [];
            foreach ($keys as $key) {
                if (str_contains($s, $key)) { $found[] = $key; }
            }
            return $found;
        },
        'count' => static fn(): Closure => static function (string $s) use ($keys, $folded): int {
            if ($folded) { $s = strtolower($s); }
            $count = 0;
            foreach ($keys as $key) {
                for ($at = strpos($s, $key); $at !== false; $at = strpos($s, $key, $at + 1)) { ++$count; }
            }
            return $count;
        },
        'all' => static fn(): Closure => static function (string $s) use ($keys, $folded): array {
            if ($folded) { $s = strtolower($s); }
            $hits = [];
            foreach ($keys as $key) {
                for ($at = strpos($s, $key); $at !== false; $at = strpos($s, $key, $at + 1)) { $hits[] = [$at, $key]; }
            }
            return $hits;
        },
    };
}

/**
 * pcre_literal / pcre_prefix (escaped alternation / shared-prefix factoring), optional _512 / _1024 chunks.
 * Presence uses one alternation; unique, count and all one lookahead alternation per prefix layer.
 */
function recipe_pcre(string $method, array $input): Closure
{
    $op = $input['op'];
    $fold = $input['ascii'];
    $prefix = str_contains($method, 'prefix');
    $chunk = str_ends_with($method, '_512') ? 512 : (str_ends_with($method, '_1024') ? 1024 : 0);
    if ($op === 'replace') {
        return recipe_pcre_replace($method, $input['mapping'], $prefix, $chunk, $fold);
    }
    $keys = $input['keys'];
    $groups = $op === 'any' ? [$keys] : recipe_layers($keys);
    return static function () use ($groups, $prefix, $chunk, $op, $fold): Closure {
        $patterns = recipe_pattern_strings($groups, $prefix, $chunk, $op, $fold);
        return match ($op) {
            'any' => static function (string $s) use ($patterns): bool {
                foreach ($patterns as $pattern) {
                    if (preg_match($pattern, $s)) { return true; }
                }
                return false;
            },
            'count' => static function (string $s) use ($patterns): int {
                $count = 0;
                foreach ($patterns as $pattern) { $count += preg_match_all($pattern, $s); }
                return $count;
            },
            'unique' => static function (string $s) use ($patterns): array {
                $found = [];
                foreach ($patterns as $pattern) {
                    preg_match_all($pattern, $s, $m);
                    $found += array_flip($m[1]);
                }
                return array_keys($found);
            },
            'all' => static function (string $s) use ($patterns): array {
                $hits = [];
                foreach ($patterns as $pattern) {
                    preg_match_all($pattern, $s, $m, PREG_OFFSET_CAPTURE);
                    $hits[] = $m[1];
                }
                return $hits ? array_merge(...$hits) : [];
            },
        };
    };
}

/** pcre_longest: longer keys first; pcre_prefix: shared-prefix factoring; _constant: one replacement value. */
function recipe_pcre_replace(string $method, array $mapping, bool $prefix, int $chunk, bool $fold): Closure
{
    $keys = array_map('strval', array_keys($mapping));
    if (str_contains($method, 'longest')) {
        usort($keys, static fn($a, $b): int => strlen($b) <=> strlen($a));
    }
    $constant = str_contains($method, '_constant') ? strtr((string) reset($mapping), ['\\' => '\\\\', '$' => '\\$']) : null;
    return static function () use ($keys, $mapping, $prefix, $chunk, $fold, $constant): Closure {
        $patterns = recipe_pattern_strings([$keys], $prefix, $chunk, 'replace', $fold);
        if ($constant !== null) {
            return static fn(string $s): string => preg_replace($patterns, $constant, $s);
        }
        $callback = static fn(array $m): string => $mapping[$m[0]];
        return static fn(string $s): string => preg_replace_callback($patterns, $callback, $s);
    };
}

function recipe_replace(string $method, array $input): Closure
{
    $mapping = $input['mapping'];
    return static fn(): Closure => static fn(string $s): string => strtr($s, $mapping);
}

/** Returns the prepare closure for $method. */
function recipe(string $method, array $input): Closure
{
    return match (true) {
        $method === 'noop' => static fn(): Closure => static fn(string $s): int => 0,
        $method === 'native' => recipe_native($input),
        str_starts_with($method, 'pcre_') => recipe_pcre($method, $input),
        $method === 'strtr' => recipe_replace($method, $input),
        default => recipe_loop($method, $input),
    };
}
