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

model="SIR"

series = []
grave = []
while p <= 1:
    covid = sir(p,i,r,graph)

    infect, removed = covid.start(turns, initInfect, crit)
    series.append(infect)
    grave.append(removed)

    '''rule = np.arange(0,turns+1,step=crit)

    plt.plot(rule, infect, color='red', label='infected')
    plt.plot(rule, removed, color='black', label='removed')
    plt.show()'''
    p += 0.1

rule = np.arange(0,turns+1,step=crit)

for index,i in enumerate(series,start=1):
    plt.plot(rule,i,label='p='+str(index/10))
    #print(i)

plt.title("Number of infected in {} model".format(model))
plt.legend()
plt.show()

for index,i in enumerate(grave,start=1):
    plt.plot(rule,i,label="p="+str(index/10))

plt.title("Number of removed in {} model".format(model))
plt.legend()
plt.show()
