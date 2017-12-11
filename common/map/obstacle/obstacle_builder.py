from common.map.obstacle.obstacle import Obstacle
from common.map.obstacle.obstacle_validator import ObstacleValidator
from random import seed
from common import constante


class ObstacleBuilder:

    def __init__(self):
        self.obstacleValidator = ObstacleValidator()

    def set_seed(self, seedNumber):
        seed(seedNumber)

    def create_obstacle(self, cases):
        obstacle = Obstacle()
        while obstacle is not None and not self.obstacleValidator.is_valid(obstacle, cases):
            obstacle = Obstacle()
        self.add_obstacle(obstacle, cases)

    def add_obstacle(self, obstacle, cases):
        for w in range(obstacle.width):
            for h in range(obstacle.height):
                cases[obstacle.X + w][obstacle.Y + h].value = constante.OBSTACLE
