import pytest

from src.compute_statistics import exact_digit_count, formula_digit_count, iterative_powers


@pytest.mark.parametrize(("prime", "exponent"), [(2, 1), (2, 100), (7, 510), (101, 8), (229, 50)])
def test_formula_and_string_digit_counts_agree(prime: int, exponent: int) -> None:
    power = prime**exponent
    assert exact_digit_count(power) == len(str(power))
    assert formula_digit_count(prime, exponent) == exact_digit_count(power)


def test_iterative_powers() -> None:
    assert list(iterative_powers(3, 4)) == [(1, 3), (2, 9), (3, 27), (4, 81)]
