
def f(x1, x2, c, win):
    if x1 + x2 <= 100:
        return c in win
    if c > max(win):
        return 0
    moves = [f(x1 - 3, x2 - 3, c + 1, win), f(x1 // 2, x2, c + 1, win), f(x1, x2 // 2, c + 1, win)]
    if c % 2 != max(win) % 2:
        return any(moves)
    else:
        return any(moves)

for s in range(53, 1000):
    if f(48, s, 0, [1]) == 0 and f(48, s, 0, [2]) == 1:
        print(s)


