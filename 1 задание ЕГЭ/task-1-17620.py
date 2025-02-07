from itertools import permutations

graph = 'AF AB FB BD FE ED DG EC CG'.split()
matrix = '256 134 267 27 16 135 34'.split()

print(*range(1,8))
for i in permutations('ABCDEFG'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)