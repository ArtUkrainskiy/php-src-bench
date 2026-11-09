# Quality checks

49 of 85 prepared comparisons passed. Two attempts at most; keep the first passing capture, otherwise flag the first. All attempts are retained.

| Input | Decision | Flags | Measured variability | Paired ratio min–max |
|---|---|---|---|---:|
| comments.all.n8.b128.single | win | none | spread: call 4.05%, A/A call 4.11%, reference 3.86%; A/A change +0.95%; SMT busy 0.28%; CPU steal 0 ticks | 0.6682–0.7122 |
| comments.any.n16.b128.absent | win | none | spread: call 4.23%, A/A call 2.72%, reference 2.44%; A/A change -0.35%; SMT busy 0.00%; CPU steal 0 ticks | 0.7408–0.7845 |
| comments.count.n8.b128.single | win | none | spread: call 3.56%, A/A call 3.03%, reference 3.43%; A/A change -1.40%; SMT busy 0.47%; CPU steal 0 ticks | 0.8836–0.9360 |
| comments.replace.n16.b128.single | win | none | spread: call 4.01%, A/A call 2.91%, reference 3.28%; A/A change +0.52%; SMT busy 0.23%; CPU steal 0 ticks | 0.7238–0.7606 |
| comments.unique.n8.b128.single | win | none | spread: call 4.79%, A/A call 3.92%, reference 3.88%; A/A change -0.16%; SMT busy 0.27%; CPU steal 0 ticks | 0.5928–0.6260 |
| technical.all.n16.b1024.single | flagged | A/A, spread:prepared, spread:prepared_aa, spread:string_loop | spread: call 9.60%, A/A call 5.15%, reference 7.37%; A/A change -2.43%; SMT busy 0.28%; CPU steal 0 ticks | 0.5665–0.6995 |
| technical.all.n16.b128.single | win | none | spread: call 1.10%, A/A call 1.21%, reference 3.35%; A/A change -0.05%; SMT busy 0.56%; CPU steal 0 ticks | 0.4983–0.5212 |
| technical.all.n16.b256.single | win | none | spread: call 1.66%, A/A call 1.94%, reference 4.36%; A/A change -0.11%; SMT busy 0.27%; CPU steal 0 ticks | 0.5703–0.6128 |
| technical.all.n16.b4096.single | win | none | spread: call 4.33%, A/A call 4.09%, reference 4.38%; A/A change -1.21%; SMT busy 0.28%; CPU steal 0 ticks | 0.9285–0.9971 |
| technical.all.n32.b1024.single | flagged | A/A, spread:prepared, spread:prepared_aa, spread:string_loop | spread: call 12.75%, A/A call 16.08%, reference 14.38%; A/A change -3.91%; SMT busy 0.28%; CPU steal 0 ticks | 0.2802–0.3249 |
| technical.all.n32.b128.single | win | none | spread: call 0.59%, A/A call 0.75%, reference 0.39%; A/A change +0.56%; SMT busy 0.83%; CPU steal 0 ticks | 0.3293–0.3344 |
| technical.all.n32.b256.single | win | none | spread: call 0.79%, A/A call 0.72%, reference 3.12%; A/A change +0.07%; SMT busy 0.28%; CPU steal 0 ticks | 0.3594–0.3810 |
| technical.all.n32.b4096.single | win | none | spread: call 2.86%, A/A call 2.38%, reference 1.82%; A/A change -1.96%; SMT busy 0.55%; CPU steal 0 ticks | 0.4004–0.4233 |
| technical.all.n48.b1024.single | flagged | A/A, spread:prepared, spread:prepared_aa | spread: call 5.78%, A/A call 5.06%, reference 2.09%; A/A change -2.48%; SMT busy 0.55%; CPU steal 0 ticks | 0.1862–0.2081 |
| technical.all.n48.b128.single | win | none | spread: call 1.69%, A/A call 1.19%, reference 0.67%; A/A change -0.12%; SMT busy 0.00%; CPU steal 0 ticks | 0.2418–0.2483 |
| technical.all.n48.b256.single | flagged | SMT load, spread:prepared, spread:prepared_aa, spread:string_loop | spread: call 54.50%, A/A call 54.87%, reference 52.30%; A/A change -0.25%; SMT busy 85.74%; CPU steal 0 ticks | 0.2553–0.3526 |
| technical.all.n48.b4096.single | win | none | spread: call 4.12%, A/A call 2.98%, reference 2.27%; A/A change -1.02%; SMT busy 0.28%; CPU steal 0 ticks | 0.2570–0.2763 |
| technical.all.n8.b1024.single | flagged | A/A, spread:prepared, spread:prepared_aa | spread: call 6.03%, A/A call 6.57%, reference 3.51%; A/A change -2.35%; SMT busy 0.00%; CPU steal 0 ticks | 1.1922–1.3020 |
| technical.all.n8.b128.single | win | none | spread: call 0.96%, A/A call 1.06%, reference 1.73%; A/A change -1.92%; SMT busy 0.28%; CPU steal 0 ticks | 0.6985–0.7212 |
| technical.all.n8.b256.single | close | none | spread: call 0.62%, A/A call 0.68%, reference 2.16%; A/A change -0.94%; SMT busy 0.55%; CPU steal 0 ticks | 0.9617–0.9863 |
| technical.all.n8.b4096.single | loss | none | spread: call 2.49%, A/A call 4.19%, reference 1.83%; A/A change -0.89%; SMT busy 0.55%; CPU steal 0 ticks | 2.1388–2.2673 |
| technical.any.n16.b1024.absent | flagged | spread:prepared_aa, spread:preg_trie | spread: call 4.39%, A/A call 11.01%, reference 5.28%; A/A change -0.11%; SMT busy 0.23%; CPU steal 0 ticks | 1.4541–1.6773 |
| technical.any.n16.b128.absent | win | none | spread: call 1.22%, A/A call 1.02%, reference 2.42%; A/A change -0.22%; SMT busy 0.71%; CPU steal 0 ticks | 0.7748–0.7983 |
| technical.any.n16.b256.absent | flagged | SMT load, spread:prepared, spread:prepared_aa, spread:preg_trie | spread: call 50.65%, A/A call 42.05%, reference 75.65%; A/A change +0.36%; SMT busy 42.83%; CPU steal 0 ticks | 0.6890–1.1892 |
| technical.any.n16.b4096.absent | flagged | spread:prepared, spread:preg_trie | spread: call 5.08%, A/A call 4.42%, reference 5.91%; A/A change -0.48%; SMT busy 0.00%; CPU steal 0 ticks | 1.9552–2.1651 |
| technical.any.n32.b1024.absent | flagged | spread:prepared, spread:prepared_aa | spread: call 6.74%, A/A call 7.59%, reference 3.95%; A/A change -0.54%; SMT busy 0.23%; CPU steal 0 ticks | 0.8057–0.9099 |
| technical.any.n32.b128.absent | win | none | spread: call 0.76%, A/A call 1.25%, reference 1.71%; A/A change -0.42%; SMT busy 0.47%; CPU steal 0 ticks | 0.6288–0.6437 |
| technical.any.n32.b256.absent | win | none | spread: call 3.17%, A/A call 4.38%, reference 3.02%; A/A change +0.46%; SMT busy 0.47%; CPU steal 0 ticks | 0.5400–0.5763 |
| technical.any.n32.b4096.absent | loss | none | spread: call 3.19%, A/A call 4.35%, reference 4.93%; A/A change -0.95%; SMT busy 0.00%; CPU steal 0 ticks | 1.0737–1.2011 |
| technical.any.n48.b1024.absent | flagged | A/A, spread:prepared, spread:prepared_aa | spread: call 7.91%, A/A call 6.18%, reference 4.41%; A/A change -4.91%; SMT busy 0.23%; CPU steal 0 ticks | 0.5087–0.5698 |
| technical.any.n48.b128.absent | win | none | spread: call 0.90%, A/A call 1.41%, reference 0.57%; A/A change -0.05%; SMT busy 0.23%; CPU steal 0 ticks | 0.4697–0.4765 |
| technical.any.n48.b256.absent | flagged | SMT load, spread:prepared, spread:preg_trie | spread: call 21.40%, A/A call 2.81%, reference 36.74%; A/A change -0.21%; SMT busy 2.76%; CPU steal 0 ticks | 0.3856–0.4410 |
| technical.any.n48.b4096.absent | flagged | spread:prepared, spread:preg_trie | spread: call 15.10%, A/A call 4.32%, reference 11.53%; A/A change -1.11%; SMT busy 1.13%; CPU steal 0 ticks | 0.6703–0.7503 |
| technical.any.n8.b1024.absent | flagged | A/A, spread:prepared, spread:prepared_aa, spread:preg_literal | spread: call 25.28%, A/A call 9.96%, reference 7.43%; A/A change +2.62%; SMT busy 0.23%; CPU steal 0 ticks | 2.0770–2.5959 |
| technical.any.n8.b128.absent | close | none | spread: call 1.06%, A/A call 1.36%, reference 1.30%; A/A change -0.04%; SMT busy 0.46%; CPU steal 0 ticks | 1.0043–1.0281 |
| technical.any.n8.b256.absent | loss | none | spread: call 1.01%, A/A call 0.63%, reference 1.44%; A/A change -0.50%; SMT busy 0.00%; CPU steal 0 ticks | 1.3568–1.4043 |
| technical.any.n8.b4096.absent | loss | none | spread: call 2.41%, A/A call 1.36%, reference 4.67%; A/A change -0.25%; SMT busy 0.23%; CPU steal 0 ticks | 3.0649–3.4151 |
| technical.count.n16.b1024.single | flagged | spread:prepared, spread:prepared_aa, spread:preg_trie | spread: call 16.54%, A/A call 12.75%, reference 9.74%; A/A change +0.52%; SMT busy 0.72%; CPU steal 0 ticks | 0.4092–0.5751 |
| technical.count.n16.b128.single | win | none | spread: call 0.53%, A/A call 0.73%, reference 0.77%; A/A change -0.43%; SMT busy 0.23%; CPU steal 0 ticks | 0.5553–0.5655 |
| technical.count.n16.b256.single | flagged | spread:prepared, spread:prepared_aa, spread:substring_count_loop | spread: call 8.76%, A/A call 12.69%, reference 25.01%; A/A change -1.38%; SMT busy 1.14%; CPU steal 0 ticks | 0.5106–0.6513 |
| technical.count.n16.b4096.single | flagged | spread:prepared_aa, spread:preg_trie | spread: call 4.10%, A/A call 8.06%, reference 6.35%; A/A change -1.10%; SMT busy 0.00%; CPU steal 0 ticks | 0.4711–0.5168 |
| technical.count.n32.b1024.single | win | none | spread: call 3.80%, A/A call 4.59%, reference 4.29%; A/A change +0.08%; SMT busy 0.45%; CPU steal 0 ticks | 0.1929–0.2142 |
| technical.count.n32.b128.single | win | none | spread: call 1.67%, A/A call 0.88%, reference 0.75%; A/A change +0.10%; SMT busy 0.23%; CPU steal 0 ticks | 0.3173–0.3250 |
| technical.count.n32.b256.single | win | none | spread: call 1.42%, A/A call 1.17%, reference 3.42%; A/A change -0.41%; SMT busy 0.23%; CPU steal 0 ticks | 0.3405–0.3577 |
| technical.count.n32.b4096.single | win | none | spread: call 4.08%, A/A call 3.98%, reference 0.81%; A/A change -0.23%; SMT busy 0.23%; CPU steal 0 ticks | 0.1974–0.2120 |
| technical.count.n48.b1024.single | flagged | spread:prepared, spread:prepared_aa, spread:string_loop | spread: call 5.05%, A/A call 5.98%, reference 7.15%; A/A change +0.78%; SMT busy 0.47%; CPU steal 0 ticks | 0.1288–0.1491 |
| technical.count.n48.b128.single | flagged | SMT load, spread:prepared_aa, spread:substring_count_loop | spread: call 2.58%, A/A call 21.70%, reference 55.95%; A/A change -0.20%; SMT busy 5.23%; CPU steal 0 ticks | 0.1480–0.2332 |
| technical.count.n48.b256.single | flagged | spread:prepared, spread:prepared_aa, spread:string_loop | spread: call 6.22%, A/A call 5.80%, reference 5.33%; A/A change -0.01%; SMT busy 0.23%; CPU steal 0 ticks | 0.2434–0.2788 |
| technical.count.n48.b4096.single | flagged | spread:prepared, spread:prepared_aa, spread:string_loop | spread: call 6.87%, A/A call 5.12%, reference 5.42%; A/A change -0.07%; SMT busy 0.23%; CPU steal 0 ticks | 0.1290–0.1463 |
| technical.count.n8.b1024.single | win | none | spread: call 1.91%, A/A call 3.01%, reference 3.27%; A/A change +0.04%; SMT busy 0.00%; CPU steal 0 ticks | 0.8486–0.8971 |
| technical.count.n8.b128.single | win | none | spread: call 1.38%, A/A call 1.20%, reference 0.62%; A/A change +0.06%; SMT busy 0.23%; CPU steal 0 ticks | 0.9187–0.9415 |
| technical.count.n8.b256.single | loss | none | spread: call 0.71%, A/A call 0.73%, reference 0.95%; A/A change -0.02%; SMT busy 0.69%; CPU steal 0 ticks | 1.2237–1.2506 |
| technical.count.n8.b4096.single | flagged | spread:prepared, spread:prepared_aa, spread:preg_trie | spread: call 6.61%, A/A call 6.48%, reference 5.78%; A/A change +0.06%; SMT busy 0.00%; CPU steal 0 ticks | 0.9781–1.0925 |
| technical.replace.n16.b1024.single | flagged | A/A | spread: call 4.87%, A/A call 3.99%, reference 4.51%; A/A change +2.37%; SMT busy 0.00%; CPU steal 0 ticks | 0.8831–0.9558 |
| technical.replace.n16.b128.single | win | none | spread: call 1.11%, A/A call 1.04%, reference 1.67%; A/A change +0.71%; SMT busy 0.92%; CPU steal 0 ticks | 0.7839–0.8005 |
| technical.replace.n16.b256.single | win | none | spread: call 2.53%, A/A call 1.90%, reference 3.53%; A/A change -0.07%; SMT busy 0.23%; CPU steal 0 ticks | 0.8374–0.8684 |
| technical.replace.n16.b4096.single | flagged | A/A, spread:prepared, spread:preg_trie_callback | spread: call 7.87%, A/A call 4.98%, reference 6.09%; A/A change +3.18%; SMT busy 0.00%; CPU steal 0 ticks | 1.0050–1.1655 |
| technical.replace.n32.b1024.single | flagged | spread:prepared, spread:preg_trie_callback | spread: call 7.26%, A/A call 4.25%, reference 5.24%; A/A change +0.76%; SMT busy 0.69%; CPU steal 0 ticks | 0.5116–0.6147 |
| technical.replace.n32.b128.single | win | none | spread: call 0.61%, A/A call 0.96%, reference 1.34%; A/A change +0.72%; SMT busy 0.46%; CPU steal 0 ticks | 0.6138–0.6265 |
| technical.replace.n32.b256.single | win | none | spread: call 1.43%, A/A call 0.84%, reference 2.94%; A/A change +0.27%; SMT busy 0.00%; CPU steal 0 ticks | 0.5940–0.6207 |
| technical.replace.n32.b4096.single | flagged | spread:prepared, spread:prepared_aa, spread:preg_trie_callback | spread: call 6.47%, A/A call 5.07%, reference 6.69%; A/A change +1.67%; SMT busy 0.47%; CPU steal 0 ticks | 0.6763–0.7959 |
| technical.replace.n48.b1024.single | win | none | spread: call 4.29%, A/A call 2.53%, reference 4.00%; A/A change +1.73%; SMT busy 0.46%; CPU steal 0 ticks | 0.3812–0.4368 |
| technical.replace.n48.b128.single | win | none | spread: call 1.06%, A/A call 1.05%, reference 0.53%; A/A change -0.12%; SMT busy 0.23%; CPU steal 0 ticks | 0.5291–0.5389 |
| technical.replace.n48.b256.single | win | none | spread: call 3.72%, A/A call 3.52%, reference 4.33%; A/A change +0.21%; SMT busy 0.00%; CPU steal 0 ticks | 0.4785–0.5078 |
| technical.replace.n48.b4096.single | flagged | A/A, spread:prepared, spread:preg_trie_callback | spread: call 7.05%, A/A call 4.63%, reference 5.01%; A/A change +2.60%; SMT busy 0.00%; CPU steal 0 ticks | 0.4179–0.4735 |
| technical.replace.n8.b1024.single | loss | none | spread: call 2.46%, A/A call 3.69%, reference 2.72%; A/A change +1.22%; SMT busy 0.47%; CPU steal 0 ticks | 1.1795–1.2642 |
| technical.replace.n8.b128.single | loss | none | spread: call 2.88%, A/A call 3.94%, reference 0.66%; A/A change +1.38%; SMT busy 0.47%; CPU steal 0 ticks | 1.0736–1.1113 |
| technical.replace.n8.b256.single | loss | none | spread: call 0.97%, A/A call 1.27%, reference 1.33%; A/A change -0.10%; SMT busy 0.23%; CPU steal 0 ticks | 1.5332–1.5691 |
| technical.replace.n8.b4096.single | flagged | spread:prepared_aa, spread:preg_trie_callback | spread: call 4.00%, A/A call 7.21%, reference 5.10%; A/A change +1.48%; SMT busy 0.69%; CPU steal 0 ticks | 1.3019–1.5007 |
| technical.unique.n16.b1024.single | flagged | spread:prepared | spread: call 6.32%, A/A call 4.69%, reference 1.10%; A/A change -1.99%; SMT busy 0.27%; CPU steal 0 ticks | 0.3615–0.4081 |
| technical.unique.n16.b128.single | win | none | spread: call 1.86%, A/A call 0.97%, reference 1.12%; A/A change -0.29%; SMT busy 0.56%; CPU steal 0 ticks | 0.4406–0.4523 |
| technical.unique.n16.b256.single | flagged | spread:prepared, spread:prepared_aa, spread:string_loop | spread: call 8.42%, A/A call 10.44%, reference 9.24%; A/A change -0.69%; SMT busy 0.00%; CPU steal 0 ticks | 0.4815–0.5426 |
| technical.unique.n16.b4096.single | flagged | A/A, spread:prepared_aa, spread:preg_literal | spread: call 2.70%, A/A call 7.63%, reference 5.20%; A/A change -2.61%; SMT busy 0.00%; CPU steal 0 ticks | 0.7894–0.8911 |
| technical.unique.n32.b1024.single | flagged | spread:prepared, spread:prepared_aa, spread:string_loop | spread: call 9.55%, A/A call 6.93%, reference 9.94%; A/A change -1.26%; SMT busy 0.27%; CPU steal 0 ticks | 0.2229–0.2563 |
| technical.unique.n32.b128.single | flagged | spread:prepared, spread:prepared_aa, spread:string_loop | spread: call 8.57%, A/A call 7.60%, reference 5.93%; A/A change -0.45%; SMT busy 1.66%; CPU steal 0 ticks | 0.2797–0.3141 |
| technical.unique.n32.b256.single | win | none | spread: call 4.38%, A/A call 2.86%, reference 3.33%; A/A change -0.27%; SMT busy 0.00%; CPU steal 0 ticks | 0.3091–0.3265 |
| technical.unique.n32.b4096.single | win | none | spread: call 3.35%, A/A call 4.75%, reference 3.84%; A/A change -1.19%; SMT busy 0.28%; CPU steal 0 ticks | 0.3623–0.3845 |
| technical.unique.n48.b1024.single | flagged | spread:prepared | spread: call 7.00%, A/A call 4.46%, reference 3.36%; A/A change -1.54%; SMT busy 1.11%; CPU steal 0 ticks | 0.1472–0.1683 |
| technical.unique.n48.b128.single | win | none | spread: call 1.22%, A/A call 1.07%, reference 1.25%; A/A change +0.12%; SMT busy 0.56%; CPU steal 0 ticks | 0.2073–0.2154 |
| technical.unique.n48.b256.single | flagged | SMT load, spread:prepared_aa, spread:string_loop | spread: call 3.77%, A/A call 5.45%, reference 8.95%; A/A change -0.45%; SMT busy 3.32%; CPU steal 0 ticks | 0.2274–0.2494 |
| technical.unique.n48.b4096.single | flagged | A/A, spread:prepared_aa | spread: call 4.47%, A/A call 14.18%, reference 1.75%; A/A change -2.17%; SMT busy 1.39%; CPU steal 0 ticks | 0.2288–0.2530 |
| technical.unique.n8.b1024.single | win | none | spread: call 1.90%, A/A call 2.82%, reference 3.13%; A/A change -0.86%; SMT busy 0.00%; CPU steal 0 ticks | 0.7476–0.7817 |
| technical.unique.n8.b128.single | win | none | spread: call 3.54%, A/A call 1.05%, reference 2.19%; A/A change +0.89%; SMT busy 0.83%; CPU steal 0 ticks | 0.6033–0.6361 |
| technical.unique.n8.b256.single | win | none | spread: call 1.59%, A/A call 0.88%, reference 1.75%; A/A change -0.52%; SMT busy 0.28%; CPU steal 0 ticks | 0.8044–0.8344 |
| technical.unique.n8.b4096.single | flagged | spread:prepared | spread: call 6.94%, A/A call 4.07%, reference 1.46%; A/A change -1.32%; SMT busy 0.00%; CPU steal 0 ticks | 1.7332–1.9271 |

## Counter quality

321 of 391 implementation results passed all five 0/N pair checks. These checks are separate from timing quality. Flagged counters are marked †.

## Opposite directions between time and counters

Only comparisons passing both sets of checks are listed. Lower time need not mean fewer instructions; no cause is inferred.

| Input | Paired elapsed ratio | Cycles ratio | Instructions ratio |
|---|---:|---:|---:|
| technical.all.n16.b4096.single | 0.980 | 1.184 | 0.301 |
| technical.any.n32.b4096.absent | 1.139 | 1.425 | 0.392 |
| technical.any.n8.b4096.absent | 3.222 | 3.412 | 0.925 |
| technical.count.n8.b256.single | 1.232 | 1.248 | 0.945 |
| technical.replace.n8.b1024.single | 1.230 | 1.303 | 0.914 |
| technical.replace.n8.b128.single | 1.081 | 1.093 | 0.963 |
| technical.unique.n8.b1024.single | 0.773 | 0.728 | 1.179 |
