# Prime-Power Digit-Sum Statistics ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â Paper 1 Reproducibility Package

## Overview

This repository supports *A Computational Study of Digit-Sum Statistics of
Prime Powers* by Radhe Dhoundiyal. It contains the authoritative Python
implementation, 400,000 exact observations, derived tables, four official
figures, validation records, tests, and a clean educational notebook.

The empirical scope is the first 50 primes, from 2 through 229, and exponents
1 through 8000. The purpose is reproducibility, not proof of the paper's
conjectures.

## Main statistic

For decimal digit sum \(S(x)\), the paper studies

\[
\widetilde A_p(n)=\frac{S(p^n)}{\lfloor n\log_{10}p\rfloor+1}.
\]

The implementation uses `len(str(power))` as the authoritative exact digit
count and independently validates it against
`floor(n * log10(p)) + 1`. The older
\(A_p(n)=S(p^n)/(n\log_{10}p)\) normalization is supplementary and is not used
for the principal results in this package.

## Results reproduced

The package reproduces:

- all 21 displayed values in Table 1;
- Figures 1-4 with manuscript-consistent notation;
- the full 50-prime, 8000-exponent experiment.

These computations provide finite empirical evidence. They do not prove the
paper's conjectures.

## Repository contents

- `src/`: authoritative computation, plotting, paths, and validation functions.
- `scripts/`: quick verification and reproduction commands.
- `data/`: full compressed observations and derived exact summaries.
- `figures/paper/`: four corrected official figures.
- `notebooks/`: clean top-to-bottom reproducibility notebook.
- `validation/`: scientific validation and traceability records.
- `docs/`: methodology, data, figures, normalization, and workflow details.
- `tests/`: fast unit and artifact tests; no default full recomputation.

See `MANIFEST.md` for artifact-level details.

## Quick start

Python 3.11 or newer is required.

```text
python -m venv .venv
.venv\Scripts\python -m pip install -r requirements.txt
.venv\Scripts\python scripts/verify_repository.py
.venv\Scripts\python scripts/reproduce_table1.py
.venv\Scripts\python scripts/reproduce_figures.py --output-dir reproduced_figures
```

On macOS or Linux, replace `.venv\Scripts\python` with `.venv/bin/python`.

## Full recomputation

To regenerate the complete experiment from Python integers:

```text
python scripts/run_full_pipeline.py --output-dir recomputed
```

The validation run took approximately **963.371 seconds** using Python 3.12.3
and Matplotlib 3.8.4 on Windows 11. Runtime varies by hardware, operating
system, and Python build.

A reduced from-scratch smoke test is available:

```text
python scripts/run_full_pipeline.py --output-dir smoke --prime-limit 2 --max-exponent 50 --skip-figures
```

## Official figure ranges

- Figure 1: \(p=2,3,5,7,11\), \(1\le n\le400\).
- Figure 2: \(p=2,3,5,7,11\), \(1\le N\le2000\).
- Figure 3: \(p=2,5,11,101,197\) at
  \(N=50,250,500,1000,2000,4000,8000\).
- Figure 4: the same five primes and cutoffs, using sample prefix standard
  deviation with denominator \(N-1\).

Figures 1 and 2 deliberately use shorter ranges to remain interpretable. No
all-50-prime line plot is included.

## Validation summary

- 400,000 exact observations generated.
- Zero digit-count mismatches.
- 21/21 Table 1 values reproduced to six decimals.
- All four figures reproduced numerically.
- Minimum distance of \(n\log_{10}(p)\) from an integer:
  \(4.0727\times10^{-7}\) at \(p=7,n=510\).

## Data availability

`data/all_exact_observations.csv.gz` contains the complete deterministic
dataset. Smaller CSV files provide all-prime cutoff summaries and exact values
used by Table 1 and Figures 3-4. No randomness or external data are involved.

## Citation

Use `CITATION.cff` for software citation metadata. The repository URL and
release date will be added after GitHub publication. A DOI will be added after
Zenodo archiving.

## Licensing

Source code is licensed under the MIT License (`LICENSE-CODE`). Data, figures,
documentation, and repository documentation are licensed under CC BY 4.0
(`LICENSE-DATA`) unless otherwise stated. See `LICENSE` for the scope overview.

## Associated manuscript

The manuscript is intentionally not included. An arXiv identifier will be added after submission:
TO-BE-ADDED-AFTER-ARXIV-SUBMISSION. This repository supports the paper but is not itself
the manuscript.

## Limitations

This is an empirical computational study. It provides no proof of the proposed
asymptotic behavior and makes no claim of normality, independence, mixing,
uniform digit frequencies, or equidistribution of digit blocks.

## Contact

Radhe Dhoundiyal
