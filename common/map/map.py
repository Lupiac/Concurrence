from common import constante


class Map:

    def __init__(self, map_builder):
        self.cases = map_builder.cases

    def add_user(self, user):
        self.cases[user.X][user.Y].value = constante.PEOPLE