def conv(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]

ans = []
for N in range(1, 100_000):
    R = conv(N, 3)
    if N % 3 == 0:
        R = '1' + R + '02'
    else:
        R = R + conv((N % 3) * 4, 3)
    R = int(R, 3)
    if R < 199:
        ans.append(N)
print(max(ans))