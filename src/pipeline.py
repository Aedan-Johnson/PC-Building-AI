"""Connects the AI and the checker. Owner: Aedan.

Flow: user question -> model answer -> parse parts -> checker -> final answer.
If the checker finds problems, return a safe fallback instead of the bad build.
"""

MAX_INPUT_CHARS = 1000  # security: cut off giant walls of text


def answer(question: str) -> str:
    raise NotImplementedError
