<?php
// One var_export($x, true) case per process: ns per call (median of 7) and an md5 of the outputs.
//   php cases.php <case|list> [calls]
// With a call count, makes exactly that many calls and prints nothing (for perf stat).
// Small values come from a pool of 64 different ones (fixed seed).

mt_srand(23189);
final class Pt { public $x; public $y; public $label; }
function word(): string { return substr(str_shuffle('abcdefghijklmnopqrstuvwxyz_ABCDEFGHIJ'), 0, mt_rand(3, 12)); }
/** $len bytes of random words; with $every > 0, one of $chars follows a word with probability 1/$every. */
function text(int $len, int $every, array $chars = ["'", '\\']): string
{
	$s = '';
	while (strlen($s) < $len) $s .= word() . ($every && mt_rand(1, $every) === 1 ? $chars[mt_rand(0, count($chars) - 1)] : '') . ' ';
	return substr($s, 0, $len);
}
function pool(int $n, callable $f): array { $p = []; for ($i = 0; $i < $n; $i++) $p[] = $f(); return $p; }
function config(int $depth): array
{
	$a = [];
	for ($i = mt_rand(4, 8); $i > 0; $i--) {
		$k = word();
		$a[$k] = $depth > 0 && mt_rand(0, 2) === 0 ? config($depth - 1) : [mt_rand(), word(), mt_rand(0, 1) === 1, null, 'App\\Service\\' . ucfirst(word())][mt_rand(0, 4)];
	}
	return $a;
}

$cases = [
	'int' => static fn () => pool(64, static fn () => mt_rand()),
	'string-20' => static fn () => pool(64, static fn () => substr(word() . word() . word(), 0, 20)),
	'string-20-quotes' => static fn () => pool(64, static fn () => "it's a \\path\\" . word()),
	'array-10-mixed' => static fn () => pool(64, static fn () => ['id' => mt_rand(), 'name' => word(), 'ok' => true, 'ratio' => mt_rand() / 7, 'tags' => [word(), word()], 'parent' => null, 'path' => '/var/' . word(), 'n' => 3, 'e' => '', 'x' => word()]),
	'config-nested' => static fn () => pool(16, static fn () => config(3)),
	'ints-1000' => static fn () => pool(4, static fn () => array_map(static fn () => mt_rand(), range(1, 1000))),
	'strings-1000' => static fn () => pool(4, static fn () => array_map(static fn () => word(), range(1, 1000))),
	'assoc-1000' => static fn () => pool(4, static function () { $a = []; for ($i = 0; $i < 1000; $i++) $a[word() . $i] = word(); return $a; }),
	'objects-100' => static fn () => pool(4, static fn () => array_map(static function () { $p = new Pt(); $p->x = mt_rand(); $p->y = mt_rand() / 3; $p->label = word(); return $p; }, range(1, 100))),
	'string-64k-plain' => static fn () => pool(2, static fn () => text(65536, 0)),
	'string-64k-quotes' => static fn () => pool(2, static fn () => text(65536, 8)),
	'string-1k-nul' => static fn () => pool(8, static fn () => text(1024, 4, ["\0"])),
];

$name = $argv[1] ?? 'list';
if ($name === 'list') { echo implode(' ', array_keys($cases)), "\n"; exit; }
$pool = $cases[$name]();
$mask = count($pool) - 1;
$run = static function (int $calls) use ($pool, $mask) { for ($i = 0; $i < $calls; $i++) { $r = var_export($pool[$i & $mask], true); } };

if (isset($argv[2])) { $run((int) $argv[2]); exit; }

$out = '';
foreach ($pool as $v) $out .= md5(var_export($v, true));
$calls = max(20, (int) (2e7 / strlen(var_export($pool[0], true))));
$t = [];
for ($k = 0; $k < 7; $k++) { $t0 = hrtime(true); $run($calls); $t[] = (hrtime(true) - $t0) / $calls; }
sort($t);
printf("%s %.1f %s\n", $name, $t[3], md5($out));
