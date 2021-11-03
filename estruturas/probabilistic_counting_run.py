import math
import sys
from typing import List

import matplotlib
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt

from probabilistic_counting import ProbabilisticaCounting

matplotlib.rcParams["text.usetex"] = True


def plot_estimate(
    sizes: List[int],
    answered_sizes: List[int],
):
    _, ax = plt.subplots()

    # expected line
    ax.plot(
        sizes,
        sizes,
        linestyle=":",
        color="lightblue",
    )

    # answered line
    ax.plot(
        sizes,
        answered_sizes,
        color="darkgreen",
    )

    error_upper_bound_10: List[float] = []
    error_lower_bound_10: List[float] = []
    error_upper_bound_5: List[float] = []
    error_lower_bound_5: List[float] = []

    for size in sizes:
        error_upper_bound_10.append(size * 1.1)
        error_lower_bound_10.append(size * 0.9)
        error_upper_bound_5.append(size * 1.05)
        error_lower_bound_5.append(size * 0.95)

    # error bounds
    ax.plot(
        sizes,
        error_upper_bound_10,
        sizes,
        error_lower_bound_10,
        color="firebrick",
        linestyle="--",
    )
    ax.plot(
        sizes,
        error_upper_bound_5,
        sizes,
        error_lower_bound_5,
        color="lightsalmon",
        linestyle="--",
    )

    ax.legend(
        handles=[
            mpatches.Patch(
                color="lightblue",
                label=r"$n$",
            ),
            mpatches.Patch(
                color="darkgreen",
                label=r"$\hat{n}$",
            ),
            mpatches.Patch(
                color="firebrick",
                label=r"erro relativo 10\%",
            ),
            mpatches.Patch(
                color="lightsalmon",
                label=r"erro relativo 5\%",
            ),
        ],
    )

    plt.xlabel(r"$n$")
    plt.ylabel(r"$\hat{n}$")
    plt.show()


def plot_relative_error(
    sizes: List[int],
    answered_sizes: List[int],
):
    _, ax = plt.subplots()

    relative_errors: List[float] = []
    no_error: List[int] = []
    for i in range(0, len(sizes)):
        relative_error = (answered_sizes[i] - sizes[i]) / i if i > 0 else 0
        relative_errors.append(relative_error * 100)
        no_error.append(0)

    ax.plot(
        sizes,
        relative_errors,
        color="lightsalmon",
        linestyle="solid",
    )

    ax.plot(
        sizes,
        no_error,
        color="lightgrey",
        linestyle="--",
    )

    plt.xlabel(r"$n$")
    plt.ylabel(r"erro relativo (\%)")
    plt.show()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise Exception("Empty filename")

    filename = sys.argv[1]
    m = 64 if len(sys.argv) < 3 else int(sys.argv[2])
    probabilistic_count = ProbabilisticaCounting(m=m)
    MAX = None if len(sys.argv) < 4 else int(sys.argv[3])

    sizes: List[int] = []
    answered_sizes: List[int] = []
    size = 0
    error = 0.78 / math.sqrt(m)

    sizes.append(size)
    answered_sizes.append(probabilistic_count.count())

    with open(f"./input/{filename}", "r") as f:
        for line in f:
            x = int(line)
            probabilistic_count.add(x)

            size += 1
            sizes.append(size)

            answered_sizes.append(probabilistic_count.count())

            if size == MAX:
                break

    plot_estimate(
        sizes,
        answered_sizes,
    )
    plot_relative_error(sizes, answered_sizes)
