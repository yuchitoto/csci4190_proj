import numpy as np
import snap
from sir import sir
from sis import sis
from sirs import sirs
from graph import *
import matplotlib.pyplot as plt
from multiprocessing import Pool, Lock, Manager
import traceback

p = 0.7
i = 3
r = 1

turns = 100
crit = 1
initInfect = 3
size = 25

model="SIRS"

series = []
grave = []

rule = np.arange(0,turns+1,step=crit)


def rand_rv(graph, rm_rate=0.5):
    edge_list = [ [i.GetSrcNId(), i.GetDstNId()] for i in graph.Edges()]
    print(np.array(edge_list).shape)
    np.random.shuffle(np.array(edge_list))
    #rmi = np.random.uniform(0, len(edge_list), (int(len(edge_list) * rm_rate), ))
    #print(rmi.shape)
    rme = edge_list[:int(len(edge_list) * rm_rate)]
    for i in rme:
        graph.DelEdge(i[0],i[1])
    #snap.PrintInfo(graph)
    snap.PrintInfo(graph, "Slashdot0922", "/dev/stdout", False)
    return graph


def handle_error(e):
    traceback.print_exception(type(e), e, e.__traceback__)


def wuhan(lft, rmd, ind, shape):
    rand_rv(graph)
    np.random.seed()
    covid = sirs(p,i,r,graph)
    print("Epoch: {}/{}".format(ind+1,size))

    infect, removed = covid.start(turns, initInfect, crit)
    lft += infect
    rmd += removed

    return infect, removed


locker = Lock()


def init(l):
    global lock
    lock = l


if __name__ == '__main__':
    lp = 0
    while lp<1:
        lp += 1
        fig, ax = plt.subplots(2,1)
        '''for ind in range(size):
            covid = sir(p,i,r,graph)
            print("Epoch: {}/{}".format(ind+1,size))

            infect, removed = covid.start(turns, initInfect, crit)
            ift.append(infect)
            rmd.append(removed)

            ax[0].plot(rule,infect)
            ax[1].plot(rule,removed)'''

        with Pool(processes=10,initializer=init, initargs=(locker,)) as process:
            with Manager() as manager:
                ift = []
                rmd = []
                inft = manager.list()
                rmvd = manager.list()
                shp = manager.list()
                proc = []
                for ind in range(size):
                    proc.append(process.apply_async(wuhan, args=(inft, rmvd, ind, shp), error_callback=handle_error))
                process.close()
                for i in proc:
                    a, b = i.get()
                    ift.append(a)
                    rmd.append(b)
                process.join()

                #print(ift)
                #print(rmd)
                #print(inft)
                #print(rmvd)
                series.append(np.average(ift,axis=0))
                grave.append(np.average(rmd,axis=0))

    np.savetxt("./simulated_data/reduced_graph/"+model+'p'+str(int(p*10))+'r'+str(r)+'i'+str(i)+'s'+str(initInfect)+"infect.csv", np.aray(ift),delimiter=',')
    np.savetxt("./simulated_data/reduced_graph/"+model+'p'+str(int(p*10))+'r'+str(r)+'i'+str(i)+'s'+str(initInfect)+"removed.csv", np.array(rmd),delimiter=',')
    for index,i in enumerate(series,start=1):
        plt.plot(rule,i,label='p='+str(p), linewidth=0.5)
        #print(i)

    plt.title("Average number of infected in {} model of {} simulations".format(model,size))
    plt.legend()
    plt.show()

    for index,i in enumerate(grave,start=1):
        plt.plot(rule,i,label="p="+str(p), linewidth=0.5)

    plt.title("Average number of removed in {} model of {} simulations".format(model,size))
    plt.legend()
    plt.show()
