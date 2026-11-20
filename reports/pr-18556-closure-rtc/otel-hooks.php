<?php
// hooks.php: no-op pre/post hooks on classes that opentelemetry-auto-laravel / -symfony / -pdo hook, so the
// observer lookup tables are not empty. Loaded with auto_prepend_file next to the opentelemetry extension.
use function OpenTelemetry\Instrumentation\hook;

$pre = static function () {};
$post = static function () {};
foreach ([
    ['Illuminate\Foundation\Http\Kernel', 'handle'],
    ['Illuminate\Contracts\Http\Kernel', 'handle'],
    ['Illuminate\Routing\Router', 'dispatchToRoute'],
    ['Illuminate\Routing\Route', 'run'],
    ['Illuminate\Database\Connection', 'logQuery'],
    ['Illuminate\Contracts\Queue\Queue', 'push'],
    ['Illuminate\Cache\Repository', 'get'],
    ['Illuminate\Log\LogManager', 'log'],
    ['Illuminate\View\View', 'render'],
    ['Illuminate\Contracts\Console\Kernel', 'handle'],
    ['Symfony\Component\HttpKernel\HttpKernel', 'handle'],
    ['Symfony\Contracts\HttpClient\HttpClientInterface', 'request'],
    ['Doctrine\DBAL\Driver\Connection', 'query'],
    ['Doctrine\DBAL\Driver\Connection', 'exec'],
    ['Doctrine\DBAL\Driver\Connection', 'prepare'],
    ['Doctrine\DBAL\Driver\Statement', 'execute'],
    ['Twig\Environment', 'render'],
    ['PDO', 'query'],
    ['PDO', 'prepare'],
    ['PDOStatement', 'execute'],
] as [$class, $method]) {
    hook($class, $method, $pre, $post);
}
