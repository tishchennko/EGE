with open('26_17537.txt') as file:
    N, M, K = map(int, file.readline().split())
    cinema = [list(map(int, i.split())) for i in file]

cinema = sorted(cinema, key = lambda x: (x[1], -x[0]))

mesto = [M + 1] * (K + 1)
for h, v in cinema:
    mesto[v] = h

ans = []
for i in range(1, len(mesto) - 1):
    p1, p2 = mesto[i:i+2]
    ans.append([min(p1, p2) - 1, i + 1])

ans = sorted(ans, key = lambda x: (x[1], -x[0]))

print(max(ans))