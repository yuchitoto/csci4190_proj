#
# Slashdot0902.txt in-degree distribution. G(82168, 948464). 7829 (0.0953) nodes with in-deg > avg deg (23.1), 3831 (0.0466) with >2*avg.deg (Wed Apr 29 17:22:35 2020)
#

set title "Slashdot0902.txt in-degree distribution. G(82168, 948464). 7829 (0.0953) nodes with in-deg > avg deg (23.1), 3831 (0.0466) with >2*avg.deg"
set key bottom right
set logscale xy 10
set format x "10^{%L}"
set mxtics 10
set format y "10^{%L}"
set mytics 10
set grid
set xlabel "In-degree"
set ylabel "Count"
set tics scale 2
set terminal png font arial 10 size 1000,800
set output 'inDeg.InDegDist.png'
plot 	"inDeg.InDegDist.tab" using 1:2 title "" with linespoints pt 6
