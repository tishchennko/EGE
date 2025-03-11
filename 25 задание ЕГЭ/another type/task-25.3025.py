def f(num):
    res = set()
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            if i % 2 != 0:
                res |= {i}
            if num // i % 2 != 0:
                res |= {num // i}
    res = sorted(res)

    if len(res) <= 5:
        return 0
    if len(res) >= 6:
        return res[-6]


cnt = 0
for i in range(200000001, 10 ** 30):
    res = f(i)
    if res:
        print(i, res)
        cnt += 1
        if cnt == 5:
            break