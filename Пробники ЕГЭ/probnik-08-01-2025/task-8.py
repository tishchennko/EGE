from string import digits, ascii_uppercase
from itertools import product

alph = digits + ascii_uppercase

cnt  = 0
for val in product(alph[:16], repeat = 6):
    val = ''.join(val)
    if  'A' not in val[0]  and val[0] != 'E' and val[5] != 'A' and val[5] != 'E':
        cnt += 1
print(cnt)