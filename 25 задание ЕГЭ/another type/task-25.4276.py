def f(num):
    res = set()
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0:
            res |= {i, num // i}
    res = sorted(res)

    if len(res) < 7:
        return 0
    if len(res) >= 7:
        return res[-7], len(res)

cnt = 0
for i in range(400_000_001, 10 ** 20):
    res = f(i)
    if res:
        print(*res)
        cnt += 1
        if cnt == 5:
            break