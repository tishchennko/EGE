from itertools import *

def f(x, y, z, w):
    return (w == (z <= x)) and y

for a1, a2, a3, a4, a5 in product([1, 0], repeat = 5):
    table = [(a1, 0, a2, 0), (1, a3, 1, 1), (a4, a5, 0, 0)]
    if len(set(table)) == len(table):
        for p in permutations('xyzw'):
            u = [f(**dict(zip(p, t))) for t in table] == [1, 0, 1]
            if u:
                print(*p)