from itertools import permutations


graph = 'АБ АЖ ЖБ БВ БЕ ЕД БД ВД ВГ ДГ'.split()
mat = '346 45 16 12567 24 1347 46'.split()

print(*range(1, 8))

for i in permutations('АБВГДЖЕ'):
    if all(str(i.index(x) + 1) in mat[i.index(y)] for x, y in graph):
        print(*i)