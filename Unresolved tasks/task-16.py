from sys import setrecursionlimit

setrecursionlimit(5000)

def f(n):
    if n == 1:
        return n
    if n > 1:
        return 3 * n * f(n - 1)

print(((f(2024) // 6) + f(2023)) // f(2022))
#6147897