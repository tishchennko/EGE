def f(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]

ans = []
for N in range(1, 100_000):
    R = f(N, 4)
    if len(R) % 2 == 0:
        R = R[:len(R)//2] + '0' + R[len(R)//2:]
    else:
        R = R
    R = int(R, 4)
    if R <= 180:
        ans.append(N)
print(max(ans))
#63