from itertools import *

alf = '0123456789'
cnt = 0
for val in product(alf, repeat = 5):
    val = ''.join(val)
    if val[0] != '0' and val[4] != '3' and val[4] != '4' and val[4] != '7':
        if '111' not in val and '222' not in val and'000' not in val and '333' not in val and '444' not in val\
                and '555' not in val and '666' not in val and '777' not in val and '888' not in val and '999' not in val:
            cnt += 1
print(cnt)