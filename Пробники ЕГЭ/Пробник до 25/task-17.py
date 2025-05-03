with open('17_2399.txt') as file:
    data = [int(i) for i in file]

summ2 = sum(sum(map(int, str(i))) for i in data if i % 35 == 0)

ans = []
for i in range(len(data) - 1):
    n1, n2 = data[i:i+2]
    summ = n1 + n2
    u1 = n1 > summ2
    u2 = n2 > summ2
    u3 = hex(n1)[-2:] == 'ef'
    u4 = hex(n2)[-2:] == 'ef'
    f1 = u1 and u4 and not u2
    f2 = u2 and u3 and not u1
    if f1 or f2:
        ans.append(summ)
print(len(ans), min(ans))
