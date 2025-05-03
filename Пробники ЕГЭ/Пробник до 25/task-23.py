def f(x ,end):
    if x > end:
        return 0
    if x == end:
        return 1
    if x == 8:
        return 0
    return f(x + 3, end) + f(x * 2, end)

print(f(2, 32)*f(32, 76))