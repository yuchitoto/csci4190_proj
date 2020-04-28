import numpy as np
import snap
from sir import sir
from sis import sis
from sirs import sirs
from graph import *
import matplotlib.pyplot as plt

p = 0.7
i = 5
r = 3

print("infect p: {}".format(p))
print("infectious period: {}".format(i))
print("removed period: {}".format(r))

print()
print("sir model")

covid = sirs(p,i,r,graph)

turns = 100
crit = 1
initInfect = 3

infect, removed = covid.start(turns, initInfect, crit)

rule = np.arange(0,turns+1,step=crit)

plt.plot(rule, infect, color='red', label='infected')
plt.plot(rule, removed, color='black', label='removed')
plt.show()
