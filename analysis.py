from graph import *
import snap

# plot deg dist
snap.PlotInDegDistr(graph, "InDegDist", flnme+" in-degree distribution")
snap.PlotOutDegDistr(graph, "OutDegDist", flnme+" out-degree distribution")

# plot connected components dist
snap.PlotSccDistr(graph, "SccDist", flnme+" strongly connected components distribution")
snap.PlotWccDistr(graph, "WccDist", flnme+" weakly connected components distribution")

# plot cluster coefficient
snap.PlotClustCf(graph, "ClustCoef", flnme+" clustering coefficient")
