
with open('17_9840.txt') as file:
    data = [int(i) for i in file]


max_39 = max(i for i in data if len(str(abs(i))) == 4 and str(abs((i)))[-2:] == '39')
ans = []
for i in range(len(data) - 1):
    num1, num2 = data[i], data[i + 1]
    summ = num1 + num2
    u1 = 1000 <= abs(num1) <= 9999
    u2 = 1000 <= abs(num2) <= 9999

    f1 =  u1 + u2 == 1
    f2 =  summ ** 2 <= max_39 ** 2
    if f1 and f2:
        ans.append(summ)

print(len(ans), max(ans))
#1591 9233