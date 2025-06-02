from itertools import *

mat = '26 147 456 237 37 13 245'.split()
graph = 'BD BG DE GF FE GC FC CA AE'.split()

print(*range(1, 8))
for i in permutations('ABCDEFG'):
    if all(str(i.index(x) + 1) in mat[i.index(y)] for x, y in graph):
        print(*i)