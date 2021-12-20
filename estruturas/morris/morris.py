from random import randint


class Morris:
    def __init__(self):
        self.X = 0

    def adiciona(self):
        r = randint(0, 2 ** self.X - 1)
        if r == 0:
            self.X = self.X + 1

    def conta(self):
        return 2 ** self.X - 1
