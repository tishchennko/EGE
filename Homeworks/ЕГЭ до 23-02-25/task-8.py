from itertools import *

alf = sorted('КАЛЕЙДОСКОП')[::-1]
ans = []
for pos, val in enumerate(product(alf, repeat = 6), 0):
    val = ''.join(val)
    if val[0] == 'К' and val.count('Й') >= 2 and val.count('С') == 0 and val.count('Е') == 0 \
        and pos % 2 == 0:
        ans.append(pos)
print(min(ans))
#821432