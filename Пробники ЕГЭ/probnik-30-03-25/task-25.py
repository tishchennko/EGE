def f(num):
    res = set()
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0:
            res |= {i, num // i}
    res = sorted(res)

    if len(res) < 1:
        return 0
    M = max(res) - min(res)
    if M % 10 == 6:
        return M

cnt = 0
for i in range(300_000, 10 ** 30):
    M = f(i)
    if M:
        print(i, M)
        cnt += 1
        if cnt == 5:
            break
