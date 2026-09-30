"""Our transformer language model (~10M parameters). Owner: Aedan.

Reference: Karpathy "Let's build GPT" and Raschka "LLMs from scratch" ch. 3 to 5.
"""

import torch.nn as nn

CONFIG = {
    "block_size": 256,   # max tokens of context
    "n_embd": 384,
    "n_head": 6,
    "n_layer": 6,
    "dropout": 0.2,
}


class GPT(nn.Module):
    def __init__(self, vocab_size: int, config: dict = CONFIG):
        super().__init__()
        raise NotImplementedError

    def forward(self, idx, targets=None):
        raise NotImplementedError

    def generate(self, idx, max_new_tokens: int):
        raise NotImplementedError
