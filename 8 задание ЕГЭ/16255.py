from itertools import *

alf = '012345678'
cnt = 0
for val in product(alf, repeat = 7):
    val = ''.join(val)
    if val[0] != '0' and '1357' not in val[0] and '124578' in val[6] and val.count('6') >= 1:
        cnt += 1
print(cnt)