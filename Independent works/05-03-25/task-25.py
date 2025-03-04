from fnmatch import *

for i in range(1035954 - 1035954 % 6437, 10 ** 10, 6437):
    if fnmatch(str(i), '1?3*5*954'):
        if i:
            print(i, i // 6437)