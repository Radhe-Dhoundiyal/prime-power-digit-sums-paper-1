# Contributing

Corrections and reproducibility improvements are welcome. Please open an issue
before proposing changes to the numerical definitions, parameter ranges, or
figure selections.

Changes should preserve the digit-count definition `len(str(power))`, the
independent logarithmic comparison, the prime list, the cutoffs, and the sample
standard-deviation convention unless the reason for changing them is clearly
explained.

Run before submitting a change:

```text
python -m pytest
python scripts/verify_repository.py
```

Please explain any proposed change to included data or figures and run the tests
and quick verification before submitting it. Do not add the manuscript, private
notebooks, credentials, local paths, or figures without a clear source. Existing
license terms continue to apply.
