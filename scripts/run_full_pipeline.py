#!/usr/bin/env python3
"""Recompute the experiment from integers and regenerate public artifacts."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.compute_statistics import MAX_EXPONENT, PRIMES, generate_experiment
from src.generate_paper_figures import generate_paper_figures


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", type=Path, default=ROOT / "recomputed")
    parser.add_argument("--max-exponent", type=int, default=MAX_EXPONENT)
    parser.add_argument("--prime-limit", type=int, default=len(PRIMES))
    parser.add_argument("--skip-figures", action="store_true")
    args = parser.parse_args()
    if not 1 <= args.prime_limit <= len(PRIMES):
        parser.error("--prime-limit must be between 1 and 50")
    if args.max_exponent < 2:
        parser.error("--max-exponent must be at least 2")

    data_dir = args.output_dir / "data"
    result = generate_experiment(
        data_dir,
        primes=PRIMES[: args.prime_limit],
        maximum_exponent=args.max_exponent,
    )
    figures_generated = False
    if (
        not args.skip_figures
        and args.prime_limit == len(PRIMES)
        and args.max_exponent == MAX_EXPONENT
    ):
        generate_paper_figures(data_dir, args.output_dir / "figures" / "paper")
        figures_generated = True
    result["figures_generated"] = figures_generated
    result["pass"] = result["digit_count_mismatch_count"] == 0
    print(json.dumps(result, indent=2))
    print("PASS" if result["pass"] else "FAIL")
    return 0 if result["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
