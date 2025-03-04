
def f(x, c, win):
    if x <= 25:
        return c in win
    if c > max(win):
        return 0
    moves = [(x - 2, c + 1, win), (x - 3, c + 1, win), (x // 2, c + 1, win)]
    if c % 2 != max(win) % 2:
        return any(moves)
    else:
        return all(moves)

for s in range(26, 1000):
    if f(s, 0,[1]) == 0 and f(s, 0, [2]) == 1:
        print(s)

