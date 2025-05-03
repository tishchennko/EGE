from itertools import *

def f(x, y, w ,z):
    return (z == (not x)) <= ((w <= (not y)) and (y <= x))

for a1, a2, a3, a4, a5 in product([1, 0], repeat = 5):
    table = [(1, 1, 1, 0),
             (a1, a2, 0, 0),
             (a3, 0, a4, a5)]
    for p in permutations('xywz'):
        u = [f(**dict(zip(p, t))) for t in table] == [1, 0, 0]
        if u:
            print(*p)