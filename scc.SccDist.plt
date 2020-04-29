#
# Slashdot0902.txt strongly connected components distribution. G(82168, 948464). Largest component has 0.867820 nodes (Wed Apr 29 17:22:35 2020)
#

set title "Slashdot0902.txt strongly connected components distribution. G(82168, 948464). Largest component has 0.867820 nodes"
set key bottom right
set logscale xy 10
set format x "10^{%L}"
set mxtics 10
set format y "10^{%L}"
set mytics 10
set grid
set xlabel "Size of strongly connected component"
set ylabel "Number of components"
set tics scale 2
set terminal png font arial 10 size 1000,800
set output 'scc.SccDist.png'
plot 	"scc.SccDist.tab" using 1:2 title "" with linespoints pt 6
