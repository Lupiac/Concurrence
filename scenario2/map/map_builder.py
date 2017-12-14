from common.map.case import Case
from common.map.lock_case import LockCase
from common.map.obstacle.obstacle_builder import ObstacleBuilder
from common import constante


class MapBuilder:

    def __init__(self):
        self.obstacle_builder = ObstacleBuilder()
        self.cases = self.init_normal_cases()
        self.init_lock_case()
        self.init_exit()
        self.init_obstacle()

    def init_lock_case(self):
        half_height = int(constante.HEIGHT / 2)
        half_width = int(constante.WIDTH / 2)
        for w in range(constante.WIDTH):
            self.cases[w][half_height - 1] = LockCase(constante.EMPTY)
        for h in range(constante.HEIGHT):
            self.cases[half_width - 1][h] = LockCase(constante.EMPTY)

    def init_normal_cases(self):
        return [[Case(constante.EMPTY) for x in range(constante.HEIGHT)] for y in range(constante.WIDTH)]

    def init_obstacle(self):
        self.obstacle_builder.set_seed(5252)
        for i in range(0, 15):
            self.obstacle_builder.create_obstacle(self.cases)

    def init_exit(self):
        for i in range(0, 2):
            for j in range(0, 2):
                self.cases[i][j].value = constante.EXIT
