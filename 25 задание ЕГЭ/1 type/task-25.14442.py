from fnmatch import fnmatch

def f(num):
    res = set()
    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0 and fnmatch((str(i)), '*7?'):
            res |= {i, num // i}
    res = sorted(res)



for i in range(400_000, 500_001):
    if fnmatch((str(i)), '*7?'):
        s = '23'
