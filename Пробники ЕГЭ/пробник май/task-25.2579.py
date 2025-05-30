def f(num):
    res = set()
    for i in range(2, int(num **.5) + 1):
        if num % i == 0:
            res |= {i, num // i}
    res = sorted(res)

    if len(res) < 3:
        return 0
    S = res[-1] + res[-2] + res[-3]
    if S ** .5 == int(S ** .5):
        return S
    return 0

cnt = 0
for i in range(10_000_000, 10 ** 20):
    S = f(i)
    if S:
        print( S)
        cnt += 1
        if cnt == 5:
            break
