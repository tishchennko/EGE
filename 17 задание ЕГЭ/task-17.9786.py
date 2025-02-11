with open('17_9786.txt') as file:
    data = [int(i) for i in file]

max_25 = max(i for i in data if str(i)[-2:] == '25')

ans = []
for i in range(len(data) - 2):
    num1, num2, num3 = data[i:i + 3]
    summ = num1 + num2 + num3
    u1 = 1000 <= abs(num1) <= 9999
    u2 = 1000 <= abs(num2) <= 9999
    u3 = 1000 <= abs(num3) <= 9999

    f1 = u1 + u2 + u3 <= 2
    f2 = summ <= max_25

    if f1 and f2:
        ans.append(summ)

print(len(ans), max(ans))