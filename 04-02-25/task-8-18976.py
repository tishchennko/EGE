
from itertools import *
from string import *

alph = digits + ascii_lowercase
chet = alph[20:][::2]
nechet = alph[20:][1::2]

count = 0
for val in product(alph[:20], repeat = 5):
    val = ''.join(val)
    if val[0] != '0' and int(val[0], 20) + int(val[-1], 20) == 26:
        for i in chet:
            val = val.replace(i, 'x')
        for j in nechet:
            val = val.replace(j, 'y')
        if 'xx' not in val and 'yy' not in val:
            count += 1

print(count)
