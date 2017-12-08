import threading
import time
from threading import Semaphore

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
    graphic_lock = Semaphore(1)

    def __init__(self, position, terrain, drawer, draw_is_enable, color):
        super(User, self).__init__()
        self.position = position
        self.terrain = terrain
        self.drawer = drawer
        self.draw_is_enable = draw_is_enable
        self.color = color

    def moove(self):
        for mouvement in self.POSSIBLE_MOUVEMENT:
            position_to_test = Point(self.position.X + mouvement.X, self.position.Y + mouvement.Y)
            if self.is_a_valid_position(position_to_test):
                self.terrain.locks[position_to_test.X][position_to_test.Y].acquire()
                if self.terrain.can_moove_to(position_to_test):
                    finish = self.terrain.moove_to(self.position, position_to_test)
                    self.terrain.locks[position_to_test.X][position_to_test.Y].release()
                    self.update_graphic(finish, position_to_test)
                    self.position = position_to_test
                    return finish
                self.terrain.locks[position_to_test.X][position_to_test.Y].release()
        return False

    def update_graphic(self, finish, position_to_test):
        if self.draw_is_enable:
            self.graphic_lock.acquire()
            if finish is not True:
                self.drawer.draw_user(self.position, position_to_test, self.color)
            else:
                self.drawer.remove_user(self.position)
            self.graphic_lock.release()
            time.sleep(0.05)

    def is_a_valid_position(self, position):
        return position.X >= 0 and position.Y >= 0

    def run(self):
        finish = False
        i = 0
        while not finish:
            i += 1
            finish = self.moove()
        exit()
