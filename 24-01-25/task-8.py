from itertools import *

alp = sorted('МИНУС')
for pos, val in enumerate(product(alp, repeat = 4), 1):
    val = ''.join(val)
    if val.count('М') + val.count('Н') + val.count('С') >= val.count('И') + val.count('У'):
        print(pos)
