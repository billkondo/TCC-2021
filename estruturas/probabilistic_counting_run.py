import sys
from typing import List

import matplotlib
import matplotlib.pyplot as plt

from probabilistic_counting import ProbabilisticaCounting

matplotlib.rcParams["text.usetex"] = True

if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise Exception("Empty filename")

    filename = sys.argv[1]
    m = 64 if len(sys.argv) < 3 else int(sys.argv[2])
    probabilistic_count = ProbabilisticaCounting(m=m)

    sizes: List[int] = []
    answered_sizes: List[int] = []
    size = 0

    sizes.append(size)
    answered_sizes.append(probabilistic_count.count())

    with open(f"./input/{filename}", "r") as f:
        for line in f:
            x = int(line)
            probabilistic_count.add(x)

            size += 1
            sizes.append(size)
            answered_sizes.append(probabilistic_count.count())

    fig, ax = plt.subplots()
    expected_line = ax.plot(
        sizes,
        sizes,
        dashes=[2, 2, 10, 2],
        label=r"$n$",
    )
    answered_line = ax.plot(
        sizes,
        answered_sizes,
        label=r"$\hat{n}$",
    )

    ax.legend()
    plt.show()
