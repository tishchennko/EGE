from itertools import *

grap = 'AB AC AE CE EG GF DF BF BD CD'.split()
mat = '235 146 145 236 137 247 56'.split()

print(*range(1, 8))
for i in permutations('ABCDEFG'):
    if all(str(i.index(x) + 1) in mat[i.index(y)] for x,y in grap):
        print(*i)

