<?php
// Bytes per FETCH_OBJ row held in memory: memory_get_usage() around fetchAll() of 100 rows, SQLite.
// Plain fetchAll() for 1, 3, 10 and 30 columns, then two cases where a row has fewer properties than
// columns: FETCH_OBJ | FETCH_GROUP on 9 columns (the first one is the group key, 8 properties; the
// bytes include the group arrays) and 9 columns of which two share a name (8 properties).
// Usage: php -n memory.php
require __DIR__ . '/suite.php';

function bytes_per_row(PDO $db, string $sql, int $mode): int
{
    $st = $db->query($sql);
    $before = memory_get_usage();
    $result = $st->fetchAll($mode);
    $rows = $mode & PDO::FETCH_GROUP ? array_sum(array_map('count', $result)) : count($result);
    return intdiv(memory_get_usage() - $before, $rows);
}

$db = fo_db('sqlite');
foreach ([1, 3, 10, 30] as $cols) {
    printf("%-30s %5d bytes per row\n", "$cols columns", bytes_per_row($db, "SELECT * FROM fo_$cols", PDO::FETCH_OBJ));
}
printf("%-30s %5d bytes per row\n", '9 columns, FETCH_GROUP',
    bytes_per_row($db, 'SELECT id, c1, c2, c3, c4, c5, c6, c7, c8 FROM fo_10', PDO::FETCH_OBJ | PDO::FETCH_GROUP));
printf("%-30s %5d bytes per row\n", '9 columns, one name twice',
    bytes_per_row($db, 'SELECT id, c1, c2, c3, c4, c5, c6, c7, c1 FROM fo_10', PDO::FETCH_OBJ));
