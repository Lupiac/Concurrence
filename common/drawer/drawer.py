from threading import Semaphore

import pygame
from common import constante


class Drawer:
    # Define some colors
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)
    ORANGE = (255,165,0)
    PINK = (255,105,180)

    # Define color of element
    EMPTY = 0
    PEOPLE = 1
    OBSTACLE = 2

    OBSTACLE_COLOR = BLACK
    PEOPLE_COLOR = BLUE
    EXIT_COLOR = GREEN
    ELEMENT_COLOR = [WHITE, None, OBSTACLE_COLOR, EXIT_COLOR]

    # Multiplicateur
    X_MULT = 3
    Y_MULT = 5

    def __init__(self, cases):
        pygame.init()
        size = (512 * self.X_MULT, 128 * self.Y_MULT)
        self.screen = pygame.display.set_mode(size)
        self.sem = Semaphore(1)
        for w in range(constante.WIDTH):
            for h in range(constante.HEIGHT):
                pygame.draw.rect(
                    self.screen,
                    self.ELEMENT_COLOR[cases[w][h].value],
                    [w * self.X_MULT, h * self.Y_MULT, self.X_MULT, self.Y_MULT]
                )
        pygame.display.flip()

    def draw_user(self, old_position, new_position, color):
        self.sem.acquire()
        pygame.draw.rect(self.screen, self.WHITE, [old_position.X * self.X_MULT, old_position.Y * self.Y_MULT, self.X_MULT, self.Y_MULT])
        pygame.draw.rect(self.screen, color, [new_position.X * self.X_MULT, new_position.Y * self.Y_MULT, self.X_MULT, self.Y_MULT])
        pygame.display.flip()
        self.sem.release()

    def draw_exit(self):
        pygame.draw.rect(self.screen, self.GREEN, [0, 0, 2 * self.X_MULT, 2 * self.Y_MULT])

    def add_user(self, position, color):
        pygame.draw.rect(self.screen, color, [position.X * self.X_MULT, position.Y * self.Y_MULT, self.X_MULT, self.Y_MULT])
        pygame.display.flip()

    def remove_user(self, position):
        self.sem.acquire()
        pygame.draw.rect(self.screen, self.WHITE, [position.X * self.X_MULT, position.Y * self.Y_MULT, self.X_MULT, self.Y_MULT])
        pygame.display.flip()
        self.sem.release()