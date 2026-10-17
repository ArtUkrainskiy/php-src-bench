<?php
// Cases for the nested and the untaken-value paths; each runs in its own process so that
// compile errors and fatal errors are part of the output too. Compare the output of builds.
$cases = [
    'nested swap' => '$a=1;$b=2;$c=3; [[$a,$b],$c] = [[$b,$c],$a]; var_dump($a,$b,$c);',
    'nested three levels' => '$a=1;$b=2;$c=3; [[[$a],$b],$c] = [[[$c],$a],$b]; var_dump($a,$b,$c);',
    'nested with untaken inner object' => 'class D{function __construct(public $n){} function __destruct(){echo "destruct $this->n\n";}}
        $a=0; [[$a], $c] = [[new D("taken"), new D("untaken")], new D("c")]; echo "after\n"; unset($a,$c); echo "end\n";',
    'nested from a function, destructor order' => 'class D{function __construct(public $n){} function __destruct(){echo "destruct $this->n\n";}}
        function f(){ return [new D("f0"), new D("f1")]; } [[$a], $c] = [f(), new D("c")]; echo "after\n"; unset($a,$c); echo "end\n";',
    'nested inner has fewer values' => '[[$a,$b],$c] = [[1],2]; var_dump($a,$b,$c);',
    'nested inner keyed value' => '[[$a,$b]] = [["x"=>1,"y"=>2]]; var_dump($a,$b);',
    'nested inner keyed target' => '[["x"=>$a]] = [["x"=>1]]; var_dump($a);',
    'nested inner value not an array' => '[[$a],[$b]] = [[1],2]; var_dump($a,$b);',
    'nested inner value is a string' => '[[$a]] = ["ab"]; var_dump($a);',
    'nested inner value is null' => '[[$a]] = [null]; var_dump($a);',
    'nested empty inner list' => '[[]] = [[1]];',
    'nested mix list and []' => '[list($a)] = [[1]];',
    'nested inner spread' => '[[$a]] = [[...[1]]]; var_dump($a);',
    'nested inner reference value' => '$x=1; [[$a]] = [[&$x]]; $a=2; var_dump($x,$a);',
    'nested inner reference target' => '$x=1; [[&$a]] = [[1]]; var_dump($a);',
    'untaken undefined variable' => 'function f(){ [, $b] = [$undef, 2]; var_dump($b); } f();',
    'untaken undefined variable order' => 'function f(){ [$a, , $c] = [$u1, $u2, $u3]; var_dump($a, $c); } f();',
    'untaken variable in a function, straight line' => 'class D{function __construct(public $n){} function __destruct(){echo "destruct $this->n\\n";}} function u(){ $x=new D("old x"); $y=new D("y"); [, $x, $y] = [$x, 1, 2]; echo "assigned\\n"; } u();',
    'untaken call result in a function' => 'class D{function __construct(public $n){} function __destruct(){echo "destruct $this->n\\n";}} function d($n){ return new D($n); } function u(){ $y=new D("y"); [, $y] = [d("call"), 1]; echo "assigned\\n"; } u();',
    'extra call result in a function' => 'class D{function __construct(public $n){} function __destruct(){echo "destruct $this->n\\n";}} function d($n){ return new D($n); } function u(){ $y=new D("y"); [$y] = [1, d("extra")]; echo "assigned\\n"; } u();',
    'untaken variable with object' => 'class D{function __destruct(){echo "destruct\n";}} $o = new D; [, $b] = [$o, 2]; echo "after\n"; unset($o); echo "end\n";',
    'untaken call result' => 'function f(){ echo "f\n"; return 1; } function g(){ echo "g\n"; return 2; } [, $b] = [f(), g()]; var_dump($b);',
    'extra values' => '[$a] = [1, 2, 3]; var_dump($a);',
    'extra values with destructors' => 'class D{function __construct(public $n){} function __destruct(){echo "destruct $this->n\n";}} [$a] = [new D("a"), new D("x"), new D("y")]; echo "after\n"; unset($a); echo "end\n";',
    'same target twice' => '[$a, $a] = [1, 2]; var_dump($a);',
    'target used in a later value' => '$a=1; [$a, $b] = [2, $a]; var_dump($a,$b);',
    'target dim with side effect order' => 'function k(){ echo "k\n"; return 0; } function v(){ echo "v\n"; return 1; } $x=[]; [$x[k()]] = [v()]; var_dump($x);',
    'property targets' => 'class P { public $a=1; public $b=2; } $p=new P; [$p->a, $p->b] = [$p->b, $p->a]; var_dump($p);',
    'typed property throws mid-way' => 'class P { public int $a=1; public string $b="x"; } class D{function __construct(public $n){} function __destruct(){echo "destruct $this->n\n";}} $p=new P; try { [$p->a, $p->b] = ["notint", new D("after-throw")]; } catch (TypeError $e) { echo get_class($e), "\n"; } echo "after\n"; var_dump($p->a, $p->b);',
    'static property targets' => 'class S { static $a=1; static $b=2; } [S::$a, S::$b] = [S::$b, S::$a]; var_dump(S::$a, S::$b);',
    'result used' => '$r = [$a, $b] = [1, 2]; var_dump($r, $a, $b);',
    'in expression context' => '$a=1;$b=2; var_dump([$a, $b] = [$b, $a]);',
    'list() syntax' => '$a=1;$b=2; list($a, $b) = array($b, $a); var_dump($a, $b);',
    'reference in value' => '$x=1; [$a] = [&$x]; $a=2; var_dump($x);',
    'reference target' => '$x=[1]; [&$a] = $x; $a=2; var_dump($x);',
    'string key value with unkeyed list' => '[$a] = ["k"=>1]; var_dump($a);',
    'fewer values' => '[$a, $b] = [1]; var_dump($a, $b);',
    'empty list' => '[] = [1];',
    'all skipped' => '[,] = [1, 2];',
    'this as target' => 'class T { function f(){ [$this] = [1]; } }',
    'global target' => '[$GLOBALS["g"]] = [1]; var_dump($g);',
    'array with trailing comma' => '$a=1;$b=2; [$a, $b,] = [$b, $a,]; var_dump($a, $b);',
    'generator value' => 'function g(){ yield 1; } [$a] = [g()]; var_dump($a instanceof Generator);',
    'closure value binding' => '$a=1; [$f, $a] = [fn() => $a, 2]; var_dump($f());',
    'value reads target after assignment in nested' => '$a=1;$b=2; [[$a],[$b]] = [[$b],[$a]]; var_dump($a,$b);',
    'exception in a later value' => 'class D{function __destruct(){echo "destruct\n";}} function boom(){ throw new Exception("boom"); } try { [$a, $b] = [new D, boom()]; } catch (Exception $e) { echo $e->getMessage(), "\n"; } echo "after\n";',
];
// Each case goes into a file: opcache does not optimize code given with -r, and
// opcache.file_update_protection=0 lets it optimize a file written a moment ago.
$file = tempnam(sys_get_temp_dir(), 'dc2');
foreach ($cases as $name => $code) {
    file_put_contents($file, "<?php\n" . $code);
    $p = proc_open([PHP_BINARY, '-n', '-d', 'opcache.enable_cli=' . (getenv('OPC') ?: '0'), '-d', 'opcache.file_update_protection=0', '-d', 'opcache.jit=' . (getenv('JIT') ?: 'disable'), '-d', 'opcache.jit_buffer_size=64M', '-d', 'display_errors=1', $file], [1 => ['pipe', 'w'], 2 => ['pipe', 'w']], $pipes);
    $out = stream_get_contents($pipes[1]) . stream_get_contents($pipes[2]);
    $code = proc_close($p);
    echo "== $name (exit $code)\n", str_replace($file, 'FILE', $out);
}
unlink($file);
