#!/usr/bin/env python3
"""Run fast scientific, schema, figure, and checksum verification."""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.validate_results import verify_repository


def main() -> int:
    result = verify_repository(ROOT)
    print(json.dumps(result, indent=2))
    print("PASS" if result["pass"] else "FAIL")
    return 0 if result["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
