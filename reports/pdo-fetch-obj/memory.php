<?php
// Bytes per FETCH_OBJ row held in memory (memory_get_usage() around fetchAll() of 100 rows), SQLite.
// Usage: php -n memory.php
require __DIR__ . '/suite.php';
foreach ([1, 3, 10, 30] as $cols) {
    $st = fo_db('sqlite')->query("SELECT * FROM fo_$cols");
    $before = memory_get_usage();
    $rows = $st->fetchAll(PDO::FETCH_OBJ);
    printf("%2d columns: %d bytes per row\n", $cols, (memory_get_usage() - $before) / count($rows));
    unset($rows, $st);
}
