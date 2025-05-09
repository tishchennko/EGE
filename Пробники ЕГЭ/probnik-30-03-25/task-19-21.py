from math import ceil
def f(x1, x2, c, win):
    if c > max(win):
        return 0
    if x1 + x2 >= 127:
        return c in win
    moves = [f(x1 + 2, x2, c + 1, win), f(x1, x2 + 2, c + 1, win), f(x1 * 3, x2, c + 1, win), f(x1, x2 * 3, c + 1, win)]
    if c % 2 != max(win) % 2:
        return any(moves)
    else:
        return all(moves)

for s in range(1, 122 + 1):
    #if f(2, s, 0, [1]) == 0 and f(2, s, 0, [2]) == 1:
        #print(s)
    if f(2, s, 0, [1]) == 0 and f(2, s, 0, [3]) == 1:
        print('20',s)
    #if f(2, s, 0, [2, 4]) == 1 and f(2, s, 0, [2]) == 0:
        #print(s)