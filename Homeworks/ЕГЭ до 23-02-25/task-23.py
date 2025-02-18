def f(x, end):
    if x == end:
        return 1
    if x == 36:
        return 0
    if x == 100:
        return 0
    if x < end:
        return 0
    return f(x // 2, end) + f(x // 3, end) + f(x - 3, end)

print(f(163, 45) * f(45, 3))
#690