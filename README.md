# Prime-Power Digit-Sum Statistics — Paper 1 Reproducibility Package

## Overview

This repository contains the code and data used for the computational
experiments in my paper, *A Computational Study of Digit-Sum Statistics of
Prime Powers*. The calculations cover the first 50 primes, from 2 through 229,
and exponents up to 8000. The repository includes 400,000 observations and
reproduces Table 1 and Figures 1-4. It also includes the tests, validation
records, and a notebook showing the reproduction workflow.

This is an empirical study. The calculations support the discussion in the
paper, but they do not prove its conjectures.

## Main statistic

For decimal digit sum $S(x)$, the paper studies

$$
\widetilde A_p(n)=\frac{S(p^n)}{\lfloor n\log_{10}p\rfloor+1}.
$$

The final calculations use `len(str(power))` for the digit count and compare
it independently with `floor(n * log10(p)) + 1`. The older
$A_p(n)=S(p^n)/(n\log_{10}p)$ normalization is supplementary and is not used
for the results reported in the paper.

## Results reproduced

The repository reproduces:

- all 21 displayed values in Table 1;
- Figures 1-4 with the notation used in the paper;
- the full experiment covering 50 primes and 8000 exponents per prime.

These computations provide finite empirical evidence. They do not prove the
paper's conjectures.

## Repository contents

- `src/`: code used for the calculations, figures, and validation checks.
- `scripts/`: commands for verification and reproduction.
- `data/`: the complete compressed observations and derived summaries.
- `figures/paper/`: the four figures used for the paper.
- `notebooks/`: a notebook showing the reproduction workflow from start to finish.
- `validation/`: validation and cross-checking records.
- `docs/`: notes on the method, data, figures, normalization, and workflow.
- `tests/`: unit and output checks that do not repeat the full computation.

See `MANIFEST.md` for a repository file guide.

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

- Figure 1: $p=2,3,5,7,11$, $1\le n\le400$.
- Figure 2: $p=2,3,5,7,11$, $1\le N\le2000$.
- Figure 3: $p=2,5,11,101,197$ at
  $N=50,250,500,1000,2000,4000,8000$.
- Figure 4: the same five primes and cutoffs, using sample prefix standard
  deviation with denominator $N-1$.

Figures 1 and 2 use shorter ranges so that the plots remain readable. No
all-50-prime line plot is included.

## Validation summary

- 400,000 exact observations generated.
- Zero digit-count mismatches.
- 21/21 Table 1 values reproduced to six decimals.
- All four figures reproduced numerically.
- Minimum distance of $n\log_{10}(p)$ from an integer:
  $4.0727\times10^{-7}$ at $p=7,n=510$.

## Data availability

`data/all_exact_observations.csv.gz` contains the complete deterministic
dataset. Smaller CSV files provide all-prime cutoff summaries and exact values
used by Table 1 and Figures 3-4. No randomness or external data are involved.

## Citation

Use `CITATION.cff` for software citation metadata. The public repository is
[https://github.com/Radhe-Dhoundiyal/prime-power-digit-sums-paper-1](https://github.com/Radhe-Dhoundiyal/prime-power-digit-sums-paper-1),
and the release date is 2026-07-30.

## Archived release

Version 1.0.0 is archived on Zenodo:

- Version-specific DOI: [10.5281/zenodo.21702236](https://doi.org/10.5281/zenodo.21702236)
- DOI for all versions: [10.5281/zenodo.21702235](https://doi.org/10.5281/zenodo.21702235)

The version-specific DOI identifies the exact v1.0.0 archive. The all-versions
DOI resolves to the repository's continuing Zenodo record.

## Licensing

Source code is licensed under the MIT License (`LICENSE-CODE`). Data, figures,
documentation, and repository documentation are licensed under CC BY 4.0
(`LICENSE-DATA`) unless otherwise stated. See `LICENSE` for the scope overview.

## Associated manuscript

The manuscript is not included in this repository. An arXiv identifier will
be added after submission: TO-BE-ADDED-AFTER-ARXIV-SUBMISSION. The repository
supports the paper but is not a copy of the manuscript.

## Limitations

This is an empirical computational study. It provides no proof of the proposed
asymptotic behavior and makes no claim of normality, independence, mixing,
uniform digit frequencies, or equidistribution of digit blocks.

## Contact

Radhe Dhoundiyal

For questions, corrections, or reproducibility issues, please open a GitHub
issue.
