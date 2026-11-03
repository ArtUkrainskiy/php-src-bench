<?php
declare(strict_types=1);
require __DIR__ . '/definitions.php';
$config = json_decode(file_get_contents($argv[1]), true, 512, JSON_THROW_ON_ERROR);
$case = $config['case'];
$jobs = $case['jobs'];
$dictionary = $jobs[0]['dictionary'];
foreach ($jobs as $i => $job) {
    if ($job['dictionary'] !== $dictionary) throw new RuntimeException('Changed dictionary cannot be reused');
    $jobs[$i]['dictionary'] = $dictionary;
}
$jobCount = count($jobs);
$methods = $config['methods'];
if (array_is_list($methods)) {
    $methods = array_combine($methods, $methods);
}
$size = $config['batch_size'];
$calls = [];
foreach ($methods as $label => $method) {
    [$setup, $query] = mp_recipes($method, $case['operation']);
    $captures = '$jobs, $dictionary, $jobCount';
    if (!in_array($method, ['matcher', 'replacer'], true)) {
        // Existing regex strings, callbacks or replacement arrays favor native APIs.
        eval($setup);
        foreach (['pattern', 'patterns', 'keys', 'values', 'replacement', 'callback'] as $name) {
            if (isset($$name)) $captures .= ', $' . $name;
        }
        $setup = '';
    }
    if (($config['mutation'] ?? false) && $method === 'matcher' && $case['operation'] === 'any') {
        $query .= ' $result = !$result;';
    }
    $consume = $config['mode'] === 'check' ? '$output[] = $result;' : '$sink += is_array($result) ? count($result) : (is_string($result) ? strlen($result) : (int) $result); unset($result);';
    $finish = $config['mode'] === 'check' ? 'return $output;' : 'return $sink;';
    $body = '$sink = 0; $output = []; ' . $setup . ' for ($i = 0; $i < ' . $size . '; $i++) { $job = $jobs[($iteration * ' . $size . ' + $i) % $jobCount]; foreach ($job["documents"] as $document) { $subject = $document["text"]; ' . $query . ' ' . $consume . ' } } ' . $finish;
    $calls[$label] = eval('return static function (int $iteration) use (' . $captures . ') { ' . $body . ' };');
}
if ($config['mode'] === 'check') {
    $checked = 0;
    foreach ($calls as $label => $call) {
        $method = $methods[$label];
        for ($iteration = 0; $iteration < $jobCount; $iteration++) {
            $expected = [];
            for ($i = 0; $i < $size; $i++) {
                $job = $jobs[($iteration * $size + $i) % $jobCount];
                foreach ($job['documents'] as $doc) $expected[] = $case['operation'] === 'replace' ? $doc['expected']['text'] : $doc['expected'];
            }
            $actual = $call($iteration);
            if ($method === 'matcher' && $case['operation'] === 'all') {
                $actual = array_map(static fn ($hits) => array_map(static fn ($hit) => ['offset'=>$hit->offset,'length'=>$hit->length,'keyword'=>$hit->keyword],$hits),$actual);
            }
            if ($actual !== $expected) throw new RuntimeException('Batch output mismatch');
            $checked += count($actual);
        }
    }
    echo json_encode(['checks'=>$checked]), "\n";
    exit;
}
$counts = $samples = [];
foreach ($calls as $method => $call) {
    mp_warm($call, $jobCount, $config['warmup_ns']);
    $counts[$method] = mp_calibrate($call, $jobCount, $config['sample_ns']);
    $samples[$method] = [];
}
$sink = 0;
for ($pass=0; $pass<$config['passes']; $pass++) {
    $order = array_keys($calls);
    $shift = intdiv($pass, 2) % count($order);
    $order = array_merge(array_slice($order, $shift), array_slice($order, 0, $shift));
    if ($pass % 2) $order = array_reverse($order);
    foreach ($order as $method) {
        $start = hrtime(true);
        $sink += mp_run($calls[$method], $counts[$method]);
        $samples[$method][] = (hrtime(true)-$start)/$counts[$method];
    }
}
echo json_encode(['ns_per_batch'=>$samples,'iterations'=>$counts,'sink'=>$sink]), "\n";
