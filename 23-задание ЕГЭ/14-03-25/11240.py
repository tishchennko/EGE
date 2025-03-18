def f(cur, end, B=0):
    if cur == end: return 1
    if cur > end: return 0
    if B == 1:
        return f(cur + 2, end) + f(cur * 3, end)
    return f(cur + 2, end) + f(cur ** 2, end, 1) + f(cur * 3, end)

print(f(2, 64))
