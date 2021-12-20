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
):
    _, ax = plt.subplots()

    # Gráfico da saída esperada
    ax.plot(
        contadores_esperados[:tamanho],
        contadores_esperados[:tamanho],
        dashes=[2, 2, 10, 2],
        label=r"$n$",
    )

    # Gráfico do Algoritmo Morris
    ax.plot(
        contadores_esperados[:tamanho],
        contadores_devolvidos_por_morris[:tamanho],
        label=r"$\hat{n}$",
    )

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

    tamanhos = [100, 1000, 1000000]
    for tamanho in tamanhos:
        constroi_grafico(contadores_esperados, contadores_devolvidos_por_morris, tamanho)
        constroi_grafico_erro_relativo(erro_relativo, tamanho)
