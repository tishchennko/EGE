from string import digits, ascii_uppercase
from itertools import product

alph = digits + ascii_uppercase

cnt = 0
for val in product(alph[:15], repeat = 5):
    val = ''.join(val)
    if val.count('8') == 1 and val.count('A') + val.count('B') + val.count('C')  \
             + val.count('D') +  val.count('E') + val.count('F') >= 2:
        cnt += 1
print(cnt)

