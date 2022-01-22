import json

import matplotlib
import matplotlib.pyplot as plt

matplotlib.rcParams["text.usetex"] = True
font = {
    "family": "normal",
    "weight": "bold",
    "size": 14,
}
matplotlib.rc("font", **font)

if __name__ == "__main__":
    morris_variance_file = open("morris_plus_simulation_02_result.json", "rb")
    morris_variance = json.load(morris_variance_file)
    morris_variance_file.close()

    X = [int(key) for key in morris_variance.keys()]
    X.sort()
    Y = [morris_variance[str(key)] for key in X]

    values = []
    for index in range(0, len(Y)):
        for _ in range(0, Y[index]):
            values.append(X[index])

    _, ax = plt.subplots()
    ax.hist(values, bins=30, alpha=0.5, histtype="bar", ec="black", color="orange")
    plt.axvline(x=1000000)
    plt.axvline(x=900000)
    plt.axvline(x=1100000)
    ax.set_xlabel("Estimativas", labelpad=15)
    ax.set_ylabel("Frequência", labelpad=15)
    ax.set_xticks([900000, 975000, 1000000, 1025000, 1100000])
    ax.tick_params(axis="x", labelsize=10)
    plt.ticklabel_format(style="plain")
    ax.set_title(r"Experimento 2 - Algoritmo \textbf{Morris++}")
    plt.tight_layout()
    plt.show()
