from math import dist


def centroid(cluster):
    dists = []
    for dot in cluster:
        sum_dist = 0
        for p1 in cluster:
            sum_dist += dist(dot, p1)
        dists.append([sum_dist, dot])
    return max(dists)[1]


with open('27_A_21931.txt') as file:
    data = [list(map(float, i.split())) for i in file]

eps = 1
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

for cluster in clusters:
    print(len(cluster), centroid(cluster))
print(0.1663069 * 10000,  16.1520663 * 10000)