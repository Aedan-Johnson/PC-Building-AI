"""Turns the parts spreadsheets into practice chats. Owner: Yunior (Aedan helps).

Output: data/train.txt in this format:

    User: I have $1200 for a gaming PC.
    Bot: CPU: Ryzen 5 7600 ($199), GPU: ... Total: $1,184.

Tips from the plan:
1. At least 20 different ways to ask the same thing
2. Mix budgets and uses (gaming, school, streaming, editing)
3. Run every build through the checker first so the AI only learns correct answers
"""

from pathlib import Path

OUTPUT = Path(__file__).resolve().parent.parent / "data" / "train.txt"

BUDGET_QUESTIONS = [
    "I have ${budget} for a {use} PC.",
    "What's the best {use} build for ${budget}?",
    # TODO: add at least 18 more
]

COMPAT_QUESTIONS = [
    "Will a {part_a} work with a {part_b}?",
    "Is the {part_a} compatible with the {part_b}?",
    # TODO: add at least 18 more
]

USES = ["gaming", "school", "streaming", "editing", "office"]


def main():
    # TODO: load parts, build valid builds, verify with checker, write chats
    raise NotImplementedError


if __name__ == "__main__":
    main()
