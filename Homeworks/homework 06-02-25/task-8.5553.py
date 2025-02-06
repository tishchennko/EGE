from itertools import *

alf = 'СОТОЧКА'
cnt = set()
for p in permutations(alf, ):
    p = ''.join(p)
    if 'ОО' in p or 'ОА' in p or 'АО' in p:
        cnt.add(p)

print(cnt)