
// Appended to sites/default/settings.php by setup.sh. drupal-run.sh sets these in the PHP-FPM pool:
// BENCH_DB_HOST/BENCH_DB_PORT (PgBouncer instead of PostgreSQL), BENCH_PDO: emulated (Drupal's default),
// emulated-persistent, native, native-persistent ("native" turns emulated prepares off, "-persistent" adds PDO::ATTR_PERSISTENT).
$databases['default']['default']['host'] = getenv('BENCH_DB_HOST') ?: $databases['default']['default']['host'];
$databases['default']['default']['port'] = getenv('BENCH_DB_PORT') ?: $databases['default']['default']['port'];
$bench_pdo = getenv('BENCH_PDO') ?: 'emulated';
if (str_starts_with($bench_pdo, 'native')) {
  $databases['default']['default']['pdo'][\PDO::ATTR_EMULATE_PREPARES] = FALSE;
}
if (str_ends_with($bench_pdo, '-persistent')) {
  $databases['default']['default']['pdo'][\PDO::ATTR_PERSISTENT] = TRUE;
}
