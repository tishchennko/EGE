def f(x, end):
    if x == end:
        return 1
    if x > end:
        return 0
    return f(x + 2, end) + f(x + max(int(i) for i in str(x)), end)

print(f(32,55) * f(55, 76))