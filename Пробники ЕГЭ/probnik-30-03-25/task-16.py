def f(n):
    if n <= 3:
        return n
    if n > 3:
        return (n-2) * f(n - 2)

print((f(1024) + 2 * (f(1024) - f(1022))) // f(1020))