import random
from user import User
from point import Point
from threading import Semaphore

class UserManager:

    POSSIBLE_COLOR = [User.BLUE, User.RED, User.ORANGE, User.PINK]

    def __init__(self, nb_user, terrain, drawer, draw_is_enable):
        self.terrain = terrain
        self.nb_user = nb_user
        self.users = [None] * nb_user
        random.seed(187852)

        for i in range(0, nb_user):
            point = self.get_valid_position()

            self.users[i] = User(point, terrain, drawer, draw_is_enable, self.POSSIBLE_COLOR[random.randint(0, 3)])
            if draw_is_enable:
                drawer.add_user(self.users[i].position, self.users[i].color)

    def start_users(self):
        for i in range(0, self.nb_user):
            self.users[i].start()

    def join_users(self):
        for i in range(0, self.nb_user):
            self.users[i].join()

    def get_valid_position(self):
        while True:
            random_point = Point(random.randint(0, 511), random.randint(0, 127))
            if self.terrain.can_moove_to(random_point):
                return random_point