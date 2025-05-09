with open('17_6089.txt') as file:
    data = [int(i) for i in file]

maxx = max(i for i in data if str(abs(i))[-1] == '2')
ans = []
for i in range(len(data)):
    n1 = data[i]
    u1 = n1 % 3 == 0 and n1 % 7 != 0 and n1 % 17 != 0
    f1 = maxx % n1 == 0
    if u1 and f1:
        ans.append(n1)
print(len(ans), max(ans))
