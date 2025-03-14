
with open('17_14952.txt') as file:
    data = [int(i) for i in file]

max_121 = max(i for i in data if abs(i) % 1000 == 121)

ans = []
for i in range(len(data) - 2):
    num1, num2, num3 = data[i:i + 3]
    summ = num1 + num2 + num3

    u1 = len(str(abs(num1))) == 4 and abs(num1) % 2 == 0
    u2 = 1000 <= abs(num2) <= 9999 and abs(num2) % 2 == 0
    u3 = 1000 <= abs(num3) <= 9999 and abs(num3) % 2 == 0

    f1 = u1 + u2 + u3 <= 1
    f2 = summ <= max_121

    if f1 and f2:
        ans.append(summ)

print(len(ans), max(ans))

#5211 20116