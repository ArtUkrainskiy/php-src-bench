<?php
/*
 * Differential test for base64_decode(): clean input, MIME and PEM line breaks, whitespace in
 * odd places, padding in every position, invalid bytes, and lengths around the vector block
 * boundaries; every input is decoded in both modes. Also base64_encode() of the raw bytes.
 *
 *   bench difftest base64 base dev --seed 1 --count 30000
 */
require dirname(__DIR__) . '/lib/difftest.php';

const ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/';
const NOISE = [' ', "\n", "\r\n", "\t", '=', '==', '-', '_', '.', "\0", "\xFF", "\x80", '*', '==', "\n\n"];

function generate(DifftestRng $rng): string
{
    $roll = $rng->next(100);
    // mostly short, some around multiples of 32 and 44 (the AVX2 block and its threshold), some long
    if ($roll < 30) {
        $chars = $rng->next(50);
    } elseif ($roll < 55) {
        $chars = 32 * $rng->next(5) + $rng->next(9) - 4;
    } elseif ($roll < 65) {
        $chars = 44 + $rng->next(5) - 2;
    } elseif ($roll < 95) {
        $chars = $rng->next(600);
    } else {
        $chars = 2000 + $rng->next(6000);
    }
    $chars = max(0, $chars);
    $s = '';
    for ($k = 0; $k < $chars; $k++) {
        $s .= ALPHABET[$rng->next(64)];
    }
    switch ($rng->next(8)) {
        case 0: // clean, padded to a full group
            $pad = (4 - strlen($s) % 4) % 4;
            return substr($s, 0, strlen($s) - ($pad === 3 ? 1 : 0)) . str_repeat('=', min($pad, 2));
        case 1: // MIME lines
            return chunk_split($s, 76, "\r\n");
        case 2: // PEM lines
            return chunk_split($s, 64, "\n");
        case 3: // random line length
            return chunk_split($s, 1 + $rng->next(100), $rng->pick(["\n", "\r\n", " ", "\t"]));
        case 4: // noise sprinkled in, including padding mid-stream and invalid bytes
            $out = '';
            for ($k = 0; $k < strlen($s); $k++) {
                $out .= $s[$k];
                if ($rng->chance(4)) {
                    $out .= $rng->pick(NOISE);
                }
            }
            return $out;
        case 5: // long runs of whitespace
            return str_repeat(' ', $rng->next(80)) . $s . str_repeat("\n", $rng->next(80));
        case 6: // padding at a random position
            $at = $rng->next(strlen($s) + 1);
            return substr($s, 0, $at) . $rng->pick(['=', '==', '===', '=A', 'A=']) . substr($s, $at);
        default: // unpadded, as is
            return $s;
    }
}

/* Tag false distinctly: the harness hashes strlen().':'.$output, so a bare false
 * and "" would both hash as "0:" and a false<->"" regression would be invisible. */
function tag($v): string { return $v === false ? "\x01FALSE" : "S:$v"; }

function outputs(string $input): Generator
{
    $lax = base64_decode($input);
    $strict = base64_decode($input, true);
    yield 'decode' => tag($lax);
    yield 'decode strict' => tag($strict);
    yield 'encode' => base64_encode($input);
    if ($lax !== false) {
        yield 'encode of decoded' => base64_encode($lax);
    }
    if ($strict !== false) {
        yield 'encode of decoded strict' => base64_encode($strict);
    }
}

difftest_run($argv, 'generate', 'outputs');
