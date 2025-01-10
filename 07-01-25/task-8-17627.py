from string import digits, ascii_uppercase
from itertools import product

alph = digits + ascii_uppercase

cnt = 0
for val in product(alph[:15], repeat = 5):
    val = ''.join(val)
        cnt += 1
print(cnt)

