import json
from typing import List

import matplotlib
import matplotlib.pyplot as plt

matplotlib.rcParams["text.usetex"] = True
font = {
    "family": "monospace",
    "weight": "bold",
    "size": 12,
}
matplotlib.rc("font", **font)

if __name__ == "__main__":
    morris_variance_file = open("morris_plus_simulation_01_result.json", "rb")
    morris_variance = json.load(morris_variance_file)
    morris_variance_file.close()

    contadores_esperados = morris_variance["contadores_esperados"]
    contadores_devolvidos_por_morris_plus = morris_variance["contadores_devolvidos_por_morris_plus"]
    erro_relativo = morris_variance["erro_relativo"]

    def desenha_grafico_01():
        _, ax = plt.subplots()
        ax.plot(
            contadores_esperados,
            contadores_devolvidos_por_morris_plus,
            label=r"$\hat{n}$",
            color="orange",
            alpha=0.5,
        )
        ax.plot(contadores_esperados, contadores_esperados, label="n", linestyle=":")
        ax.set_xlabel("Iterações", labelpad=15, fontsize=16)
        ax.set_ylabel("Quantidade de elementos", labelpad=15, fontsize=16)
        ax.set_title(r"Estimativas", fontsize=16)
        ax.legend()
        ax.ticklabel_format(style="plain")
        ax.tick_params(axis="x", labelsize=12)
        ax.tick_params(axis="y", labelsize=12)
        plt.tight_layout()
        plt.show()

    def desenha_grafico_02(
        inicio=0,
        fim=-1,
        xticks: List[int] = [],
        erro_esperado: int = 0,
        title="Erro relativo",
    ):
        _, ax = plt.subplots()
        erro_relativo_100 = list(map(lambda erro: 100 * erro, erro_relativo))
        ax.plot(contadores_esperados[inicio:fim], erro_relativo_100[inicio:fim], alpha=0.5, color="orange")
        ax.set_xlabel("Iterações", labelpad=15, fontsize=16)
        ax.set_ylabel("Erro relativo", labelpad=15, fontsize=16)
        ax.set_title(title, fontsize=16)
        ax.axhline(y=0, xmin=0, xmax=1000000, linestyle=":")
        ax.ticklabel_format(style="plain")

        if xticks:
            ax.set_xticks(xticks)

        if erro_esperado:
            ax.axhline(
                y=erro_esperado,
                xmin=0,
                xmax=1000000,
                linestyle=":",
            )
            ax.axhline(
                y=-erro_esperado,
                xmin=0,
                xmax=1000000,
                linestyle=":",
            )

            new_yticks = list(set(list(ax.get_yticks()) + [erro_esperado, -erro_esperado]))
            ax.set_yticks(new_yticks)

        ax.tick_params(axis="x", labelsize=12)
        ax.tick_params(axis="y", labelsize=12)
        plt.tight_layout()
        plt.show()

    desenha_grafico_01()
    desenha_grafico_02(erro_esperado=10)
    desenha_grafico_02(
        fim=50,
        erro_esperado=10,
        title="50 primeiras iterações",
    )
    desenha_grafico_02(
        inicio=50,
        xticks=[50, 250000, 500000, 750000, 1000000],
        erro_esperado=10,
        title="Desconsiderando as 50 primeiras iterações",
    )
