from itertools import *

mat = '457 567 45 136 123 247 126'.split()
graph = 'AB FA EF FD DA EC DC EG GB CB'.split()

print(*range(1, 8))
for i in permutations('ABCDEFG'):
    if all(str(i.index(x) + 1) in mat[i.index(y)] for x,y in graph):
        print(*i)