def f(cur, end, A = 0, C = 0):
    if cur == end: return 1
    if cur > end: return 0
    if A == 0 or C == 0:
        return f(cur + 2, end, 1 ,0) + f(cur + 5, end) + f(cur * 2, end,  0, 1)
    return f(cur + 2, end) + f(cur + 5, end) + f(cur * 2, end)

print(f(7, 23)*f(23, 35))