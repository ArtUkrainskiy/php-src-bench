# Full tables: PDO::FETCH_OBJ report

Change in CPU cycles per call against master (negative = fewer cycles, faster), with the range over the 15 passes and the change in instructions on both compilers. Then the control: master against itself, on GCC 15.2, at the start and at the end of the series. Machine and method: [README](README.md#machine-and-method).

<!-- bench-table series.json --labels labels.txt --full -->
| call | master, CPU cycles per call (GCC 15.2) | GCC 15.2 | clang 21.1 | instructions |
|---|--:|--:|--:|--:|
| `query()` + `fetchAll(PDO::FETCH_OBJ)`, SQLite, 100 rows × 1 column | 58,096 | −4% (−7 … −2) | −8% (−9 … −6) | −3% |
| same, 3 columns | 117,352 | −6% (−10 … −3) | −6% (−8 … −3) | −8% |
| same, 10 columns | 296,345 | −12% (−13 … −2) | −15% (−16 … −12) | −14% |
| same, 30 columns | 819,889 | −12% (−13 … −11) | −17% (−19 … −14) | −15% |
| same, MySQL 8.4, 10 columns | 200,195 | −16% (−19 … −12) | −20% (−21 … −18) | −19% |
| `query()` + `fetchAll(PDO::FETCH_OBJ \| PDO::FETCH_GROUP)`, SQLite, 100 rows × 10 columns | 318,553 | −13% (−14 … −12) | −12% (−14 … −10) | −12% |
| `query()` + `fetch(PDO::FETCH_OBJ)` in a loop, SQLite, 100 rows × 10 columns | 303,828 | −12% (−13 … −11) | −16% (−19 … −15) | −14% |
| control, code not touched: `fetchAll(PDO::FETCH_ASSOC)`, SQLite, 1 column | 48,226 | 0% (−2 … +2) | −4% (−5 … −2) layout? | 0% … +1% |
| control, code not touched: same, 3 columns | 101,449 | 0% (−10 … +2) ~ | +2% (−1 … +3) | 0% |
| control, code not touched: same, 10 columns | 255,270 | +1% (−2 … +2) | −1% (−3 … +2) | 0% |
| control, code not touched: same, 30 columns | 709,250 | 0% (−2 … +2) ~ | 0% (−3 … +1) ~ | 0% |
| control, code not touched: same, MySQL 8.4, 10 columns | 157,703 | +1% (−2 … +4) ~ | 0% (−5 … +7) ~ | 0% |
| control, code not touched: `fetchAll(PDO::FETCH_CLASS)`, SQLite, 10 columns | 302,255 | −1% (−2 … 0) | 0% (−1 … +2) ~ | 0% |
| control, code not touched: same, MySQL 8.4, 10 columns | 186,744 | +1% (−2 … +4) ~ | +1% (−2 … +4) | −1% … 0% |
| `execute()` + `fetchAll(PDO::FETCH_OBJ)` of a prepared statement, MySQL 8.4, native prepares, 10 columns | 178,031 | −17% (−22 … −15) | −20% (−23 … −12) | −22% … −21% |
| control, code not touched: same with `fetchAll(PDO::FETCH_ASSOC)` | 138,597 | 0% (−2 … +3) ~ | 0% (−2 … +1) ~ | 0% |

Control: master against itself.

| call | master, CPU cycles per call (GCC 15.2) | A/A start | A/A end |
|---|--:|--:|--:|
| `query()` + `fetchAll(PDO::FETCH_OBJ)`, SQLite, 100 rows × 1 column | 58,252 | 0% (−2 … +1) | 0% (−2 … +2) |
| same, 3 columns | 116,778 | 0% (−7 … +2) | 0% (−2 … +4) |
| same, 10 columns | 296,769 | 0% (−1 … +2) | 0% (−3 … +2) |
| same, 30 columns | 820,990 | 0% (−1 … +1) | 0% (−3 … +5) |
| same, MySQL 8.4, 10 columns | 199,570 | 0% (−5 … +4) | +1% (−2 … +3) |
| `query()` + `fetchAll(PDO::FETCH_OBJ \| PDO::FETCH_GROUP)`, SQLite, 100 rows × 10 columns | 317,373 | 0% (−3 … +2) | 0% (−3 … +2) |
| `query()` + `fetch(PDO::FETCH_OBJ)` in a loop, SQLite, 100 rows × 10 columns | 303,316 | +1% (−1 … +2) | 0% (−13 … +1) |
| control, code not touched: `fetchAll(PDO::FETCH_ASSOC)`, SQLite, 1 column | 48,054 | 0% (−3 … +3) | 0% (−2 … +4) |
| control, code not touched: same, 3 columns | 101,035 | 0% (−2 … +1) | 0% (−2 … +2) |
| control, code not touched: same, 10 columns | 253,824 | 0% (−2 … +2) | 0% (−2 … +2) |
| control, code not touched: same, 30 columns | 712,796 | −1% (−2 … +3) | 0% (−2 … +2) |
| control, code not touched: same, MySQL 8.4, 10 columns | 158,601 | −1% (−5 … +1) | 0% (−3 … +2) |
| control, code not touched: `fetchAll(PDO::FETCH_CLASS)`, SQLite, 10 columns | 303,237 | 0% (−2 … +2) | 0% (−3 … +1) |
| control, code not touched: same, MySQL 8.4, 10 columns | 184,337 | 0% (−4 … +37) | +1% (−5 … +7) |
| `execute()` + `fetchAll(PDO::FETCH_OBJ)` of a prepared statement, MySQL 8.4, native prepares, 10 columns | 176,237 | 0% (−3 … +1) | 0% (−2 … +2) |
| control, code not touched: same with `fetchAll(PDO::FETCH_ASSOC)` | 137,105 | +1% (−4 … +6) | 0% (−20 … +13) |

~: within noise, the change is no larger than the difference between master and master on the same row.

layout?: in every pass the cycles changed in the same direction, by 3% or more in the median, the instructions by less than 0.5%: the work is the same, so look for the cause (code placement, branch prediction) with `bench why` before reporting the row.
<!-- /bench-table -->
