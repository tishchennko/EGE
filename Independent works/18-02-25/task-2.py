from itertools import *

alf = sorted('ШКОЛА')

for pos, val in enumerate(product(alf, repeat = 5), 1):
    val = ''.join(val)
    if 'ШАЛАШ' in val:
        print(pos)
