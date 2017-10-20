import constante
import pygame
import time
from drawer import Drawer
from terrain import Terrain
from user import User
from point import Point


def launch_simulation():
    drawer = Drawer(constante.obstacle)
    terrain = Terrain()
    user = User(Point(500, 100), terrain, drawer)
    finish = False
    while not finish:
        finish = user.moove()
        time.sleep(0.0005)
    pygame.quit()


if __name__ == '__main__':
    launch_simulation()
