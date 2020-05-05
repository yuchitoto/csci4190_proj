import numpy as np

data = []
for i in range(1,11):
    data.append(np.loadtxt("simulated_data/SIRp{}r1i3s3infected.csv".format(i),delimiter=','))

print(np.array(data).shape)
amax = []
st = []
alx = []
for i in data:
    x=[]
    lmax = []
    ast = 0
    for j in i:
        tmpx = []
        sh=-1
        for k in range(1,len(j)-1):
            if j[k]>j[k+1] and j[k]>j[k-1]:
                if sh==-1:
                    sh=k
                tmpx.append(k-sh+1)
        ast += sh
        x.append(tmpx)
        lmax.append(np.amax(j))
    st.append(ast/len(i))
    alx.append(x)
    amax.append(np.average(np.array(lmax)))

amax = np.array(amax)/82168
for i in np.around(amax,decimals=5):
    print("& {}".format(i),end="")
print()

for i in st:
    print("& {}".format(i),end='')
print()
#print(alx)

for i in alx:
    btmp = []
    for j in i:
        for k in range(len(j)-1):
            btmp.append(j[k+1]-j[k])
    btmp = np.array(btmp)
    print("& {}".format(np.around(btmp.mean(),decimals=4)),end='')
print()
