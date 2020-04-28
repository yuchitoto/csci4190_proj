import snap

flnme = "Slashdot0902.txt"

graph = snap.LoadEdgeList(snap.PNGraph, flnme, 0, 1, '\t')

snap.PrintInfo(graph)

'''bridge = snap.TIntPrV()
snap.GetEdgeBridges(graph, bridge)
print("Number of bridges: {}".format(len(bridge)))'''
