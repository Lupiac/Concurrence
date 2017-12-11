# import getopt
#
# import time
# import psutil
# from scenario1.terrainBuilder import TerrainBuilder
# from scenario1.user_mangager import UserManager
# import sys
#
# from simulation_launcher import SimulationLauncher
#
#
# def launch_simulation(draw_is_enable, nb_user):
#     drawer = None
#     terrain = TerrainBuilder().build()
#     if draw_is_enable:
#         import pygame
#         from scenario1.drawer import Drawer
#         drawer = Drawer(terrain.obstacles)
#     user_manager = UserManager(nb_user, terrain, drawer, draw_is_enable)
#     terrain.add_users(user_manager.users)
#
#     psutil.cpu_percent(interval=None)
#     user_manager.start_users()
#     start_time = time.time()
#     user_manager.join_users()
#     if draw_is_enable:
#         pygame.quit()
#     cpu_usage = psutil.cpu_percent(interval=None)
#     elapsed_time = time.time() - start_time
#     return cpu_usage, elapsed_time
#
#
# def parse_arg(argv):
#     p = 2 ** 9
#     t = 0
#     m = False
#     i = False
#
#     try:
#         opts, args = getopt.getopt(argv, "ip:t:m", [])
#     except getopt.GetoptError:
#         # usage()
#         sys.exit(2)
#     for opt, arg in opts:
#         if opt in ("-h", "--help"):
#             p = -1
#             # usage()
#             sys.exit()
#         elif opt == "-p":
#             p = 2 ** int(arg)
#
#         elif opt == "-t":
#             t = int(arg)
#         elif opt == "-m":
#             m = True
#         elif opt == "-i":
#             i = True
#     return p, t, m, i
#
#
# def launch_metrics(nb_person):
#     cpu_usage_average = 0
#     time_elapse_average = 0
#     for i in range(0, 5):
#         metrics = launch_simulation(False, nb_person)
#         cpu_usage_average += metrics[0]
#         time_elapse_average += metrics[1]
#     print("cpu usage : " + str(cpu_usage_average / 5))
#     print("time elapse : " + str(time_elapse_average / 5))
import sys

from simulation_launcher import SimulationLauncher

if __name__ == '__main__':
    simulation_launcher = SimulationLauncher(sys.argv[1:])
    simulation_launcher.launch()
