def conv(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]

ans = []
for N in range(1, 100_000):
    R = conv(N, 3)
    if sum(int(i) for i in R) == 3:
        R = '20' + R
    else: R = R + '10'
    R = int(R, 3)
    if R < 100:
        ans.append(N)
print(ans)

