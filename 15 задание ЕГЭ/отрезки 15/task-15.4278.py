def f(A):
    for x in range(1, 1000):
        a_12 = A % 12 == 0
        x_530 = 530 % x == 0
        x_a = A % x == 0
        x_170 = 170 % x == 0
        f = a_12 and (x_530 <= ((not x_a) <= (not x_170)))
        if f != 1:
            return 0
    return 1

ans = []
for A in range(1, 1001):
    if f(A) == 1:
        ans.append(A)

print(len(ans))
