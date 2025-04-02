with open('1706.txt') as file:
    data = [int(i) for i in file]

ans = []
min_19 = min(i for i in data if len(str(abs(i))) == 3 and str(abs(i))[-2:] == '19')
for i in range(len(data) - 2):
    n1, n2, n3 = data[i:i+3]
    summ = n1 + n2 + n3
    u1 = str(abs(n1))[-2:] == '19' and 10000 <= abs(n1) <= 99999
    u2 = str(abs(n2))[-2:] == '19' and 10000 <= abs(n2) <= 99999
    u3 = str(abs(n3))[-2:] == '19' and 10000 <= abs(n3) <= 99999

    f1 = u1 + u2 + u3 >= 1
    f2 = summ > min_19 ** 2
    if f1 and f2:
        ans.append(summ)
print(len(ans), min(ans))

