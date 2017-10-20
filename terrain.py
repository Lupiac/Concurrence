import constante


class Terrain:
    def __init__(self):
        self.terrain = [[0 for x in range(constante.HEIGHT)] for y in range(constante.WIDTH)]
        self.add_obstacles()
        self.add_exit()

    def add_obstacle(self, obstacle):
        for i in range(0, obstacle.width):
            for j in range(0, obstacle.height):
                self.terrain[obstacle.point.X + i][obstacle.point.Y + j] = constante.OBSTACLE

    def add_obstacles(self):
        for i, val in enumerate(constante.obstacle):
            self.add_obstacle(val)

    def add_exit(self):
        for i in range(0, 2):
            for j in range(0, 2):
                self.terrain[i][j] = constante.EXIT

    def can_moove_to(self, position):
        return 512 > position.X >= 0 \
               and 512 > position.Y >= 0 \
               and self.terrain[position.X][position.Y] in [constante.EXIT, constante.EMPTY]

    def moove_to(self, old_position, new_position):
        self.terrain[old_position.X][old_position.Y] = constante.EMPTY
        if self.terrain[new_position.X][new_position.Y] == constante.EXIT:
            return True
        self.terrain[new_position.X][new_position.Y] = constante.PEOPLE
        return False
