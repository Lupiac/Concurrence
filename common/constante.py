from common.point import Point

WIDTH = 512
HEIGHT = 128
EMPTY = 0
PEOPLE = 1
OBSTACLE = 2
EXIT = 3

# MOUVEMENT
NORTH = Point(0, -1)
EAST = Point(-1, 0)
NORTH_EAST = Point(-1, -1)
SOUTH_EAST = Point(-1, 1)
POSSIBLE_MOUVEMENT = [NORTH_EAST, NORTH, EAST, SOUTH_EAST]
