<?php
// One html-function case per process: ns per call (median of 7) and an md5 of the outputs.
//   php cases.php <case|list> [calls]
// With a call count, makes exactly that many calls and prints nothing (for perf stat).
// Short strings come from a pool of 256 different strings (fixed seed).

mt_srand(23961);
function word(): string { return substr(str_shuffle('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'), 0, mt_rand(3, 9)); }
function title(int $len, bool $special): string
{
	$s = '';
	while (strlen($s) < $len) $s .= word() . ($special && mt_rand(0, 3) === 0 ? ['&', '"', "'", '<'][mt_rand(0, 3)] : ' ');
	return substr($s, 0, $len);
}
function text1k(): string { $s = ''; while (strlen($s) < 1024) $s .= word() . (mt_rand(0, 40) ? ' ' : ' & '); return substr($s, 0, 1024); }
function pool(int $n, callable $f): array { $p = []; for ($i = 0; $i < $n; $i++) $p[] = $f(); return $p; }

$q = ENT_QUOTES | ENT_SUBSTITUTE | ENT_HTML401;
// [expression with $s, pool maker]
$cases = [
	'hsc-8-utf8' => ['htmlspecialchars($s, ' . $q . ', "UTF-8")', static fn () => pool(256, static fn () => title(8, false))],
	'hsc-40-utf8' => ['htmlspecialchars($s, ' . $q . ', "UTF-8")', static fn () => pool(256, static fn () => title(40, false))],
	'hsc-40-default' => ['htmlspecialchars($s)', static fn () => pool(256, static fn () => title(40, false))],
	'hsc-40-special-default' => ['htmlspecialchars($s)', static fn () => pool(256, static fn () => title(40, true))],
	'hsc-40-lower-utf8' => ['htmlspecialchars($s, ' . $q . ', "utf-8")', static fn () => pool(256, static fn () => title(40, false))],
	'hsc-40-iso-8859-1' => ['htmlspecialchars($s, ' . $q . ', "ISO-8859-1")', static fn () => pool(256, static fn () => title(40, false))],
	'hsc-40-cp1251' => ['htmlspecialchars($s, ' . $q . ', "cp1251")', static fn () => pool(256, static fn () => title(40, false))],
	'hsc-40-macroman' => ['htmlspecialchars($s, ' . $q . ', "MacRoman")', static fn () => pool(256, static fn () => title(40, false))],
	'hsc-1k-default' => ['htmlspecialchars($s)', static fn () => pool(16, 'text1k')],
	'htmlentities-40-default' => ['htmlentities($s)', static fn () => pool(256, static fn () => title(40, true))],
	'decode-40-default' => ['html_entity_decode($s)', static fn () => pool(256, static fn () => htmlspecialchars(title(40, true)))],
	'translation-table' => ['get_html_translation_table(HTML_SPECIALCHARS)', static fn () => ['x']],
];

$name = $argv[1] ?? 'list';
if ($name === 'list') { echo implode(' ', array_keys($cases)), "\n"; exit; }
[$expr, $make] = $cases[$name];
$pool = $make();
$mask = count($pool) - 1;
$run = eval('return static function (int $calls) use ($pool, $mask) { for ($i = 0; $i < $calls; $i++) { $s = $pool[$i & $mask]; $r = ' . $expr . '; } };');

if (isset($argv[2])) { $run((int) $argv[2]); exit; }

$out = '';
foreach ($pool as $s) $out .= md5(serialize(eval('return ' . $expr . ';')));
$calls = 200000;
$t = [];
for ($k = 0; $k < 7; $k++) { $t0 = hrtime(true); $run($calls); $t[] = (hrtime(true) - $t0) / $calls; }
sort($t);
printf("%s %.1f %s\n", $name, $t[3], md5($out));
