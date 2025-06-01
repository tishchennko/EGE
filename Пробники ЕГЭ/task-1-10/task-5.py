def f(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]
ans = []
for N in range(1, 100_000):
    R = f(N, 7)
    if R.count('2') % 2 == 0:
        R = R + '555'
    else:
        R = '1' + R
    R = int(R, 7)
    if R < 3799:
        ans.append(N)
print(max(ans))