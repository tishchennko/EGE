
from string import *
from itertools import*

alph = digits + ascii_lowercase
chet = '02468ac'
nechet = '13579b'

count = 0
for val in product(alph[0:12], repeat = 7):
    val=''.join(val)
    if val[0] != '0' and val.count('b') == 2:
        for r in chet:
            val = val.replace(r, 'x')
        for i in nechet:
            val = val.replace(i, 'y')
        if 'xx' not in val and 'yy' not in val:
            count += 1

print(count)


