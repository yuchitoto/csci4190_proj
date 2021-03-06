import numpy as np
import snap
from sir import sir
from sis import sis
from sirs import sirs
from graph import *
import matplotlib.pyplot as plt

p = 0.1
i = 3
r = 1

turns = 25
crit = 1
initInfect = 3

size=25

model="SIR"

series = []
grave = []

rule = np.arange(0,turns+1,step=crit)

while p <= 1:
    ift = []
    rmd = []
    fig, ax = plt.subplots(2,1)
    for ind in range(size):
        covid = sir(p,i,r,graph)
        print("Epoch: {}/{}".format(ind+1,size))

        infect, removed = covid.start(turns, initInfect, crit)
        ift.append(infect)
        rmd.append(removed)

        ax[0].plot(rule,infect, linestyle='--', linewidth=0.5)
        ax[1].plot(rule,removed, linestyle='--', linewidth=0.5)

    ift = np.array(ift)
    rmd = np.array(rmd)
    ax[0].plot(rule,np.average(ift,axis=0), linewidth=0.5)
    ax[1].plot(rule,np.average(rmd,axis=0), linewidth=0.5)
    plt.show()
    series.append(np.average(ift,axis=0))
    grave.append(np.average(rmd,axis=0))
    p += 0.1

for index,i in enumerate(series,start=1):
    plt.plot(rule,i,label='p='+str(index/10), linewidth=0.5)
    #print(i)

plt.title("Number of infected in {} model".format(model))
plt.legend()
plt.show()

for index,i in enumerate(grave,start=1):
    plt.plot(rule,i,label="p="+str(index/10), linewidth=0.5)

plt.title("Number of removed in {} model".format(model))
plt.legend()
plt.show()
