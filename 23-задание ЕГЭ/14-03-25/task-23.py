def f(x, end, C = 0):
    if x > end:
        return 0
    if x == end:
        return 1
    return f(x + 2, end) + f(x+5, end) + f(x ** 2, end)

print(f(4, 36))