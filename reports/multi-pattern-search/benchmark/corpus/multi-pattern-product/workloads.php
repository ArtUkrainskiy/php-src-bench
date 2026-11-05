<?php

declare(strict_types=1);

/* Correctness adapters for saved product jobs. This file performs no timing. */

function product_keywords(array $dictionary, string $operation): array
{
    return $operation === 'replace' ? array_map('strval', array_keys($dictionary)) : $dictionary;
}

function product_sorted_keywords(array $keywords): array
{
    usort($keywords, static function (string $a, string $b): int {
        return strlen($b) <=> strlen($a);
    });
    return $keywords;
}

function product_pattern(array $keywords): string
{
    $quoted = array_map(static fn (string $keyword): string => preg_quote($keyword, '~'), product_sorted_keywords($keywords));
    return '~(?:' . implode('|', $quoted) . ')~';
}

function product_hit_order(array $a, array $b): int
{
    return ($a['offset'] <=> $b['offset']) ?: ($a['length'] <=> $b['length']);
}

function product_all_strpos(string $subject, array $keywords): array
{
    $hits = [];
    foreach ($keywords as $keyword) {
        $offset = 0;
        while (($position = strpos($subject, $keyword, $offset)) !== false) {
            $hits[] = ['offset' => $position, 'length' => strlen($keyword), 'keyword' => $keyword];
            $offset = $position + 1;
        }
    }
    usort($hits, 'product_hit_order');
    return $hits;
}

function product_all_preg(string $subject, array $keywords): array
{
    $hits = [];
    foreach ($keywords as $keyword) {
        $status = preg_match_all('~(?=(' . preg_quote($keyword, '~') . '))~', $subject, $matches, PREG_SET_ORDER | PREG_OFFSET_CAPTURE);
        if ($status === false) {
            throw new RuntimeException(preg_last_error_msg());
        }
        foreach ($matches as $match) {
            $hits[] = ['offset' => $match[1][1], 'length' => strlen($keyword), 'keyword' => $keyword];
        }
    }
    usort($hits, 'product_hit_order');
    return $hits;
}

function product_unique(string $subject, array $keywords, bool $preg): array
{
    $first = [];
    foreach ($keywords as $keyword) {
        if ($preg) {
            $status = preg_match('~' . preg_quote($keyword, '~') . '~', $subject, $matches, PREG_OFFSET_CAPTURE);
            if ($status === false) {
                throw new RuntimeException(preg_last_error_msg());
            }
            $position = $status ? $matches[0][1] : false;
        } else {
            $position = strpos($subject, $keyword);
        }
        if ($position !== false) {
            $first[] = ['offset' => $position, 'length' => strlen($keyword), 'keyword' => $keyword];
        }
    }
    usort($first, 'product_hit_order');
    return array_column($first, 'keyword');
}

function product_prepare(string $method, string $operation, array $dictionary): Closure
{
    $keywords = product_keywords($dictionary, $operation);
    switch ($method) {
        case 'contains_loop':
            return static function (string $subject) use ($keywords): bool {
                foreach ($keywords as $keyword) {
                    if (str_contains($subject, $keyword)) {
                        return true;
                    }
                }
                return false;
            };
        case 'strtr':
            return static fn (string $subject): string => strtr($subject, $dictionary);
        case 'str_replace':
            $keys = product_sorted_keywords($keywords);
            $values = array_map(static fn (string $key): string => $dictionary[$key], $keys);
            return static fn (string $subject): string => str_replace($keys, $values, $subject);
        case 'preg_match':
            $pattern = product_pattern($keywords);
            return static function (string $subject) use ($pattern): bool {
                $result = preg_match($pattern, $subject);
                if ($result === false) {
                    throw new RuntimeException(preg_last_error_msg());
                }
                return $result === 1;
            };
        case 'preg_replace':
            $values = array_unique(array_values($dictionary));
            if (count($values) !== 1 || str_contains($values[0], '$') || str_contains($values[0], '\\')) {
                throw new RuntimeException('Direct regex replacement requires one plain literal replacement in this corpus');
            }
            $pattern = product_pattern($keywords);
            $replacement = $values[0];
            return static function (string $subject) use ($pattern, $replacement): string {
                $result = preg_replace($pattern, $replacement, $subject);
                if ($result === null) {
                    throw new RuntimeException(preg_last_error_msg());
                }
                return $result;
            };
        case 'preg_replace_callback':
            $pattern = product_pattern($keywords);
            return static function (string $subject) use ($pattern, $dictionary): string {
                $result = preg_replace_callback($pattern, static fn (array $match): string => $dictionary[$match[0]], $subject);
                if ($result === null) {
                    throw new RuntimeException(preg_last_error_msg());
                }
                return $result;
            };
        case 'strpos_unique':
        case 'preg_each_unique':
            return static fn (string $subject): array => product_unique($subject, $keywords, $method === 'preg_each_unique');
        case 'strpos_count':
            return static function (string $subject) use ($keywords): int {
                $count = 0;
                foreach ($keywords as $keyword) {
                    $offset = 0;
                    while (($position = strpos($subject, $keyword, $offset)) !== false) {
                        $count++;
                        $offset = $position + 1;
                    }
                }
                return $count;
            };
        case 'preg_each_count':
            return static function (string $subject) use ($keywords): int {
                $count = 0;
                foreach ($keywords as $keyword) {
                    $result = preg_match_all('~(?=' . preg_quote($keyword, '~') . ')~', $subject);
                    if ($result === false) {
                        throw new RuntimeException(preg_last_error_msg());
                    }
                    $count += $result;
                }
                return $count;
            };
        case 'strpos_all':
            return static fn (string $subject): array => product_all_strpos($subject, $keywords);
        case 'preg_each_all':
            return static fn (string $subject): array => product_all_preg($subject, $keywords);
        case 'matcher':
            $matcher = new Str\Matcher($keywords);
            switch ($operation) {
                case 'any': return static fn (string $subject): bool => $matcher->matches($subject);
                case 'unique': return static fn (string $subject): array => $matcher->getMatchedKeywords($subject);
                case 'count': return static fn (string $subject): int => $matcher->countMatches($subject);
                case 'all':
                    return static function (string $subject) use ($matcher): array {
                        return array_map(static fn ($hit): array => ['offset' => $hit->offset, 'length' => $hit->length, 'keyword' => $hit->keyword], $matcher->matchAll($subject));
                    };
            }
            throw new RuntimeException('Unknown Matcher operation');
        case 'replacer':
            $replacer = new Str\Replacer($dictionary);
            return static fn (string $subject): string => $replacer->replace($subject);
    }
    throw new RuntimeException('Unknown method: ' . $method);
}
