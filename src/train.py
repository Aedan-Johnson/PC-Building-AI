"""Training loop. Owner: Aedan.

Saves model to checkpoints/ and the loss chart to results/loss_chart.png.
Falls back to CPU if no GPU; use Google Colab if the home PC is too slow.
"""

import torch

DEVICE = "cuda" if torch.cuda.is_available() else "cpu"


def main():
    # TODO: load train.txt, tokenize, train, log loss, save checkpoint and chart
    raise NotImplementedError


if __name__ == "__main__":
    main()
