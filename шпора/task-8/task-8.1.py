from itertools import *

alf= sorted('ФОКУС')

for pos,val in enumerate(product(alf, repeat = 5), 1):
    val = ''.join(val)
    if val.count('Ф') == 0 and val.count('У') == 2:
        print(pos)