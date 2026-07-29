"""Reproducibility tools for Paper 1 prime-power digit-sum statistics."""

from .compute_statistics import (
    CUTOFFS,
    MAX_EXPONENT,
    PRIMES,
    digit_sum,
    exact_digit_count,
    formula_digit_count,
    normalized_digit_sum_exact,
)

__all__ = [
    "CUTOFFS",
    "MAX_EXPONENT",
    "PRIMES",
    "digit_sum",
    "exact_digit_count",
    "formula_digit_count",
    "normalized_digit_sum_exact",
]
