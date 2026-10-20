<?php
// What survives from one use of a persistent pdo_pgsql connection to the next: the PDO object is freed
// (as at the end of an FPM request) and created again on the same persistent connection.
//   php session-reset-check.php <dsn>
$dsn = $argv[1];
$opt = [PDO::ATTR_PERSISTENT => true, PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION];

$db = new PDO($dsn, null, null, $opt);
$pid = $db->query('SELECT pg_backend_pid()')->fetchColumn();
$db->exec("SET application_name = 'changed'");
$db->exec('CREATE TEMP TABLE reset_check (a int)');
$db->query('SELECT pg_advisory_lock(4242)');
$db->exec('LISTEN reset_check');
$db->exec('PREPARE reset_check_sql AS SELECT 1');
$st = $db->prepare('SELECT 2');
$st->execute();
$db = $st = null;

$db = new PDO($dsn, null, null, $opt);
$other = new PDO($dsn, null, null, [PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION]);
$same = $db->query('SELECT pg_backend_pid()')->fetchColumn() === $pid;
printf("same backend: %s\n", var_export($same, true));
$otherBackend = $other->query('SELECT pg_backend_pid()')->fetchColumn() !== $pid;
printf("second connection on another backend: %s\n", var_export($otherBackend, true));
printf("application_name reset: %s\n", var_export($db->query('SHOW application_name')->fetchColumn() !== 'changed', true));
printf("temp table dropped: %s\n", var_export($db->query("SELECT to_regclass('pg_temp.reset_check') IS NULL")->fetchColumn(), true));
// a backend can take its own session-level advisory lock again, so only another backend can tell
printf("advisory lock released: %s\n", $otherBackend
	? var_export($other->query('SELECT pg_try_advisory_lock(4242)')->fetchColumn(), true)
	: 'not applicable (same backend)');
$other->query('SELECT pg_advisory_unlock_all()');
printf("not listening: %s\n", var_export($db->query('SELECT count(*) = 0 FROM pg_listening_channels()')->fetchColumn(), true));
// listed after the checks above, which prepare statements of their own
printf("server statements: [%s]\n", implode(', ', $db->query('SELECT name FROM pg_prepared_statements ORDER BY name')->fetchAll(PDO::FETCH_COLUMN)));
