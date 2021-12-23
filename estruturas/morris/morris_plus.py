from morris import Morris


class MorrisPlus:
    def __init__(self, t: int):
        self._t = t
        self._morris = [Morris() for _ in range(0, self._t)]

    def adiciona(self):
        for i in range(0, self._t):
            self._morris[i].adiciona()

    def conta(self) -> int:
        sum = 0

        for i in range(0, self._t):
            sum += self._morris[i].conta()

        return sum // self._t
