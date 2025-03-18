def f(x, end, A = 0, B = 0, C = 0):
    if x > end: return 0
    if x == end: return 1
    if A == 0 or B == 0 or C == 0:
        return f(x + 1, end,1 ,0, 1) + f(x + 7, end, 0, 1, 0) + f(x * 4, end)