import constante
from random import seed
from random import randint


class Terrain:
    cpt = 1

    def __init__(self):
        self.terrain = [[0 for x in range(constante.HEIGHT)] for y in range(constante.WIDTH)]
        self.obstacles = [None]*15
        self.add_obstacles()
        self.add_exit()

    # Generation et Ajout d'obstacle
    def add_obstacle(self, obstacle):

        for i in range(0, obstacle[2]):
            for j in range(0, obstacle[3]):
                self.terrain[obstacle[0] + i][obstacle[1] + j] = constante.OBSTACLE


    def add_obstacles(self):
        seed(5256)
        for i in range(0, 15):
            obstacle = (randint(2, 510), randint(2, 126), randint(10, 30), randint(10, 30))
            while obstacle is not None and not self.obstacle_is_valid(obstacle):
                obstacle = (randint(2, 510), randint(2, 126), randint(10, 30), randint(10, 30))
            self.add_obstacle(obstacle)
            self.obstacles[i] = obstacle
            print(i)

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

    def obstacle_is_valid(self, obstacle):
        return (not self.verify_if_near_to_border(obstacle)) and not self.verify_if_on_other_obstacle(obstacle)\
               and self.verify_bottom_side(obstacle) and self.verify_top_side(obstacle) and \
               self.verify_left_side(obstacle) and self.verify_right_side(obstacle)


    def verify_if_on_other_obstacle(self, obstacle):
        for i in range(0, obstacle[2]):
            for j in range(0, obstacle[3]):
                if self.terrain[obstacle[0] + i][obstacle[1] + j] != constante.EMPTY:
                    return True
        return False

    def verify_if_near_to_border(self, obstacle):
        # print(obstacle)
        if (obstacle[0] <= 1 or obstacle[0] >= 510) or (obstacle[1] <= 1 or obstacle[1] >= 126)\
                or obstacle[0] + obstacle[2] >= 510 or obstacle[1] + obstacle[3] >= 126:
            return True
        return False

    def verify_left_side(self, obstacle):
        for i in range(0, obstacle[3]):
            if self.terrain[obstacle[0]][obstacle[1] + i] != constante.EMPTY:
                return False
        return True

    def verify_right_side(self, obstacle):
        for i in range(0, obstacle[3]):
            if self.terrain[obstacle[0] + obstacle[2]][obstacle[1] + i] != constante.EMPTY:
                return False
        return True

    def verify_top_side(self, obstacle):
        for i in range(0, obstacle[2]):
            if self.terrain[obstacle[0] + i][obstacle[1]] != constante.EMPTY:
                return False
        return True

    def verify_bottom_side(self, obstacle):
        print(obstacle)
        for i in range(0, obstacle[2]):
            print(i)
            if self.terrain[obstacle[0] + i][obstacle[1] + obstacle[3]] != constante.EMPTY:
                return False
        return True
