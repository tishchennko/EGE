from math import dist

def centroid(cluster):
    distance = []
    for dot1 in cluster:
        summ = 0
        for dot2 in cluster:
            summ += dist(dot1, dot2)
        distance.append([summ, dot1])
    return min(distance)[1]

with open('27_A_21911.txt') as file:
    data = [list(map(float, i.split())) for i in file]

eps = 2
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

centers= [centroid(cluster) for cluster in clusters]
p_x = sum(center[0] for center in centers) / len(centers)
p_y = sum(center[1] for center in centers) / len(centers)

print(int(p_x * 10000), int(p_y * 10000))


