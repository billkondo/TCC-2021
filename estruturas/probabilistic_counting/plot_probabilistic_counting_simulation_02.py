import json
from typing import List

import matplotlib
import matplotlib.pyplot as plt

matplotlib.rcParams["text.usetex"] = True
font = {
    "family": "normal",
    "weight": "bold",
    "size": 10,
}
matplotlib.rc("font", **font)

M = 64

config = {
    1024: {
        "expected_lower_bound_02": 975625,
        "expected_lower_bound_01": 951250,
        "expected_upper_bound_01": 1024375,
        "expected_upper_bound_02": 1048750,
        "xticks": [975625, 951250, 1000000, 1024375, 1048750],
    },
    64: {
        "expected_lower_bound_02": 805000,
        "expected_lower_bound_01": 902500,
        "expected_upper_bound_01": 1097500,
        "expected_upper_bound_02": 1195000,
        "xticks": [805000, 902500, 1000000, 1097500, 1195000],
    },
}[M]


def read_file(path: str) -> dict:
    with open(path, "rb") as input:
        return json.load(input)


def convert_keys_to_int(d: dict) -> dict:
    return {int(key): value for key, value in d.items()}


def sort_dict(d: dict) -> dict:
    return dict(sorted(d.items()))


def get_histogram_data(d: dict) -> List[int]:
    data: List[int] = []

    for key in d.keys():
        for _ in range(0, d[key]):
            data.append(key)

    return data


if __name__ == "__main__":
    data = sort_dict(
        convert_keys_to_int(
            read_file(
                f"probabilistic_counting_simulation_02_{M}.json",
            ),
        )
    )
    estimates = list(data.keys())
    histogram_data = get_histogram_data(data)

    _, ax = plt.subplots()
    ax.hist(histogram_data, bins=30, alpha=0.5, histtype="bar", ec="black", color="orange")
    plt.axvline(x=1000000, linestyle=":")
    plt.axvline(x=config["expected_lower_bound_01"], linestyle=":")
    plt.axvline(x=config["expected_upper_bound_01"], linestyle=":")
    plt.axvline(x=config["expected_lower_bound_02"], linestyle=":")
    plt.axvline(x=config["expected_upper_bound_02"], linestyle=":")
    ax.set_xlabel("Estimativas", labelpad=15, fontsize=16)
    ax.set_ylabel("Frequência", labelpad=15, fontsize=16)
    ax.set_xticks([estimates[0], *config["xticks"], estimates[-1]])
    ax.tick_params(axis="x")
    plt.ticklabel_format(style="plain")
    ax.set_title(rf"m = {M}", fontsize=16)
    plt.tight_layout()
    plt.show()
