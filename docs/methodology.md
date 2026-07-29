# Methodology

For each of the first 50 primes, powers are generated iteratively from
`power = 1` by repeated multiplication. Python integers provide arbitrary
precision. Each power is converted once to decimal text; this representation
supplies both its digit sum and authoritative digit count.

For every observation the code independently evaluates
`floor(n * log10(p)) + 1`. All 400,000 values agreed with decimal string
length. The exact normalized value is digit sum divided by string length.

Prefix means use the first $N$ exact normalized values. Prefix dispersion is
Python's `statistics.stdev`, which uses the required sample denominator
$N-1$. Each prime's full sequence is computed once and sliced at the seven
cutoffs.

The experiment is deterministic and uses no external data or randomness.
