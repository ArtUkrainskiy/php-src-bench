<?php
// Cost of one deprecated call: ReflectionProperty::setAccessible() (deprecated on master) in a loop.
// MODE selects what listens: none | noop (handler that returns false) | symfony-like (handler that
// formats and stores the message like a framework logger would) | baseline (no deprecated call).
$mode = $argv[1] ?? 'none';
$n = (int)($argv[2] ?? 100000);
class C { public $p = 1; }
$rp = new ReflectionProperty(C::class, 'p');
$log = [];
if ($mode === 'noop') {
    set_error_handler(static function (int $t, string $m, string $f, int $l): bool { return false; });
} elseif ($mode === 'framework') {
    set_error_handler(static function (int $t, string $m, string $f, int $l) use (&$log): bool {
        if (!(error_reporting() & $t)) { return true; }
        $log[] = ['level' => 'info', 'message' => sprintf('Deprecated: %s in %s:%d', $m, $f, $l), 'context' => ['exception' => null]];
        if (count($log) > 1000) { $log = []; }
        return true;
    });
}
if ($mode === 'baseline') {
    for ($i = 0; $i < $n; $i++) { $rp->getName(); }
} else {
    for ($i = 0; $i < $n; $i++) { $rp->setAccessible(true); }
}
echo "done $mode $n\n";
