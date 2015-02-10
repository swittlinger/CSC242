import csv
import numpy
import matplotlib.pyplot as plt
import random as r

def distance (a, b):
    return numpy.sqrt(numpy.power((a[0]-b[0]),2) + numpy.power((a[1]-b[1]),2))

with open('A.txt') as f:
    reader = csv.reader(f, delimiter=" ")
    data = list(reader)

#such that data is now an array of the points from A.txt

#each point is a two-member array of the form (x,y)

#each meanX is a mean, the first item in list is its coords, the rest of the items will be its points
r.seed()
mean1 = [[r.random()*2,r.random()*2]]
mean2 = [[r.random()*2,r.random()*2]]
mean3 = [[r.random()*2,r.random()*2]]

print mean1
print mean2
print mean3

#converted from strings to floats
for point in data:
    point[0] = float(point[0])
    point[1] = float(point[1])

x=0
while(True):
    #assigned each point to a mean
    for point in data:
        closest_mean = mean1
        closest_dist = distance(closest_mean[0], point)
        if distance(mean2[0], point) < closest_dist:
            closest_dist = distance(mean2[0], point)
            closest_mean = mean2
        if distance(mean3[0], point) < closest_dist:
            closest_dist = distance(mean3[0], point)
            closest_mean = mean3
        closest_mean.append(point)

    #calculate centroid for mean1
    x_init = mean1[0][0]
    y_init = mean1[0][1]

    x_total = 0
    y_total = 0
    for point in mean1:
        x_total += point[0]
        y_total += point[1]

    #remove the cluster's own coordinates from the sum
    x_total -= mean1[0][0]
    y_total -= mean1[0][1]

    #take average
    x_avg = x_total/(len(mean1)-1)
    y_avg = y_total/(len(mean1)-1)

    #assign average to new cluster coordinate
    mean1[0][0] = x_avg
    mean1[0][1] = y_avg

    #check if we've changed anything
    mean1_same = (x_init == x_avg) and (y_init == y_avg)

    #------------------------------
    x_init = mean2[0][0]
    y_init = mean2[0][1]

    #calculate centroid for mean2
    x_total = 0
    y_total = 0
    for point in mean2:
        x_total += point[0]
        y_total += point[1]

    #remove the cluster's own coordinates from the sum
    x_total -= mean2[0][0]
    y_total -= mean2[0][1]

    #take average
    x_avg = x_total/(len(mean2)-1)
    y_avg = y_total/(len(mean2)-1)

    #assign average to new cluster coordinate
    mean2[0][0] = x_avg
    mean2[0][1] = y_avg

    #check if we've changed anything
    mean2_same = (x_init == x_avg) and (y_init == y_avg)

    #------------------------------
    x_init = mean3[0][0]
    y_init = mean3[0][1]

    #calculate centroid for mean3
    x_total = 0
    y_total = 0
    for point in mean3:
        x_total += point[0]
        y_total += point[1]

    #remove the cluster's own coordinates from the sum
    x_total -= mean3[0][0]
    y_total -= mean3[0][1]

    #take average
    x_avg = x_total/(len(mean3)-1)
    y_avg = y_total/(len(mean3)-1)

    #assign average to new cluster coordinate
    mean3[0][0] = x_avg
    mean3[0][1] = y_avg

    #check if we've changed anything
    mean3_same = (x_init == x_avg) and (y_init == y_avg)

    print mean3_same
    print mean2_same
    print mean1_same

    x += 1

    if (mean3_same and mean2_same and mean1_same):
        break
    else:
        mean1 = [mean1[0]]
        mean2 = [mean2[0]]
        mean3 = [mean3[0]]
        print "One more time! %d" % (x)

#calculate Distortion
distortion = 0.0
for point in mean1:
    distortion += numpy.power(distance(point, mean1[0]),2)

for point in mean2:
    distortion += numpy.power(distance(point, mean2[0]),2)

for point in mean3:
    distortion += numpy.power(distance(point, mean3[0]),2)


x_coords = [None]
y_coords = [None]

for point in mean1:
    x_coords.append(point[0])
    y_coords.append(point[1])

plt.plot(x_coords, y_coords, 'ro')

x_coords = [None]
y_coords = [None]

for point in mean2:
    x_coords.append(point[0])
    y_coords.append(point[1])

plt.plot(x_coords, y_coords, 'g^')

x_coords = [None]
y_coords = [None]

for point in mean3:
    x_coords.append(point[0])
    y_coords.append(point[1])

plt.plot(x_coords, y_coords, 'bs')
plt.title('Distortion value: %f' %(distortion))
plt.show()