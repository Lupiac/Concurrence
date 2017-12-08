import constante


class Terrain:

    def __init__(self, terrain, locks, obstacles):
        self.terrain = terrain
        self.locks = locks
        self.obstacles = obstacles

    def add_users(self, users):
        for i in range(len(users)):
            position = users[i].position
            self.terrain[position.Y][position.X] = constante.PEOPLE
            self.locks[position.X][position.Y].acquire()

    def can_moove_to(self, position):
        return constante.WIDTH > position.X >= 0 \
               and constante.HEIGHT > position.Y >= 0 \
               and self.terrain[position.Y][position.X] in [constante.EXIT, constante.EMPTY]

    def moove_to(self, old_position, new_position):
        self.terrain[old_position.Y][old_position.X] = constante.EMPTY
        if self.terrain[new_position.Y][new_position.X] == constante.EXIT:
            return True
        self.terrain[new_position.Y][new_position.X] = constante.PEOPLE
        return False