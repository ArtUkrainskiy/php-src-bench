# Quality checks and flagged results

212 of 236 GCC 14 timing comparisons passed; 24 remain flagged.

Limits: A/A difference 2%; maximum sample deviation from its median 5%; SMT sibling busy time 2%; no CPU steal. With at most two attempts, the collector keeps the first passing attempt or flags the first if neither passes. All attempts are retained.

In summary tables, † marks a quality issue in the object or its shared reference. Observed times and relative changes are always retained. Spread is the largest absolute sample deviation from its median.

| Exact input | Mode | Flags | A/A change | Sample spread by implementation |
|---|---|---|---:|---|
| comment.41719.unique | oneshot | smt-load, spread:native | +0.07% | native: 44.01%, string_loop: 34.56%, preg_literal: 0.68%, preg_trie: 0.89%, folded_string_loop: 1.40%, native_aa: 0.96%; SMT busy 3.42%; CPU steal 0 ticks |
| comment.13918.unique | oneshot | spread:native_aa | +0.14% | native: 0.78%, string_loop: 4.79%, preg_literal: 1.32%, preg_trie: 0.80%, folded_string_loop: 4.08%, native_aa: 5.35%; SMT busy 0.92%; CPU steal 0 ticks |
| document.cookielib.all | prepared | smt-load | -0.19% | native: 4.11%, string_loop: 3.90%, preg_literal: 4.58%, preg_trie: 4.21%, native_aa: 2.07%; SMT busy 2.49%; CPU steal 0 ticks |
| document.cookielib.all | oneshot | spread:native | +0.10% | native: 8.80%, string_loop: 3.54%, preg_literal: 5.14%, preg_trie: 5.79%, native_aa: 4.80%; SMT busy 1.93%; CPU steal 0 ticks |
| document.configparser.replace | prepared | spread:native | -0.04% | native: 6.77%, strtr: 0.47%, preg_literal_callback: 0.87%, preg_trie_callback: 1.87%, str_replace: 0.68%, native_aa: 4.75%; SMT busy 0.47%; CPU steal 0 ticks |
| document.cookie.replace | prepared | spread:native, spread:native_aa | +0.21% | native: 7.59%, strtr: 6.03%, preg_literal_callback: 5.66%, preg_trie_callback: 4.56%, str_replace: 2.52%, native_aa: 7.90%; SMT busy 1.38%; CPU steal 0 ticks |
| document.stringio.unique | prepared | smt-load, spread:native, spread:native_aa | +0.42% | native: 45.49%, string_loop: 0.66%, preg_literal: 2.21%, preg_trie: 1.95%, native_aa: 23.95%; SMT busy 5.14%; CPU steal 0 ticks |
| document.stringio.unique | oneshot | smt-load, spread:native | +0.45% | native: 14.46%, string_loop: 0.67%, preg_literal: 1.54%, preg_trie: 1.59%, native_aa: 1.04%; SMT busy 3.29%; CPU steal 0 ticks |
| document.stringio.replace | prepared | spread:native | +0.00% | native: 6.57%, strtr: 4.18%, preg_literal_callback: 0.80%, preg_trie_callback: 2.96%, str_replace: 0.35%, native_aa: 2.92%; SMT busy 0.23%; CPU steal 0 ticks |
| document.thread.all | prepared | spread:native, spread:native_aa | +0.08% | native: 6.29%, string_loop: 0.67%, preg_literal: 1.86%, preg_trie: 2.62%, native_aa: 11.71%; SMT busy 0.55%; CPU steal 0 ticks |
| document.thread.replace | prepared | spread:native, spread:preg_trie_callback | +0.29% | native: 7.16%, strtr: 2.63%, preg_literal_callback: 1.53%, preg_trie_callback: 5.12%, native_aa: 1.82%; SMT busy 0.55%; CPU steal 0 ticks |
| document.thread.replace | oneshot | spread:preg_trie_callback | +0.06% | native: 3.19%, strtr: 2.07%, preg_literal_callback: 1.12%, preg_trie_callback: 6.87%, native_aa: 2.24%; SMT busy 0.82%; CPU steal 0 ticks |
| document.simplehttpserver.all | prepared | spread:native | +0.31% | native: 7.33%, string_loop: 3.15%, preg_literal: 10.04%, preg_trie: 8.52%, native_aa: 2.10%; SMT busy 1.66%; CPU steal 0 ticks |
| document.simplehttpserver.all | oneshot | smt-load, spread:native | -0.67% | native: 6.37%, string_loop: 2.56%, preg_literal: 10.21%, preg_trie: 7.46%, native_aa: 3.72%; SMT busy 2.47%; CPU steal 0 ticks |
| document.simplehttpserver.replace | oneshot | spread:native, spread:native_aa | +0.26% | native: 8.19%, strtr: 3.62%, preg_literal_callback: 1.85%, preg_trie_callback: 3.82%, str_replace: 0.34%, native_aa: 7.48%; SMT busy 0.69%; CPU steal 0 ticks |
| document.robotparser.count | oneshot | spread:native_aa | +0.72% | native: 1.92%, string_loop: 0.41%, preg_literal: 0.78%, preg_trie: 0.92%, native_aa: 16.02%; SMT busy 0.55%; CPU steal 0 ticks |
| document.robotparser.all | prepared | aa-outside-2-percent, spread:native | +2.26% | native: 5.07%, string_loop: 0.42%, preg_literal: 0.75%, preg_trie: 0.85%, native_aa: 4.90%; SMT busy 0.54%; CPU steal 0 ticks |
| email.usage-alert.txt | oneshot | spread:native_aa | -0.11% | native: 4.09%, strtr: 1.78%, preg_literal_callback: 9.00%, preg_trie_callback: 7.98%, str_replace: 1.84%, preg_tokens_callback: 11.10%, native_aa: 6.29%; SMT busy 1.98%; CPU steal 0 ticks |
| batch.validation.any.b4 | batch | smt-load, spread:native | +0.22% | native: 14.20%, string_loop: 41.55%, preg_literal: 2.34%, preg_trie: 1.92%, folded_string_loop: 1.39%, native_aa: 1.15%; SMT busy 2.95%; CPU steal 0 ticks |
| batch.validation.unique.b4 | batch | smt-load | +0.40% | native: 0.91%, string_loop: 1.10%, preg_literal: 0.98%, preg_trie: 1.41%, folded_string_loop: 2.94%, native_aa: 3.23%; SMT busy 3.42%; CPU steal 0 ticks |
| batch.references.all.b1 | batch | spread:native, spread:native_aa | +0.19% | native: 5.01%, string_loop: 2.30%, preg_literal: 5.54%, preg_trie: 4.58%, native_aa: 5.17%; SMT busy 0.83%; CPU steal 0 ticks |
| batch.references.unique.b16 | batch | smt-load | +0.34% | native: 0.85%, string_loop: 0.34%, preg_literal: 1.46%, preg_trie: 1.03%, native_aa: 0.73%; SMT busy 4.10%; CPU steal 0 ticks |
| batch.references.count.b16 | batch | smt-load | -0.04% | native: 0.64%, string_loop: 0.50%, preg_literal: 0.98%, preg_trie: 0.43%, native_aa: 1.09%; SMT busy 3.27%; CPU steal 0 ticks |
| batch.references.all.b16 | batch | smt-load, spread:native | +0.34% | native: 5.83%, string_loop: 0.44%, preg_literal: 0.79%, preg_trie: 0.74%, native_aa: 1.55%; SMT busy 3.95%; CPU steal 0 ticks |

## Counter checks: separate from timing checks

855 of 1096 method results passed all five 0/N pairs. 241 have a failed pair; 241 include SMT sibling load above 2%. One result means one implementation on one input in one mode.

Every pair requires positive corrected cycles and instructions, available events running at least 99% of the interval, and SMT sibling busy time at most 2%. All five pairs must pass. Flagged medians are shown with † without supporting comparative claims. No counter retries were made.

## Where elapsed time and instruction counts disagree

These rows passed timing and counter checks, but time differs by at least 2% in one direction and cycles or instructions by at least 2% in the other. The captures are independent; the table records the disagreement without attributing a cause. Ratios below 1 favor the native implementation.

| Input | Mode | Elapsed native/reference | Cycles native/reference | Instructions native/reference |
|---|---|---:|---:|---:|
| document.basehttpserver.unique | oneshot | 0.613 | 0.616 | 1.135 |
| document.queue.count | oneshot | 0.662 | 0.669 | 1.315 |
| document.queue.replace | oneshot | 1.247 | 1.262 | 0.955 |
| document.queue.unique | oneshot | 0.717 | 0.722 | 1.486 |
| document.simplehttpserver.unique | oneshot | 0.916 | 0.907 | 1.965 |
| document.simplexmlrpcserver.unique | oneshot | 0.597 | 0.598 | 1.112 |
| document.stringio.all | oneshot | 0.761 | 0.766 | 1.237 |
| document.thread.count | oneshot | 0.682 | 0.681 | 1.318 |
