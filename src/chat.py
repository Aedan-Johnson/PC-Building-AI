"""Terminal chat program. Owner: Yunior.

Run with:  python -m src.chat
Uses `rich` for nice tables and prompts. Print user text with markup disabled
so weird formatting codes show as plain text (security test).
"""

from rich.console import Console

console = Console()


def main():
    console.print("[bold]PC Building Specialist AI[/bold]  (type 'quit' to exit)")
    # TODO: loop: read input, call src.pipeline.answer(), print result
    raise NotImplementedError


if __name__ == "__main__":
    main()
