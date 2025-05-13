def f(num):
    res = set()
    for i in range(1, int(num ** .5) + 1):
        if num % i == 0:
            res |= {i, num // i}
    res = sorted(res)


    if len(res) <= 1:
        return 0
    R = sum(res)
    if str(R)[-1] == '6':
        return R

cnt = 0
for i in range(500001, 10 ** 20):
    res = f(i)
    if res:
        print(i, res)
        cnt += 1
        if cnt == 5: break
