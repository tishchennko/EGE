from itertools import *

def f(x,y,z,w):
    return (y <= x) and (not z) and w

for a1, a2, a3, a4, a5, a6 in product([1, 0], repeat = 6):
    table = [(1, 0, a1, a2),
             (1, 1, a3, a4), (a5, 1, 1, a6)]
    if len(set(table)) == len(table):
        for p in permutations('xyzw'):
            u = [f(**dict(zip(p, t))) for t in table] == [1, 1, 1]
            if u:
                print(*p)