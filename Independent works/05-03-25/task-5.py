def f(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]

ans = []
for N in range(1, 100_000):
    R = f(N, 7)
    if N % 2 == 0:
        R = '52' + R + '1'
    else:
        R = R[-1] + R[1:-1] + R[0] + '15'
    R = R.strip('0')
    if N <= 1000 and len(R) == 4:
        ans.append(N)
print(max(ans))






