def conv(num,sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]

ans = []
for N in range(11, 100_000):
    R = conv(N , 3)
    if R.count('2') + R.count('0') > R.count('1'):
        R = '22' + R
    else:
        R = '11' + R
    R = int(R, 3)
    if R > 100:
        ans.append(R)
print(min(ans))
