<?php
// One unserialize() case per process: ns per call (median of 7) and an md5 of serialize() of the result.
//   php cases.php <case|list> [calls]
// With a call count, makes exactly that many calls and prints nothing (for perf stat).
// Payloads are built with serialize(), which PR #23110 does not change; small ones come from a pool
// of 64 different payloads (fixed seed) so that the branch predictor does not see one string repeated.

mt_srand(23110);

final class Item { public int $id; public string $name; public ?Item $ref = null; public ?Category $cat = null; }
final class Category { public int $id; public string $title; }

function word(): string { return substr(md5((string) mt_rand()), 0, mt_rand(4, 12)); }
function pool(int $n, callable $make): array { $p = []; for ($i = 0; $i < $n; $i++) $p[] = serialize($make()); return $p; }

function session(): array
{
	return ['user_id' => mt_rand(), 'name' => word() . ' ' . word(), 'roles' => ['user', word()],
		'csrf' => md5((string) mt_rand()), 'flash' => [], 'cart' => array_map(static fn () => ['sku' => word(), 'qty' => mt_rand(1, 5), 'price' => mt_rand(100, 9999) / 100], range(1, mt_rand(3, 8))),
		'last_seen' => 1760000000 + mt_rand(0, 86400), 'prefs' => ['lang' => 'en', 'tz' => 'UTC', 'theme' => word()]];
}

/** $n items; every item gets a ref to an earlier item chosen by $pick ($i => index or null) and one of $cats categories. */
function items(int $n, int $cats, callable $pick): array
{
	$c = [];
	for ($i = 0; $i < $cats; $i++) { $x = new Category(); $x->id = $i; $x->title = word(); $c[] = $x; }
	$items = [];
	for ($i = 0; $i < $n; $i++) {
		$it = new Item(); $it->id = $i; $it->name = word();
		$j = $pick($i);
		if ($j !== null) $it->ref = $items[$j];
		if ($cats) $it->cat = $c[mt_rand(0, $cats - 1)];
		$items[] = $it;
	}
	return ['categories' => $c, 'items' => $items];
}

$cases = [
	// no references
	'array-10' => static fn () => pool(64, static fn () => array_map(static fn () => mt_rand(0, 1) ? mt_rand() : word(), range(1, 10))),
	'session' => static fn () => pool(64, 'session'),
	'ints-1000' => static fn () => pool(4, static fn () => array_map(static fn () => mt_rand(), range(1, 1000))),
	'ints-6200' => static fn () => pool(4, static fn () => array_map(static fn () => mt_rand(), range(1, 6200))),
	'strings-50k' => static fn () => pool(2, static fn () => array_map(static fn () => word(), range(1, 50000))),
	'objects-5000' => static fn () => pool(2, static fn () => items(5000, 0, static fn () => null)),
	// object references (r:)
	'objects-5000-50-categories' => static fn () => pool(2, static fn () => items(5000, 50, static fn () => null)),
	'objects-20000-ref-previous' => static fn () => pool(2, static fn () => items(20000, 0, static fn ($i) => $i ? $i - 1 : null)),
	'objects-20000-ref-random' => static fn () => pool(2, static fn () => items(20000, 0, static fn ($i) => $i ? mt_rand(0, $i - 1) : null)),
	// value references (R:): 6,200 ints and 100,000 references to random ones
	'ints-6200-100k-R' => static fn () => pool(2, static function () {
		$a = array_map(static fn () => mt_rand(), range(1, 6200));
		$b = [];
		for ($i = 0; $i < 100000; $i++) $b[] = &$a[mt_rand(0, 6199)];
		return [$a, $b];
	}),
];

$name = $argv[1] ?? 'list';
if ($name === 'list') { echo implode(' ', array_keys($cases)), "\n"; exit; }
$pool = $cases[$name]();
$mask = count($pool) - 1;
$run = static function (int $calls) use ($pool, $mask) { for ($i = 0; $i < $calls; $i++) { $r = unserialize($pool[$i & $mask]); } };

if (isset($argv[2])) { $run((int) $argv[2]); exit; }

$out = '';
foreach ($pool as $s) $out .= md5(serialize(unserialize($s)));
$calls = max(5, (int) (2e7 / strlen($pool[0])));
$t = [];
for ($k = 0; $k < 7; $k++) { $t0 = hrtime(true); $run($calls); $t[] = (hrtime(true) - $t0) / $calls; }
sort($t);
printf("%s %.1f %s %d\n", $name, $t[3], md5($out), strlen($pool[0]));
