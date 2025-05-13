def f(num):
    res = set()
    for i in range(2, int(num **.5) + 1):
        if num % i == 0:
            res |= {i, num // i}
    res = sorted(res)

    if len(res) <= 3:
        return 0
    S = res[-1] + res[-2] + res[-3]
    for i in range(1, 100_000):
        if S == int(i ** .5):
            return S

cnt = 0
for i in range(10_000_000, 10 ** 20):
    S = f(i)
    if S:
        print(i, S)
        cnt += 1
        if cnt == 5:
            break
