
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
    res = sorted(res)

    if len(res) <= 1:
        return 0
    S = sum(res)
    if S % 145 == 0:
        return S
    return 0



cnt = 0
for i in range(32_500_000, 10 ** 20):
    S = f(i)
    if S:
        print(i, S)
        cnt += 1
        if cnt == 7:
            break
