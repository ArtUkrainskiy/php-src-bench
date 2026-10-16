<?php
// One mb_substr()/mb_strpos() case per process: ns per call (median of 7) and an md5 of the last result.
//   php cases.php <case|list> [calls]
// With a call count, makes exactly that many calls and prints nothing (for perf stat).
// "flagged" strings went through mb_check_encoding() first (valid-UTF-8 flag set), as after preg_*() with /u.
require dirname(__DIR__, 2) . '/lib/Corpus.php';

$texts = [
	'en-title' => fn() => substr(Corpus::text('en', 60), 0, strpos(Corpus::text('en', 60), "\n")),
	'ru-title' => fn() => substr(Corpus::text('ru', 60), 0, strpos(Corpus::text('ru', 60), "\n")),
	'en-1k' => fn() => Corpus::text('en', 1024),
	'ru-1k' => fn() => Corpus::text('ru', 1024),
	'zh-1k' => fn() => Corpus::text('zh', 1024),
	'emoji-1k' => fn() => Corpus::text('emoji', 1024),
	'en-64k' => fn() => Corpus::text('en', 65536),
	'ru-64k' => fn() => Corpus::text('ru', 65536),
];
$calls = [
	'head10' => 'mb_substr($s, 0, 10)',
	'mid20' => 'mb_substr($s, $half, 20)',
	'tail20' => 'mb_substr($s, -20)',
	'firsthalf' => 'mb_substr($s, 0, $half)',
	'strpos-mid' => 'mb_strpos($s, $needle, $half)',
];
$plan = [
	'en-title' => ['head10'], 'ru-title' => ['head10'],
	'en-1k' => ['mid20'], 'ru-1k' => ['mid20', 'tail20', 'firsthalf', 'strpos-mid'], 'zh-1k' => ['mid20'], 'emoji-1k' => ['mid20'],
	'en-64k' => ['mid20'], 'ru-64k' => ['mid20', 'tail20', 'strpos-mid'],
];
$cases = [];
foreach ($plan as $text => $list) {
	foreach ($list as $call) {
		$cases["$call@$text"] = [$calls[$call], $text, true];
	}
}
$cases['mid20@ru-1k-plain'] = [$calls['mid20'], 'ru-1k', false];
$cases['head10@ru-title-plain'] = [$calls['head10'], 'ru-title', false];

$name = $argv[1] ?? 'list';
if ($name === 'list') { echo implode(' ', array_keys($cases)), "\n"; exit; }
[$code, $text, $flagged] = $cases[$name];
$src = $texts[$text]();
$copy = strrev(strrev($src)); // mb_strlen() sets the flag, so measure lengths on a copy
$half = intdiv(mb_strlen($copy, 'UTF-8'), 2);
$needle = mb_substr($copy, -12, 6, 'UTF-8');
$s = strrev(strrev($src));
if ($flagged) mb_check_encoding($s, 'UTF-8');
mb_internal_encoding('UTF-8');
$run = eval('return static function (int $calls, string $s, int $half, string $needle) { $r = ""; for ($i = 0; $i < $calls; $i++) { $r = ' . $code . '; } return md5((string) $r); };');
if (isset($argv[2])) { $run((int) $argv[2], $s, $half, $needle); exit; }

$out = $run(300, $s, $half, $needle);
$t0 = hrtime(true); $run(3, $s, $half, $needle); $one = max(1, (hrtime(true) - $t0) / 3);
$n = max(5, (int) (2e7 / $one));
$t = [];
for ($k = 0; $k < 7; $k++) { $t0 = hrtime(true); $run($n, $s, $half, $needle); $t[] = (hrtime(true) - $t0) / $n; }
sort($t);
printf("%s %.1f %s %d\n", $name, $t[3], $out, strlen($s));
