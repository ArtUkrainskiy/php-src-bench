# Confirmation of one noisy elapsed-time row

One full-series sample set exceeded the 10% max/min spread check: Clang 21, a prepared dictionary of 512 moderation terms, with a match in the body of a short comment. The PCRE sample span was 10.22%. The complete case was remeasured with the same protocol, all methods and both lifecycles.

The original measurements remain in the main/full tables and raw data. No individual sample was removed. A dagger marks the original noisy PCRE cell. The confirmation does not change the winning method.

All times below are µs per complete comment; lower is better.

| Run | Loop | PCRE | Matcher | Largest sample max/min |
|---|---:|---:|---:|---:|
| Full series | 12.322 | 23.226 | 0.419 | 1.1022 |
| Confirmation | 12.526 | 22.903 | 0.418 | 1.0226 |

The confirmation A/A elapsed medians were within 0.03%. Its largest within-method sample span was 2.26% for the prepared row.

[Captured confirmation data](checks/confirmation-clang21.json). Both preparation-included and prepared-dictionary results are retained there.
