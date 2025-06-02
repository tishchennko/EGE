
from itertools import *

alf = '0123456789'
alf2 = '02468'
alf3 = '13579'
for pos,val in enumerate(range(10000, 100000), 1):
    val = str(val)
    for i in alf2:
        val = val.replace(i, '*')
    for i in alf3:
        val = val.replace(i, '!')
    if '**' not in val and '!!' not in val and pos % 15 == 0:
        print(pos)
