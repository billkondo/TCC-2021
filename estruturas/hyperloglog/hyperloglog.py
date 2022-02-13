import math


class HyperLogLog:
    def __init__(self, m=64):
        self.m = m
        self.B = math.floor(math.log2(m))
        self.M = [0] * m
        self.Z = self.m
        self.alpha = 0.7213

    def p(self, x: int):
        return (x & -x).bit_length()

    @property
    def prefixo(self):
        return (1 << self.B) - 1

    def adiciona(self, x: int):
        lote = x & self.prefixo
        w = x >> self.B

        if self.p(w) > self.M[lote]:
            self.Z -= math.pow(2, -self.M[lote])
            self.M[lote] = self.p(w)
            self.Z += math.pow(2, -self.M[lote])

    def conta(self):
        return math.floor(self.alpha * self.m * self.m / self.Z)
