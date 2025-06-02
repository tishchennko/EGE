from itertools import *

mat = '68 47 45 237 368 15 248 157'.split()
graph = 'CD CE CA DH HE EG GF BF AF AB'.split()

print(*range(1, 9))
for i in permutations('ABCDEFGH'):
    if all(str(i.index(x) + 1) in mat[i.index(y)] for x,y in graph):
        print(*i)