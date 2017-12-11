class User:

    RED = (255, 0, 0)
    BLUE = (0, 0, 255)
    ORANGE = (255, 165, 0)
    PINK = (255, 105, 180)
    POSSIBLE_COLOR = [BLUE, RED, ORANGE, PINK]

    def __init__(self, x, y, color):
        self.X = x
        self.Y = y
        self.color = color