import json
import math

import matplotlib
import matplotlib.pyplot as plt

matplotlib.rcParams["text.usetex"] = True
font = {
    "family": "normal",
    "weight": "bold",
    "size": 12,
}
matplotlib.rc("font", **font)

if __name__ == "__main__":
    morris_variance_file = open("morris_simulation_02_result.json", "rb")
    morris_variance = json.load(morris_variance_file)
    morris_variance_file.close()

    X = [int(key) for key in morris_variance.keys()]
    X.sort()

    X_log = list(map(lambda x: math.floor(math.log2(x + 1)), X))
    Y = [morris_variance[str(x)] for x in X]
    labels = list(map(lambda x: str(x), X_log))

    _, ax = plt.subplots()

    p1 = ax.bar(X_log, Y, tick_label=labels, alpha=0.5, color="orange")
    ax.bar_label(p1, label_type="edge", font={"size": 10})
    ax.set_xlabel(r"Valor de $X$ ao final da simulação", labelpad=15)
    ax.set_ylabel("Frequência", labelpad=15)
    ax.set_title(r"Experimento 2 - Algortimo \textbf{Morris}")
    plt.tight_layout()
    plt.show()
