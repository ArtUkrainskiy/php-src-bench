<?php
// Small independent compact-Sunday comparison; no adaptive engine is included.
$suite = require __DIR__ . '/../../suites/substr-product.php';
$wanted = [];
foreach (['en', 'ru', 'es', 'ar', 'hi', 'zh', 'ja', 'ko', 'emoji'] as $lang) {
    $wanted[] = "banlist12/$lang/post/clean";
    $wanted[] = "banlist12/$lang/thread/clean";
}
$wanted = array_merge($wanted, ['render-template/4k', 'parse-http/body64k', 'explode/colon2/4k', 'explode/pipe2/4k']);
$suite['cases'] = array_intersect_key($suite['cases'], array_flip($wanted));
$suite['cases']['count-template/4k'] = ['code' => "substr_count(\$s, '{{order.id}}')", 'inputs' => ['template-4k']];
$suite['inputs']['short-absent'] = str_repeat('normal application text ', 600);
$suite['inputs']['short-early'] = 'prefix:product-token-in-request-metadat' . str_repeat('normal application text ', 600);
$suite['inputs']['long-early'] = 'prefix:' . str_repeat('a', 31) . 'b' . str_repeat('ordinary text ', 1200);
$suite['cases']['boundary/9/absent'] = ['code' => "strpos(\$s, 'product-t')", 'inputs' => ['short-absent']];
$suite['cases']['boundary/31/early'] = ['code' => "strpos(\$s, 'product-token-in-request-metadat')", 'inputs' => ['short-early']];
$suite['cases']['boundary/32/early'] = ['code' => 'strpos($s, ' . var_export(str_repeat('a', 31) . 'b', true) . ')', 'inputs' => ['long-early']];
return $suite;
