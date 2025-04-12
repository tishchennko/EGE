def f(x, end, A = 0):
    if x > 17:
        return 0
    if x == end:
        return 1
    if A == 1:
        return f(x * 2, end) + f(x * 3, end)
    return f(x - 1, end, 1) + f(x * 2, end) + f(x * 3, end)
print(f(3, 15))
