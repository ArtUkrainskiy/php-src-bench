# Measurement data notes

The tables use measured byte lengths and descriptive case names. The raw case
identifier `boundary/31/early @ short-early` contains a 32-byte text needle;
its displayed name is **32-byte early match (text)**. The true 31-byte input has
the raw identifier `boundary/31/early-corrected @ early31`. Raw identifiers,
measurements and hashes are retained unchanged. The A/A controls use the same
32-byte input on both sides.

The suite's relative `require` path and heading comment are adjusted for this
report. [check.py](check.py) restores both before checking the recorded source
hash; executable code and inputs are unchanged. Display-only counter JSON replaces machine paths; the
[native archive](data/native.tar.gz) preserves the recorded metadata and logs.

[Excluded Intel timing attempts](data/excluded-intel.tar.gz) are retained for
inspection. Their failed A/A controls prevent using them as elapsed-time evidence.
The separate Intel counter tables are labelled diagnostic throughout the report.
