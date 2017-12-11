import getopt

import sys


class ArgumentParser:

    def parse(self, argv):
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