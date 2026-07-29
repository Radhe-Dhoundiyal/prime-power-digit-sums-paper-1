import pytest

from src.compute_statistics import digit_sum, normalized_digit_sum_exact


@pytest.mark.parametrize(("value", "expected"), [(0, 0), (7, 7), (1729, 19), (101**4, 16)])
def test_digit_sum(value: int, expected: int) -> None:
    assert digit_sum(value) == expected


def test_normalized_hand_example() -> None:
    assert normalized_digit_sum_exact(1729) == 19 / 4
