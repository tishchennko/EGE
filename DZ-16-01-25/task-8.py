
from itertools import*


cnt = 0
for val in product('0123456789', repeat = 5):
    if val.count('6') == 2 and val[0] != 0:
        x = ''.join(val)
        x = x.replace('0', '8', 1).replace('2', '8', 1).replace('4', '8', 1) \
            .replace('6', '8', 1)
        if x.count('86') == 0 and x.count('68') ==0:
            cnt += 1

print(cnt)
