<?php
// One array_diff() case per process: ns per call (median of 7) and an md5 of the results.
//   php cases.php <case|list> [calls]
// With a call count, makes exactly that many calls and prints nothing (for perf stat).
// Small inputs come from a pool of 64 different argument sets (fixed seed).

mt_srand(22648);
function ints(int $n, int $lo, int $hi): array { $a = []; for ($i = 0; $i < $n; $i++) $a[] = mt_rand($lo, $hi); return $a; }
function pool(int $n, callable $f): array { $p = []; for ($i = 0; $i < $n; $i++) $p[] = $f(); return $p; }
function words(int $n): array { $a = []; for ($i = 0; $i < $n; $i++) $a[] = substr(md5((string) mt_rand()), 0, 8); return $a; }

$cases = [
	// the example from the PR description
	'description-200k' => static fn () => [[range(0, 200000), range(100000, 300000)]],
	// dense ints (ids), fast path
	'ints-10' => static fn () => pool(64, static fn () => [ints(10, 1, 30), ints(10, 1, 30)]),
	'ints-100' => static fn () => pool(64, static fn () => [ints(100, 1, 300), ints(100, 1, 300)]),
	'ints-1000' => static fn () => pool(16, static fn () => [ints(1000, 1, 3000), ints(1000, 1, 3000)]),
	'ints-1000-3-arrays' => static fn () => pool(16, static fn () => [ints(1000, 1, 3000), ints(300, 1, 3000), ints(300, 1, 3000), ints(300, 1, 3000)]),
	// fallbacks: what the PR scans before giving up
	'sparse-1000' => static fn () => pool(16, static fn () => [ints(1000, 1, 1000000000), ints(1000, 1, 1000000000)]),
	'dense-1000-one-far' => static fn () => pool(16, static fn () => [ints(1000, 1, 3000), [...ints(999, 1, 3000), 1000000000]]),
	'ints-1000-string-last' => static fn () => pool(16, static fn () => [ints(1000, 1, 3000), [...ints(999, 1, 3000), '5']]),
	'first-string-last-1000' => static fn () => pool(16, static fn () => [[...ints(999, 1, 3000), '5'], ints(1000, 1, 3000)]),
	// strings: rejected at the first element
	'strings-1000' => static fn () => pool(16, static fn () => [words(1000), words(1000)]),
	'strings-10' => static fn () => pool(64, static fn () => [words(10), words(10)]),
];

$name = $argv[1] ?? 'list';
if ($name === 'list') { echo implode(' ', array_keys($cases)), "\n"; exit; }
$pool = $cases[$name]();
$mask = count($pool) - 1;
$run = static function (int $calls) use ($pool, $mask) { for ($i = 0; $i < $calls; $i++) { $r = array_diff(...$pool[$i & $mask]); } };

if (isset($argv[2])) { $run((int) $argv[2]); exit; }

$out = '';
foreach ($pool as $args) $out .= md5(serialize(array_diff(...$args)));
$t0 = hrtime(true); $run(3); $one = max(1, (hrtime(true) - $t0) / 3);
$calls = max(5, (int) (2e7 / $one));
$t = [];
for ($k = 0; $k < 7; $k++) { $t0 = hrtime(true); $run($calls); $t[] = (hrtime(true) - $t0) / $calls; }
sort($t);
printf("%s %.1f %s\n", $name, $t[3], md5($out));
