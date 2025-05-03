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
            if is_prime(i): res.add(i)
            if is_prime(num // i): res.add(num // i)

    if len(res) <= 1:
        return 0
    M = min(res) + max(res)
    if M % 213 == 171:
        return M
    return 0

cnt = 0
for i in range(23600000, 10 ** 20):
    M = f(i)
    if M:
        print(i, M)
        cnt += 1
        if cnt == 6: break

