from itertools import*

def f(x, y, z, w):
    return x and ((z <= y) == w)

for a1, a2, a3, a4, a5 in product([1, 0], repeat = 5):
    table = [(1, a1, 1, a2), (0, a3, 1, 1), (1, 1, 1, a4), (1, 1, 1, a5)]
    if len(set(table)) == len(table):
        for p in permutations('xyzw'):
            u = [f(**dict(zip(p, t))) for t in table] == [1, 1, 1, 1]
            if u:
                print(*p)
#wyxz