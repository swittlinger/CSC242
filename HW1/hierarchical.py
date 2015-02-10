import csv
import numpy
import matplotlib.pyplot as plt
import random as r
import scipy.cluster.hierarchy as hierarch

def distance (a, b):
    return numpy.sqrt(numpy.power((a[0]-b[0]),2) + numpy.power((a[1]-b[1]),2))

with open('B.txt') as f:
    reader = csv.reader(f, delimiter=' ')
    data = list(reader)

#such that data is now an array of the points from B.txt

#each point is a two-member array of the form (x,y)

#assign each point a label & convert to floats

x=0
for point in data:
    point[0] = float(point[0])
    point[1] = float(point[1])

#compute distances

distances = [[None]*len(data)] * len(data)

cluster1 = []
cluster2 = []

#for point1 in data:
#    for point2 in data:
#        distances[point2[2]][point1[2]] = distance(point1, point2)

for point in data:
    if point[0] > 0.4 and point[0] < 1.4 and point[1] > 0.9 and point[1] < 1.68:
        plt.plot(point[0], point[1], 'ro')
    else:
        plt.plot(point[0], point[1], 'bs')

plt.show()