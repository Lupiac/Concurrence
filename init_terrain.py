import constante

WIDTH = 512
HEIGHT = 128
OBSTACLE = 2
PEOPLE = 1


def print_terrain(terrain):
    for i in range(0, WIDTH):
        for j in range(0, HEIGHT):
            None


def add_obstacle(terrain, obstacle):
    for i in range(0, obstacle.height):
        for j in range(0, obstacle.width):
            terrain[obstacle.point.X + i][obstacle.point.Y + j] = OBSTACLE


def add_obstacles(terrain):
    for i, val in enumerate(constante.obstacle):
        add_obstacle(terrain, val)
        print "coucou"


# LE HAUT DU TERRAIN EST A L INDEX 0,0
def init_terrain():
    print "Initialisation du terrain"
    terrain = [[0 for x in range(HEIGHT)] for y in range(WIDTH)]
    add_obstacles(terrain)
    return terrain