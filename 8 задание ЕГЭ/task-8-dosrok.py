from itertools import *

alf = 'ДГИАШЭ'
cnt = 0
for val in product(alf, repeat = 5):
    val = ''.join(val)
    if val[0] not in 'ИАЭ' and val[-1] not in 'ДГШ':
        cnt += 1
print(cnt)