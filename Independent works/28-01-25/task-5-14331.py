def conv(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]

ans = []
for N in range(1, 100_000):
    R = conv(N, 3)
    if sum(int(i) for i in R) % 3 == 0:
        R = R + '212'
    else: R = R + conv(sum(int(i) for i in R)*2, 3)
    R = int(R, 3)
    if R > 490:
        ans.append(R)
print(min(ans))