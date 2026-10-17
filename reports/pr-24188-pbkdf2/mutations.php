<?php
// Mutations of the precomputed HMAC states in hash_pbkdf2() (php-src PR 24188, on PHP-8.2).
$calls = [
    'implode(",", array_map(fn($a) => hash_pbkdf2($a, $s, "salt", 1), hash_hmac_algos()))',
    'implode(",", array_map(fn($a) => hash_pbkdf2($a, $s, "", 3, 200), hash_hmac_algos()))',
    'implode(",", array_map(fn($a) => bin2hex(hash_pbkdf2($a, "pw", $s, 2, 0, true)), hash_hmac_algos()))',
    'implode(",", array_map(fn($a) => bin2hex(hash_pbkdf2($a, $s, $s, 5, 100, true)), hash_hmac_algos()))',
];
$args = ['--input', 'bytes', '--max', '300', '--boundaries', '64,72,104,128,136,144', '--seed', '3', '--count', '1000'];
foreach ($calls as $call) {
    array_push($args, '--code', $call);
}
$f = 'ext/hash/hash.c';

return [
    'difftest' => ['generator' => 'code', 'against' => 'pr24188-base-gcc13', 'args' => $args],
    'tests' => ['ext/hash/tests'],
    'mutations' => [
        'round starts from a fresh state instead of the copy' => ['file' => $f,
            'from' => "\tops->hash_copy(ops, base_context, context);\n", 'to' => "\tops->hash_init(context, NULL);\n"],
        'inner state absorbs the opad block' => ['file' => $f,
            'from' => 'ops->hash_update(inner_context, K1, ops->block_size);', 'to' => 'ops->hash_update(inner_context, K2, ops->block_size);'],
        'outer state absorbs no key block' => ['file' => $f,
            'from' => 'ops->hash_update(outer_context, K2, ops->block_size);', 'to' => 'ops->hash_update(outer_context, K2, 0);'],
        'first block: inner round with the outer state' => ['file' => $f,
            'from' => 'php_hash_hmac_round_with_copy(digest, ops, inner_context, context, computed_salt',
            'to' => 'php_hash_hmac_round_with_copy(digest, ops, outer_context, context, computed_salt'],
        'iterations: inner round with the outer state' => ['file' => $f,
            'from' => 'php_hash_hmac_round_with_copy(digest, ops, inner_context, context, digest, ops->digest_size);',
            'to' => 'php_hash_hmac_round_with_copy(digest, ops, outer_context, context, digest, ops->digest_size);'],
        'iterations: outer round left out' => ['file' => $f,
            'from' => "inner_context, context, digest, ops->digest_size);\n\t\t\tphp_hash_hmac_round_with_copy(digest, ops, outer_context, context, digest, ops->digest_size);",
            'to' => 'inner_context, context, digest, ops->digest_size);'],
    ],
];
