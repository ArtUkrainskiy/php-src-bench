<?php
$pdo = new PDO('mysql:host=127.0.0.1;port=3307;dbname=test', 'root', 'pw');
$handler = static function () use ($pdo): void {
    $st = $pdo->prepare('SELECT id, title, body, created_at FROM t ORDER BY id LIMIT 20 OFFSET ?');
    $st->bindValue(1, random_int(0, 980), PDO::PARAM_INT);
    $st->execute();
    header('Content-Type: application/json');
    echo json_encode($st->fetchAll(PDO::FETCH_ASSOC));
};
while (frankenphp_handle_request($handler)) {
}
