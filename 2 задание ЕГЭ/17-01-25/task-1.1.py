
from itertools import*

graph = 'AB BC CD BD AD CF FD GF GE ED AE'.split()
mat = '23567 145 146 23 127 137 156'.split()

print(*range(1, 8))
for i in permutations('ABCDEFG'):
    if all(str(i.index(x) + 1) in mat[i.index(y)] for x, y in graph):
        print(*i)

#65
