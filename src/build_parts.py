"""Builds the clean parts spreadsheets in data/parts/ from the raw dataset in data/raw/.

Raw data: docyx/pc-part-dataset (https://github.com/docyx/pc-part-dataset), MIT License.
The raw files have thousands of parts and are missing columns the checker needs,
so this script:
  1. Keeps only current generation parts with a price
  2. Picks the most popular ones (the raw files are sorted by popularity)
  3. Fills in columns the checker needs (socket, RAM type, GPU power, case sizes)
  4. Saves them in the format described in data/README.md

Run with:  python -m src.build_parts
Then check data/parts/cases.csv and fill in max_gpu_length_mm by hand.
"""

import re
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "data" / "raw"
OUT = ROOT / "data" / "parts"

# How many parts to keep
CPUS_PER_SOCKET = 3
BOARDS_PER_SOCKET = 3
RAM_PER_TYPE = 5
N_GPUS = 12
N_CASES = 10
N_PSUS = 8
N_STORAGE = 8

# CPU generation -> socket (current platforms only; anything else is dropped)
ARCH_TO_SOCKET = {
    "Zen 5": "AM5",
    "Zen 4": "AM5",
    "Zen 3": "AM4",
    "Arrow Lake": "LGA1851",
    "Raptor Lake Refresh": "LGA1700",
    "Raptor Lake": "LGA1700",
    "Alder Lake": "LGA1700",
}

# Total board power in watts, from NVIDIA / AMD / Intel spec pages.
# GPUs whose chipset isn't listed here are skipped.
GPU_POWER = {
    "GeForce RTX 3050 8GB": 130,
    "GeForce RTX 3060 12GB": 170,
    "GeForce RTX 4060": 115,
    "GeForce RTX 4060 Ti": 160,
    "GeForce RTX 4070": 200,
    "GeForce RTX 4070 SUPER": 220,
    "GeForce RTX 4070 Ti SUPER": 285,
    "GeForce RTX 4080 SUPER": 320,
    "GeForce RTX 4090": 450,
    "GeForce RTX 5060": 145,
    "GeForce RTX 5060 Ti": 180,
    "GeForce RTX 5070": 250,
    "GeForce RTX 5070 Ti": 300,
    "GeForce RTX 5080": 360,
    "GeForce RTX 5090": 575,
    "Radeon RX 7600": 165,
    "Radeon RX 7600 XT": 190,
    "Radeon RX 7700 XT": 245,
    "Radeon RX 7800 XT": 263,
    "Radeon RX 7900 GRE": 260,
    "Radeon RX 7900 XT": 315,
    "Radeon RX 7900 XTX": 355,
    "Radeon RX 9060 XT": 160,
    "Radeon RX 9070": 220,
    "Radeon RX 9070 XT": 304,
    "Arc B580": 190,
}

FORM_FACTORS = {"ATX": "ATX", "Micro ATX": "Micro-ATX", "Mini ITX": "Mini-ITX"}

# Case type -> motherboard sizes it fits (bigger cases fit smaller boards)
CASE_FITS = {
    "ATX": "ATX;Micro-ATX;Mini-ITX",
    "MicroATX": "Micro-ATX;Mini-ITX",
    "Mini ITX": "Mini-ITX",
}


def read(name: str) -> pd.DataFrame:
    df = pd.read_csv(RAW / f"{name}.csv")
    df = df.dropna(subset=["price"])          # can't budget without a price
    df = df[df["price"] > 0]
    df["price"] = df["price"].round().astype(int)
    return df


def first_number(text) -> int | None:
    match = re.search(r"\d+", str(text))
    return int(match.group()) if match else None


def build_cpus() -> pd.DataFrame:
    df = read("cpu")
    df["socket"] = df["microarchitecture"].map(ARCH_TO_SOCKET)
    df = df.dropna(subset=["socket", "tdp"])
    df["brand"] = df["name"].str.split().str[0]
    df["has_igpu"] = df["graphics"].notna()
    df = df.groupby("socket", sort=False).head(CPUS_PER_SOCKET)
    return df.rename(columns={"core_count": "cores", "tdp": "tdp_watts"})[
        ["name", "brand", "socket", "cores", "tdp_watts", "has_igpu", "price"]]


def board_ram_type(row) -> str:
    if row["socket"] == "AM4":
        return "DDR4"
    if row["socket"] == "LGA1700":
        # Intel 12th to 14th gen boards come in both. DDR4 boards say so in the name.
        name = row["name"].upper()
        return "DDR4" if ("DDR4" in name or re.search(r"\bD4\b", name)) else "DDR5"
    return "DDR5"  # AM5 and LGA1851 are DDR5 only


def build_motherboards() -> pd.DataFrame:
    df = read("motherboard")
    df = df[df["socket"].isin(set(ARCH_TO_SOCKET.values()))]
    df = df[df["form_factor"].isin(FORM_FACTORS)]
    df["form_factor"] = df["form_factor"].map(FORM_FACTORS)
    df["ram_type"] = df.apply(board_ram_type, axis=1)
    # One extra DDR4 Intel board so the checker has DDR4 vs DDR5 conflicts to catch
    picks = df.groupby("socket", sort=False).head(BOARDS_PER_SOCKET)
    ddr4_intel = df[(df["socket"] == "LGA1700") & (df["ram_type"] == "DDR4")].head(1)
    df = pd.concat([picks, ddr4_intel]).drop_duplicates("name")
    return df[["name", "socket", "ram_type", "form_factor", "price"]]


def build_ram() -> pd.DataFrame:
    df = read("memory")
    # speed looks like "5,6000" (DDR5 at 6000 MHz); modules like "2,16" (2 sticks of 16 GB)
    speed = df["speed"].astype(str).str.split(",", expand=True)
    modules = df["modules"].astype(str).str.split(",", expand=True)
    df["ram_type"] = "DDR" + speed[0]
    df["speed_mhz"] = pd.to_numeric(speed[1], errors="coerce")
    df["sticks"] = pd.to_numeric(modules[0], errors="coerce")
    df["capacity_gb"] = df["sticks"] * pd.to_numeric(modules[1], errors="coerce")
    df = df[df["ram_type"].isin(["DDR4", "DDR5"])].dropna(subset=["speed_mhz", "capacity_gb"])
    df["name"] = df["name"] + " " + df["ram_type"] + "-" + df["speed_mhz"].astype(int).astype(str)
    df = df.drop_duplicates("name")
    df = df.groupby("ram_type", sort=False).head(RAM_PER_TYPE)
    df[["speed_mhz", "sticks", "capacity_gb"]] = df[["speed_mhz", "sticks", "capacity_gb"]].astype(int)
    return df[["name", "ram_type", "capacity_gb", "sticks", "speed_mhz", "price"]]


def gpu_brand(chipset: str) -> str:
    if chipset.startswith("GeForce"):
        return "NVIDIA"
    if chipset.startswith("Radeon"):
        return "AMD"
    return "Intel"


def build_gpus() -> pd.DataFrame:
    df = read("video-card")
    df = df[df["chipset"].isin(GPU_POWER)].dropna(subset=["length"])
    # Some names leave out the chip (e.g. "Sapphire PULSE"), so add it
    def model_number(chipset: str) -> str:
        return next(word for word in chipset.split() if any(ch.isdigit() for ch in word))

    df["name"] = df.apply(
        lambda r: r["name"] if model_number(r["chipset"]) in r["name"] else f"{r['name']} {r['chipset']}",
        axis=1)
    df = df.drop_duplicates("name").head(N_GPUS)
    df["brand"] = df["chipset"].map(gpu_brand)
    df["tdp_watts"] = df["chipset"].map(GPU_POWER)
    df["vram_gb"] = df["memory"].astype(int)
    df["length_mm"] = df["length"].astype(int)
    return df[["name", "brand", "chipset", "vram_gb", "length_mm", "tdp_watts", "price"]]


def case_fits(case_type: str) -> str | None:
    for prefix, fits in CASE_FITS.items():
        if case_type.startswith(prefix):
            return fits
    return None


def build_cases() -> pd.DataFrame:
    df = read("case")
    df = df[df["type"].str.contains("Tower", na=False)]
    df["supported_form_factors"] = df["type"].map(case_fits)
    df = df.dropna(subset=["supported_form_factors"])
    # Keep a mix of sizes so the checker sees boards that don't fit
    big = df[df["supported_form_factors"].str.startswith("ATX")].head(N_CASES - 3)
    small = df[~df["supported_form_factors"].str.startswith("ATX")].head(3)
    df = pd.concat([big, small])
    df["max_gpu_length_mm"] = pd.NA  # not in the dataset: fill in from each maker's spec page
    return df[["name", "type", "supported_form_factors", "max_gpu_length_mm", "price"]]


def build_psus() -> pd.DataFrame:
    df = read("power-supply")
    df = df[df["type"] == "ATX"].dropna(subset=["wattage"]).head(N_PSUS)
    df["watts"] = df["wattage"].astype(int)
    return df[["name", "watts", "efficiency", "price"]]


def build_storage() -> pd.DataFrame:
    df = read("internal-hard-drive")
    df = df[df["interface"].str.startswith(("M.2 PCIe", "SATA 6"), na=False)]
    # Raw "type" is "SSD" or a spin speed like 7200 (a hard drive)
    df["type"] = df.apply(
        lambda r: "NVMe SSD" if r["interface"].startswith("M.2")
        else ("SATA SSD" if str(r["type"]) == "SSD" else "HDD"),
        axis=1)
    df["name"] = df["name"] + " " + (df["capacity"] / 1000).map(lambda tb: f"{tb:g} TB")
    df = df.drop_duplicates("name").head(N_STORAGE)
    df["capacity_gb"] = df["capacity"].astype(int)
    return df[["name", "type", "capacity_gb", "price"]]


BUILDERS = {
    "cpus": build_cpus,
    "motherboards": build_motherboards,
    "ram": build_ram,
    "gpus": build_gpus,
    "cases": build_cases,
    "psus": build_psus,
    "storage": build_storage,
}


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    for category, build in BUILDERS.items():
        df = build()
        df.to_csv(OUT / f"{category}.csv", index=False)
        print(f"{category:13} {len(df):3} parts")
    print("\nNext: fill in max_gpu_length_mm in data/parts/cases.csv from each case maker's spec page.")


if __name__ == "__main__":
    main()
