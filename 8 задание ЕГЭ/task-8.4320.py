from itertools import *

alf = '01234567'
cnt = 0
for val in product(alf, repeat = 6):
    val = ''.join(val)
    if val[0] != '0' and len(set(val)) == len(val) and int(val, 8) % 5 == 0:
        for i in alf:
            val = val.replace('2', 'x').replace('4', 'x').replace('6', 'x').replace('0', 'x').replace('1', 'y').replace('3', 'y').replace('5', 'y').replace('7', 'y')
        if 'xx' not in val and 'yy' not in val:
            cnt += 1
print(cnt)
