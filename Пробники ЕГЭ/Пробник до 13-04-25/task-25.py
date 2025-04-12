from fnmatch import *


def f(num):
    res = set()
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0 and fnmatch((str(i)), '12?*45'):
            res |= {i, num // i}
    res = sorted(res)

    if len(res) < 1:
        return 0

cnt = 0
for i in range(10 ** 7):
    res = f(i)
    while res:
        print(res)