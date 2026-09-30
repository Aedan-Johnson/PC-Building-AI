"""Tokenizer. Owner: Aedan.

Start with character level (simplest). Upgrade to BPE later if time allows
(see Karpathy "Let's build the GPT Tokenizer").
"""


class CharTokenizer:
    def __init__(self, text: str):
        raise NotImplementedError

    def encode(self, text: str) -> list[int]:
        raise NotImplementedError

    def decode(self, ids: list[int]) -> str:
        raise NotImplementedError
