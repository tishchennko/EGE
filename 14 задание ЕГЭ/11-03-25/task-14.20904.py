for x in range(1, 2031)[::-1]:
    n = 3 ** 100 - x
    res = ''
    while n:
        res += str(n % 3)
        n //= 3
    if res.count('0') == 1:
        print(x)
        break