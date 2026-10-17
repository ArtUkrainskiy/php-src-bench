<?php
// Behaviour of destructuring assignments whose right side is an array literal.
// Run with two php builds and diff the output.

set_error_handler(static function (int $no, string $msg): bool {
    echo "  [warning] $msg\n";
    return true;
});

function f(string $label, $value = null)
{
    echo "  eval $label\n";
    return $value ?? $label;
}

final class D
{
    public function __construct(public string $name) {}
    public function __destruct() { echo "  destruct {$this->name}\n"; }
}

final class Typed
{
    public int $int = 0;
    public string $string = '';
    public static int $static = 0;
}

final class Box implements ArrayAccess
{
    public array $data = [];
    public function offsetExists($o): bool { return isset($this->data[$o]); }
    public function offsetGet($o): mixed { echo "  offsetGet $o\n"; return $this->data[$o]; }
    public function offsetSet($o, $v): void { echo "  offsetSet " . var_export($o, true) . "\n"; $this->data[$o ?? count($this->data)] = $v; }
    public function offsetUnset($o): void {}
}

$cases = [
    'swap ints' => static function () { $a = 1; $b = 2; [$a, $b] = [$b, $a]; return [$a, $b]; },
    'swap strings' => static function () { $a = 'x' . mt_getrandmax(); $b = 'y'; [$a, $b] = [$b, $a]; return [$a, $b]; },
    'swap arrays' => static function () { $a = [1, 2]; $b = ['k' => 'v']; [$a, $b] = [$b, $a]; return [$a, $b]; },
    'rotate three' => static function () { $a = 1; $b = 2; $c = 3; [$a, $b, $c] = [$b, $c, $a]; return [$a, $b, $c]; },
    'list() and array()' => static function () { $a = 1; $b = 2; list($a, $b) = array($b, $a); return [$a, $b]; },
    'constants' => static function () { [$a, $b] = [1, 'two']; return [$a, $b]; },
    'fibonacci step' => static function () { $a = 3; $b = 5; [$a, $b] = [$b, $a + $b]; return [$a, $b]; },
    'more values than targets' => static function () { [$a] = [f('one'), f('two')]; return $a; },
    'skipped target' => static function () { [, $b] = [f('one'), f('two')]; return $b; },
    'skipped in the middle' => static function () { [$a, , $c] = [f('one'), f('two'), f('three')]; return [$a, $c]; },
    'undefined variable on the right' => static function () { [$a, $b] = [$undefined, 1]; return [$a, $b]; },
    'value changed by a later value' => static function () { $x = 1; [$a, $b] = [$x, $x = 5]; return [$a, $b, $x]; },
    'value changed by a later value, by reference' => static function () { $x = 1; $inc = static function () use (&$x) { return ++$x; }; [$a, $b] = [$x, $inc()]; return [$a, $b, $x]; },
    'same variable twice on the left' => static function () { [$a, $a] = [1, 2]; return $a; },
    'same variable twice on the right' => static function () { $a = 7; [$a, $b] = [$a, $a]; return [$a, $b]; },
    'order of evaluation' => static function () { $arr = []; [$arr[f('i')], $arr[f('j')]] = [f('v1'), f('v2')]; return $arr; },
    'target index uses a variable assigned earlier' => static function () { $i = 0; $arr = []; [$i, $arr[$i]] = [1, 'x']; return [$i, $arr]; },
    'append targets' => static function () { $arr = []; [$arr[], $arr[]] = [1, 2]; return $arr; },
    'nested' => static function () { [[$a, $b], $c] = [[1, 2], 3]; return [$a, $b, $c]; },
    'nested with variables' => static function () { $a = 1; $b = 2; [[$a, $b], $c] = [[$b, $a], $a]; return [$a, $b, $c]; },
    'nested target, scalar value' => static function () { [[$a, $b], $c] = [5, 6]; return [$a, $b, $c]; },
    'nested keyed' => static function () { [['x' => $a], $c] = [['x' => 1], 2]; return [$a, $c]; },
    'properties' => static function () { $o = new stdClass; $o->a = 1; $o->b = 2; [$o->a, $o->b] = [$o->b, $o->a]; return $o; },
    'typed properties coerce' => static function () { $t = new Typed; [$t->int, $t->string] = ['42', 43]; return $t; },
    'typed property error' => static function () { $t = new Typed; $a = 1; try { [$a, $t->int, $b] = [2, 'nope', f('third')]; } catch (TypeError $e) { echo "  TypeError\n"; } return [$a, $t, isset($b)]; },
    'static property' => static function () { $a = 5; [Typed::$static, $a] = [$a, Typed::$static]; $r = [Typed::$static, $a]; Typed::$static = 0; return $r; },
    'ArrayAccess targets' => static function () { $box = new Box; [$box['k'], $box[]] = [1, 2]; return $box->data; },
    'ArrayAccess values' => static function () { $box = new Box; $box->data = ['p' => 1, 'q' => 2]; [$a, $b] = [$box['q'], $box['p']]; return [$a, $b]; },
    'string offset target' => static function () { $s = 'abc'; [$s[0], $s[2]] = ['X', 'Z']; return $s; },
    'variable variables' => static function () { $n = 'dyn'; $dyn = 1; $b = 2; [$$n, $b] = [$b, $$n]; return [$dyn, $b]; },
    'references on the right' => static function () { $a = 1; $b = 2; $r = &$a; [$a, $b] = [$b, $r]; return [$a, $b, $r]; },
    'reference to a target' => static function () { $a = 1; $b = 2; $r = &$b; [$a, $b] = [$b, $a]; return [$a, $b, $r]; },
    'objects are not copied' => static function () { $o = new stdClass; $p = new stdClass; $o->n = 'o'; $p->n = 'p'; [$o, $p] = [$p, $o]; return [$o->n, $p->n]; },
    'destructors, all taken' => static function () { $a = new D('old a'); $b = new D('old b'); [$a, $b] = [new D('new a'), new D('new b')]; echo "  assigned\n"; return [$a->name, $b->name]; },
    'destructors, value not taken' => static function () { $a = new D('old a'); [$a] = [new D('new a'), new D('extra')]; echo "  assigned\n"; return $a->name; },
    'destructors, target skipped' => static function () { $b = new D('old b'); [, $b] = [new D('skipped'), new D('new b')]; echo "  assigned\n"; return $b->name; },
    'exception in a value' => static function () { $a = 1; $b = 2; try { [$a, $b] = [f('one'), throw new Exception('boom'), f('never')]; } catch (Exception $e) { echo "  caught\n"; } return [$a, $b]; },
    'exception in a value with objects' => static function () { $a = 1; try { [$a, $b] = [new D('first'), throw new Exception('boom')]; } catch (Exception $e) { echo "  caught\n"; } return $a; },
    'generator' => static function () { $g = (static function () { [$a, $b] = [yield 'y1', yield 'y2']; return [$a, $b]; })(); $out = [$g->current()]; $out[] = $g->send('s1'); $g->send('s2'); $out[] = $g->getReturn(); return $out; },
    'result used' => static function () { $a = 1; $b = 2; $r = ([$a, $b] = [$b, $a]); return [$a, $b, $r]; },
    'in a condition' => static function () { $a = 1; $b = 2; if ([$a, $b] = [$b, $a]) { return [$a, $b]; } return null; },
    'fewer values than targets' => static function () { [$a, $b] = [1]; return [$a, $b]; },
    'keyed' => static function () { $a = 1; $b = 2; ['x' => $a, 'y' => $b] = ['x' => $b, 'y' => $a]; return [$a, $b]; },
    'reference target' => static function () { $x = 1; $arr = [&$x]; [&$a] = $arr; $a = 2; return $x; },
    'spread on the right' => static function () { $rest = [2, 3]; [$a, $b, $c] = [1, ...$rest]; return [$a, $b, $c]; },
    'by-reference value' => static function () { $x = 1; [$a, $b] = [&$x, 2]; $a = 9; return [$a, $b, $x]; },
    'loop of swaps' => static function () { $a = 0; $b = 1; for ($i = 0; $i < 10; $i++) { [$a, $b] = [$b, $a + $b]; } return [$a, $b]; },
    'this' => static function () { $o = new class { public $a = 1; public $b = 2; public function swap() { [$this->a, $this->b] = [$this->b, $this->a]; return [$this->a, $this->b]; } }; return $o->swap(); },
    'call results' => static function () { [$a, $b] = [strtoupper('x'), strrev('abc')]; return [$a, $b]; },
    'global scope style variables' => static function () { $GLOBALS['ga'] = 1; $GLOBALS['gb'] = 2; [$GLOBALS['ga'], $GLOBALS['gb']] = [$GLOBALS['gb'], $GLOBALS['ga']]; return [$GLOBALS['ga'], $GLOBALS['gb']]; },
];

foreach ($cases as $name => $case) {
    echo "== $name\n";
    try {
        $result = $case();
        echo '  => ', json_encode($result), "\n";
    } catch (Throwable $e) {
        echo '  !! ', get_class($e), ': ', $e->getMessage(), "\n";
    }
}
echo "done\n";
