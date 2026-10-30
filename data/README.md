# Parts Data

## Where it comes from
`data/raw/` holds the original CSVs from [docyx/pc-part-dataset](https://github.com/docyx/pc-part-dataset) (MIT License). They have thousands of parts and are missing some columns the checker needs.

`src/build_parts.py` turns them into the small, clean spreadsheets in `data/parts/` that the checker and chat generator use:

```bash
python -m src.build_parts
```

It keeps the most popular current generation parts with a price, and fills in:
- **CPU socket** from the CPU generation (Zen 4/5 = AM5, Zen 3 = AM4, Alder/Raptor Lake = LGA1700, Arrow Lake = LGA1851)
- **Motherboard RAM type** from the socket (Intel LGA1700 DDR4 boards have DDR4 or D4 in the name)
- **RAM type, speed, and capacity** from the dataset's speed and modules columns
- **GPU power** from NVIDIA, AMD, and Intel spec pages
- **Case board sizes** from the case type

**Filled in by hand:** `max_gpu_length_mm` in `cases.csv`, from each case maker's spec page. Running the script again clears it, so re-enter it or stop rerunning after it's filled in.

## Files

Prices in USD, whole dollars. Every `name` must be unique across all files (the checker uses names to confirm a part exists).

| File | Columns |
|---|---|
| `cpus.csv` | name, brand, socket, cores, tdp_watts, has_igpu, price |
| `motherboards.csv` | name, socket, ram_type, form_factor, price |
| `ram.csv` | name, ram_type, capacity_gb, sticks, speed_mhz, price |
| `gpus.csv` | name, brand, chipset, vram_gb, length_mm, tdp_watts, price |
| `cases.csv` | name, type, supported_form_factors, max_gpu_length_mm, price |
| `psus.csv` | name, watts, efficiency, price |
| `storage.csv` | name, type, capacity_gb, price |

**Allowed values**
- `socket`: `AM5`, `AM4`, `LGA1700`, `LGA1851`
- `ram_type`: `DDR4` or `DDR5`
- `form_factor`: `ATX`, `Micro-ATX`, `Mini-ITX`
- `supported_form_factors`: separated with `;` e.g. `ATX;Micro-ATX;Mini-ITX`
