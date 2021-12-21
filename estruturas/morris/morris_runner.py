import random
from typing import List

import matplotlib
import matplotlib.pyplot as plt

from morris import Morris

matplotlib.rcParams["text.usetex"] = True


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
            dashes=[2, 2, 10, 2],
            label=r"$n$",
        )

    # Gráfico do Algoritmo Morris
    ax.plot(
        contadores_esperados[inicio:fim],
        contadores_devolvidos_por_morris[inicio:fim],
        label=r"$\hat{n}$",
    )

    if vlines:
        ax.set_xticks(vlines)

    for vline in vlines:
        ax.axvline(x=vline, c="r", ls=":")

    ax.legend()
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
    )

    ax.legend()
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
        erro_relativo.append((morris.conta() - i) / i)

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
