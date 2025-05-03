from itertools import *

grap = 'АБ АГ АВ ВБ БГ ВД ГД ГЖ ДЕ ЖЕ ДЗ ЕЗ ЖЗ'.split()
mat = '256 1458 478 237 126 158 348 2367'.split()

print(*range(1, 9))

for i in permutations('АБВГДЖЗЕ'):
    if all(str(i.index(x) + 1) in mat[i.index(y)] for x,y in grap):
        print(*i)