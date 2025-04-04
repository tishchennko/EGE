from itertools import *

graph = 'BE EG BA AG BF FD AD GH HC AC DC'.split()
mat = '36 478 178 258 46 158 23 2346'.split()

print(*range(1, 9))

for i in permutations('ABEGHCDF'):
    if all(str(i.index(x) + 1) in mat[i.index(y)] for x,y in graph):
        print(*i)
#57