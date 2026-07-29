# Contributing

Please open an issue before changing scientific parameters or numerical
definitions. Contributions must preserve the authoritative exact digit count
`len(str(power))`, the independent logarithmic comparison, the prime list,
cutoffs, sample standard-deviation convention, and official figure selections.

Run before submitting a change:

```text
python -m pytest
python scripts/verify_repository.py
```

Do not add the associated manuscript, private historical notebooks, credentials,
local paths, or unprovenanced figures. Code contributions use the MIT License;
documentation and contributed data use CC BY 4.0 unless explicitly agreed
otherwise.
