from itertools import *

alf = '012345678'
cnt = 0
for val in product(alf, repeat = 7):
    val = ''.join(val)
    if val[-1] != '3' and val[-1] != '4' and val[-1] != '7' and val[0] != '0' and '000' not in val \
        and '111' not in val and '222' not in val and '333' not in val and  '444' not in val and '555' not in val \
             and '666' not in val and '777' not in val and '888' not in val:
        cnt += 1
print(cnt)