def conv(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]

ans = []
for N in range(1, 100_000):
    R = conv(N, 4)
    if N % 4 == 0:
        R = '2' + R + '03'
    else:
        R = R + conv((N % 4) * 5, 4)
    R = int(R, 4)
    if R <= 557:
        ans.append(N)
print(max(ans))




