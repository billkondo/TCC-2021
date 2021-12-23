import json
import random
from multiprocessing import Pool

from morris_plus import MorrisPlus

NUMERO_DE_THREADS = 8
NUMERO_DE_EXPERIMENTOS = 1000
TAMANHO_DO_CONJUNTO = 1000000
T = 10


def executa_experimento(seed):
    random.seed(seed)

    morris_plus = MorrisPlus(T)
    for _ in range(0, TAMANHO_DO_CONJUNTO):
        morris_plus.adiciona()

    print(f"Experimento {seed} concluído")

    return morris_plus.conta()


if __name__ == "__main__":
    pool = Pool(NUMERO_DE_THREADS)
    tamanhos = pool.map(executa_experimento, range(0, NUMERO_DE_EXPERIMENTOS))

    frequencia_dos_contadores = {}
    for tamanho in tamanhos:
        frequencia_dos_contadores[tamanho] = frequencia_dos_contadores.get(tamanho, 0) + 1

    arquivo_de_saida = open("morris_plus_variance.json", "w")

    json.dump(
        frequencia_dos_contadores,
        arquivo_de_saida,
        indent=4,
    )

    arquivo_de_saida.close()
