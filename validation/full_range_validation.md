# Full-Range Validation

- Prime set: **PASS** - exactly the first 50 primes, 2 through 229.
- Exponent coverage: **PASS** - 1 through 8000 for every prime.
- Observation count: **400,000** (expected 400,000).
- Digit-count equality: **PASS** - 0 mismatches.
- Minimum distance of n log10(p) to an integer: `4.0727098848947207e-07` at `p=7, n=510`.
- Computation runtime: **963.370784 seconds**.
- Table 1 six-decimal validation: **PASS**.
- Official figure numerical validation: **PASS**.

## Data-file row counts

| File | Rows | Expected | Status |
|---|---:|---:|---|
| `all_exact_observations.csv.gz` | 400,000 | 400,000 | PASS |
| `all_primes_cutoff_summary_exact.csv` | 350 | 350 | PASS |
| `selected_prefix_means_exact.csv` | 35 | 35 | PASS |
| `selected_prefix_sample_std_exact.csv` | 35 | 35 | PASS |
| `table1_prefix_sample_std_exact.csv` | 21 | 21 | PASS |

## Unresolved issues

- The manuscript publishes Table 1 only to six decimal places, so
  equality to a higher manuscript precision cannot be tested.
- Corrected figures are numerically equivalent but intentionally not
  byte-identical to the old notation-inconsistent PNGs.
- Final repository construction, licensing, citation metadata, and
  publication remain outside this pass.

**Overall: PASS.**
