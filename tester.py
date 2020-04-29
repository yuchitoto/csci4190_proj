import numpy as np
import snap
from sir import sir
from sis import sis
from sirs import sirs
from graph import *
import matplotlib.pyplot as plt
from multiprocessing import Pool, Lock, Manager

p = 0.1
i = 3
r = 1

turns = 25
crit = 1
initInfect = 3
size = 25

model="SIR"

series = []
grave = []

rule = np.arange(0,turns+1,step=crit)

def wuhan(lft, rmd, ind):
    covid = sir(p,i,r,graph)
    print("Epoch: {}/{}".format(ind+1,size))

    infect, removed = covid.start(turns, initInfect, crit)

    ax[0].plot(rule,infect, linestyle='--', linewidth=0.5)
    ax[1].plot(rule,removed, linestyle='--', linewidth=0.5)

    lft+infect
    rmd+removed


locker = Lock()


def init(l):
    global lock
    lock = l


if __name__ == '__main__':
    while p <= 1:
        ift = []
        rmd = []
        fig, ax = plt.subplots(2,1)
        '''for ind in range(size):
            covid = sir(p,i,r,graph)
            print("Epoch: {}/{}".format(ind+1,size))

            infect, removed = covid.start(turns, initInfect, crit)
            ift.append(infect)
            rmd.append(removed)

            ax[0].plot(rule,infect)
            ax[1].plot(rule,removed)'''

        with Pool(processes=10,initializer=init, initargs=(locker,)) as p:
            with Manager() as manager:
                inft = manager.list()
                rmvd = manager.list()
                for ind in range(size):
                    p.apply_async(wuhan, args=(inft, rmvd, ind))
                p.close()
                p.join()
                ift = inft
                rmd = rmvd

                ift = np.array(ift).reshape((len(rule), size))
                rmd = np.array(rmd).reshape((len(rule), size))
                print(ift)
                print(rmd)
                ax[0].plot(rule,np.average(ift,axis=0), linestyle='-', linewidth=0.5, label='Avg')
                ax[1].plot(rule,np.average(rmd,axis=0), linestyle='-', linewidth=0.5, label='Avg')
                ax[0].legend()
                ax[1].legend()
                ax[0].title("Infected in p="+str(p))
                ax[1].title("Removed in p="+str(p))
                plt.show()
                series.append(np.average(ift,axis=0))
                grave.append(np.average(rmd,axis=0))
                p += 0.1

    for index,i in enumerate(series,start=1):
        plt.plot(rule,i,label='p='+str(index/10), linewidth=0.5)
        #print(i)

    plt.title("Average number of infected in {} model of {} simulations".format(model,size))
    plt.legend()
    plt.show()

    for index,i in enumerate(grave,start=1):
        plt.plot(rule,i,label="p="+str(index/10), linewidth=0.5)

    plt.title("Average number of removed in {} model of {} simulations".format(model,size))
    plt.legend()
    plt.show()
