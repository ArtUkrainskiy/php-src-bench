<?php
// Route-attribution fixtures; product controls use the frozen published corpus.
$suite = require __DIR__ . '/../../../suites/substr-product.php';
$wanted = [];
foreach (['en', 'ru', 'es', 'ar', 'hi', 'zh', 'ja', 'ko', 'emoji'] as $lang) {
    $wanted[] = "banlist12/$lang/post/clean";
}
$wanted = array_merge($wanted, [
    'banlist12/en/post/early', 'banlist12/hi/post/early',
    'explode/pipe2/4k', 'explode/colon2/4k',
    'substr-count/colon2/4k', 'str-replace/colon2/4k', 'parse-http/body64k',
    'render-template/4k', 'log-filter/thread/clean',
]);
$suite['cases'] = array_intersect_key($suite['cases'], array_flip($wanted));
$add = static function (string $name, string $h, string $n) use (&$suite): void {
    $input = 'route-' . count($suite['inputs']);
    $suite['inputs'][$input] = $h;
    $suite['cases']['route/' . $name] = ['code' => 'strpos($s, ' . var_export($n, true) . ')', 'inputs' => [$input]];
};
foreach ([9, 16, 31] as $length) {
    $n = substr('product-token-in-request-metadata', 0, $length);
    $h = str_repeat('normal application text ', 600);
    $add("short$length/absent", $h, $n);
    $add("short$length/early", 'prefix:' . $n . $h, $n);
}
$n = str_repeat('a', 31) . 'b';
$add('long/ordinary-miss', str_repeat('normal application text ', 600), $n);
$add('long/early', 'prefix:' . $n . str_repeat('ordinary text ', 1200), $n);
foreach (['ascii' => ['a', 'b'], 'dna' => ['A', 'C'], 'binary' => ["\x00", "\xff"]] as $label => [$x, $y]) {
    $add("pair/$label/absent", str_repeat($x, 16384), str_repeat($x, 31) . $y);
}
$prefix = str_repeat('a', 64) . 'c';
$selective = substr($prefix . str_repeat('ab', 8192), 0, 16384);
$add('gram/selective/absent', $selective, $n);
$add('gram/selective/late', substr_replace($selective, $n, -32), $n);
$add('gram/dense/absent', substr($prefix . str_repeat('aaab', 4096), 0, 16384), $n);
$add('gram/changing/absent', substr($prefix . str_repeat('ab', 4096), 0, 8192) . str_repeat('aaab', 14336), $n);
$add('twoway/periodic-memory', str_repeat('bb' . str_repeat('ab', 15), 2048), str_repeat('ab', 16));
foreach ([8191, 8192] as $length) {
    $add("threshold/$length", str_repeat('a', $length), $n);
}
return $suite;
