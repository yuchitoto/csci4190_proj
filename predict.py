from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("simulated_data/SISp7r1i3s1infect.csv",delimiter=',')

y = []
x = []
shapex = []
shapey = []
st = []
for i in data:
    sh = -1
    tmpx=[]
    tmpy=[]
    for j in range(1,len(i)-1):
        if i[j]>=i[j+1] and i[j]>i[j-1]:
            if sh == -1:
                sh = j
            y.append(i[j])
            x.append(j-sh+1)
            tmpy.append(i[j])
            tmpx.append(j-sh+1)
    shapex.append(tmpx)
    shapey.append(tmpy)
    print(sh)
    st.append(sh)

print(np.average(np.array(st)))
print(np.array(y).reshape(-1,1).shape)
reg = LinearRegression()
reg.fit(np.log(np.array(x).reshape(-1,1)),(np.array(y).reshape(-1,1)))
rule = np.arange(0,1000)
plt.plot(rule,reg.predict(rule.reshape(-1,1)), label="predict")
print(reg.score(np.log(np.array(x).reshape(-1,1)),(np.array(y).reshape(-1,1))))

invreg = LinearRegression()
invreg.fit((np.array(y).reshape(-1,1)), np.log(np.array(x).reshape(-1,1)))
print(invreg.predict(np.array([0]).reshape(-1,1)))

plt.legend()
plt.show()

for i in range(len(data)):
    plt.plot(np.log(shapex[i]),(shapey[i]),linewidth=0.5)
    #plt.plot(np.log(shapex[i]),(shapey[i]),linewidth=0.5)

plt.show()
