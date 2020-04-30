import numpy as np
import snap
from sir import sir
from sis import sis
from sirs import sirs
from graph import *
import matplotlib.pyplot as plt

p = 1.0
i = 3
r = 1

turns = 100
crit = 1
initInfect = 3

size= 50

model="SIS"

series = []
grave = []

rule = np.arange(0,turns+1,step=crit)

fig, ax = plt.subplots(2,1)
for ind in range(size):
    covid = sis(p,i,r,graph)
    print("Epoch: {}/{}".format(ind+1,size))

    infect, removed = covid.start(turns, initInfect, crit)
    series.append(infect)
    grave.append(removed)

    ax[0].plot(rule,infect, linestyle='--', linewidth=0.5)
    ax[1].plot(rule,removed, linestyle='--', linewidth=0.5)

series = np.array(series)
grave = np.array(grave)
ax[0].plot(rule,np.average(series,axis=0), linewidth=1.5, label='Ave')
ax[1].plot(rule,np.average(grave,axis=0), linewidth=1.5, label='Ave')
ax[0].legend()
ax[1].legend()
ax[0].set_title("Infected in "+model+" model of p="+str(p))
ax[1].set_title("Removed in "+model+" model of p="+str(p))
np.savetxt("./simulated_data/"+model+"p"+str(int(p*10))+"infect.csv", series, delimiter=",")
np.savetxt('./simulated_data/'+model+'p'+str(int(p*10))+'r'+str(r)+model+'s'+str(initInfect)+"removed.csv", grave, delimiter=",")
plt.show()
