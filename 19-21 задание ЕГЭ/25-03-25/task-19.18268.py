from math import ceil
def f(x1, x2, c, win):
    if x1 + x2 <= 72:
        return c in win
    if c > max(win):
        return 0
    moves = [f(x1 - 3, x2, c + 1, win), f(x1, x2 - 3, c + 1, win)]
    if x1 % 2 != 0 and x2 % 2 != 0:
        moves.append([f(ceil(x1 // 2), x2,  c + 1, win), f(x1, ceil(x2 // 2), c + 1, win)])
    else:
        moves.append([f(x1 // 2, x2, c + 1, win), f(x1, x2 // 2, c + 1, win)])
    if c % 2 != max(win) % 2:
        return any(moves)
    else:
        return any(moves)

for s in range(22, 100+ 1):
    if f(50, s, 0, [1]) == 0 and f(50, s, 0, [2]) == 1:
        print(s)