from itertools import *

alf = '012345678'
cnt = 0
for val in product(alf, repeat = 7):
    val = ''.join(val)
    if val[0] != '0' and val[0] not in '1357' and val[6] in '124578' and val.count('6') >= 1:
        cnt += 1
print(cnt)