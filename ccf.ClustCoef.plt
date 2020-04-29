#
# Slashdot0902.txt clustering coefficient. G(82168, 948464). Average clustering: 0.0603  OpenTriads: 73175813 (0.9918)  ClosedTriads: 602592 (0.0082) (Wed Apr 29 17:22:37 2020)
#

set title "Slashdot0902.txt clustering coefficient. G(82168, 948464). Average clustering: 0.0603  OpenTriads: 73175813 (0.9918)  ClosedTriads: 602592 (0.0082)"
set key bottom right
set logscale xy 10
set format x "10^{%L}"
set mxtics 10
set format y "10^{%L}"
set mytics 10
set grid
set xlabel "Node degree"
set ylabel "Average clustering coefficient"
set tics scale 2
set terminal png font arial 10 size 1000,800
set output 'ccf.ClustCoef.png'
plot 	"ccf.ClustCoef.tab" using 1:2 title "" with linespoints pt 6
