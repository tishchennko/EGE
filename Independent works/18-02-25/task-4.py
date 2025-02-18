with open('17_19486.txt') as file:
    data = [int(i) for i in file]


ans = []
max_7 = len([i for i in data if str(abs(i))[-1:] == '7'])
for i in range(len(data) - 1):
    num1, num2 = data[i:i+2]
    summ = num1 + num2
    u1 = num1 > 0
    u2 = num2 < 0

    f1 = u1 + u2 == 1
    f2 = summ < max_7
    if f1 and f2:
        ans.append(summ)
print(len(ans), max(ans))

