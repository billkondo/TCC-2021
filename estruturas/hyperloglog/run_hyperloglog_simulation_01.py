import random
import time
from typing import List

import matplotlib
import matplotlib.pyplot as plt

from ..random_number_generator import gera_numeros_aleatorios
from .hyperloglog import HyperLogLog

matplotlib.rcParams["text.usetex"] = True
font = {
    "family": "normal",
    "weight": "bold",
    "size": 8,
}
matplotlib.rc("font", **font)


TAMANHO_DO_CONJUNTO = 1000000


def constroi_grafico(
    tamanhos: List[int],
    respostas: List[int],
    m: int,
    inicio: int = 0,
    fim: int = -1,
):
    _, ax = plt.subplots()
    ax.plot(
        tamanhos[inicio:fim],
        tamanhos[inicio:fim],
        linestyle=":",
        label=r"$n$",
    )
    ax.plot(
        tamanhos[inicio:fim],
        respostas[inicio:fim],
        label=r"$\hat{n}$",
        color="orange",
        alpha=0.5,
    )

    ax.set_xlabel("Iterações", labelpad=15)
    ax.set_ylabel("Quantidade de elementos distintos", labelpad=15)
    ax.legend()
    ax.set_title(rf"Experimento 1 - Algoritmo $\textbf{{HyperLogLog}}$ ($m = {{{m}}}$)")
    plt.ticklabel_format(style="plain")
    plt.tight_layout()
    plt.show()


def constroi_grafico_erro(
    tamanhos: List[int],
    respostas: List[int],
    m: int,
    inicio: int = 0,
    fim: int = -1,
    xticks: List[int] = [],
    erro_esperado=0,
):
    erros: List[int] = []

    erros.append(0)
    for i in range(1, len(tamanhos)):
        erro_relativo = (respostas[i] - tamanhos[i]) / i
        erros.append(erro_relativo * 100)

    _, ax = plt.subplots()
    ax.plot(
        tamanhos[inicio:fim],
        erros[inicio:fim],
        label=r"$\hat{n}$",
        color="orange",
        alpha=0.5,
    )
    ax.axhline(
        y=0,
        xmin=0,
        xmax=1000000,
        linestyle="--",
    )

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
        ax.axhline(
            y=2 * erro_esperado,
            xmin=0,
            xmax=1000000,
            linestyle=":",
        )
        ax.axhline(
            y=-2 * erro_esperado,
            xmin=0,
            xmax=1000000,
            linestyle=":",
        )

        ax.set_yticks([-2 * erro_esperado, -erro_esperado, 0.0, erro_esperado, 2 * erro_esperado])
        ax.tick_params(axis="y")

    if xticks:
        ax.set_xticks(xticks)

    ax.set_xlabel("Iterações", labelpad=15)
    ax.set_ylabel("Erro Relativo", labelpad=15)
    ax.legend()
    ax.set_title(rf"Experimento 1 - Algoritmo $\textbf{{HyperLogLog}}$ ($m = {{{m}}}$)")
    plt.ticklabel_format(style="plain")
    plt.tight_layout()
    plt.show()


def experimento(M: int, erro_esperado: int = 0):
    random.seed(0)
    hyperloglog = HyperLogLog(m=M)

    tamanhos: List[int] = []
    respostas: List[int] = []
    tamanho_atual = 0

    tamanhos.append(tamanho_atual)
    respostas.append(hyperloglog.conta())

    start_time = time.time()

    for x in gera_numeros_aleatorios(TAMANHO_DO_CONJUNTO):
        hyperloglog.adiciona(x)

        tamanho_atual += 1
        tamanhos.append(tamanho_atual)
        respostas.append(hyperloglog.conta())

    print(time.time() - start_time)

    constroi_grafico(tamanhos, respostas, M)
    constroi_grafico_erro(tamanhos, respostas, M)
    constroi_grafico(tamanhos, respostas, fim=M * 4)
    constroi_grafico_erro(tamanhos, respostas, M, fim=M * 4)
    constroi_grafico_erro(
        tamanhos,
        respostas,
        inicio=M * 4,
        xticks=[4 * M, 250000, 500000, 750000, 1000000],
        erro_esperado=erro_esperado,
    )


if __name__ == "__main__":
    experimento(64, 13)
    experimento(1024, 3.25)
