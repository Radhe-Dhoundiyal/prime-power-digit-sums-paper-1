"""Generate the four official exact-normalization figures from included data."""

from __future__ import annotations

import csv
import gzip
from collections import defaultdict
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

from .compute_statistics import CUTOFFS, FIGURE_1_2_PRIMES, FIGURE_3_4_PRIMES, running_means


def _load_values(data_file: Path) -> dict[int, list[float]]:
    values: dict[int, list[float]] = defaultdict(list)
    with gzip.open(data_file, "rt", encoding="utf-8", newline="") as handle:
        for row in csv.DictReader(handle):
            prime = int(row["prime"])
            exponent = int(row["exponent"])
            if prime in FIGURE_1_2_PRIMES and exponent <= 2000:
                values[prime].append(float(row["normalized_digit_sum_exact"]))
    return dict(values)


def _load_summary(summary_file: Path) -> dict[int, dict[int, tuple[float, float]]]:
    result: dict[int, dict[int, tuple[float, float]]] = defaultdict(dict)
    with summary_file.open("r", encoding="utf-8", newline="") as handle:
        for row in csv.DictReader(handle):
            prime = int(row["prime"])
            cutoff = int(row["cutoff"])
            if prime in FIGURE_3_4_PRIMES and cutoff in CUTOFFS:
                result[prime][cutoff] = (
                    float(row["prefix_mean_exact"]),
                    float(row["sample_prefix_standard_deviation_exact"]),
                )
    return dict(result)


def generate_paper_figures(data_dir: Path, output_dir: Path) -> list[Path]:
    """Generate Figures 1-4 with manuscript-consistent notation."""

    values = _load_values(data_dir / "all_exact_observations.csv.gz")
    summary = _load_summary(data_dir / "all_primes_cutoff_summary_exact.csv")
    if any(len(values.get(prime, [])) != 2000 for prime in FIGURE_1_2_PRIMES):
        raise ValueError("The dataset does not contain complete Figure 1/2 inputs.")
    if any(set(summary.get(prime, {})) != set(CUTOFFS) for prime in FIGURE_3_4_PRIMES):
        raise ValueError("The summary does not contain complete Figure 3/4 inputs.")
    output_dir.mkdir(parents=True, exist_ok=True)
    outputs: list[Path] = []

    def save(name: str) -> None:
        plt.grid(True)
        plt.legend()
        plt.tight_layout()
        path = output_dir / name
        plt.savefig(path, dpi=100)
        plt.close()
        outputs.append(path)

    plt.figure(figsize=(12, 6))
    for prime in FIGURE_1_2_PRIMES:
        plt.plot(range(1, 401), values[prime][:400], label=f"p = {prime}")
    plt.axhline(4.5, color="black", linestyle="--", label=r"$9/2$")
    plt.xlabel(r"$n$")
    plt.ylabel(r"$\widetilde{A}_p(n)$")
    plt.title(r"Exact normalized digit sum $\widetilde{A}_p(n)$")
    save("figure1_raw_values_exact.png")

    plt.figure(figsize=(12, 6))
    for prime in FIGURE_1_2_PRIMES:
        plt.plot(range(1, 2001), running_means(values[prime]), label=f"p = {prime}")
    plt.axhline(4.5, color="black", linestyle="--", label=r"$9/2$")
    plt.xlabel(r"$N$")
    plt.ylabel(r"$\widetilde{\mu}_p(N)$")
    plt.title(r"Exact prefix mean $\widetilde{\mu}_p(N)$")
    save("figure2_running_mean_exact.png")

    plt.figure(figsize=(10, 6))
    for prime in FIGURE_3_4_PRIMES:
        plt.plot(
            CUTOFFS,
            [summary[prime][cutoff][0] for cutoff in CUTOFFS],
            marker="o",
            label=f"p = {prime}",
        )
    plt.axhline(4.5, color="black", linestyle="--", label=r"$9/2$")
    plt.xlabel(r"$N$ (number of powers included)")
    plt.ylabel(r"$\widetilde{\mu}_p(N)$")
    plt.title(r"Exact prefix mean $\widetilde{\mu}_p(N)$ at selected cutoffs")
    save("figure3_prefix_mean_cutoffs_exact.png")

    plt.figure(figsize=(10, 6))
    for prime in FIGURE_3_4_PRIMES:
        plt.plot(
            CUTOFFS,
            [summary[prime][cutoff][1] for cutoff in CUTOFFS],
            marker="o",
            label=f"p = {prime}",
        )
    plt.xlabel(r"$N$ (number of powers included)")
    plt.ylabel(r"$\widetilde{\sigma}_p(N)$")
    plt.title(r"Exact sample prefix standard deviation $\widetilde{\sigma}_p(N)$")
    save("figure4_prefix_std_exact.png")
    return outputs
