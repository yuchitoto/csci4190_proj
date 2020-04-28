import snap
import numpy as np

# 0: S, >0: R, -i: I

class epidemics():
    def __init__(self, p, i, r, graph):
        self.p = p
        self.i = i
        self.r = r
        self.state = np.zeros((graph.GetNodes()+1,), dtype=np.int)
        self.graph = graph


    def infect(self, n):
        infected = np.random.randint(1,len(self.state),(n,))
        self.state[infected] = -self.i


    def transmit(self):
        infect = []
        for edge in self.graph.Edges():
            if self.state[edge.GetSrcNId()] < 0:
                if self.state[edge.GetDstNId()] == 0:
                    if np.random.rand() < self.p:
                        infect.append(edge.GetDstNId())
            elif self.state[edge.GetDstNId()] < 0:
                if self.state[edge.GetSrcNId()] == 0:
                    if np.random.rand() < self.p:
                        infect.append(edge.GetSrcNId())
        return infect
