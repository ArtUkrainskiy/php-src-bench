<?php
// Differential test for php-src PR #24157 (array_push() bulk append to packed arrays).
// Records after every call: return value, exception, the array (keys and values), key()/current(),
// the next free index (by appending a marker to a copy), and memory_get_usage() relative to
// before the call (shows a different table size).
//   php -n difftest.php [fuzz-count] [seed]

$fuzz = (int) ($argv[1] ?? 2000);
mt_srand((int) ($argv[2] ?? 1));

function state(array $a): array {
	$k = key($a);
	$c = $k === null ? null : current($a);
	$probe = $a;
	try { $probe[] = 'marker'; $next = array_key_last($probe); } catch (Error $e) { $next = 'full'; }
	return ['keys' => array_keys($a), 'vals' => array_map(static fn ($v) => is_object($v) ? 'obj#' . spl_object_id($v) : $v, array_values($a)), 'key' => $k, 'cur' => is_object($c) ? 'obj' : $c, 'next' => $next, 'count' => count($a)];
}
function out(string $label, array $r): void { echo $label, ' ', json_encode($r, JSON_PARTIAL_OUTPUT_ON_ERROR), "\n"; }
function push(array &$a, array $vals): array {
	$m0 = memory_get_usage();
	try { $ret = array_push($a, ...$vals); $ex = null; } catch (Throwable $t) { $ret = null; $ex = get_class($t) . ': ' . $t->getMessage(); }
	return ['ret' => $ret, 'ex' => $ex, 'mem' => memory_get_usage() - $m0, 'st' => state($a)];
}

// Starting arrays; each builder makes a fresh array so the state (packed, holes, next index, pointer) is known.
$starts = [
	'literal-empty' => static fn () => [],
	'values-empty' => static fn () => array_values([]),
	'range-0' => static fn () => array_slice([1], 1),
	'neg-next' => static function () { $a = [-3 => 0]; unset($a[-3]); return $a; },
	'neg-next-copy' => static function () { $a = [-3 => 0]; unset($a[-3]); $c = $a; return $c; },
	'hash' => static fn () => ['a' => 1, 'b' => 2],
	'hash-int' => static fn () => [5 => 1, 2 => 2],
	'packed-gap-key' => static fn () => [0 => 1, 1 => 2, 5 => 3],
	'unset-last' => static function () { $a = [0, 1, 2]; unset($a[2]); return $a; },
	'unset-mid' => static function () { $a = [0, 1, 2, 3]; unset($a[1]); return $a; },
	'unset-first' => static function () { $a = [0, 1, 2, 3]; unset($a[0]); return $a; },
	'popped' => static function () { $a = [0, 1, 2, 3]; array_pop($a); return $a; },
	'shifted' => static function () { $a = [0, 1, 2, 3]; array_shift($a); return $a; },
	'ptr-mid' => static function () { $a = [10, 11, 12, 13]; next($a); next($a); return $a; },
	'ptr-end' => static function () { $a = [10, 11, 12, 13]; end($a); return $a; },
	'ptr-past-end' => static function () { $a = [10, 11, 12, 13]; end($a); next($a); return $a; },
	'ptr-past-end-full8' => static function () { $a = range(0, 7); end($a); next($a); return $a; },
	'holes-many' => static function () { $a = range(0, 15); for ($i = 0; $i < 14; $i++) unset($a[$i]); return $a; },
	'holes-many-ptr' => static function () { $a = range(0, 15); for ($i = 0; $i < 14; $i++) unset($a[$i]); end($a); next($a); return $a; },
	'holes-full' => static function () { $a = range(0, 7); unset($a[3]); return $a; },
	'holes-full-16' => static function () { $a = range(0, 15); unset($a[0], $a[5], $a[9]); return $a; },
	'holes-half' => static function () { $a = range(0, 15); for ($i = 0; $i < 9; $i++) unset($a[$i]); return $a; },
	'refs-inside' => static function () { $x = 1; $a = [&$x, 2]; return $a; },
	'big-next' => static fn () => [PHP_INT_MAX - 1 => 1],
	'max-next' => static fn () => [PHP_INT_MAX => 1],
];
foreach ([1, 2, 3, 6, 7, 8, 9, 15, 16, 17, 31, 32, 33, 1023, 1024, 1025] as $n) {
	$starts["range-$n"] = static fn () => range(0, $n - 1);
	$starts["fill-$n"] = static function () use ($n) { $a = []; for ($i = 0; $i < $n; $i++) $a[] = $i; return $a; };
}
$valueSets = static function (int $argc) {
	if ($argc === 0) return ['ints' => [], 'strings' => [], 'mixed' => []]; // range() would count down
	$s = [];
	$s['ints'] = range(100, 99 + $argc);
	$s['strings'] = array_map(static fn ($i) => str_repeat('s', $i % 5) . $i, range(1, $argc));
	$s['mixed'] = array_map(static fn ($i) => [$i % 4 === 0 ? [$i] : ($i % 4 === 1 ? "x$i" : ($i % 4 === 2 ? 1.5 * $i : null))][0], range(1, $argc));
	return $s;
};
$argcs = [0, 1, 2, 3, 4, 7, 8, 9, 15, 16, 17, 100, 1000, 1025];

foreach ($starts as $sname => $make) {
	foreach ($argcs as $argc) {
		foreach ($valueSets($argc) as $vname => $vals) {
			$a = $make();
			out("push $sname/$argc/$vname", push($a, $vals));
			// a second push onto the result, then direct appends
			out("push2 $sname/$argc/$vname", push($a, [7, 8, 9]));
		}
	}
}

// copy-on-write: the original must not change
$orig = [1, 2, 3]; $copy = $orig; array_push($copy, 4, 5);
out('cow', ['orig' => $orig, 'copy' => $copy]);
$orig = []; $copy = $orig; array_push($copy, 4, 5);
out('cow-empty', ['orig' => $orig, 'copy' => $copy]);
// self push
$a = [1, 2]; array_push($a, $a, $a);
out('self', ['a' => $a]);
$a = [1, 2]; array_push($a, ...$a);
out('self-spread', ['a' => $a]);
// references
$x = 1; $a = [0]; array_push($a, $x); $x = 2;
out('by-value', ['a' => $a]);
$a = [0]; $r = &$a; array_push($r, 1, 2);
out('ref-array', ['a' => $a, 'r' => $r]);
unset($r, $a);
// object and refcounted values: refcounts after the array is freed
$o = new stdClass; $s = str_repeat('z', 50);
$m0 = memory_get_usage(); $rc = [0]; array_push($rc, $o, $s, $o, $s, [$s]); unset($rc);
$w = WeakReference::create($o); unset($o);
out('refcounts', ['mem' => memory_get_usage() - $m0, 'freed' => $w->get() === null, 's' => strlen($s)]);
// typed property and object property
final class T { public array $a = [1, 2]; public $u = []; }
$t = new T; array_push($t->a, 3, 4); array_push($t->u, 'p', 'q');
out('prop', ['a' => $t->a, 'u' => $t->u]);
// foreach by reference while pushing (array iterators)
$a = [1, 2, 3]; $seen = [];
foreach ($a as $k => &$v) { $seen[] = $k; if ($k < 3) array_push($a, $k * 10, $k * 10 + 1); }
unset($v);
out('foreach-ref', ['a' => $a, 'seen' => $seen]);
$a = range(0, 7); $seen = [];
foreach ($a as $k => &$v) { $seen[] = $k; if ($k === 7) array_push($a, ...range(100, 120)); }
unset($v);
out('foreach-ref-grow', ['a' => $a, 'seen' => $seen]);
$a = [1, 2, 3]; $seen = [];
foreach ($a as $k => $v) { $seen[] = $k; array_push($a, 9, 9); }
out('foreach-val', ['n' => count($a), 'seen' => $seen]);
// errors
$a = [PHP_INT_MAX => 1];
try { array_push($a, 1, 2); } catch (Throwable $e) { out('err-max', ['ex' => $e->getMessage(), 'a' => $a]); }

// fuzz: random operation sequences, state after each push
$ops = ['push', 'push', 'push', 'unset', 'pop', 'shift', 'set', 'next', 'end', 'reset', 'copy', 'append'];
for ($k = 0; $k < $fuzz; $k++) {
	$a = mt_rand(0, 3) === 0 ? [] : range(0, mt_rand(0, 40));
	$log = [];
	for ($step = 0; $step < 12; $step++) {
		$op = $ops[mt_rand(0, count($ops) - 1)];
		switch ($op) {
			case 'push': $argc = [0, 1, 1, 2, 3, 5, 9, 17, 40][mt_rand(0, 8)]; $res = push($a, array_slice(range(1000, 1050), 0, $argc)); $log[] = [$op, $argc, $res]; continue 2;
			case 'unset': if ($a) { $keys = array_keys($a); unset($a[$keys[mt_rand(0, count($keys) - 1)]]); } break;
			case 'pop': array_pop($a); break;
			case 'shift': array_shift($a); break;
			case 'set': $a[mt_rand(0, 60)] = 's'; break;
			case 'next': next($a); break;
			case 'end': end($a); break;
			case 'reset': reset($a); break;
			case 'copy': $b = $a; $a = $b; break;
			case 'append': $a[] = 'ap'; break;
		}
		$log[] = [$op, state($a)];
	}
	out("fuzz $k", $log);
}
