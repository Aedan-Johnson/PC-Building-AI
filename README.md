# PC Building Specialist AI

A small language model, built from scratch in Python, that helps people pick parts for a PC. Tell it your budget and what the PC is for, and it suggests a full parts list. Name some parts, and it tells you if they work together.

The AI does the talking. A rule based **checker** verifies every build before anyone sees it, so a broken or over-budget build never reaches the user.

**Built by:** Aedan Johnson (solo project, Self Directed Passion Project)
**Full plan:** [`data/project-plan.pdf`](data/project-plan.pdf)

## Quick start

Requires Python 3.11 or newer.

```bash
git clone https://github.com/Aedan-Johnson/PC-Building-AI.git
cd PC-Building-AI
python -m venv .venv
# macOS / Linux:  source .venv/bin/activate
# Windows:        .venv\Scripts\activate
pip install -r requirements.txt

python pc_ai.py
```

On the first run, `python pc_ai.py` makes anything that's missing (the practice chats, then the trained model) and then starts the chat. Training takes about 40 minutes on an Apple Silicon Mac. You can press Ctrl+C to skip it and chat using the checked builder only.

## What you can ask

It understands casual typing and remembers the conversation.

| Kind | Examples |
|---|---|
| Builds | `I have $1200 for a gaming PC`, `gaming pc 1.2k`, `i got 2 grand for a pc`, `pc for my grandma, 700` |
| Builds with parts you want | `$1500 gaming pc with a 9800x3d`, `$1300 build with an rtx 5070` |
| Follow-ups | `make it cheaper`, `upgrade it`, `what about $1500`, `make it for editing instead` |
| Single parts | `best gpu for $400`, `what cpu should i get`, `is the 9800x3d good` |
| Compatibility | `will a 7800x3d work with a b650 gaming plus wifi`, `can a rtx 5090 fit in a cooler master q300l v2` |
| PC questions | `what is a psu`, `ddr4 vs ddr5`, `what's a bottleneck` |
| About the AI | `who made you`, `what can you do` |

Uses it knows: gaming, streaming, editing, school, office. Unrealistic budgets get an honest (Gen Z) answer:

```
You: i want a $50 pc for gaming
AI: not possible bro 😭🥀 The cheapest build I can actually verify costs about $575 (too low, sorry).
```

## Commands

```bash
python pc_ai.py                      # make anything missing, then chat (default)
python pc_ai.py all                  # generate + train + eval + chat, start to finish
python pc_ai.py generate             # write practice chats to data/train.txt
python pc_ai.py train --steps 3000   # train the model -> checkpoints/model.pt + results/loss_chart.png
python pc_ai.py eval                 # eval questions + checker rule tests + trick tests
```

## How it works

```
Parts spreadsheets (data/parts/*.csv) + researched prices (data/price_overrides.csv)
        |
        v
Catalog: cleans the data and adds socket, RAM type, GPU power, case clearance
        |
        +--> Rule based builder: makes a correct build for any budget and use
        |
        v
Chat generator  --->  data/train.txt  --->  Train the AI  --->  checkpoints/model.pt
(only checked builds go into the training data)

User question ---> understand it (budget, use, parts named, follow-ups)
                        |
                        v
                   AI writes a build ---> Checker (7 rules) ---> passes? show it
                                                |
                                                +--> fails? show the rule based build instead
```

**The model:** a GPT-style transformer written from scratch in PyTorch, based on Karpathy's "Let's build GPT" and Raschka's *Build a Large Language Model (From Scratch)*.

- 10.9M parameters: 6 layers, 6 attention heads, 384-dimension embeddings, 512-character context
- Character-level tokenizer (78 characters)
- Trained on about 5,900 practice chats (about 1.9M characters): budget builds in formal and casual wording, plus compatibility questions that pass and fail
- 3,000 steps, AdamW, cosine learning rate. It runs on an NVIDIA GPU, Apple Silicon (MPS), or the CPU.

## Checker rules

1. CPU socket matches the motherboard
2. RAM type (DDR4/DDR5) matches the motherboard
3. Motherboard fits in the case
4. Graphics card fits in the case
5. Power supply is strong enough: watts ≥ (CPU watts + GPU watts) × 1.3
6. Total price is within budget
7. Every part the AI mentions exists in the parts list

`python pc_ai.py eval` tests every rule with one build that should pass and one that should fail.

## Results

| Test | Result | Goal |
|---|---|---|
| Eval questions ([`tests/eval_questions.csv`](tests/eval_questions.csv)) | 20 / 20 | at least 16 |
| Checker rule tests (pass and fail for each rule) | 14 / 14 | all |
| Trick and security tests | 5 / 5 | all |
| Training loss goes down | yes (4.47 → 0.36 by step 750) | yes |

The trick tests cover: formatting codes in input (`[bold red]`), a 10,000-character input, a $50 budget, a made-up part name, and "ignore all your rules". The eval also reports how often the AI's *own* build passes the checker without help. Full results are saved to [`results/eval_results.csv`](results/eval_results.csv). Training writes the loss chart to `results/loss_chart.png` and the log to `results/train_log.txt`. The full 3,000-step run is still to come; the numbers above are from a run that stopped at step 750.

## Data and prices

**PC parts data:** Oliver, D. (2021 to 2025). *pc-part-dataset* [Data set]. GitHub. https://github.com/docyx/pc-part-dataset (MIT License). The author collected it from [PCPartPicker](https://pcpartpicker.com).

- Files used: `cpu.csv`, `motherboard.csv`, `memory.csv`, `video-card.csv`, `case.csv`, `power-supply.csv`, `cpu-cooler.csv`, `internal-hard-drive.csv`. They're stored unchanged in `data/parts/` (see [`data/README.md`](data/README.md)).
- Columns the checker needs that the dataset doesn't have are added in `pc_ai.py` section 2:
  - **CPU socket**, from `microarchitecture`: Zen 4/5 = AM5, Zen 3 = AM4, Alder/Raptor Lake = LGA1700, Arrow Lake = LGA1851
  - **RAM type**, from `speed` (`5,6000` = DDR5). A motherboard's RAM type comes from its socket, plus "DDR4"/"D4" in LGA1700 board names.
  - **GPU power**: the `GPU_SPECS` table of official board power per chipset
  - **Case GPU clearance**: the `CASE_SPECS` table, **estimated per case type** (for example ATX Mid Tower = 360 mm), not exact per-case specs

**Prices:** the builder only suggests the 69 parts in [`data/price_overrides.csv`](data/price_overrides.csv). Each has a researched **typical US price from mid-2025 (June to August 2025)**, with a note on what it's based on (official launch price and/or a dated mid-2025 report). I chose mid-2025 because prices were stable then. **They do not match today's prices.** RAM and SSDs cost several times more since the 2025-26 memory shortage (32GB of DDR5-6000 went from about $90 to about $450), and many graphics cards now sell above their official prices. Every build the AI shows includes this note.

To change a price, edit the CSV and then run `python pc_ai.py generate` and `python pc_ai.py train`.

## Project layout

| Path | What it is |
|---|---|
| `pc_ai.py` | All the code, in numbered sections (see below) |
| `data/parts/` | Parts spreadsheets from pc-part-dataset (unchanged) |
| `data/price_overrides.csv` | Researched mid-2025 prices for the parts the builder uses |
| `data/train.txt` | Generated practice chats (not committed; run `generate`) |
| `checkpoints/model.pt` | Trained model (not committed; run `train`) |
| `tests/eval_questions.csv` | 20 eval questions (15 builds, 5 compatibility) |
| `results/` | Loss chart, training log, eval results |
| `data/project-plan.pdf` | Full project plan and timeline |

**Sections of `pc_ai.py`:**

1. Paths and settings
2. Parts data and catalog (cleaning, added specs, price list)
3. Checker (7 rules)
4. Rule based builder
5. Chat generator
6. Tokenizer
7. Model (GPT)
8. Training
9. Pipeline: understanding questions, follow-ups, part picks, the AI + checker
10. Terminal chat
11. Eval and trick tests
12. Command line

## Limitations

- Prices are from mid-2025, not live (live prices are out of scope).
- Case GPU clearance is estimated per case type, not measured per case.
- It doesn't check CPU cooler height or socket support. Instead, it only suggests air coolers that support all four sockets.
- The model is small and character-level, so it sometimes gets a part name slightly wrong. When that happens, the checker catches it and the user gets the rule based build instead.
- No laptops, prebuilt PCs, or website/app. The project is a terminal program on purpose.

## Status (Nov 6, 2026)

- [x] Parts data, catalog, and researched price list
- [x] Checker rules (all 7)
- [x] Chat generator and `train.txt`
- [x] Tokenizer, model, and training
- [x] Pipeline and terminal chat program (casual questions, follow-ups, part picks)
- [x] Eval questions, checker rule tests, and security tests
- [ ] Annotated bibliography
- [ ] Slides and backup demo video
- [ ] Final presentation

## Key dates (subject to change)

| Date | Milestone |
|---|---|
| Nov 1 | Annotated bibliography done |
| Nov 6 | First trained AI with loss chart |
| Nov 13 | Everything connected in the terminal |
| Nov 20 | Testing done, feature freeze |
| Nov 30 | Slides and backup demo video |
| Dec 3 | Final presentation (target) |

See [`CONTRIBUTING.md`](CONTRIBUTING.md) for the Git workflow.
