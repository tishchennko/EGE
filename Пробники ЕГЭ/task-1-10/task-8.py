from itertools import *

alf = '012345678'
cnt = 0
for val in product(alf, repeat = 9):
    val = ''.join(val)
    if val.count('0') == 0:
        for i in '13579':
            val = val.replace(i, 'x')
        for i in '02468':
            val = val.replace(i, 'y')
        if 'xx' not in val and 'yy' not in val and 'xxx' not in val and 'yyy' not in val:
            cnt += 1
print(cnt)