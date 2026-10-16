<?php
// One htmlspecialchars()/htmlentities() case per process: ns per call (median of 7) and an md5 of the last result.
//   php cases.php <case|list> [calls]
// With a call count, makes exactly that many calls and prints nothing (for perf stat).
// Inputs and calls are those of suites/htmlspecialchars.php.
require dirname(__DIR__, 3) . '/lib/Corpus.php';
$suite = require dirname(__DIR__, 3) . '/suites/htmlspecialchars.php';

$prefix = [
	'htmlspecialchars' => 'hsc', 'htmlspecialchars !double_encode' => 'hsc-nodbl', 'htmlspecialchars ENT_DISALLOWED' => 'hsc-disallowed',
	'htmlspecialchars cp1251' => 'hsc-cp1251', 'htmlspecialchars Shift_JIS' => 'hsc-sjis', 'htmlspecialchars BIG5' => 'hsc-big5', 'htmlentities' => 'ent',
];
$cases = [];
foreach ($suite['cases'] as $title => $case) {
	foreach ($case['inputs'] as $input) {
		$cases[$prefix[$title] . '@' . $input] = [$case['code'], $input];
	}
}

$name = $argv[1] ?? 'list';
if ($name === 'list') { echo implode(' ', array_keys($cases)), "\n"; exit; }
[$code, $input] = $cases[$name];
$s = $suite['inputs'][$input];
if ($s instanceof Closure) $s = $s();
$run = eval('return static function (int $calls, string $s) { $r = ""; for ($i = 0; $i < $calls; $i++) { $r = ' . $code . '; } return md5($r); };');
if (isset($argv[2])) { $run((int) $argv[2], $s); exit; }

$out = $run(300, $s);
$t0 = hrtime(true); $run(3, $s); $one = max(1, (hrtime(true) - $t0) / 3);
$calls = max(5, (int) (2e7 / $one));
$t = [];
for ($k = 0; $k < 7; $k++) { $t0 = hrtime(true); $run($calls, $s); $t[] = (hrtime(true) - $t0) / $calls; }
sort($t);
printf("%s %.1f %s %d\n", $name, $t[3], $out, strlen($s));
