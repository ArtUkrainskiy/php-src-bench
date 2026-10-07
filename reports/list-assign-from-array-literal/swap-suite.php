<?php
// Destructuring assignment from an array literal, against the same work done by hand.
return [
    'inputs' => ['ints' => [1, 2], 'strings' => ['first', 'second'], 'arrays' => [[1, 2, 3], ['k' => 'v']]],
    'cases' => [
        'call only' => '(static function ($a, $b) { return $a; })($s[0], $s[1])',
        'swap [$a, $b] = [$b, $a]' => '(static function ($a, $b) { [$a, $b] = [$b, $a]; return $a; })($s[0], $s[1])',
        'swap via temporary' => '(static function ($a, $b) { $t = $a; $a = $b; $b = $t; return $a; })($s[0], $s[1])',
        'rotate three' => ['code' => '(static function ($a, $b) { $c = $a; [$a, $b, $c] = [$b, $c, $a]; return $a; })($s[0], $s[1])', 'inputs' => ['ints']],
        'fibonacci step x10' => ['code' => '(static function ($a, $b) { for ($i = 0; $i < 10; $i++) { [$a, $b] = [$b, $a + $b]; } return $a; })($s[0], $s[1])', 'inputs' => ['ints']],
        'fibonacci step x10 in for list' => ['code' => '(static function ($a, $b) { for ($i = 0; $i < 10; $i++, [$a, $b] = [$b, $a + $b]); return $a; })($s[0], $s[1])', 'inputs' => ['ints']],
        'swap array elements' => ['code' => '(static function ($p) { [$p[0], $p[1]] = [$p[1], $p[0]]; return $p[0]; })($s)', 'inputs' => ['ints']],
        'swap array elements via temporary' => ['code' => '(static function ($p) { $t = $p[0]; $p[0] = $p[1]; $p[1] = $t; return $p[0]; })($s)', 'inputs' => ['ints']],
        'swap properties' => ['code' => '(static function ($o) { [$o->a, $o->b] = [$o->b, $o->a]; return $o->a; })(new class($s) { public $a; public $b; function __construct($s) { [$this->a, $this->b] = $s; } })', 'inputs' => ['ints']],
        'init [$a, $b] = [1, 2]' => ['code' => '(static function () { [$a, $b] = [1, 2]; return $a; })()', 'inputs' => ['ints']],
        'from a variable (not covered)' => ['code' => '(static function ($pair) { [$a, $b] = $pair; return $a; })($s)', 'inputs' => ['ints']],
        'keyed (not covered)' => ['code' => '(static function ($a, $b) { ["x" => $a, "y" => $b] = ["x" => $b, "y" => $a]; return $a; })($s[0], $s[1])', 'inputs' => ['ints']],
    ],
];
