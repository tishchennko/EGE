def f(x, end):
    if x > end:
        return 0
    if x == end:
        return 1
    if x == 21:
        return 0
    return f(x + 2, end) + f(x + 3, end) + f(x * 2, end)
print(f(7, 14)*f(14, 32))