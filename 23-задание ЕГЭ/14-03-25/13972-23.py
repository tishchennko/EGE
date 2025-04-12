def f(cur, end, A = 0, C = 0):
    if cur == end: return 1
    if cur > end: return 0
    if cur == 7:
        return f(cur + 2, end) + f(cur * 2, end)
    return f(cur + 2, end) + f(cur + 5, end) + f(cur * 2, end)

print(f(7, 23)*f(23, 35))