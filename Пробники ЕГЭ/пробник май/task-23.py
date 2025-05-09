def f(x, end):
    if x < end:
        return 0
    if x == end:
        return 1
    if x == 15:
        return 0
    return f(x - 2, end) + f(x - 3, end) + f(x//3, end)

print(f(48, 25)*f(25, 17)*f(17,4))