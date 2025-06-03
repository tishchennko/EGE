from itertools import *

alf = sorted('ПОБЕДА')
ans = []
for pos,val in enumerate(product(alf, repeat = 6), 1):
    val = ''.join(val)
    if pos % 2 == 0 and val[0] == 'О':
        if len(set(val)) == len(val):
            ans.append(pos)
print(max(ans))