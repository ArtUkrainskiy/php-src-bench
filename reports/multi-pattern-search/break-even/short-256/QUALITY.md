# Quality checks

68 of 68 native timing comparisons passed. The primary two-attempt policy, A/A, spread and sibling-load limits match the parent study.

A win requires a paired median below 0.98 and every paired ratio below 1. A loss requires a median above 1.02 and every ratio above 1. Other qualified results are inconclusive.

| Input | Mode | Decision | Flags | Measured variability | Paired ratio min–max |
|---|---|---|---|---|---:|
| comments.all.n8.b256.single | prepared | loss | none | spread: call 0.76%, A/A call 0.70%, reference 0.53%; A/A change +0.05%; SMT busy 0.40%; CPU steal 0 ticks | 1.0314–1.0479 |
| comments.all.n8.b256.single | oneshot | loss | none | spread: call 2.73%, A/A call 3.06%, reference 0.53%; A/A change -0.20%; SMT busy 0.40%; CPU steal 0 ticks | 7.3264–7.6286 |
| comments.any.n16.b256.absent | prepared | win | none | spread: call 4.53%, A/A call 3.18%, reference 0.54%; A/A change +0.52%; SMT busy 0.35%; CPU steal 0 ticks | 0.8650–0.9137 |
| comments.any.n16.b256.absent | oneshot | loss | none | spread: call 0.61%, A/A call 0.60%, reference 0.54%; A/A change +0.09%; SMT busy 0.35%; CPU steal 0 ticks | 18.3232–18.5644 |
| comments.count.n16.b256.single | prepared | win | none | spread: call 0.50%, A/A call 1.05%, reference 0.90%; A/A change -0.03%; SMT busy 0.17%; CPU steal 0 ticks | 0.5725–0.5839 |
| comments.count.n16.b256.single | oneshot | loss | none | spread: call 0.37%, A/A call 0.36%, reference 0.90%; A/A change +0.05%; SMT busy 0.17%; CPU steal 0 ticks | 11.4972–11.6728 |
| comments.replace.n16.b256.single | prepared | win | none | spread: call 0.86%, A/A call 1.09%, reference 0.56%; A/A change -0.16%; SMT busy 0.35%; CPU steal 0 ticks | 0.9117–0.9290 |
| comments.replace.n16.b256.single | oneshot | loss | none | spread: call 1.76%, A/A call 1.81%, reference 0.56%; A/A change -0.02%; SMT busy 0.35%; CPU steal 0 ticks | 7.3952–7.6028 |
| comments.unique.n8.b256.single | prepared | win | none | spread: call 2.26%, A/A call 2.30%, reference 1.04%; A/A change +0.01%; SMT busy 0.20%; CPU steal 0 ticks | 0.8767–0.9017 |
| comments.unique.n8.b256.single | oneshot | loss | none | spread: call 0.65%, A/A call 0.38%, reference 1.04%; A/A change +0.03%; SMT busy 0.20%; CPU steal 0 ticks | 7.2908–7.4516 |
| technical.all.n1.b256.single | prepared | loss | none | spread: call 0.74%, A/A call 0.63%, reference 0.78%; A/A change -0.14%; SMT busy 0.20%; CPU steal 0 ticks | 1.3744–1.4050 |
| technical.all.n1.b256.single | oneshot | loss | none | spread: call 0.78%, A/A call 1.15%, reference 0.78%; A/A change +0.12%; SMT busy 0.20%; CPU steal 0 ticks | 2.4583–2.4954 |
| technical.all.n16.b256.single | prepared | win | none | spread: call 0.78%, A/A call 0.52%, reference 0.73%; A/A change +0.14%; SMT busy 0.00%; CPU steal 0 ticks | 0.6115–0.6196 |
| technical.all.n16.b256.single | oneshot | loss | none | spread: call 0.60%, A/A call 0.27%, reference 0.73%; A/A change -0.13%; SMT busy 0.00%; CPU steal 0 ticks | 10.5641–10.7149 |
| technical.all.n4.b256.single | prepared | loss | none | spread: call 1.39%, A/A call 0.82%, reference 0.62%; A/A change -0.24%; SMT busy 0.20%; CPU steal 0 ticks | 1.2220–1.2538 |
| technical.all.n4.b256.single | oneshot | loss | none | spread: call 2.55%, A/A call 2.78%, reference 0.62%; A/A change +0.03%; SMT busy 0.20%; CPU steal 0 ticks | 4.7738–4.9855 |
| technical.all.n48.b256.single | prepared | win | none | spread: call 1.73%, A/A call 0.68%, reference 1.06%; A/A change -0.32%; SMT busy 0.00%; CPU steal 0 ticks | 0.2855–0.2928 |
| technical.all.n48.b256.single | oneshot | loss | none | spread: call 0.93%, A/A call 1.13%, reference 1.06%; A/A change -0.28%; SMT busy 0.00%; CPU steal 0 ticks | 13.4956–13.7130 |
| technical.all.n8.b256.single | prepared | win | none | spread: call 0.80%, A/A call 0.58%, reference 0.89%; A/A change -0.08%; SMT busy 0.39%; CPU steal 0 ticks | 0.9674–0.9868 |
| technical.all.n8.b256.single | oneshot | loss | none | spread: call 1.12%, A/A call 1.13%, reference 0.89%; A/A change +0.08%; SMT busy 0.39%; CPU steal 0 ticks | 6.7728–6.9401 |
| technical.any.n1.b256.absent | prepared | loss | none | spread: call 0.54%, A/A call 0.60%, reference 1.37%; A/A change -0.10%; SMT busy 0.16%; CPU steal 0 ticks | 2.5326–2.5970 |
| technical.any.n1.b256.absent | oneshot | loss | none | spread: call 0.56%, A/A call 0.60%, reference 1.37%; A/A change -0.03%; SMT busy 0.16%; CPU steal 0 ticks | 5.0084–5.1145 |
| technical.any.n16.b256.absent | prepared | win | none | spread: call 0.86%, A/A call 1.26%, reference 0.65%; A/A change +0.11%; SMT busy 0.00%; CPU steal 0 ticks | 0.8325–0.8537 |
| technical.any.n16.b256.absent | oneshot | loss | none | spread: call 0.88%, A/A call 0.71%, reference 0.65%; A/A change -0.08%; SMT busy 0.00%; CPU steal 0 ticks | 17.2068–17.5338 |
| technical.any.n4.b256.absent | prepared | loss | none | spread: call 1.20%, A/A call 1.01%, reference 1.65%; A/A change -0.08%; SMT busy 0.17%; CPU steal 0 ticks | 1.8316–1.8728 |
| technical.any.n4.b256.absent | oneshot | loss | none | spread: call 3.69%, A/A call 3.45%, reference 1.65%; A/A change +0.14%; SMT busy 0.17%; CPU steal 0 ticks | 8.0194–8.4925 |
| technical.any.n48.b256.absent | prepared | win | none | spread: call 0.47%, A/A call 0.75%, reference 0.80%; A/A change +0.35%; SMT busy 0.17%; CPU steal 0 ticks | 0.4291–0.4373 |
| technical.any.n48.b256.absent | oneshot | loss | none | spread: call 0.93%, A/A call 0.71%, reference 0.80%; A/A change -0.06%; SMT busy 0.17%; CPU steal 0 ticks | 24.5908–25.0148 |
| technical.any.n48.b256.early | prepared | win | none | spread: call 2.38%, A/A call 0.81%, reference 1.38%; A/A change -0.34%; SMT busy 0.17%; CPU steal 0 ticks | 0.6514–0.6795 |
| technical.any.n48.b256.early | oneshot | loss | none | spread: call 2.21%, A/A call 0.67%, reference 1.38%; A/A change -0.09%; SMT busy 0.17%; CPU steal 0 ticks | 86.8913–89.7718 |
| technical.any.n48.b256.late | prepared | win | none | spread: call 2.45%, A/A call 0.60%, reference 2.30%; A/A change +0.05%; SMT busy 0.17%; CPU steal 0 ticks | 0.4901–0.5184 |
| technical.any.n48.b256.late | oneshot | loss | none | spread: call 0.83%, A/A call 0.83%, reference 2.30%; A/A change +0.10%; SMT busy 0.17%; CPU steal 0 ticks | 28.6515–29.4133 |
| technical.any.n48.b256.middle | prepared | win | none | spread: call 1.08%, A/A call 1.02%, reference 1.19%; A/A change +0.04%; SMT busy 0.17%; CPU steal 0 ticks | 0.4806–0.4949 |
| technical.any.n48.b256.middle | oneshot | loss | none | spread: call 2.76%, A/A call 2.03%, reference 1.19%; A/A change -0.03%; SMT busy 0.17%; CPU steal 0 ticks | 38.9216–40.3457 |
| technical.any.n8.b256.absent | prepared | loss | none | spread: call 0.61%, A/A call 0.67%, reference 0.71%; A/A change +0.21%; SMT busy 0.00%; CPU steal 0 ticks | 1.3728–1.3976 |
| technical.any.n8.b256.absent | oneshot | loss | none | spread: call 1.90%, A/A call 0.55%, reference 0.71%; A/A change -0.10%; SMT busy 0.00%; CPU steal 0 ticks | 11.5259–11.7934 |
| technical.count.n1.b256.single | prepared | loss | none | spread: call 0.87%, A/A call 0.68%, reference 1.09%; A/A change +0.10%; SMT busy 0.16%; CPU steal 0 ticks | 2.4787–2.5484 |
| technical.count.n1.b256.single | oneshot | loss | none | spread: call 0.91%, A/A call 1.93%, reference 1.09%; A/A change -0.18%; SMT busy 0.16%; CPU steal 0 ticks | 4.9710–5.0841 |
| technical.count.n16.b256.single | prepared | win | none | spread: call 0.59%, A/A call 0.71%, reference 0.56%; A/A change +0.04%; SMT busy 0.35%; CPU steal 0 ticks | 0.6177–0.6292 |
| technical.count.n16.b256.single | oneshot | loss | none | spread: call 0.53%, A/A call 0.59%, reference 0.56%; A/A change -0.11%; SMT busy 0.35%; CPU steal 0 ticks | 12.4171–12.5802 |
| technical.count.n4.b256.single | prepared | loss | none | spread: call 1.09%, A/A call 1.41%, reference 0.65%; A/A change +0.15%; SMT busy 0.00%; CPU steal 0 ticks | 1.6970–1.7215 |
| technical.count.n4.b256.single | oneshot | loss | none | spread: call 1.47%, A/A call 1.32%, reference 0.65%; A/A change -0.02%; SMT busy 0.00%; CPU steal 0 ticks | 7.5644–7.7579 |
| technical.count.n48.b256.single | prepared | win | none | spread: call 0.81%, A/A call 0.29%, reference 1.35%; A/A change -0.21%; SMT busy 0.17%; CPU steal 0 ticks | 0.2591–0.2643 |
| technical.count.n48.b256.single | oneshot | loss | none | spread: call 1.36%, A/A call 1.09%, reference 1.35%; A/A change -0.12%; SMT busy 0.17%; CPU steal 0 ticks | 14.0449–14.4050 |
| technical.count.n48.b4096.single | prepared | win | none | spread: call 4.57%, A/A call 2.48%, reference 0.29%; A/A change -0.08%; SMT busy 0.17%; CPU steal 0 ticks | 0.1299–0.1376 |
| technical.count.n48.b4096.single | oneshot | win | none | spread: call 1.06%, A/A call 1.25%, reference 0.29%; A/A change -0.23%; SMT busy 0.17%; CPU steal 0 ticks | 0.8754–0.8927 |
| technical.count.n8.b256.single | prepared | loss | none | spread: call 0.62%, A/A call 0.82%, reference 1.46%; A/A change -0.17%; SMT busy 0.17%; CPU steal 0 ticks | 1.2162–1.2561 |
| technical.count.n8.b256.single | oneshot | loss | none | spread: call 0.81%, A/A call 0.88%, reference 1.46%; A/A change +0.22%; SMT busy 0.17%; CPU steal 0 ticks | 10.0869–10.3512 |
| technical.replace.n1.b256.single | prepared | loss | none | spread: call 0.99%, A/A call 0.87%, reference 2.20%; A/A change -0.05%; SMT busy 0.17%; CPU steal 0 ticks | 2.0961–2.1741 |
| technical.replace.n1.b256.single | oneshot | loss | none | spread: call 4.68%, A/A call 3.44%, reference 2.20%; A/A change -0.09%; SMT busy 0.17%; CPU steal 0 ticks | 3.9727–4.2687 |
| technical.replace.n16.b256.single | prepared | win | none | spread: call 0.92%, A/A call 1.08%, reference 0.58%; A/A change -0.14%; SMT busy 0.35%; CPU steal 0 ticks | 0.8734–0.8872 |
| technical.replace.n16.b256.single | oneshot | loss | none | spread: call 1.85%, A/A call 1.40%, reference 0.58%; A/A change -0.13%; SMT busy 0.35%; CPU steal 0 ticks | 6.9664–7.1457 |
| technical.replace.n4.b256.single | prepared | loss | none | spread: call 0.56%, A/A call 0.99%, reference 1.22%; A/A change +0.04%; SMT busy 0.00%; CPU steal 0 ticks | 1.7833–1.8160 |
| technical.replace.n4.b256.single | oneshot | loss | none | spread: call 0.53%, A/A call 0.55%, reference 1.22%; A/A change +0.02%; SMT busy 0.00%; CPU steal 0 ticks | 5.5374–5.6433 |
| technical.replace.n48.b256.single | prepared | win | none | spread: call 1.31%, A/A call 0.69%, reference 0.55%; A/A change -1.38%; SMT busy 0.34%; CPU steal 0 ticks | 0.5120–0.5229 |
| technical.replace.n48.b256.single | oneshot | loss | none | spread: call 0.84%, A/A call 0.63%, reference 0.55%; A/A change -0.08%; SMT busy 0.34%; CPU steal 0 ticks | 15.9342–16.1724 |
| technical.replace.n8.b256.single | prepared | loss | none | spread: call 1.05%, A/A call 1.45%, reference 1.28%; A/A change +0.02%; SMT busy 0.18%; CPU steal 0 ticks | 1.5130–1.5572 |
| technical.replace.n8.b256.single | oneshot | loss | none | spread: call 2.09%, A/A call 3.63%, reference 1.28%; A/A change -0.16%; SMT busy 0.18%; CPU steal 0 ticks | 8.7245–9.1132 |
| technical.unique.n1.b256.single | prepared | loss | none | spread: call 0.96%, A/A call 1.03%, reference 1.19%; A/A change +1.13%; SMT busy 0.17%; CPU steal 0 ticks | 1.7472–1.7880 |
| technical.unique.n1.b256.single | oneshot | loss | none | spread: call 0.95%, A/A call 0.52%, reference 1.19%; A/A change -0.21%; SMT busy 0.17%; CPU steal 0 ticks | 4.2398–4.3560 |
| technical.unique.n16.b256.single | prepared | win | none | spread: call 0.81%, A/A call 1.04%, reference 0.51%; A/A change +0.13%; SMT busy 0.20%; CPU steal 0 ticks | 0.5109–0.5183 |
| technical.unique.n16.b256.single | oneshot | loss | none | spread: call 0.43%, A/A call 0.56%, reference 0.51%; A/A change -0.11%; SMT busy 0.20%; CPU steal 0 ticks | 10.2682–10.4068 |
| technical.unique.n4.b256.single | prepared | close | none | spread: call 0.90%, A/A call 0.83%, reference 0.57%; A/A change -0.04%; SMT busy 0.20%; CPU steal 0 ticks | 1.0006–1.0147 |
| technical.unique.n4.b256.single | oneshot | loss | none | spread: call 0.72%, A/A call 0.84%, reference 0.57%; A/A change +0.22%; SMT busy 0.20%; CPU steal 0 ticks | 4.3622–4.4369 |
| technical.unique.n48.b256.single | prepared | win | none | spread: call 0.84%, A/A call 4.55%, reference 0.76%; A/A change +0.19%; SMT busy 0.00%; CPU steal 0 ticks | 0.2383–0.2429 |
| technical.unique.n48.b256.single | oneshot | loss | none | spread: call 0.82%, A/A call 1.31%, reference 0.76%; A/A change -0.26%; SMT busy 0.00%; CPU steal 0 ticks | 13.0427–13.2703 |
| technical.unique.n8.b256.single | prepared | win | none | spread: call 0.96%, A/A call 1.15%, reference 0.93%; A/A change -0.10%; SMT busy 0.59%; CPU steal 0 ticks | 0.8146–0.8253 |
| technical.unique.n8.b256.single | oneshot | loss | none | spread: call 2.16%, A/A call 1.37%, reference 0.93%; A/A change +0.19%; SMT busy 0.59%; CPU steal 0 ticks | 6.6866–6.9926 |

## Counter checks

137 of 195 method results passed every 0/N pair. These checks are independent of timing checks; flagged medians remain in COUNTERS with †.

## Opposite directions in time and counters

Only comparisons passing timing and both counter checks are listed. Lower time can coexist with more instructions. This table records that observation without attributing a cause.

| Input | Mode | Paired elapsed ratio | Cycles ratio | Instructions ratio |
|---|---|---:|---:|---:|
| technical.count.n48.b4096.single | oneshot | 0.885 | 0.898 | 2.041 |
| technical.count.n8.b256.single | prepared | 1.241 | 1.249 | 0.946 |
