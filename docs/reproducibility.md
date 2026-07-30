# Reproducing the Results

## Quick workflow

The included compressed dataset supports fast verification without repeating
the approximately 16-minute integer computation:

```text
python scripts/verify_repository.py
python scripts/reproduce_table1.py
python scripts/reproduce_figures.py --output-dir reproduced_figures
```

## Full workflow

```text
python scripts/run_full_pipeline.py --output-dir recomputed
```

The default recomputes all 400,000 powers, checks both digit-count methods,
exports all data products, regenerates Figures 1-4, and prints runtime and
PASS/FAIL status.

For a smaller test of the same workflow:

```text
python scripts/run_full_pipeline.py --output-dir smoke --prime-limit 2 --max-exponent 50 --skip-figures
```

Run commands from the repository root. No private preparation directory is
required.
