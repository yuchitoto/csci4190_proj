from epidemics import *
import snap
import numpy as np


class sis(epidemics):
    def __init__(self, p, i, r, graph):
        super().__init__(p,i,r,graph)
        print("\nSIS model")
        print("-------------------------------------")


    def remove(self):
        self.state[self.state<0] += 1


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
                if num_infected==0:
                    tmp = [0 for j in range(i+1,turn)]
                    infected_perturn+=tmp
                    tmp=[num_removed for j in range(i+1,turn)]
                    removed_perturn+=tmp
                    for j in range(i+1,turn):
                        print("turn{}: infected=0 removed={}".format(j,num_removed))
                    break
            iftd = self.transmit()
            self.remove()
            self.state[iftd] = - self.i

        num_infected = np.sum(self.state<0)
        num_removed = np.sum(self.state>0)
        infected_perturn.append(num_infected)
        removed_perturn.append(num_removed)
        return infected_perturn, removed_perturn
