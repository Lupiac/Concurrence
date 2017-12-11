import threading
from common import constante
from common.point import Point


class BotomRightUserMangager(threading.Thread):

    def __init__(self, users, cases, events, finish_event, drawer, draw_is_enable):
        super().__init__()
        self.cases = cases
        self.users = []
        self.draw_is_enable = draw_is_enable
        self.events = events
        self.drawer = drawer
        self.top_left_manager = None
        self.top_right_manager = None
        self.bottom_left_manager = None
        self.finish_event = finish_event
        for i in range(len(users)):
            user = users[i]
            if self.case_is_in_my_responsability(user.X, user.Y):
                self.users.append(user)

    def set_top_left_manager(self, top_left_manager):
        self.top_left_manager = top_left_manager

    def set_top_right_manager(self, top_right_manager):
        self.top_right_manager = top_right_manager

    def set_bottom_left_manager(self, bottom_left_manager):
        self.bottom_left_manager = bottom_left_manager

    def case_is_in_my_responsability(self, X, Y):
        return X >= constante.WIDTH / 2 and Y >= constante.HEIGHT / 2

    def can_moove(self, X, Y):
        return X >= 0 and Y >= 0 and self.cases[X][Y].value == constante.EMPTY

    def give_user(self, user):
        self.users.remove(user)
        if len(self.users) <= 0:
            self.events[3].clear()
        if user.X < constante.WIDTH / 2 and user.Y >= constante.HEIGHT / 2:
            self.bottom_left_manager.users.append(user)
            self.events[2].set()
        elif user.X < constante.WIDTH / 2 and user.Y < constante.HEIGHT / 2:
            self.top_left_manager.users.append(user)
            self.events[0].set()
        elif user.X >= constante.WIDTH / 2 and user.Y < constante.HEIGHT / 2:
            self.top_right_manager.users.append(user)
            self.events[1].set()

    def moove_user(self, user):
        for mouvement in constante.POSSIBLE_MOUVEMENT:
            X = user.X + mouvement.X
            Y = user.Y + mouvement.Y
            case = self.cases[X][Y]
            case.lock()
            if self.can_moove(X, Y):
                current_case = self.cases[user.X][user.Y]
                current_case.lock()
                case.value = constante.PEOPLE
                self.cases[user.X][user.Y].value = constante.EMPTY
                current_case.unlock()
                case.unlock()
                self.update_graphique(user, X, Y)
                user.X = X
                user.Y = Y
                if not self.case_is_in_my_responsability(X, Y):
                    self.give_user(user)
                return
            case.unlock()

    def moove_users(self):
        for user in self.users:
            self.moove_user(user)

    def run(self):
        while True:
            while len(self.users) <= 0:
                if self.finish_event.isSet():
                    exit(1)
                else:
                    self.events[3].wait()
            self.moove_users()

    def update_graphique(self, user, X, Y):
        if self.draw_is_enable:
            old_point = Point(user.X, user.Y)
            new_point = Point(X, Y)
            self.drawer.draw_user(old_point, new_point, user.color)
