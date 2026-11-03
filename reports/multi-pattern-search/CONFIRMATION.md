# Order and noise controls

The primary time series is preserved unchanged. Additional runs select every row with an even method count, every candidate within 5% of the fastest existing alternative, and any method whose maximum/minimum sample exceeds 1.10. Selection is an OR of these rules, defined before the final data was inspected.

The original rotation/reversal sequence does not visit all positions for four methods, and its two-label A/A traversal keeps a fixed order. The additional harness reverses each pair and rotates the start between pairs. The only source change is that traversal. At 15 passes it is not an exactly complete positional cycle. Hardware-counter runs already use separate forward/reverse alternation and are not repeated here.

Runs occur at different times and processes, so differences cannot be attributed solely to ordering. Both results are retained. Close medians and ranking changes are not decisive wins. Main-table bold marks only a lower median; it does not establish significance. Strong summary claims require a margin on both compilers and must survive an available repeat.

## gcc15

| Task | Mode | Main reference | Main Δ | Repeat reference | Repeat Δ | Reading |
|---|---|---|---:|---|---:|---|
| [Flag a short EN comment: phrase inside the message](../../corpus/multi-pattern-product/suites/moderation.json) | worker | str_contains() loop | +1.65% | str_contains() loop | +1.96% | Close / ranking changes |
| [Flag a short RU comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | worker | preg_match() | -3.18% | preg_match() | -2.65% | Both lower |
| [Decide whether a request trace needs an alert: healthy trace](../../corpus/multi-pattern-product/suites/error-routing.json) | worker | preg_match() | -4.21% | preg_match() | -4.94% | Both lower |
| [Decide whether a request trace needs an alert: error in the first record](../../corpus/multi-pattern-product/suites/error-routing.json) | worker | preg_match() | +1.58% | preg_match() | +2.31% | Close / ranking changes |
| [Decide whether a request trace needs an alert: error in the last record](../../corpus/multi-pattern-product/suites/error-routing.json) | worker | preg_match() | +2.50% | preg_match() | +3.31% | Both higher |
| [Order confirmation email](../../corpus/multi-pattern-product/suites/order-emails.json) | request | strtr() | +399.53% | strtr() | +399.00% | Both higher |
| [Order confirmation in HTML and plain text](../../corpus/multi-pattern-product/suites/order-emails.json) | request | strtr() | +296.53% | strtr() | +297.37% | Both higher |
| [Expand fixed tenant labels in one shop notice](../../corpus/multi-pattern-product/suites/tenant-text.json) | request | strtr() | +510.62% | strtr() | +512.44% | Both higher |
| [Expand fixed tenant labels in one shop notice](../../corpus/multi-pattern-product/suites/tenant-text.json) | worker | str_replace() | +79.35% | str_replace() | +80.45% | Both higher |
| [Publish eight different shop pages using one tenant configuration](../../corpus/multi-pattern-product/suites/tenant-text.json) | request | strtr() | +151.44% | strtr() | +155.47% | Both higher |
| [Publish eight different shop pages using one tenant configuration](../../corpus/multi-pattern-product/suites/tenant-text.json) | worker | str_replace() | +113.20% | str_replace() | +105.96% | Both higher |
| [Leave ordinary ASCII customer text unchanged](../../corpus/multi-pattern-product/suites/text-cleanup.json) | request | strtr() | +671.94% | strtr() | +683.61% | Both higher |
| [Leave ordinary ASCII customer text unchanged](../../corpus/multi-pattern-product/suites/text-cleanup.json) | worker | preg_replace_callback() | +52.27% | preg_replace_callback() | +52.27% | Both higher |
| [Normalize quotes, dashes and spaces in imported customer text](../../corpus/multi-pattern-product/suites/text-cleanup.json) | request | strtr() | +474.25% | strtr() | +481.23% | Both higher |
| [Normalize quotes, dashes and spaces in imported customer text](../../corpus/multi-pattern-product/suites/text-cleanup.json) | worker | strtr() | +42.36% | strtr() | +41.54% | Both higher |
| [Check already-migrated content for old literal links](../../corpus/multi-pattern-product/suites/link-migration.json) | request | strtr() | +2165.50% | strtr() | +2190.05% | Both higher |
| [Check already-migrated content for old literal links](../../corpus/multi-pattern-product/suites/link-migration.json) | worker | preg_replace_callback() | +53.12% | preg_replace_callback() | +51.95% | Both higher |
| [Rewrite known legacy links in one content page](../../corpus/multi-pattern-product/suites/link-migration.json) | request | strtr() | +1781.92% | strtr() | +1789.95% | Both higher |
| [Rewrite known legacy links in one content page](../../corpus/multi-pattern-product/suites/link-migration.json) | worker | str_replace() | +26.76% | str_replace() | +26.98% | Both higher |
| [Migrate eight different content pages with the same URL rules](../../corpus/multi-pattern-product/suites/link-migration.json) | request | strtr() | +290.76% | strtr() | +280.11% | Both higher |
| [Migrate eight different content pages with the same URL rules](../../corpus/multi-pattern-product/suites/link-migration.json) | worker | str_replace() | +34.97% | str_replace() | +32.83% | Both higher |
| [Check plain support replies for configured emoticons](../../corpus/multi-pattern-product/suites/chat-formatting.json) | request | strtr() | +660.83% | strtr() | +672.51% | Both higher |
| [Check plain support replies for configured emoticons](../../corpus/multi-pattern-product/suites/chat-formatting.json) | worker | preg_replace_callback() | +15.37% | preg_replace_callback() | +15.03% | Both higher |
| [Render configured emoticons in short customer replies](../../corpus/multi-pattern-product/suites/chat-formatting.json) | request | strtr() | +560.90% | strtr() | +565.22% | Both higher |
| [Render configured emoticons in short customer replies](../../corpus/multi-pattern-product/suites/chat-formatting.json) | worker | strtr() | +17.34% | strtr() | +16.83% | Both higher |
| [Synthetic control: 64 literals sharing a long prefix](../../corpus/multi-pattern-product/suites/synthetic.json) | request | strtr() | +22701.25% | strtr() | +23558.81% | Both higher |
| [Synthetic control: 64 literals sharing a long prefix](../../corpus/multi-pattern-product/suites/synthetic.json) | worker | strtr() | +18.44% | strtr() | +18.73% | Both higher |
| [Synthetic control: 64 literals sharing a long suffix](../../corpus/multi-pattern-product/suites/synthetic.json) | request | strtr() | +5491.74% | strtr() | +5326.68% | Both higher |
| [Synthetic control: 64 literals sharing a long suffix](../../corpus/multi-pattern-product/suites/synthetic.json) | worker | strtr() | +45.64% | strtr() | +44.31% | Both higher |
| [Synthetic control: nested repeated-byte literals](../../corpus/multi-pattern-product/suites/synthetic.json) | request | strtr() | +340.10% | strtr() | +339.39% | Both higher |
| [Synthetic control: nested repeated-byte literals](../../corpus/multi-pattern-product/suites/synthetic.json) | worker | strtr() | +51.95% | strtr() | +50.88% | Both higher |
| [Check a short comment](../../corpus/multi-pattern-scaling/suites/moderation.json) | worker | str_contains() loop | +1.57% | str_contains() loop | +1.69% | Close / ranking changes |
| [Check a detailed support message](../../corpus/multi-pattern-scaling/suites/moderation.json) | worker | str_contains() loop | -4.20% | str_contains() loop | -3.38% | Both lower |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | request | preg_replace_callback() | -1.06% | preg_replace_callback() | -2.91% | Close / ranking changes |

Paired-reversal A/A:

| Stage | Time Δ |
|---|---:|
| before | +0.027% |
| after | +0.070% |

## clang21

| Task | Mode | Main reference | Main Δ | Repeat reference | Repeat Δ | Reading |
|---|---|---|---:|---|---:|---|
| [Flag a short EN comment: no configured phrase](../../corpus/multi-pattern-product/suites/moderation.json) | worker | preg_match() | -3.55% | preg_match() | -2.72% | Both lower |
| [Flag a short EN comment: phrase inside the message](../../corpus/multi-pattern-product/suites/moderation.json) | worker | preg_match() | +4.88% | preg_match() | +5.02% | Both higher |
| [Flag a short RU comment: phrase at the start](../../corpus/multi-pattern-product/suites/moderation.json) | worker | preg_match() | +4.31% | preg_match() | +3.39% | Both higher |
| [Order confirmation email](../../corpus/multi-pattern-product/suites/order-emails.json) | request | strtr() | +393.19% | strtr() | +391.87% | Both higher |
| [Order confirmation in HTML and plain text](../../corpus/multi-pattern-product/suites/order-emails.json) | request | strtr() | +286.54% | strtr() | +291.77% | Both higher |
| [Expand fixed tenant labels in one shop notice](../../corpus/multi-pattern-product/suites/tenant-text.json) | request | strtr() | +526.90% | strtr() | +547.16% | Both higher |
| [Expand fixed tenant labels in one shop notice](../../corpus/multi-pattern-product/suites/tenant-text.json) | worker | str_replace() | +48.21% | str_replace() | +52.17% | Both higher |
| [Publish eight different shop pages using one tenant configuration](../../corpus/multi-pattern-product/suites/tenant-text.json) | request | strtr() | +134.45% | strtr() | +140.45% | Both higher |
| [Publish eight different shop pages using one tenant configuration](../../corpus/multi-pattern-product/suites/tenant-text.json) | worker | str_replace() | +73.94% | str_replace() | +72.66% | Both higher |
| [Leave ordinary ASCII customer text unchanged](../../corpus/multi-pattern-product/suites/text-cleanup.json) | request | strtr() | +759.70% | strtr() | +748.10% | Both higher |
| [Leave ordinary ASCII customer text unchanged](../../corpus/multi-pattern-product/suites/text-cleanup.json) | worker | preg_replace_callback() | +7.52% | preg_replace_callback() | +6.68% | Both higher |
| [Normalize quotes, dashes and spaces in imported customer text](../../corpus/multi-pattern-product/suites/text-cleanup.json) | request | strtr() | +505.65% | strtr() | +491.89% | Both higher |
| [Normalize quotes, dashes and spaces in imported customer text](../../corpus/multi-pattern-product/suites/text-cleanup.json) | worker | strtr() | +13.25% | strtr() | +11.23% | Both higher |
| [Replace four special space characters with ordinary spaces](../../corpus/multi-pattern-product/suites/text-cleanup.json) | worker | strtr() | +0.03% | strtr() | -0.16% | Close / ranking changes |
| [Check already-migrated content for old literal links](../../corpus/multi-pattern-product/suites/link-migration.json) | request | strtr() | +2259.52% | strtr() | +2256.54% | Both higher |
| [Check already-migrated content for old literal links](../../corpus/multi-pattern-product/suites/link-migration.json) | worker | preg_replace_callback() | +33.61% | preg_replace_callback() | +31.12% | Both higher |
| [Rewrite known legacy links in one content page](../../corpus/multi-pattern-product/suites/link-migration.json) | request | strtr() | +1787.47% | strtr() | +1778.01% | Both higher |
| [Rewrite known legacy links in one content page](../../corpus/multi-pattern-product/suites/link-migration.json) | worker | str_replace() | +9.26% | str_replace() | +11.09% | Both higher |
| [Migrate eight different content pages with the same URL rules](../../corpus/multi-pattern-product/suites/link-migration.json) | request | strtr() | +273.19% | strtr() | +269.33% | Both higher |
| [Migrate eight different content pages with the same URL rules](../../corpus/multi-pattern-product/suites/link-migration.json) | worker | str_replace() | +17.78% | str_replace() | +17.53% | Both higher |
| [Check plain support replies for configured emoticons](../../corpus/multi-pattern-product/suites/chat-formatting.json) | request | strtr() | +784.11% | strtr() | +780.79% | Both higher |
| [Check plain support replies for configured emoticons](../../corpus/multi-pattern-product/suites/chat-formatting.json) | worker | strtr() | -6.94% | strtr() | -7.92% | Both lower |
| [Render configured emoticons in short customer replies](../../corpus/multi-pattern-product/suites/chat-formatting.json) | request | strtr() | +639.95% | strtr() | +644.11% | Both higher |
| [Render configured emoticons in short customer replies](../../corpus/multi-pattern-product/suites/chat-formatting.json) | worker | strtr() | +6.50% | strtr() | +2.29% | Both higher |
| [Synthetic control: 64 literals sharing a long prefix](../../corpus/multi-pattern-product/suites/synthetic.json) | request | strtr() | +22066.60% | strtr() | +21991.84% | Both higher |
| [Synthetic control: 64 literals sharing a long prefix](../../corpus/multi-pattern-product/suites/synthetic.json) | worker | strtr() | +9.23% | strtr() | +8.52% | Both higher |
| [Synthetic control: 64 literals sharing a long suffix](../../corpus/multi-pattern-product/suites/synthetic.json) | request | strtr() | +5302.15% | strtr() | +5440.31% | Both higher |
| [Synthetic control: 64 literals sharing a long suffix](../../corpus/multi-pattern-product/suites/synthetic.json) | worker | strtr() | +35.74% | strtr() | +37.09% | Both higher |
| [Synthetic control: nested repeated-byte literals](../../corpus/multi-pattern-product/suites/synthetic.json) | request | strtr() | +381.10% | strtr() | +376.46% | Both higher |
| [Synthetic control: nested repeated-byte literals](../../corpus/multi-pattern-product/suites/synthetic.json) | worker | strtr() | +77.42% | strtr() | +73.67% | Both higher |
| [Add support links to a help article](../../corpus/multi-pattern-scaling/suites/replacement.json) | request | preg_replace_callback() | -3.25% | preg_replace_callback() | -3.91% | Both lower |
| [Flag a short EN comment: no configured phrase](../../corpus/multi-pattern-scaling/suites/controls.json) | worker | preg_match() | -3.71% | preg_match() | -2.24% | Both lower |

Paired-reversal A/A:

| Stage | Time Δ |
|---|---:|
| before | -0.304% |
| after | -0.121% |

Complete original/repeat samples and selection reasons: [GCC](data/order-gcc15.json), [Clang](data/order-clang21.json). Compiler, inputs, binary hashes and JIT settings match the main series. Supplemental calls explicitly set memory_limit=1G; main calls use the -n default. This A/A compares identical code in a single build, not independently linked PHP binaries.
