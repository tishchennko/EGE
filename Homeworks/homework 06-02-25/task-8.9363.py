from itertools import *

alf = 'ХОЧУНАБЮДЖЕТ'
alf_2 = 'ОУАЮЕ'
cnt = set()
for val in permutations(alf):
    val = ''.join(val)
    for i in alf_2:
        val = val.replace(i, 'x')
    if 'xxxxx' not in val:
        cnt.add(val)

print(len(cnt))

