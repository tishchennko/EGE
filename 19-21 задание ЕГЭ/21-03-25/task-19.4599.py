def f(x1, x2, c, win):
    if x1 + x2 >= 259:
        return c in win
    if c > max(win):
        return 0
    moves = [f(x1 + 1, x2, c + 1, win), f(x1, x2  + 1, c + 1, win), f(x1 * 2, x2, c + 1, win), f(x1, x2 * 2, c + 1, win)]
    if c % 2 != max(win) % 2:
        return any(moves)
    else:
        return all(moves)

for s in range(1, 241 + 1):
    #if f(17, s, 0, [1]) == 0 and f(17, s, 0, [2]) == 1:
        #print('19', s)
        #break
    if f(17, s, 0, [1]) == 0 and f(17, s, 0, [3]) == 1:
        print('20', s)
        #112 120
    if f(17, s, 0, [2, 4]) == 1 and f(17, s, 0, [2]) == 0:
        print('21', s)
        #111

