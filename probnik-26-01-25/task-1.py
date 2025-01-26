from itertools import *

graph = 'FB BD DE CE BC EA GA GC GF'.split()
mat = '47 57 45 136 236 457 126'.split()

print(*range(1, 8))
for i in permutations('ABCDEFG'):
    if all(str(i.index(x) + 1) in mat[i.index(y)] for x, y in graph):
        print(*i)