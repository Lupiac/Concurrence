import random
from threading import Event

from common import constante
from common.point import Point
from common.drawer.drawer import Drawer
from common.map.map import Map
from scenario2.user_manager.bottom_left_user_manager import BotomLeftUserMangager
from scenario2.user_manager.bottom_right_user_manger import BotomRightUserMangager
from scenario2.user_manager.top_right_user_manager import TopRightUserMangager
from scenario2.user_manager.top_left_user_manager import TopLeftUserMangager
from scenario2.map.map_builder import MapBuilder
from common.user import User


class Scenario2:

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
        events = [Event(), Event(), Event(), Event()]
        finish_event = Event()

        top_left_manager = TopLeftUserMangager(self.users, self.map.cases, events, finish_event, self.drawer, self.nb_personne, self.draw_is_enable)
        top_righ_manager = TopRightUserMangager(self.users, self.map.cases, events, finish_event, self.drawer, self.draw_is_enable)
        bottom_left_manager = BotomLeftUserMangager(self.users, self.map.cases, events, finish_event, self.drawer, self.draw_is_enable)
        bottom_right_manager = BotomRightUserMangager(self.users, self.map.cases, events, finish_event, self.drawer, self.draw_is_enable)

        bottom_left_manager.set_top_left_manager(top_left_manager)
        bottom_right_manager.set_bottom_left_manager(bottom_right_manager)
        bottom_right_manager.set_top_left_manager(top_left_manager)
        bottom_right_manager.set_top_right_manager(top_righ_manager)
        top_righ_manager.set_bottom_left_manager(bottom_left_manager)
        top_righ_manager.set_bottom_right_manager(bottom_right_manager)
        top_righ_manager.set_top_left_manager(top_left_manager)

        return [top_righ_manager, top_left_manager, bottom_right_manager, bottom_left_manager]

