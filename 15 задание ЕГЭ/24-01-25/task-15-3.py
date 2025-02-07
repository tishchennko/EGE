def check(A):
    for x in range(1, 12000):
        x_a = (A % x == 0)
        f = x_a <= ((x == A) or (x == 1))
        if f != 1:
            return 0
    return 1

ans = []
for A in range(1, 11112):
    if check(A) == 1:
        ans.append(A)
print(len(ans))
