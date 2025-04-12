with open('17_6791.txt') as file:
    data = [int(i) for i in file]

minn = min(i for i in data if str(abs(i))[-2:] == '68')
ans = []
for i in range(len(data) - 2):
    n1, n2 = data[i:i+2]
    summ = n1 ** 2 + n2 ** 2
    u1 = str(abs(n1))[-2:] == '68'
    u2 = str(abs(n2))[-2:] == '68'

    f1 = u1 + u2 == 1
    f2 = summ >= minn**2
    if f1 and f2:
        ans.append(summ)
print(len(ans), max(ans))