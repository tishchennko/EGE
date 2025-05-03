def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0:
            return False
    return True

def f(num):
    res = set()
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            res |= {i, num // i}
    res = sorted(res)

    if len(res) <= 1:
        return 0
    M = sum(res)
    if is_prime(M % 100_000):
        return M
    return False

cnt = 0
for i in range(1273548, 10 ** 20):
    M = f(i)
    if M:
        print(i, M)
        cnt += 1
        if cnt == 5:
            break