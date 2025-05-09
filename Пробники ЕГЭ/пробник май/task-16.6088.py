from sys import setrecursionlimit
setrecursionlimit(5000)
def f(n):
    if n > 3000:
        return n
    if n <= 3000 and n % 2 == 0:
        return f(n + 1) - n + 1
    if n <= 3000 and n % 2 != 0:
        return f(n + 2) - 2 * n + 2
print(2*f(39) - 2 * f(34))