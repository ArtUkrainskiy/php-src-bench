<?php
$needle = substr('product-token-in-request-metadata', 0, 31);
if (strlen($needle) !== 31) { throw new LogicException('Expected a 31-byte needle'); }
return ['inputs' => ['early31' => 'prefix:' . $needle . str_repeat('normal application text ', 600)],
        'cases' => ['boundary/31/early-corrected' => ['code' => 'strpos($s, ' . var_export($needle, true) . ')', 'inputs' => ['early31']]]];
