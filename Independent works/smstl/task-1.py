from itertools import *

graph = 'CH FC CG GD DH HB BA BE AE FA'.split()
mat = '248 157 456 136 23 34 28 17'.split()

print(*range(1, 9))

for i in permutations('ABCDEFGH'):
    if all(str(i.index(x) + 1) in mat[i.index(y)] for x, y in graph):
        print(*i)