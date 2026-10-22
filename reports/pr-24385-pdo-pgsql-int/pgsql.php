<?php
// pdo_pgsql integer columns (php-src #24385): execute() + fetchAll() of 10,000 rows from a prepared statement,
// PostgreSQL 17 on 127.0.0.1:55432 (README, Reproduce), tables in schema pr24385 (pgsql.sql).
// bench passes the input, the table name, as $s; the statement is prepared once per process and reused.

function pr24385_fetch(string $table, int $mode): int
{
    static $stmts = [];
    if (!isset($stmts[$table])) {
        $db = new PDO('pgsql:host=127.0.0.1 port=55432 dbname=postgres user=postgres password=bench');
        $db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
        $stmts[$table] = $db->prepare("SELECT * FROM pr24385.$table");
    }
    $stmts[$table]->execute();
    return count($stmts[$table]->fetchAll($mode));
}

return [
    'inputs' => [
        'int2-4cols' => 'int2',
        'int4-small-4cols' => 'int4_small',
        'int4-4cols' => 'int4',
        'int8-small-4cols' => 'int8_small',
        'int8-4cols' => 'int8',
        'mixed-2int-9text' => 'mixed',
        'text-4cols' => 'text',
    ],
    'cases' => [
        'fetchAll NUM' => 'pr24385_fetch($s, PDO::FETCH_NUM)',
        'fetchAll ASSOC' => [
            'code' => 'pr24385_fetch($s, PDO::FETCH_ASSOC)',
            'inputs' => ['int4-4cols', 'mixed-2int-9text'],
        ],
    ],
];
