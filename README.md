# PC Building Specialist AI

A small language model, built from scratch in Python, that helps people pick parts for a gaming or office PC. Give it a budget and a use case and it suggests a parts list. Give it a list of parts and it tells you if they work together.

The AI does the talking. A rule based **checker** verifies every answer before anyone sees it.

**Built by:** Aedan Johnson (solo project, Self Directed Passion Project)
**Full plan:** [`data/project-plan.pdf`](data/project-plan.pdf)

## Status (Oct 19, 2026)

- [x] Repo structure, file outlines, and spreadsheet headers
- [x] Parts loader (`src/parts.py`)
- [ ] Parts spreadsheets filled in
- [ ] Checker rules and tests
- [ ] Chat generator and `train.txt`
- [ ] Tokenizer, model, and training
- [ ] Pipeline and terminal chat program
- [ ] Testing and security tests

## How it works

```
Parts spreadsheet (data/parts/*.csv)
        |
        v
Chat generator (src/generate_chats.py) ---> data/train.txt
        |
        v
Train the AI (src/train.py) ---> checkpoints/
        |
        v
User question ---> AI answer ---> Checker ---> Final answer
                  (src/model.py)  (src/checker.py)
```

## Scope

**I am building:** a parts dataset, a practice chat generator, my own ~10M parameter model, a compatibility checker, a terminal chat program, tests (including security tests), a proposal pitch, and a final presentation.

**I am not building:** a website or app, live store prices, laptops or prebuilt PCs.

## Setup

Requires Python 3.11 or newer, Git, and VS Code (Python extension).

```bash
git clone https://github.com/Aedan-Johnson/PC-Building-AI.git
cd PC-Building-AI
python -m venv .venv
# Windows:        .venv\Scripts\activate
# macOS / Linux:  source .venv/bin/activate
pip install -r requirements.txt
pytest
```

## Project layout

| Path | What it is |
|---|---|
| `data/parts/` | Parts spreadsheets (one CSV per category) |
| `data/train.txt` | Generated practice chats (not committed if large) |
| `src/checker.py` | Compatibility rules |
| `src/generate_chats.py` | Turns parts into practice chats |
| `src/tokenizer.py` | Text to numbers and back |
| `src/model.py` | The transformer model |
| `src/train.py` | Training loop, saves loss chart |
| `src/pipeline.py` | Connects model and checker |
| `src/chat.py` | Terminal chat program |
| `tests/` | Checker tests, security tests, 20 eval questions |
| `results/` | Loss charts, example chats, test results |
| `data/project-plan.pdf` | Full project plan and timeline |

## Checker rules

1. CPU socket matches the motherboard
2. RAM type matches the motherboard
3. Motherboard fits in the case
4. Graphics card fits in the case
5. Power supply is strong enough (total watts × 1.3)
6. Total price is within budget
7. Every part the AI mentions exists in the spreadsheets

Each rule gets one test with a build that should pass and one that should fail.

## Success criteria

1. Loss goes down during training
2. At least 16 of 20 eval questions get a correct, in budget build
3. Checker blocks 100% of broken builds
4. All trick tests pass

## Key dates (subject to change)

| Date | Milestone |
|---|---|
| Oct 25 | Parts spreadsheets filled, checker done with tests |
| Oct 30 | `train.txt` done |
| Nov 1 | Annotated bibliography done |
| Nov 6 | First trained AI with loss chart |
| Nov 13 | Everything connected in the terminal |
| Nov 20 | Testing done, feature freeze |
| Nov 30 | Slides and backup demo video |
| Dec 3 | Final presentation (target) |

See [`CONTRIBUTING.md`](CONTRIBUTING.md) for the Git workflow.
