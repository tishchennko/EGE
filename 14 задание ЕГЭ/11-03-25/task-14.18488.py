for x in range(1, 100_000):
    n = 7 ** 666 + 7 ** 333 + 49 ** x - 343
    res = ''
    while n:
        res += str(n % 7)
        n //= 7
    if res.count('6') == 49:
        print(x)
        break
