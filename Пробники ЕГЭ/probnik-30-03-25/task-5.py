def f(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]

ans = []
for N in range(1, 100_000):
    R = f(N, 4)
    if sum(map(int, R)) % 2 == 0:
        R = R + R[-2:]
    else:
        R = '2' + R + '0'
    R = int(R, 4)
    if R > 120 and R % 2 == 0:
        ans.append(R)
print(min(ans))


