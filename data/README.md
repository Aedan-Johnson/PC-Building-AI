# Parts Data

The files in `data/parts/` are the full CSVs from [docyx/pc-part-dataset](https://github.com/docyx/pc-part-dataset) (MIT License), unchanged. `src/parts.py` loads them.

| Category | File | Columns |
|---|---|---|
| cpus | `cpu.csv` | name, price, core_count, core_clock, boost_clock, microarchitecture, tdp, graphics |
| motherboards | `motherboard.csv` | name, price, socket, form_factor, max_memory, memory_slots, color |
| ram | `memory.csv` | name, price, speed, modules, price_per_gb, color, first_word_latency, cas_latency |
| gpus | `video-card.csv` | name, price, chipset, memory, core_clock, boost_clock, color, length |
| cases | `case.csv` | name, price, type, color, psu, side_panel, external_volume, internal_35_bays |
| psus | `power-supply.csv` | name, price, type, efficiency, wattage, modular, color |
| coolers | `cpu-cooler.csv` | name, price, rpm, noise_level, color, size |
| storage | `internal-hard-drive.csv` | name, price, capacity, price_per_gb, type, cache, form_factor, interface |

## Things to know when using it
- **Some parts have no price.** Skip them for budget builds.
- **Names repeat** (for example, the same GPU model from different listings). Don't rely on names alone being unique.
- **Columns the checker needs that aren't included:**
  - CPU socket: work it out from `microarchitecture` (Zen 4/5 = AM5, Zen 3 = AM4, Alder/Raptor Lake = LGA1700, Arrow Lake = LGA1851)
  - RAM type: `memory.csv` `speed` looks like `5,6000`, meaning DDR5 at 6000 MHz
  - Motherboard RAM type: not included (AM5 and LGA1851 are DDR5, AM4 is DDR4, LGA1700 boards can be either)
  - GPU power, case GPU clearance, cooler height and sockets: not included

## Price list (`price_overrides.csv`)

The dataset's prices are one-day lowest listings, so some are wrong. For example, discontinued parts show inflated reseller prices: the Ryzen 7 5800X3D is listed at $704.86. `price_overrides.csv` replaces those with researched **typical US prices from mid-2025 (Jun-Aug 2025)** for about 75 well-known parts. The `basis` column says where each number comes from.

- `slot`: cpu, cooler, motherboard, ram, gpu, storage, psu, case
- `name`: must match the part's name in `pc_ai.py`. GPU names have the chipset and memory added (for example `PNY OC GeForce RTX 5070 12GB`), and RAM names have the kit and speed added (for example `Corsair Vengeance 32 GB (2x16GB) DDR5-6000`). A name that doesn't match prints a warning.
- The builder only suggests parts listed in this file. Compatibility questions still work for every part in the dataset.
