import random
from typing import List

import matplotlib
import matplotlib.pyplot as plt

from morris import Morris

matplotlib.rcParams["text.usetex"] = True
font = {
    "family": "monospace",
    "weight": "bold",
    "size": 12,
}
matplotlib.rc("font", **font)


def constroi_grafico(
    contadores_esperados: List[int],
    contadores_devolvidos_por_morris: List[int],
    tamanho: int,
    inicio: int = 0,
    vlines: List[int] = [],
    hide_expected_line=False,
):
    _, ax = plt.subplots()
    fim = inicio + tamanho

    if not hide_expected_line:
        # Gráfico da saída esperada
        ax.plot(
            contadores_esperados[inicio:fim],
            contadores_esperados[inicio:fim],
            linestyle=":",
            label=r"$n$",
        )

    # Gráfico do Algoritmo Morris
    ax.plot(
        contadores_esperados[inicio:fim],
        contadores_devolvidos_por_morris[inicio:fim],
        label=r"$\hat{n}$",
        alpha=0.5,
        color="orange",
    )

    if vlines:
        ax.set_xticks(vlines)

    for vline in vlines:
        ax.axvline(x=vline, ls=":")

    ax.set_xlabel("Iterações", labelpad=15, fontsize=16)
    ax.set_ylabel("Quantidade de elementos", labelpad=15, fontsize=16)
    ax.set_title(r"Estimativas", fontsize=16)
    ax.legend()
    ax.ticklabel_format(style="plain")
    ax.tick_params(axis="x", labelsize=12)
    ax.tick_params(axis="y", labelsize=12)
    plt.tight_layout()
    plt.show()


def constroi_grafico_erro_relativo(
    erro_relativo: List[int],
    tamanho: int,
):
    _, ax = plt.subplots()

    # Gráfico do erro esperado
    ax.plot(
        erro_relativo[:tamanho],
        label="erro relativo",
        alpha=0.5,
        color="orange",
    )

    # Linha de erro relativo zero
    ax.axhline(y=0, xmin=0, xmax=1000000, linestyle=":")

    ax.set_xlabel("Iterações", labelpad=15, fontsize=16)
    ax.set_ylabel("Erro relativo", labelpad=15, fontsize=16)
    ax.set_title(r"Erro Relativo", fontsize=16)
    ax.legend()
    ax.ticklabel_format(style="plain")
    ax.tick_params(axis="x", labelsize=12)
    ax.tick_params(axis="y", labelsize=12)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    random.seed(0)
    morris = Morris()

    contadores_devolvidos_por_morris = []
    contadores_esperados = []
    erro_relativo = []

    contadores_devolvidos_por_morris.append(morris.conta())
    contadores_esperados.append(0)
    erro_relativo = []
    for i in range(1, 1000001):
        morris.adiciona()
        contadores_devolvidos_por_morris.append(morris.conta())
        contadores_esperados.append(i)
        erro = (morris.conta() - i) / i
        erro_relativo.append(erro * 100)

    constroi_grafico(
        contadores_esperados,
        contadores_devolvidos_por_morris,
        250000,
        inicio=50000,
        vlines=[
            75720,
            176384,
            241343,
        ],
        hide_expected_line=True,
    )

    tamanhos = [100, 1000, 1000000]
    for tamanho in tamanhos:
        constroi_grafico(contadores_esperados, contadores_devolvidos_por_morris, tamanho)
        constroi_grafico_erro_relativo(erro_relativo, tamanho)
