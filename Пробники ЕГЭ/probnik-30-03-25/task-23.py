def f(x, end):
    if x > end:
        return 0
    if x == end:
        return 1
    if x == 8:
        return 0
    return f(x + 1, end) + f(x * 2, end) + f(x * 5, end)

print(f(2, 27)*f(27, 54))