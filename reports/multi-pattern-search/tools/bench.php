<?php
// Times Str\Matcher / Str\Replacer and the existing-method recipes on one cell.
//
//   php bench.php <cell.json> verify
//   php bench.php <cell.json> time <passes> <first-pass> <method,method,...>
//
// A cell names an operation, a dictionary and a pool of texts.
// verify: every candidate recipe runs on every text; it stays eligible only if its result carries the same
//   information as the native one (unique keys and occurrences compared without order).
// time: in each pass every timed method makes the same number of calls on the same texts of the pool.
//   The call count gives the slowest timed method at most SLOW_NS per pass, and the fastest at least FAST_NS
//   when that limit allows. Window pools get passes until a process makes MIN_TEXTS calls per method;
//   document pools get passes until the whole pool is covered. Existing methods estimated more than
//   UNTIMED_RATIO times slower than the fastest existing method can't be the reference; they keep only
//   their estimate. Methods run in a rotated order that reverses every other pass; one untimed call
//   precedes each timed block. "native_aa" repeats native as an A/A check; "noop" measures the empty call.
//   <first-pass> offsets the pass numbers (run.py passes 0, so every process times the same texts).
declare(strict_types=1);

const FAST_NS = 20_000_000;
const SLOW_NS = 100_000_000;
const ESTIMATE_NS = 2_000_000;
const MIN_TEXTS = 64;
const UNTIMED_RATIO = 5.0;

setlocale(LC_CTYPE, 'C');
gc_disable();
set_error_handler(static function (int $number, string $message): bool {
    throw new ErrorException($message, 0, $number);
});
require __DIR__ . '/recipes.php';

function cell_texts(array $cell, string $base): array
{
    $pool = $cell['pool'];
    if (isset($pool['documents'])) {
        $json = file_get_contents($base . '/' . $pool['documents']);
        if (hash('sha256', $json) !== $pool['corpus_sha256']) {
            throw new RuntimeException('Corpus changed: ' . $pool['documents']);
        }
        $documents = json_decode($json, true, 512, JSON_THROW_ON_ERROR);
        return array_map(static fn(int $i): string => $documents[$i], $pool['indices']);
    }
    $corpus = file_get_contents($base . '/' . $pool['corpus']);
    if (hash('sha256', $corpus) !== $pool['corpus_sha256']) {
        throw new RuntimeException('Corpus changed: ' . $pool['corpus']);
    }
    $texts = [];
    foreach ($pool['offsets'] as $i => $offset) {
        $text = substr($corpus, $offset, $pool['length']);
        foreach ($pool['inserts'][$i] ?? [] as [$at, $key]) {
            $text = substr_replace($text, $key, $at, strlen($key));
        }
        $texts[] = $text;
    }
    return $texts;
}

function candidates(array $input): array
{
    $keys = $input['op'] === 'replace' ? array_keys($input['mapping']) : $input['keys'];
    $pcre = ['pcre_literal', 'pcre_prefix'];
    if (count($keys) > 512) {   // alternations of at most 512 or 1024 keys
        array_push($pcre, 'pcre_literal_512', 'pcre_literal_1024', 'pcre_prefix_512', 'pcre_prefix_1024');
    }

    if ($input['op'] === 'replace') {
        // Only recipes that are right on every text: one pass, leftmost match, longest key at a position.
        $methods = ['strtr', 'pcre_prefix', 'pcre_longest'];
        if (count(array_unique($input['mapping'])) === 1) {
            $methods[] = 'pcre_prefix_constant';
        }
        return $methods;
    }
    $methods = ['strpos_loop'];
    if ($input['ascii']) {
        $methods[] = 'folded_strpos_loop';
    } elseif ($input['op'] === 'any') {
        $methods[] = 'contains_loop';
    }
    if ($input['op'] === 'count') {
        $methods[] = 'substring_count_loop';
    }
    if (count($keys) === 1 && in_array($input['op'], ['any', 'unique'], true)) {
        $methods[] = $input['op'] === 'any' ? 'single_contains' : 'single_unique';
    }
    return array_merge($methods, $pcre);
}

/** Result in a comparable form: occurrences as [offset, length, key]; unique keys and occurrences sorted. */
function normalized(string $op, mixed $result, bool $fold): mixed
{
    $key = static fn($k): string => $fold ? strtolower((string) $k) : (string) $k;
    if ($op === 'all') {
        $result = array_map(static function ($m) use ($key): array {
            if (is_object($m)) { return [$m->offset, $m->length, $key($m->keyword)]; }
            [$a, $b] = $m;
            return is_string($a) ? [$b, strlen($a), $key($a)] : [$a, strlen((string) $b), $key($b)];
        }, $result);
        sort($result);
    } elseif ($op === 'unique') {
        $result = array_values(array_unique(array_map($key, $result)));
        sort($result, SORT_STRING);
    }
    return $result;
}

function consume(mixed $result): int
{
    return is_array($result) ? count($result) : (is_string($result) ? strlen($result) : (int) $result);
}

function run_calls(string $mode, Closure $prepare, Closure $query, array $texts, int $first, int $calls): int
{
    $count = count($texts);
    $sink = 0;
    for ($i = 0, $at = $first; $i < $calls; ++$i, $at = $at + 1 === $count ? 0 : $at + 1) {
        if ($mode === 'prepared') {
            $result = $query($texts[$at]);
        } else {
            $once = $prepare();
            $result = $once($texts[$at]);
            unset($once);
        }
        $sink += consume($result);
        unset($result);
    }
    return $sink;
}

$cellFile = $argv[1];
$action = $argv[2];
$cell = json_decode(file_get_contents($cellFile), true, 512, JSON_THROW_ON_ERROR);
$texts = cell_texts($cell, dirname(__DIR__));
$input = ['keys' => $cell['keys'] ?? [], 'mapping' => $cell['mapping'] ?? [], 'op' => $cell['op'],
    'ascii' => ($cell['policy'] ?? 'case-sensitive') === 'ascii-insensitive'];
$modes = $cell['modes'] ?? ['prepared', 'oneshot'];
if (!(opcache_get_status(false)['opcache_enabled'] ?? false)) {
    throw new RuntimeException('OPcache must be enabled');
}

if ($action === 'verify') {
    $native = recipe('native', $input)();
    $expected = [];
    $results = [];
    foreach ($texts as $i => $text) {
        $value = $native($text);
        $results[] = is_array($value) ? count($value) : (is_string($value) ? null : (int) $value);
        $expected[$i] = normalized($input['op'], $value, $input['ascii']);
    }
    $eligible = ['native'];
    $excluded = [];
    foreach (candidates($input) as $method) {
        try {
            $query = recipe($method, $input)();
            foreach ($texts as $i => $text) {
                if (normalized($input['op'], $query($text), $input['ascii']) !== $expected[$i]) {
                    throw new RuntimeException('result differs on text ' . $i);
                }
            }
            $eligible[] = $method;
        } catch (Throwable $error) {
            $excluded[$method] = $error->getMessage();
        }
        unset($query);
    }
    $counted = array_values(array_filter($results, 'is_int'));
    sort($counted);
    echo json_encode(['cell' => $cell['id'], 'texts' => count($texts), 'eligible' => $eligible, 'excluded' => (object) $excluded,
        'result_median' => $counted ? $counted[intdiv(count($counted), 2)] : null, 'php' => PHP_VERSION]), "\n";
    exit;
}

[, , , $passes, $firstPass, $methodList] = $argv;
$eligible = explode(',', $methodList);
$middle = intdiv(count($eligible) + 1, 2);
$timed = array_merge(array_slice($eligible, 0, $middle), ['native_aa'], array_slice($eligible, $middle), ['noop']);
$prepare = $query = [];
foreach ($timed as $method) {
    $prepare[$method] = recipe($method === 'native_aa' ? 'native' : $method, $input);
    $query[$method] = $prepare[$method]();
}

$samples = [];
$calls = [];
$perCall = [];
$untimed = [];
$passCount = [];
$sink = 0;
$usage = getrusage();
foreach ($modes as $mode) {
    // Warm-up and per-call estimate: one untimed call (compiles patterns), then batches of growing size
    // until one batch takes ESTIMATE_NS.
    foreach ($timed as $method) {
        $sink += run_calls($mode, $prepare[$method], $query[$method], $texts, 0, 1);
        $n = 1;
        do {
            $start = hrtime(true);
            $sink += run_calls($mode, $prepare[$method], $query[$method], $texts, $n % count($texts), $n);
            $elapsed = hrtime(true) - $start;
            $n *= 2;
        } while ($elapsed < ESTIMATE_NS && $n <= (1 << 22));   // cap: about 4 million calls
        $perCall[$mode][$method] = $elapsed / ($n / 2);
    }
    $existing = array_diff_key($perCall[$mode], ['native' => true, 'native_aa' => true, 'noop' => true]);
    $best = min($existing);
    $untimed[$mode] = array_keys(array_filter($existing, static fn(float $ns): bool => $ns > UNTIMED_RATIO * $best));
    $modeTimed = array_values(array_diff($timed, $untimed[$mode]));
    $measured = array_intersect_key($perCall[$mode], array_flip(array_diff($modeTimed, ['noop'])));
    $calls[$mode] = max(1, min((int) ceil(FAST_NS / min($measured)), (int) floor(SLOW_NS / max($measured))));
    // Window pools: passes start at a prime stride (7919) over the pool, at least MIN_TEXTS calls in all.
    // Document pools (whole comments, User-Agents, pages differ in size): consecutive passes tile the
    // shuffled pool and cover all of it.
    $documents = isset($cell['pool']['documents']);
    $passCount[$mode] = max((int) $passes, (int) ceil(($documents ? count($texts) : min(MIN_TEXTS, count($texts))) / $calls[$mode]));
    for ($p = 0; $p < $passCount[$mode]; ++$p) {
        $pass = (int) $firstPass + $p;
        $first = $documents ? ($pass * $calls[$mode]) % count($texts) : ($pass * 7919) % count($texts);
        $order = $modeTimed;
        $shift = $pass % count($order);
        $order = array_merge(array_slice($order, $shift), array_slice($order, 0, $shift));
        if ($pass % 2) {
            $order = array_reverse($order);
        }
        foreach ($order as $method) {
            $sink += run_calls($mode, $prepare[$method], $query[$method], $texts, ($first + $calls[$mode]) % count($texts), 1);
            $start = hrtime(true);
            $sink += run_calls($mode, $prepare[$method], $query[$method], $texts, $first, $calls[$mode]);
            $samples[$mode][$method][] = (hrtime(true) - $start) / $calls[$mode];
        }
    }
}
$after = getrusage();
echo json_encode(['cell' => $cell['id'], 'texts' => count($texts), 'methods' => $eligible, 'calls' => $calls,
    'passes' => $passCount, 'untimed' => $untimed,
    'per_call_estimate_ns' => $perCall, 'samples' => $samples, 'sink' => $sink,
    'involuntary_switches' => $after['ru_nivcsw'] - $usage['ru_nivcsw'], 'php' => PHP_VERSION]), "\n";
