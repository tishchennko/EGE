```
from itertools import*

count = 0
for val in product('012345678', repeat = 7):
    val = ''.join(val)
    if val[0] != '2' and val[0] != '4' and val[0] != '6' and val[6] != '3' and val[0] != '0' and '111' not in val and \
            '555' not in val and '777' not in val and '888' not in val:
        count += 1
print(count)
```