<?php
/*
 * Command-line plumbing of the orchestrator: option parsing, warnings and the progress line.
 */
declare(strict_types=1);

const FLAGS = ['perf', 'md', 'quick', 'no-save', 'help'];
const VALUE_OPTIONS = ['a', 'b', 'filter', 'rounds', 'samples', 'target-ms', 'warmup-ms', 'cpu', 'wait-idle'];

/** An error the user can fix: reported as one line, without a stack trace. */
final class BenchError extends RuntimeException
{
}

/**
 * Splits arguments into positional ones and --options (`--key value` or `--key=value`).
 *
 * @return array{list<string>, array<string, string|true>}
 */
function parse_args(array $args): array
{
    $positional = [];
    $options = [];
    for ($i = 0; $i < count($args); $i++) {
        $arg = $args[$i];
        if (!str_starts_with($arg, '--')) {
            $positional[] = $arg;
            continue;
        }
        $key = substr($arg, 2);
        $value = null;
        if (str_contains($key, '=')) {
            [$key, $value] = explode('=', $key, 2);
        }
        if (in_array($key, FLAGS, true)) {
            $options[$key] = true;
        } elseif (in_array($key, VALUE_OPTIONS, true)) {
            $value ??= $args[++$i] ?? throw new BenchError("--$key needs a value");
            $options[$key] = $value;
        } else {
            throw new BenchError("unknown option --$key");
        }
    }
    return [$positional, $options];
}

function int_option(array $options, string $key, int $default): int
{
    if (!isset($options[$key])) {
        return $default;
    }
    if (!preg_match('/^\d+$/', (string) $options[$key])) {
        throw new BenchError("--$key expects an integer");
    }
    return (int) $options[$key];
}

function float_option(array $options, string $key, float $default): float
{
    if (!isset($options[$key])) {
        return $default;
    }
    if (!is_numeric($options[$key])) {
        throw new BenchError("--$key expects a number");
    }
    return (float) $options[$key];
}

function warn(string $message): void
{
    $color = stream_isatty(STDERR) && getenv('NO_COLOR') === false;
    fwrite(STDERR, ($color ? "\033[33mwarning:\033[0m " : 'warning: ') . $message . "\n");
}

/** Rewrites one status line on a terminal; prints plain lines when stderr is redirected. */
function progress(string $message): void
{
    static $tty = null;
    $tty ??= stream_isatty(STDERR);
    if ($tty) {
        fwrite(STDERR, "\r\033[K" . $message);
    } elseif ($message !== '') {
        fwrite(STDERR, $message . "\n");
    }
}
