from itertools import *

graf = 'АБ АД БД АГ ГД ДЕ ВГ ВЖ ЖЗ ВЗ ЗЕ'.split()
mat = '245 15 478 135 1246 58 38 367 '.split()

print(*range(1, 9))
for i in permutations('АБВГДЕЖЗ'):
    if all(str(i.index(x) + 1) in mat[i.index(y)] for x,y in graf):
        print(*i)