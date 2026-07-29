"""Authoritative exact computation for the Paper 1 experiment.

Decimal string length is the implementation authority for digit count.
``floor(n * log10(p)) + 1`` is computed independently as a validation check.
"""

from __future__ import annotations

import csv
import gzip
import json
import math
import platform
import statistics
import sys
import time
from datetime import datetime, timezone
from importlib.metadata import PackageNotFoundError, version
from pathlib import Path
from typing import Final, Iterable, Sequence

PAPER_TITLE: Final = "A Computational Study of Digit-Sum Statistics of Prime Powers"
AUTHOR: Final = "Radhe Dhoundiyal"
PRIMES: Final[tuple[int, ...]] = (
    2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
    31, 37, 41, 43, 47, 53, 59, 61, 67, 71,
    73, 79, 83, 89, 97, 101, 103, 107, 109, 113,
    127, 131, 137, 139, 149, 151, 157, 163, 167, 173,
    179, 181, 191, 193, 197, 199, 211, 223, 227, 229,
)
MAX_EXPONENT: Final = 8000
CUTOFFS: Final[tuple[int, ...]] = (50, 250, 500, 1000, 2000, 4000, 8000)
FIGURE_1_2_PRIMES: Final = (2, 3, 5, 7, 11)
FIGURE_3_4_PRIMES: Final = (2, 5, 11, 101, 197)
TABLE_1_PRIMES: Final = (2, 101, 197)
OBSERVATION_FIELDS: Final = (
    "prime",
    "exponent",
    "digit_sum",
    "digit_count",
    "formula_digit_count",
    "normalized_digit_sum_exact",
)


def digit_sum(value: int | str) -> int:
    """Return the decimal digit sum of a nonnegative integer."""

    text = str(value)
    if text.startswith("-") or not text.isdigit():
        raise ValueError("digit_sum expects a nonnegative integer")
    return sum(ord(character) - 48 for character in text)


def iterative_powers(prime: int, maximum_exponent: int) -> Iterable[tuple[int, int]]:
    """Yield ``(n, prime**n)`` using iterative arbitrary-precision multiplication."""

    power = 1
    for exponent in range(1, maximum_exponent + 1):
        power *= prime
        yield exponent, power


def exact_digit_count(power: int) -> int:
    """Return the authoritative decimal digit count."""

    return len(str(power))


def formula_digit_count(prime: int, exponent: int) -> int:
    """Return the manuscript logarithmic digit-count expression."""

    return math.floor(exponent * math.log10(prime)) + 1


def normalized_digit_sum_exact(power: int) -> float:
    """Return S(power) divided by its authoritative decimal string length."""

    decimal_power = str(power)
    return digit_sum(decimal_power) / len(decimal_power)


def running_means(values: Sequence[float]) -> list[float]:
    """Return arithmetic means of all consecutive prefixes."""

    result: list[float] = []
    total = 0.0
    for index, value in enumerate(values, start=1):
        total += value
        result.append(total / index)
    return result


def sample_prefix_standard_deviation(values: Sequence[float], cutoff: int) -> float:
    """Return sample SD of ``values[:cutoff]`` using denominator N-1."""

    return statistics.stdev(values[:cutoff])


def write_csv(path: Path, fields: Sequence[str], rows: Iterable[dict[str, object]]) -> None:
    """Write a deterministic UTF-8 CSV."""

    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def _package_version(name: str) -> str:
    try:
        return version(name)
    except PackageNotFoundError:
        return "not installed"


def generate_experiment(
    output_dir: Path,
    *,
    primes: Sequence[int] = PRIMES,
    maximum_exponent: int = MAX_EXPONENT,
) -> dict[str, object]:
    """Generate exact observations and derived summaries in ``output_dir``.

    Default arguments reproduce the declared 400,000-observation experiment.
    Reduced arguments are supported for smoke testing and write only cutoffs not
    exceeding ``maximum_exponent``.
    """

    sys.set_int_max_str_digits(1_000_000)
    output_dir.mkdir(parents=True, exist_ok=True)
    active_cutoffs = tuple(cutoff for cutoff in CUTOFFS if cutoff <= maximum_exponent)
    if maximum_exponent >= 2 and not active_cutoffs:
        active_cutoffs = (maximum_exponent,)
    started = datetime.now(timezone.utc)
    start_clock = time.perf_counter()
    observation_count = 0
    mismatches: list[dict[str, int]] = []
    minimum_distance = 1.0
    minimum_pair: tuple[int, int] | None = None
    values_by_prime: dict[int, list[float]] = {}
    summary_rows: list[dict[str, object]] = []

    with gzip.open(
        output_dir / "all_exact_observations.csv.gz",
        "wt",
        encoding="utf-8",
        newline="",
        compresslevel=9,
    ) as handle:
        writer = csv.writer(handle, lineterminator="\n")
        writer.writerow(OBSERVATION_FIELDS)
        for prime in primes:
            exact_values: list[float] = []
            log_prime = math.log10(prime)
            for exponent, power in iterative_powers(prime, maximum_exponent):
                decimal_power = str(power)
                count = len(decimal_power)
                sum_of_digits = digit_sum(decimal_power)
                formula_count = math.floor(exponent * log_prime) + 1
                distance = abs(exponent * log_prime - round(exponent * log_prime))
                if distance < minimum_distance:
                    minimum_distance = distance
                    minimum_pair = (prime, exponent)
                if count != formula_count:
                    mismatches.append(
                        {
                            "prime": prime,
                            "exponent": exponent,
                            "digit_count": count,
                            "formula_digit_count": formula_count,
                        }
                    )
                normalized = sum_of_digits / count
                exact_values.append(normalized)
                writer.writerow(
                    (
                        prime,
                        exponent,
                        sum_of_digits,
                        count,
                        formula_count,
                        format(normalized, ".17g"),
                    )
                )
                observation_count += 1
            values_by_prime[prime] = exact_values
            for cutoff in active_cutoffs:
                prefix = exact_values[:cutoff]
                summary_rows.append(
                    {
                        "prime": prime,
                        "cutoff": cutoff,
                        "prefix_mean_exact": format(statistics.mean(prefix), ".17g"),
                        "sample_prefix_standard_deviation_exact": format(
                            statistics.stdev(prefix), ".17g"
                        ),
                    }
                )

    write_csv(
        output_dir / "all_primes_cutoff_summary_exact.csv",
        (
            "prime",
            "cutoff",
            "prefix_mean_exact",
            "sample_prefix_standard_deviation_exact",
        ),
        summary_rows,
    )
    selected = [row for row in summary_rows if row["prime"] in FIGURE_3_4_PRIMES]
    write_csv(
        output_dir / "selected_prefix_means_exact.csv",
        ("prime", "cutoff", "prefix_mean_exact"),
        (
            {
                "prime": row["prime"],
                "cutoff": row["cutoff"],
                "prefix_mean_exact": row["prefix_mean_exact"],
            }
            for row in selected
        ),
    )
    write_csv(
        output_dir / "selected_prefix_sample_std_exact.csv",
        ("prime", "cutoff", "sample_prefix_standard_deviation_exact"),
        (
            {
                "prime": row["prime"],
                "cutoff": row["cutoff"],
                "sample_prefix_standard_deviation_exact": row[
                    "sample_prefix_standard_deviation_exact"
                ],
            }
            for row in selected
        ),
    )
    write_csv(
        output_dir / "table1_prefix_sample_std_exact.csv",
        ("prime", "cutoff", "sample_prefix_standard_deviation_exact"),
        (
            {
                "prime": row["prime"],
                "cutoff": row["cutoff"],
                "sample_prefix_standard_deviation_exact": row[
                    "sample_prefix_standard_deviation_exact"
                ],
            }
            for row in selected
            if row["prime"] in TABLE_1_PRIMES
        ),
    )

    parameters = {
        "paper_title": PAPER_TITLE,
        "author": AUTHOR,
        "primes": list(primes),
        "maximum_exponent": maximum_exponent,
        "cutoffs": list(active_cutoffs),
        "normalization_definitions": {
            "exact_mathematical": "S(p^n) / (floor(n log10(p)) + 1)",
            "exact_implementation": "S(p^n) / len(str(p^n))",
            "approximate_supplementary": "S(p^n) / (n log10(p))",
        },
        "standard_deviation_convention": "sample standard deviation with denominator N - 1",
        "generation_timestamp_utc": started.isoformat(),
        "python_version": sys.version,
        "platform": platform.platform(),
        "package_versions": {"matplotlib": _package_version("matplotlib")},
    }
    (output_dir / "experiment_parameters.json").write_text(
        json.dumps(parameters, indent=2) + "\n", encoding="utf-8"
    )
    return {
        "observation_count": observation_count,
        "digit_count_mismatch_count": len(mismatches),
        "digit_count_mismatches": mismatches,
        "minimum_distance_to_nearest_integer": minimum_distance,
        "minimum_distance_pair": minimum_pair,
        "runtime_seconds": time.perf_counter() - start_clock,
        "prime_count": len(primes),
        "maximum_exponent": maximum_exponent,
    }
