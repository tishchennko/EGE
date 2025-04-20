from functools import *

@lru_cache(None)
def f(n):
    if n >= 10000:
        return n
    if n < 10000 and n % 2 == 0:
        return f(n + 1) + n ** 2 - 3 * (n - 1)
    if n < 10000 and n % 2 != 0:
        return f(n + 2) + 5*n - (n - 1)

for i in range(10_010, 1, -1):
    f(i)

print(f(90)- f(99))
