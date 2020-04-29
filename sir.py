from epidemics import *
import snap
import numpy as np


class sir(epidemics):
    def __init__(self, p, i, r, graph):
        super().__init__(p,i,r,graph)
        print("\nSIR model")
        print("-------------------------------------")


    def remove(self):
        for node in self.graph.Nodes():
            if self.state[node.GetId()] < 0:
                self.state[node.GetId()] += 1
                if self.state[node.GetId()] == 0:
                    self.state[node.GetId()] = 1


    def start(self, turn=5000, infected=6, crit=20):
        self.infect(infected)
        infected_perturn = []
        removed_perturn = []
        for i in range(turn):
            if i % crit == 0:
                num_infected = np.sum(self.state<0)
                num_removed = np.sum(self.state>0)
                infected_perturn.append(num_infected)
                removed_perturn.append(num_removed)
                print("turn {}: infected={} removed={}".format(i,num_infected,num_removed))

            iftd = self.transmit()
            self.remove()
            self.state[iftd] = - self.i

        num_infected = np.sum(self.state<0)
        num_removed = np.sum(self.state>0)
        infected_perturn.append(num_infected)
        removed_perturn.append(num_removed)
        return infected_perturn, removed_perturn
