from itertools import *

alf = '0123456'
chet = '0246'
nechet = '135'

cnt = 0
for val in product(alf, repeat = 5):
    val = ''.join(val)
    if val[0] != '0' and val.count('6') == 1 and (sum(int(i) for i  in val if i in chet) < sum(int(i) for i  in val if i in nechet)):
        cnt += 1
print(cnt)
