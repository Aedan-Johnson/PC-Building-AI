# PC Building Specialist AI

A small language model, built from scratch in Python, that helps people pick parts for a gaming or office PC. Give it a budget and a use case and it suggests a parts list. Give it a list of parts and it tells you if they work together.

The AI does the talking. A rule based **checker** verifies every answer before anyone sees it.

**Team:** Aedan and Yunior
**Full plan:** [`docs/project-plan.pdf`](docs/project-plan.pdf)

## How it works

```
Parts spreadsheet (data/parts/*.csv)
        |
        v
Chat generator (src/generate_chats.py) ---> data/train.txt
        |
        v
Train our AI (src/train.py) ---> checkpoints/
        |
        v
User question ---> AI answer ---> Checker ---> Final answer
                  (src/model.py)  (src/checker.py)
```

## Scope

**We are building:** a parts dataset, a practice chat generator, our own ~10M parameter model, a compatibility checker, a terminal chat program, tests (including security tests), and two presentations.

**We are not building:** a website or app, live store prices, laptops or prebuilt PCs.

## Setup

Requires Python 3.11 or newer, Git, and VS Code (Python + Live Share extensions).

```bash
git clone https://github.com/<your-username>/pc-building-ai.git
cd pc-building-ai
python -m venv .venv
# Windows:        .venv\Scripts\activate
# macOS / Linux:  source .venv/bin/activate
pip install -r requirements.txt
pytest
```

## Project layout

| Path | What it is | Owner |
|---|---|---|
| `data/parts/` | Parts spreadsheets (one CSV per category) | Yunior |
| `data/train.txt` | Generated practice chats (not committed if large) | Yunior |
| `src/checker.py` | Compatibility rules | Aedan |
| `src/generate_chats.py` | Turns parts into practice chats | Yunior (Aedan helps) |
| `src/tokenizer.py` | Text to numbers and back | Aedan |
| `src/model.py` | The transformer model | Aedan |
| `src/train.py` | Training loop, saves loss chart | Aedan |
| `src/pipeline.py` | Connects model and checker | Aedan |
| `src/chat.py` | Terminal chat program | Yunior |
| `tests/` | Checker tests, security tests, 30 eval questions | Both |
| `results/` | Loss charts, example chats, test results | Both |

## Checker rules

1. CPU socket matches the motherboard
2. RAM type matches the motherboard
3. Motherboard fits in the case
4. Graphics card fits in the case
5. Power supply is strong enough (total watts × 1.3)
6. Total price is within budget
7. Every part the AI mentions exists in our spreadsheet

Each rule gets one test with a build that should pass and one that should fail.

## Success criteria

1. Loss goes down during training
2. At least 24 of 30 eval questions get a correct, in budget build
3. Checker blocks 100% of broken builds
4. All trick tests pass

## Key dates (subject to change)

| Date | Milestone |
|---|---|
| Oct 2 | Proposal presentation |
| Oct 9 | Everything installed, both using GitHub |
| Oct 21 | Parts spreadsheet and checker done |
| Oct 26 | `train.txt` done |
| Oct 30 | First trained AI |
| Nov 13 | Everything connected in the terminal |
| Nov 20 | Testing done, feature freeze |
| Nov 30 | Slides and backup demo video |
| Dec 3 | Final presentation |

See [`CONTRIBUTING.md`](CONTRIBUTING.md) for how we work together.
