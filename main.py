import init_terrain
import pygame


def launch_simulation():
    terrain = init_terrain.init_terrain()


if __name__ == '__main__':
    pygame.init()
    launch_simulation()
