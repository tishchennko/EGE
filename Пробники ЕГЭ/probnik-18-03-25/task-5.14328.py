from string import *
def f(num, sys):
    alf = digits + ascii_lowercase
    res = ''
    while num:
        res += alf[num % sys]
        num //= sys
    return res[::-1]

ans = []
for N in range(1, 10000):
    R = f(N, 12)
    if N % 3 == 0:
        R = '1' + R + 'B'
    else:
        R = '2' + R + '0'
    R = int(R, 12)
    if R < 1996:
        ans.append(R)
print(max(ans))
#1991