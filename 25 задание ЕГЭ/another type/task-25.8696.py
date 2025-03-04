def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0:
            return False
    return True

def f(num):
    res = set()
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0:
            res |= {i, num // i}

    if len(res) <= 1:
        return 0
    M = sum(res)
    if is_prime(M % 100000):
        return M
    return 0

cnt = 0
for i in range(1273547, 10 ** 20):
    M = f(i)
    if M:
        print(i, M)
        cnt += 1
        if cnt == 5: break








