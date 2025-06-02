from itertools import *

mat = '256 134 267 27 16 135 34'.split()
graph = 'AF AB FB FE BD ED DG EC CG'.split()

print(*range(1, 8))
for i in permutations('ABCDEFG'):
    if all(str(i.index(x) + 1) in mat[i.index(y)] for x,y in graph):
        print(*i)