from graph import *
import snap

i=0
clusters = snap.TCnComV()
mdlty = snap.CommunityGirvanNewman(graph, clusters)
for clu in clusters:
    file = open("cluster"+str(i)+".txt","w")
    for n in clu:
        file.write(str(n)+"\n")
    file.close()
