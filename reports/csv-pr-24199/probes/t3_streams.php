<?php
use function Csv\{collection_to_file, collection_to_buffer};
use Csv\LazyLaxCollection as L;
$D = __DIR__ . '/data'; @mkdir($D);
function t(string $label, callable $f) {
    echo "== $label: ";
    try { $r = $f(); echo is_string($r) ? $r : json_encode($r, JSON_UNESCAPED_SLASHES|JSON_INVALID_UTF8_SUBSTITUTE), "\n"; }
    catch (\Throwable $e) { echo get_class($e), ": ", $e->getMessage(), "\n"; }
}
function rows(L $c): array { $r = []; foreach ($c as $k => $row) { $r[] = [$k, $row]; } return $r; }
function same(array $expect, string $path, ...$dialect): string {
    $got = iterator_to_array(L::createFromFile($path, ...$dialect), false);
    return $got === $expect ? "ok (" . count($got) . " rows)" : "MISMATCH got " . json_encode(array_slice($got, 0, 3)) . " expected " . json_encode(array_slice($expect, 0, 3));
}
// 1. chunk boundaries: place an enclosed field with embedded CRLF and doubled quotes straddling 8192, 16384 ... with filler
foreach ([8190, 8191, 8192, 8193, 8194, 16383, 16384, 16385] as $pos) {
    foreach (['"a""b"', "\"x\r\ny\"", "\"\"\"\"", "\"q\",\"\""] as $special) {
        $filler = str_repeat('f', $pos - 4) . ",zz"; // row 1 ends exactly near pos
        $expect = [];
        $buf = $filler . "\r\n"; $expect[] = explode(',', $filler);
        $row2 = $special . ",tail"; $buf .= $row2 . "\r\n"; $expect[] = Csv\row_to_array($row2);
        for ($i = 0; $i < 3; $i++) { $buf .= "r$i,s$i\r\n"; $expect[] = ["r$i", "s$i"]; }
        file_put_contents("$D/cb.csv", $buf);
        $res = same($expect, "$D/cb.csv");
        if ($res[0] !== 'o') echo "chunk pos=$pos special=" . json_encode($special) . ": $res\n";
    }
}
echo "chunk boundary sweep done\n";
// CRLF split exactly at 8192: row1 of length 8191 then \r at 8191 and \n at 8192
foreach ([8190, 8191, 8192] as $len) {
    $r1 = str_repeat('a', $len); $buf = "$r1\r\nb,c\r\n"; file_put_contents("$D/eol.csv", $buf);
    echo "eol split len=$len: ", same([[$r1], ['b','c']], "$D/eol.csv"), "\n";
    $buf = "$r1\n\nb|c\n\n"; file_put_contents("$D/eol2.csv", $buf);
    echo "custom eol split len=$len: ", same([[$r1], ['b','c']], "$D/eol2.csv", '|', '"', "\n\n"), "\n";
    $buf = "XY" . str_repeat('a', $len - 2) . "XYXY" . "bXY,c\r\n"; file_put_contents("$D/enc.csv", $buf);
    echo "mb enclosure doubled at boundary len=$len: ", same([[str_repeat('a', $len - 2) . "XYb", 'c']], "$D/enc.csv", ',', 'XY'), "\n";
}
// 2. big file memory bound
$fh = fopen("$D/big.csv", 'w'); for ($i = 0; $i < (getenv("SMALL") ? 2000 : 200000); $i++) fwrite($fh, "$i,\"x,y\",zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz\r\n"); fclose($fh);
$m0 = memory_get_peak_usage(true); $n = 0; foreach (L::createFromFile("$D/big.csv") as $row) { $n++; }
echo "big: rows=$n peak_delta=" . (memory_get_peak_usage(true) - $m0) . "\n";
// 3. nested iteration / getIterator twice
file_put_contents("$D/s.csv", "1,a\r\n2,b\r\n3,c\r\n");
t('nested foreach', function() use ($D) { $c = L::createFromFile("$D/s.csv"); $out = []; foreach ($c as $o) { foreach ($c as $i) { $out[] = $o[0] . $i[0]; } } return $out; });
t('nested foreach buffer', function() { $c = L::createFromBuffer("1,a\r\n2,b\r\n3,c\r\n"); $out = []; foreach ($c as $o) { foreach ($c as $i) { $out[] = $o[0] . $i[0]; } } return $out; });
t('two iterators interleaved', function() use ($D) { $c = L::createFromFile("$D/s.csv"); $a = $c->getIterator(); $b = $c->getIterator(); $a->rewind(); $b->rewind(); $a->next(); return [$a->current(), $b->current(), $a->key(), $b->key()]; });
t('iterator current before rewind', function() use ($D) { $c = L::createFromFile("$D/s.csv"); $a = $c->getIterator(); return [$a->valid(), $a->current(), $a->key()]; });
t('keys', fn() => rows(L::createFromFile("$D/s.csv")));
t('error mid-iteration then continue', function() use ($D) { file_put_contents("$D/err.csv", "1,a\r\n2,b\"x\r\n3,c\r\n"); $c = L::createFromFile("$D/err.csv"); $it = $c->getIterator(); $out = []; try { foreach ($it as $r) { $out[] = $r; } } catch (ValueError $e) { $out[] = 'VE'; } $out[] = $it->valid(); $it->next(); $out[] = $it->valid(); $out[] = $it->current(); return $out; });
t('error row then rewind works', function() use ($D) { $c = L::createFromFile("$D/err.csv"); try { foreach ($c as $r) {} } catch (ValueError) {} return iterator_to_array($c, false)[0] ?? null; });
// 4. non-seekable
t('non-seekable second iteration (stdin pipe)', function() { $out = shell_exec('printf "a,b\r\nc,d\r\n" | ' . escapeshellarg(PHP_BINARY) . ' -r ' . escapeshellarg('$c = Csv\LazyLaxCollection::createFromFile("php://stdin"); echo count(iterator_to_array($c, false)); try { iterator_to_array($c, false); } catch (Throwable $e) { echo " ", get_class($e), ": ", $e->getMessage(); }') . ' 2>&1'); return $out; });
t('fifo partial reads', function() use ($D) { @unlink("$D/fifo"); posix_mkfifo("$D/fifo", 0600); $cmd = '(printf "a,b\r\n"; sleep 0.3; printf "c,"; sleep 0.3; printf "d\r\n") > ' . escapeshellarg("$D/fifo") . ' &'; shell_exec($cmd); $c = L::createFromFile("$D/fifo"); $t0 = microtime(true); $out = []; foreach ($c as $r) { $out[] = [round(microtime(true) - $t0, 1), $r]; } return $out; });
// 5. file changes during iteration
t('file grows during iteration', function() use ($D) { file_put_contents("$D/g.csv", "1\r\n2\r\n"); $c = L::createFromFile("$D/g.csv"); $out = []; foreach ($c as $r) { $out[] = $r[0]; if ($r[0] === '2') file_put_contents("$D/g.csv", "3\r\n", FILE_APPEND); } return $out; });
t('file truncated during iteration', function() use ($D) { $buf = ''; for ($i = 0; $i < 3000; $i++) $buf .= "$i,xxxxxxxxxxxxxxxxxxxxxxxxxxxxx\r\n"; file_put_contents("$D/tr.csv", $buf); $c = L::createFromFile("$D/tr.csv"); $n = 0; foreach ($c as $r) { $n++; if ($n === 1) file_put_contents("$D/tr.csv", ""); } return $n; });
t('empty file', fn() => iterator_to_array(L::createFromFile("$D/empty.csv"), false) ?: (file_put_contents("$D/empty.csv", "") === 0 ? iterator_to_array(L::createFromFile("$D/empty.csv"), false) : null));
t('file with only CRLF', function() use ($D) { file_put_contents("$D/crlf.csv", "\r\n"); return iterator_to_array(L::createFromFile("$D/crlf.csv"), false); });
t('file with unterminated enclosure', function() use ($D) { file_put_contents("$D/unt.csv", "a,\"b\r\nc,d\r\n"); return iterator_to_array(L::createFromFile("$D/unt.csv"), false); });
t('directory', fn() => iterator_to_array(L::createFromFile($D), false));
t('createFromFile data: url', fn() => iterator_to_array(L::createFromFile("data://text/plain,a%2Cb%0D%0Ac%2Cd"), false));
t('createFromFile php://memory', fn() => iterator_to_array(L::createFromFile("php://memory"), false));
t('createFromFile php://filter', function() use ($D) { return iterator_to_array(L::createFromFile("php://filter/read=string.toupper/resource=$D/s.csv"), false); });
t('createFromFile NUL in path', fn() => L::createFromFile("a\0b"));
t('clone', fn() => clone L::createFromBuffer("a"));
t('serialize', fn() => serialize(L::createFromBuffer("a")));
t('var_export/var_dump', function() { ob_start(); var_dump(L::createFromBuffer("a")); return trim(ob_get_clean()); });
t('compare ==', fn() => L::createFromBuffer("a") == L::createFromBuffer("a"));
t('dynamic prop', function() { $c = L::createFromBuffer("a"); $c->x = 1; return 1; });
t('foreach by ref', function() { $c = L::createFromBuffer("a"); foreach ($c as &$r) {} return 1; });
t('get_resources after createFromFile', function() use ($D) { $before = count(get_resources('stream')); $c = L::createFromFile("$D/s.csv"); return [count(get_resources('stream')) - $before]; });
// 6. collection_to_file
t('ctf nonexistent dir', fn() => collection_to_file("$D/nope/x.csv", [[1]]));
t('ctf /dev/full', fn() => collection_to_file("/dev/full", [[str_repeat('x', 10)]]));
t('ctf directory', fn() => collection_to_file($D, [[1]]));
t('ctf php://memory', fn() => collection_to_file("php://memory", [[1]]));
t('ctf data:', fn() => collection_to_file("data://text/plain,x", [[1]]));
t('ctf http://', fn() => collection_to_file("http://127.0.0.1:9/x", [[1]]));
t('ctf php://filter write', function() use ($D) { collection_to_file("php://filter/write=string.toupper/resource=$D/up.csv", [['a','b']]); return file_get_contents("$D/up.csv"); });
t('ctf error mid: file left partially written?', function() use ($D) { try { collection_to_file("$D/part.csv", [[1,2],[3]]); } catch (ValueError $e) {} return [file_exists("$D/part.csv"), file_get_contents("$D/part.csv")]; });
t('ctf first element bad: truncates existing file', function() use ($D) { file_put_contents("$D/keep.csv", "old"); try { collection_to_file("$D/keep.csv", [1]); } catch (TypeError $e) {} return file_get_contents("$D/keep.csv"); });
t('ctf stream_flush false user wrapper', function() {
    class W { public $context; static $data = ''; function stream_open($p,$m,$o,&$op){return true;} function stream_write($d){ self::$data .= $d; return strlen($d);} function stream_flush(){ return false; } function stream_close(){} }
    stream_wrapper_register('w', 'W'); try { collection_to_file("w://x", [[1]]); return "no error, data=" . json_encode(W::$data); } finally { stream_wrapper_unregister('w'); } });
t('ctf short write user wrapper', function() {
    class W2 { public $context; function stream_open($p,$m,$o,&$op){return true;} function stream_write($d){ return 1; } function stream_flush(){ return true; } function stream_close(){} }
    stream_wrapper_register('w2', 'W2'); try { collection_to_file("w2://x", [[str_repeat('x', 100)]]); return "no error"; } finally { stream_wrapper_unregister('w2'); } });
t('ctf open_basedir', function() use ($D) { $out = shell_exec(escapeshellarg(PHP_BINARY) . ' -d open_basedir=/nonexistent -r ' . escapeshellarg('try { Csv\collection_to_file("/tmp/zzz_csv.csv", [[1]]); echo "written"; } catch (Throwable $e) { echo get_class($e), ": ", $e->getMessage(); } try { Csv\LazyLaxCollection::createFromFile("/etc/passwd"); echo " opened"; } catch (Throwable $e) { echo " | ", get_class($e), ": ", $e->getMessage(); }') . ' 2>&1'); return $out; });
t('ctf generator throws mid: cleanup', function() use ($D) { try { collection_to_file("$D/gen.csv", (function() { yield [1]; throw new LogicException("mid"); })()); } catch (LogicException $e) { return [file_get_contents("$D/gen.csv")]; } });
t('ctf same file as source', function() use ($D) { file_put_contents("$D/self.csv", "1,2\r\n"); collection_to_file("$D/self.csv", L::createFromFile("$D/self.csv")); return json_encode(file_get_contents("$D/self.csv")); });
echo "done\n";
