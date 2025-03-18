from itertools import *

alf = '0123456789ab'
alf_2 = '9ab'

cnt = 0
for val in product(alf, repeat = 5):
    val = ''.join(val)
    if val.count('7') == 1 and val[0] != '0':
        for i in alf_2:
            val = val.replace(i, 'x')
        if val.count('x') <= 3:
            cnt += 1

print(cnt)
#67476
