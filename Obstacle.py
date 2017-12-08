from random import randint


class Obstacle:
    def __init__(self):
        self.x = randint(2, 510)
        self.y = randint(2, 126)
        self.heigh = randint(10, 30)
        self.width = randint(10, 30)