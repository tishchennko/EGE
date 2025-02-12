with open('17_4705.txt') as file:
    data = [int(i) for i in file]

ans = []
max_3 = max(i for i in data if str(i)[-1:] == '3')
for i in range(len(data) - 1):
    num1, num2 = data[i:i+2]
    summ = num1**2 + num2**2
    u1 = str(num1)[-1:] == '3'
    u2 = str(num2)[-1:] == '3'

    f1 = u1 + u2 == 1
    f2 = summ >= max_3 ** 2

    if f1 and f2:
        ans.append(summ)
print(len(ans), max(ans))
#180 190360573