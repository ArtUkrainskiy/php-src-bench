<?php
// One process for callgrind: query() + fetchAll() of 100 rows × 10 columns from SQLite, N times.
// Usage: php -n profile.php N [obj|assoc]   (N = 0 runs only the setup; take the difference)
//   valgrind --tool=callgrind --callgrind-out-file=cg.out php -n profile.php 100 obj
//   callgrind_annotate --inclusive=yes cg.out
require __DIR__ . '/suite.php';
$mode = ($argv[2] ?? 'obj') === 'assoc' ? PDO::FETCH_ASSOC : PDO::FETCH_OBJ;
$s = ['sqlite', 10];
fo_db('sqlite');
$n = (int) ($argv[1] ?? 100);
$rows = 0;
for ($i = 0; $i < $n; $i++) {
    $rows += fo_all($s, $mode);
}
echo $rows, "\n";
