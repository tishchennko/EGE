def f(x, c, win):
    if x > 40:
        return c in win
    if c > max(win):
        return 0
    moves = [f(x + 3, c + 1, win), f(x + 6, c + 1, win), f(x * 2, c + 1, win)]
    if c % 2 != max(win) % 2:
        return any(moves)
    else:
        return all(moves)

for s in range(2, 36 + 1):
    #if f(s, 0, [1]) == 0 and f(s, 0, [2]) == 1:
        #print(s)
    #if f(s, 0, [1]) == 0 and f(s, 0, [3]) == 1:
        #print('20',s)
    if f(s, 0, [2, 4]) == 1 and f(s, 0, [2]) == 0:
        print('21', s)


























