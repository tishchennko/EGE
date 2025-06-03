from itertools import *
from string import *

alf = digits+ ascii_lowercase
cnt = 0
for val in product(alf[:15], repeat = 5):
    val = ''.join(val)
    if val.count('8') == 1 and val[0] != '0':
        for i in alf[10:15]:
            val = val.replace(i, 'x')
        if val.count('x') >= 2:
            cnt += 1
print(cnt)