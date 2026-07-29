# Manuscript Traceability

| Manuscript item | Source function | Parameters | Data output | Figure output | Status |
|---|---|---|---|---|---|
| Experimental range | `compute_statistics.main` | 50 primes; n=1..8000 | `all_exact_observations.csv.gz`; `all_primes_cutoff_summary_exact.csv` | Not applicable | PASS |
| Table 1 | `sample_prefix_standard_deviation` / `statistics.stdev` | p=2,101,197; seven cutoffs; N-1 divisor | `table1_prefix_sample_std_exact.csv` | Not applicable | PASS at six decimals |
| Figure 1 | `generate_paper_figures.main` | p=2,3,5,7,11; n=1..400 | `all_exact_observations.csv.gz` | `figure1_raw_values_exact.png` | PASS |
| Figure 2 | `running_means` | p=2,3,5,7,11; N=1..2000 | `all_exact_observations.csv.gz` | `figure2_running_mean_exact.png` | PASS |
| Figure 3 | `statistics.mean` in `compute_statistics.main` | p=2,5,11,101,197; seven cutoffs | `selected_prefix_means_exact.csv` | `figure3_prefix_mean_cutoffs_exact.png` | PASS |
| Figure 4 | `sample_prefix_standard_deviation` / `statistics.stdev` | p=2,5,11,101,197; seven cutoffs; N-1 divisor | `selected_prefix_sample_std_exact.csv` | `figure4_prefix_std_exact.png` | PASS |

The exact implementation authority is `len(str(power))`. The mathematical
formula `floor(n*log10(p))+1` was independently checked for every observation.
