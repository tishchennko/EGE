with open('17_9748.txt') as file:
    data = [int(i) for i in file]

max_15 = max(i for i in data if i % 100 == 15)

ans = []
for i in range(len(data) - 2):
    num1, num2, num3 = data[i:i + 3]
    summ = num1 + num2 + num3

    u1 = len(str(num1)) == 4
    u2 = 1000 <= num2 <= 9999
    u3 = 1000 <= num3 <= 9999

    f1 = u1 + u2 + u3 == 1
    f2 = summ >= max_15

    if f1 and f2:
        ans.append(summ)

print(len(ans), max(ans))