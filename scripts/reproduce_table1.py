#!/usr/bin/env python3
"""Recompute Table 1 from the included full observation dataset."""

from __future__ import annotations

import argparse
import csv
import gzip
import statistics
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.compute_statistics import CUTOFFS, TABLE_1_PRIMES
from src.validate_results import EXPECTED_TABLE_1


def reproduce(data_file: Path, output: Path | None = None) -> bool:
    values: dict[int, list[float]] = defaultdict(list)
    with gzip.open(data_file, "rt", encoding="utf-8", newline="") as handle:
        for row in csv.DictReader(handle):
            prime = int(row["prime"])
            if prime in TABLE_1_PRIMES:
                values[prime].append(float(row["normalized_digit_sum_exact"]))
    rows: list[tuple[int, int, float]] = []
    passed = True
    print("prime,cutoff,sample_prefix_standard_deviation_exact,status")
    for prime in TABLE_1_PRIMES:
        for cutoff in CUTOFFS:
            value = statistics.stdev(values[prime][:cutoff])
            status = "PASS" if f"{value:.6f}" == f"{EXPECTED_TABLE_1[(prime, cutoff)]:.6f}" else "FAIL"
            passed &= status == "PASS"
            rows.append((prime, cutoff, value))
            print(f"{prime},{cutoff},{value:.17g},{status}")
    if output:
        output.parent.mkdir(parents=True, exist_ok=True)
        with output.open("w", encoding="utf-8", newline="") as handle:
            writer = csv.writer(handle, lineterminator="\n")
            writer.writerow(("prime", "cutoff", "sample_prefix_standard_deviation_exact"))
            writer.writerows((prime, cutoff, format(value, ".17g")) for prime, cutoff, value in rows)
    print("PASS" if passed else "FAIL")
    return passed


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--data-file", type=Path, default=ROOT / "data" / "all_exact_observations.csv.gz")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    return 0 if reproduce(args.data_file, args.output) else 1


if __name__ == "__main__":
    raise SystemExit(main())
