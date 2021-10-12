from typing import List


class AdaptiveSampling:
    def __init__(self, m=64, L=64):
        self.depth: int = 0
        self.m: int = m
        self.L: int = L
        self.list: List[int] = []

    @property
    def __prefix__(self):
        return ((1 << self.L) - 1) ^ ((1 << self.depth) - 1)

    def add(self, x: int):
        if x not in self.list and (x & self.__prefix__) == x:
            self.list.append(x)

        while len(self.list) > self.m:
            self.depth = self.depth + 1
            temp: List[int] = []

            for y in self.list:
                if (self.__prefix__ & y) == y:
                    temp.append(y)

            self.list = temp

    def count(self):
        return (1 << self.depth) * len(self.list)
