import constante
from Obstacle import Obstacle
from random import seed
from threading import Semaphore
from terrain import Terrain


class TerrainBuilder:

    def __init__(self):
        self.terrain = None
        self.locks = None
        self.obstacles = None

    def build(self):
        self.terrain = [[0 for x in range(constante.WIDTH)] for y in range(constante.HEIGHT)]
        self.locks = [[Semaphore(1) for i in range(128)] for j in range(528)]
        self.obstacles = [None] * 15
        self.add_obstacles()
        self.add_exit()
        return Terrain(self.terrain, self.locks, self.obstacles)

    def add_obstacle(self, obstacle):
        for w in range(obstacle.width):
            for h in range(obstacle.heigh):
                self.terrain[obstacle.y + h][obstacle.x + w] = constante.OBSTACLE

    def add_obstacles(self):
        seed(5256)
        for i in range(0, 15):
            obstacle = Obstacle()
            while obstacle is not None and not self.obstacle_is_valid(obstacle):
                obstacle = Obstacle()
            self.add_obstacle(obstacle)
            self.obstacles[i] = obstacle

    def add_exit(self):
        for i in range(0, 2):
            for j in range(0, 2):
                self.terrain[i][j] = constante.EXIT

    def obstacle_is_valid(self, obstacle):
        return (not self.verify_if_near_to_border(obstacle)) and not self.verify_if_on_other_obstacle(obstacle) \
               and self.verify_bottom_side(obstacle) and self.verify_top_side(obstacle) and \
               self.verify_left_side(obstacle) and self.verify_right_side(obstacle)

    def verify_if_on_other_obstacle(self, obstacle):
        for h in range(obstacle.heigh):
            for w in range(0, obstacle.width):
                if self.terrain[obstacle.y + h][obstacle.x + w] != constante.EMPTY:
                    return True
        return False

    def verify_if_near_to_border(self, obstacle):
        if (obstacle.x <= 1 or obstacle.x >= 510) or (obstacle.y <= 1 or obstacle.y >= 126) \
                or obstacle.x + obstacle.width >= 510 or obstacle.y + obstacle.heigh >= 126:
            return True
        return False

        # Verifie si le cote gauche de l'obstacle ne touche aucun autre elements

    def verify_left_side(self, obstacle):
        for h in range(obstacle.heigh):
            if self.terrain[obstacle.y + h][obstacle.x] != constante.EMPTY:
                return False
        return True

        # Verfie si le cote droite de l'obstacle ne touche aucun autre elements

    def verify_right_side(self, obstacle):
        for h in range(obstacle.heigh):
            if self.terrain[obstacle.y + h][obstacle.x + obstacle.width] != constante.EMPTY:
                return False
        return True

        # Verifie si le haut de l'obstale ne touche aucun autre elements

    def verify_top_side(self, obstacle):
        for w in range(obstacle.width):
            if self.terrain[obstacle.y][obstacle.x + w] != constante.EMPTY:
                return False
        return True

        # Verifie si le bat de l'obstacle ne touche aucun autre elements

    def verify_bottom_side(self, obstacle):
        for w in range(obstacle.width):
            if self.terrain[obstacle.y + obstacle.heigh][obstacle.x + w] != constante.EMPTY:
                return False
        return True
