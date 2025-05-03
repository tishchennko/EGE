from itertools import *

alf = 'ПАРИЖАНКА'
cnt = 0
for val in set(permutations(alf)):
    val = ''.join(val)
    val = val.replace('И', 'А')
    if val.count('АА') == 1 and 'ААА' not in val:
        cnt += 1


print(cnt)