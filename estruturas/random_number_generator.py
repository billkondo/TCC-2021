import random


def gera_numeros_aleatorios(N, L=64):
    generated_numbers = set()
    MAX_NUMBER = (1 << L) - 1

    while len(generated_numbers) < N:
        number = random.randint(0, MAX_NUMBER)

        if number in generated_numbers:
            continue

        generated_numbers.add(number)
        yield number
