from itertools import *

def f(x, y, z, w):
    return (not(x <= y)) or (z == w) or z

for a1, a2, a3, a4,a5 ,a6, a7 in product([1, 0], repeat = 7):
    table = [(0, 0, a1, a2), (a3, a4, 1, a5), (a6, 1, 0, a7)]
    if len(set(table)) == len(table):
        for p in permutations('xyzw'):
            u = [f(**dict(zip(p, t))) for t in table] == [0, 0, 0]
            if u:
                print(*p)