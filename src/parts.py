"""Loads the parts spreadsheets from data/parts/ into pandas DataFrames."""

from pathlib import Path

import pandas as pd

PARTS_DIR = Path(__file__).resolve().parent.parent / "data" / "parts"
# Category name -> CSV file in data/parts/ (files from docyx/pc-part-dataset)
FILES = {
    "cpus": "cpu.csv",
    "motherboards": "motherboard.csv",
    "ram": "memory.csv",
    "gpus": "video-card.csv",
    "cases": "case.csv",
    "psus": "power-supply.csv",
    "coolers": "cpu-cooler.csv",
    "storage": "internal-hard-drive.csv",
}
CATEGORIES = list(FILES)


def load_parts() -> dict[str, pd.DataFrame]:
    """Return {category: DataFrame} for every CSV in data/parts/."""
    return {cat: pd.read_csv(PARTS_DIR / file) for cat, file in FILES.items()}


def all_part_names(parts: dict[str, pd.DataFrame]) -> set[str]:
    """Every part name across all categories (used by checker rule 7)."""
    names = set()
    for df in parts.values():
        names.update(df["name"].astype(str))
    return names
