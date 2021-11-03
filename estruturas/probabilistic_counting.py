from math import floor
from typing import List


class ProbabilisticaCounting:
    def __init__(self, m=64, L=32):
        self.m: int = m
        self.L: int = L
        self.magic = 0.77351

        self.BITMAP: List[List[int]] = []
        for i in range(0, self.m):
            self.BITMAP.append([None] * self.L)

        self.R: List[int] = [0] * self.m

    def p(self, x: int):
        return (x & -x).bit_length() - 1

    def add(self, x: int):
        k = x % self.m
        y = x // self.m

        self.BITMAP[k][self.p(y)] = 1

        while self.BITMAP[k][self.R[k]] == 1:
            self.R[k] += 1

    def count(self):
        R = 0
        for r in self.R:
            R += r

        R = R / self.m

        return floor((self.m * pow(2, R)) / self.magic)
