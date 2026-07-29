import csv
import gzip
import re
from collections import Counter

from src.compute_statistics import OBSERVATION_FIELDS, PRIMES


def test_full_dataset_schema_and_coverage(repository_root) -> None:
    counts: Counter[int] = Counter()
    rows = 0
    with gzip.open(
        repository_root / "data" / "all_exact_observations.csv.gz",
        "rt",
        encoding="utf-8",
        newline="",
    ) as handle:
        reader = csv.DictReader(handle)
        assert tuple(reader.fieldnames or ()) == OBSERVATION_FIELDS
        for row in reader:
            counts[int(row["prime"])] += 1
            rows += 1
    assert rows == 400_000
    assert tuple(counts) == PRIMES
    assert all(counts[prime] == 8000 for prime in PRIMES)


def test_official_figures_exist(repository_root) -> None:
    figures = sorted((repository_root / "figures" / "paper").glob("figure*.png"))
    assert len(figures) == 4
    assert all(path.stat().st_size > 0 for path in figures)


def test_no_private_absolute_paths_in_public_text(repository_root) -> None:
    patterns = (
        re.compile(r"C:" + re.escape("\\") + r"Projects", re.IGNORECASE),
        re.compile(r"Paper-1-" + r"GitHub-Preparation", re.IGNORECASE),
        re.compile(r"C:" + re.escape("\\") + r"Users", re.IGNORECASE),
        re.compile(r"/content/" + r"drive", re.IGNORECASE),
    )
    suffixes = {".md", ".py", ".json", ".toml", ".cff", ".txt", ".csv"}
    failures: list[str] = []
    for path in repository_root.rglob("*"):
        if path.is_file() and (path.suffix.lower() in suffixes or path.name.startswith("LICENSE")):
            text = path.read_text(encoding="utf-8")
            if any(pattern.search(text) for pattern in patterns):
                failures.append(path.relative_to(repository_root).as_posix())
    assert not failures
