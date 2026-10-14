<?php
// One array_push() case per process: ns per call (median of 7) and an md5 of the last array.
//   php cases.php <case|list> [calls]
// With a call count, makes exactly that many calls and prints nothing (for perf stat).
// "build" cases append to one array and start a new one every 1024 calls (growth included);
// "new" cases push onto a fresh empty array each call (array creation and freeing included).

$v16 = range(1, 16);
$v1000 = range(1, 1000);
$s = 'str';

$cases = [
	'build-1-int' => static function (int $calls) use ($v16, $s) { $st = []; $a = $st; for ($i = 0; $i < $calls; $i++) { if (($i & 1023) === 0) $a = $st; array_push($a, $i); } return md5(serialize($a)); },
	'build-1-string' => static function (int $calls) use ($v16, $s) { $st = []; $a = $st; for ($i = 0; $i < $calls; $i++) { if (($i & 1023) === 0) $a = $st; array_push($a, $s); } return md5(serialize($a)); },
	'build-3-ints' => static function (int $calls) use ($v16, $s) { $st = []; $a = $st; for ($i = 0; $i < $calls; $i++) { if (($i & 1023) === 0) $a = $st; array_push($a, $i, $i, $i); } return md5(serialize($a)); },
	'build-16-spread' => static function (int $calls) use ($v16, $s) { $st = []; $a = $st; for ($i = 0; $i < $calls; $i++) { if (($i & 1023) === 0) $a = $st; array_push($a, ...$v16); } return md5(serialize($a)); },
	'build-1-hash' => static function (int $calls) use ($v16, $s) { $st = ['k' => 0]; $a = $st; for ($i = 0; $i < $calls; $i++) { if (($i & 1023) === 0) $a = $st; array_push($a, $i); } return md5(serialize($a)); },
	'build-3-hash' => static function (int $calls) use ($v16, $s) { $st = ['k' => 0]; $a = $st; for ($i = 0; $i < $calls; $i++) { if (($i & 1023) === 0) $a = $st; array_push($a, $i, $i, $i); } return md5(serialize($a)); },
	'build-1-holes' => static function (int $calls) use ($v16, $s) { $st = (static function () { $a = range(0, 7); unset($a[3]); return $a; })(); $a = $st; for ($i = 0; $i < $calls; $i++) { if (($i & 1023) === 0) $a = $st; array_push($a, $i); } return md5(serialize($a)); },
	'new-1' => static function (int $calls) { for ($i = 0; $i < $calls; $i++) { $a = []; array_push($a, $i); } return md5(serialize($a)); },
	'new-2' => static function (int $calls) { for ($i = 0; $i < $calls; $i++) { $a = []; array_push($a, $i, $i); } return md5(serialize($a)); },
	'new-16-spread' => static function (int $calls) use ($v16) { for ($i = 0; $i < $calls; $i++) { $a = []; array_push($a, ...$v16); } return md5(serialize($a)); },
	'new-1000-spread' => static function (int $calls) use ($v1000) { for ($i = 0; $i < $calls; $i++) { $a = []; array_push($a, ...$v1000); } return md5(serialize($a)); },
];

$name = $argv[1] ?? 'list';
if ($name === 'list') { echo implode(' ', array_keys($cases)), "\n"; exit; }
$run = $cases[$name];
if (isset($argv[2])) { $run((int) $argv[2]); exit; }

$out = $run(3000);
$t0 = hrtime(true); $run(3); $one = max(1, (hrtime(true) - $t0) / 3);
$calls = max(5, (int) (2e7 / $one));
$t = [];
for ($k = 0; $k < 7; $k++) { $t0 = hrtime(true); $run($calls); $t[] = (hrtime(true) - $t0) / $calls; }
sort($t);
printf("%s %.1f %s\n", $name, $t[3], $out);
