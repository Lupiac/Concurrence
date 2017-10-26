import threading
import time
from point import Point


class User(threading.Thread):
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)
    ORANGE = (255, 165, 0)
    PINK = (255, 105, 180)

    # CONSTANT
    NORTH = Point(0, -1)
    EAST = Point(-1, 0)
    NORTH_EAST = Point(-1, -1)
    SOUTH_EAST = Point(1, -1)
    POSSIBLE_MOUVEMENT = [NORTH_EAST, NORTH, EAST, SOUTH_EAST]

    # STATIC VAR
    locks = None

    def __init__(self, position, terrain, drawer, draw_is_enable, color, sem):
        super(User, self).__init__()
        self.position = position
        self.terrain = terrain
        self.drawer = drawer
        self.draw_is_enable = draw_is_enable
        self.color = color
        self.sem = sem

    def moove(self):
        for mouvement in self.POSSIBLE_MOUVEMENT:
            position_to_test = Point(self.position.X + mouvement.X, self.position.Y + mouvement.Y)
            if self.terrain.can_moove_to(position_to_test):
                finish = self.terrain.moove_to(self.position, position_to_test)
                if finish is not True:
                    if self.draw_is_enable:
                        self.drawer.draw_user(self.position, position_to_test, self.color)
                self.position = position_to_test
                return finish
        return False

    def run(self):
        finish = False
        while not finish:
            self.sem.acquire()
            finish = self.moove()
            self.sem.release()
            if self.draw_is_enable:
                time.sleep(0.005)
        exit()
