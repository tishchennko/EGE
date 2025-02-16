from sys import setrecursionlimit

setrecursionlimit(5000)

def f(n):
    if n < 5:
        return n
    if n > 4:
        return 4 * f(n - 4)
print(f(4444)//f(4400))
#4194304