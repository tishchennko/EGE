with open ('17_17530.txt') as file:
    data = [int(i) for i in file]


minn = min(data)
ans = []
for i in range(len(data) - 1):
    num1, num2 = data[i], data[i + 1]
    summ = num1 + num2
    u1 = num1 % 55 == minn
    u2 = num2 % 55 == minn

    f1 = u1 + u2 >= 1
    if f1:
        ans.append(summ)
print(len(ans), min(ans))
#201 2942