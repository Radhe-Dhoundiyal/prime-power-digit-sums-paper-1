"""Fast integrity and scientific checks for the included public artifacts."""

from __future__ import annotations

import csv
import gzip
import hashlib
from collections import Counter
from pathlib import Path

from .compute_statistics import OBSERVATION_FIELDS, PRIMES

EXPECTED_TABLE_1 = {
    (2, 50): 1.133173, (101, 50): 1.070391, (197, 50): 0.467804,
    (2, 250): 0.629786, (101, 250): 0.577555, (197, 250): 0.260586,
    (2, 500): 0.480795, (101, 500): 0.420376, (197, 500): 0.197870,
    (2, 1000): 0.365714, (101, 1000): 0.304266, (197, 1000): 0.148158,
    (2, 2000): 0.275150, (101, 2000): 0.219562, (197, 2000): 0.110349,
    (2, 4000): 0.206469, (101, 4000): 0.157948, (197, 4000): 0.082032,
    (2, 8000): 0.154229, (101, 8000): 0.113429, (197, 8000): 0.060665,
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def verify_checksum_manifest(root: Path, manifest: Path) -> list[str]:
    """Return checksum-manifest failures."""

    failures: list[str] = []
    for line_number, line in enumerate(manifest.read_text(encoding="ascii").splitlines(), 1):
        try:
            expected, relative = line.split("  ", 1)
        except ValueError:
            failures.append(f"malformed checksum line {line_number}")
            continue
        target = root / relative
        if not target.is_file():
            failures.append(f"missing: {relative}")
        elif sha256(target) != expected:
            failures.append(f"checksum mismatch: {relative}")
    return failures


def verify_dataset(data_file: Path) -> dict[str, object]:
    """Validate schema, row counts, prime coverage, and digit-count equality."""

    counts: Counter[int] = Counter()
    mismatches = 0
    rows = 0
    with gzip.open(data_file, "rt", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        if tuple(reader.fieldnames or ()) != OBSERVATION_FIELDS:
            raise ValueError(f"Unexpected dataset schema: {reader.fieldnames}")
        for row in reader:
            prime = int(row["prime"])
            counts[prime] += 1
            rows += 1
            mismatches += int(row["digit_count"] != row["formula_digit_count"])
    coverage_ok = tuple(counts) == PRIMES and all(counts[prime] == 8000 for prime in PRIMES)
    return {
        "rows": rows,
        "prime_counts": dict(counts),
        "digit_count_mismatches": mismatches,
        "coverage_ok": coverage_ok,
        "pass": rows == 400_000 and coverage_ok and mismatches == 0,
    }


def verify_table1(table_file: Path) -> dict[str, object]:
    """Check all 21 Table 1 values at manuscript six-decimal precision."""

    failures: list[str] = []
    rows = 0
    with table_file.open("r", encoding="utf-8", newline="") as handle:
        for row in csv.DictReader(handle):
            rows += 1
            key = (int(row["prime"]), int(row["cutoff"]))
            actual = float(row["sample_prefix_standard_deviation_exact"])
            if key not in EXPECTED_TABLE_1 or f"{actual:.6f}" != f"{EXPECTED_TABLE_1[key]:.6f}":
                failures.append(f"{key}: {actual:.17g}")
    return {"rows": rows, "failures": failures, "pass": rows == 21 and not failures}


def verify_repository(root: Path, *, check_checksums: bool = True) -> dict[str, object]:
    """Run the fast public-repository verification suite."""

    dataset = verify_dataset(root / "data" / "all_exact_observations.csv.gz")
    table = verify_table1(root / "data" / "table1_prefix_sample_std_exact.csv")
    figures = sorted((root / "figures" / "paper").glob("figure*.png"))
    figures_ok = len(figures) == 4 and all(path.stat().st_size > 0 for path in figures)
    checksum_failures = (
        verify_checksum_manifest(root, root / "checksums.sha256") if check_checksums else []
    )
    return {
        "dataset": dataset,
        "table1": table,
        "figures_ok": figures_ok,
        "checksum_failures": checksum_failures,
        "pass": bool(dataset["pass"] and table["pass"] and figures_ok and not checksum_failures),
    }
