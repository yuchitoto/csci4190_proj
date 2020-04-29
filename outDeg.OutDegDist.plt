#
# Slashdot0902.txt out-degree distribution. G(82168, 948464). 7896 (0.0961) nodes with out-deg > avg deg (23.1), 3970 (0.0483) with >2*avg.deg (Wed Apr 29 17:22:35 2020)
#

set title "Slashdot0902.txt out-degree distribution. G(82168, 948464). 7896 (0.0961) nodes with out-deg > avg deg (23.1), 3970 (0.0483) with >2*avg.deg"
set key bottom right
set logscale xy 10
set format x "10^{%L}"
set mxtics 10
set format y "10^{%L}"
set mytics 10
set grid
set xlabel "Out-degree"
set ylabel "Count"
set tics scale 2
set terminal png font arial 10 size 1000,800
set output 'outDeg.OutDegDist.png'
plot 	"outDeg.OutDegDist.tab" using 1:2 title "" with linespoints pt 6
