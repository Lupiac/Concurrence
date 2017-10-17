OBSTACLE_1 = []

WIDTH = 512
HEIGHT = 128


# LE HAUT DU TERRAIN EST A L INDEX 0,0
def init_terrain():
    print "Initialisation du terrain"
    terrain = [[0 for x in range(HEIGHT)] for y in range(WIDTH)]

    return terrain

if __name__ == '__main__':
    terrain = init_terrain()
