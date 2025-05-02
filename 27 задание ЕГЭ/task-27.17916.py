from math import dist

def centroid(cluster):
    distance = []
    for dot in cluster:
        sum_dist = 0
        for dot2 in cluster:
            sum_dist += dist(dot, dot2)
        distance.append([sum_dist, dot])
    return min(distance)[1]

with open('27_A_17916.txt') as file:
    cluster1 = []
    cluster2= []
    for i in file:
        x, y = map(float, i.split())
        if y < 8:
            cluster1.append((x, y))
        else:
            cluster2.append((x, y))

centr1 = centroid(cluster1)
centr2 = centroid(cluster2)

ans_x = (centr1[0] + centr2[0]) / 2
ans_y = (centr1[1] + centr2[1]) / 2

print(int(ans_x * 10000), int(ans_y * 10000))