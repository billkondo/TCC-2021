from morris import Morris


class MorrisPlus:
    def __init__(self, t: int):
        self.t = t
        self.morris = [Morris() for _ in range(0, self.t)]

    def adiciona(self):
        for i in range(0, self.t):
            self.morris[i].adiciona()

    def conta(self):
        sum = 0
        for i in range(0, self.t):
            sum += self.morris[i].conta()

        return sum // self.t
