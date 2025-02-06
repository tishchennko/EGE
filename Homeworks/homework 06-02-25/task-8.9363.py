```
from itertools import *

alf = sorted(set('ХОЧУНАБЮДЖЕТ'))
alf_2 = 'ОУАЮЕ'
cnt = 0
for val in permutations(alf,  12):
    val = ''.join(val)
    for i in alf_2:
        val = val.replace(i, 'x')
        if 'xxxxx' not in val:
            cnt += 1

print(cnt)
```
