from point import Point


class User:
    NORTH = Point(0, -1)
    EAST = Point(-1, 0)
    NORTH_EAST = Point(-1, -1)
    POSSIBLE_MOUVEMENT = [NORTH, EAST, NORTH_EAST]

    def __init__(self, position, terrain, drawer):
        self.position = position
        self.terrain = terrain
        self.drawer = drawer

    def moove(self):
        for mouvement in self.POSSIBLE_MOUVEMENT:
            position_to_test = Point(self.position.X + mouvement.X,self.position.Y + mouvement.Y)
            if self.terrain.can_moove_to(position_to_test):
                finish = self.terrain.moove_to(self.position, position_to_test)
                if finish is not True:
                    self.drawer.draw_user(self.position, position_to_test)
                self.position = position_to_test
                return finish
        return False
