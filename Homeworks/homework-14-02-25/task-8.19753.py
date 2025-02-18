from itertools import *

alf = '0123456789'
chet = '02468'
cnt = 0
for val in product(alf, repeat = 6):
    val = ''.join(val)
    if val[0] != '0' and len(set(val)) == len(val) and int(val) % 4 == 0:
        for i in chet:
            val = val.replace(i, 'x')
        if 'xx' not in val:
            cnt += 1
print(cnt)
