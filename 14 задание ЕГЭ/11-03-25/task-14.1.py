ans = []
for x in range(1, 2006):
    n = 43 ** 56 + 113 ** 841 - x
    res = ''
    while n:
        res += str(n % 4)
        n //= 4
    if res.count('2') <= 712 and res.count('0') % 2 == 0 and res.count('2') % 2 == 0\
        and res.count('1') % 2 == 0 and res.count('3') % 2 == 0:
        ans.append(x)
print(max(ans))
