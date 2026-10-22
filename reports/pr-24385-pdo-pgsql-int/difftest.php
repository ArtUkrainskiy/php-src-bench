<?php
// Differential check for php-src #24385: for 9 queries, prints the row count and a SHA-256 over every fetched value
// with its type, once with native and once with emulated prepares.
//   <build>/sapi/cli/php -n difftest.php > out.txt   (on master and on the PR; the outputs must be identical)
$db = new PDO('pgsql:host=127.0.0.1 port=55432 dbname=postgres user=postgres password=bench');
$db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
$queries = [
    'int2 all values' => 'SELECT g::int2 FROM generate_series(-32768, 32767) g',
    'int4 around powers of ten' => "SELECT (s * (10::int8 ^ e + d))::int4 FROM generate_series(0, 9) e, generate_series(-2, 2) d, (VALUES (1), (-1)) v(s) WHERE abs(10::int8 ^ e + d) <= 2147483647",
    'int4 limits' => 'SELECT v::int4 FROM (VALUES (-2147483648), (-2147483647), (-1), (0), (1), (2147483646), (2147483647)) t(v)',
    'int8 around powers of ten' => "SELECT (s * (10::numeric ^ e + d))::int8 FROM generate_series(0, 18) e, generate_series(-2, 2) d, (VALUES (1), (-1)) v(s)",
    'int8 limits' => "SELECT v::int8 FROM (VALUES ('-9223372036854775808'), ('-9223372036854775807'), ('9223372036854775806'), ('9223372036854775807'), ('-1000000000000000000'), ('1000000000000000000')) t(v)",
    'int8 random' => 'SELECT ((random() * 2 - 1) * 9.2e18)::int8 FROM generate_series(1, 200000)',
    'int8 random small' => 'SELECT (floor(random() * 2e6) - 1e6)::int8 FROM generate_series(1, 100000)',
    'tables' => 'SELECT a, b, c, d FROM pr24385.int4 UNION ALL SELECT a, b, c, d FROM pr24385.int4_small UNION ALL SELECT a, b, c, d FROM pr24385.int2',
    'nulls' => 'SELECT NULL::int4, 1::int4, NULL::int8',
];
foreach ([false, true] as $emulate) {
    $db->setAttribute(PDO::ATTR_EMULATE_PREPARES, $emulate);
    foreach ($queries as $name => $sql) {
        // the same random() sequence on every run, so the outputs of different builds can be compared
        $db->query('SELECT setseed(0.5)');
        $rows = $db->query($sql)->fetchAll(PDO::FETCH_NUM);
        $h = hash_init('sha256');
        foreach ($rows as $row) {
            foreach ($row as $v) {
                hash_update($h, get_debug_type($v) . ':' . var_export($v, true) . "\n");
            }
        }
        printf("%s emulate=%d rows=%d %s\n", $name, $emulate, count($rows), hash_final($h));
    }
}
