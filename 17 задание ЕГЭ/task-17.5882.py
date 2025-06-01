with open('17_5882.txt') as file:
    data = [int(i) for i in file]

minn = (i for i in data if str(abs(i))[-1] == '3')
ans = []
for i in range(len(data) - 1):
    n1, n2 = data[i:i+2]
    summ = n1 + n2
    u1 = n1.count('3') >= 1
    u2 = n2.count('3') >= 1
    f1 = sum(map(int, minn))
    f2 = u1 >= f1 ** 2
    f3 = u2 >= f1 ** 2
    if f2 or f3:
        ans.append(summ)

print(len(ans), min(ans))
