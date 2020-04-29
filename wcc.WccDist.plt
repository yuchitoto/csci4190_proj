#
# Slashdot0902.txt weakly connected components distribution. G(82168, 948464). Largest component has 1.000000 nodes (Wed Apr 29 17:22:35 2020)
#

set title "Slashdot0902.txt weakly connected components distribution. G(82168, 948464). Largest component has 1.000000 nodes"
set key bottom right
set logscale xy 10
set format x "10^{%L}"
set mxtics 10
set format y "10^{%L}"
set mytics 10
set grid
set xlabel "Size of weakly connected component"
set ylabel "Number of components"
set tics scale 2
set terminal png font arial 10 size 1000,800
set output 'wcc.WccDist.png'
plot 	"wcc.WccDist.tab" using 1:2 title "" with linespoints pt 6
