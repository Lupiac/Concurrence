import sys

import time

from argument_parser import ArgumentParser
from scenario1.scenario1 import Scenario1
from scenario2.scenario2 import Scenario2


class SimulationLauncher:

    def __init__(self, argv):
        arg_parser = ArgumentParser()
        arg = arg_parser.parse(sys.argv[1:])
        self.nb_person = arg[0]
        self.simulation_type = arg[1]
        self.metrics_enable = arg[2]
        self.scenario = None

    def init_scenario(self):
        if self.simulation_type == 0:
            return Scenario1(self.nb_person, not self.metrics_enable)
        elif self.simulation_type == 1:
            return Scenario2(self.nb_person, not self.metrics_enable)
        else:
            print("Argument -t error")
            exit(-1)

    def launch(self):
        if self.metrics_enable:
            self.launch_with_metrics()
        else:
            self.launch_without_metrics()

    def launch_with_metrics(self):
        time_avg = 0
        time_avg_clock = 0
        for i in range(5):
            self.scenario = self.init_scenario()
            start_time_clock = time.process_time()
            start_time = time.time()
            self.scenario.launch()
            elapsed_time_clock = time.process_time() - start_time_clock
            elapsed_time = time.time() - start_time
            time_avg += elapsed_time
            time_avg_clock += elapsed_time_clock
        time_avg = time_avg / 5
        time_avg_clock = time_avg_clock / 5
        print("average time : " + str(time_avg))
        print("average clock time : " + str(time_avg_clock))


    def launch_without_metrics(self):
        self.scenario = self.init_scenario()
        self.scenario.launch()
