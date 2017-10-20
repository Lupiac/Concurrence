import getopt

import constante
import pygame
import time
from drawer import Drawer
from terrain import Terrain
from user import User
from point import Point
import sys


def launch_simulation():
    drawer = Drawer(constante.obstacle)
    terrain = Terrain()
    user = User(Point(500, 100), terrain, drawer)
    finish = False
    while not finish:
        finish = user.moove()
        time.sleep(0.005)
    pygame.quit()


def parse_arg(argv):
    p = 2 ** 9
    t = 0
    m = False
    i = False

    try:
        opts, args = getopt.getopt(argv, "ip:t:m", [])
    except getopt.GetoptError:
        # usage()
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            p = -1
            # usage()
            sys.exit()
        elif opt == "-p":
            p = 2 ** int(arg)

        elif opt == "-t":
            t = int(arg)
        elif opt == "-m":
            m = True
        elif opt == "-i":
            i = True
    return p, t, m, i

def main(argv):
    arg = parse_arg(argv)
    P = arg[0]
    T = arg[1]
    M = arg[2]
    INTERFACE = arg[3]
    print P, T, M, INTERFACE
    # launch_simulation()

if __name__ == '__main__':
    main(sys.argv[1:])

