import random
from typing import List

import matplotlib
import matplotlib.pyplot as plt

from ..random_number_generator import gera_numeros_aleatorios
from .probabilistic_counting import ProbabilisticaCounting

matplotlib.rcParams["text.usetex"] = True
matplotlib.rcParams["text.usetex"] = True
font = {
    "family": "normal",
    "weight": "bold",
    "size": 12,
}
matplotlib.rc("font", **font)

NUMERO_DE_ELEMENTOS = 1000000


def constroi_estimativa(
    tamanhos: List[int],
    respostas: List[int],
    start=0,
    end=-1,
    mostra_y_label=True,
    titulo="",
):
    _, ax = plt.subplots()

    # Tamanho esperado
    ax.plot(
        tamanhos[start:end],
        tamanhos[start:end],
        linestyle=":",
        label=r"$n$",
    )

    # Resposta devolvida
    ax.plot(
        tamanhos[start:end],
        respostas[start:end],
        color="orange",
        alpha=0.5,
        label=r"$\hat{n}$",
    )

    if mostra_y_label:
        ax.set_ylabel("Quantidade de elementos distintos", labelpad=15, fontsize=16)

    if titulo:
        ax.set_title(titulo, fontsize=16)

    ax.set_xlabel("Iterações", labelpad=15, fontsize=16)
    ax.tick_params(axis="x", labelsize=12)
    ax.tick_params(axis="y", labelsize=12)
    ax.ticklabel_format(style="plain")
    ax.legend()
    plt.tight_layout()
    plt.show()


def constroi_erro(
    tamanhos: List[int],
    respostas: List[int],
    start=0,
    end=-1,
    expected_error=0,
    xticks=[],
    vlines=[],
    titulo="",
    mostra_y_label=True,
):
    _, ax = plt.subplots()

    erros_relativo: List[float] = []
    for i in range(0, len(tamanhos)):
        erro_relativo = (respostas[i] - tamanhos[i]) / i if i > 0 else 0
        erros_relativo.append(erro_relativo * 100)

    ax.plot(
        tamanhos[start:end],
        erros_relativo[start:end],
        color="orange",
        alpha=0.5,
    )
    ax.axhline(y=0, xmin=0, xmax=1000000, linestyle=":")

    if expected_error:
        ax.axhline(
            y=expected_error,
            xmin=0,
            xmax=1000000,
            linestyle=":",
        )
        ax.axhline(
            y=-expected_error,
            xmin=0,
            xmax=1000000,
            linestyle=":",
        )
        ax.axhline(
            y=2 * expected_error,
            xmin=0,
            xmax=1000000,
            linestyle=":",
        )
        ax.axhline(
            y=-2 * expected_error,
            xmin=0,
            xmax=1000000,
            linestyle=":",
        )

        new_yticks = list(
            [
                -expected_error * 2,
                -expected_error,
                0,
                expected_error,
                expected_error * 2,
                25,
            ]
        )
        ax.set_yticks(new_yticks)
        ax.tick_params(axis="y", labelsize=12)

    if xticks:
        ax.set_xticks(xticks)
        ax.tick_params(axis="x", labelsize=12)

    if vlines:
        for x in vlines:
            ax.axvline(x=x, linestyle=":", alpha=0.5)

    if titulo:
        ax.set_title(titulo, fontsize=16)

    if mostra_y_label:
        ax.set_ylabel("Erro Relativo", labelpad=15, fontsize=16)

    ax.set_xlabel("Iterações", labelpad=15, fontsize=16)
    ax.tick_params(axis="x", labelsize=12)
    ax.tick_params(axis="y", labelsize=12)
    ax.ticklabel_format(style="plain")
    plt.tight_layout()
    plt.show()


def experimento(
    M: int,
    expected_error: int,
    xticks: List[int] = [],
    vlines: List[int] = [],
    mostra_y_label=True,
):
    random.seed(0)

    probabilistic_count = ProbabilisticaCounting(M)
    tamanhos: List[int] = []
    respostas: List[int] = []
    tamanho = 0

    tamanhos.append(tamanho)
    respostas.append(probabilistic_count.conta())

    for x in gera_numeros_aleatorios(NUMERO_DE_ELEMENTOS):
        probabilistic_count.adiciona(x)

        tamanho += 1
        tamanhos.append(tamanho)
        respostas.append(probabilistic_count.conta())

    constroi_estimativa(tamanhos, respostas, mostra_y_label=mostra_y_label, titulo=rf"m = {M}")
    constroi_estimativa(tamanhos, respostas, 0, 2 * M, mostra_y_label=mostra_y_label, titulo=rf"m = {M}")
    constroi_erro(tamanhos, respostas, 0, 2 * M, titulo="Erro Relativo")
    constroi_erro(
        tamanhos,
        respostas,
        2 * M,
        expected_error=expected_error,
        xticks=xticks,
        vlines=vlines,
        mostra_y_label=mostra_y_label,
        titulo=rf"m = {M}",
    )


if __name__ == "__main__":
    experimento(
        M=64,
        expected_error=9.75,
        xticks=[128, 250000, 500000, 750000, 1000000],
    )
    experimento(
        M=1024,
        expected_error=2.5,
        xticks=[2048, 250000, 500000, 750000, 1000000],
        mostra_y_label=False,
    )
