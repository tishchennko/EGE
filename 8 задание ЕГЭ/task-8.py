from itertools import *

alf = ''.join(sorted('АРГУМЕНТ'))

for pos, val in enumerate(product(alf, repeat = 4), 1):
    val = ''.join(val)
    if val in alf:
        print(pos)
