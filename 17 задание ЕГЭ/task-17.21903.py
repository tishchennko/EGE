with open('17_21903.txt') as file:
    data = [int(i) for i in file]

minn = min(i for i in data if str(abs(i))[-2:] == '15' and len(str(abs(i))) == 3)
ans = []

for i in range(len(data) - 2):
    n1, n2, n3 = data[i:i+3]
    summ = n1 + n2 + n3
    arr = sorted(data[i:i+3])
    u1 = n1 >= 0
    u2 = n2 >= 0
    u3 = n3 >= 0
    u4 = n1 < 0
    u5 = n2 < 0
    u6 = n3 < 0
    f1 = arr[0] * arr[-1] > minn ** 2
    f2 = u1 + u2 + u3  or u4 + u5 + u6 == 3
    if f1 and f2:
        ans.append(arr[0] * arr[-1])
print(len(ans), min(ans))















