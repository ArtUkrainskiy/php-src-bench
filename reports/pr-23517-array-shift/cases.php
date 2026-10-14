<?php
// One array_shift() case per process: ns per operation (median of 7) and an md5 of the results.
//   php cases.php <case|list> [calls]
// With a call count, makes exactly that many operations and prints nothing (for perf stat).
// An operation is one loop body below: a whole drain, one queue step, or one shift of a fresh copy.

$drain = static fn (int $n) => static function (int $calls) use ($n) {
	$base = range(1, $n);
	$r = 0;
	for ($i = 0; $i < $calls; $i++) { $a = $base; while ($a) $r += array_shift($a); }
	return $r;
};
// Steady queue of $n elements: shift one, append one. No copy of the array.
$queue = static fn (int $n) => static function (int $calls) use ($n) {
	$q = range(1, $n);
	$r = 0;
	for ($i = 0; $i < $calls; $i++) { $r += array_shift($q); $q[] = $i; }
	return $r;
};
// One shift of a fresh copy of $base (the copy is part of the cost, as in real code that shifts a local copy).
$fresh = static fn (array $base) => static function (int $calls) use ($base) {
	$r = '';
	for ($i = 0; $i < $calls; $i++) { $a = $base; $r = array_shift($a); }
	return $r;
};
$holed = range(1, 1000); unset($holed[500]);
$strings = []; for ($i = 0; $i < 100; $i++) $strings["k$i"] = $i;

$cases = [
	'two-elements' => $fresh([0, 1]),
	'queue-10' => $queue(10),
	'queue-100' => $queue(100),
	'queue-1000' => $queue(1000),
	'queue-10000' => $queue(10000),
	'drain-100' => $drain(100),
	'drain-1000' => $drain(1000),
	'drain-10000' => $drain(10000),
	'fresh-1000' => $fresh(range(1, 1000)),
	'fresh-1000-hole' => $fresh($holed),
	'fresh-100-string-keys' => $fresh($strings),
];

$name = $argv[1] ?? 'list';
if ($name === 'list') { echo implode(' ', array_keys($cases)), "\n"; exit; }
$run = $cases[$name];
if (isset($argv[2])) { $run((int) $argv[2]); exit; }

$out = md5(serialize($run(50)));
$t0 = hrtime(true); $run(5); $one = max(1, (hrtime(true) - $t0) / 5);
$calls = max(5, (int) (2e7 / $one));
$t = [];
for ($k = 0; $k < 7; $k++) { $t0 = hrtime(true); $run($calls); $t[] = (hrtime(true) - $t0) / $calls; }
sort($t);
printf("%s %.1f %s\n", $name, $t[3], $out);
