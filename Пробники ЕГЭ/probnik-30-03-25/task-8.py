from itertools import *

alf = sorted('ЛУНАТИК')
for pos, val in enumerate(product(alf, repeat = 6), 1):
    val = ''.join(val)
    if (val.count('У') + val.count('А') + val.count('И')) == 1 and val[0] == 'Н':
        print(pos)