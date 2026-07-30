# Repository File Guide

## Repository information

- `README.md`: overview and reproduction instructions.
- `LICENSE`, `LICENSE-CODE`, `LICENSE-DATA`: licensing scope, MIT code license,
  and CC BY 4.0 data/documentation license.
- `CITATION.cff`, `codemeta.json`: citation and software metadata.
- `requirements.txt`, `pyproject.toml`: runtime and test environment metadata.
- `.gitignore`, `.gitattributes`: files excluded from Git and text-file settings.
- `CHANGELOG.md`, `CONTRIBUTING.md`: change history and contribution guidance.
- `MANIFEST.md`: this repository file guide.
- `checksums.sha256`: repository-relative file checksums.

## Source used for the final calculations

- `src/__init__.py`: exported functions.
- `src/paths.py`: repository-relative paths.
- `src/compute_statistics.py`: integer calculations and data exports.
- `src/generate_paper_figures.py`: official Figure 1-4 generator.
- `src/validate_results.py`: fast dataset, Table 1, figure, and checksum checks.

## Command-line scripts

- `scripts/verify_repository.py`: quick integrity and scientific verification.
- `scripts/reproduce_table1.py`: Table 1 reproduction from included data.
- `scripts/reproduce_figures.py`: Figure 1-4 reproduction from included data.
- `scripts/run_full_pipeline.py`: full or reduced from-scratch computation.

## Notebook

- `notebooks/paper1_reproducibility.ipynb`: clean included-data workflow with a
  disabled optional full-recomputation cell.

## Data

- `data/all_exact_observations.csv.gz`: all 400,000 exact observations.
- `data/all_primes_cutoff_summary_exact.csv`: 50-prime, seven-cutoff summary.
- `data/selected_prefix_means_exact.csv`: Figure 3 numerical values.
- `data/selected_prefix_sample_std_exact.csv`: Figure 4 numerical values.
- `data/table1_prefix_sample_std_exact.csv`: Table 1 numerical values.
- `data/experiment_parameters.json`: calculation parameters and environment
  record.

## Official figures

- `figures/paper/figure1_raw_values_exact.png`
- `figures/paper/figure2_running_mean_exact.png`
- `figures/paper/figure3_prefix_mean_cutoffs_exact.png`
- `figures/paper/figure4_prefix_std_exact.png`

## Validation records

- `validation/full_range_validation.md`
- `validation/table1_validation.md`
- `validation/figure_validation.md`
- `validation/manuscript_traceability.md`
- `validation/expected_table1.csv`
- `validation/scientific_checksums.sha256`: checksum evidence from the
  separate scientific validation pass; repository file integrity uses the root
  `checksums.sha256`.

## Documentation

- `docs/methodology.md`
- `docs/figure_guide.md`
- `docs/data_dictionary.md`
- `docs/reproducibility.md`
- `docs/normalization_notes.md`

## Tests

- `tests/conftest.py`
- `tests/test_digit_sum.py`
- `tests/test_digit_count.py`
- `tests/test_prime_list.py`
- `tests/test_statistics.py`
- `tests/test_table1.py`
- `tests/test_output_schema.py`

The associated manuscript, exploratory notebook, historical figures, and
private preparation files are deliberately excluded.
