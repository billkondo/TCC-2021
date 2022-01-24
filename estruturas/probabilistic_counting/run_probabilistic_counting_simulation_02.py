import json
import random
import time
from multiprocessing import Pool

from ..random_number_generator import gera_numeros_aleatorios
from .probabilistic_counting import ProbabilisticaCounting

PROCESSES = 8
NUMERO_DE_EXPERIMENTOS = 8
NUMERO_DE_ELEMENTOS = 1000000
M = 1024


def experimento(seed: int):
    random.seed(seed)

    probabilistic_counting = ProbabilisticaCounting(M)
    for x in gera_numeros_aleatorios(NUMERO_DE_ELEMENTOS):
        probabilistic_counting.adiciona(x)

    return probabilistic_counting.conta()


if __name__ == "__main__":
    start_time = time.time()

    with Pool(PROCESSES) as pool:
        respostas = pool.map(experimento, range(0, NUMERO_DE_EXPERIMENTOS))

    frequencias = {}
    for respota in respostas:
        frequencias[respota] = frequencias.get(respota, 0) + 1

    with open(f"probabilistic_counting_simulation_02_{M}.json", "w") as output:
        json.dump(frequencias, output)

    print(time.time() - start_time)
