<?php
// Differential test for array_diff(): each result is recorded with debug_zval_dump() (values, keys,
// refcounts and reference flags), plus the warnings and exceptions.   php -n difftest.php [fuzz-count] [seed]

$fuzzCount = (int) ($argv[1] ?? 20000);
$seed = (int) ($argv[2] ?? 1);

$sections = [];
$counts = [];
$rec = static function (string $name, array $args) use (&$sections, &$counts) {
	ob_start();
	try {
		$r = array_diff(...$args);
		debug_zval_dump($r);
	} catch (Throwable $e) {
		echo get_class($e), ': ', $e->getMessage(), "\n";
	}
	$out = ob_get_clean();
	$sections[$name] ??= hash_init('sha256');
	hash_update($sections[$name], $out);
	$counts[$name] = ($counts[$name] ?? 0) + 1;
};

// 1. dense ranges around the 8-bits-per-exclusion threshold: span = 8 * count - 2 .. 8 * count + 1, word boundaries
foreach ([1, 2, 3, 7, 8, 9, 63, 64, 65, 100, 1000] as $cnt) {
	foreach ([-2, -1, 0, 1] as $d) {
		$span = max(0, 8 * $cnt + $d);
		$excl = [];
		for ($i = 0; $i < $cnt; $i++) $excl[] = $i === $cnt - 1 ? $span : intdiv($span * $i, max(1, $cnt - 1));
		$first = range(-3, $span + 3);
		$rec('threshold', [$first, $excl]);
		$rec('threshold', [array_reverse($first, true), $excl, [$span + 2]]);
	}
}
// 2. extremes: PHP_INT_MIN/MAX, negative ranges, wraparound of max - min
$m = PHP_INT_MAX; $n = PHP_INT_MIN;
foreach ([[$n, $n + 1, $n + 2], [$m - 2, $m - 1, $m], [$n, $m], [-5, -1, 0, 3], [0], [$m], [$n]] as $excl) {
	$rec('extremes', [[$n, $n + 1, -1, 0, 1, $m - 1, $m, 7, $n + 2], $excl]);
	$rec('extremes', [[$n, $m, 0], $excl, $excl]);
}
// 3. keys, references, duplicates, objects in the first array; references and duplicates in exclusions
$x = 5; $y = 6;
$rec('refs keys', [['a' => 1, 'b' => &$x, 10 => 5, 'c' => 6, 'd' => &$y, 7], [6, 6, 2]]);
$rec('refs keys', [[1, 2, 3, 2, 1], [&$x, 3]]);
$rec('refs keys', [['k' => &$x, 'l' => &$x], [1, 2, 3, 4]]);
$r = [3, 4];
$rec('refs keys', [[1, 2, 3, 4, 5], &$r]);
// 4. mixed types: int-like strings, floats, bools, null, objects with __toString, arrays (TypeError/warning paths)
final class S { public function __construct(private string $s) {} public function __toString(): string { return $this->s; } }
foreach ([['2'], [2.0], [true], [null], [new S('2')], ['02'], [' 2'], ['2 '], [2, '3'], [2, 3.0]] as $excl) {
	$rec('mixed', [[1, 2, 3, '2', 2.0], $excl]);
	$rec('mixed', [[1, 2, 3], $excl]);
	$rec('mixed', [['1', '2', 3], $excl]);
}
$rec('mixed', [[1, 2, [3]], [1]]);
$rec('mixed', [[1, 2], [[1]]]);
// 5. fewer than two elements, empty arrays, one argument
foreach ([[[], [1]], [[1], [1]], [[1], []], [[1, 2], []], [[1, 2]], [[], []]] as $args) $rec('small', $args);
// 6. fuzz: random int arrays, dense (half) or sparse, with keys, references, occasional non-int values
mt_srand($seed);
for ($k = 0; $k < $fuzzCount; $k++) {
	$base = mt_rand(0, 3) ? mt_rand(-1000, 1000) : (mt_rand(0, 1) ? PHP_INT_MAX - mt_rand(0, 5000) : PHP_INT_MIN + mt_rand(0, 5000));
	$width = [10, 100, 1000, 100000, PHP_INT_MAX >> 2][mt_rand(0, 4)];
	$dense = mt_rand(0, 1) === 1; // half of the cases: values within about 4 * count, so the bitset path is taken
	$gen = static function (int $n) use ($base, $width, $dense) {
		$a = [];
		$w = $dense ? max(1, 4 * $n) : $width;
		for ($i = 0; $i < $n; $i++) {
			$v = $dense ? $base + mt_rand(0, $w) : ($width > PHP_INT_MAX >> 3 ? mt_rand() * (mt_rand(0, 1) ? 1 : -1) : $base + mt_rand(0, $width) * (mt_rand(0, 9) ? 1 : -1));
			if (mt_rand(0, $dense ? 499 : 49) === 0) $v = [(string) $v, (float) $v, null, true][mt_rand(0, 3)];
			if (mt_rand(0, 4) === 0) $a['k' . mt_rand(0, 3 * $n)] = $v; else $a[] = $v;
		}
		return $a;
	};
	$args = [$gen(mt_rand(0, 3) ? mt_rand(0, 40) : mt_rand(0, 400))];
	for ($j = mt_rand(1, 3); $j > 0; $j--) $args[] = $gen(mt_rand(0, 3) ? mt_rand(0, 40) : mt_rand(0, 400));
	if (mt_rand(0, 9) === 0 && $args[0]) { $kk = array_key_first($args[0]); $ref = $args[0][$kk]; $args[0][$kk] = &$ref; unset($ref); }
	$rec('fuzz', $args);
}

foreach ($sections as $name => $ctx) echo str_pad($name, 12), str_pad((string) $counts[$name], 8, ' ', STR_PAD_LEFT), '  ', hash_final($ctx), "\n";
