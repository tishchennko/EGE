from math import dist


def centroid(cluster):
    dists = []
    for dot in cluster:
        sum_dist = 0
        for p1 in cluster:
            sum_dist += dist(dot, p1)
        dists.append([sum_dist, dot])
    return min(dists)[1]


with open('27.13.B_19567.txt') as file:
    data = [list(map(float, i.split())) for i in file]

eps = 0.8
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

print(int(p_x * 10_000), int(p_y * 10_000))
