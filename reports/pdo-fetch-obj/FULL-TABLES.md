# Full tables: PDO::FETCH_OBJ report

Change in CPU cycles per call against master (negative = fewer cycles, faster), with the range over the 15 passes and the change in instructions on both compilers. Then the control: master against itself, on GCC 15.2, at the start and at the end of the series. Machine and method: [README](README.md#machine-and-method).

<!-- bench-table series.json --labels labels.txt --full -->
| call | master, CPU cycles per call (GCC 15.2) | GCC 15.2 | clang 21.1 | instructions |
|---|--:|--:|--:|--:|
| `query()` + `fetchAll(PDO::FETCH_OBJ)`, SQLite, 100 rows × 1 column | 59,800 | −7% (−10 … +7) | 0% (−7 … +2) ~ | −2% |
| same, 3 columns | 119,979 | −4% (−6 … −1) | −7% (−9 … −4) | −7% |
| same, 10 columns | 304,032 | −12% (−13 … −10) | −13% (−18 … −11) | −13% |
| same, 30 columns | 841,453 | −14% (−16 … −12) | −14% (−17 … −11) | −14% |
| same, MySQL 8.4, 10 columns | 199,072 | −16% (−18 … −13) | −19% (−22 … −18) | −18% |
| `query()` + `fetchAll(PDO::FETCH_OBJ \| PDO::FETCH_GROUP)`, SQLite, 100 rows × 10 columns | 321,583 | −11% (−12 … −9) | −11% (−12 … −9) | −11% |
| `query()` + `fetch(PDO::FETCH_OBJ)` in a loop, SQLite, 100 rows × 10 columns | 313,346 | −12% (−13 … −11) | −14% (−17 … −10) | −13% |
| control, code not touched: `fetchAll(PDO::FETCH_ASSOC)`, SQLite, 1 column | 49,580 | −3% (−4 … 0) | −2% (−4 … 0) | 0% |
| control, code not touched: same, 3 columns | 101,743 | −1% (−1 … +2) | +2% (0 … +4) | 0% |
| control, code not touched: same, 10 columns | 254,914 | 0% (−1 … +1) | 0% (−16 … +2) ~ | 0% |
| control, code not touched: same, 30 columns | 703,745 | 0% (−2 … +1) | 0% (−2 … +2) ~ | 0% |
| control, code not touched: same, MySQL 8.4, 10 columns | 157,031 | −1% (−3 … +4) ~ | +1% (−4 … +4) | 0% |
| control, code not touched: `fetchAll(PDO::FETCH_CLASS)`, SQLite, 10 columns | 292,877 | +1% (0 … +12) | −1% (−2 … +2) | 0% |
| control, code not touched: same, MySQL 8.4, 10 columns | 184,829 | +1% (−3 … +5) | 0% (−2 … +7) ~ | 0% |
| `execute()` + `fetchAll(PDO::FETCH_OBJ)` of a prepared statement, MySQL 8.4, native prepares, 10 columns | 178,149 | −16% (−18 … −15) | −19% (−22 … −15) | −20% |
| control, code not touched: same with `fetchAll(PDO::FETCH_ASSOC)` | 138,391 | 0% (−3 … +3) ~ | 0% (−2 … +5) ~ | 0% |

Control: master against itself.

| call | master, CPU cycles per call (GCC 15.2) | A/A start | A/A end |
|---|--:|--:|--:|
| `query()` + `fetchAll(PDO::FETCH_OBJ)`, SQLite, 100 rows × 1 column | 60,052 | 0% (−1 … +15) | 0% (−2 … +2) |
| same, 3 columns | 119,987 | 0% (−2 … +2) | 0% (−14 … +3) |
| same, 10 columns | 304,253 | 0% (−12 … +3) | 0% (−2 … +2) |
| same, 30 columns | 837,213 | 0% (−8 … +1) | +1% (−2 … +2) |
| same, MySQL 8.4, 10 columns | 196,408 | +1% (−2 … +3) | −1% (−2 … +3) |
| `query()` + `fetchAll(PDO::FETCH_OBJ \| PDO::FETCH_GROUP)`, SQLite, 100 rows × 10 columns | 319,995 | 0% (−2 … +4) | 0% (−2 … +9) |
| `query()` + `fetch(PDO::FETCH_OBJ)` in a loop, SQLite, 100 rows × 10 columns | 313,795 | 0% (−1 … +2) | +1% (−34 … +2) |
| control, code not touched: `fetchAll(PDO::FETCH_ASSOC)`, SQLite, 1 column | 49,362 | 0% (−3 … +3) | 0% (−3 … +3) |
| control, code not touched: same, 3 columns | 101,357 | 0% (−2 … +3) | 0% (−1 … +5) |
| control, code not touched: same, 10 columns | 254,037 | 0% (−2 … +2) | 0% (−5 … +2) |
| control, code not touched: same, 30 columns | 701,896 | 0% (−3 … +3) | 0% (−1 … +2) |
| control, code not touched: same, MySQL 8.4, 10 columns | 155,549 | +1% (−2 … +2) | 0% (−1 … +4) |
| control, code not touched: `fetchAll(PDO::FETCH_CLASS)`, SQLite, 10 columns | 293,233 | 0% (−1 … +2) | 0% (−2 … +3) |
| control, code not touched: same, MySQL 8.4, 10 columns | 184,859 | 0% (−2 … +4) | −1% (−13 … +3) |
| `execute()` + `fetchAll(PDO::FETCH_OBJ)` of a prepared statement, MySQL 8.4, native prepares, 10 columns | 177,389 | 0% (−2 … +2) | −1% (−2 … +2) |
| control, code not touched: same with `fetchAll(PDO::FETCH_ASSOC)` | 137,482 | 0% (−3 … +2) | −1% (−3 … +2) |

~: the change is not larger than the A/A control of the same row: not evidence of a difference.
<!-- /bench-table -->
