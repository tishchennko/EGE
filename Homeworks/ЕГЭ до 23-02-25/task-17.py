with open('17.txt') as file:
    data = [int(i) for i in file]

max_50 = max(i for i in data if str(abs(i))[-2:] == '50')
ans = []
for i in range(len(data) - 2):
    num1, num2, num3 = data[i:i+3]
    summ = num1 + num2 + num3
    u1 = 10000 <= abs(num1) <= 99999
    u2 = 10000 <= abs(num2) <= 99999
    u3 = 10000 <= abs(num3) <= 99999

    f1 = u1 + u2 + u3 == 3
    f2 = summ <= max_50
    if f1 and f2:
        ans.append(summ)
print(len(ans), max(ans))
#72 58037