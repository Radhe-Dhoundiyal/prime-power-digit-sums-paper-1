# Data Dictionary

## `all_exact_observations.csv.gz`

This gzip-compressed CSV contains 400,000 data rows: 50 primes and 8000
exponents per prime.

| Column | Meaning |
|---|---|
| `prime` | Prime base $p$, one of the first 50 primes from 2 through 229 |
| `exponent` | Exponent $n$, from 1 through 8000 |
| `digit_sum` | Decimal digit sum $S(p^n)$ |
| `digit_count` | Authoritative exact count `len(str(p**n))` |
| `formula_digit_count` | Independent `floor(n * log10(p)) + 1` check |
| `normalized_digit_sum_exact` | `digit_sum / digit_count` |

Generation is deterministic and uses no randomness. The two digit-count
columns agreed for every tested row.

## Derived CSV files

- `all_primes_cutoff_summary_exact.csv`: exact prefix mean and sample prefix
  standard deviation for every prime and official cutoff.
- `selected_prefix_means_exact.csv`: Figure 3 values.
- `selected_prefix_sample_std_exact.csv`: Figure 4 values.
- `table1_prefix_sample_std_exact.csv`: the 21 Table 1 values at full computed
  precision.

All standard deviations use denominator $N-1$.
