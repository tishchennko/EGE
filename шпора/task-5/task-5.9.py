def f(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]
ans = []
for N in range(3, 100_000):
    R = f(N, 3)
    if N % 3 == 0:
        R = R + R[-2:]
    else:
        R = R + f((N % 3) * 3, 3)
    R = int(R, 3)
    if R < 150:
        ans.append(N)
print(max(ans))