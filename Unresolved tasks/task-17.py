
with open('17-1.txt') as file:
    data = [int(i) for i in file]

max_43 = max(i for i in data if len(str(abs(i))) == 5 and str(abs(i))[-2:] == '43')

ans = []
for i in range(len(data) - 2):
    num1, num2, num3 = data[i:i+3]
    summ = num1  ** 2 + num2 **2 + num3 ** 2
    u1 = 10000 <= abs(num1) <= 99999 and str(abs(num1))[-2:] == '43'
    u2 = 10000 <= abs(num2) <= 99999 and str(abs(num2))[-2:] == '43'
    u3 = 10000 <= abs(num3) <= 99999 and str(abs(num3))[-2:] == '43'

    f1 = u1 + u2 + u3 >= 1
    f2 = summ <= max_43 ** 2

    if f1 and f2:
        ans.append(summ)

print(len(ans), min(ans))
