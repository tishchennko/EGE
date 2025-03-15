with open("26var01.txt") as file:
    n, m, k = map(int, file.readline().split())
    ans = [list(map(int, i.split())) for i in file]

ans = sorted(ans, key=lambda x: (x[1], -x[0]))

pole = [m + 1] * (k + 1)
for h, v in ans:
    pole[v] = h

for i in range(1, len(pole) - 1):
    p1, p2 = pole[i:i+2]
    ans.append([min(p1,p2) - 1, i])

ans = sorted(ans, key = lambda x: (-x[0], x[1]))
print(min(ans))

