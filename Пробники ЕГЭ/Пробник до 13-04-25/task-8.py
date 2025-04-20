from itertools import *

alph = '01234'

cnt = 0
for val in product(alph, repeat=6):
    val = ''.join(val)
    if int(val, 5) % 2 == 0 and \
        val[0] == '3':
        cnt += 1
print(cnt)