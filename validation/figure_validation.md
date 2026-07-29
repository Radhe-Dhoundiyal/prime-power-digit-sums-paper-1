# Figure Validation

The old PNGs were first verified byte-for-byte against their documented
embedded notebook outputs. Numerical comparison then reconstructed the old
formula-based exact statistic from the exported `digit_sum` and
`formula_digit_count` columns and compared it with the new string-length
authoritative statistic.

| Figure | Old source | New output | Parameters | Numerical values | Notation change | Status |
|---|---|---|---|---|---|---|
| 1 | Validated private notebook output (not included) | `figures/paper/figure1_raw_values_exact.png` | p=2,3,5,7,11; n=1..400 | Exact match | Formula title/general y-label changed to $\widetilde{A}_p(n)$ | PASS |
| 2 | Validated private notebook output (not included) | `figures/paper/figure2_running_mean_exact.png` | p=2,3,5,7,11; N=1..2000 | Exact match | $A_p(n)$ label corrected to $\widetilde{\mu}_p(N)$ | PASS |
| 3 | Validated private notebook output (not included) | `figures/paper/figure3_prefix_mean_cutoffs_exact.png` | p=2,5,11,101,197; seven cutoffs | Exact match | $A_p(n)$ label corrected to $\widetilde{\mu}_p(N)$ | PASS |
| 4 | Validated private notebook output (not included) | `figures/paper/figure4_prefix_std_exact.png` | p=2,5,11,101,197; seven cutoffs | Exact match | $A_p(n)$ label corrected to $\widetilde{\sigma}_p(N)$ | PASS |

Maximum difference between the new exact values and the old notebook's
formula-denominator values: `0`.

Other intentional visual changes: clearer manuscript-consistent titles,
math-text axes, `9/2` benchmark notation, tight layout, and regenerated
Matplotlib rendering. Old PNG provenance checks: `{'figure1': True, 'figure2': True, 'figure3': True, 'figure4': True}`.

**Overall: PASS.**
