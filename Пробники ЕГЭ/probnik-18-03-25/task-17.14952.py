with open('17_14952.txt') as file:
    data = [int(i) for i in file]

maxx_121 = max([i for i in data if abs(i) % 1000 == 121])
ans = []
for i in range(len(data) - 2):
    p1, p2, p3 = data[i:i+3]
    summ = p1 + p2 + p3
    u1 = 1000 <= abs(p1) <= 9999 and abs(p1) % 2 == 0
    u2 = 1000 <= abs(p2) <= 9999 and abs(p2) % 2 == 0
    u3 = 1000 <= abs(p3) <= 9999 and abs(p3) % 2 == 0
    f1 = u1 + u2 + u3 <= 1
    f2 = summ <= maxx_121
    if f1 and f2:
        ans.append(summ)
print(len(ans), max(ans))