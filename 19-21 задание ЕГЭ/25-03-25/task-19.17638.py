
def f(x1, x2, c, win):
    if x1 + x2 >= 44:
        return c in win
    if c > max(win):
        return 0
    moves = [f(x1 + x2, x2, c + 1, win), f(x1,x2 + x1, c + 1, win)]
    if c % 2 != max(win) % 2:
        return any(moves)
    else:
        return all(moves)

ans = []
for s in range(1, 100):
    for s_2 in range(1, 100):
        if f(s_2, s, 0, [2]):
            ans.append((abs(s - s_2), s, s_2))
    print('20', s)

def f(x1, x2, c, win):
    if x1 + x2 >= 44:
        return c in win
    if c > max(win):
        return 0
    moves = [f(x1 + x2, x2, c + 1, win), f(x1,x2 + x1, c + 1, win)]
    if c % 2 != max(win) % 2:
        return any(moves)
    else:
        return all(moves)

for s in range(1, 100):
    if f(11, s, 0, [2]) == 1:
        print('20', s)

    #if f(6, s, 0, [1]) == 0 and f(6, s, 0, [3]) == 1:
        #print('20',s)
    #if f(6, s, 0, [2]) == 0 and f(6, s, 0, [2, 4]) == 1:
        #print('21', s)
