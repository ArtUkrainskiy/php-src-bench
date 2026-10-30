<?php
// Whole application operations, deliberately without regex or multibyte extensions.
declare(strict_types=1);

function substr_product_moderate(string $text, array $terms): int
{
    foreach ($terms as $index => $term) {
        if (str_contains($text, $term)) {
            return $index;
        }
    }
    return -1;
}

function substr_product_headers(string $request): array
{
    $end = strpos($request, "\r\n\r\n");
    if ($end === false) {
        return [];
    }
    $lines = explode("\r\n", substr($request, 0, $end));
    $headers = [];
    foreach ($lines as $index => $line) {
        if ($index === 0) {
            continue;
        }
        $colon = strpos($line, ': ');
        if ($colon !== false) {
            $headers[strtolower(substr($line, 0, $colon))] = substr($line, $colon + 2);
        }
    }
    return $headers;
}

function substr_product_query(string $query): array
{
    $pairs = [];
    foreach (explode('&', $query) as $part) {
        $pair = explode('=', $part, 2);
        $pairs[] = [urldecode($pair[0]), urldecode($pair[1] ?? '')];
    }
    return $pairs;
}

function substr_product_records(string $text): array
{
    $records = [];
    foreach (explode("\r\n", $text) as $line) {
        if ($line !== '') {
            $records[] = explode('||', $line);
        }
    }
    return $records;
}

function substr_product_slots(string $template): array
{
    $slots = [];
    $offset = 0;
    while (($open = strpos($template, '{{', $offset)) !== false) {
        $close = strpos($template, '}}', $open + 2);
        if ($close === false) {
            break;
        }
        $slots[] = substr($template, $open + 2, $close - $open - 2);
        $offset = $close + 2;
    }
    return $slots;
}

function substr_product_log_errors(string $text): array
{
    $errors = [];
    foreach (explode("\n", $text) as $index => $line) {
        if (str_contains($line, '"level":"error"')) {
            $errors[] = $index;
        }
    }
    return $errors;
}

function substr_product_token_offsets(string $text, string $token): array
{
    $offsets = [];
    $offset = 0;
    while (($position = strpos($text, $token, $offset)) !== false) {
        $offsets[] = $position;
        $offset = $position + strlen($token);
    }
    return $offsets;
}
