with open('17.txt') as file:
    data = [int(i) for i in file]

ans = []
minn = sum([i for i in data if i < 0])
for i in range(len(data) - 2):
    num1, num2, num3 = data[i:i+3]
    summ = num1 + num2 + num3
    u1 = max(num1, num2, num3)
    u2 = min(num1, num2, num3)
    if u1 * u2 > minn:
        ans.append(summ)
print(len(ans), abs(max(ans)))

