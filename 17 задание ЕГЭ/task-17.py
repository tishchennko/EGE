with open('17_12249.txt') as file:
    data = [int(i) for i in file]

maxx = max(i for i in data if str(abs(i))[-1] == '3' and len(str(abs(i))) == 5)
ans = []
for i in range(len(data) - 2):
    n1, n2, n3 = data[i:i+3]
    summ = n1 + n2 + n3
    u1 = str(abs(n1))[-1] == '3'
    u2 = str(abs(n2))[-1] == '3'
    u3 = str(abs(n3))[-1] == '3'

    f1 = u1 + u2 + u3 >= 1
    f2 = summ <= maxx
    if f1 and f2:
        ans.append(summ)
print(len(ans), max(ans))