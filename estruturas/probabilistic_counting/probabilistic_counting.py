from math import floor
from typing import List


class ProbabilisticaCounting:
    def __init__(self, m=64, L=64):
        self.m: int = m
        self.L: int = L
        self.phi = 0.77351
        self.BITMAP: List[List[int]] = []

        for _ in range(0, self.m):
            self.BITMAP.append([None] * self.L)

        self.R: List[int] = [0] * self.m
        self.R_sum = 0

    def p(self, x: int):
        return (x & -x).bit_length() - 1

    def adiciona(self, x: int):
        lote = x % self.m
        y = x // self.m
        self.BITMAP[lote][self.p(y)] = 1

        while self.BITMAP[lote][self.R[lote]] == 1:
            self.R[lote] += 1
            self.R_sum += 1

    def conta(self):
        R = self.R_sum / self.m

        return floor((self.m * pow(2, R)) / self.phi)
