def f(x, end):
    if x < end:
        return 0
    if x == end:
        return 1
    return f(x - 2, end) + f(x//2, end)
print(f(38, 10)* f(10, 2))