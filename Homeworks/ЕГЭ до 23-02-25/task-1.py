from itertools import *

graph = 'АБ БГ АВ ВГ ГЕ ГД ЕЗ ЗЖ ГЗ ЖД ГЖ'.split()
mat = '235 13 12345678 36 13 347 368 37'.split()

print(*range(1, 9))
for i in permutations('АБВГДЖЗЕ'):
    if all(str(i.index(x) + 1) in mat[i.index(y)] for x,y in graph):
        print(*i)
#11 + 17 + 16 = 44