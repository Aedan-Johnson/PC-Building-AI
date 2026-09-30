"""Sanity checks on the parts spreadsheets. Runs now, catches data typos early."""

from src.parts import CATEGORIES, load_parts

VALID_RAM = {"DDR4", "DDR5"}


def test_all_files_load():
    parts = load_parts()
    assert set(parts) == set(CATEGORIES)


def test_names_unique_across_categories():
    parts = load_parts()
    names = [n for df in parts.values() for n in df["name"]]
    dupes = {n for n in names if names.count(n) > 1}
    assert not dupes, f"Duplicate part names: {dupes}"


def test_prices_positive():
    for cat, df in load_parts().items():
        assert (df["price"] > 0).all(), f"Bad price in {cat}"


def test_ram_types_valid():
    parts = load_parts()
    for cat in ("motherboards", "ram"):
        bad = set(parts[cat]["ram_type"]) - VALID_RAM
        assert not bad, f"Invalid ram_type in {cat}: {bad}"
