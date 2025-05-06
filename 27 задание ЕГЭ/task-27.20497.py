from math import dist
import turtle

def centroid(cluster):
    dists = []
    for dot in cluster:
        sum_dist = 0
        for dot2 in cluster:
            sum_dist += dist(dot, dot2)
        dists.append([sum_dist, dot])
    return max(dists)[1]

turtle.tracer(0)

with open('27.19.A_20497.txt') as file:
    data = [list(map(float, i.split())) for i in file]

eps = 0.4
clusters = []
while data:
    cluster = [data.pop()]
    for dot in cluster:
        for dot2 in data.copy():
            if dist(dot, dot2) < eps:
                cluster.append(dot2)
                data.remove(dot2)
    if len(cluster) > 10:
        clusters.append(cluster)

print([len(cluster) for cluster in clusters])

turtle.up()
colors = ['red', 'green', 'blue']
m = 40
for cluster, color in zip(clusters, colors):
    for dot in cluster:
        turtle.goto(dot[0] * m, dot[1] * m)
        turtle.dot(3, color)

turtle.update()
turtle.done()

ends = [centroid(cluster) for cluster in clusters]
p_x = sum(end[0] for end in ends) / len(ends)
p_y = sum(end[1] for end in ends) / len(ends)
print(int(p_x * 10_000), int(p_y * 10_000))


















