<?php
// Usage: php mem.php <case> <live nodes> [payload KiB]
// pairs:    live graph + 2-object garbage cycles; one object of each cycle holds a <payload> KiB string
// dtor:     same, but the garbage objects have __destruct() and a reference to the live graph
// Every iteration also touches one live node, so it becomes a GC root.
// Prints time, GC stats and PHP peak memory; peak RSS comes from /usr/bin/time.
class Node { public $owner; public $data; public $payload; }
class DNode { public $owner; public $data; public $payload; function __destruct() {} }

function live(int $n): stdClass {
    $c = new stdClass;
    $c->nodes = [];
    for ($i = 0; $i < $n; $i++) {
        $node = new Node;
        $node->owner = $c;
        $c->nodes[] = $node;
    }
    return $c;
}

[, $case, $liveCount] = $argv;
$liveCount = (int) $liveCount;
$kib = (int) ($argv[3] ?? 0);
$iterations = 200000;

$t = hrtime(true);
$c = live($liveCount);
$class = $case === 'dtor' ? DNode::class : Node::class;
for ($i = 0; $i < $iterations; $i++) {
    $a = new $class; $b = new $class;
    $a->data = $b; $b->data = $a;
    if ($kib) {
        $a->payload = str_repeat(chr(65 + $i % 26), $kib * 1024);
    }
    if ($case === 'dtor') {
        $a->owner = $c;
    }
    unset($a, $b);
    $node = $c->nodes[$i % $liveCount];
    unset($node);
}
$s = gc_status();
printf("RESULT case=%s live=%d kib=%d time=%.3f gc=%.3f runs=%d collected=%d threshold=%d buffer=%d php_peak_mib=%.1f\n",
    $case, $liveCount, $kib, (hrtime(true) - $t) / 1e9, $s['collector_time'], $s['runs'], $s['collected'],
    $s['threshold'], $s['buffer_size'], memory_get_peak_usage(true) / 2 ** 20);
