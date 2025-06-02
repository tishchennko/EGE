from itertools import *

graph = 'АБ БД ВД АВ АГ ВГ ЖГ ЖД ГЗ ЕЗ ДЕ ГЕ ВЖ'.split()
mat = '457 37 267 1678 16 3458 12348 467'.split()

print(*range(1, 9))

for i in permutations('АБВГДЖЗЕ'):
    if all(str(i.index(x) + 1) in mat[i.index(y)] for x,y in graph):
        print(*i)