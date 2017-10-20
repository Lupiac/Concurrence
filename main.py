import constante
import time
import psutil
from terrain import Terrain
from user_mangager import UserManager


def launch_simulation(draw_is_enable, nb_user):
    drawer = None
    if draw_is_enable:
        import pygame
        from drawer import Drawer
        drawer = Drawer(constante.obstacle)
    terrain = Terrain()
    user_manager = UserManager(nb_user, terrain, drawer, draw_is_enable)
    time.sleep(10)
    psutil.cpu_percent(interval=None)
    user_manager.start_users()
    start_time = time.time()
    user_manager.join_users()
    if draw_is_enable:
        pygame.quit()
    cpu_usage = psutil.cpu_percent(interval=None)
    elapsed_time = time.time() - start_time
    print cpu_usage
    print elapsed_time
    return cpu_usage, elapsed_time


if __name__ == '__main__':
    # launch_simulation(True, 300)
    cpu_usage_average = 0
    time_elapse_average = 0
    for i in range(0, 5):
        metrics = launch_simulation(False, 256)
        cpu_usage_average += metrics[0]
        time_elapse_average += metrics[1]
    print "cpu usage : " + str(cpu_usage_average / 5)
    print "time elapse : " + str(time_elapse_average / 5)
