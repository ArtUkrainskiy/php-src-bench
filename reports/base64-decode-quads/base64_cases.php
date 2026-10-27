<?php
/* base64_decode() perf cases for PR #base64-quads. Builds a named input once, then
 * decodes it $n times. Measure with perf stat over $n minus $n=0 (generation/startup).
 * Usage: php -n base64_cases.php <case> <n> [strict0|1] */
$case = $argv[1] ?? 'token24';
$n    = (int)($argv[2] ?? 0);
$strict = (bool)($argv[3] ?? 0);

/* Content is random; base64_decode()'s instruction count depends on the length and the
 * structure (clean vs line-wrapped), not on the specific bytes, so the counts reproduce. */
function mk(int $rawbytes): string { return base64_encode(random_bytes($rawbytes)); }
/* Wrapped with LF; real MIME/PEM use CRLF, but the extra skipped byte per line does not change
 * which branch the decoder takes, so the counts hold. The differential test uses CRLF. */
function wrap(string $b64, int $col): string { return implode("\n", str_split($b64, $col)) . "\n"; }

switch ($case) {
    case 'token24':   $in = mk(18); break;            // ~24 b64 chars
    case 'key44':     $in = mk(32); break;            // 44 chars (32-byte key)
    case 'b136':      $in = mk(102); break;           // ~136 chars
    case 'clean1k':   $in = mk(768); break;           // ~1 KB
    case 'clean64k':  $in = mk(49152); break;         // ~64 KB
    case 'mime1k':    $in = wrap(mk(768), 76); break;
    case 'mime64k':   $in = wrap(mk(49152), 76); break;
    case 'pem64k':    $in = wrap(mk(49152), 64); break;
    default: fwrite(STDERR, "unknown case\n"); exit(2);
}
$len = strlen($in);
$sink = 0;
for ($i = 0; $i < $n; $i++) { $sink += strlen(base64_decode($in, $strict)); }
echo "$case $len $sink\n";
