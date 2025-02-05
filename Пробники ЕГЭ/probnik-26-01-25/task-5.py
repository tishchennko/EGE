def f(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num  //= sys
    return res[::-1]

ans = []
for n in range(1, 100_000):
    R = f(n, 3)
    if n % 3 == 0:
        R = R + R[-2:]
    else: R = f(n % 3 * 5, 3)
    R = int(R, 3)
    if R > 133:
        ans.append(R)
print(min(ans))
