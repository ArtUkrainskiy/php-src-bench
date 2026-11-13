<?php
// Usage: php synth.php <case>
// live200k: PR test workload (200k live nodes, each iteration makes a 2-node garbage cycle and touches a live node)
// live1m:   same with 1M live nodes
// ring100k: 100k live nodes, garbage cycles of 1000 nodes
// ring10k / ring100k100k: 100k live nodes, garbage cycles of 10k / 100k nodes
// nolive:   only 2-node garbage cycles, no live graph
class Node { public $owner; public $data; }

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

function pairs(?stdClass $c, int $iterations, int $live): void {
    for ($i = 0; $i < $iterations; $i++) {
        $a = new Node; $b = new Node;
        $a->data = $b; $b->data = $a;
        unset($a, $b);
        if ($c) {
            $node = $c->nodes[$i % $live];
            unset($node);
        }
    }
}

function rings(stdClass $c, int $rings, int $size, int $live): void {
    for ($r = 0; $r < $rings; $r++) {
        $first = $prev = new Node;
        for ($i = 1; $i < $size; $i++) {
            $n = new Node; $prev->data = $n; $prev = $n;
            $node = $c->nodes[($r * $size + $i) % $live];
            unset($node);
        }
        $prev->data = $first;
        unset($first, $prev, $n);
    }
}

$case = $argv[1];
$t = hrtime(true);
switch ($case) {
    case 'live200k': $c = live(200000); pairs($c, 500000, 200000); break;
    case 'live1m':   $c = live(1000000); pairs($c, 2000000, 1000000); break;
    case 'ring100k': $c = live(100000); rings($c, 2000, 1000, 100000); break;
    case 'ring10k':  $c = live(100000); rings($c, 200, 10000, 100000); break;
    case 'ring100k100k': $c = live(100000); rings($c, 20, 100000, 100000); break;
    case 'nolive':   pairs(null, 2000000, 1); break;
}
$s = gc_status();
printf("%-9s time %7.3f s  gc %7.3f s  runs %5d  collected %9d  threshold %8d  buffer %8d  peak %6.1f MiB\n",
    $case, (hrtime(true) - $t) / 1e9, $s['collector_time'], $s['runs'], $s['collected'], $s['threshold'],
    $s['buffer_size'], memory_get_peak_usage(true) / 2 ** 20);
