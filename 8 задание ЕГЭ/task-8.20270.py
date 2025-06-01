from itertools import *

alf = '0123456'
alf2 = '0246'
alf3 = '135'

cnt = 0
for val in product(alf, repeat = 5):
    val = ''.join(val)
    if val[0] != '0':
        for i in alf2:
            val = val.replace(i, '*')
        if val.count('**') >= 2:
            if '**' in val and '***' not in val:
                cnt += 1
print(cnt)