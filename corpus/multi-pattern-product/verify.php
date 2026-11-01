<?php

declare(strict_types=1);

require __DIR__ . '/workloads.php';

$options = getopt('', ['limit:', 'no-extension', 'mutation', 'corpus:']);
$root = isset($options['corpus']) ? realpath($options['corpus']) : __DIR__;
if ($root === false) {
    throw new RuntimeException('Corpus directory not found');
}
$limit = isset($options['limit']) ? (int) $options['limit'] : PHP_INT_MAX;
$extension = !isset($options['no-extension']) && class_exists('Str\\Matcher');
$mutation = isset($options['mutation']);
$index = json_decode(file_get_contents($root . '/index.json'), true, 512, JSON_THROW_ON_ERROR);
$seen = [];
$cases = $jobs = $documents = $comparisons = $countChecks = 0;
$methods = [];

foreach ($index['suite_sha256'] as $file => $hash) {
    if (hash_file('sha256', $root . '/' . $file) !== $hash) {
        throw new RuntimeException('Input hash mismatch: ' . $file);
    }
    $suite = json_decode(file_get_contents($root . '/' . $file), true, 512, JSON_THROW_ON_ERROR);
    foreach ($suite['cases'] as $case) {
        if ($cases >= $limit) {
            break 2;
        }
        if (isset($seen[$case['id']])) {
            throw new RuntimeException('Duplicate case ID');
        }
        $seen[$case['id']] = true;
        foreach ($case['jobs'] as $job) {
            $prepared = [];
            foreach ($case['methods'] as $method) {
                if (!$extension && in_array($method, ['matcher', 'replacer'], true)) {
                    continue;
                }
                $prepared[$method] = product_prepare($method, $case['operation'], $job['dictionary']);
            }
            $counter = $extension && $case['operation'] === 'replace' ? new Str\Replacer($job['dictionary']) : null;
            foreach ($job['documents'] as $document) {
                $keys = product_keywords($job['dictionary'], $case['operation']);
                $hits = product_all_strpos($document['text'], $keys);
                $distinct = array_unique(array_column($hits, 'keyword'));
                $ranks = array_map(static fn (array $hit): int => array_search($hit['keyword'], $keys, true), $hits);
                $facts = $document['facts'];
                if ($facts['bytes'] !== strlen($document['text']) || $facts['occurrences'] !== count($hits)
                    || $facts['distinct_keywords'] !== count($distinct)
                    || $facts['first_match_offset'] !== ($hits[0]['offset'] ?? null)
                    || $facts['first_matching_dictionary_rank'] !== ($ranks ? min($ranks) : null)) {
                    throw new RuntimeException('Input facts mismatch: ' . $document['id']);
                }
                if ($case['operation'] === 'replace') {
                    $selected = $consumed = 0;
                    $map = $job['dictionary'];
                    $replaced = preg_replace_callback(product_pattern($keys), static function (array $match) use ($map, &$selected, &$consumed): string {
                        $selected++;
                        $consumed += strlen($match[0]);
                        return $map[$match[0]];
                    }, $document['text']);
                    if ($selected !== $facts['selected_matches'] || $consumed !== $facts['matched_source_bytes']
                        || $selected !== $document['expected']['replacements']
                        || $replaced !== $document['expected']['text']
                        || strlen($replaced) !== $facts['output_bytes']) {
                        throw new RuntimeException('Replacement facts mismatch: ' . $document['id']);
                    }
                }
                $expected = $case['operation'] === 'replace' ? $document['expected']['text'] : $document['expected'];
                foreach ($prepared as $method => $call) {
                    $actual = $call($document['text']);
                    if ($mutation && $case['operation'] === 'any' && $method === 'contains_loop') {
                        $actual = !$actual;
                    }
                    if ($actual !== $expected) {
                        fwrite(STDERR, json_encode(['case' => $case['id'], 'job' => $job['id'], 'document' => $document['id'],
                            'method' => $method, 'actual' => $actual, 'expected' => $expected], JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT) . "\n");
                        exit(1);
                    }
                    $methods[$method] = true;
                    $comparisons++;
                }
                if ($counter !== null) {
                    $text = $counter->replace($document['text'], $count);
                    if (['text' => $text, 'replacements' => $count] !== $document['expected']) {
                        throw new RuntimeException('Replacement count mismatch: ' . $case['id']);
                    }
                    $countChecks++;
                }
                $documents++;
            }
            $jobs++;
        }
        $cases++;
    }
}

if ($cases === 0 || $comparisons === 0) {
    throw new RuntimeException('No cases verified');
}
echo json_encode(['status' => 'PASS', 'extension' => $extension ? phpversion('strmatch') : null,
    'cases' => $cases, 'jobs' => $jobs, 'documents' => $documents, 'comparisons' => $comparisons,
    'replacement_count_checks' => $countChecks, 'methods' => array_keys($methods),
    'pcre' => PCRE_VERSION, 'pcre_jit' => ini_get('pcre.jit')], JSON_PRETTY_PRINT), "\n";
