<?php
/* Input-shape benchmark for PR #23585. Beyond uniform-random: the shapes the
 * code review flagged as where cost could shift (already/reverse sorted, all
 * equal, many duplicates with the Z_EXTRA tie-break, packed-with-holes, all
 * references). sort cost = sort mode minus nop mode.
 * Usage: php -n sort_shapes.php <size> <batch> <ints|strings> <shape> <sort|rsort> <sort|nop>
 *   shape: random sorted reverse allequal dup holes refs */
ini_set('memory_limit', '-1');
$size  = (int)($argv[1] ?? 1000);
$batch = (int)($argv[2] ?? 2000);
$type  = $argv[3] ?? 'ints';
$shape = $argv[4] ?? 'random';
$op    = $argv[5] ?? 'sort';
$mode  = $argv[6] ?? 'sort';

$mk = function(int $n) use ($type) {
    return $type === 'ints' ? mt_rand(-1000000, 1000000) : ('v' . mt_rand(0, 999999));
};

mt_srand(717);
$rows = [];
$refholders = [];
for ($i = 0; $i < $batch; $i++) {
    $row = [];
    for ($j = 0; $j < $size; $j++) { $row[] = $mk($size); }
    switch ($shape) {
        case 'sorted':   sort($row); break;
        case 'reverse':  rsort($row); break;
        case 'allequal': $v = $mk($size); $row = array_fill(0, $size, $v); break;
        case 'dup':      for ($j = 0; $j < $size; $j++) { $row[$j] = $type === 'ints' ? mt_rand(0, 7) : ('v' . mt_rand(0, 7)); } break;
        case 'holes':    for ($h = 0; $h < $size / 4; $h++) { unset($row[mt_rand(0, $size - 1)]); } $row = array_values($row); $row[] = $mk($size); unset($row[count($row) - 1]); break;
        case 'refs':     $refholders[$i] = $row; foreach ($row as $k => $v) { $row[$k] =& $refholders[$i][$k]; } break;
    }
    $rows[] = $row;
}
unset($row);

if ($mode === 'nop') { $s = 0; foreach ($rows as &$r) { $s += count($r); } unset($r); echo $s, "\n"; return; }

foreach ($rows as &$r) {
    if ($op === 'rsort') { rsort($r, SORT_REGULAR); } else { sort($r, SORT_REGULAR); }
}
unset($r);
echo "done\n";
