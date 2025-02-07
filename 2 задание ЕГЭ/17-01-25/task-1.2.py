
from itertools import*

def f(x,y, w, z):
    return (w == x) and (y <= z)


for a1, a2 ,a3, a4, a5, a6, a7, a8, a9 in product([1, 0], repeat = 9):
    table = [(0, a1, a2, a3), (a4, a5, 0, a6), (0, a7, a8, 0), (0, a9, 0, 0)]
    if len(set(table)) == len(table):
        for p in permutations('abcd'):
            u = [f(**(dict(zip(p, t)))) for t in table] == [0, 0, 0, 0]
            if u:
                print(*p)