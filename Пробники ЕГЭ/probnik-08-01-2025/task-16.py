from sys import setrecursionlimit

setrecursionlimit(6500)

def f(n):
    if n <= 6:
        return 1
    if n > 6:
        return 2 * n + 3 + f(n - 1)

print(f(6188)- f(6185))