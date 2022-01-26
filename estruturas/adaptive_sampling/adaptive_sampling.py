from typing import Set


class AdaptiveSampling:
    def __init__(self, m=64, L=64):
        self.delta: int = 0
        self.m: int = m
        self.L: int = L
        self.LIST: Set[int] = set()

    def zeros_no_prefixo(self, x: int):
        return (x & -x).bit_length() - 1

    def adiciona(self, x: int):
        if x not in self.LIST and self.zeros_no_prefixo(x) >= self.delta:
            self.LIST.add(x)

        while len(self.LIST) > self.m:
            self.delta = self.delta + 1
            temp: Set[int] = set()

            for y in self.LIST:
                if self.zeros_no_prefixo(y) >= self.delta:
                    temp.add(y)

            self.LIST = temp

    def conta(self):
        return (1 << self.delta) * len(self.LIST)
