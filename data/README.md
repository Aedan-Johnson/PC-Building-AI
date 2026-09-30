# Parts Data

One CSV per category in `data/parts/`. Prices in USD, whole dollars. Every `name` must be unique across all files (the checker uses names to confirm a part exists).

| File | Columns |
|---|---|
| `cpus.csv` | name, brand, socket, cores, tdp_watts, price |
| `motherboards.csv` | name, socket, ram_type, form_factor, price |
| `ram.csv` | name, ram_type, capacity_gb, speed_mhz, price |
| `gpus.csv` | name, brand, vram_gb, length_mm, tdp_watts, price |
| `cases.csv` | name, supported_form_factors, max_gpu_length_mm, price |
| `psus.csv` | name, watts, price |
| `storage.csv` | name, type, capacity_gb, price |

**Allowed values**
- `socket`: e.g. `AM5`, `AM4`, `LGA1700`, `LGA1851`
- `ram_type`: `DDR4` or `DDR5`
- `form_factor`: `ATX`, `Micro-ATX`, `Mini-ITX`
- `supported_form_factors`: separate with `;` e.g. `ATX;Micro-ATX;Mini-ITX`

Pull specs from manufacturer pages, not store listings.
