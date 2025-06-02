'''
from math import dist

def centroid(cluster):
    dists = []
    for dot in cluster:
        summ = 0
        for dot2 in cluster:
            summ += dist(dot, dot2)
        dists.append([summ, dot])
    return min(dists)[1]

with open('27_A_21599.txt') as file:
    data = [list(map(float, i.split())) for i in file]

eps = 5.5
clusters = []
while data:
    cluster = [data.pop()]
    for dot in cluster:
        for dot2 in data.copy():
            if dist(dot, dot2) < eps:
                cluster.append(dot2)
                data.remove(dot2)
    clusters.append(cluster)

print([len(cluster) for cluster in clusters])

centers = [centroid(cluster) for cluster in clusters]
p_x = sum(center[0] for center in centers) / len(centers)
p_y = sum(center[1] for center in centers) / len(centers)

print(int(p_x * 10000), int(p_y * 10000))
'''

from math import dist

def centroid(cluster):
    dists = []
    for dot in cluster:
        summ = 0
        for dot2 in cluster:
            summ += dist(dot, dot2)
        dists.append([summ, dot])
    return min(dists)[1]

with open('27_A_21599.txt') as file:
    cluster1 = []
    cluster2= []
    cluster3 = []
    for i in file:
        x, y = map(float, i.split())
        if y > x - 10:
            cluster1.append((x, y))
        elif y < x - 10 and y > -7:
            cluster2.append((x, y))
        elif y < -7:
            cluster3.append((x, y))


centr1 = centroid(cluster1)
centr2 = centroid(cluster2)
centr3 = centroid(cluster3)

ans_x = (centr1[0] + centr2[0] + centr3[0]) / 3
ans_y = (centr1[1] + centr2[1] + centr3[1]) / 3

print(int(ans_x * 10000), int(ans_y * 10000))