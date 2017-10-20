import pygame


class Drawer:
    # Define some colors
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)

    # Define color of element
    OBSTACLE_COLOR = BLACK
    PEOPLE_COLOR = BLUE
    EXIT_COLOR = GREEN

    # Multiplicateur
    X_MULT = 3
    Y_MULT = 7

    # CONSTRUCTEUR
    def __init__(self, obstacles):
        self.obstacles = obstacles
        pygame.init()
        size = (512 * self.X_MULT, 128 * self.Y_MULT)
        self.screen = pygame.display.set_mode(size)
        self.screen.fill(self.WHITE)
        self.draw_exit()
        self.draw_obstacle()
        pygame.display.flip()

    def draw_obstacle(self):
        for i, val in enumerate(self.obstacles):
            pygame.draw.rect(
                self.screen,
                self.BLACK,
                [val.point.X * self.X_MULT, val.point.Y * self.Y_MULT, val.width * self.X_MULT, val.height * self.Y_MULT]
            )

    def draw_user(self, old_position, new_position):
        pygame.draw.rect(self.screen, self.WHITE, [old_position.X * self.X_MULT, old_position.Y * self.Y_MULT, self.X_MULT, self.Y_MULT])
        pygame.draw.rect(self.screen, self.BLUE, [new_position.X * self.X_MULT, new_position.Y * self.Y_MULT, self.X_MULT, self.Y_MULT])
        pygame.display.flip()

    def draw_exit(self):
        pygame.draw.rect(self.screen, self.GREEN, [0, 0, 2 * self.X_MULT, 2 * self.Y_MULT])