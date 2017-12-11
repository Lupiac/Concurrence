from random import randint


class Obstacle:

    def __init__(self):
        self.X = randint(2, 510)
        self.Y = randint(2, 126)
        self.height = randint(10, 30)
        self.width = randint(10, 30)