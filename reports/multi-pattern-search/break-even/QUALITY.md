# Quality checks and uncertain points

111 of 128 native timing comparisons passed. Both modes have separate A/A controls and share the reference samples.

A win requires a paired median below 0.98 and every paired ratio below 1. A loss requires a median above 1.02 and every ratio above 1. Other qualified results are close. Flagged observations retain their time and measured relative change; the flag describes measurement quality.

The primary collector allows two attempts. 6 uncertain boundary inputs received one additional quality confirmation under the saved follow-up policy. A confirmation replaces the summary capture only when both modes pass; all original attempts remain in the raw data. No fastest-attempt selection is used.

| Input | Mode | State | Flags | Measured variability | Paired native/reference min–max |
|---|---|---|---|---|---:|
| comments.all.n32.b4096.single | prepared | win | none | spread: call 2.34%, A/A call 2.66%, reference 0.47%; A/A change -0.18%; SMT busy 1.94%; CPU steal 0 ticks | 0.3937–0.4093 |
| comments.all.n32.b4096.single | oneshot | loss | none | spread: call 1.04%, A/A call 0.84%, reference 0.47%; A/A change -0.08%; SMT busy 1.94%; CPU steal 0 ticks | 1.0472–1.0663 |
| comments.all.n48.b4096.single | prepared | win | none | spread: call 3.79%, A/A call 4.08%, reference 0.76%; A/A change -0.38%; SMT busy 0.97%; CPU steal 0 ticks | 0.2491–0.2630 |
| comments.all.n48.b4096.single | oneshot | win | none | spread: call 1.02%, A/A call 1.59%, reference 0.76%; A/A change +0.45%; SMT busy 0.97%; CPU steal 0 ticks | 0.9606–0.9795 |
| comments.any.n48.b32768.absent | prepared | win | none | spread: call 0.76%, A/A call 0.94%, reference 1.37%; A/A change -0.07%; SMT busy 0.52%; CPU steal 0 ticks | 0.4399–0.4529 |
| comments.any.n48.b32768.absent | oneshot | win | none | spread: call 1.68%, A/A call 1.64%, reference 1.37%; A/A change -0.12%; SMT busy 0.52%; CPU steal 0 ticks | 0.5724–0.5957 |
| comments.any.n48.b4096.absent | prepared | flagged | spread:preg_trie | spread: call 2.68%, A/A call 2.22%, reference 9.11%; A/A change -0.84%; SMT busy 0.34%; CPU steal 0 ticks | 0.6880–0.7845 |
| comments.any.n48.b4096.absent | oneshot | flagged | spread:preg_trie | spread: call 1.14%, A/A call 2.44%, reference 9.11%; A/A change -0.20%; SMT busy 0.34%; CPU steal 0 ticks | 2.5706–2.9665 |
| comments.any.n48.b65536.absent | prepared | win | none | spread: call 2.37%, A/A call 1.11%, reference 1.30%; A/A change -0.07%; SMT busy 1.21%; CPU steal 0 ticks | 0.4214–0.4392 |
| comments.any.n48.b65536.absent | oneshot | win | none | spread: call 1.70%, A/A call 1.76%, reference 1.30%; A/A change +0.05%; SMT busy 1.21%; CPU steal 0 ticks | 0.4979–0.5076 |
| comments.count.n32.b4096.single | prepared | flagged | A/A | spread: call 4.22%, A/A call 2.31%, reference 0.45%; A/A change -2.06%; SMT busy 0.20%; CPU steal 0 ticks | 0.1997–0.2147 |
| comments.count.n32.b4096.single | oneshot | win | none | spread: call 1.62%, A/A call 1.85%, reference 0.45%; A/A change +0.11%; SMT busy 0.20%; CPU steal 0 ticks | 0.8447–0.8737 |
| comments.count.n48.b4096.single | prepared | win | none | spread: call 4.76%, A/A call 4.80%, reference 0.42%; A/A change -1.62%; SMT busy 0.00%; CPU steal 0 ticks | 0.1280–0.1401 |
| comments.count.n48.b4096.single | oneshot | win | none | spread: call 0.99%, A/A call 1.22%, reference 0.42%; A/A change -0.30%; SMT busy 0.00%; CPU steal 0 ticks | 0.8947–0.9155 |
| comments.replace.n48.b16384.single | prepared | win | none | spread: call 3.16%, A/A call 3.62%, reference 3.90%; A/A change -0.14%; SMT busy 0.34%; CPU steal 0 ticks | 0.4638–0.5188 |
| comments.replace.n48.b16384.single | oneshot | win | none | spread: call 2.40%, A/A call 2.21%, reference 3.90%; A/A change -0.06%; SMT busy 0.34%; CPU steal 0 ticks | 0.6530–0.7248 |
| comments.unique.n16.b4096.single | prepared | loss | none | spread: call 2.15%, A/A call 0.80%, reference 1.70%; A/A change -0.04%; SMT busy 0.40%; CPU steal 0 ticks | 1.0102–1.0606 |
| comments.unique.n16.b4096.single | oneshot | loss | none | spread: call 1.19%, A/A call 0.95%, reference 1.70%; A/A change +0.37%; SMT busy 0.40%; CPU steal 0 ticks | 1.9289–1.9908 |
| comments.unique.n48.b4096.single | prepared | win | none | spread: call 1.42%, A/A call 0.65%, reference 0.67%; A/A change -0.55%; SMT busy 0.00%; CPU steal 0 ticks | 0.2420–0.2483 |
| comments.unique.n48.b4096.single | oneshot | win | none | spread: call 1.62%, A/A call 1.30%, reference 0.67%; A/A change -0.76%; SMT busy 0.00%; CPU steal 0 ticks | 0.9527–0.9752 |
| technical.all.n1.b4096.single | prepared | flagged | spread:prepared, spread:prepared_aa | spread: call 5.82%, A/A call 5.93%, reference 0.83%; A/A change +0.16%; SMT busy 1.42%; CPU steal 0 ticks | 17.8130–19.5121 |
| technical.all.n1.b4096.single | oneshot | loss | none | spread: call 1.79%, A/A call 1.13%, reference 0.83%; A/A change -0.00%; SMT busy 1.42%; CPU steal 0 ticks | 18.9929–19.4965 |
| technical.all.n16.b4096.single | prepared | loss | none | spread: call 1.66%, A/A call 2.30%, reference 1.45%; A/A change -0.13%; SMT busy 0.60%; CPU steal 0 ticks | 1.0702–1.1062 |
| technical.all.n16.b4096.single | oneshot | loss | none | spread: call 1.02%, A/A call 0.94%, reference 1.45%; A/A change -0.24%; SMT busy 0.60%; CPU steal 0 ticks | 1.9781–2.0267 |
| technical.all.n32.b4096.single | prepared | win | none | spread: call 4.09%, A/A call 2.40%, reference 0.46%; A/A change -0.68%; SMT busy 0.39%; CPU steal 0 ticks | 0.4028–0.4257 |
| technical.all.n32.b4096.single | oneshot | close | none | spread: call 0.98%, A/A call 1.33%, reference 0.46%; A/A change +0.08%; SMT busy 0.39%; CPU steal 0 ticks | 1.0077–1.0233 |
| technical.all.n48.b128.single | prepared | win | none | spread: call 1.50%, A/A call 1.60%, reference 0.68%; A/A change +0.14%; SMT busy 0.20%; CPU steal 0 ticks | 0.2412–0.2479 |
| technical.all.n48.b128.single | oneshot | loss | none | spread: call 0.62%, A/A call 0.77%, reference 0.68%; A/A change +0.16%; SMT busy 0.20%; CPU steal 0 ticks | 16.5998–16.8078 |
| technical.all.n48.b2048.single | prepared | flagged | spread:prepared | spread: call 5.70%, A/A call 3.17%, reference 0.81%; A/A change -0.52%; SMT busy 0.20%; CPU steal 0 ticks | 0.2159–0.2355 |
| technical.all.n48.b2048.single | oneshot | loss | none | spread: call 0.82%, A/A call 1.63%, reference 0.81%; A/A change -0.17%; SMT busy 0.20%; CPU steal 0 ticks | 1.5469–1.5729 |
| technical.all.n48.b4096.single | prepared | win | none | spread: call 2.34%, A/A call 1.53%, reference 0.42%; A/A change -0.43%; SMT busy 0.39%; CPU steal 0 ticks | 0.2606–0.2690 |
| technical.all.n48.b4096.single | oneshot | win | none | spread: call 0.85%, A/A call 2.10%, reference 0.42%; A/A change +0.34%; SMT busy 0.39%; CPU steal 0 ticks | 0.9482–0.9634 |
| technical.all.n48.b65536.single | prepared | win | none | spread: call 1.95%, A/A call 0.55%, reference 0.36%; A/A change -0.17%; SMT busy 0.20%; CPU steal 0 ticks | 0.2627–0.2686 |
| technical.all.n48.b65536.single | oneshot | win | none | spread: call 0.48%, A/A call 0.45%, reference 0.36%; A/A change -0.15%; SMT busy 0.20%; CPU steal 0 ticks | 0.3039–0.3066 |
| technical.all.n48.b8192.single | prepared | win | none | spread: call 0.71%, A/A call 1.22%, reference 0.56%; A/A change -0.15%; SMT busy 0.00%; CPU steal 0 ticks | 0.2818–0.2851 |
| technical.all.n48.b8192.single | oneshot | win | none | spread: call 0.49%, A/A call 0.78%, reference 0.56%; A/A change -0.13%; SMT busy 0.00%; CPU steal 0 ticks | 0.6368–0.6449 |
| technical.all.n8.b4096.single | prepared | loss | none | spread: call 2.29%, A/A call 1.15%, reference 2.37%; A/A change -0.22%; SMT busy 0.40%; CPU steal 0 ticks | 2.3481–2.4483 |
| technical.all.n8.b4096.single | oneshot | loss | none | spread: call 1.06%, A/A call 1.36%, reference 2.37%; A/A change -0.49%; SMT busy 0.40%; CPU steal 0 ticks | 2.9971–3.1394 |
| technical.any.n1.b4096.absent | prepared | loss | none | spread: call 3.13%, A/A call 1.84%, reference 1.15%; A/A change -0.56%; SMT busy 0.92%; CPU steal 0 ticks | 36.8997–39.3070 |
| technical.any.n1.b4096.absent | oneshot | loss | none | spread: call 1.64%, A/A call 1.30%, reference 1.15%; A/A change -0.04%; SMT busy 0.92%; CPU steal 0 ticks | 39.6179–41.2231 |
| technical.any.n16.b4096.absent | prepared | loss | none | spread: call 2.12%, A/A call 2.09%, reference 1.66%; A/A change +0.12%; SMT busy 0.52%; CPU steal 0 ticks | 2.2162–2.2777 |
| technical.any.n16.b4096.absent | oneshot | loss | none | spread: call 1.69%, A/A call 1.91%, reference 1.66%; A/A change +0.19%; SMT busy 0.52%; CPU steal 0 ticks | 4.1801–4.2656 |
| technical.any.n32.b4096.absent | prepared | loss | none | spread: call 4.03%, A/A call 3.77%, reference 2.51%; A/A change -1.10%; SMT busy 0.17%; CPU steal 0 ticks | 1.2219–1.3006 |
| technical.any.n32.b4096.absent | oneshot | loss | none | spread: call 1.34%, A/A call 1.87%, reference 2.51%; A/A change +0.09%; SMT busy 0.17%; CPU steal 0 ticks | 3.1049–3.2186 |
| technical.any.n48.b128.absent | prepared | win | none | spread: call 1.30%, A/A call 2.45%, reference 0.55%; A/A change +0.23%; SMT busy 0.69%; CPU steal 0 ticks | 0.4686–0.4779 |
| technical.any.n48.b128.absent | oneshot | loss | none | spread: call 0.95%, A/A call 1.44%, reference 0.55%; A/A change -0.20%; SMT busy 0.69%; CPU steal 0 ticks | 38.9831–39.7620 |
| technical.any.n48.b16384.absent | prepared | win | none | spread: call 0.57%, A/A call 0.76%, reference 0.94%; A/A change -0.22%; SMT busy 0.86%; CPU steal 0 ticks | 0.5773–0.5899 |
| technical.any.n48.b16384.absent | oneshot | close | none | spread: call 1.37%, A/A call 1.14%, reference 0.94%; A/A change +0.24%; SMT busy 0.86%; CPU steal 0 ticks | 1.0057–1.0338 |
| technical.any.n48.b2048.absent | prepared | win | none | spread: call 4.24%, A/A call 2.33%, reference 0.85%; A/A change -1.48%; SMT busy 0.35%; CPU steal 0 ticks | 0.6870–0.7435 |
| technical.any.n48.b2048.absent | oneshot | loss | none | spread: call 1.44%, A/A call 2.78%, reference 0.85%; A/A change -0.18%; SMT busy 0.35%; CPU steal 0 ticks | 4.8735–5.0343 |
| technical.any.n48.b32768.absent | prepared | win | none | spread: call 0.53%, A/A call 0.54%, reference 0.67%; A/A change +0.16%; SMT busy 0.69%; CPU steal 0 ticks | 0.5492–0.5560 |
| technical.any.n48.b32768.absent | oneshot | win | none | spread: call 0.98%, A/A call 0.63%, reference 0.67%; A/A change -0.05%; SMT busy 0.69%; CPU steal 0 ticks | 0.7575–0.7691 |
| technical.any.n48.b4096.absent | prepared | win | none | spread: call 4.54%, A/A call 1.75%, reference 4.86%; A/A change -0.30%; SMT busy 0.68%; CPU steal 0 ticks | 0.7193–0.8165 |
| technical.any.n48.b4096.absent | oneshot | loss | none | spread: call 1.44%, A/A call 1.71%, reference 4.86%; A/A change -0.62%; SMT busy 0.68%; CPU steal 0 ticks | 2.7817–3.0021 |
| technical.any.n48.b65536.absent | prepared | win | none | spread: call 0.73%, A/A call 0.64%, reference 0.56%; A/A change +0.05%; SMT busy 0.35%; CPU steal 0 ticks | 0.5043–0.5112 |
| technical.any.n48.b65536.absent | oneshot | win | none | spread: call 0.78%, A/A call 0.73%, reference 0.56%; A/A change +0.03%; SMT busy 0.35%; CPU steal 0 ticks | 0.6104–0.6176 |
| technical.any.n48.b65536.early | prepared | win | none | spread: call 1.55%, A/A call 1.63%, reference 0.90%; A/A change -0.02%; SMT busy 0.69%; CPU steal 0 ticks | 0.6456–0.6652 |
| technical.any.n48.b65536.early | oneshot | loss | none | spread: call 1.67%, A/A call 1.59%, reference 0.90%; A/A change +0.09%; SMT busy 0.69%; CPU steal 0 ticks | 88.0864–91.8221 |
| technical.any.n48.b65536.late | prepared | flagged | spread:prepared | spread: call 8.10%, A/A call 0.63%, reference 1.03%; A/A change -0.19%; SMT busy 0.17%; CPU steal 0 ticks | 0.4981–0.5447 |
| technical.any.n48.b65536.late | oneshot | win | none | spread: call 0.36%, A/A call 0.68%, reference 1.03%; A/A change -0.05%; SMT busy 0.17%; CPU steal 0 ticks | 0.6078–0.6189 |
| technical.any.n48.b65536.middle | prepared | flagged | SMT load | spread: call 0.71%, A/A call 0.82%, reference 1.71%; A/A change -0.24%; SMT busy 2.24%; CPU steal 0 ticks | 0.5431–0.5571 |
| technical.any.n48.b65536.middle | oneshot | flagged | SMT load | spread: call 1.44%, A/A call 1.60%, reference 1.71%; A/A change -0.37%; SMT busy 2.24%; CPU steal 0 ticks | 0.7597–0.7803 |
| technical.any.n48.b8192.absent | prepared | win | none | spread: call 1.96%, A/A call 0.99%, reference 1.81%; A/A change -0.16%; SMT busy 0.17%; CPU steal 0 ticks | 0.6555–0.6858 |
| technical.any.n48.b8192.absent | oneshot | loss | none | spread: call 0.84%, A/A call 1.67%, reference 1.81%; A/A change -0.61%; SMT busy 0.17%; CPU steal 0 ticks | 1.5540–1.6124 |
| technical.any.n8.b4096.absent | prepared | loss | none | spread: call 2.64%, A/A call 2.03%, reference 0.79%; A/A change -0.26%; SMT busy 0.17%; CPU steal 0 ticks | 3.2549–3.3928 |
| technical.any.n8.b4096.absent | oneshot | loss | none | spread: call 1.86%, A/A call 1.58%, reference 0.79%; A/A change -0.03%; SMT busy 0.17%; CPU steal 0 ticks | 4.2346–4.3507 |
| technical.count.n1.b4096.single | prepared | loss | none | spread: call 1.83%, A/A call 2.40%, reference 0.70%; A/A change -0.53%; SMT busy 0.79%; CPU steal 0 ticks | 12.0364–12.3858 |
| technical.count.n1.b4096.single | oneshot | loss | none | spread: call 2.58%, A/A call 1.94%, reference 0.70%; A/A change -0.48%; SMT busy 0.79%; CPU steal 0 ticks | 13.3083–13.8827 |
| technical.count.n16.b4096.single | prepared | flagged | A/A, spread:prepared | spread: call 5.37%, A/A call 4.38%, reference 2.80%; A/A change -2.70%; SMT busy 0.40%; CPU steal 0 ticks | 0.5133–0.5634 |
| technical.count.n16.b4096.single | oneshot | loss | none | spread: call 2.59%, A/A call 3.99%, reference 2.80%; A/A change +0.44%; SMT busy 0.40%; CPU steal 0 ticks | 1.5497–1.6278 |
| technical.count.n2.b4096.single | prepared | loss | none | spread: call 3.21%, A/A call 2.58%, reference 0.68%; A/A change +0.22%; SMT busy 0.40%; CPU steal 0 ticks | 3.9998–4.1309 |
| technical.count.n2.b4096.single | oneshot | loss | none | spread: call 1.23%, A/A call 2.25%, reference 0.68%; A/A change -0.52%; SMT busy 0.40%; CPU steal 0 ticks | 5.0103–5.1230 |
| technical.count.n32.b4096.single | prepared | win | none | spread: call 4.14%, A/A call 3.35%, reference 0.24%; A/A change -1.24%; SMT busy 0.59%; CPU steal 0 ticks | 0.1966–0.2108 |
| technical.count.n32.b4096.single | oneshot | win | none | spread: call 1.64%, A/A call 1.69%, reference 0.24%; A/A change -0.25%; SMT busy 0.59%; CPU steal 0 ticks | 0.8288–0.8579 |
| technical.count.n4.b4096.single | prepared | loss | none | spread: call 1.76%, A/A call 1.58%, reference 0.52%; A/A change -0.05%; SMT busy 0.20%; CPU steal 0 ticks | 2.7777–2.8549 |
| technical.count.n4.b4096.single | oneshot | loss | none | spread: call 0.65%, A/A call 1.91%, reference 0.52%; A/A change -0.15%; SMT busy 0.20%; CPU steal 0 ticks | 3.7676–3.8152 |
| technical.count.n48.b128.single | prepared | win | none | spread: call 0.73%, A/A call 0.82%, reference 0.99%; A/A change -0.11%; SMT busy 0.40%; CPU steal 0 ticks | 0.2218–0.2268 |
| technical.count.n48.b128.single | oneshot | loss | none | spread: call 0.88%, A/A call 1.43%, reference 0.99%; A/A change -0.03%; SMT busy 0.40%; CPU steal 0 ticks | 18.1265–18.6007 |
| technical.count.n48.b2048.single | prepared | win | none | spread: call 3.57%, A/A call 4.44%, reference 1.10%; A/A change -0.43%; SMT busy 0.60%; CPU steal 0 ticks | 0.1355–0.1432 |
| technical.count.n48.b2048.single | oneshot | loss | none | spread: call 1.10%, A/A call 1.30%, reference 1.10%; A/A change -0.94%; SMT busy 0.60%; CPU steal 0 ticks | 1.5349–1.5727 |
| technical.count.n48.b4096.single | prepared | win | none | spread: call 3.49%, A/A call 4.19%, reference 1.49%; A/A change -1.02%; SMT busy 0.78%; CPU steal 0 ticks | 0.1277–0.1366 |
| technical.count.n48.b4096.single | oneshot | win | none | spread: call 1.46%, A/A call 2.04%, reference 1.49%; A/A change +0.36%; SMT busy 0.78%; CPU steal 0 ticks | 0.8675–0.8971 |
| technical.count.n48.b65536.single | prepared | win | none | spread: call 0.58%, A/A call 0.52%, reference 0.64%; A/A change -0.22%; SMT busy 0.99%; CPU steal 0 ticks | 0.2409–0.2442 |
| technical.count.n48.b65536.single | oneshot | win | none | spread: call 0.66%, A/A call 4.24%, reference 0.64%; A/A change +0.21%; SMT busy 0.99%; CPU steal 0 ticks | 0.2946–0.2979 |
| technical.count.n48.b8192.single | prepared | win | none | spread: call 1.16%, A/A call 1.10%, reference 0.78%; A/A change -0.40%; SMT busy 0.40%; CPU steal 0 ticks | 0.1875–0.1924 |
| technical.count.n48.b8192.single | oneshot | win | none | spread: call 1.41%, A/A call 1.24%, reference 0.78%; A/A change -0.23%; SMT busy 0.40%; CPU steal 0 ticks | 0.6070–0.6232 |
| technical.count.n8.b4096.single | prepared | flagged | A/A, spread:prepared | spread: call 5.15%, A/A call 2.55%, reference 0.84%; A/A change -2.02%; SMT busy 0.99%; CPU steal 0 ticks | 1.0506–1.1336 |
| technical.count.n8.b4096.single | oneshot | flagged | spread:oneshot_aa | spread: call 2.47%, A/A call 7.88%, reference 0.84%; A/A change +0.19%; SMT busy 0.99%; CPU steal 0 ticks | 1.8692–1.9475 |
| technical.replace.n1.b4096.single | prepared | loss | none | spread: call 3.33%, A/A call 1.72%, reference 0.78%; A/A change +0.06%; SMT busy 0.52%; CPU steal 0 ticks | 13.7076–14.4427 |
| technical.replace.n1.b4096.single | oneshot | loss | none | spread: call 2.10%, A/A call 4.52%, reference 0.78%; A/A change +0.18%; SMT busy 0.52%; CPU steal 0 ticks | 14.8267–15.4389 |
| technical.replace.n16.b4096.single | prepared | loss | none | spread: call 3.23%, A/A call 1.96%, reference 1.68%; A/A change -0.72%; SMT busy 0.68%; CPU steal 0 ticks | 1.1256–1.2066 |
| technical.replace.n16.b4096.single | oneshot | loss | none | spread: call 1.44%, A/A call 3.00%, reference 1.68%; A/A change +0.99%; SMT busy 0.68%; CPU steal 0 ticks | 1.7880–1.8787 |
| technical.replace.n32.b4096.single | prepared | win | none | spread: call 1.70%, A/A call 3.40%, reference 3.93%; A/A change +0.51%; SMT busy 0.69%; CPU steal 0 ticks | 0.7473–0.8149 |
| technical.replace.n32.b4096.single | oneshot | loss | none | spread: call 2.17%, A/A call 2.27%, reference 3.93%; A/A change +0.34%; SMT busy 0.69%; CPU steal 0 ticks | 1.8908–2.0666 |
| technical.replace.n4.b4096.single | prepared | loss | none | spread: call 4.17%, A/A call 2.00%, reference 1.11%; A/A change -1.11%; SMT busy 0.52%; CPU steal 0 ticks | 1.8772–2.0009 |
| technical.replace.n4.b4096.single | oneshot | loss | none | spread: call 1.81%, A/A call 2.10%, reference 1.11%; A/A change +0.25%; SMT busy 0.52%; CPU steal 0 ticks | 2.2782–2.3175 |
| technical.replace.n48.b128.single | prepared | win | none | spread: call 0.99%, A/A call 1.36%, reference 1.35%; A/A change +0.26%; SMT busy 1.04%; CPU steal 0 ticks | 0.5288–0.5436 |
| technical.replace.n48.b128.single | oneshot | loss | none | spread: call 1.25%, A/A call 1.80%, reference 1.35%; A/A change -0.20%; SMT busy 1.04%; CPU steal 0 ticks | 24.7610–25.5737 |
| technical.replace.n48.b16384.single | prepared | flagged | spread:prepared, spread:prepared_aa | spread: call 6.23%, A/A call 7.88%, reference 1.74%; A/A change +0.17%; SMT busy 1.55%; CPU steal 0 ticks | 0.5128–0.5491 |
| technical.replace.n48.b16384.single | oneshot | win | none | spread: call 3.22%, A/A call 3.85%, reference 1.74%; A/A change -0.87%; SMT busy 1.55%; CPU steal 0 ticks | 0.7318–0.7733 |
| technical.replace.n48.b2048.single | prepared | win | none | spread: call 3.32%, A/A call 4.87%, reference 2.08%; A/A change +0.42%; SMT busy 0.00%; CPU steal 0 ticks | 0.4056–0.4331 |
| technical.replace.n48.b2048.single | oneshot | loss | none | spread: call 1.37%, A/A call 1.35%, reference 2.08%; A/A change -0.07%; SMT busy 0.00%; CPU steal 0 ticks | 2.9832–3.1079 |
| technical.replace.n48.b4096.single | prepared | flagged | spread:prepared, spread:prepared_aa, spread:preg_trie_callback | spread: call 5.04%, A/A call 7.70%, reference 5.41%; A/A change -0.48%; SMT busy 0.17%; CPU steal 0 ticks | 0.4472–0.4870 |
| technical.replace.n48.b4096.single | oneshot | flagged | spread:preg_trie_callback | spread: call 0.75%, A/A call 1.57%, reference 5.41%; A/A change +0.39%; SMT busy 0.17%; CPU steal 0 ticks | 1.7044–1.8316 |
| technical.replace.n48.b65536.single | prepared | flagged | spread:prepared, spread:prepared_aa | spread: call 5.89%, A/A call 5.72%, reference 0.67%; A/A change -0.01%; SMT busy 0.69%; CPU steal 0 ticks | 0.4790–0.5162 |
| technical.replace.n48.b65536.single | oneshot | win | none | spread: call 3.43%, A/A call 3.57%, reference 0.67%; A/A change +0.15%; SMT busy 0.69%; CPU steal 0 ticks | 0.5393–0.5619 |
| technical.replace.n48.b8192.single | prepared | win | none | spread: call 3.46%, A/A call 2.88%, reference 3.39%; A/A change -0.30%; SMT busy 1.04%; CPU steal 0 ticks | 0.5572–0.5916 |
| technical.replace.n48.b8192.single | oneshot | loss | none | spread: call 2.11%, A/A call 2.92%, reference 3.39%; A/A change -0.17%; SMT busy 1.04%; CPU steal 0 ticks | 1.1013–1.1618 |
| technical.replace.n8.b4096.single | prepared | flagged | A/A, SMT load | spread: call 3.33%, A/A call 4.90%, reference 0.92%; A/A change -2.82%; SMT busy 2.09%; CPU steal 0 ticks | 1.4649–1.5476 |
| technical.replace.n8.b4096.single | oneshot | flagged | SMT load, spread:oneshot_aa | spread: call 1.96%, A/A call 5.61%, reference 0.92%; A/A change +0.30%; SMT busy 2.09%; CPU steal 0 ticks | 2.0507–2.1283 |
| technical.unique.n1.b4096.single | prepared | loss | none | spread: call 1.49%, A/A call 1.84%, reference 1.08%; A/A change +0.02%; SMT busy 0.52%; CPU steal 0 ticks | 16.1188–16.6411 |
| technical.unique.n1.b4096.single | oneshot | loss | none | spread: call 1.32%, A/A call 1.34%, reference 1.08%; A/A change +0.40%; SMT busy 0.52%; CPU steal 0 ticks | 18.7746–19.2205 |
| technical.unique.n16.b4096.single | prepared | win | none | spread: call 2.03%, A/A call 1.47%, reference 1.05%; A/A change -0.40%; SMT busy 0.39%; CPU steal 0 ticks | 0.8578–0.8886 |
| technical.unique.n16.b4096.single | oneshot | loss | none | spread: call 0.80%, A/A call 1.17%, reference 1.05%; A/A change +0.07%; SMT busy 0.39%; CPU steal 0 ticks | 1.7584–1.7938 |
| technical.unique.n32.b4096.single | prepared | win | none | spread: call 1.46%, A/A call 1.39%, reference 0.38%; A/A change -0.49%; SMT busy 0.79%; CPU steal 0 ticks | 0.3506–0.3604 |
| technical.unique.n32.b4096.single | oneshot | close | none | spread: call 1.55%, A/A call 1.45%, reference 0.38%; A/A change -0.80%; SMT busy 0.79%; CPU steal 0 ticks | 0.9639–0.9960 |
| technical.unique.n48.b128.single | prepared | win | none | spread: call 1.01%, A/A call 0.96%, reference 1.08%; A/A change -0.11%; SMT busy 0.40%; CPU steal 0 ticks | 0.2104–0.2157 |
| technical.unique.n48.b128.single | oneshot | loss | none | spread: call 1.07%, A/A call 0.83%, reference 1.08%; A/A change +0.01%; SMT busy 0.40%; CPU steal 0 ticks | 16.1150–16.4623 |
| technical.unique.n48.b2048.single | prepared | win | none | spread: call 2.44%, A/A call 1.27%, reference 0.94%; A/A change -0.87%; SMT busy 0.39%; CPU steal 0 ticks | 0.1797–0.1850 |
| technical.unique.n48.b2048.single | oneshot | loss | none | spread: call 1.75%, A/A call 1.46%, reference 0.94%; A/A change +0.07%; SMT busy 0.39%; CPU steal 0 ticks | 1.5057–1.5542 |
| technical.unique.n48.b4096.single | prepared | win | none | spread: call 3.60%, A/A call 2.35%, reference 0.41%; A/A change -0.63%; SMT busy 0.20%; CPU steal 0 ticks | 0.2157–0.2306 |
| technical.unique.n48.b4096.single | oneshot | win | none | spread: call 0.87%, A/A call 1.05%, reference 0.41%; A/A change -0.61%; SMT busy 0.20%; CPU steal 0 ticks | 0.9248–0.9413 |
| technical.unique.n48.b65536.single | prepared | win | none | spread: call 1.75%, A/A call 1.29%, reference 0.70%; A/A change +0.02%; SMT busy 0.20%; CPU steal 0 ticks | 0.2511–0.2587 |
| technical.unique.n48.b65536.single | oneshot | win | none | spread: call 0.58%, A/A call 1.31%, reference 0.70%; A/A change -0.26%; SMT busy 0.20%; CPU steal 0 ticks | 0.3049–0.3094 |
| technical.unique.n48.b8192.single | prepared | win | none | spread: call 1.13%, A/A call 3.39%, reference 0.40%; A/A change +0.06%; SMT busy 0.20%; CPU steal 0 ticks | 0.2564–0.2628 |
| technical.unique.n48.b8192.single | oneshot | win | none | spread: call 1.14%, A/A call 1.11%, reference 0.40%; A/A change -0.12%; SMT busy 0.20%; CPU steal 0 ticks | 0.6198–0.6342 |
| technical.unique.n8.b4096.single | prepared | loss | none | spread: call 3.26%, A/A call 4.03%, reference 0.58%; A/A change -0.11%; SMT busy 0.79%; CPU steal 0 ticks | 1.8722–1.9567 |
| technical.unique.n8.b4096.single | oneshot | loss | none | spread: call 2.34%, A/A call 3.51%, reference 0.58%; A/A change +0.20%; SMT busy 0.79%; CPU steal 0 ticks | 2.6111–2.7065 |

## Hardware counters

271 of 351 method results passed all five 0/N pairs. A failed pair flags its median independently of timing quality. Events must run for at least 99% of the interval; corrected counts must be positive and sibling load at most 2%. Raw pairs identify the failed checks.

## Faster time with more cycles or instructions

Only comparisons passing both timing and relevant counter checks are listed. Ratios below 1 favor the native operation. A lower elapsed time does not imply fewer instructions; these measurements do not identify the cause of different instruction throughput.

| Input | Mode | Paired elapsed native/reference | Cycles native/reference | Instructions native/reference |
|---|---|---:|---:|---:|
| comments.unique.n48.b4096.single | oneshot | 0.966 | 0.970 | 2.095 |
| technical.all.n48.b4096.single | oneshot | 0.957 | 0.965 | 2.029 |
| technical.all.n48.b8192.single | oneshot | 0.640 | 0.652 | 1.199 |
| technical.any.n16.b4096.absent | prepared | 2.247 | 2.281 | 0.566 |
| technical.count.n32.b4096.single | oneshot | 0.845 | 0.859 | 2.011 |
| technical.count.n48.b4096.single | oneshot | 0.885 | 0.895 | 2.042 |
| technical.count.n48.b8192.single | oneshot | 0.613 | 0.621 | 1.202 |
| technical.replace.n16.b4096.single | prepared | 1.162 | 1.207 | 0.612 |
| technical.replace.n48.b8192.single | oneshot | 1.130 | 1.155 | 0.910 |
| technical.unique.n48.b8192.single | oneshot | 0.628 | 0.635 | 1.249 |
| technical.unique.n8.b4096.single | prepared | 1.941 | 1.854 | 0.685 |
