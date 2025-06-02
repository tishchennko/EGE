for x in range(1, 10001):
    n = 6 ** 900 + 6 ** 10 - x
    res = ''
    ans = []
    while n:
        res += str(n % 6)
        n //= 6
    if res.count('3') == res.count('5'):
        ans.append(x)
        print(max(ans))