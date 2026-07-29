"""Repository-relative paths used by public scripts."""

from pathlib import Path

REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = REPOSITORY_ROOT / "data"
FIGURE_DIR = REPOSITORY_ROOT / "figures" / "paper"
VALIDATION_DIR = REPOSITORY_ROOT / "validation"
CHECKSUM_FILE = REPOSITORY_ROOT / "checksums.sha256"
