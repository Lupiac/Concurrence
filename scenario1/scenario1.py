import random

from common import constante
from common.drawer.drawer import Drawer
from common.map.map import Map
from common.point import Point
from common.user import User
from scenario1.map.map_builder import MapBuilder
from scenario1.user_manager.user_manager import UserManager


class Scenario1:

    def __init__(self, nb_personne, draw_is_enable):
        self.nb_personne = nb_personne
        self.draw_is_enable = draw_is_enable
        self.map = Map(MapBuilder())
        self.drawer = Drawer(self.map.cases) if draw_is_enable == True else None
        self.users = self.init_users()
        self.managers = self.init_manager()

    def launch(self):
        for i in range(len(self.managers)):
            self.managers[i].start()
        for i in range(len(self.managers)):
            self.managers[i].join()
        if self.draw_is_enable:
            import pygame
            pygame.quit()

    def init_users(self):
        users = []
        for i in range(self.nb_personne):
            point = self.get_valid_position()
            users.append(User(point.X, point.Y, User.POSSIBLE_COLOR[random.randint(0, 3)]))
            if self.draw_is_enable:
                self.drawer.add_user(Point(users[i].X, users[i].Y), users[i].color)
        return users

    def get_valid_position(self):
        while True:
            random_point = Point(random.randint(0, 511), random.randint(0, 127))
            if self.map.cases[random_point.X][random_point.Y].value == constante.EMPTY:
                return random_point

    def init_manager(self):
        managers = []
        for user in self.users:
            managers.append(UserManager(user, self.map.cases, self.drawer, self.draw_is_enable))
        return managers
