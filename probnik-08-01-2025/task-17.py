with open('input.txt') as file:
    arr = [int(i) for i in file]

max_68 = max([i for i in arr if abs(i) % 100 == 68])

ans = []
for i in range(len(arr) - 3):
    c1, c2, c3, c4 = arr[i:i + 4]
    summ = c1 + c2 + c3 + c4
    u1 = len(str(abs(c1))) == 2
    u2 = len(str(abs(c1))) == 2
    u3 = len(str(abs(c1))) == 2
    u4 = len(str(abs(c1))) == 2

    f1 = u1 + u2 + u3 + u4 == 1
    f2 = u1 * u2 * u3 + u4
    f3 = summ >= max_68

    if (f1 or f2) and f3:
        ans.append(summ)

print(len(ans), max(ans))
