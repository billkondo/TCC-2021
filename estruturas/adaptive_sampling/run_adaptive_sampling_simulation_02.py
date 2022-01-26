import json
import random
import time
from multiprocessing import Pool

from ..random_number_generator import gera_numeros_aleatorios
from .adaptive_sampling import AdaptiveSampling

PROCESSES = 8
NUMERO_DE_EXPERIMENTOS = 8
NUMERO_DE_ELEMENTOS = 1000000
M = 64


def experimento(seed: int):
    random.seed(seed)

    adaptive_sampling = AdaptiveSampling(M)
    for x in gera_numeros_aleatorios(NUMERO_DE_ELEMENTOS):
        adaptive_sampling.adiciona(x)

    return adaptive_sampling.conta()


if __name__ == "__main__":
    start_time = time.time()

    with Pool(PROCESSES) as pool:
        respostas = pool.map(experimento, range(0, NUMERO_DE_EXPERIMENTOS))

    frequencias = {}
    for respota in respostas:
        frequencias[respota] = frequencias.get(respota, 0) + 1

    with open(f"adaptive_sampling_simulation_02_{M}.json", "w") as output:
        json.dump(frequencias, output)

    print(time.time() - start_time)
