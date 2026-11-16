<?php
// PDO::FETCH_OBJ against FETCH_ASSOC and FETCH_CLASS, a php-src-bench suite (README, Reproduce):
//   bench compare suite.php gcc15=<master build>:<change build> ...
// One call = query() + fetchAll() of 100 rows, or query() + fetch() in a loop, or execute() + fetchAll()
// of a statement prepared once.
//
// Tables of 1, 3, 10 and 30 columns: id BIGINT, then VARCHAR(64), DOUBLE and BIGINT in turn (in SQLite
// the affinities INTEGER, TEXT, REAL), 100 rows, built once per process. SQLite in memory; MySQL through
// the DSN in PDO_MYSQL_DSN, user root, password bench, the 10-column table only. Without PDO_MYSQL_DSN
// the MySQL cases are left out. The numbers are CPU cycles of the PHP process only.

function fo_db(string $driver): PDO
{
    static $dbs = [];
    if (isset($dbs[$driver])) {
        return $dbs[$driver];
    }
    $db = $driver === 'mysql'
        ? new PDO(getenv('PDO_MYSQL_DSN'), 'root', 'bench')
        : new PDO('sqlite::memory:');
    $db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    foreach ([1, 3, 10, 30] as $cols) {
        $types = [];
        for ($c = 1; $c < $cols; $c++) {
            $types[] = "c$c " . ['VARCHAR(64)', 'DOUBLE', 'BIGINT'][($c - 1) % 3];
        }
        $db->exec("DROP TABLE IF EXISTS fo_$cols");
        $db->exec("CREATE TABLE fo_$cols (id BIGINT" . ($types ? ', ' . implode(', ', $types) : '') . ')');
        $ins = $db->prepare("INSERT INTO fo_$cols VALUES (" . implode(',', array_fill(0, $cols, '?')) . ')');
        $db->beginTransaction();
        for ($i = 1; $i <= 100; $i++) {
            $row = [$i];
            for ($c = 1; $c < $cols; $c++) {
                $row[] = [fn() => "value $c of row $i", fn() => $i * 1.25 + $c, fn() => $i * 1000 + $c][($c - 1) % 3]();
            }
            $ins->execute($row);
        }
        $db->commit();
    }
    return $dbs[$driver] = $db;
}

// A class with every column declared, for FETCH_CLASS.
function fo_class(int $cols): string
{
    $name = "FoRow$cols";
    if (!class_exists($name, false)) {
        $props = ['public $id;'];
        for ($c = 1; $c < $cols; $c++) {
            $props[] = "public \$c$c;";
        }
        eval("final class $name { " . implode(' ', $props) . ' }');
    }
    return $name;
}

function fo_all(array $s, int $mode): int
{
    $st = fo_db($s[0])->query("SELECT * FROM fo_$s[1]");
    $rows = $mode === PDO::FETCH_CLASS ? $st->fetchAll($mode, fo_class($s[1])) : $st->fetchAll($mode);
    return count($rows);
}

// The way Laravel queries MySQL: prepare() + execute() with native prepared statements.
function fo_prepared(array $s, int $mode): int
{
    static $stmts = [];
    if (!isset($stmts[$s[1]])) {
        $db = fo_db($s[0]);
        $db->setAttribute(PDO::ATTR_EMULATE_PREPARES, false);
        $stmts[$s[1]] = $db->prepare("SELECT * FROM fo_$s[1] WHERE id > ?");
    }
    $stmts[$s[1]]->execute([0]);
    return count($stmts[$s[1]]->fetchAll($mode));
}

// FETCH_OBJ | FETCH_GROUP on the id column: one group per row.
function fo_group(array $s): int
{
    return count(fo_db($s[0])->query("SELECT * FROM fo_$s[1]")->fetchAll(PDO::FETCH_OBJ | PDO::FETCH_GROUP));
}

function fo_each(array $s): int
{
    $st = fo_db($s[0])->query("SELECT * FROM fo_$s[1]");
    $n = 0;
    while ($st->fetch(PDO::FETCH_OBJ)) {
        $n++;
    }
    return $n;
}

$inputs = [
    'sqlite-1col' => ['sqlite', 1],
    'sqlite-3cols' => ['sqlite', 3],
    'sqlite-10cols' => ['sqlite', 10],
    'sqlite-30cols' => ['sqlite', 30],
];
if (getenv('PDO_MYSQL_DSN')) {
    $inputs['mysql-10cols'] = ['mysql', 10];
}
$prime = 'fo_db($s[0]); fo_class($s[1]);';
$mysqlOnly = array_values(array_intersect(['mysql-10cols'], array_keys($inputs)));

return [
    'inputs' => $inputs,
    'cases' => [
        'fetchAll OBJ' => ['code' => 'fo_all($s, PDO::FETCH_OBJ)', 'setup' => $prime],
        'fetchAll OBJ GROUP' => ['code' => 'fo_group($s)', 'inputs' => ['sqlite-10cols'], 'setup' => $prime],
        'fetch OBJ loop' => ['code' => 'fo_each($s)', 'inputs' => ['sqlite-10cols'], 'setup' => $prime],
        'fetchAll ASSOC' => ['code' => 'fo_all($s, PDO::FETCH_ASSOC)', 'setup' => $prime],
        'prepared OBJ' => ['code' => 'fo_prepared($s, PDO::FETCH_OBJ)', 'inputs' => $mysqlOnly, 'setup' => $prime],
        'prepared ASSOC' => ['code' => 'fo_prepared($s, PDO::FETCH_ASSOC)', 'inputs' => $mysqlOnly, 'setup' => $prime],
        'fetchAll CLASS' => ['code' => 'fo_all($s, PDO::FETCH_CLASS)', 'inputs' => array_values(array_intersect(['sqlite-10cols', 'mysql-10cols'], array_keys($inputs))), 'setup' => $prime],
    ],
];
