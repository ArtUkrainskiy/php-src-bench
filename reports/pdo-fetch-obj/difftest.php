<?php
// Prints everything a script can observe about PDO::FETCH_OBJ rows. Run it with master and with the
// change and compare the outputs byte for byte (README, Output verification).
// Usage: php difftest.php [DSN [user [password]]]   (default: sqlite::memory:)
// Control bytes (the BLOB column) are printed as \xNN, so that the outputs are text.
ob_start(static fn(string $out): string => preg_replace_callback('/[\x00-\x08\x0b-\x1f\x7f]/', static fn(array $m): string => sprintf('\\x%02x', ord($m[0])), $out));
$dsn = $argv[1] ?? 'sqlite::memory:';
$db = new PDO($dsn, $argv[2] ?? null, $argv[3] ?? null);
$db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
$mysql = $db->getAttribute(PDO::ATTR_DRIVER_NAME) === 'mysql';
$q = static fn(string $name): string => $mysql ? "`$name`" : "\"$name\"";

$db->exec('DROP TABLE IF EXISTS fo_t');
$db->exec('CREATE TABLE fo_t (id INTEGER, grp VARCHAR(8), name VARCHAR(64), price DOUBLE, data BLOB, note VARCHAR(8))');
$ins = $db->prepare('INSERT INTO fo_t VALUES (?, ?, ?, ?, ?, ?)');
$names = ['hello', 'señor', 'привет', '你好', 'こんにちは', '안녕', 'hi 🎉', ''];
for ($i = 1; $i <= 8; $i++) {
    $ins->execute([$i, 'g' . ($i % 3), $names[$i - 1], $i * 1.25, str_repeat("\0\x01", $i), $i % 2 ? null : "n$i"]);
}

$queries = [
    'plain'   => 'SELECT * FROM fo_t ORDER BY id',
    'dup'     => 'SELECT id AS a, name AS a, price AS b, note AS a FROM fo_t ORDER BY id',
    'numeric' => "SELECT id AS {$q('0')}, name AS {$q('1')}, price AS {$q('01')}, note AS {$q('-1')}, grp AS {$q('9223372036854775808')} FROM fo_t ORDER BY id",
    'unicode' => "SELECT id AS {$q('имя')}, name AS {$q('名前')}, price AS {$q('🎉')} FROM fo_t ORDER BY id",
    'spaces'  => "SELECT id AS {$q(' a b ')}, name AS {$q('a-b')}, price AS {$q('class')} FROM fo_t ORDER BY id",
    'onecol'  => 'SELECT name FROM fo_t ORDER BY id',
    'norows'  => 'SELECT 1 AS x FROM fo_t WHERE 1 = 0',
    'many'    => 'SELECT ' . implode(', ', array_map(fn($i) => "id + $i AS c$i", range(0, 40))) . ' FROM fo_t ORDER BY id',
];
if (!$mysql) {
    // MySQL turns an empty alias into a generated name, SQLite keeps it empty.
    $queries['empty'] = 'SELECT id AS "", name FROM fo_t ORDER BY id';
}

function dump(string $label, mixed $v): void
{
    echo "== $label\n";
    var_dump($v);
    if (is_object($v)) {
        var_dump((array) $v, get_object_vars($v), json_encode($v, JSON_INVALID_UTF8_SUBSTITUTE));
        foreach ($v as $k => $x) {
            echo var_export($k, true), ' => ', gettype($x), "\n";
        }
        echo serialize($v), "\n";
    }
}

foreach ($queries as $label => $sql) {
    $st = $db->query($sql);
    dump("$label fetch", $st->fetch(PDO::FETCH_OBJ));
    dump("$label fetchObject", $st->fetchObject());
    dump("$label fetchAll", $st->fetchAll(PDO::FETCH_OBJ));
}

if ($mysql) {
    // Native prepared statements return typed values, emulated ones return strings.
    $db->setAttribute(PDO::ATTR_EMULATE_PREPARES, false);
    $st = $db->prepare('SELECT * FROM fo_t ORDER BY id');
    $st->execute();
    dump('native prepare fetchAll', $st->fetchAll(PDO::FETCH_OBJ));
    $db->setAttribute(PDO::ATTR_EMULATE_PREPARES, true);
}

$db->setAttribute(PDO::ATTR_CASE, PDO::CASE_UPPER);
dump('ATTR_CASE upper', $db->query('SELECT id, name AS MixedCase FROM fo_t ORDER BY id')->fetchAll(PDO::FETCH_OBJ));
$db->setAttribute(PDO::ATTR_CASE, PDO::CASE_NATURAL);

if ($mysql) {
    $db->setAttribute(Pdo\Mysql::ATTR_USE_BUFFERED_QUERY, false);
    $st = $db->query('SELECT * FROM fo_t ORDER BY id');
    dump('unbuffered fetchAll', $st->fetchAll(PDO::FETCH_OBJ));
    $st = null;
    $db->setAttribute(Pdo\Mysql::ATTR_USE_BUFFERED_QUERY, true);
}

foreach (['GROUP' => PDO::FETCH_GROUP, 'UNIQUE' => PDO::FETCH_UNIQUE] as $name => $flag) {
    dump("FETCH_OBJ | FETCH_$name", $db->query('SELECT grp, id, name FROM fo_t ORDER BY id')->fetchAll(PDO::FETCH_OBJ | $flag));
}

$st = $db->query('SELECT id, name FROM fo_t ORDER BY id');
$st->setFetchMode(PDO::FETCH_OBJ);
foreach ($st as $i => $row) {
    dump("foreach $i", $row);
}

$db->setAttribute(PDO::ATTR_DEFAULT_FETCH_MODE, PDO::FETCH_OBJ);
dump('ATTR_DEFAULT_FETCH_MODE', $db->query("SELECT 1 AS a, 'x' AS b")->fetchAll());

// Rows are independent objects with writable dynamic properties.
$rows = $db->query('SELECT id, name FROM fo_t ORDER BY id')->fetchAll(PDO::FETCH_OBJ);
$rows[0]->id = 'changed';
$rows[0]->extra = [1, 2];
unset($rows[0]->name);
$c = clone $rows[1];
$c->id = -1;
dump('changed rows', [$rows[0], $rows[1], $c, $rows[0] == $rows[1], spl_object_id($rows[0]) !== spl_object_id($rows[1])]);
$r = $rows[2];
$r->{'0'} = 'zero';
var_dump(isset($r->id), property_exists($r, 'name'), $r->{'0'}, array_key_exists(0, (array) $r));

// The same statement executed again.
$st = $db->prepare('SELECT id AS x FROM fo_t WHERE id = ?');
$st->execute([3]);
dump('execute 1', $st->fetch(PDO::FETCH_OBJ));
$st->execute([4]);
dump('execute 2', $st->fetch(PDO::FETCH_OBJ));

$st = null;
$db->exec('DROP TABLE fo_t');
