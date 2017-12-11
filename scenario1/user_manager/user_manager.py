import threading

import time

from common import constante
from common.point import Point


class UserManager(threading.Thread):

    def __init__(self, user, cases, drawer, draw_is_enable):
        super().__init__()
        self.user = user
        self.cases = cases
        self.drawer = drawer
        self.draw_is_enable = draw_is_enable

    def run(self):
        finish = False
        while not finish:
            finish = self.moove()
        exit()

    def is_valid(self, X, Y):
        return 0 <= X < constante.WIDTH and constante.HEIGHT > Y >= 0

    def moove(self):
        for mouvement in constante.POSSIBLE_MOUVEMENT:
            X = self.user.X + mouvement.X
            Y = self.user.Y + mouvement.Y
            if self.is_valid(X, Y):
                case = self.cases[X][Y]
                case.lock()
                if self.can_moove(X, Y):
                    current_case = self.cases[self.user.X][self.user.Y]
                    current_case.lock()
                    finish = case.value == constante.EXIT
                    if not finish:
                        case.value = constante.PEOPLE
                    current_case.value = constante.EMPTY
                    case.unlock()
                    current_case.unlock()
                    if not finish:
                        self.update_graphique(self.user, X, Y)
                    else:
                        self.remove_user()
                    self.user.X = X
                    self.user.Y = Y
                    return finish
                case.unlock()
        return False

    def can_moove(self, X, Y):
        return self.cases[X][Y].value == constante.EMPTY or self.cases[X][Y].value == constante.EXIT

    def update_graphique(self, user, X, Y):
        if self.draw_is_enable:
            old_point = Point(user.X, user.Y)
            new_point = Point(X, Y)
            self.drawer.draw_user(old_point, new_point, user.color)

    def remove_user(self):
        if self.draw_is_enable:
            self.drawer.remove_user(Point(self.user.X, self.user.Y))
            time.sleep(0.05)

