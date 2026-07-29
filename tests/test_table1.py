import csv

from src.validate_results import EXPECTED_TABLE_1, verify_table1


def test_table1_has_21_matching_rows(repository_root) -> None:
    result = verify_table1(repository_root / "data" / "table1_prefix_sample_std_exact.csv")
    assert result["pass"], result
    assert result["rows"] == 21


def test_public_expected_table_matches_constants(repository_root) -> None:
    with (repository_root / "validation" / "expected_table1.csv").open(
        encoding="utf-8", newline=""
    ) as handle:
        rows = list(csv.DictReader(handle))
    assert len(rows) == 21
    for row in rows:
        key = (int(row["prime"]), int(row["cutoff"]))
        assert f"{float(row['sample_prefix_standard_deviation_exact']):.6f}" == (
            f"{EXPECTED_TABLE_1[key]:.6f}"
        )
