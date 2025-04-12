def f(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]

ans= []
for n in range(1 ,100_000):
    R = f(n, 3)
    if n % 5 == 0:
        R = R + R[-3:]
    else:
        R = R + f((n % 5) * 5, 3)
    R = int(R, 3)
    if R < 5496:
        ans.append(n)
print(max(ans))
