"""Loads the parts spreadsheets from data/parts/ into pandas DataFrames."""

from pathlib import Path

import pandas as pd

PARTS_DIR = Path(__file__).resolve().parent.parent / "data" / "parts"
CATEGORIES = ["cpus", "motherboards", "ram", "gpus", "cases", "psus", "storage"]


def load_parts() -> dict[str, pd.DataFrame]:
    """Return {category: DataFrame} for every CSV in data/parts/."""
    return {cat: pd.read_csv(PARTS_DIR / f"{cat}.csv") for cat in CATEGORIES}


def all_part_names(parts: dict[str, pd.DataFrame]) -> set[str]:
    """Every part name across all categories (used by checker rule 7)."""
    names = set()
    for df in parts.values():
        names.update(df["name"].astype(str))
    return names
