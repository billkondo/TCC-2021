import sys
from typing import List

import matplotlib
import matplotlib.pyplot as plt

from adaptive_sampling import AdaptiveSampling

matplotlib.rcParams["text.usetex"] = True

if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise Exception("Empty filename")

    filename = sys.argv[1]
    m = 64 if len(sys.argv) < 3 else int(sys.argv[2])
    adaptive_sampling = AdaptiveSampling(m=m)

    sizes: List[int] = []
    answered_sizes: List[int] = []
    size = 0

    sizes.append(size)
    answered_sizes.append(adaptive_sampling.count())

    with open(f"./input/{filename}", "r") as f:
        for line in f:
            x = int(line)
            adaptive_sampling.add(x)

            size += 1
            sizes.append(size)
            answered_sizes.append(adaptive_sampling.count())

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
