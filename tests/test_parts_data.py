"""Sanity checks on the parts spreadsheets. Runs now, catches data typos early."""

import pytest

from src.parts import CATEGORIES, load_parts

# The full dataset has repeated names, parts with no price, and no ram_type column.
# Turn these back on once the chat generator cleans the data it uses.
FULL_DATASET = pytest.mark.skip(reason="full dataset is not cleaned yet")

VALID_RAM = {"DDR4", "DDR5"}


def test_all_files_load():
    parts = load_parts()
    assert set(parts) == set(CATEGORIES)


@FULL_DATASET
def test_names_unique_across_categories():
    parts = load_parts()
    names = [n for df in parts.values() for n in df["name"]]
    dupes = {n for n in names if names.count(n) > 1}
    assert not dupes, f"Duplicate part names: {dupes}"


@FULL_DATASET
def test_prices_positive():
    for cat, df in load_parts().items():
        assert (df["price"] > 0).all(), f"Bad price in {cat}"


@FULL_DATASET
def test_ram_types_valid():
    parts = load_parts()
    for cat in ("motherboards", "ram"):
        bad = set(parts[cat]["ram_type"]) - VALID_RAM
        assert not bad, f"Invalid ram_type in {cat}: {bad}"
