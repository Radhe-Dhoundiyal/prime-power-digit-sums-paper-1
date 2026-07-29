import statistics

from src.compute_statistics import running_means, sample_prefix_standard_deviation


def test_running_means() -> None:
    assert running_means([2.0, 4.0, 9.0]) == [2.0, 3.0, 5.0]


def test_sample_standard_deviation_uses_n_minus_one() -> None:
    values = [1.0, 2.0, 3.0]
    assert sample_prefix_standard_deviation(values, 3) == statistics.stdev(values) == 1.0
