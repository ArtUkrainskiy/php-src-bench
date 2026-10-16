<?php
// One mb_substr()/mb_strpos() case per process: ns per call (median of 7) and an md5 of the last result.
//   php cases.php <case|list> [calls]
// With a call count, makes exactly that many calls and prints nothing (for perf stat).
// "flagged" strings went through mb_check_encoding() first (valid-UTF-8 flag set), as after preg_*() with /u.
require dirname(__DIR__, 2) . '/lib/Corpus.php';

$langs = ['en', 'es', 'ru', 'ar', 'hi', 'zh', 'ja', 'ko', 'emoji'];
$texts = [];
foreach ($langs as $l) {
	$texts["$l-title"] = fn() => strstr(Corpus::text($l, 200), "\n", true); // first sentence
	$texts["$l-1k"] = fn() => Corpus::text($l, 1024);
	$texts["$l-64k"] = fn() => Corpus::text($l, 65536);
}
$calls = [
	'head10' => 'mb_substr($s, 0, 10)',
	'mid20' => 'mb_substr($s, $half, 20)',
	'tail20' => 'mb_substr($s, -20)',
	'firsthalf' => 'mb_substr($s, 0, $half)',
	'strpos-mid' => 'mb_strpos($s, $needle, $half)',
];
// The same calls for every language; the other call shapes on English.
$cases = [];
foreach ($langs as $l) {
	$cases["head10@$l-title"] = [$calls['head10'], "$l-title", true];
	$cases["mid20@$l-1k"] = [$calls['mid20'], "$l-1k", true];
	$cases["mid20@$l-64k"] = [$calls['mid20'], "$l-64k", true];
}
foreach (['tail20', 'firsthalf', 'strpos-mid'] as $c) {
	$cases["$c@en-1k"] = [$calls[$c], 'en-1k', true];
}
$cases['tail20@en-64k'] = [$calls['tail20'], 'en-64k', true];
$cases['strpos-mid@en-64k'] = [$calls['strpos-mid'], 'en-64k', true];
$cases['head10@en-title-plain'] = [$calls['head10'], 'en-title', false];
$cases['mid20@en-1k-plain'] = [$calls['mid20'], 'en-1k', false];
$cases['mid20@zh-1k-plain'] = [$calls['mid20'], 'zh-1k', false];

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
