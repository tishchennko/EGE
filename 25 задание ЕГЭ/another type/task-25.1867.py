
def f(num):
    res = set()
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            res |= {i, num // i}
    res = sorted(res)

    for i in res:
        if str(i)[-1] == '8' and i != 8:
            return i
    return 0

cnt = 0
for i in range(500001, 10 ** 20):
    res = f(i)
    if res:
        print(i, res)
        cnt += 1
        if cnt == 5:
            break
