
with open('17_18582.txt') as file:
    data = [int(i) for i in file]

min_data = min(i for i in data)
ans = []
for i in range(len(data) - 2):
    num1, num2, num3 = data[i:i+3]
    summ = num1 + num2 + num3
    u1 = num1 > 0
    u2 = num2 > 0
    u3 = num3 > 0

    f1 = u1 + u2 + u3 <= 1
    f2 = str(summ)[-1:] == str(min_data)[-1:]

    if f1 and f2:
        ans.append(abs(num1 + num2 + num3))

print(len(ans), max(ans))
#440 210834