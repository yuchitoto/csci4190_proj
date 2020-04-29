import numpy as np
import snap
from sir import sir
from sis import sis
from sirs import sirs
from graph import *
import matplotlib.pyplot as plt
from multiprocessing import Pool, Lock

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

def wuhan(lift, rmd, ind):
    covid = sir(p,i,r,graph)
    print("Epoch: {}/{}".format(ind+1,size))

    infect, removed = covid.start(turns, initInfect, crit)

    ax[0].plot(rule,infect)
    ax[1].plot(rule,removed)

    lock.acquire()
    try:
        ift.append(infect)
        rmd.append(removed)
    finally:
        lock.release()


locker = Lock()


def init(l):
    global lock
    lock = l


if __name__ == '__main__':
    while p <= 1:
        ift = []
        rmd = []
        fig, ax = plt.subplots(212)
        '''for ind in range(size):
            covid = sir(p,i,r,graph)
            print("Epoch: {}/{}".format(ind+1,size))

            infect, removed = covid.start(turns, initInfect, crit)
            ift.append(infect)
            rmd.append(removed)

            ax[0].plot(rule,infect)
            ax[1].plot(rule,removed)'''

        with Pool(processes=10,initializer=init, initargs=(locker,)) as p:
            for ind in range(size):
                p.apply_async(wuhan, args=(ift,rmd,ind))
            p.close()
            p.join()

        ift = np.array(ift)
        rmd = np.array(rmd)
        ax[0].plot(rule,np.average(ift,axis=0))
        ax[1].plot(rule,np.average(rmd,axis=0))
        plt.show()
        series.append(np.average(ift,axis=0))
        grave.append(np.average(rmd,axis=0))
        p += 0.1

    for index,i in enumerate(series,start=1):
        plt.plot(rule,i,label='p='+str(index/10))
        #print(i)

    plt.title("Average number of infected in {} model of {} simulations".format(model,size))
    plt.legend()
    plt.show()

    for index,i in enumerate(grave,start=1):
        plt.plot(rule,i,label="p="+str(index/10))

    plt.title("Average number of removed in {} model of {} simulations".format(model,size))
    plt.legend()
    plt.show()
